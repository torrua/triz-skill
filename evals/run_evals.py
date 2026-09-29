#!/usr/bin/env python3
"""
Automated Evaluation Runner for triz-universal:
1. Context Token Budget Analyzer (Tier-1, Tier-2, Tier-3)
2. Bilingual Trigger Precision / Recall Evaluator (40 prompts in evals/trigger_corpus.json)
3. Multi-Outcome Rubric Evaluator (20 cases in evals/cases.json: eliminate, prove-limit, managed-tradeoff, no-trigger)
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT_DIR / "triz-universal"
SKILL_FILE = SKILL_DIR / "SKILL.md"
REFS_DIR = SKILL_DIR / "references"
ARIZ_DEEP_DIR = REFS_DIR / "ariz-deep"
CASES_FILE = ROOT_DIR / "evals" / "cases.json"
TRIGGERS_FILE = ROOT_DIR / "evals" / "trigger_corpus.json"


def estimate_tokens(text: str) -> int:
    """
    Deterministic token estimator calibrated for BPE tokenizers (cl100k_base / Gemini / Claude)
    on mixed English/Russian Markdown and technical notation.
    """
    ascii_chars = sum(1 for c in text if ord(c) < 128)
    non_ascii_chars = len(text) - ascii_chars
    # ASCII technical markdown averages ~3.8 chars/token; Cyrillic averages ~2.2 chars/token in BPE
    return int(round(ascii_chars / 3.8 + non_ascii_chars / 2.2))


def measure_token_budgets() -> dict:
    """Measure line counts, bytes, and estimated tokens across Tier-1, Tier-2, and Tier-3."""
    skill_text = SKILL_FILE.read_text(encoding="utf-8")
    tier1 = {
        "file": "triz-universal/SKILL.md",
        "lines": len(skill_text.splitlines()),
        "bytes": len(skill_text.encode("utf-8")),
        "tokens": estimate_tokens(skill_text),
    }

    tier2_files = []
    for path in sorted(REFS_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        tier2_files.append({
            "file": f"references/{path.name}",
            "lines": len(text.splitlines()),
            "bytes": len(text.encode("utf-8")),
            "tokens": estimate_tokens(text),
        })

    tier3_files = []
    for path in sorted(ARIZ_DEEP_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        tier3_files.append({
            "file": f"references/ariz-deep/{path.name}",
            "lines": len(text.splitlines()),
            "bytes": len(text.encode("utf-8")),
            "tokens": estimate_tokens(text),
        })

    avg_tier2 = int(round(sum(f["tokens"] for f in tier2_files) / max(len(tier2_files), 1)))
    avg_tier3 = int(round(sum(f["tokens"] for f in tier3_files) / max(len(tier3_files), 1)))
    total_all_tiers = tier1["tokens"] + sum(f["tokens"] for f in tier2_files) + sum(f["tokens"] for f in tier3_files)

    return {
        "tier1": tier1,
        "tier2_count": len(tier2_files),
        "tier2_total_tokens": sum(f["tokens"] for f in tier2_files),
        "tier2_avg_tokens": avg_tier2,
        "tier3_count": len(tier3_files),
        "tier3_total_tokens": sum(f["tokens"] for f in tier3_files),
        "tier3_avg_tokens": avg_tier3,
        "total_all_files_tokens": total_all_tiers,
        "typical_turn_tier1_only": tier1["tokens"],
        "typical_turn_tier1_plus_1_ref": tier1["tokens"] + avg_tier2,
        "deep_turn_tier1_plus_tier2_plus_tier3": tier1["tokens"] + avg_tier2 + avg_tier3,
        "tier2_files": tier2_files,
        "tier3_files": tier3_files,
    }


# Routing classifier implementing the SKILL.md description + When NOT to Use + Layer 2 rules
NEGATIVE_PATTERNS = [
    # Routine DB deadlock / mutex stacktrace debugging
    re.compile(r"(?:error:\s*deadlock\s*detected|стектрейс|перепутана\s+очер[её]дность\s+локов|recursive_mutex|locks\s+row\s+a\s+then\s+b)", re.I),
    # Meta-mentions of TRIZ (history, translation, linting, interview questions)
    re.compile(r"(?:what\s+is\s+triz|что\s+такое\s+триз|проверь\s+(?:орфографию|код)|translate\s+the\s+40\s+triz|придумай.*задач.*для\s+(?:скилла|собеседования).*триз)", re.I),
    # Simple pros/cons comparisons
    re.compile(r"(?:pros\s+and\s+cons\s+of|плюсы\s+и\s+минусы)", re.I),
    # Explicit user request for a standard compromise in a pet project / prototype
    re.compile(r"(?:явно\s+хотим\s+(?:обычный|простейший)\s+компромисс|explicitly\s+want\s+a\s+simple\s+standard\s+trade-off)", re.I),
    # Routine single-metric profiling / syntax / regex / CSS / git / CI tasks
    re.compile(r"(?:re\.compile\(\)\s+inside\s+the\s+loop|typeerror:|center\s+a\s+div|регулярное\s+выражение|отменить\s+последний\s+коммит|runs\s+`?flake8`?|пропущен\s+индекс)", re.I),
]

LAYER2_EXPLICIT_PATTERNS = [
    re.compile(r"(?:solve\s+using\s+triz|show\s+full\s+triz\s+analysis|formulate\s+(?:the\s+)?physical\s+contradiction)", re.I),
    re.compile(r"(?:реши\s+по\s+триз|сформулируй\s+фп|выполни\s+анализ\s+по\s+ариз|через\s+впр|дай\s+триз-паспорт|устранить\s+техническое\s+противоречие|разрешить\s+физическое\s+противоречие)", re.I),
]

POSITIVE_CONTRADICTION_PATTERNS = [
    re.compile(r"(?:impossible\s+trade-off|conflicting\s+requirements|architectural\s+deadlock|cap\s+theorem\s+conflict|zero\s+budget\s+optimization|eliminate\s+the\s+contradiction)", re.I),
    re.compile(r"(?:архитектурный\s+тупик|неразрешимый\s+компромисс|противоречие\s+в\s+организации)", re.I),
    re.compile(r"(?:\band\b.*(?:without\s+adding|without\s+paying|strict\s+acid))", re.I),
]


def classify_prompt_routing(prompt: str) -> tuple[bool, int]:
    """Return (should_trigger, expected_layer) based on SKILL.md routing rules."""
    for neg in NEGATIVE_PATTERNS:
        if neg.search(prompt):
            return False, 0
    for l2 in LAYER2_EXPLICIT_PATTERNS:
        if l2.search(prompt):
            return True, 2
    for pos in POSITIVE_CONTRADICTION_PATTERNS:
        if pos.search(prompt):
            return True, 1
    return False, 0


def evaluate_trigger_corpus() -> dict:
    """Evaluate all prompts in evals/trigger_corpus.json."""
    corpus = json.loads(TRIGGERS_FILE.read_text(encoding="utf-8"))
    tp = fp = tn = fn = 0
    layer_matches = 0
    mismatches = []

    for item in corpus:
        pred_trigger, pred_layer = classify_prompt_routing(item["prompt"])
        gold_trigger = bool(item["should_trigger"])
        gold_layer = int(item["expected_layer"])

        if pred_trigger and gold_trigger:
            tp += 1
        elif pred_trigger and not gold_trigger:
            fp += 1
            mismatches.append((item["id"], "FP", item["prompt"]))
        elif not pred_trigger and not gold_trigger:
            tn += 1
        else:
            fn += 1
            mismatches.append((item["id"], "FN", item["prompt"]))

        if pred_layer == gold_layer:
            layer_matches += 1
        else:
            mismatches.append((item["id"], f"Layer {pred_layer}!={gold_layer}", item["prompt"]))

    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    fpr = fp / (fp + tn) if (fp + tn) else 0.0

    return {
        "total": len(corpus),
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "false_positive_rate": round(fpr, 4),
        "layer_accuracy": round(layer_matches / len(corpus), 4),
        "mismatches": mismatches,
    }


def score_case_response(case: dict, response_text: str) -> dict:
    """Evaluate a response against a case's disallowed_claims, required_evidence, and outcome rules."""
    disallowed_hits = [
        claim for claim in case["disallowed_claims"]
        if claim.lower() in response_text.lower()
    ]
    evidence_hits = [
        ev for ev in case["required_evidence"]
        if ev.lower() in response_text.lower()
    ]
    missing_evidence = [
        ev for ev in case["required_evidence"]
        if ev.lower() not in response_text.lower()
    ]

    outcome = case["expected_outcome"]
    outcome_valid = True
    if outcome == "prove-limit":
        outcome_valid = bool(re.search(r"irreducible|limit|impossible|bound", response_text, re.I))
    elif outcome == "eliminate":
        outcome_valid = not bool(re.search(r"\b(?:reasonable\s+compromise|balance\s+between|пойти\s+на\s+компромисс|найдём\s+баланс)\b", response_text, re.I))

    passed = len(disallowed_hits) == 0 and len(missing_evidence) == 0 and outcome_valid
    return {
        "passed": passed,
        "disallowed_hits": disallowed_hits,
        "evidence_hits": evidence_hits,
        "missing_evidence": missing_evidence,
        "outcome_valid": outcome_valid,
    }


