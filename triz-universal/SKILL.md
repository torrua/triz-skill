---
name: triz-universal
description: >-
  Use when facing seemingly impossible trade-offs, architectural deadlocks, conflicting constraints,
  performance bottlenecks where improving one metric degrades another, business dilemmas (security vs friction, cost vs quality),
  or when conventional optimization fails. Enforces non-compromising inventive problem solving via TRIZ.
metadata:
  category: technique
  triggers:
    - TRIZ
    - ТРИЗ
    - trade-off
    - contradiction
    - bottleneck
    - conflicting requirements
    - latency vs memory
    - CAP theorem conflict
    - zero budget optimization
    - deadlock
    - unsolvable problem
    - inventive problem
    - physical contradiction
    - technical contradiction
    - ideal final result
---

# Universal TRIZ: Non-Compromising Inventive Problem Solving

> **Core Axiom:** A compromise is an admission of failure. A true inventive solution eliminates the contradiction so that Parameter $A$ improves without Parameter $B$ deteriorating, using only existing system resources (ВПР).

---

## 1. Anti-Rationalization Guardrails (Compromise Prevention)

LLMs naturally gravitate toward compromise and middle-ground solutions due to RLHF conditioning. The table below intercepts standard rationalizations:

| LLM Rationalization | Dialectical Reality & Mandatory Rule |
|---|---|
| *"In real-world engineering, trade-offs are inevitable."* | **FORBIDDEN.** A trade-off means you gave up before finding the Physical Contradiction. Eliminate the contradiction. |
| *"I'll just add Redis / Kafka / a new service / extra staff to fix this."* | **VIOLATION OF IFR.** Adding infrastructure increases complexity and cost. Use resources already present (VPR). |
| *"I will offer a balanced middle-ground solution."* | **UNACCEPTABLE.** Middle grounds leave both sides dissatisfied. Sharpen the contradiction to its extreme limit. |
| *"Let's ask the user which constraint they want to drop."* | **FORBIDDEN.** The user invoked TRIZ because both constraints are mandatory. Resolve both. |
| *"I am following TRIZ in spirit by brainstorming."* | **VIOLATION.** Violating the letter is violating the spirit. Follow the 5-step ARIZ-AI pipeline. |

### 🚨 Red Flags — STOP and Restart
If your output contains:
1. *"We can balance between X and Y..."*
2. *"A reasonable compromise would be..."*
3. *"Accepting a slight performance hit in exchange for..."*
4. *"The user must decide which constraint matters more..."*

**ACTION:** Delete the proposed solution immediately. Return to Step 2 and sharpen the Physical Contradiction.

### ⚖️ Irreducible Constraints (Escape Valve)
Если после 3 итераций ARIZ-AI противоречие остаётся неразрешимым из-за фундаментального физического закона (CAP, Amdahl, thermodynamics) — явно объявить irreducible constraint и предложить решение с максимальной идеальностью в рамках данного закона.

---

## 2. The ARIZ-AI 5-Step Pipeline

When invoked, execute this 5-step loop:

```
[Step 1: IFR Framing] ─► [Step 2: PC Sharpening] ─► [Step 3: VPR Audit]
                                                           │
[Step 5: Verification] ◄─ [Step 4: Separation Operators] ◄─┘
```

### Step 1: Mini-Problem & Ideal Final Result (IFR / ИКР)
- Define the system boundary. **Forbidden:** Introducing new complex entities or external paid services.
- State the IFR:
  > *"The element [X] itself (or an existing resource/waste), at zero additional cost and zero added complexity, performs [Function 1] while preventing [Harm 2]."*

### Step 2: Sharpen the Physical Contradiction (PC)
Sharpen the dual Technical Contradictions ($\text{TC}_1, \text{TC}_2$) into the atomic Physical Contradiction at the extreme limit:
$$\mathbf{\text{Element } X \text{ must have property } [P] \text{ to satisfy } [R_1]}$$
$$\mathbf{\text{AND}}$$
$$\mathbf{\text{Element } X \text{ must have property } [\neg P] \text{ to satisfy } [R_2]}$$
*(e.g., "The cache must exist to guarantee 1ms latency, AND the cache must NOT exist to avoid memory overhead and stale data.")*

### Step 3: Substance-Field Resource Audit (ВПР)
Identify latent, free resources in the Operational Zone (OZ) and Operational Time (OT):
- **Temporal:** Idle CPU cycles, network round-trip wait intervals, off-peak periods.
- **Spatial:** Struct padding bytes, unused bitflags, cache lines, cold storage.
- **Informational:** Natural data sorting, deterministic hashing, idempotency keys, write-read asymmetry.
- **System Waste:** Discarded error traces, backpressure watermarks, young-gen GC sweeps.
- **Supersystem / Environment:** OS kernel (`io_uring`, `sendfile`), client device compute, ambient fields.

### Step 4: Apply Resolution Strategies (7 options)

**First, run Diagnostic Questions** (Zlotin/Zusman) to narrow the search:
- **WHERE** must $X$ be $P$ and $\neg P$? → **Space**
- **WHEN?** → **Time**
- **UNDER WHAT CONDITION?** → **Condition**
- **Parts vs Whole?** → **Structure**

