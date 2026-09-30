# `triz-universal` v3.1.0 — Evaluation, Trigger & Context Token Benchmark Report

> **Reproducibility:** Run `python evals/run_evals.py` and `python evals/live_eval.py validate-criteria` from the repository root to recompute all metrics below from the live source tree.

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

## 3. Offline Reference-Corpus Self-Test (`evals/cases.json`) & Live-Model Evaluation Harness (`evals/live_eval.py`)

> **Important Methodological Distinction (Offline Reference Self-Test vs. Live Blinded Model Evaluation):**
> - **Offline Reference-Corpus Self-Test (`python evals/run_evals.py`):** Evaluates the 20 reference RED/GREEN pairs embedded in `evals/cases.json` against the deterministic offline check (`disallowed_claims`, `required_evidence`, and `expected_outcome` validators). This runs offline in CI with zero API keys to guard against regressions in the reference corpus, **not** as proof that live models improve.
> - **Live Blinded Multi-Judge Evaluation (`python evals/live_eval.py`):** Replaces substring matching for real LLM outputs (`baseline` vs. `skill`) with **105 paraphrase-tolerant `must` / `avoid` criteria** in `evals/judge_criteria.json` and the blinded rubric in `evals/judge_prompt.md`:
>   1. `prepare` strictly validates that all `(case_id, arm)` pairs exist (failing on missing entries unless `--allow-partial` is explicitly passed — never silently falling back to reference texts), runs deterministic `hard_fail_patterns` / `anchors`, and writes shuffled, cryptographically salted `judge_items.jsonl` + `judge_key.json`.
>   2. `score` verifies SHA-256 integrity of `responses` and `judge_criteria.json`, checks that verbatim quoted `evidence` strings actually exist in the graded response, combines multiple judges by strict majority, and outputs **Wilson 95% confidence intervals**, **exact two-sided McNemar/sign test $p$-values**, **skill regressions**, and **Cohen's $\kappa$ inter-judge agreement**.

The 20-case corpus spans 7 domains (`software`, `ai`, `fintech`, `business`, `hardware`, `organization`, `meta`) and 5 outcome classes:

| Outcome Category | Cases | Reference RED Baseline Pass Rate | Reference GREEN Skill Pass Rate | Key Failure Mode Caught by Criteria |
|---|---:|---:|---:|---|
| **`eliminate`** (Contradiction Resolved) | 10 | 0 / 10 (0%) | **10 / 10 (100%)** | Prematurely sacrifices latency, durability, or security via naive middle-ground compromises |
| **`prove-limit`** (Irreducible Physical/Math Bound) | 4 | 0 / 4 (0%) | **4 / 4 (100%)** | Hallucinates impossible speedups/compression/energy (violating CAP, Amdahl's 1/s bound & 4-core baseline, Shannon entropy, or Li-ion energy density) |
| **`conditional`** (Jurisdiction-Dependent Legal Bound) | 1 | 0 / 1 (0%) | **1 / 1 (100%)** | Assumes deferred KYC is universally permitted without a jurisdiction gate or treats device/SIM telemetry as free without privacy/consent review |
| **`managed-tradeoff`** (User-Authorized Soft Target) | 1 | 0 / 1 (0%) | **1 / 1 (100%)** | Claims 100M keys fit in 16 MB at 0.01% FP (~19 bits/key holds only ~7–8M keys / ~4–5 min of traffic) without bounding the deduplication window |
| **`no-trigger`** (Scope Guardrail / Ordinary Task) | 4 | 0 / 4* | **4 / 4 (100%)** | Forces artificial TRIZ passports onto SQL lock-ordering bugs, CSS centering, meta-TRIZ history questions, or explicit weekend-prototype TTL choices |
| **Total Across All Outcomes** | **20** | **0 / 20** | **20 / 20 (100%)** | **105 paraphrase-tolerant criteria (`must` / `avoid`) validated** |

*\*Note on `no-trigger` reference RED scoring:* The reference RED baselines in `evals/cases.json` intentionally represent over-engineered TRIZ-jargon failures (which also trigger `hard_fail_patterns` in `evals/judge_criteria.json`).

---

## 4. Documented Failure Modes: Where `triz-universal` Does Not Help or Can Hurt

Honest engineering requires documenting where forcing TRIZ is counterproductive:

1. **Routine Bug Fixing & Lock-Ordering Deadlocks (`sql-deadlock-stacktrace-debug`):**
   - *How TRIZ hurts if misapplied:* If an agent treats a classic AB/BA mutex deadlock in application code as an "inventive contradiction" and proposes event-sourcing or striped counters instead of sorting lock acquisition order (`ORDER BY account_id`), it introduces massive accidental complexity.
   - *Mitigation in v3.1.0:* Explicit negative triggers in `SKILL.md` frontmatter, pruned `metadata.triggers`, Section 1 (`When NOT to Use This Skill`), and deterministic `hard_fail_patterns` in `evals/judge_criteria.json`.
2. **Simple Prototypes & Explicit Compromise Requests (`explicit-user-compromise-request-ru`):**
   - *How TRIZ hurts if misapplied:* When a developer building a weekend prototype explicitly asks whether to use a 10s or 60s TTL cache, refusing to answer and lecturing them on CDC/MVCC wastes time and tokens.
   - *Mitigation in v3.1.0:* Classified as `no-trigger` in both `evals/cases.json` and `evals/judge_criteria.json` (with `hard_fail_patterns` rejecting any TRIZ passport output).
3. **Jurisdiction-Dependent Regulatory Problems (`regulated-onboarding`):**
   - *How TRIZ hurts if misapplied:* Treating "defer KYC until withdrawal" as a universal Separation-in-Time triumph violates AML/CDD regimes that require identity verification before establishing a customer relationship, and treating device/SIM signals as "free VPR" ignores GDPR/ePrivacy consent rules.
   - *Mitigation in v3.1.0:* Classified as `conditional` outcome requiring a mandatory jurisdiction gate, legal sign-off on the state machine, and privacy review for telemetry.
4. **Reasoning Latency & Token Overhead on Trivial Tasks:**
   - Running the ARIZ-AI pipeline adds ~400–900 internal reasoning tokens and ~6.6k system prompt tokens. For straightforward CRUD or single-metric optimizations where no opposing constraint degrades, standard coding skills are faster and cheaper.
