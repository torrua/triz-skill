---
name: triz-universal
description: >-
  Use when facing conflicting requirements where improving one metric degrades another and premature trade-offs must be avoided:
  architectural dead ends, performance vs memory/consistency conflicts, security vs usability, cost vs quality,
  or when the user asks to solve a problem "по ТРИЗ / using TRIZ", formulate a physical contradiction (ФП / ИКР / ВПР / АРИЗ),
  or resolve a "неразрешимый компромисс / архитектурный тупик".
  Do NOT use for routine bug fixing, ordinary database lock/deadlock stack-trace debugging, simple pros/cons comparisons,
  general questions about what TRIZ is, or when the user explicitly requests a quick standard trade-off.
metadata:
  category: technique
  triggers:
    - TRIZ
    - ТРИЗ
    - физическое противоречие
    - техническое противоречие
    - идеальный конечный результат
    - ИКР
    - ВПР
    - АРИЗ
    - неразрешимый компромисс
    - архитектурный тупик
    - physical contradiction
    - technical contradiction
    - ideal final result
    - inventive problem
    - CAP theorem conflict
    - zero budget optimization
---

# Universal TRIZ: Non-Compromising Inventive Problem Solving

> **Core Axiom:** First seek an inventive resolution that improves Parameter A without degrading Parameter B. If a hard physical, mathematical, legal, budgetary, or contractual limit prevents that outcome, state the limit and its evidence rather than inventing a guarantee.

> **Language Adaptation Directive:** Always respond in the language of the user's prompt (Russian prompt -> Russian response and Russian terminology; English prompt -> English response), unless the user explicitly requests another language.

---

## 1. Anti-Rationalization Guardrails & Scope

LLMs often gravitate toward middle-ground compromises before testing whether a contradiction can be eliminated (see `C-RLHF-01` in [references/CLAIMS.md](references/CLAIMS.md)). The table below intercepts premature rationalizations:

| LLM Rationalization | Dialectical Reality & Mandatory Rule |
|---|---|
| *"In real-world engineering, trade-offs are inevitable."* | **INCOMPLETE.** First formulate the Physical Contradiction and test whether it can be eliminated. If not, identify the irreducible limit and the evidence. |
| *"I'll just add Redis / Kafka / a new service / extra staff to fix this."* | **VIOLATION OF IFR unless disclosed and within budget.** Explore existing resources first. **Exception — Acceptable Standard Solution:** If a standard component satisfies all hard constraints within the user's acceptable budget and complexity limit, it is a valid choice once its cost, complexity, and new risks are disclosed. |
| *"I will offer a balanced middle-ground solution."* | **UNACCEPTABLE without diagnosis.** Do not offer a compromise before testing separation, bypass, and hard limits. |
| *"Let's ask the user which constraint they want to drop."* | **FORBIDDEN for hard constraints.** Clarify ambiguous assumptions and soft constraints; never silently discard a stated hard constraint. |
| *"I am following TRIZ in spirit by brainstorming."* | **VIOLATION.** Follow the ARIZ-AI pipeline (Step 0 through Step 5) and make the mechanism testable. |

### 🚨 Red Flags — STOP and Restart
Stop if your draft proposes weakening a requirement **that has not been classified as a soft constraint and authorized by the user**, or uses premature compromise phrasing before running Step 0 through Step 4:
1. *"We can balance between X and Y..."* (without testing separation/bypass first)
2. *"A reasonable compromise would be..."* (when applied to a hard constraint)
3. *"Accepting a slight performance hit in exchange for..."* (when violating a stated hard bound)
4. *"The user must decide which constraint matters more..."* (when applied to hard constraints rather than asking for authorization on a soft target)

**ACTION:** Return to Step 0 / Step 2, classify the constraint, and either find a resolution, prove an irreducible limit, or ask the user to authorize relaxing a soft constraint.

### 🛑 When NOT to Use This Skill
Do **not** force the TRIZ contradiction pipeline when:
- The user has an ordinary code bug, syntax error, or routine database deadlock/lock-ordering bug that needs standard debugging rather than inventive redesign.
- A standard off-the-shelf component (e.g., an index, cache, or queue) already satisfies all hard constraints within the user's stated budget and operational complexity.
- The user asks a purely informational or meta-question about TRIZ (*"What is TRIZ?"*, *"Review this TRIZ markdown file"*).
- The task is a straightforward feature request or pros/cons comparison with no conflicting hard requirements.
- The user explicitly states they want a standard quick trade-off and declines architectural changes.

---