Then apply the matching strategy:
1. **Separation in Space:** $P$ in Zone 1, $\neg P$ in Zone 2 (CQRS, sharding, memory zoning).
2. **Separation in Time:** $P$ during $T_1$, $\neg P$ during $T_2$ (MVCC, pre-computation, batching).
3. **Separation by Condition:** $P$ under $C_1$, $\neg P$ under $C_2$ (circuit breakers, feature flags, adaptive routing).
4. **Separation by Structure:** Subsystems have $P$, supersystem has $\neg P$ (actor models, consensus clusters).

If classical separation fails, try:
5. **Satisfy:** Find one resource that delivers BOTH $P$ and $\neg P$ simultaneously (memory-mapped files, passkeys).
6. **Bypass:** Reformulate the problem so the contradiction vanishes ("Do we need X at all?").
7. **Alternative System:** Replace the system entirely with one that lacks this contradiction.

*(Cross-reference [references/03-separation-principles.md](references/03-separation-principles.md) for diagnostic questions, recommended principles per strategy, and multi-domain examples. For matrix lookup: [references/11-contradiction-matrix.md](references/11-contradiction-matrix.md).)*

### Step 5: Verification & Secondary Harm Audit
Verify the resolution against the **Inventive Quality Checklist**:
- [ ] Did Parameter $A$ improve significantly?
- [ ] Did Parameter $B$ remain completely unimpaired (zero degradation)?
- [ ] Were zero expensive external dependencies added?
- [ ] System Operator Check: Does the solution create technical debt in the future or break the supersystem?

---

## 3. Operational Modes

The skill functions in three execution modes depending on user intent:
- **Autonomous Mode (Default):** Silently executes the 5-step ARIZ-AI pipeline, sharpens the physical contradiction, mobilizes latent resources (VPR), and directly delivers the non-compromising resolution and verification template.
- **Semi-Automatic Mode:** Asks 4 key diagnostic questions (What is the system? What is the conflict? What parameters matter? What resources are available?), then generates the full ARIZ-AI resolution. Best when the user provides partial context.
- **Socratic Mode:** Interactively guides the user step-by-step through the ARIZ-AI stages (Mini-Problem → Physical Contradiction → VPR Audit → Separation Operators → Verification), prompting for feedback at each milestone before proceeding.

---

## 4. Output Delivery Template

When delivering a TRIZ-derived solution, append this concise verification block:

```markdown
### 💡 TRIZ Inventive Resolution
- **Physical Contradiction:** [Element X had to be P for R1, and NOT-P for R2]
- **Diagnostic Path:** [Which question led to strategy selection: WHERE/WHEN/CONDITION/STRUCTURE/SATISFY/BYPASS/ALT]
- **Strategy Applied:** [Space | Time | Condition | Structure | Satisfy | Bypass | Alternative System]
- **Inventive Principle(s) Used:** [Principle #N: Name — and WHY it was selected for this specific contradiction]
- **Resource Mobilized (VPR):** [Zero-cost internal/supersystem resource used]
- **Resolution:** [How the contradiction was resolved without compromise]
- **Verified Outcome:** [Parameter A improved with 0% degradation of Parameter B]
```

---

## 5. Quick Decision Tree (Extended)

| Situation / Need | Action & Reference |
|---|---|
| **Stuck in a trade-off, deadlock, or conflicting constraints** | Run **ARIZ-AI** (Section 2 above) or see [references/04-ariz-lite-algorithm.md](references/04-ariz-lite-algorithm.md) |
| **Need to formulate the Ideal Final Result (zero added cost)** | See [references/01-ikr-ideality.md](references/01-ikr-ideality.md) |
| **Need to sharpen a vague conflict into a Physical Contradiction** | See [references/02-contradictions.md](references/02-contradictions.md) |
| **Have a Physical Contradiction, need resolution strategies** | See [references/03-separation-principles.md](references/03-separation-principles.md) |
| **Need creative principle inspiration mapped across domains** | See [references/05-40-principles-catalog.md](references/05-40-principles-catalog.md) |
| **Need to evaluate supersystem risks or future tech debt** | See [references/06-system-operator-9screens.md](references/06-system-operator-9screens.md) |
| **Need to locate hidden "free" resources in system or code** | See [references/07-resource-audit-vpr.md](references/07-resource-audit-vpr.md) |
| **Applying TRIZ to AI Agents, Business Strategy, or Hardware** | See [references/08-multi-domain-lenses.md](references/08-multi-domain-lenses.md) |
| **Dealing with harmful, deficient, or uncontrollable interactions** | See [references/09-su-field-and-standards.md](references/09-su-field-and-standards.md) |
| **Running pressure verification benchmarks (RED vs GREEN)** | See [references/10-testing-scenarios.md](references/10-testing-scenarios.md) |
| **Need deterministic contradiction matrix lookup** | See [references/11-contradiction-matrix.md](references/11-contradiction-matrix.md) |
| **Self-evaluating TRIZ compliance with reference solutions** | See [references/12-evaluation-suite.md](references/12-evaluation-suite.md) |
| **Resolving organizational / people-centric contradictions** | See [references/13-perception-mapping.md](references/13-perception-mapping.md) |
