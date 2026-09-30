# Contributing to `triz-universal`

Thank you for your interest in improving `triz-universal`! Because this skill enforces rigorous, non-compromising problem solving across software, AI, business, and physical engineering, every change must preserve methodological discipline, token efficiency, and verifiable honesty.

## Core Principles for Contributors

1. **No Fabricated Guarantees:** Never add examples or rules that claim "100% compliance", "zero memory overhead", or "measured speedup" without stating the boundary assumptions and required verification.
2. **Respect Context Token Budgets:**
   - `triz-universal/SKILL.md` (Tier-1 dispatcher) must remain under **300 lines** (~6,600 tokens).
   - Every reference file in `triz-universal/references/` (Tier-2 and Tier-3) must remain under **500 lines**.
3. **Quarantine Offline Benchmarks:** Benchmark scenarios (`evals/10-testing-scenarios.md`), reference problem solutions (`evals/12-evaluation-suite.md`), and evaluation corpora (`evals/cases.json`, `evals/trigger_corpus.json`) must reside in `evals/` outside `triz-universal/` and must never be injected into the active problem-solving routing table in `SKILL.md` to prevent answer-key anchoring.
4. **Bilingual Parity (EN / RU):** Any change to `SKILL.md` templates, triggers, or `README.md` must be reflected in the Russian equivalents (`README.ru.md`, Russian template in `SKILL.md`).

## Development & Verification Workflow

Before opening a Pull Request, run the full verification suite (requires only Python 3.10+ standard library):

```bash
# 1. Run unit and structural integrity tests
python tests/test_triz_skill.py

# 2. Run offline token budget, trigger accuracy, and reference corpus self-tests
python evals/run_evals.py

# 3. Validate paraphrase-tolerant live-eval judge criteria
python evals/live_eval.py validate-criteria

# 4. Test cross-platform deployment parity and release packaging
python scripts/sync_deployment.py --package-zip
```

## Adding New Evaluation Cases

When adding cases to `evals/cases.json`:
- Specify `id`, `domain`, `language` (`en` or `ru`), `prompt`, `hard_constraints`, `disallowed_claims`, `expected_outcome` (`eliminate`, `prove-limit`, `managed-tradeoff`, `conditional`, or `no-trigger`), and `required_evidence`.
- Add matching paraphrase-tolerant `must` / `avoid` criteria (`critical: true/false`) to `evals/judge_criteria.json`.
- Ensure `python evals/live_eval.py validate-criteria`, `python evals/run_evals.py`, and `python tests/test_triz_skill.py` pass.

## License

By contributing to `torrua/triz-skill`, you agree that your contributions are original clean-room work and will be licensed under the [MIT License](LICENSE).
