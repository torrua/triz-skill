# triz-universal — AI Skill for Non-Compromising Inventive Problem Solving

[English](README.md) | [Русский](README.ru.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-local%20validation-blue.svg)](#testing)
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
| 📚 **15 Reference Modules** | Progressive context disclosure — loaded on demand, not all at once |
| 🌐 **Multi-Domain** | Software, AI/LLM, Business/Fintech, Physics, Organizations |
| 🗺️ **Perception Mapping** | Business TRIZ for organizational contradictions and stakeholder conflicts |
| ⚖️ **Escape Valve** | Honest handling of irreducible constraints (CAP, Amdahl, thermodynamics) |
| 🎯 **Three Modes** | Autonomous (default), Semi-Automatic, and Socratic (interactive) |
| 🇷🇺 **Bilingual (EN / RU)** | Canonical Altshuller Russian terminology, bilingual triggers, localized template |
| 🔍 **Evidence & Risk Traceability** | Output records confidence, validation plan, and residual risks |
| 📝 **Evaluation Assets** | Reference problems plus blind expert-review cases |
| ✅ **Portable Validation** | Source checks run locally; deployment parity is an explicit release check |

## Architecture

```
triz-universal/
├── SKILL.md                           ← Tier-1: Lightweight dispatcher
└── references/                        ← Tier-2: Deep knowledge (loaded on demand)
    ├── README.md                      Navigation index
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
    └── CLAIMS.md                       Claim register and evidence levels
```

**Why Tier-2?** Loading all TRIZ theory into context at once wastes tokens and causes "lost in the middle" degradation. The dispatcher `SKILL.md` is always loaded (~144 lines); reference modules are loaded **only when needed**.

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

### v2.1.0 (Current Release)
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
