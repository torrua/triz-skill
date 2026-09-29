# Behavioral & Trigger Evaluation Protocol

The structural unit tests in `tests/test_triz_skill.py` validate document structure, cross-links, version parity, and safety guardrails. This directory (`evals/`) provides the **behavioral, trigger, and token-budget evaluation suite** (`evals/cases.json`, `evals/trigger_corpus.json`, `evals/run_evals.py`, and [BENCHMARK_REPORT.md](BENCHMARK_REPORT.md)).

## Quick Start: Automated Evaluation Runner

Run the automated evaluation and token-budget suite from the repository root:

```bash
python evals/run_evals.py
```

This verifies:
1. **Context Token Budget:** Measures exact lines, bytes, and estimated tokens across Tier-1 (`SKILL.md`), Tier-2 (`references/*.md`), and Tier-3 (`references/ariz-deep/*.md`).
2. **Trigger Precision & Recall (`evals/trigger_corpus.json`):** Tests 40 bilingual (EN/RU) positive and negative prompts (including DB deadlocks, CPU profiling bugs, meta-TRIZ mentions, and explicit compromise requests) across No-Trigger, Layer 1, and Layer 2 routing.
3. **Multi-Outcome Rubric (`evals/cases.json`):** Evaluates 20 multi-domain cases across all four valid outcomes: `eliminate`, `prove-limit`, `managed-tradeoff`, and `no-trigger`.

## Running a Live Blinded Expert Evaluation Across Models

To evaluate live LLM checkpoints (e.g., Claude Sonnet/Opus, Gemini Pro/Flash, GPT) with human domain reviewers:

1. Give each case prompt from `evals/cases.json` to the target model **with** and **without** `triz-universal`.
2. Store raw outputs without exposing `expected_outcome`, `disallowed_claims`, or `required_evidence` to the model or evaluators.
3. Randomize and blind the outputs (strip TRIZ headers or evaluate in Layer 1 default mode) before expert review.
4. Have domain-qualified reviewers independently score constraint handling, factual support, feasibility, risk disclosure, and absence of over-engineering.
5. Record disagreements, environment, model checkpoint, prompt version, token consumption, and tool access.

## Passing Rubric

An answer passes only when it:

- preserves each hard constraint, proves the relevant irreducible limit (`prove-limit`), honors an authorized soft-constraint trade-off (`managed-tradeoff`), or bypasses TRIZ ceremony on routine non-contradiction bugs (`no-trigger`);
- avoids every `disallowed_claim` in the case;
- identifies assumptions and gives evidence/confidence (`Established`, `Pattern`, or `Hypothesis`);
- supplies a measurable verification plan and residual risks;
- is judged feasible by expert review for the relevant domain.

Phrase matching is intentionally insufficient. A response that merely says “Physical Contradiction”, “VPR”, and “Separation” must fail if it makes an unsupported guarantee or over-engineers a routine bug.

## Published Results

See [BENCHMARK_REPORT.md](BENCHMARK_REPORT.md) for current token budgets, trigger precision/recall, rubric scores, and documented failure modes.
