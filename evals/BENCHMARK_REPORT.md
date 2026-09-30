# `triz-universal` v3.0.0 — Evaluation, Trigger & Context Token Benchmark Report

> **Reproducibility:** Run `python evals/run_evals.py` from the repository root to recompute all metrics below from the live source tree.

---

## 1. Context Token Budget Measurements (Tier-1 vs. Tier-2 vs. Tier-3)

To verify the progressive disclosure claim empirically, `evals/run_evals.py` measures exact line counts, UTF-8 byte sizes, and BPE token estimates across all 21 deployed skill files (`SKILL.md` + 13 Tier-2 modules + 7 Tier-3 deep protocols; benchmark files `10-testing-scenarios.md` and `12-evaluation-suite.md` are quarantined outside `triz-universal/` in `evals/`):

| Architecture Layer | Files | Lines | UTF-8 Bytes | Estimated Tokens | Context Overhead vs. Monolithic Load |
|---|---:|---:|---:|---:|---:|
| **Tier-1 (`triz-universal/SKILL.md`)** | 1 | 251 | 25,637 | ~6,622 | **88.1% reduction** (always-loaded dispatcher) |
| **Tier-2 Foundation (`references/*.md`)** | 13 | 1,262 | 103,734 | ~26,954 (avg ~2,073/file) | Loaded on demand (0–2 files per task) |
| **Tier-3 Deep ARIZ-85-V (`references/ariz-deep/*.md`)** | 7 | 824 | 93,834 | ~21,985 (avg ~3,141/file) | Loaded only for Level 4–5 deadlocks |
| **Total Deployed Skill Knowledge Base** | **21** | **2,337** | **223,205** | **~55,561** | 100.0% (if loaded monolithically) |

### Typical Turn Consumption Profiles
- **Fast-Path Contradiction Turn (Tier-1 only):** `~6,622 tokens` (**88.1% savings** vs. monolithic load).
- **Standard Domain Turn (Tier-1 + 1 Tier-2 module):** `~8,695 tokens` (**84.4% savings** vs. monolithic load).
- **Deep Level 4–5 Deadlock Turn (Tier-1 + 1 Tier-2 + 1 Tier-3 protocol):** `~11,836 tokens` (**78.7% savings** vs. monolithic load).

---

## 2. Trigger Precision, Recall & Layer Routing (`evals/trigger_corpus.json`)

Evaluated across **40 bilingual (EN/RU) prompts** (20 positive contradiction/TRIZ prompts + 20 negative/boundary prompts including routine SQL deadlocks, CPU profiling loops, simple pros/cons comparisons, meta-mentions of "TRIZ", and explicit user compromise requests):

| Metric | Value | Notes |
|---|---:|---|
| **Total Prompts Evaluated** | 40 | 20 English, 20 Russian |
| **True Positives (TP)** | 20 / 20 | Contradictions & explicit TRIZ/ИКР/ФП/ВПР/АРИЗ requests |
| **True Negatives (TN)** | 20 / 20 | Routine DB deadlocks, single-metric bugs, pros/cons, meta-TRIZ questions |
| **False Positives (FP)** | 0 / 20 | Prevented by `When NOT to Use`, `Routing Guardrail`, and pruned `metadata.triggers` |
| **False Negatives (FN)** | 0 / 20 | Bilingual EN/RU triggers in `description` cover both languages |
| **Trigger Precision** | **100.0%** | `TP / (TP + FP)` |
| **Trigger Recall** | **100.0%** | `TP / (TP + FN)` |
| **Layer Routing Accuracy (No-Trigger vs. Layer 1 vs. Layer 2)** | **100.0%** | Practical conflicts route to Layer 1; explicit TRIZ requests route to Layer 2 |

---

## 3. Multi-Outcome Rubric Harness & Reference Corpus (`evals/cases.json`)

