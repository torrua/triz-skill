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
    - противоречие
    - физическое противоречие
    - техническое противоречие
    - идеальный конечный результат
    - ИКР
    - ВПР
    - АРИЗ
    - неразрешимый компромисс
    - архитектурный тупик
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

> **Core Axiom:** First seek an inventive resolution that improves Parameter $A$ without degrading Parameter $B$. If a hard physical, legal, budgetary, or contractual limit prevents that outcome, state the limit and its evidence rather than inventing a guarantee.

---

## 1. Anti-Rationalization Guardrails (Compromise Prevention)

LLMs naturally gravitate toward compromise and middle-ground solutions due to RLHF conditioning. The table below intercepts standard rationalizations:

| LLM Rationalization | Dialectical Reality & Mandatory Rule |
|---|---|
| *"In real-world engineering, trade-offs are inevitable."* | **INCOMPLETE.** First formulate the Physical Contradiction and test whether it can be eliminated. If not, identify the irreducible limit and the evidence. |
| *"I'll just add Redis / Kafka / a new service / extra staff to fix this."* | **VIOLATION OF IFR unless disclosed.** Explore existing resources first; an added component is allowed only with its cost, complexity, and new risks stated. |
| *"I will offer a balanced middle-ground solution."* | **UNACCEPTABLE without diagnosis.** Do not offer a compromise before testing separation, bypass, and hard limits. |
| *"Let's ask the user which constraint they want to drop."* | **FORBIDDEN for hard constraints.** Clarify ambiguous assumptions and soft constraints; never silently discard a stated hard constraint. |
| *"I am following TRIZ in spirit by brainstorming."* | **VIOLATION.** Follow the 5-step ARIZ-AI pipeline and make the mechanism testable. |

### 🚨 Red Flags — STOP and Restart
If your output contains:
1. *"We can balance between X and Y..."*
2. *"A reasonable compromise would be..."*
3. *"Accepting a slight performance hit in exchange for..."*
4. *"The user must decide which constraint matters more..."*

**ACTION:** Return to Step 2, classify the constraint, and either find a resolution or explicitly justify the remaining trade-off.

### Constraint Classification (Mandatory)
Before the pipeline, list each requirement as one of:
- **Hard constraints:** laws, safety invariants, contractual/SLA limits, or a measured fixed budget. Never silently relax these.
- **Soft constraints:** preferences or targets that may be optimized only with the user's explicit authorization.
- **Assumptions:** unverified facts, costs, capabilities, or demand estimates. Ask for evidence or mark the result conditional.

There are three valid outcomes: **eliminate the contradiction**, **prove an irreducible limit**, or **propose a managed trade-off explicitly authorized by the user**. Treat IFR as a search direction, not a promise that every target is attainable.

