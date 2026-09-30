#!/usr/bin/env python3
"""
Live-model evaluation harness for triz-universal.

Replaces the substring rubric for *real* model outputs. The old
`run_evals.py` rubric stays only as an offline self-test of the reference
corpus; it is not evidence that the skill improves answers.

Workflow
--------
1. Collect raw model outputs (with and without the skill) into one JSON file:
       [{"model": "...", "case_id": "...", "arm": "baseline"|"skill",
         "run": 1, "output": "..."}, ...]
2. `prepare`  validates the file (strictly: no silent fallbacks), runs the
   deterministic pre-checks and writes blinded judge inputs + a key file.
3. Give judge_items.jsonl to one or more judges (LLM and/or human). Each
   judge returns one JSON object per line:
       {"item_id": "...", "verdicts": [{"criterion_id": "m1",
         "satisfied": true, "evidence": "short quote or reason"}, ...]}
4. `score` combines verdicts, applies deterministic hard-fails, and prints
   pass rates with Wilson intervals, a paired sign test (baseline vs skill),
   skill regressions and judge agreement (Cohen's kappa).

Usage
-----
    python evals/live_eval.py prepare --responses live.json --out evals/out
    python evals/live_eval.py score   --responses live.json --key evals/out/judge_key.json \
        --verdicts judgeA.jsonl [--verdicts judgeB.jsonl] --out evals/out/report.md
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CASES = ROOT / "evals" / "cases.json"
DEFAULT_CRITERIA = ROOT / "evals" / "judge_criteria.json"
DEFAULT_PROMPT = ROOT / "evals" / "judge_prompt.md"
ARMS = ("baseline", "skill")
KINDS = ("must", "avoid")


class EvalInputError(ValueError):
    """Raised on any malformed or incomplete evaluation input."""


# ----------------------------------------------------------------- loading

def _load_json(path: Path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise EvalInputError(f"file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise EvalInputError(f"invalid JSON in {path}: {exc}") from exc


def load_cases(path: Path = DEFAULT_CASES) -> dict[str, dict]:
    raw = _load_json(path)
    if not isinstance(raw, list):
        raise EvalInputError("cases file must be a JSON list")
    cases = {}
    for item in raw:
        cid = item.get("id")
        if not cid or "prompt" not in item:
            raise EvalInputError(f"case without id/prompt: {item!r:.80}")
        if cid in cases:
            raise EvalInputError(f"duplicate case id: {cid}")
        cases[cid] = item
    return cases


def load_criteria(path: Path = DEFAULT_CRITERIA, case_ids: set[str] | None = None) -> dict[str, dict]:
    raw = _load_json(path)
    cases = raw.get("cases")
    if not isinstance(cases, dict) or not cases:
        raise EvalInputError("criteria file has no 'cases' object")
    for cid, entry in cases.items():
        crit = entry.get("criteria")
        if not crit:
            raise EvalInputError(f"{cid}: no criteria")
        seen = set()
        for c in crit:
            for field in ("id", "kind", "critical", "text"):
                if field not in c:
                    raise EvalInputError(f"{cid}: criterion missing '{field}'")
            if c["kind"] not in KINDS:
                raise EvalInputError(f"{cid}/{c['id']}: kind must be one of {KINDS}")
            if c["id"] in seen:
                raise EvalInputError(f"{cid}: duplicate criterion id {c['id']}")
            seen.add(c["id"])
        if not any(c["critical"] for c in crit):
            raise EvalInputError(f"{cid}: needs at least one critical criterion")
        if not any(c["kind"] == "avoid" for c in crit):
            raise EvalInputError(f"{cid}: needs at least one 'avoid' criterion")
        for pat in entry.get("hard_fail_patterns", []):
            re.compile(pat)
        for pat in entry.get("anchors", {}).values():
            re.compile(pat)
    if case_ids is not None:
        missing = case_ids - set(cases)
        extra = set(cases) - case_ids
        if missing:
            raise EvalInputError(f"cases without criteria: {sorted(missing)}")
        if extra:
            raise EvalInputError(f"criteria for unknown cases: {sorted(extra)}")
    return cases


def load_responses(path: Path, case_ids: set[str], allow_partial: bool = False) -> list[dict]:
    """Strictly load model outputs. Never falls back to reference outputs."""
    raw = _load_json(path)
    if isinstance(raw, dict) and "responses" in raw:
        raw = raw["responses"]
    items: list[dict] = []
    if isinstance(raw, dict):  # legacy {case_id: {baseline_output, skill_output}}
        for cid, entry in raw.items():
            for arm, key in (("baseline", "baseline_output"), ("skill", "skill_output")):
                if key in entry:
                    items.append({"case_id": cid, "arm": arm, "run": 1,
                                  "model": entry.get("model", "unknown"), "output": entry[key]})
    elif isinstance(raw, list):
        items = [dict(x) for x in raw]
    else:
        raise EvalInputError("responses must be a list (or legacy dict)")

    seen = set()
    for it in items:
        for field in ("case_id", "arm", "output"):
            if field not in it:
                raise EvalInputError(f"response missing '{field}': {str(it)[:80]}")
        it.setdefault("run", 1)
        it.setdefault("model", "unknown")
        if it["case_id"] not in case_ids:
            raise EvalInputError(f"unknown case_id: {it['case_id']}")
        if it["arm"] not in ARMS:
            raise EvalInputError(f"arm must be one of {ARMS}, got {it['arm']!r}")
        if not isinstance(it["output"], str) or not it["output"].strip():
            raise EvalInputError(f"empty output for {it['case_id']}/{it['arm']}/run {it['run']}")
        k = (it["model"], it["case_id"], it["arm"], it["run"])
        if k in seen:
            raise EvalInputError(f"duplicate response: {k}")
        seen.add(k)
    if not items:
        raise EvalInputError("no responses found")

    groups = defaultdict(set)
    for it in items:
        groups[(it["model"], it["run"])].add((it["case_id"], it["arm"]))
    expected = {(c, a) for c in case_ids for a in ARMS}
    for g, have in sorted(groups.items(), key=str):
        missing = expected - have
        if missing and not allow_partial:
            raise EvalInputError(
                f"model={g[0]} run={g[1]} is missing {len(missing)} of {len(expected)} "
                f"(case, arm) pairs, e.g. {sorted(missing)[:3]}; use --allow-partial to score partial runs")
    return items


# ---------------------------------------------------------- deterministic

def deterministic_checks(entry: dict, text: str) -> dict:
    """Cheap, paraphrase-tolerant checks. Only `hard_fail` affects the score."""
    hard_hits = [p for p in entry.get("hard_fail_patterns", []) if re.search(p, text, re.I)]
    anchors = entry.get("anchors", {})
    anchor_missing = [name for name, pat in anchors.items() if not re.search(pat, text, re.I)]
    return {"hard_fail": bool(hard_hits), "hard_fail_hits": hard_hits, "anchor_missing": anchor_missing}


# ------------------------------------------------------------ judge inputs

def item_id(salt: str, model: str, case_id: str, arm: str, run: int) -> str:
    return hashlib.sha256(f"{salt}|{model}|{case_id}|{arm}|{run}".encode()).hexdigest()[:12]


def render_criteria(criteria: list[dict]) -> str:
    lines = []
    for c in criteria:
        tag = "CRITICAL" if c["critical"] else "minor"
        lines.append(f"- [{c['id']}] ({tag}) {c['text']}")
    return "\n".join(lines)


def build_judge_prompt(template: str, task: str, criteria: list[dict], response: str, iid: str = "") -> str:
    return (template.replace("{{ITEM_ID}}", iid)
            .replace("{{TASK}}", task)
            .replace("{{CRITERIA}}", render_criteria(criteria))
            .replace("{{RESPONSE}}", response))


def sha256_file(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def prepare(cases_path, criteria_path, responses_path, out_dir, prompt_path=DEFAULT_PROMPT,
            allow_partial=False, seed=None) -> dict:
    cases = load_cases(cases_path)
    criteria = load_criteria(criteria_path, set(cases))
    responses = load_responses(responses_path, set(cases), allow_partial)
    template = Path(prompt_path).read_text(encoding="utf-8")
    salt = f"{random.Random(seed).getrandbits(64):016x}" if seed is not None else f"{random.SystemRandom().getrandbits(64):016x}"

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    key, det, judge_lines = {}, {}, []
    for r in responses:
        iid = item_id(salt, r["model"], r["case_id"], r["arm"], r["run"])
        entry = criteria[r["case_id"]]
        key[iid] = {"model": r["model"], "case_id": r["case_id"], "arm": r["arm"], "run": r["run"]}
        det[iid] = deterministic_checks(entry, r["output"])
        judge_lines.append({
            "item_id": iid,
            "case_id": r["case_id"],
            "criterion_ids": [c["id"] for c in entry["criteria"]],
            "judge_prompt": build_judge_prompt(template, cases[r["case_id"]]["prompt"], entry["criteria"], r["output"], iid),
        })
    random.Random(seed).shuffle(judge_lines)  # do not leak arm/model through ordering
    (out / "judge_items.jsonl").write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in judge_lines) + "\n", encoding="utf-8")
    (out / "judge_key.json").write_text(json.dumps({
        "responses_sha256": sha256_file(responses_path),
        "criteria_sha256": sha256_file(criteria_path),
        "items": key, "deterministic": det,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"items": len(judge_lines), "hard_fails": sum(d["hard_fail"] for d in det.values()), "out": str(out)}


# ----------------------------------------------------------------- verdicts

_QUOTE = re.compile(r'["«“]([^"»”]{8,})["»”]')


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def load_verdicts(path: Path, key_items: dict, criteria: dict, responses_by_id: dict,
                  allow_partial: bool = False) -> tuple[dict, list[str]]:
    """Return ({item_id: {criterion_id: bool}}, warnings)."""
    text = Path(path).read_text(encoding="utf-8").strip()
    if not text:
        raise EvalInputError(f"empty verdicts file: {path}")
    if text.startswith("["):
        rows = json.loads(text)
    else:
        rows = [json.loads(line) for line in text.splitlines() if line.strip()]
    result: dict[str, dict[str, bool]] = {}
    warnings: list[str] = []
    for row in rows:
        iid = row.get("item_id")
        if iid not in key_items:
            raise EvalInputError(f"{path}: unknown item_id {iid}")
        if iid in result:
            raise EvalInputError(f"{path}: duplicate item_id {iid}")
        need = [c["id"] for c in criteria[key_items[iid]["case_id"]]["criteria"]]
        got = {}
        for v in row.get("verdicts", []):
            cid = v.get("criterion_id")
            if cid in got:
                raise EvalInputError(f"{path}: {iid} duplicate criterion {cid}")
            if not isinstance(v.get("satisfied"), bool):
                raise EvalInputError(f"{path}: {iid}/{cid} 'satisfied' must be true/false")
            ev = v.get("evidence")
            if not isinstance(ev, str) or not ev.strip():
                raise EvalInputError(f"{path}: {iid}/{cid} needs a non-empty 'evidence' string")
            m = _QUOTE.search(ev)
            if m and _norm(m.group(1)) not in _norm(responses_by_id[iid]):
                warnings.append(f"{path.name}: {iid}/{cid} quoted evidence not found in response")
            got[cid] = v["satisfied"]
        if set(got) != set(need):
            raise EvalInputError(f"{path}: {iid} criteria mismatch: missing={sorted(set(need)-set(got))} "
                                 f"extra={sorted(set(got)-set(need))}")
        result[iid] = got
    missing = set(key_items) - set(result)
    if missing and not allow_partial:
        raise EvalInputError(f"{path}: {len(missing)} items have no verdict; use --allow-partial")
    return result, warnings


def combine_judges(per_judge: list[dict]) -> dict[str, dict[str, bool]]:
    """Per criterion: satisfied only if a strict majority of judges say so (ties = not satisfied)."""
    combined: dict[str, dict[str, bool]] = {}
    ids = set().union(*[set(j) for j in per_judge])
    for iid in ids:
        votes = [j[iid] for j in per_judge if iid in j]
        crit_ids = votes[0].keys()
        combined[iid] = {c: sum(v[c] for v in votes) * 2 > len(votes) for c in crit_ids}
    return combined


def cohens_kappa(a: list[bool], b: list[bool]) -> float:
    n = len(a)
    if n == 0:
        return float("nan")
    po = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def judge_agreement(per_judge: list[dict]) -> list[tuple[int, int, float, int]]:
    out = []
    for i in range(len(per_judge)):
        for j in range(i + 1, len(per_judge)):
            common = sorted(set(per_judge[i]) & set(per_judge[j]))
            a = [per_judge[i][k][c] for k in common for c in sorted(per_judge[i][k])]
            b = [per_judge[j][k][c] for k in common for c in sorted(per_judge[j][k])]
            out.append((i + 1, j + 1, cohens_kappa(a, b), len(a)))
    return out


# --------------------------------------------------------------- statistics

def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (max(0.0, (c - h) / d), min(1.0, (c + h) / d))


def sign_test_p(b: int, c: int) -> float:
    """Exact two-sided McNemar/sign test on discordant pairs (b vs c)."""
    n = b + c
    if n == 0:
        return 1.0
    tail = sum(math.comb(n, i) for i in range(0, min(b, c) + 1)) / 2 ** n
    return min(1.0, 2 * tail)


# ------------------------------------------------------------------ scoring

def score_item(criteria: list[dict], sat: dict[str, bool], det: dict) -> dict:
    total = sum(c.get("weight", 1) for c in criteria)
    got = sum(c.get("weight", 1) for c in criteria if sat[c["id"]])
    failed = [c["id"] for c in criteria if not sat[c["id"]]]
    critical_failed = [c["id"] for c in criteria if c["critical"] and not sat[c["id"]]]
    passed = not critical_failed and not det["hard_fail"]
    return {"pass": passed, "score": got / total, "failed": failed,
            "critical_failed": critical_failed, "det_hard_fail": det["hard_fail"]}


def aggregate(results: list[dict], criteria: dict) -> dict:
    by_model = defaultdict(list)
    for r in results:
        by_model[r["model"]].append(r)
    report = {}
    for model, rows in by_model.items():
        arms = {}
        for arm in ARMS:
            sub = [r for r in rows if r["arm"] == arm]
            k = sum(r["pass"] for r in sub)
            lo, hi = wilson(k, len(sub))
            arms[arm] = {"n": len(sub), "pass": k, "rate": k / len(sub) if sub else float("nan"),
                         "ci": (lo, hi), "mean_score": sum(r["score"] for r in sub) / len(sub) if sub else float("nan")}
        idx = {(r["case_id"], r["run"], r["arm"]): r for r in rows}
        b = c = both = neither = 0
        regressions, gains = [], []
        for (cid, run, arm), r in idx.items():
            if arm != "skill" or (cid, run, "baseline") not in idx:
                continue
            base = idx[(cid, run, "baseline")]
            if r["pass"] and not base["pass"]:
                b += 1; gains.append((cid, run))
            elif base["pass"] and not r["pass"]:
                c += 1; regressions.append((cid, run, r["critical_failed"], r["det_hard_fail"]))
            elif r["pass"]:
                both += 1
            else:
                neither += 1
        by_outcome = defaultdict(lambda: {arm: [0, 0] for arm in ARMS})
        for r in rows:
            oc = criteria[r["case_id"]].get("expected_outcome", "?")
            by_outcome[oc][r["arm"]][0] += r["pass"]
            by_outcome[oc][r["arm"]][1] += 1
        missed = {arm: Counter() for arm in ARMS}
        for r in rows:
            for cid in r["critical_failed"]:
                missed[r["arm"]][f"{r['case_id']}/{cid}"] += 1
        report[model] = {"arms": arms, "paired": {"skill_only": b, "baseline_only": c, "both": both,
                                                   "neither": neither, "p": sign_test_p(b, c)},
                         "by_outcome": {k: v for k, v in by_outcome.items()},
                         "regressions": regressions, "gains": gains,
                         "top_missed": {a: m.most_common(8) for a, m in missed.items()}}
    return report


def render_report(report: dict, agreement, warnings, n_judges: int, n_runs: int) -> str:
    L = ["# Live evaluation report", ""]
    L.append(f"Judges: {n_judges} | runs per (model, case, arm): up to {n_runs}")
    if n_judges < 2 or n_runs < 3:
        L.append("")
        L.append("> **Not sufficient for public claims:** use at least 2 judges (one human) and 3 runs per case.")
    for model, rep in sorted(report.items()):
        L += ["", f"## Model: {model}", "", "| Arm | n | passed | rate | 95% CI (Wilson) | mean criterion score |", "|---|--:|--:|--:|---|--:|"]
        for arm in ARMS:
            a = rep["arms"][arm]
            L.append(f"| {arm} | {a['n']} | {a['pass']} | {a['rate']:.0%} | {a['ci'][0]:.0%}-{a['ci'][1]:.0%} | {a['mean_score']:.2f} |")
        p = rep["paired"]
        L += ["", f"Paired (same case and run): skill-only passes {p['skill_only']}, baseline-only passes {p['baseline_only']}, "
                  f"both {p['both']}, neither {p['neither']}; exact sign test p = {p['p']:.3f}."]
        L += ["", "| Expected outcome | baseline | skill |", "|---|--:|--:|"]
        for oc, v in sorted(rep["by_outcome"].items()):
            L.append(f"| {oc} | {v['baseline'][0]}/{v['baseline'][1]} | {v['skill'][0]}/{v['skill'][1]} |")
        if rep["regressions"]:
            L += ["", "**Skill regressions (baseline passed, skill failed):**"]
            for cid, run, cf, hf in rep["regressions"]:
                L.append(f"- {cid} (run {run}): critical failed {cf or '-'}{', deterministic hard-fail' if hf else ''}")
        for arm in ARMS:
            if rep["top_missed"][arm]:
                L += ["", f"Most missed critical criteria ({arm}): " + ", ".join(f"{k} x{v}" for k, v in rep["top_missed"][arm])]
    if agreement:
        L += ["", "## Judge agreement (Cohen's kappa on criterion verdicts)"]
        for i, j, k, n in agreement:
            L.append(f"- judge {i} vs judge {j}: kappa = {k:.2f} over {n} verdicts")
    if warnings:
        L += ["", "## Warnings", *[f"- {w}" for w in warnings[:30]]]
    return "\n".join(L) + "\n"


def score(cases_path, criteria_path, responses_path, key_path, verdict_paths, allow_partial=False):
    cases = load_cases(cases_path)
    criteria = load_criteria(criteria_path, set(cases))
    responses = load_responses(responses_path, set(cases), allow_partial)
    key = _load_json(key_path)
    if key["responses_sha256"] != sha256_file(responses_path):
        raise EvalInputError("responses file changed since `prepare`; re-run prepare and re-judge")
    if key["criteria_sha256"] != sha256_file(criteria_path):
        raise EvalInputError("criteria file changed since `prepare`; re-run prepare and re-judge")
    text_by_id = {}
    lookup = {(r["model"], r["case_id"], r["arm"], r["run"]): r["output"] for r in responses}
    for iid, meta in key["items"].items():
        text_by_id[iid] = lookup[(meta["model"], meta["case_id"], meta["arm"], meta["run"])]
    per_judge, warnings = [], []
    for vp in verdict_paths:
        v, w = load_verdicts(Path(vp), key["items"], {cid: criteria[cid] for cid in criteria}, text_by_id, allow_partial)
        per_judge.append(v)
        warnings += w
    combined = combine_judges(per_judge)
    results = []
    for iid, sat in combined.items():
        meta = key["items"][iid]
        r = score_item(criteria[meta["case_id"]]["criteria"], sat, key["deterministic"][iid])
        r.update(meta)
        results.append(r)
    runs = max(m["run"] for m in key["items"].values())
    return aggregate(results, criteria), judge_agreement(per_judge), warnings, len(per_judge), runs


# ---------------------------------------------------------------------- CLI

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("prepare", "score"):
        p = sub.add_parser(name)
        p.add_argument("--cases", type=Path, default=DEFAULT_CASES)
        p.add_argument("--criteria", type=Path, default=DEFAULT_CRITERIA)
        p.add_argument("--responses", type=Path, required=True)
        p.add_argument("--allow-partial", action="store_true")
        p.add_argument("--out", type=Path, required=True)
    sub.choices["prepare"].add_argument("--seed", type=int, default=None)
    sub.choices["prepare"].add_argument("--judge-prompt", type=Path, default=DEFAULT_PROMPT)
    sub.choices["score"].add_argument("--key", type=Path, required=True)
    sub.choices["score"].add_argument("--verdicts", type=Path, action="append", required=True)
    sub.add_parser("validate-criteria").add_argument("--cases", type=Path, default=DEFAULT_CASES)
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    try:
        if args.cmd == "validate-criteria":
            cases = load_cases(args.cases)
            load_criteria(DEFAULT_CRITERIA, set(cases))
            print(f"OK: {len(cases)} cases have valid criteria")
            return 0
        if args.cmd == "prepare":
            info = prepare(args.cases, args.criteria, args.responses, args.out, args.judge_prompt,
                           args.allow_partial, args.seed)
            print(f"Wrote {info['items']} blinded judge items to {info['out']} "
                  f"({info['hard_fails']} deterministic hard-fails).")
            return 0
        report, agreement, warnings, n_judges, n_runs = score(
            args.cases, args.criteria, args.responses, args.key, args.verdicts, args.allow_partial)
        md = render_report(report, agreement, warnings, n_judges, n_runs)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(md, encoding="utf-8")
        print(md)
        return 0
    except EvalInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