> **Important Methodological Note (Reference Corpus vs. Live Model Runs):**
> - By default (`python evals/run_evals.py`), the evaluator runs in **`reference_regression_corpus` mode**: it verifies that the deterministic scoring rubric (`disallowed_claims`, `required_evidence`, and `expected_outcome` validators) rejects 20 representative unconstrained RED failure baselines (`0/20`) and accepts 20 compliant GREEN reference resolutions (`20/20`) stored in `evals/cases.json`. This runs offline in CI with zero API keys or network dependencies.
> - To score **live, unedited LLM outputs** from external API runs (e.g., Claude, Gemini, GPT), pass `--responses-file <path.json>` (`python evals/run_evals.py --responses-file live_runs.json`), where each entry maps `case_id` to `{"baseline_output": "...", "skill_output": "..."}`.

The 20-case evaluation corpus spans 7 domains (`software`, `ai`, `fintech`, `business`, `hardware`, `organization`, `meta`) and 4 required outcome classes:

| Outcome Category | Cases | Reference RED Baseline Pass Rate | Reference GREEN Skill Pass Rate | Key Failure Mode Caught by Rubric |
|---|---:|---:|---:|---|
| **`eliminate`** (Contradiction Resolved) | 10 | 0 / 10 (0%) | **10 / 10 (100%)** | Prematurely sacrifices latency, durability, or security via naive middle-ground compromises |
| **`prove-limit`** (Irreducible Physical/Math/Legal Bound) | 5 | 0 / 5 (0%) | **5 / 5 (100%)** | Hallucinates impossible speedups/compliance (violating CAP, Amdahl, Shannon, Li-ion chemistry, or KYC law) |
| **`managed-tradeoff`** (User-Authorized Soft Target) | 2 | 0 / 2 (0%) | **2 / 2 (100%)** | Either claims a probabilistic filter has zero error or omits error-budget/staleness bounds |
| **`no-trigger`** (Scope Guardrail / Ordinary Bug) | 3 | 0 / 3* | **3 / 3 (100%)** | Forces artificial TRIZ contradictions onto SQL lock-ordering bugs or CSS alignment |
| **Total Across All Outcomes** | **20** | **0 / 20** | **20 / 20 (100%)** | — |

*\*Note on `no-trigger` baseline scoring:* The rubric requires explicit verification evidence (e.g., `unit test for concurrent transfer` in `sql-deadlock-stacktrace-debug`) alongside avoiding unnecessary TRIZ ceremony.

---

## 4. Documented Failure Modes: Where `triz-universal` Does Not Help or Can Hurt

Honest engineering requires documenting where forcing TRIZ is counterproductive:

1. **Routine Bug Fixing & Lock-Ordering Deadlocks (`sql-deadlock-stacktrace-debug`):**
   - *How TRIZ hurts if misapplied:* If an agent treats a classic AB/BA mutex deadlock in application code as an "inventive contradiction" and proposes event-sourcing or striped counters instead of sorting lock acquisition order (`ORDER BY account_id`), it introduces massive accidental complexity.
   - *Mitigation in v3.0.0:* Explicit negative triggers in `SKILL.md` frontmatter, pruned `metadata.triggers`, and Section 1 (`When NOT to Use This Skill`).
2. **Simple Prototypes & Explicit Compromise Requests (`explicit-user-compromise-request-ru`):**
   - *How TRIZ hurts if misapplied:* When a developer building a weekend prototype explicitly asks whether to use a 10s or 60s TTL cache, refusing to answer and lecturing them on CDC/MVCC wastes time and tokens.
   - *Mitigation in v3.0.0:* `Step 0` pre-check, Outcome 3 (`managed-tradeoff` on soft constraints with explicit user authorization), and the `Fast-Path` rule.
3. **Reasoning Latency & Token Overhead on Trivial Tasks:**
   - Running the ARIZ-AI pipeline adds ~400–900 internal reasoning tokens and ~6.5k system prompt tokens. For straightforward CRUD or single-metric optimizations where no opposing constraint degrades, standard coding skills are faster and cheaper.
4. **Automated Reference Rubric vs. Live Blind Human Expert Review:**
   - The default run of `evals/run_evals.py` deterministically validates the scoring rubric against embedded reference RED/GREEN outputs.
   - Evaluating stochastic live model behavior across new model checkpoints requires running live generations through `--responses-file` and conducting the blinded multi-reviewer protocol described in [evals/README.md](README.md).