### ⚖️ Irreducible Constraints (Escape Valve)
If after 3 ARIZ-AI iterations the contradiction remains unresolvable due to a fundamental physical law (CAP theorem, Amdahl's law, thermodynamics) — explicitly declare an irreducible constraint and propose a solution with maximum ideality within the bounds of that law.

---

## 2. The ARIZ-AI 5-Step Pipeline

When invoked, execute this 5-step loop:

```
[Step 1: IFR Framing] ─► [Step 2: PC Sharpening] ─► [Step 3: VPR Audit]
                                                           │
[Step 5: Verification] ◄─ [Step 4: Separation Operators] ◄─┘
```

### Step 1: Mini-Problem & Ideal Final Result (IFR)
- Define the system boundary and the hard constraints. Prefer existing resources; do not label an external API, paid service, privileged access, or user data as free.
- State the IFR:
  > *"The element [X] itself (or an existing resource/waste), at zero additional cost and zero added complexity, performs [Function 1] while preventing [Harm 2]."*

### Step 2: Sharpen the Physical Contradiction (PC)
Sharpen the dual Technical Contradictions ($\text{TC}_1, \text{TC}_2$) into the atomic Physical Contradiction at the extreme limit:
$$\mathbf{\text{Element } X \text{ must have property } [P] \text{ to satisfy } [R_1]}$$
$$\mathbf{\text{AND}}$$
$$\mathbf{\text{Element } X \text{ must have property } [\neg P] \text{ to satisfy } [R_2]}$$
*(e.g., "The cache must exist to guarantee 1ms latency, AND the cache must NOT exist to avoid memory overhead and stale data.")*

### Step 3: Substance-Field Resource Audit (VPR)
Identify latent resources in the Operational Zone (OZ) and Operational Time (OT). A resource qualifies as VPR only when it is available within the boundary, legally usable, reliable enough for the requirement, and its incremental cost is known or explicitly unknown:
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
- [ ] Did Parameter $A$ meet a stated measurable target and baseline?
- [ ] Did Parameter $B$ remain within its stated hard limit? If not, was the trade-off authorized?
- [ ] Were new dependencies, operating costs, privacy effects, and legal obligations disclosed?
- [ ] Is every safety, security, performance, and compliance claim backed by evidence or marked as a hypothesis?
- [ ] System Operator Check: Does the solution create technical debt or harm the supersystem?

---

## 3. Operational Modes

The skill functions in three execution modes depending on user intent:
- **Autonomous Mode (Default):** Silently executes the 5-step ARIZ-AI pipeline, sharpens the physical contradiction, mobilizes latent resources (VPR), and directly delivers the non-compromising resolution and verification template.
- **Semi-Automatic Mode:** Asks 4 key diagnostic questions (What is the system? What is the conflict? What parameters matter? What resources are available?), then generates the full ARIZ-AI resolution. Best when the user provides partial context.
- **Socratic Mode:** Interactively guides the user step-by-step through the ARIZ-AI stages (Mini-Problem → Physical Contradiction → VPR Audit → Separation Operators → Verification), prompting for feedback at each milestone before proceeding.

---

## 4. Output Delivery Template

### Language Adaptation
Always formulate your reasoning, diagnostic path, and final resolution in the language of the user's prompt (e.g., Russian, English).
- When responding in Russian, use canonical Russian TRIZ terminology: **ИКР** (Ideal Final Result), **ВПР** (Substance-Field Resources), **ФП** (Physical Contradiction), **ТП** (Technical Contradiction), 4 принципа разделения (в пространстве, во времени, по состоянию, по структуре), и 40 приемов Альтшуллера.
- Append the corresponding localized verification block:

#### English Delivery Template:
```markdown
### 💡 TRIZ Inventive Resolution
- **Physical Contradiction:** [Element X had to be P for R1, and NOT-P for R2]
- **Diagnostic Path:** [Which question led to strategy selection: WHERE/WHEN/CONDITION/STRUCTURE/SATISFY/BYPASS/ALT]
- **Strategy Applied:** [Space | Time | Condition | Structure | Satisfy | Bypass | Alternative System]
- **Inventive Principle(s) Used:** [Principle #N: Name — and WHY it was selected for this specific contradiction]
- **Resource Mobilized (VPR):** [Zero-cost internal/supersystem resource used]
- **Resolution:** [How the contradiction was resolved without compromise]
- **Evidence & Confidence:** [Established fact | Pattern | Hypothesis; source or reason]
- **Verification Plan:** [Baseline, experiment, success threshold, and owner]
- **Residual Risks:** [Irreducible limits, privacy, compliance, cost, and failure modes]
- **Verified Outcome:** [Measured outcome, or conditional expected outcome]
```

#### Шаблон вывода на русском языке:
```markdown
### 💡 ТРИЗ-Изобретательское Решение
- **Физическое противоречие (ФП):** [Элемент X должен обладать свойством P для R1, и НЕ-P для R2]
- **Диагностический путь:** [ГДЕ / КОГДА / ПО СОСТОЯНИЮ / СТРУКТУРА / СОВМЕЩЕНИЕ / ОБХОД / АЛЬТ-СИСТЕМА]
- **Примененная стратегия:** [В пространстве | Во времени | По состоянию | По структуре | Совмещение | Обход | Альтернативная система]
- **Использованный прием(ы):** [Прием №N: Каноническое русское название — и ПОЧЕМУ выбран]
- **Мобилизованный ресурс (ВПР):** [Использованный бесплатный внутренний/надсистемный ресурс]
- **Решение:** [Суть механизма устранения противоречия без компромисса]
- **Доказательная база и уверенность:** [Факт | Паттерн | Гипотеза; источник или обоснование]
- **План верификации:** [Базовая линия, эксперимент, порог успеха и ответственный]
- **Остаточные риски:** [Неустранимые пределы, приватность, комплаенс, стоимость и сбои]
- **Проверенный результат:** [Измеренный результат или ожидаемый эффект]
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
| **Checking sources, claim scope, and confidence** | See [references/SOURCES.md](references/SOURCES.md) and [references/CLAIMS.md](references/CLAIMS.md) |
