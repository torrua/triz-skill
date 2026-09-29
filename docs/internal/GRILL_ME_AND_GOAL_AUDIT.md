# /grill-me & /goal Audit: Stress-Testing the Universal TRIZ Skill

> **Role:** Red Team & Systems Architect  
> **Directives:** Rigorous questioning of assumptions, edge case exposure, non-negotiable quality criteria.

---

## Part 1: The `/goal` Definition & Success Invariants

### 1.1 The Core Mission
To engineer a **3-Tier Agent Skill** that enables an AI agent to execute non-compromising inventive problem solving on complex systems (software architecture, algorithmic bottlenecks, business dilemmas, hardware engineering) using Classical and Modern TRIZ, while honestly reporting proven limits and authorized soft-constraint trade-offs.

### 1.2 Quantitative & Qualitative Success Metrics (KPIs)

| Metric | Target | Failure Mode if Not Met |
|--------|--------|-------------------------|
| **Hard-Constraint Integrity** | 100% of solutions either resolve the Physical Contradiction, prove an irreducible limit with explicit assumptions, or request user authorization on a soft constraint. | Agent silently drops a hard constraint or invents an unsupported guarantee (FAIL). |
| **Resource Audit Discipline** | Proposed mechanisms prioritize existing in-boundary resources (VPR) and disclose costs/risks of any added component. | Agent claims external paid services, third-party APIs, or regulated user telemetry are "free" (FAIL). |
| **ARIZ-AI Pipeline Rigor** | Agent executes constraint classification, IFR, PC sharpening, VPR audit, and strategy selection before proposing a mechanism. | Agent jumps straight to generic brainstorming without isolating the contradiction (FAIL). |
| **Token Efficiency** | Root `SKILL.md` $< 300$ lines (~2.6k tokens); reference files modularized into $< 500$ lines each and loaded on demand. | Monolithic skill saturating the agent context window (FAIL). |
| **Trigger Precision & Recall** | Positive contradiction prompts in EN/RU activate the skill; routine debugging, SQL lock stack traces, and meta-mentions of "TRIZ" do not trigger false TRIZ passports. | Skill hijacks ordinary bug fixing or misses Russian TRIZ queries (FAIL). |

---

## Part 2: The `/grill-me` Interrogation (10 Core Design Tensions)

### Dilemma 1: The "Philosophy Bot" Trap
* **The Trap:** Superficial TRIZ prompts cause LLMs to lecture the user with TRIZ jargon instead of solving the problem.
* **Architectural Remedy:** **Dual-Loop Progressive Disclosure** (v3.0.0). Loop 1 runs the 5-step ARIZ-AI pipeline internally; Loop 2 outputs **Layer 1 (Plain-Language Core)** by default with zero TRIZ jargon and concrete mechanisms, offering **Layer 2 (Professional TRIZ Passport)** on demand.

### Dilemma 2: Altshuller's 39×39 Matrix vs Modern LLM Architecture
* **The Trap:** Classical 39×39 mechanical matrices are noisy for software/AI problems and non-deterministic when mapped to modern domains.
* **Architectural Remedy:** Treat the **7 Resolution Strategies for Physical Contradictions** as the primary engine, and explicitly label `11-contradiction-matrix.md` as a **curated, non-deterministic heuristic lookup**.

### Dilemma 3: Premature Compromise Bias
* **The Trap:** Conversational models often propose middle-ground compromises before testing whether conflicting requirements can be separated in space, time, condition, or structure.
* **Architectural Remedy:** Phase-gated **Anti-Rationalization Guardrails** combined with **Mandatory Constraint Classification** (`Hard`, `Soft`, `Assumptions`) so hard constraints are never silently relaxed, while legitimate soft-constraint trade-offs and irreducible limits have honest, structured output paths.

### Dilemma 4: ARIZ-85-V Context Bloat vs Deep Deadlocks
* **The Trap:** Full 9-part ARIZ-85-V is too heavy for every prompt, but 5-step ARIZ-AI may be too shallow for Level 4–5 deadlocks.
* **Architectural Remedy:** **3-Tier Architecture** with a Fast-Path for simple contradictions in Tier-1 (`SKILL.md`), domain modules in Tier-2 (`references/`), and full ARIZ-85-V, MMC, Step Back from IFR, Table 2, Trimming, and AFD in Tier-3 (`references/ariz-deep/`).

### Dilemma 5: The Illusion of "Free" Resources in Software & Business
* **The Trap:** Calling OS page cache, third-party APIs, or user telemetry "free" hides memory pressure, vendor costs, and GDPR/KYC legal risks.
* **Architectural Remedy:** Strict VPR qualification rule in Step 3: a resource qualifies only when available within the boundary, lawful, reliable enough, and its incremental cost is known or explicitly marked conditional.

### Dilemma 6: Universal vs Domain-Specific Tension
* **The Trap:** Examples skewed only toward low-level systems programming make the skill feel narrow.
* **Architectural Remedy:** Multi-domain VPR examples directly in Tier-1 (`SKILL.md`) plus dedicated translation lenses in `08-multi-domain-lenses.md` (Software, AI, Business, Hardware, OTSM-TRIZ ENV) and `13-perception-mapping.md`.

### Dilemma 7: Fabricated "Verified" Outcomes
* **The Trap:** A template field titled "Verified Outcome" pressures the LLM to claim a benchmark was measured when it only generated text.
* **Architectural Remedy:** Require explicit verification status (`Status: UNVERIFIED — conditional expected outcome` vs `MEASURED — only when empirical data was provided by the user`) plus mandatory `Evidence & Confidence` (`Established`, `Pattern`, `Hypothesis`) linked to `CLAIMS.md`.

### Dilemma 8: Benchmark Contamination
* **The Trap:** Listing benchmark scenarios and reference solutions in the live routing table allows the agent to read the answer key during evaluations.
* **Architectural Remedy:** Quarantine `10-testing-scenarios.md` and `12-evaluation-suite.md` under an explicit `DO NOT load during live problem-solving` rule outside the active routing table.