## 2. The ARIZ-AI Pipeline (Step 0 + 5 Steps)

When invoked, execute this pipeline (use the **Fast-Path**: if Step 0 shows a known hard limit or Pass 1 resolves the contradiction cleanly with existing VPR, complete a single compact pass without redundant iterations):

```text
[Step 0: Limit & Constraint Pre-Check] -> [Step 1: IFR Framing] -> [Step 2: PC Sharpening]
                                                                              |
[Step 5: Verification] <--- [Step 4: Resolution Strategies] <--- [Step 3: VPR Audit]
```

### Step 0: Constraint Classification & Known-Limit Pre-Check (Mandatory)
1. **Classify every requirement** as one of:
   - **Hard constraints:** physical laws, formal mathematical bounds under active assumptions, statutes/regulations, safety invariants, contractual/SLA limits, or a fixed budget. Never silently relax these.
   - **Soft constraints:** preferences or optimization targets that may be traded off only with the user's explicit authorization.
   - **Assumptions:** unverified facts, costs, capabilities, or demand estimates. Ask for evidence or mark the result conditional.
2. **Upfront Limit & Sufficiency Gate:**
   - If a **statutory/regulatory mandate** (e.g., KYC/AML before regulated money movement) or **formal/physical bound** (CAP theorem under active partition, Shannon entropy bound on random ciphertext, thermodynamics) directly governs the request, test in Step 4 whether its assumptions can be bypassed (Strategy 6). If the assumptions are fixed by the prompt, declare the **irreducible constraint** immediately without running 3 redundant ideation passes.
   - If a standard engineering component already fits all hard constraints and the stated budget, present it directly with its cost and risks disclosed.

There are three valid outcomes: **(1) eliminate the contradiction**, **(2) prove an irreducible limit**, or **(3) propose a managed trade-off on a soft constraint explicitly authorized by the user**. Treat IFR as a search direction, not a promise that every target is attainable.

### Step 1: Mini-Problem & Ideal Final Result (IFR)
- Define the system boundary. Prefer existing resources; do not label an external API, paid service, privileged access, or user data as free.
- State the IFR:
  > *"The element [X] itself (or an existing resource/waste), at zero additional cost and zero added complexity, performs [Function 1] while preventing [Harm 2]."*

### Step 2: Sharpen the Physical Contradiction (PC)
Sharpen the dual Technical Contradictions (TC1, TC2) into the atomic Physical Contradiction at the extreme limit:
> **Element X must have property [P] to satisfy [R1] AND Element X must have property [NOT-P] to satisfy [R2].**

*(e.g., "The cache must exist to guarantee 1ms latency, AND the cache must NOT exist to avoid memory overhead and stale data.")*

### Step 3: Substance-Field Resource Audit (VPR)
Identify latent resources in the Operational Zone (OZ) and Operational Time (OT). A resource qualifies as VPR only when it is available within the boundary, legally usable, reliable enough for the requirement, and its incremental cost is known or explicitly marked unknown:
- **Software & AI:** Idle CPU cycles, struct padding, deterministic hashing, write-read asymmetry, OS kernel (`io_uring`, `sendfile`), tool-call hooks.
- **Business & Organizations:** Existing customer touchpoints, billing/renewal cycles, contract tiers, self-serve onboarding intent, partner distribution.
- **Physical & Hardware:** Ambient air/cooling, gravity, thermal expansion, waste heat, structural geometry, hydrostatic pressure.
*(See [references/07-resource-audit-vpr.md](references/07-resource-audit-vpr.md) and [references/08-multi-domain-lenses.md](references/08-multi-domain-lenses.md) for domain catalogs.)*

### Step 4: Apply Resolution Strategies (7 options)

**First, run Diagnostic Questions** (Zlotin/Zusman + Litvin) to select the strategy:
1. **Separation in Space:** *WHERE must X be P and NOT-P?* -> P in Zone 1, NOT-P in Zone 2 (CQRS, sharding, thermal zoning).
2. **Separation in Time:** *WHEN must X be P and NOT-P?* -> P during T1, NOT-P during T2 (MVCC, pre-computation, phased rollout).
3. **Separation by Condition:** *UNDER WHAT CONDITION?* -> P under C1, NOT-P under C2 (circuit breakers, risk-based triggers, phase-change materials).
4. **Separation by Structure:** *Do parts need P while the whole needs NOT-P?* -> Subsystems have P, supersystem has NOT-P (actor models, consensus clusters, honeycomb composites).
5. **Satisfy:** *Can one resource deliver BOTH P and NOT-P at once?* -> Meet both simultaneously (passkeys, aerogel, memory-mapped files under tested flush rules).
6. **Bypass:** *Can the goal be reformulated so X is not needed?* -> Eliminate the need for X ("Do we need X at all?").
7. **Alternative System:** *Can the entire system be replaced?* -> Transition to a system lacking this contradiction.

