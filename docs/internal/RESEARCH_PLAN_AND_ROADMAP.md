# Master Research Plan & Roadmap: Universal TRIZ Skill for AI Agents

> **Status:** v3.0.0 implemented; source validation, token budget benchmarks, and trigger evaluation corpus complete; multi-model blind human evaluation protocol published in `evals/`.  
> **Methodology:** Classical & Modern TRIZ + Advanced Agent Skill Engineering (3-Tier Architecture)  
> **Directives Applied:** `/goal` (Goal Rigor), `/grill-me` (Stress-Testing Assumptions), `/boost` (Max Depth & Engineering Precision)

---

## Executive Summary

The objective of this project is to design, research, validate, and build a **Universal TRIZ (Theory of Inventive Problem Solving) Skill for AI Agents**.

Large Language Models (LLMs) are probabilistic sequence predictors. When confronted with difficult engineering, algorithmic, or architectural problems, LLMs often exhibit three failure modes:
1. **Premature Trade-off Bias:** Offering a middle-ground compromise before diagnosing whether the underlying contradiction can be eliminated. The skill seeks an inventive resolution first, while distinguishing a proven hard limit from an explicitly authorized soft-constraint trade-off.
2. **Psychological Inertia (Statistical Cliché Trapping):** Gravitating toward conventional solutions saturated in training data rather than exploring structural separations or existing system resources.
3. **Premature Solutionizing (Skipping the Contradiction):** Jumping straight from symptom to implementation without isolating the **Physical Contradiction** or defining the **Ideal Final Result (IFR / ИКР)**.

---

## 1. Goal Specification (`/goal`)

### 1.1 Primary Objective
Create an agent skill (`triz-universal`) that guides an LLM agent to:
1. Refuse premature, undisclosed compromises on hard constraints while supporting proven irreducible limits and explicitly authorized soft-constraint trade-offs.
2. Systematically sharpen a conflict through the contradiction pipeline:
   $$\text{Administrative Contradiction (AC)} \longrightarrow \text{Technical Contradiction (TC)} \longrightarrow \text{Physical Contradiction (PC)}$$
3. Formulate the **Ideal Final Result (IFR / ИКР)** as a search direction, then assess whether existing resources (VPR) are available, lawful, reliable, and cost-effective within the stated boundary.
4. Resolve the Physical Contradiction using the **7 Resolution Strategies** (Space, Time, Condition, Structure, Satisfy, Bypass, Alternative System).
5. Apply the **40 Inventive Principles** mapped across multiple domains (Software Engineering, AI Agents, Business Strategy, Physical/Hardware Engineering).
6. Verify that the resolution does not introduce secondary harmful effects (System Operator / 9 Screens) and clearly report evidence levels and verification status.

### 1.2 Target Form Factor & Architecture
- **Skill Architecture:** **3-Tier Progressive Disclosure** adhering to Agent Skill Guidelines.
- **Tier-1 Entry Point:** `triz-universal/SKILL.md` (<300 lines) containing:
  - Bilingual (EN/RU) positive and negative trigger rules in `description`.
  - Anti-rationalization guardrails, constraint classification, and `When NOT to Use` scope filter.
  - 5-step ARIZ-AI execution protocol and 3-pass Escape Valve.
  - Dual-Loop Progressive Disclosure templates (Layer 1 Plain-Language Core + Layer 2 TRIZ Passport).
  - Decision tree routing to Tier-2 and Tier-3 sub-modules.
- **Tier-2 Foundation References (`triz-universal/references/`):** Modular domain, matrix, resource, and provenance files loaded on demand.
- **Tier-3 Deep Protocols (`triz-universal/references/ariz-deep/`):** Full ARIZ-85-V, MMC, Step Back from IFR, Table 2, Trimming, and AFD protocols.

