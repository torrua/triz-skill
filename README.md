# triz-universal — AI Skill for Non-Compromising Inventive Problem Solving

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-53%20passed-brightgreen.svg)](#testing)
[![Platform](https://img.shields.io/badge/platform-Antigravity-blue.svg)](https://github.com/google-deepmind)

> **Core Axiom:** A compromise is an admission of failure. A true inventive solution eliminates the contradiction so that Parameter A improves without Parameter B deteriorating.

## What is this?

An AI agent skill that enforces **TRIZ (Теория Решения Изобретательских Задач)** — the Theory of Inventive Problem Solving — developed by Genrich Altshuller. Instead of letting the AI propose trade-offs and "balanced middle-ground" solutions, this skill forces the agent through a rigorous 5-step **ARIZ-AI pipeline** that eliminates contradictions using only existing system resources.

## Key Features

| Feature | Description |
|---|---|
| 🚫 **Anti-Compromise Guardrails** | 5 rules + Red Flags that prevent the AI from proposing trade-offs |
| ⚡ **ARIZ-AI 5-Step Pipeline** | IFR → Physical Contradiction → VPR Audit → 7 Resolution Strategies → Verification |
| 🔬 **7 Resolution Strategies** | 4 Separation Operators + Satisfy, Bypass, Alternative System (Litvin + Zlotin/Zusman) |
| 🧭 **Diagnostic Questions** | Zlotin/Zusman navigation: WHERE? WHEN? CONDITION? → instant strategy selection |
| 📊 **Contradiction Matrix** | 39 parameters mapped to software/AI/business + top-30 lookup pairs |
| 📚 **13 Reference Modules** | Progressive context disclosure — loaded on demand, not all at once |
| 🌐 **Multi-Domain** | Software, AI/LLM, Business/Fintech, Physics, Organizations |
| 🗺️ **Perception Mapping** | Business TRIZ for organizational contradictions and stakeholder conflicts |
| ⚖️ **Escape Valve** | Honest handling of irreducible constraints (CAP, Amdahl, thermodynamics) |
| 🎯 **Three Modes** | Autonomous (default), Semi-Automatic, and Socratic (interactive) |
| 🔍 **Reasoning Traceability** | Output template logs which principle was chosen and WHY |
| 📝 **Evaluation Suite** | 5 reference problems with expected solutions and pass/fail scoring |
| ✅ **53 Automated Tests** | Structural validation + RED/GREEN pressure benchmarks + SHA-256 parity |

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
    ├── 11-contradiction-matrix.md     39 parameters + matrix lookup
    ├── 12-evaluation-suite.md         5 reference problems with scoring
    └── 13-perception-mapping.md       Business TRIZ for organizations
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

1. **Frame the IFR** — "The system itself, at zero cost, delivers both 10ms latency AND full ACID consistency"
2. **Sharpen the Physical Contradiction** — "The data must be in-memory (fast) AND on-disk (consistent)"
3. **Audit free resources (VPR)** — OS page cache, WAL logs, idle CPU cores
4. **Apply Separation** — e.g., Separation in Structure: hot data in memory-mapped files, cold data on disk
5. **Verify** — Parameter A improved? Parameter B unimpaired? No new dependencies?

## Testing

Run the full test suite (53 tests):

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
- SHA-256 parity between working and deployed copies
- **v2.0.0:** 7 strategies, diagnostic questions, contradiction matrix, evaluation suite, perception mapping, semi-automatic mode, reasoning traceability

## Roadmap

### v1.0.0
- ✅ ARIZ-AI 5-step pipeline
- ✅ Anti-compromise guardrails with Red Flags
- ✅ 10 reference modules covering core TRIZ
- ✅ 5 multi-domain pressure benchmarks (RED/GREEN)
- ✅ 39 automated tests
- ✅ Escape valve for irreducible constraints

### v2.0.0 (Current Release)
- ✅ CSV/YAML contradiction matrices (Altshuller 39×39 + Matrix 2003) for deterministic lookup
- ✅ Inventive principles mapped to each separation operator
- ✅ Evaluation suite with 5 reference solutions and pass/fail scoring
- ✅ Reasoning traceability — diagnostic path and principle selection logged in output
- ✅ Litvin + Zlotin/Zusman dual strategy sets (Satisfy, Bypass, Alternative System)
- ✅ Semi-automatic mode (between Autonomous and Socratic)
- ✅ Perception Mapping for organizational/people contradictions
- ✅ 53 automated tests

## Acknowledgments

- **Genrich Altshuller** — creator of TRIZ methodology
- **truinorva/triz-skills** — comprehensive Claude TRIZ skill library (inspiration for matrix lookups and dual strategy sets)
- **Heinrich: The Inventing Machine** — evaluation suite and traceability concepts
- **jenson500/triz-prompt-engineering (ccTOPP)** — XML prompt engineering for TRIZ

## License

[MIT](LICENSE)
