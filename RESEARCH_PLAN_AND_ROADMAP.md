# Master Research Plan & Roadmap: Universal TRIZ Skill for AI Agents

> **Status:** v2.1.0 implemented; source validation complete, independent expert evaluation pending.  
> **Methodology:** Classical & Modern TRIZ + Advanced Agent Skill Engineering (Tier-2 Architecture)  
> **Directives Applied:** `/goal` (Goal Rigor), `/grill-me` (Stress-Testing Assumptions), `/boost` (Max Depth & Engineering Precision)

---

## Executive Summary

The objective of this project is to design, research, validate, and build a **Universal TRIZ (Theory of Inventive Problem Solving) Skill for AI Agents**.

Large Language Models (LLMs) are inherently probabilistic sequence predictors. When confronted with difficult engineering, algorithmic, or architectural problems, LLMs suffer from three critical failure modes:
1. **Premature Trade-off Bias:** LLMs may offer a compromise before diagnosing the contradiction. The skill must seek an inventive resolution first, then distinguish a proven hard limit from an explicitly authorized trade-off.
2. **Psychological Inertia (Statistical Cliché Trapping):** LLMs gravitate toward high-probability tokens, which correspond to conventional, mainstream solutions already saturated in their training data. Breakthroughs require traversing orthogonal search spaces.
3. **Premature Solutionizing (Skipping the Contradiction):** LLMs jump straight from symptom to implementation code without isolating the **Physical Contradiction** or defining the **Ideal Final Result (IFR / ИКР)**, leading to bloated architectures and technical debt.

This master plan establishes the complete research cycle and execution roadmap to create a production-grade agent skill that transforms an LLM into a rigorous, non-compromising inventive problem solver.

---

## 1. Goal Specification (`/goal`)

### 1.1 Primary Objective
Create an agent skill (`triz-universal`) that forces any LLM agent to:
1. Refuse premature, undisclosed compromises while allowing proven limits and explicitly authorized trade-offs.
2. Systematically sharpen any vague problem through a 3-stage contradiction pipeline:
   $$\text{Administrative Contradiction (AC)} \longrightarrow \text{Technical Contradiction (TC)} \longrightarrow \text{Physical Contradiction (PC)}$$
3. Formulate the **Ideal Final Result (IFR / ИКР)** as a search direction, then assess whether resources are available, lawful, reliable, and truly cost-free within the stated boundary.
4. Resolve the Physical Contradiction using the **4 Classical Separation Principles** (Space, Time, Condition/Relation, Structure/System Transition).
5. Apply the **40 Inventive Principles** mapped across multiple domains (Software Engineering, Distributed Systems, Algorithms, Product/Process Architecture).
6. Verify that the resolution does not introduce secondary harmful effects (checking the System Operator / 9 Screens).

### 1.2 Target Form Factor & Architecture
- **Skill Tier:** **Tier 2 (Expanded Skill)** adhering to Agent Skill Guidelines.
- **Root Entry Point:** `SKILL.md` (<400 lines) containing:
  - Strict CSO (Claude/Context Search Optimization) triggers.
  - Decision tree routing to specific sub-modules.
  - Anti-rationalization table (countering LLM excuses to compromise).
  - Quick-start ARIZ-lite execution protocol.
- **Supporting References (`references/`):**
  - Modular deep-dive files loaded on demand to minimize context token overhead.

### 1.3 Definition of Done (DoD)
- [x] Algorithmic AI workflow formulated (ARIZ-AI) that fits within agent token budgets.
- [x] Constraint classification, evidence, verification, and residual-risk contract added.
- [x] Source, claim, source-only test, and release-sync infrastructure added.
- [ ] Complete the source dossier with exact editions/pages and external expert review.
- [ ] Run blinded model evaluations using `evals/cases.json` and publish results.

---

## 2. Research Phases & Milestones

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           RESEARCH & BUILD PHASES                           │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
      ┌────────────────────────────────┼────────────────────────────────┐
      ▼                                ▼                                ▼
[PHASE 1: Theory]              [PHASE 2: Alignment]             [PHASE 3: Skill Arch]
• Altshuller Classical TRIZ    • LLM Cognitive Obstacles        • Tier-2 Modularization
• Modern TRIZ (Mann, Zlotin)   • Compromise Prevention Engine   • CSO Trigger Engineering
• Software/System TRIZ         • Resource Auditing for Code     • Anti-Rationalization
      │                                │                                │
      └────────────────────────────────┼────────────────────────────────┘
                                       ▼
                         [PHASE 4: ARIZ-AI Engine]
                         • 5-Step Algorithmic Pipeline
                         • 4 Separation Heuristics
                         • 40 Principles Mapping
                                       │
                                       ▼
                       [PHASE 5: Testing & Stress-Test]
                       • Hard Pressure Scenarios (RED)
                       • Skill Deployment (GREEN)
                       • Edge Cases & Hardening (REFACTOR)
