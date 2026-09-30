#!/usr/bin/env python3
"""Tests for evals/live_eval.py (run: python tests/test_live_eval.py)."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "evals"))

import live_eval as le  # noqa: E402

CRITERIA_PATH = ROOT / "evals" / "judge_criteria.json"
PROMPT_PATH = ROOT / "evals" / "judge_prompt.md"


def stub_cases(tmp: Path) -> Path:
    ids = list(json.loads(CRITERIA_PATH.read_text(encoding="utf-8"))["cases"])
    path = tmp / "cases.json"
    path.write_text(json.dumps([{"id": i, "prompt": f"Task for {i}"} for i in ids]), encoding="utf-8")
    return path


def full_responses(case_ids, model="m1", run=1, text_for=lambda cid, arm: f"{arm} answer for {cid}"):
    return [{"model": model, "case_id": c, "arm": a, "run": run, "output": text_for(c, a)}
            for c in case_ids for a in le.ARMS]


class CriteriaFileTests(unittest.TestCase):
    def test_criteria_file_is_valid_and_complete(self):
        data = json.loads(CRITERIA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(len(data["cases"]), 20)
        le.load_criteria(CRITERIA_PATH, set(data["cases"]))

    def test_every_case_has_critical_must_and_avoid(self):
        data = le.load_criteria(CRITERIA_PATH)
        for cid, entry in data.items():
            kinds = {(c["kind"], c["critical"]) for c in entry["criteria"]}
            self.assertIn(("must", True), kinds, cid)
            self.assertTrue(any(k == "avoid" for k, _ in kinds), cid)

    def test_no_tabs_or_empty_text(self):
        for cid, entry in le.load_criteria(CRITERIA_PATH).items():
            for c in entry["criteria"]:
                self.assertTrue(c["text"].strip(), f"{cid}/{c['id']}")


class StrictLoadingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.cases = stub_cases(self.tmp)
        self.ids = set(le.load_cases(self.cases))

    def _write(self, rows):
        p = self.tmp / "resp.json"
        p.write_text(json.dumps(rows), encoding="utf-8")
        return p

    def test_complete_file_loads(self):
        rows = full_responses(sorted(self.ids))
        self.assertEqual(len(le.load_responses(self._write(rows), self.ids)), 40)

    def test_missing_pair_is_an_error_not_a_fallback(self):
        rows = full_responses(sorted(self.ids))[:-1]
        with self.assertRaises(le.EvalInputError):
            le.load_responses(self._write(rows), self.ids)

    def test_allow_partial_scores_what_exists(self):
        rows = full_responses(sorted(self.ids))[:-1]
        self.assertEqual(len(le.load_responses(self._write(rows), self.ids, allow_partial=True)), 39)

    def test_unknown_case_duplicate_bad_arm_and_empty_output(self):
        base = full_responses(sorted(self.ids))
        bad = [
            base + [dict(base[0], case_id="nope")],
            base + [dict(base[0])],
            [dict(base[0], arm="reference")] + base[1:],
            [dict(base[0], output="   ")] + base[1:],
        ]
        for rows in bad:
            with self.assertRaises(le.EvalInputError):
                le.load_responses(self._write(rows), self.ids)

    def test_legacy_dict_format(self):
        legacy = {c: {"baseline_output": "b", "skill_output": "s"} for c in sorted(self.ids)}
        self.assertEqual(len(le.load_responses(self._write(legacy), self.ids)), 40)


class DeterministicTests(unittest.TestCase):
    def setUp(self):
        self.crit = le.load_criteria(CRITERIA_PATH)

    def test_ceremony_in_no_trigger_case_is_hard_fail(self):
        e = self.crit["simple-css-button-alignment"]
        self.assertTrue(le.deterministic_checks(e, "### 💡 TRIZ Inventive Resolution\n...")["hard_fail"])
        self.assertFalse(le.deterministic_checks(e, ".card { display: grid; place-items: center; }")["hard_fail"])

    def test_meta_question_may_mention_concepts_without_passport(self):
        e = self.crit["meta-triz-question-ru"]
        text = "ТРИЗ работает с понятиями идеального конечного результата и физического противоречия. Статья вышла в 1956 году."
        self.assertFalse(le.deterministic_checks(e, text)["hard_fail"])

    def test_anchor_missing_is_reported_but_not_a_hard_fail(self):
        e = self.crit["amdahl-serial-bottleneck"]
        r = le.deterministic_checks(e, "Just add cores.")
        self.assertFalse(r["hard_fail"])
        self.assertIn("limit_4x", r["anchor_missing"])


class StatsTests(unittest.TestCase):
    def test_wilson_bounds(self):
        lo, hi = le.wilson(10, 10)
        self.assertGreater(lo, 0.6)
        self.assertEqual(hi, 1.0)
        self.assertEqual(le.wilson(0, 0), (0.0, 0.0))

    def test_sign_test(self):
        self.assertEqual(le.sign_test_p(0, 0), 1.0)
        self.assertAlmostEqual(le.sign_test_p(10, 0), 2 / 1024, places=6)
        self.assertEqual(le.sign_test_p(5, 5), 1.0)

    def test_kappa(self):
        self.assertEqual(le.cohens_kappa([True, False, True], [True, False, True]), 1.0)
        self.assertLess(le.cohens_kappa([True, True, False, False], [True, False, True, False]), 0.1)


class EndToEndTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.cases = stub_cases(self.tmp)
        self.ids = sorted(le.load_cases(self.cases))
        self.crit = le.load_criteria(CRITERIA_PATH, set(self.ids))

    def _prepare(self, rows):
        resp = self.tmp / "resp.json"
        resp.write_text(json.dumps(rows), encoding="utf-8")
        info = le.prepare(self.cases, CRITERIA_PATH, resp, self.tmp / "out", PROMPT_PATH, seed=7)
        return resp, info

    def _verdicts(self, key, decide, path):
        lines = []
        for iid, meta in key["items"].items():
            crit = self.crit[meta["case_id"]]["criteria"]
            vs = [{"criterion_id": c["id"], "satisfied": decide(meta, c), "evidence": "absent - test"} for c in crit]
            lines.append(json.dumps({"item_id": iid, "verdicts": vs}))
        path.write_text("\n".join(lines), encoding="utf-8")
        return path

    def test_judge_inputs_are_blinded(self):
        rows = full_responses(self.ids, text_for=lambda c, a: f"secret-{a}-marker")
        _, info = self._prepare(rows)
        self.assertEqual(info["items"], 40)
        text = (self.tmp / "out" / "judge_items.jsonl").read_text(encoding="utf-8")
        for line in text.strip().splitlines():
            row = json.loads(line)
            self.assertNotIn("arm", row)
            self.assertNotIn("model", row)
            self.assertIn("CRITERIA:", row["judge_prompt"])
            self.assertNotIn("{{", row["judge_prompt"])
            self.assertIn(row["item_id"], row["judge_prompt"])
        first_arms = [json.loads(l)["item_id"] for l in text.strip().splitlines()[:6]]
        self.assertEqual(len(set(first_arms)), 6)

    def test_skill_wins_are_measured_and_regressions_reported(self):
        rows = full_responses(self.ids)
        resp, _ = self._prepare(rows)
        key = json.loads((self.tmp / "out" / "judge_key.json").read_text(encoding="utf-8"))

        def decide(meta, crit):
            if meta["arm"] == "skill":
                return not (meta["case_id"] == "simple-css-button-alignment")  # one regression
            return crit["kind"] == "avoid" or meta["case_id"] in ("sql-deadlock-stacktrace-debug", "simple-css-button-alignment")

        v = self._verdicts(key, decide, self.tmp / "j1.jsonl")
        report, agreement, warnings, n_judges, n_runs = le.score(
            self.cases, CRITERIA_PATH, resp, self.tmp / "out" / "judge_key.json", [v])
        rep = report["m1"]
        self.assertEqual(rep["arms"]["skill"]["pass"], 19)
        self.assertEqual(rep["paired"]["baseline_only"], 1)
        self.assertEqual(rep["paired"]["both"], 1)
        self.assertTrue(any(r[0] == "simple-css-button-alignment" for r in rep["regressions"]))
        md = le.render_report(report, agreement, warnings, n_judges, n_runs)
        self.assertIn("Not sufficient for public claims", md)

    def test_deterministic_hard_fail_overrides_a_lenient_judge(self):
        def text_for(cid, arm):
            if cid == "simple-css-button-alignment" and arm == "skill":
                return "### 💡 TRIZ Inventive Resolution\n- Physical Contradiction: ..."
            return f"{arm} answer"
        resp, _ = self._prepare(full_responses(self.ids, text_for=text_for))
        key = json.loads((self.tmp / "out" / "judge_key.json").read_text(encoding="utf-8"))
        v = self._verdicts(key, lambda m, c: True, self.tmp / "j1.jsonl")
        report, *_ = le.score(self.cases, CRITERIA_PATH, resp, self.tmp / "out" / "judge_key.json", [v])
        self.assertEqual(report["m1"]["arms"]["skill"]["pass"], 19)
        self.assertEqual(report["m1"]["arms"]["baseline"]["pass"], 20)

    def test_changed_responses_after_prepare_are_rejected(self):
        resp, _ = self._prepare(full_responses(self.ids))
        key = json.loads((self.tmp / "out" / "judge_key.json").read_text(encoding="utf-8"))
        v = self._verdicts(key, lambda m, c: True, self.tmp / "j1.jsonl")
        rows = full_responses(self.ids, text_for=lambda c, a: "changed")
        resp.write_text(json.dumps(rows), encoding="utf-8")
        with self.assertRaises(le.EvalInputError):
            le.score(self.cases, CRITERIA_PATH, resp, self.tmp / "out" / "judge_key.json", [v])

    def test_verdict_without_evidence_or_with_missing_criterion_is_rejected(self):
        resp, _ = self._prepare(full_responses(self.ids))
        key = json.loads((self.tmp / "out" / "judge_key.json").read_text(encoding="utf-8"))
        iid, meta = next(iter(key["items"].items()))
        crit = self.crit[meta["case_id"]]["criteria"]
        p = self.tmp / "bad.jsonl"
        p.write_text(json.dumps({"item_id": iid, "verdicts": [
            {"criterion_id": c["id"], "satisfied": True, "evidence": ""} for c in crit]}), encoding="utf-8")
        with self.assertRaises(le.EvalInputError):
            le.load_verdicts(p, key["items"], self.crit, {iid: "x"}, allow_partial=True)
        p.write_text(json.dumps({"item_id": iid, "verdicts": [
            {"criterion_id": crit[0]["id"], "satisfied": True, "evidence": "ok"}]}), encoding="utf-8")
        with self.assertRaises(le.EvalInputError):
            le.load_verdicts(p, key["items"], self.crit, {iid: "x"}, allow_partial=True)

    def test_two_judges_majority_and_kappa(self):
        resp, _ = self._prepare(full_responses(self.ids))
        key = json.loads((self.tmp / "out" / "judge_key.json").read_text(encoding="utf-8"))
        v1 = self._verdicts(key, lambda m, c: True, self.tmp / "j1.jsonl")
        v2 = self._verdicts(key, lambda m, c: m["arm"] == "skill", self.tmp / "j2.jsonl")
        report, agreement, *_ = le.score(self.cases, CRITERIA_PATH, resp, self.tmp / "out" / "judge_key.json", [v1, v2])
        self.assertEqual(len(agreement), 1)
        # tie between two judges counts as not satisfied -> baseline cannot pass
        self.assertEqual(report["m1"]["arms"]["baseline"]["pass"], 0)
        self.assertEqual(report["m1"]["arms"]["skill"]["pass"], 20)


if __name__ == "__main__":
    unittest.main(verbosity=2)
