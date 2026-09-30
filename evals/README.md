# Behavioral, Trigger & Live-Model Evaluation Suite

The structural unit tests in `tests/test_triz_skill.py` validate document structure, cross-links, version parity, and safety guardrails. This directory (`evals/`) separates **offline regression self-tests** from the **paraphrase-tolerant blinded live-model evaluation harness**:

- **`evals/live_eval.py` + `evals/judge_criteria.json` + `evals/judge_prompt.md`:** The live-model evaluation harness for real LLM outputs (`baseline` vs. `skill`), featuring 105 paraphrase-tolerant `must` / `avoid` criteria (`critical: true/false`), deterministic `hard_fail_patterns` and `anchors`, randomized blinded item generation (`judge_items.jsonl` + `judge_key.json`), verbatim quote verification, strict majority voting across multiple judges, Cohen's kappa inter-judge agreement, Wilson 95% confidence intervals, and exact two-sided McNemar/sign tests.
- **`evals/run_evals.py` + `evals/cases.json` + `evals/trigger_corpus.json`:** Offline self-test of the reference corpus, context token budgets, and bilingual trigger routing rules (not evidence that live models improve).

## 1. Quick Start: Offline Self-Test & Criteria Validation

Run the offline self-test and criteria validator from the repository root:

```bash
python evals/run_evals.py
python evals/live_eval.py validate-criteria
```

This verifies:
1. **Context Token Budget:** Measures exact lines, bytes, and estimated tokens across Tier-1 (`SKILL.md`), Tier-2 (`references/*.md`), and Tier-3 (`references/ariz-deep/*.md`).
2. **Trigger Precision & Recall (`evals/trigger_corpus.json`):** Tests 40 bilingual (EN/RU) positive and negative prompts (including DB deadlocks, CPU profiling bugs, meta-TRIZ mentions, and explicit compromise requests) across No-Trigger, Layer 1, and Layer 2 routing.
3. **Offline Reference-Corpus Self-Test (`evals/cases.json`):** Evaluates the 20 reference RED/GREEN pairs across all 5 outcome categories: `eliminate` (10), `prove-limit` (4), `conditional` (1), `managed-tradeoff` (1), and `no-trigger` (4).
4. **Judge Criteria Validation (`evals/judge_criteria.json`):** Confirms all 20 cases define valid `must`/`avoid` criteria (at least one `critical` and one `avoid` per case) and valid regexes for `hard_fail_patterns` and `anchors`.

## 2. Running a Blinded Live-Model Evaluation (`evals/live_eval.py`)

To evaluate real LLM checkpoints (e.g., Claude, Gemini, GPT) with zero substring bias and no silent fallbacks:

1. **Collect raw model outputs** (with and without `triz-universal`, across `run: 1..N`) into a JSON file `live.json`:
   ```json
   [
     {"model": "model-name", "case_id": "distributed-inventory-consistency", "arm": "baseline", "run": 1, "output": "..."},
     {"model": "model-name", "case_id": "distributed-inventory-consistency", "arm": "skill", "run": 1, "output": "..."}
   ]
   ```
2. **Prepare blinded judge items** (strictly validates completeness unless `--allow-partial` is explicitly passed, runs deterministic pre-checks, and shuffles items with a cryptographic salt so judges cannot guess the arm or model):
   ```bash
   python evals/live_eval.py prepare --responses live.json --out evals/out
   ```
3. **Grade `evals/out/judge_items.jsonl`** using at least 2 independent judges (including human expert review for public claims) following `evals/judge_prompt.md`. Each judge outputs one JSON object per line:
   ```json
   {"item_id": "...", "verdicts": [{"criterion_id": "m1", "satisfied": true, "evidence": "\"verbatim quote from response\""}, ...]}
   ```
4. **Score and generate the statistical report** (verifies SHA-256 hashes of responses/criteria against `judge_key.json`, checks that quoted evidence actually appears in the response, combines judges by strict majority, and computes Wilson 95% CIs, exact two-sided McNemar/sign test $p$-values, skill regressions, and Cohen's kappa):
   ```bash
   python evals/live_eval.py score --responses live.json --key evals/out/judge_key.json \
       --verdicts judgeA.jsonl --verdicts judgeB.jsonl --out evals/out/report.md
   ```

## Published Results

See [BENCHMARK_REPORT.md](BENCHMARK_REPORT.md) for current token budgets, trigger precision/recall, offline reference-corpus self-test results, live evaluation methodology, and documented failure modes.