*(Cross-reference [references/03-separation-principles.md](references/03-separation-principles.md) for principles per strategy, and [references/11-contradiction-matrix.md](references/11-contradiction-matrix.md) for the curated heuristic lookup.)*

### ⚖️ Irreducible Constraints (Escape Valve)
An **irreducible constraint** may stem from:
1. **Physical laws** (thermodynamics, conservation laws, speed-of-light latency floor),
2. **Formal/mathematical theorems** (CAP theorem, Amdahl's law, FLP impossibility, information-theoretic bounds) — *only after verifying that the theorem's assumptions hold and cannot be bypassed via problem reformulation*, or
3. **Non-negotiable external limits** (statutory/regulatory mandates, fixed budget ceilings, binding contracts).

When the limit was not already established in Step 0, test up to **3 distinct ARIZ-AI passes** — **Pass 1:** Classical Separation (Strategies 1–4), **Pass 2:** Satisfy / micro-level VPR shift (Strategy 5), **Pass 3:** Bypass or Alternative System testing the limit's assumptions (Strategies 6–7). If the conflict remains bound by a verified hard limit, explicitly declare an **irreducible constraint**, state which assumptions hold, and propose the highest-ideality design within that boundary.

### Step 5: Verification & Secondary Harm Audit
Verify the outcome against the **Inventive Quality Checklist**:
- [ ] Did Parameter A meet a stated measurable target and baseline (or was an irreducible limit proven)?
- [ ] Did Parameter B remain within its stated hard limit? If a soft constraint was relaxed, was it explicitly authorized?
- [ ] Were new dependencies, operating costs, privacy effects, and legal obligations disclosed?
- [ ] Is every safety, security, performance, and compliance claim backed by evidence or marked as a hypothesis?
- [ ] System Operator Check: Does the solution create technical debt or harm the supersystem?

---

## 3. Operational Modes & Dual-Loop Execution

The skill enforces a strict separation between **internal reasoning** and **external delivery**:

1. **Loop 1: Deep Methodological Reasoning (Internal State Lock)**
   - Before generating any user-facing text, lock in 6 internal state variables: `Constraints (Hard/Soft/Assumptions)`, `Outcome Type (Eliminate / Proven Limit / Managed Trade-off)`, `Physical Contradiction`, `Mobilized VPR`, `Selected Strategy & Principle`, and `Verification Plan`.
   - **Pre-Commitment Rule (Anti-Post-Hoc):** Both Layer 1 and Layer 2 must render these exact locked Loop 1 variables so that a follow-up Layer 2 passport is never fabricated post-hoc.
   - **Explicit Audit Flag (`[AUDIT]`):** When the user prompt includes the token `[AUDIT]` or `--audit` (or when running on a model without hidden thinking tokens), emit a visible 4-line `<triz_scratchpad>` block containing those locked variables right before the answer.
2. **Loop 2: Contextual Output Delivery (User-Facing)**
   - **Layer 1: Plain-Language Core (Default)** — clear everyday explanation with zero TRIZ jargon, covering solutions, proven limits, or soft trade-off options.
   - **Layer 2: Professional TRIZ Passport** — full structured TRIZ breakdown when requested.

The skill operates in **three execution modes** (selected by context completeness and user intent):
- **Autonomous Mode (Default):** Use when the prompt provides enough context to identify the conflict and boundary. Runs Loop 1 internally and outputs Layer 1 (or Layer 2 if TRIZ analysis was requested).
- **Semi-Automatic Mode:** Use in interactive chat when critical constraints or system boundaries are missing: ask up to 4 targeted diagnostic questions first. **Non-Interactive / Single-Turn Fallback:** In one-shot API calls, batch evaluations, or if the user does not reply, do not block — proceed immediately using explicitly stated default assumptions.
- **Socratic Mode:** Use when the user explicitly requests interactive coaching or step-by-step facilitation (*"/triz-session"*, *"пошагово"*, *"guide me step by step"*). Pause for user feedback after each ARIZ-AI milestone.

---

## 4. Output Delivery Template (Progressive Disclosure)

To maximize practical impact and prevent cognitive overload, the skill employs a **two-layer progressive disclosure model**:

### Layer 1: Plain-Language Core (Default Output)
*When to use:* By default for all practical, engineering, business, and everyday problem prompts unless the user explicitly requests a TRIZ solution or methodological analysis.
*Rules:*
1. **Outcome-Honest & Solution-First:**
   - *If the contradiction is eliminated (Outcome 1):* Present 1–3 concrete, non-compromising inventive solutions in clear, everyday language.
   - *If an irreducible limit applies (Outcome 2):* Clearly state the limit, which assumptions make it unbreakable, and the best design within that boundary.
   - *If a soft constraint trade-off is needed (Outcome 3):* Keep all hard constraints intact, explain the soft-constraint options, and ask the user which option they authorize.
2. **Zero Jargon:** Do NOT use TRIZ terminology (*ФП, ИКР, ВПР, ТП, Оператор РВС, Прием №...*). Explain the physical, architectural, or organizational mechanism using intuitive language (what to change, how it works, why the conflict disappears or where the hard bound lies).
3. **Assumptions, Residual Limits & Quick Verification (Mandatory 2–3 lines):** Briefly state the key assumption(s), what remains unverified or bounded, and one concrete check to validate the expected effect.
4. **Contextual Closing Invitation:** When responding in standard conversational mode, offer a follow-up invitation to explore the underlying methodology:
   - *Russian:*
     > *«Хотите, я подробно покажу, как именно ТРИЗ-алгоритм привёл нас к этому решению (с разбором противоречия, скрытых ресурсов и применённых приёмов)?»*
   - *English:*
     > *“Would you like a detailed breakdown of how the TRIZ algorithm arrived at this solution (including the contradiction, resources, and inventive principles used)?”*
   - *Format Exception:* Omit the closing invitation if the user requested a strict machine-readable format (JSON, YAML, raw code), an ultra-compact list, a one-line answer, or when continuing an interactive multi-step workflow where trailing prompts add unnecessary noise.

### Layer 2: Professional TRIZ Passport (Deep Mode)
*When to use:* Triggered immediately when:
1. **User requests a TRIZ solution upfront:** The initial prompt explicitly asks to solve using TRIZ or requests methodological analysis (*"реши по ТРИЗ", "найди решение с помощью ТРИЗ", "разбери по ТРИЗ", "выполни анализ по АРИЗ-85-В", "сформулируй ФП и ИКР", "дай ТРИЗ-паспорт решения", "solve using TRIZ", "show full TRIZ analysis", "formulate physical contradiction"*).
2. **User accepts the Layer 1 follow-up:** The user responds affirmatively (*"Да", "Расскажи", "Интересно", "Давай подробнее", "Yes", "Show breakdown"*) **directly to the Layer 1 closing invitation** (do not confuse an affirmative reply to a separate clarifying question with a request for Layer 2).
3. **Formal verification context:** The user explicitly requests an auditable engineering contradiction passport or technical claim structuring (note: patent-style claim structuring is an engineering ideation aid, not legal or patent-attorney advice).

*Routing Guardrail:* Incidental or purely meta-mentions of the word "TRIZ" / "ТРИЗ" (e.g., *"придумай задачи для скилла ТРИЗ"*, *"что такое ТРИЗ?"*, *"проверь код ТРИЗ-модуля"*) MUST NOT trigger the Layer 2 contradiction passport. Layer 2 requires an explicit intent to solve or decompose a problem using TRIZ methodology.

*Confidence Levels (see [references/CLAIMS.md](references/CLAIMS.md)):*
- **Established fact / Факт:** Verified by primary documentation, formal proof, or measured user benchmark.
- **Pattern / Паттерн:** Known engineering/business pattern whose quantitative effect depends on workload or context.
- **Hypothesis / Гипотеза:** Untested mechanism requiring an experiment before adoption.

#### Шаблон вывода на русском языке:
```markdown
### 💡 ТРИЗ-Изобретательское Решение
- **Классификация ограничений:** [Жёсткие (Hard): ... | Мягкие (Soft): ... | Допущения (Assumptions): ...]
- **Тип исхода:** [Устранение противоречия | Доказанный предел | Авторизованный мягкий компромисс]
- **Физическое противоречие (ФП):** [Элемент X должен обладать свойством P для R1, и НЕ-P для R2]
- **Диагностический путь:** [ГДЕ / КОГДА / ПО СОСТОЯНИЮ / СТРУКТУРА / СОВМЕЩЕНИЕ / ОБХОД / АЛЬТ-СИСТЕМА / ПРЕДЕЛ]
- **Примененная стратегия:** [В пространстве | Во времени | По состоянию | По структуре | Совмещение | Обход | Альтернативная система | Доказанный предел | Управляемый компромисс]
- **Использованный прием(ы):** [Прием №N: Каноническое русское название — и ПОЧЕМУ выбран]
- **Мобилизованный ресурс (ВПР):** [Использованный внутренний/надсистемный ресурс и его граничные условия]
- **Решение:** [Суть механизма устранения противоречия, работа в рамках предела или согласованный мягкий компромисс]
- **Доказательная база и уверенность:** [Факт | Паттерн | Гипотеза; источник или обоснование из CLAIMS.md]
- **План верификации:** [Базовая линия, эксперимент, порог успеха и предлагаемая роль для проверки]
- **Остаточные риски:** [Неустранимые пределы, приватность, комплаенс, стоимость и режимы отказа]
- **Ожидаемый результат и статус проверки:** [Статус: НЕ ПРОВЕРЕНО (ожидаемый эффект при указанных допущениях) | ИЗМЕРЕНО (только при наличии реальных замеров)]
```

#### English Delivery Template:
```markdown
### 💡 TRIZ Inventive Resolution
- **Constraint Classification:** [Hard: ... | Soft: ... | Assumptions: ...]
- **Outcome Type:** [Contradiction Eliminated | Proven Limit | Authorized Managed Trade-off]
- **Physical Contradiction:** [Element X must have property P for R1, and NOT-P for R2]
- **Diagnostic Path:** [WHERE / WHEN / CONDITION / STRUCTURE / SATISFY / BYPASS / ALT / LIMIT]
- **Strategy Applied:** [Space | Time | Condition | Structure | Satisfy | Bypass | Alternative System | Proven Limit | Managed Trade-off]
- **Inventive Principle(s) Used:** [Principle #N: Name — and WHY it was selected for this specific contradiction]
- **Resource Mobilized (VPR):** [Internal/supersystem resource used and its boundary conditions]
- **Resolution:** [How the contradiction was resolved, highest-ideality design within a proven limit, or authorized soft trade-off]
- **Evidence & Confidence:** [Established fact | Pattern | Hypothesis; source or reason per CLAIMS.md]
- **Verification Plan:** [Baseline, experiment, success threshold, and suggested verification role]
- **Residual Risks:** [Irreducible limits, privacy, compliance, cost, and failure modes]
- **Expected Outcome & Verification Status:** [Status: UNVERIFIED (conditional expected outcome) | MEASURED (only if empirical data was provided)]
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
| **Need curated heuristic contradiction lookup (non-deterministic)** | See [references/11-contradiction-matrix.md](references/11-contradiction-matrix.md) |
| **Resolving organizational / people-centric contradictions** | See [references/13-perception-mapping.md](references/13-perception-mapping.md) |
| **Deep Level 4-5 deadlock or canonical ARIZ-85-V required** | See [references/ariz-deep/01a-ariz-85v-analysis.md](references/ariz-deep/01a-ariz-85v-analysis.md) & [references/ariz-deep/01b-ariz-85v-resolution.md](references/ariz-deep/01b-ariz-85v-resolution.md) |
| **Micro-level conflict, concurrency races, or agent role-prompting** | Run MMC: [references/ariz-deep/02-mmc-operator-protocol.md](references/ariz-deep/02-mmc-operator-protocol.md) |
| **Synthesizing deployment, assembly, zero-downtime, or cold start** | See [references/ariz-deep/03-step-back-from-ifr.md](references/ariz-deep/03-step-back-from-ifr.md) |
| **Decision tree for physical contradictions (ARIZ Table 2)** | See [references/ariz-deep/04-physical-contradiction-tree.md](references/ariz-deep/04-physical-contradiction-tree.md) |
| **Pruning architectural bloat, queues, microservices without loss** | Run Trimming: [references/ariz-deep/05-trimming-algorithm.md](references/ariz-deep/05-trimming-algorithm.md) |
| **Stress-testing failure modes and inverted vulnerability search** | Run Subversion Analysis (AFD): [references/ariz-deep/06-subversion-analysis-afd.md](references/ariz-deep/06-subversion-analysis-afd.md) |
| **Checking sources, claim scope, and confidence** | See [references/SOURCES.md](references/SOURCES.md) and [references/CLAIMS.md](references/CLAIMS.md) |

> **Offline Maintainer & Regression Assets (Moved Outside Skill Directory):** All pressure benchmark scenarios, reference problem suites, and evaluation corpora reside outside `triz-universal/` in `evals/`. Never load `evals/` files during live problem-solving.
