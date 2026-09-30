# Changelog

All notable changes to `triz-universal` are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0] - 2026-09-29

### Added
- **Dual-Loop Execution Architecture:** Strict separation between Loop 1 (internal ARIZ-AI methodological reasoning starting at Step 0) and Loop 2 (user-facing progressive disclosure), with a Pre-Commitment Rule (Anti-Post-Hoc) and a compact `<triz_scratchpad>` fallback for non-thinking models and `[AUDIT]` / `--audit` evaluation runs.
- **Step 0 (Constraint Classification & Known-Limit Pre-Check):** Evaluates Hard/Soft/Assumption constraints, statutory/mathematical bounds (KYC, CAP, Shannon, thermodynamics), and budget-fitting standard components before running multi-pass ideation.
- **Progressive Disclosure Delivery (Layer 1 & Layer 2):**
  - *Layer 1 (Plain-Language Core, Default):* Solution-first, zero TRIZ jargon, supports all three valid outcomes (inventive elimination, proven irreducible limit, or user-authorized soft trade-off), mandatory 2–3 line assumptions/verification summary, and contextual closing invitation with format exceptions (JSON/YAML/code/compact).
  - *Layer 2 (Professional TRIZ Passport):* Includes explicit `Constraint Classification`, `Outcome Type` (including `Managed Trade-off`), and `Expected Outcome & Verification Status`.
- **Scope & Trigger Guardrails:** Explicit `When NOT to Use` section, negative trigger rules in `SKILL.md` frontmatter (`description`), and pruned `metadata.triggers` (removing generic words like `deadlock`, `bottleneck`, `trade-off`, `contradiction`) to prevent false activation.
- **Language Adaptation Directive & Non-Interactive Fallback:** Tier-1 rule requiring responses to match the user's prompt language alongside a single-turn / batch API fallback for `Semi-Automatic Mode`.
- **Canonical Source Bibliography & Expanded Claim Register:** Added exact editions, publishers, and page ranges to `references/SOURCES.md` (`TRIZ-ALT-79`, `TRIZ-ALT-86`, `TRIZ-ZZ-89`, `TRIZ-ZZ-01`, `TRIZ-LIT-91`, `TRIZ-OTSM-00`, `CS-CAP-02`, `CS-AMDAHL-67`) plus clean-room provenance notice and expanded `references/CLAIMS.md` (`C-CAP-01`, `C-AMDAHL-01`, `C-BLOOM-01`, `C-IOURING-01`, `C-RLHF-01`).
- **Expanded Evaluation & Trigger Corpus:** 20 multi-domain evaluation cases in `evals/cases.json` (covering `eliminate`, `prove-limit`, `managed-tradeoff`, and `no-trigger`), 40 bilingual trigger test prompts in `evals/trigger_corpus.json`, automated evaluation & token budget runner `evals/run_evals.py` (with `--responses-file` support for scoring external live LLM runs), and published `evals/BENCHMARK_REPORT.md`.
- **Cross-Platform Tooling, CI Template & Release Packaging:** Added CI workflow template `scripts/github-actions-ci.yml`, cross-platform `scripts/sync_deployment.py` (with `--package-zip` support for Claude.ai), `CONTRIBUTING.md`, `SECURITY.md`, and `CITATION.cff`.

### Changed
- **Broadened Escape Valve & Standard Solution Exception:** Distinguished physical laws, formal mathematical theorems with explicit model assumptions (CAP, Amdahl), and external legal/budgetary/contractual limits across 3 defined ARIZ-AI passes, and clarified that standard components fitting all hard constraints and budget are acceptable once disclosed.
- **Expected Outcome & Verification Status Labeling:** Renamed Layer 2 `Verified Outcome` / `Проверенный результат` to `Expected Outcome & Verification Status` / `Ожидаемый результат и статус проверки` (`Status: UNVERIFIED` by default unless empirical measurements were provided).
- **Physical Quarantine of Benchmark Assets:** Moved `10-testing-scenarios.md` and `12-evaluation-suite.md` out of `triz-universal/references/` into `evals/` (`evals/10-testing-scenarios.md` and `evals/12-evaluation-suite.md`) and removed all inline LaTeX (`$`) from `triz-universal/SKILL.md`.
- **Repository Hygiene:** Moved internal planning notes (`RESEARCH_PLAN_AND_ROADMAP.md`, `GRILL_ME_AND_GOAL_AUDIT.md`) to `docs/internal/` and removed all local workstation paths.

## [2.2.0] - 2026-09-28

### Added
- **Tier-3 Deep Algorithmic Protocols (`references/ariz-deep/`):** 7 step-by-step protocols for Level 4–5 contradictions:
  - `01a-ariz-85v-analysis.md` (ARIZ-85-V Parts 1–4: Mini-problem, Article-Tool, OT/OZ, Micro-PC, IKR-2, 6 rules)
  - `01b-ariz-85v-resolution.md` (ARIZ-85-V Parts 5–9: Information fund, Deadlock breakthrough, Verification, Reflection)
  - `02-mmc-operator-protocol.md` (Modeling with Little People role-prompting protocol)
  - `03-step-back-from-ifr.md` (Step Back from IFR for deployment, cold start, and zero-downtime migration)
  - `04-physical-contradiction-tree.md` (ARIZ Table 2 decision tree and particle rules)
  - `05-trimming-algorithm.md` (Functional Trimming Rules A, B, and C)
  - `06-subversion-analysis-afd.md` (Anticipatory Failure Determination / Subversion analysis)
- **3-Tier Context Architecture:** Tier-1 dispatcher (`SKILL.md`), Tier-2 foundation references, and Tier-3 deep protocols.

## [2.1.1] - 2026-09-27

### Added
- Canonical Russian language support: bilingual triggers, localized delivery template, and bilingual 40 Inventive Principles catalog with Altshuller's canonical Russian titles.
- Separate Russian documentation (`README.ru.md`) and `TestMultilingualRussianSupport` test suite.

## [2.1.0] - 2026-09-26

### Added
- Constraint classification (`Hard constraints`, `Soft constraints`, `Assumptions`), evidence levels, verification plans, and residual-risk reporting.
- Reframed the Ideal Final Result (IFR) as a search direction and added explicit irreducible-limit and authorized-trade-off outcomes.
- Qualified distributed-systems, storage, authentication, and KYC examples.
- Added provenance (`SOURCES.md`) and claim (`CLAIMS.md`) registers plus deployment synchronization script (`scripts/sync-deployment.ps1`).

## [2.0.0] - 2026-09-25

### Added
- 7 resolution strategies combining Litvin and Zlotin/Zusman (4 Separation Operators + Satisfy, Bypass, Alternative System) with diagnostic navigation questions.
- Curated non-deterministic contradiction lookup (`11-contradiction-matrix.md`), reference evaluation suite (`12-evaluation-suite.md`), and Perception Mapping (`13-perception-mapping.md`).
- Three operational modes: Autonomous, Semi-Automatic, and Socratic.

## [1.0.0] - 2026-09-24

### Added
- Initial release of `triz-universal`: 5-step ARIZ-AI pipeline, anti-rationalization guardrails, 10 reference modules, 5 RED/GREEN pressure benchmarks, and automated test suite.