### 1.3 Definition of Done (DoD)
- [x] Algorithmic AI workflow formulated (ARIZ-AI) that fits within agent token budgets.
- [x] Constraint classification, evidence, verification, and residual-risk contract added.
- [x] Source, claim, source-only test, CI workflow, and cross-platform release-sync infrastructure added.
- [x] Complete the canonical source dossier (`SOURCES.md` and `CLAIMS.md`) with exact editions/pages and clean-room provenance notice.
- [x] Publish expanded evaluation corpus (`evals/cases.json`, `evals/trigger_corpus.json`), automated evaluation runner (`evals/run_evals.py`), and token/trigger benchmark report (`evals/BENCHMARK_REPORT.md`).

---

## 2. Deliverable Repository Structure

```text
triz-skill/
├── README.md                                   # Primary English documentation & showcase
├── README.ru.md                                # Primary Russian documentation & showcase
├── CHANGELOG.md                                # Keep a Changelog release history
├── VERSION                                     # Single source of truth for semantic version (3.0.0)
├── LICENSE                                     # MIT License
├── CONTRIBUTING.md                             # Contribution & evaluation guidelines
├── SECURITY.md                                 # Security policy & prompt-injection threat model
├── CITATION.cff                                # Academic & repository citation metadata
├── triz-universal/                             # Production skill package
│   ├── SKILL.md                                # Tier-1 dispatcher (<300 lines)
│   └── references/                             # Tier-2 reference modules (13 modules)
│       ├── README.md                           # Navigation index across all tiers
│       ├── 01-ikr-ideality.md                  # IFR formulas, ideality calculus, zero-cost rules
│       ├── 02-contradictions.md                # AC -> TC -> PC sharpening mechanics
│       ├── 03-separation-principles.md         # 7 resolution strategies & diagnostic navigation
│       ├── 04-ariz-lite-algorithm.md           # Full ARIZ-AI protocol with multi-domain case studies
│       ├── 05-40-principles-catalog.md         # 40 principles mapped across software/business/hardware
│       ├── 06-system-operator-9screens.md      # 9-screen schema, supersystem & anti-system audit
│       ├── 07-resource-audit-vpr.md            # Substance-Field & latent resource discovery
│       ├── 08-multi-domain-lenses.md           # Multi-domain lenses & OTSM-TRIZ ENV model
│       ├── 09-su-field-and-standards.md        # Su-Field analysis & 76 Standard Solutions
│       ├── 11-contradiction-matrix.md          # Curated non-deterministic 39-parameter lookup
│       ├── 13-perception-mapping.md            # Organizational & stakeholder contradiction mapping
│       ├── SOURCES.md                          # Canonical bibliography with editions/pages & provenance
│       ├── CLAIMS.md                           # Claim register & confidence levels
│       └── ariz-deep/                          # Tier-3 deep algorithmic protocols (7 modules)
├── evals/
│   ├── cases.json                              # 20 structured evaluation cases (eliminate/limit/tradeoff/no-trigger)
│   ├── trigger_corpus.json                     # 40 positive & negative bilingual trigger test prompts
│   ├── 10-testing-scenarios.md                 # 5 pressure verification benchmarks (quarantined outside skill)
│   ├── 12-evaluation-suite.md                  # 5 reference problems with scoring rubric (quarantined outside skill)
│   ├── run_evals.py                            # Automated token budget, trigger, and rubric validator
│   ├── BENCHMARK_REPORT.md                     # Published token, trigger, and baseline evaluation metrics
│   └── README.md                               # Blinded evaluation & expert review protocol
├── scripts/
│   ├── sync_deployment.py                      # Cross-platform installer, parity checker & zip packager
│   ├── sync-deployment.ps1                     # PowerShell deployment parity helper
│   └── github-actions-ci.yml                   # Cross-platform GitHub Actions CI & release zip workflow
├── tests/
│   └── test_triz_skill.py                      # Portable automated test suite
└── docs/
    └── internal/
        ├── RESEARCH_PLAN_AND_ROADMAP.md        # Architecture & research roadmap
        └── GRILL_ME_AND_GOAL_AUDIT.md          # Red-team design stress test
```
