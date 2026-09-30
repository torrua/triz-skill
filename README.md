# triz-universal — AI Skill for Non-Compromising Inventive Problem Solving

[English](README.md) | [Русский](README.ru.md)

[![CI & Release Verification](https://github.com/torrua/triz-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/torrua/triz-skill/actions/workflows/ci.yml)
[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platforms](https://img.shields.io/badge/platforms-Antigravity%20%7C%20Claude%20Code%20%7C%20Claude.ai%20%7C%20Cursor%20%7C%20Codex-blueviolet.svg)](#installation)

> **Core Axiom:** First seek an inventive resolution that improves Parameter $A$ without degrading Parameter $B$. When a hard physical, mathematical, legal, budgetary, or contractual limit remains, state its evidence and consequences rather than inventing a guarantee.

## What is this?

An AI agent skill that applies **TRIZ (Теория Решения Изобретательских Задач)** — the Theory of Inventive Problem Solving — created by Genrich Altshuller, extended with modern TRIZ heuristics (Zlotin/Zusman, Litvin/Gerasimov, OTSM-TRIZ). It guides the agent through a 5-step **ARIZ-AI pipeline** to eliminate contradictions using existing system resources, classify constraints (`Hard`, `Soft`, `Assumptions`), and separate proven facts from hypotheses.

## Key Features

| Feature | Description |
|---|---|
| 🚫 **Anti-Rationalization & Scope Guardrails** | Intercepts premature compromises on hard constraints while preventing false triggers on routine bug fixes or DB deadlocks |
| ⚡ **ARIZ-AI Pipeline (`Step 0` → `Step 5`)** | Constraint & Known-Limit Pre-Check → IFR → Physical Contradiction → VPR Audit → 7 Resolution Strategies → Verification |
| 🔬 **7 Resolution Strategies** | 4 Separation Operators + Satisfy, Bypass, Alternative System (Litvin + Zlotin/Zusman) |
| 🧭 **7 Diagnostic Questions** | Zlotin/Zusman + Litvin navigation across Space, Time, Condition, Structure, Satisfy, Bypass, and Alternative System |
| 📊 **Curated Non-Deterministic Lookup** | 39 parameters mapped to software/AI/business + 30 candidate principle pairs |
| 📚 **20 Reference Modules (3 Tiers)** | Progressive context disclosure (Tier 1-2-3) — **84–88% token savings** vs. monolithic loading ([Benchmark Report](evals/BENCHMARK_REPORT.md)) |
| 🧬 **Deep ARIZ-85-V Protocols (Tier-3)** | Step-by-step protocols: Full 9-part ARIZ-85-V, MMC, Step Back from IFR, Table 2, Trimming, AFD |
| 🌐 **Multi-Domain** | Software Engineering, AI/LLM Agents, Business/Fintech, Physical/Hardware, Organizations |
| ⚖️ **3-Pass Escape Valve** | Honest handling of irreducible limits across physical laws, mathematical bounds (CAP, Amdahl, Shannon), and legal/budgetary ceilings |
| 🎯 **Dual-Loop & Three Modes** | Autonomous with Progressive Disclosure (Layer 1 plain default / Layer 2 deep passport), Semi-Automatic (with non-interactive fallback), Socratic |
| 🇷🇺 **Bilingual (EN / RU)** | Language Adaptation Directive, bilingual frontmatter triggers, canonical Altshuller Russian terminology |
| 🔍 **Evidence & Risk Traceability** | Output records constraint classes, outcome type, confidence (`Established`, `Pattern`, `Hypothesis`), verification plan, residual risks, and explicit `UNVERIFIED` vs. `MEASURED` status |
| 📝 **Evaluation & Trigger Corpus** | 20 multi-outcome cases (`evals/cases.json`) + 40 bilingual trigger prompts (`evals/trigger_corpus.json`) + quarantined benchmark suites (`evals/10-testing-scenarios.md`, `evals/12-evaluation-suite.md`) + automated runner (`evals/run_evals.py`) |
| ✅ **Cross-Platform Tooling & CI** | Zero-dependency Python & PowerShell installers, SHA-256 parity verification, zip packager, and GitHub Actions CI template |

## Architecture & Context Token Budget

The skill follows a 3-tier progressive disclosure model (Tier-1 $\to$ Tier-2 $\to$ Tier-3), with all evaluation benchmarks quarantined outside `triz-universal/` in `evals/`:

```text
triz-universal/
├── SKILL.md                           ← Tier-1: Always-loaded dispatcher (250 lines, ~6.5k tokens)
└── references/                        ← Tier-2: Foundation modules (loaded on demand, ~2.1k tokens avg)
    ├── README.md                      Navigation index across all tiers
    ├── 01-ikr-ideality.md             Ideal Final Result & Ideality
    ├── 02-contradictions.md           Technical → Physical Contradiction
    ├── 03-separation-principles.md    7 Resolution Strategies (Litvin + Zlotin/Zusman)
    ├── 04-ariz-lite-algorithm.md      ARIZ-AI detailed walkthrough
    ├── 05-40-principles-catalog.md    40 Inventive Principles (Software + Business + Russian names)
    ├── 06-system-operator-9screens.md 9-Screen System Operator
    ├── 07-resource-audit-vpr.md       VPR Resource Audit catalog
    ├── 08-multi-domain-lenses.md      Cross-domain mapping + OTSM-TRIZ ENV model
    ├── 09-su-field-and-standards.md   Su-Field Analysis & 76 Standards
    ├── 11-contradiction-matrix.md     Curated non-deterministic 39-parameter lookup
    ├── 13-perception-mapping.md       Business TRIZ for organizations
    ├── SOURCES.md                     Canonical bibliography (editions/pages) & provenance policy
    ├── CLAIMS.md                      Claim register and confidence levels
    └── ariz-deep/                     ← Tier-3: Deep Algorithmic Protocols (~3.1k tokens avg)
        ├── 01a-ariz-85v-analysis.md   ARIZ-85-V Parts 1–4: De-specialization, Article-Tool, OT/OZ, Micro-PC
        ├── 01b-ariz-85v-resolution.md ARIZ-85-V Parts 5–9: Information fund, Deadlock breakout, Verification
        ├── 02-mmc-operator-protocol.md Modeling with Little People (MMC) role-prompting algorithm
        ├── 03-step-back-from-ifr.md   Step Back from IFR: Synthesis of deployment & cold start
        ├── 04-physical-contradiction-tree.md Table 2 Decision Tree: Particle rules 8–10, Phase shifts, Void
        ├── 05-trimming-algorithm.md   Functional Trimming Protocol: Rules A, B, and C
        └── 06-subversion-analysis-afd.md Anticipatory Failure Determination (AFD / Subversion analysis)
```

| Layer | Files | Lines | Estimated Tokens | Typical Turn Usage |
|---|---:|---:|---:|---|
| **Tier-1 (`SKILL.md`)** | 1 | 251 | ~6,622 | Always loaded in active skill context (**88.1% smaller** than full corpus) |
| **Tier-2 (`references/*.md`)** | 13 | 1,262 | ~26,954 | 0–1 module loaded on demand (~2,073 tokens/module) |
| **Tier-3 (`references/ariz-deep/*.md`)** | 7 | 824 | ~21,985 | Loaded only for Level 4–5 deadlocks (~3,141 tokens/module) |

See [evals/BENCHMARK_REPORT.md](evals/BENCHMARK_REPORT.md) for full token and trigger measurements.

## Installation

### 1. Cross-Platform Installer (Recommended — Python 3.10+)

Install directly into your target agent's global skill directory and verify SHA-256 parity:

```bash
# Google Antigravity (~/.gemini/config/skills/triz-universal)
python scripts/sync_deployment.py --mode apply --platform antigravity

# Claude Code (~/.claude/skills/triz-universal)
python scripts/sync_deployment.py --mode apply --platform claude-code

# Cursor (~/.cursor/skills/triz-universal)
python scripts/sync_deployment.py --mode apply --platform cursor

# OpenAI Codex CLI (~/.codex/skills/triz-universal)
python scripts/sync_deployment.py --mode apply --platform codex

# Custom or project-local path (e.g., .claude/skills/triz-universal)
python scripts/sync_deployment.py --mode apply --destination "/path/to/.claude/skills/triz-universal"
```

### 2. Claude.ai (Web & Desktop App)

Build the single-file skill archive and upload `dist/triz-universal-v3.0.0.zip` in **Claude.ai → Settings → Capabilities / Skills**:

```bash
python scripts/sync_deployment.py --package-zip
```

### 3. Manual Copy / PowerShell

```bash
# Linux / macOS (Antigravity or Claude Code)
cp -r triz-universal/ ~/.gemini/config/skills/triz-universal/
cp -r triz-universal/ ~/.claude/skills/triz-universal/

# Windows (PowerShell)
.\scripts\sync-deployment.ps1 -Mode Apply -Destination "$env:USERPROFILE\.gemini\config\skills\triz-universal"
```

## Example: Before vs. After (Layer 1 & Layer 2)

**Prompt:**
> *"Our C++ trading core has a strict `<5 µs` order execution budget. Regulators demand logging every internal state transition, but writing logs to NVMe disk takes `45 µs`. How do we design this?"*

### ❌ Without Skill (Typical LLM Compromise)
> *"Since disk writes take 45 µs and your budget is 5 µs, a trade-off is unavoidable. A reasonable compromise is to sample 1% of orders for logging, or buffer logs in standard heap memory and flush every 5 seconds, accepting a slight compliance risk."*

### ✅ With `triz-universal` — Layer 1 (Default Plain-Language Output)
> **Solution (Decouple Memory Capture from Disk Flush):**
> Instead of formatting and writing logs to disk on the trading thread, have the trading thread write a fixed 64-byte binary struct into a pre-allocated, lock-free shared-memory ring buffer (`mmap` / `io_uring`) using a single atomic pointer increment (`~10–30 ns`). Pin a separate background worker thread to an isolated CPU core that continuously drains the ring buffer to NVMe disk outside the critical trading path.
>
> **Assumptions, Residual Limits & Verification:**
> - *Assumptions & Limits:* Assumes an isolated CPU core is available. If server power fails instantaneously before the background thread flushes the ring buffer, the last few milliseconds of in-flight records can be lost unless backed by NVRAM/UPS.
> - *How to verify:* Benchmark p99.9 order path latency under peak burst load (`<5 µs` target) and verify ring-buffer sizing prevents overflow during NVMe GC pauses.
>
> *“Would you like a detailed breakdown of how the TRIZ algorithm arrived at this solution (including the contradiction, resources, and inventive principles used)?”*

### ✅ With `triz-universal` — Layer 2 (Professional TRIZ Passport, on request)
```markdown
### 💡 TRIZ Inventive Resolution
- **Constraint Classification:** Hard: [<5 µs hot-path budget, 100% state-transition logging] | Soft: [Disk flush immediacy] | Assumptions: [Isolated CPU core available for background worker]
- **Outcome Type:** Contradiction Eliminated
- **Physical Contradiction:** Telemetry I/O must occur synchronously on every state change (to satisfy regulatory completeness) AND must NOT occur on the order thread (to preserve the <5 µs latency ceiling).
- **Diagnostic Path:** WHEN / STRUCTURE
- **Strategy Applied:** Separation in Time & Structure
- **Inventive Principle(s) Used:** Principle #10 (Preliminary Action — pre-allocated ring buffer), Principle #24 (Intermediary — shared-memory ring buffer between hot thread and kernel/NVMe)
- **Resource Mobilized (VPR):** Idle isolated CPU core, OS shared-memory page mapping (`mmap` / `io_uring`), 64-byte CPU cache line alignment
- **Resolution:** Hot thread writes a raw 64-byte struct to a lock-free ring buffer in ~20 ns; a dedicated background core flushes pages to NVMe asynchronously.
- **Evidence & Confidence:** Pattern (`C-IOURING-01` in CLAIMS.md) — well-established low-latency architecture; exact p99.9 depends on hardware and kernel tuning.
- **Verification Plan:** Baseline: 45 µs synchronous write. Experiment: replay 1M orders/sec peak burst on isolated cores. Threshold: p99.9 hot-path overhead < 100 ns, zero dropped ring-buffer frames. Suggested verification role: Systems Performance Engineer.
- **Residual Risks:** Unflushed ring-buffer tail on catastrophic power loss (mitigate via battery-backed NVRAM or synchronous replication before external ACK).
- **Expected Outcome & Verification Status:** Status: UNVERIFIED (conditional expected outcome: <100 ns hot-path impact with 100% state-transition capture under stated hardware assumptions).
```

## When NOT to Use & Limitations

`triz-universal` is a specialized contradiction-resolution framework, **not** a general-purpose coding assistant.

### When NOT to Use
- **Routine Bugs & Lock-Ordering Deadlocks:** If PostgreSQL throws `deadlock detected` because Transaction A locks Row 1 then Row 2 while Transaction B locks Row 2 then Row 1, fix the lock acquisition order (`ORDER BY id`). Do not invent a new architecture.
- **Single-Metric Profiling Bottlenecks:** Optimizing an $O(N^2)$ loop or adding a missing SQL index involves no opposing constraint degradation.
- **Simple Prototypes & Explicit Trade-Offs:** When a user explicitly wants a quick 30-second TTL cache for a weekend prototype, forcing a zero-compromise architecture is over-engineering.
- **Meta-Questions:** Asking *"What is TRIZ?"* or linting a TRIZ file will not trigger a contradiction passport.

### Known Limitations
1. **Token & Latency Overhead:** Loading `SKILL.md` adds ~6.5k tokens to the system context, and running the ARIZ-AI loop adds ~400–900 reasoning tokens.
2. **Not a Substitute for Empirical or Legal Validation:** An LLM cannot measure latency, prove hardware thermal limits, or grant GDPR/KYC regulatory approval. All outputs default to `Status: UNVERIFIED` until validated by domain engineers or legal counsel.
3. **Stochastic Model Compliance:** While `evals/run_evals.py` runs an offline self-test of the reference corpus and routing rules, evaluating live LLM checkpoints (`baseline` vs. `skill`) uses `evals/live_eval.py` + `evals/judge_criteria.json` (105 paraphrase-tolerant criteria, blinded multi-judge scoring, Wilson 95% CIs, and exact McNemar sign tests). See [evals/README.md](evals/README.md) and [evals/BENCHMARK_REPORT.md](evals/BENCHMARK_REPORT.md).

## Testing & Evaluation

Run the portable test suite, offline self-test, and live-eval criteria validator (requires only Python 3.10+ standard library):

```bash
# 1. Run structural, version-parity, security, and live-eval workflow unit tests
python tests/test_triz_skill.py

# 2. Run token budget, 40-prompt trigger accuracy, and 20-case offline self-tests
python evals/run_evals.py

# 3. Validate the 105 paraphrase-tolerant live-eval judge criteria
python evals/live_eval.py validate-criteria
```

> **Note on Active Deployment Tests (`TRIZ_DEPLOY_DIR`):** `tests/test_triz_skill.py` includes 3 deployment-parity tests in `TestActiveDeployment` that compare the repository source against an installed copy via SHA-256. When running source tests without `TRIZ_DEPLOY_DIR` set, those 3 tests are skipped by design. Set `TRIZ_DEPLOY_DIR` (as CI does automatically) to run all tests with 0 skipped:
> ```bash
> TRIZ_DEPLOY_DIR=~/.gemini/config/skills/triz-universal python tests/test_triz_skill.py
> ```

## Release History

See [CHANGELOG.md](CHANGELOG.md) for the full release history (`v1.0.0` → `v3.0.0`).

### v3.0.0 (Current Release)
- ✅ **Dual-Loop Progressive Disclosure:** Layer 1 Plain-Language Core (covering all valid outcomes: contradiction eliminated, proven/conditional limit, or authorized soft trade-off) + Layer 2 Professional TRIZ Passport
- ✅ **Hardened Guardrails & Escape Valve:** Bilingual positive/negative triggers in `description`, `When NOT to Use` scope filter, 3-pass Escape Valve distinguishing physical laws, mathematical bounds (CAP, Amdahl, Shannon), and legal/budgetary limits
- ✅ **Canonical Sources & Claims:** Exact editions and page ranges in `SOURCES.md`, clean-room notice, and 10 formal claims in `CLAIMS.md`
- ✅ **Live-Eval Multi-Judge Harness & Trigger Suite:** 20 multi-domain cases (`evals/cases.json`), 105 paraphrase-tolerant criteria (`evals/judge_criteria.json`), blinded multi-judge evaluator (`evals/live_eval.py` + `evals/judge_prompt.md`), 40 bilingual trigger prompts (`evals/trigger_corpus.json`), offline self-test (`evals/run_evals.py`), and [Benchmark Report](evals/BENCHMARK_REPORT.md)
- ✅ **Cross-Platform CI & Packaging:** CI template (`scripts/github-actions-ci.yml`), `scripts/sync_deployment.py`, `CONTRIBUTING.md`, `SECURITY.md`, and `CITATION.cff`

## Acknowledgments

- **Genrich Altshuller (Г. С. Альтшуллер)** — creator of TRIZ, ARIZ-85-V, and the 40 Inventive Principles
- **B. Zlotin, A. Zusman, S. Litvin, V. Gerasimov, N. Khomenko** — diagnostic questions, Satisfy/Bypass operators, Trimming, AFD, and OTSM-TRIZ ENV model
- **truinorva/triz-skills**, **Heinrich: The Inventing Machine**, and **jenson500/triz-prompt-engineering (ccTOPP)** — conceptual inspiration (all content in this repository is original clean-room work; see [SOURCES.md](triz-universal/references/SOURCES.md))

## License

[MIT](LICENSE)
