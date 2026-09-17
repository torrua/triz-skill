---
description: >-
  TRIZ Perception Mapping for organizational and people-centric contradictions.
  Surfaces stakeholder beliefs, builds Leads-To networks, and extracts contradictions
  for inventive resolution.
metadata:
  tags: [perception-mapping, business-triz, organizational, stakeholders, leads-to, conflict]
  source: Business TRIZ (Darrell Mann, Dr. Robert Adunka)
---

# 13. Perception Mapping — TRIZ for Organizations & People

Classical TRIZ resolves **technical** contradictions (parameters of physical/software systems). But many of the hardest problems are **organizational**: conflicting stakeholder beliefs, political deadlocks, team misalignment.

Perception Mapping is a Business TRIZ tool that makes hidden contradictions in human systems visible and resolvable.

---

## When to Use

- Team disagreements where both sides "are right"
- Strategic decisions where data supports contradictory conclusions
- Organizational change resistance
- Cross-functional conflicts (Engineering vs Product, Sales vs Support)
- Merger/acquisition integration friction

---

## The 5-Stage Process

```
[Stage 1: Gather] → [Stage 2: Link] → [Stage 3: Conflict] → [Stage 4: Leverage] → [Stage 5: Resolve]
 Perceptions      Leads-To Network   Conflict Pairs       Leverage Points      TRIZ Contradictions
```

### Stage 1: Gather Perceptions

Collect raw beliefs, concerns, and observations from each stakeholder (or stakeholder group). One idea per item. Target 30-100 items.

**Rules:**
- No filtering, no judging, no correcting
- Capture exact wording — the language reveals mental models
- Include emotional statements ("I feel like we're always firefighting")
- Tag each perception with its source stakeholder/group

**Example perceptions (Product vs Engineering):**

| # | Stakeholder | Perception |
|---|---|---|
| P1 | Product | "We need to ship features faster to stay competitive" |
| P2 | Product | "Technical debt discussions slow us down" |
| P3 | Engineering | "Rushing features creates bugs that cost more to fix later" |
| P4 | Engineering | "We need dedicated refactoring sprints" |
| P5 | Product | "Customers don't care about code quality, they care about features" |
| P6 | Engineering | "Customers will leave when the system becomes unreliable" |
| P7 | Management | "We need both speed and quality — find a balance" |

> ⚠️ **Note:** P7 is a classic **compromise trap**. TRIZ treats this as a contradiction to resolve, not a balance to find.

### Stage 2: Build Leads-To Network

For every perception, ask: **"What does this lead to?"** Link each to exactly one other perception.

```
P1 ("Ship faster") → P3 ("Rushing creates bugs")
P3 ("Bugs cost more") → P4 ("Need refactoring sprints")
P4 ("Refactoring sprints") → P2 ("Tech debt discussions slow us down")
P2 ("Slowed down") → P1 ("Need to ship faster")
```

**Result:** A directed graph. Look for **loops** — they indicate self-reinforcing contradictions.

### Stage 3: Spot Conflict Pairs

Scan for perceptions that directly oppose each other:

| Conflict Pair | Perception A | Perception B |
|---|---|---|
| **CP1** | P1: "Ship features faster" | P4: "Need refactoring sprints" |
| **CP2** | P5: "Customers want features" | P6: "Customers want reliability" |
| **CP3** | P2: "Tech debt talk slows us" | P3: "Rushing creates costly bugs" |

### Stage 4: Find Leverage Points

Identify perceptions that appear most frequently as targets in the Leads-To network (high in-degree). These are **leverage points** — changing them shifts the entire system.

Also identify **feedback loops** (A → B → C → A). Breaking a loop at its weakest link can dissolve multiple conflicts.

### Stage 5: Extract TRIZ Contradictions

Convert each conflict pair into a formal TRIZ contradiction:

**CP1 → Technical Contradiction:**
> "IF we allocate sprints to refactoring, THEN code quality improves, BUT feature delivery slows down."
> "IF we skip refactoring, THEN features ship faster, BUT technical debt accumulates."

**CP1 → Physical Contradiction:**
> "Development time must be spent on **new features** (to satisfy market needs) AND on **refactoring** (to satisfy system health) — but each sprint hour can only be spent once."

**Now apply ARIZ-AI:**

| Step | Application |
|---|---|
| **IFR** | The code improves itself at zero cost to feature delivery |
| **Separation in Time** | Refactor DURING feature work (boy scout rule: leave code cleaner than you found it) |
| **Separation in Structure** | Micro-refactors in every PR (subsystem: clean), feature velocity maintained (supersystem: fast) |
| **VPR** | Code review time (already spent), CI pipeline idle cycles, automated linting |
| **Satisfy** | Strangler Fig pattern: new features written in clean architecture alongside legacy, gradually replacing it |

---

## Perception Mapping Template

When running a Perception Mapping session, use this output structure:

```markdown
### 🗺️ Perception Map Results

**Stakeholders:** [List]
**Perceptions collected:** [N items]

#### Leads-To Network
[Directed graph or table of A → B links]

#### Conflict Pairs Identified
| # | Perception A | Perception B | Extracted Contradiction |
|---|---|---|---|

#### Leverage Points
- [High in-degree perception — changing this shifts the system]

#### TRIZ Contradictions (ready for ARIZ-AI)
1. [PC formulation from CP1]
2. [PC formulation from CP2]

#### Recommended Resolution Path
[Which separation principle / strategy applies to each contradiction]
```

---

## Common Organizational Contradiction Patterns

| Pattern | Contradiction | Typical TRIZ Resolution |
|---|---|---|
| **Speed vs Quality** | Dev time must be for features AND for quality | **Time**: refactor during feature work; **Structure**: automated quality gates |
| **Autonomy vs Alignment** | Teams must be independent AND coordinated | **Structure**: local autonomy + shared interfaces/contracts |
| **Innovation vs Stability** | Must experiment (risk) AND maintain reliability (safety) | **Space**: innovation sandbox + stable production; **Condition**: feature flags |
| **Centralization vs Decentralization** | Decisions must be fast (local) AND consistent (global) | **Condition**: local for reversible decisions, global for irreversible |
| **Transparency vs Privacy** | Must share info (collaboration) AND protect info (security) | **Condition**: share with authorized roles, protect from unauthorized |
| **Growth vs Profitability** | Must invest (grow) AND save (profit) | **Time**: invest now, harvest later; **Structure**: grow in one segment, profit in another |

---

**Index:** [README.md](README.md)
**Related:** [02-contradictions.md](02-contradictions.md) — How to formalize contradictions extracted from perception maps.
**Related:** [08-multi-domain-lenses.md](08-multi-domain-lenses.md) — Business & Strategy domain lens.
