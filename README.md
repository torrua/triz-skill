# triz-universal — AI Skill for Non-Compromising Inventive Problem Solving

[English](README.md) | [Русский](README.ru.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-67%20passed%2C%203%20skipped-brightgreen.svg)](#testing)
[![Platform](https://img.shields.io/badge/platform-Antigravity-blue.svg)](https://github.com/google-deepmind)

> **Core Axiom:** Seek an inventive resolution first; when a hard limit remains, state its evidence and consequences rather than inventing a guarantee.

## What is this?

An AI agent skill that applies **TRIZ (Теория Решения Изобретательских Задач)** — the Theory of Inventive Problem Solving — developed by Genrich Altshuller. It drives the agent through a 5-step **ARIZ-AI pipeline** to seek contradiction-eliminating designs, classify constraints, and distinguish evidence-backed conclusions from hypotheses.

## Key Features

| Feature | Description |
|---|---|
| 🚫 **Anti-Rationalization Guardrails** | Requires contradiction analysis before an unauthorized trade-off |
| ⚡ **ARIZ-AI 5-Step Pipeline** | IFR → Physical Contradiction → VPR Audit → 7 Resolution Strategies → Verification |
| 🔬 **7 Resolution Strategies** | 4 Separation Operators + Satisfy, Bypass, Alternative System (Litvin + Zlotin/Zusman) |
| 🧭 **Diagnostic Questions** | Zlotin/Zusman navigation: WHERE? WHEN? CONDITION? → instant strategy selection |
| 📊 **Curated Lookup** | 39 parameters mapped to software/AI/business + 30 candidate principle pairs |
| 📚 **22 Reference Modules (3 Tiers)** | Progressive context disclosure (Tier 1-2-3) — zero context bloat |
| 🧬 **Deep ARIZ-85-V Protocols (Tier-3)** | Deterministic algorithms: Full 9-part ARIZ-85-V, MMC, Step Back, Table 2, Trimming, AFD |
| 🌐 **Multi-Domain** | Software, AI/LLM, Business/Fintech, Physics, Organizations |
| 🗺️ **Perception Mapping** | Business TRIZ for organizational contradictions and stakeholder conflicts |
| ⚖️ **Escape Valve** | Honest handling of irreducible constraints (CAP, Amdahl, thermodynamics) |
| 🎯 **Dual-Loop & Three Modes** | Autonomous with Progressive Disclosure (Layer 1 plain default / Layer 2 deep passport), Semi-Automatic, Socratic |
| 🇷🇺 **Bilingual (EN / RU)** | Canonical Altshuller Russian terminology, bilingual triggers, localized template |
| 🔍 **Evidence & Risk Traceability** | Output records confidence, validation plan, and residual risks |
| 📝 **Evaluation Assets** | Reference problems plus blind expert-review cases |
| ✅ **Portable Validation** | Source checks run locally; deployment parity is an explicit release check |

## Architecture

The skill follows a 3-tier progressive disclosure model (Tier-1 $\to$ Tier-2 $\to$ Tier-3):

```
triz-universal/
├── SKILL.md                           ← Tier-1: Lightweight dispatcher (~215 lines)
└── references/                        ← Tier-2: Reference modules (on demand)
    ├── README.md                      Navigation index across all tiers
    ├── 01-ikr-ideality.md             Ideal Final Result & Ideality
    ├── 02-contradictions.md           Technical → Physical Contradiction
    ├── 03-separation-principles.md    7 Resolution Strategies (Litvin + Zlotin/Zusman)
    ├── 04-ariz-lite-algorithm.md      ARIZ-AI detailed walkthrough
    ├── 05-40-principles-catalog.md    40 Inventive Principles (Software + Business)
    ├── 06-system-operator-9screens.md 9-Screen System Operator
    ├── 07-resource-audit-vpr.md       VPR Resource Audit catalog
    ├── 08-multi-domain-lenses.md      Cross-domain mapping + OTSM-TRIZ
    ├── 09-su-field-and-standards.md   Su-Field Analysis & 76 Standards
    ├── 10-testing-scenarios.md        5 RED/GREEN pressure benchmarks
    ├── 11-contradiction-matrix.md     Curated 39-parameter lookup
    ├── 12-evaluation-suite.md         5 reference problems with scoring
    ├── 13-perception-mapping.md       Business TRIZ for organizations
    ├── SOURCES.md                      Provenance policy
    ├── CLAIMS.md                       Claim register and evidence levels
    └── ariz-deep/                     ← Tier-3: Deep Algorithmic Protocols (Level 4–5)
        ├── 01a-ariz-85v-analysis.md   ARIZ-85-V Parts 1–4: De-specialization, Article-Tool, OT/OZ, Micro-PC
        ├── 01b-ariz-85v-resolution.md ARIZ-85-V Parts 5–9: Information fund, Deadlock breakout, Verification, Reflection
        ├── 02-mmc-operator-protocol.md Modeling with Little People (MMC) role-prompting algorithm
        ├── 03-step-back-from-ifr.md    Step Back from IFR: Synthesis of assembly, deployment, cold start
        ├── 04-physical-contradiction-tree.md Table 2 Decision Tree: Particle rules 8–10, Phase shifts, Vacuum
        ├── 05-trimming-algorithm.md    Functional Trimming Protocol: Rules A, B, and C
        └── 06-subversion-analysis-afd.md Anticipatory Failure Determination (AFD / Subversion analysis)
```

**Why a 3-tier architecture?** Loading all TRIZ theory into context at once wastes tokens and causes "lost in the middle" degradation. The dispatcher `SKILL.md` is always loaded in working memory. Reference modules (Tier-2) are fetched for standard tasks, while deep protocols (Tier-3) are consulted only for Level 4–5 deadlocks, deep microscopic modeling, or adversarial verification.

## Installation

### For Antigravity (Google Gemini)

Copy to your global skills directory:

```bash
# Linux / macOS
cp -r triz-universal/ ~/.gemini/config/skills/triz-universal/

# Windows (PowerShell)
Copy-Item -Recurse triz-universal\ "$env:USERPROFILE\.gemini\config\skills\triz-universal\"
```

### For other AI agent frameworks

The skill is a set of Markdown files. Copy `triz-universal/` into your agent's skill/prompt directory and configure triggers for keywords like `TRIZ`, `contradiction`, `trade-off`, `bottleneck`, `deadlock`.

## How It Works

When you present the agent with a problem like:

> *"Our API needs sub-10ms latency AND full ACID consistency for analytics queries"*

Instead of saying *"Let's find a reasonable balance..."*, the TRIZ skill forces the agent to:

1. **Classify constraints** — distinguish non-negotiable invariants from targets and assumptions.
2. **Frame the IFR** — use the ideal result as a search direction, not an unsupported promise.
3. **Sharpen the Physical Contradiction** — "The data access path must be lock-free for reads AND locked for the inventory invariant."
4. **Audit resources (VPR)** — assess availability, cost, permissions, and reliability of page cache, WAL, and idle CPU.
5. **Apply Separation** — create a design, then state its consistency, cost, and operational implications.
6. **Verify** — define baseline, measurable thresholds, evidence, and residual risks.

## Testing

Run the portable source test suite:

```bash
python tests/test_triz_skill.py
```

Tests cover:
- YAML metadata and standards compliance
- Reference file integrity and cross-links
- Anti-rationalization guardrails
- ARIZ-AI pipeline formulation
- All 12 audit fixes verification
- RED/GREEN pressure benchmark evaluation
- constraint classification, evidence, verification, and risk reporting
- provenance and claim registers
- behavioral-evaluation assets distinct from phrase-based linting

To check or synchronize an installed copy, provide its explicit destination:

```powershell
.\scripts\sync-deployment.ps1 -Mode Check -Destination "C:\path\to\triz-universal"
.\scripts\sync-deployment.ps1 -Mode Apply -Destination "C:\path\to\triz-universal"
```

## Roadmap

### v1.0.0
- ✅ ARIZ-AI 5-step pipeline
- ✅ Anti-compromise guardrails with Red Flags
- ✅ 10 reference modules covering core TRIZ
- ✅ 5 multi-domain pressure benchmarks (RED/GREEN)
- ✅ 39 automated tests
- ✅ Escape valve for irreducible constraints

### v3.0.0 (Current Release)
- ✅ **Dual-Loop Execution:** Strict separation between internal methodological reasoning (always 100% TRIZ under the hood) and external user-facing delivery
- ✅ **Progressive Disclosure Architecture:** Layer 1 Plain-Language Core by default (solution-first, zero TRIZ jargon, intuitive analogies) + Layer 2 Professional TRIZ Passport
- ✅ **Contextual Follow-Up & Routing Guardrails:** Contextual closing invitation with format exceptions (JSON/code/minimal), preventing false triggers on meta-mentions of "TRIZ"
- ✅ **Hardened Tier-3 Canonical Protocols:** Restructured ARIZ-85-V Parts 1-4 with canonical MMC, Step Back from IFR, and Table 2 cross-references
- ✅ **70 Automated Unit Tests:** 67 passed, 3 skipped, full verification across all tiers and output layers

### v2.2.0
- ✅ **Tier-3 Deep Algorithmic Protocols:** 7 dedicated executable step-by-step protocols in `references/ariz-deep/` (ARIZ-85-V Parts 1-9, MMC Operator, Step Back from IFR, Table 2 Tree, Trimming, AFD)
- ✅ **3-Tier Context Architecture:** Tier-1 Dispatcher (<250 lines), Tier-2 Foundation Modules (15 files), Tier-3 Algorithmic Protocols (7 files)
- ✅ **Quick Decision Tree Routing:** Routing rows in SKILL.md for deep ARIZ-85-V deadlock resolution

### v2.1.0
- ✅ Curated, explicitly non-deterministic contradiction lookup
- ✅ Inventive principles mapped to each separation operator
- ✅ Evaluation suite with 5 reference solutions and pass/fail scoring
- ✅ Reasoning traceability — diagnostic path and principle selection logged in output
- ✅ Litvin + Zlotin/Zusman dual strategy sets (Satisfy, Bypass, Alternative System)
- ✅ Semi-automatic mode (between Autonomous and Socratic)
- ✅ Perception Mapping for organizational/people contradictions
- ✅ Constraint classification, provenance, and release synchronization

## Acknowledgments

- **Genrich Altshuller** — creator of TRIZ methodology
- **truinorva/triz-skills** — comprehensive Claude TRIZ skill library (inspiration for matrix lookups and dual strategy sets)
- **Heinrich: The Inventing Machine** — evaluation suite and traceability concepts
- **jenson500/triz-prompt-engineering (ccTOPP)** — XML prompt engineering for TRIZ

## License

[MIT](LICENSE)