```

### Phase 1: TRIZ Theoretical Deep Dive (`research/01_triz_theoretical_foundations.md`)
- **Objective:** Exhaustive extraction of core invariant TRIZ mechanisms:
  - **Laws of Technical Systems Evolution (ZRTS):** Ideality increase, non-uniform development, transition to supersystem, transition from macro to micro, dynamization, rhythm synchronization.
  - **The Contradiction Continuum:**
    - Administrative: "Need to make database faster, don't know how."
    - Technical: "If we add an index (speed ↑), write throughput drops and disk storage expands (resource loss ↓)."
    - Physical: "The index must exist (to serve reads in O(log N)) and must NOT exist (to avoid overhead on writes)."
  - **The Ideal Final Result (IKR):**
    $$I = \frac{\sum F_{\text{useful}}}{\sum C_{\text{cost}} + \sum H_{\text{harm}}} \longrightarrow \infty$$
    - The Ideal Machine: "There is no machine, but its function is performed."
    - The Ideal Code: "There is no code, but the output is produced."
  - **ARIZ-85B Decomposition:** Analyzing the 9 parts of Altshuller's classical algorithm and isolating the high-leverage cognitive steps suitable for automated agents.
  - **Substance-Field (Su-Field / Веполь) & 76 Standards:** Modeling interactions as (S1, S2, F) and resolving deficient, harmful, or uncontrolled fields.
  - **System Operator (9 Screens / Многоэкранная схема):** Analyzing Subsystem, System, Supersystem across Past, Present, Future, plus Anti-Systems.

### Phase 2: TRIZ for AI & Software Systems (`research/02_triz_for_ai_and_software.md`)
- **Objective:** Bridge classical mechanical/physical TRIZ into digital, algorithmic, and AI contexts:
  - Translation of Altshuller's 39 parameters into computational parameters (Latency, Memory, Throughput, Concurrency Contention, Complexity, Maintainability, Security, Data Consistency, Network Bandwidth).
  - Mapping the 40 Inventive Principles to software engineering, cloud architecture, and algorithms (e.g., Principle 1 Segmentation → Sharding/Microservices; Principle 10 Preliminary Action → Prefetching/JIT; Principle 13 Inversion → IoC/Reactive Pull; Principle 25 Self-Service → Autonomous Self-Healing).
  - Translation of Su-Field Analysis into "Data-Process-Mechanism" triplets.
  - Mapping Substance-Field Resources (ВПР) to Computational Resources: Unused CPU idle cycles, cache lines, network payloads, metadata headers, DNS lookups, memory alignment padding, read-heavy replicas.

### Phase 3: Skill Engineering & Cognitive Mechanics (`research/03_skill_engineering_architecture.md`)
- **Objective:** Design the skill structure to ensure guaranteed triggering, low context overhead, and strict agent compliance:
  - **Context-Search Optimization (CSO):** Crafting triggers that activate when an agent encounters deadlock, architectural bottlenecks, intractable trade-offs, or complex optimization challenges.
  - **Progressive Disclosure:** Keeping `SKILL.md` under 400 lines while organizing deep knowledge in dedicated `references/` files loaded strictly on demand.
  - **Psychological Anti-Rationalization:** Countering the specific ways LLMs evade deep problem-solving (e.g., "A trade-off is good enough here", "I will just use a generic cache", "Let's ask the user to choose between speed and accuracy").

### Phase 4: ARIZ-AI Algorithmic Pipeline (`research/04_universal_skill_spec_and_ariz_ai.md`)
- **Objective:** Formalize a lightweight, 5-stage executable procedure for agents:
  1. **Step 1: Frame the Mini-Problem & IFR:** Formulate the system without introducing new complex entities. State the ideal outcome.
  2. **Step 2: Sharpen the Physical Contradiction:** Drive the problem to extreme, opposing physical/logical demands on a single operational zone and operational time:
     `Element X must be [P] to satisfy [R1] AND [not-P] to satisfy [R2]`
  3. **Step 3: Mobilize Resources (VPR Audit):** Scan internal, external, waste, and differential resources within the operational zone/time.
  4. **Step 4: Execute Separation / Transformation:**
     - Separate in Space (e.g., different nodes, cores, memory regions).
     - Separate in Time (e.g., pre-computation, off-peak processing, phase transitions).
     - Separate by Condition / Context (e.g., dynamic branching, state-dependent behavior).
     - Separate by Structure / System Transition (e.g., emergent property at supersystem or subsystem level).
  5. **Step 5: Secondary Harm Audit & Verification:** Ensure the solution does not create new bottleneck contradictions.

### Phase 5: Verification, Benchmarking & Stress-Testing
- **Objective:** Prove the skill's efficacy through RED-GREEN-REFACTOR testing:
  - Design 3 real-world, high-difficulty engineering paradoxes where standard LLMs fail (defaulting to lazy trade-offs).
  - Baseline Test (RED): Run LLM without the skill; document verbatim compromise rationalizations.
  - Implementation Test (GREEN): Run LLM with `triz-universal`; verify the agent refuses the trade-off and derives an inventive solution.
  - Refactor Test: Plug any newly discovered rationalization loopholes.

---

## 3. The Grill-Me Matrix (`/grill-me`)

To guarantee maximum robustness, the following fundamental tensions must be interrogated and stress-tested:

| # | Dilemma / Tension | The Skeptical Challenge | Proposed TRIZ Skill Resolution |
|---|-------------------|-------------------------|--------------------------------|
| **G1** | **Universality vs Specificity** | "If the skill is universal, it will output vague philosophy ('apply separation in time'). If it's specific, it's not universal." | Two-tier architecture: Universal core engine (ARIZ-AI + Contradictions + Separation) + Domain adapter lenses (Software, Hardware, Business). |
| **G2** | **Token Budget vs ARIZ Depth** | Full ARIZ-85B has 9 parts and ~40 steps. Injecting it will cause context saturation and instruction drift. | ARIZ-AI distilled into a 5-step strict pipeline, with sub-tools (40 Principles, Su-Field) loaded only as reference sub-skills. |
| **G3** | **The Premature Trade-off Bias of LLMs** | Models may settle on a compromise before testing inventive transformations or hard limits. | Constraint classification, separation search, evidence requirements, and explicit authorization for any remaining trade-off. |
| **G4** | **Verification in Non-Code Domains** | In code, solutions can be tested via `pytest`. In architectural or business problems, how do we know the solution works? | Falsifiability checklist: Did parameter A improve? Did parameter B stay invariant or improve? Did cost increase? If cost increased, reject. |
| **G5** | **Agent Autonomy vs Human Interaction** | Should the skill guide an autonomous background agent or act as a Socratic sparring partner for a human? | Dual operational mode: `Autonomous Mode` (agent solves and outputs synthesized solution) vs `Socratic Mode` (agent asks probing questions). |

---

## 4. Deliverable File Structure

```
c:\Users\User\Dropbox\Python\PRIZI\gemini-discussions\triz-skill\
├── RESEARCH_PLAN_AND_ROADMAP.md            # [Phase 0] Master Plan & Roadmap
├── GRILL_ME_AND_GOAL_AUDIT.md              # [Phase 0] Rigorous stress-test & critical interrogation
├── research/
│   ├── 01_triz_theoretical_foundations.md   # [Phase 1] Classical, Modern & OTSM-TRIZ, 76 Standards
│   ├── 02_triz_for_ai_and_software.md       # [Phase 2] TRIZ mapped to Software & AI agents
│   ├── 03_skill_engineering_architecture.md # [Phase 3] CSO, Anti-Rationalization & Tier-2 spec
│   └── 04_universal_skill_spec_and_ariz_ai.md # [Phase 4] Functional specification & ARIZ-AI
├── triz-universal/                         # [Phase 5] Production-grade skill package
│   ├── SKILL.md                            # Main entry point & dispatcher (<150 lines)
│   └── references/
│       ├── README.md                       # Sub-topic index and navigation guide
│       ├── 01-ikr-ideality.md              # IFR formulas, ideality calculus, zero-cost rules
│       ├── 02-contradictions.md            # AC -> TC -> PC sharpening mechanics
│       ├── 03-separation-principles.md     # 4 separation principles with multi-domain examples
│       ├── 04-ariz-lite-algorithm.md       # Full ARIZ-AI protocol with end-to-end case studies
│       ├── 05-40-principles-catalog.md     # 40 principles mapped across modern domains
│       ├── 06-system-operator-9screens.md  # 9-screen schema, supersystem & anti-system audit
│       ├── 07-resource-audit-vpr.md        # Substance-Field & latent resource discovery
│       ├── 08-multi-domain-lenses.md       # Multi-domain lenses (Software, AI, Business, Physical)
│       ├── 09-su-field-and-standards.md    # Su-Field analysis & 5 classes of standard solutions
│       └── 10-testing-scenarios.md         # 5 pressure verification benchmarks (RED vs GREEN)
│       ├── 11-contradiction-matrix.md      # Curated heuristic lookup
│       ├── 12-evaluation-suite.md          # Reference problems
│       ├── 13-perception-mapping.md        # Organizational contradictions
│       ├── SOURCES.md                       # Provenance policy
│       └── CLAIMS.md                        # Claim register
├── evals/
│   ├── cases.json                           # Blind-evaluation seed corpus
│   └── README.md                            # Expert review protocol
├── scripts/
│   └── sync-deployment.ps1                 # Explicit Check/Apply deployment parity
├── tests/
│   └── test_triz_skill.py                  # Automated test suite & pressure evaluation harness
└── [Deployed Location]:
    └── C:\Users\User\.gemini\config\skills\triz-universal\  # Active in Antigravity catalog
```