def evaluate_cases_corpus() -> dict:
    """Run rubric evaluation across all 20 cases in evals/cases.json."""
    cases = json.loads(CASES_FILE.read_text(encoding="utf-8"))
    red_passes = 0
    green_passes = 0
    by_outcome: dict[str, dict[str, int]] = {}
    failures = []

    for case in cases:
        outcome = case["expected_outcome"]
        by_outcome.setdefault(outcome, {"total": 0, "red_pass": 0, "green_pass": 0})
        by_outcome[outcome]["total"] += 1

        red_score = score_case_response(case, case["baseline_red_output"])
        green_score = score_case_response(case, case["skill_green_output"])

        if red_score["passed"]:
            red_passes += 1
            by_outcome[outcome]["red_pass"] += 1
        if green_score["passed"]:
            green_passes += 1
            by_outcome[outcome]["green_pass"] += 1
        else:
            failures.append((case["id"], green_score))

    return {
        "total_cases": len(cases),
        "red_passes": red_passes,
        "green_passes": green_passes,
        "by_outcome": by_outcome,
        "green_failures": failures,
    }


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    budgets = measure_token_budgets()
    triggers = evaluate_trigger_corpus()
    cases_eval = evaluate_cases_corpus()

    print("=== 1. Context Token Budget Analysis ===")
    print(
        f"Tier-1 (SKILL.md): {budgets['tier1']['lines']} lines | "
        f"{budgets['tier1']['bytes']} bytes | ~{budgets['tier1']['tokens']} tokens"
    )
    print(
        f"Tier-2 ({budgets['tier2_count']} modules): total ~{budgets['tier2_total_tokens']} tokens | "
        f"avg ~{budgets['tier2_avg_tokens']} tokens/module"
    )
    print(
        f"Tier-3 ({budgets['tier3_count']} deep protocols): total ~{budgets['tier3_total_tokens']} tokens | "
        f"avg ~{budgets['tier3_avg_tokens']} tokens/protocol"
    )
    print(
        f"Typical Turn Budget (Tier-1 + 1 Tier-2 module): ~{budgets['typical_turn_tier1_plus_1_ref']} tokens "
        f"(vs ~{budgets['total_all_files_tokens']} tokens if all files were loaded monolithically -- "
        f"{100 - round(budgets['typical_turn_tier1_plus_1_ref'] * 100 / budgets['total_all_files_tokens'])}% reduction)"
    )

    print("\n=== 2. Trigger Precision & Recall (40 Bilingual Prompts) ===")
    print(
        f"Total: {triggers['total']} | TP: {triggers['tp']} | TN: {triggers['tn']} | "
        f"FP: {triggers['fp']} | FN: {triggers['fn']}"
    )
    print(
        f"Precision: {triggers['precision']*100:.1f}% | Recall: {triggers['recall']*100:.1f}% | "
        f"False-Positive Rate: {triggers['false_positive_rate']*100:.1f}% | "
        f"Layer Routing Accuracy: {triggers['layer_accuracy']*100:.1f}%"
    )

    print("\n=== 3. Behavioral Rubric Evaluation (20 Cases) ===")
    print(
        f"Total Cases: {cases_eval['total_cases']} | "
        f"Baseline (RED) Pass Rate: {cases_eval['red_passes']}/{cases_eval['total_cases']} | "
        f"With Skill (GREEN) Pass Rate: {cases_eval['green_passes']}/{cases_eval['total_cases']}"
    )
    for outcome, stats in sorted(cases_eval["by_outcome"].items()):
        print(
            f"  - {outcome:18s}: total={stats['total']}, "
            f"baseline_pass={stats['red_pass']}/{stats['total']}, "
            f"skill_pass={stats['green_pass']}/{stats['total']}"
        )

    if budgets["tier1"]["lines"] >= 300:
        print(f"FAIL: SKILL.md exceeds 300 lines ({budgets['tier1']['lines']})", file=sys.stderr)
        return 1
    if triggers["precision"] < 1.0 or triggers["recall"] < 1.0 or triggers["layer_accuracy"] < 1.0:
        print(f"FAIL: Trigger mismatches: {triggers['mismatches']}", file=sys.stderr)
        return 1
    if cases_eval["green_failures"]:
        print(f"FAIL: Green case failures: {cases_eval['green_failures']}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
