---
description: >-
  Systematic protocol for sharpening Administrative Contradictions into Technical and extreme Physical Contradictions across domains.
metadata:
  tags: [contradiction, technical-contradiction, physical-contradiction, sharpening, otsm]
  source: TRIZ-Classical & Modern
---

# 02. Sharpening Contradictions: AC $\longrightarrow$ TC $\longrightarrow$ PC

> *"The sharper the contradiction, the easier the solution."* — Genrich Altshuller

---

## 1. The 3-Tier Contradiction Pipeline

Problems in engineering and strategy usually begin as vague administrative complaints. To solve them inventively, they must undergo two successive dialectical transformations:

```
[Level 1: Administrative Contradiction (AC)]
"The system is too slow / churn is high / the sensor overheats."
                     │
                     ▼ (Step 1: Isolate competing parameters)
[Level 2: Dual Technical Contradictions (TC1 & TC2)]
TC1: If we optimize Parameter A, Parameter B degrades.
TC2: If we preserve Parameter B, Parameter A cannot achieve its goal.
                     │
                     ▼ (Step 2: Isolate the single element & state opposing requirements)
[Level 3: Physical Contradiction (Sharpened to Extreme Limit)]
"Element X must have property [P] (to satisfy Requirement 1)
 AND must have property [NOT-P] (to satisfy Requirement 2)."
```

---

## 2. Step-by-Step Sharpening Guide

### Step 2.1: Formulate Dual Technical Contradictions ($\text{TC}_1$ and $\text{TC}_2$)
Formulating both symmetrical sides prevents confirmation bias:
- **$\text{TC}_1$:** When we optimize [Parameter $A$] by doing [Action $X$], [Parameter $B$] deteriorates because of [Mechanism $Y$].
- **$\text{TC}_2$:** When we optimize [Parameter $B$] by avoiding [Action $X$], [Parameter $A$] fails to meet specifications.

### Step 2.2: Identify the Operational Element ($X$)
Pinpoint the exact physical, logical, or organizational entity where the two demands collide:
- Software: Data buffer, network socket, database lock, API payload, memory pointer.
- AI Agents: Prompt context window, reasoning steps, tool schema, attention mask.
- Business: Onboarding form, pricing gate, approval tier, sales commission policy.
- Physical: Enclosure wall, turbine blade, gear teeth, electrical conductor.

### Step 2.3: Drive to the Extreme Limit (Предельное Обострение)
Moderate formulations invite compromise. Drive values to infinity and zero:
- Not *"The buffer should be somewhat smaller"* $\longrightarrow$ *"The buffer must occupy ZERO bytes."*
- Not *"The function should be reasonably fast"* $\longrightarrow$ *"The function must complete in ZERO milliseconds."*
- Not *"The onboarding flow should be slightly shorter"* $\longrightarrow$ *"The flow must take ZERO user clicks."*

### Step 2.4: Formulate the Canonical Physical Contradiction (PC)
Use the strict canonical syntax:

$$\mathbf{\text{Element } [X] \text{ must have property } [P] \text{ to satisfy } [\text{Requirement } 1]}$$
$$\mathbf{\text{AND}}$$
$$\mathbf{\text{Element } [X] \text{ must have property } [\neg P] \text{ to satisfy } [\text{Requirement } 2]}$$

---

## 3. Multi-Domain Real-World Examples

### Example A: Database Concurrency Contention (Software)
- **AC:** "Database performance collapses under 50,000 concurrent checkout transactions."
- **TC:** If we lock the inventory row, overselling is prevented, but throughput drops to 20 TPS.
- **Sharpened PC:** "The inventory counter must be **locked** (to guarantee ACID consistency) and must **NOT be locked** (to achieve 50,000 TPS instantly)."
- *Resolution:* Separation in Space/Structure (Striped lock-free counters via CPU atomic CAS operations).

### Example B: AI Agent Context Saturation vs Deep Knowledge (AI Architecture)
- **AC:** "Agent hallucinations increase when detailed API reference documentation is omitted, but adding full docs causes context window exhaustion and high inference costs."
- **TC:** If we include 500 pages of API docs in context, accuracy rises, but cost and latency surge $10\times$.
- **Sharpened PC:** "The API documentation must be **present in prompt memory** (to provide grounded zero-hallucination tools) and must **NOT be present in prompt memory** (to keep context lightweight and sub-second)."
- *Resolution:* Separation by Condition & Structure (Tier-2 Progressive Disclosure: lightweight dispatcher skill with dynamic, on-demand reference loading via tool calls).

### Example C: Secure Frictionless Onboarding (Business / Fintech)
- **AC:** "Strict identity verification causes 40% signup drop-off, but removing verification causes surging fraud losses."
- **TC:** If we enforce 5-step KYC upfront, fraud is eliminated, but user conversion collapses.
- **Sharpened PC:** "The identity verification must be **exhaustively rigorous** (to satisfy regulators and prevent fraud) and must be **completely absent** (to achieve instantaneous frictionless signup)."
- *Resolution:* Separation in Time & Condition (Progressive verification: 1-click instantaneous signup with zero checks; dynamic risk-scored verification triggered only upon high-value money transfer).

### Example D: High-Temperature Sensor Housing (Physical Engineering)
- **AC:** "Engine exhaust temperature sensor melts when exposed to 1,200°C combustion gas."
- **TC:** If we thicken the thermal insulation shield, sensor lifetime is preserved, but temperature response lag increases to 10 seconds, causing engine control failures.
- **Sharpened PC:** "The sensor housing wall must be **infinitely thick and insulating** (to block 1,200°C heat) and must be **infinitely thin and conductive** (to deliver instantaneous microsecond thermal response)."
- *Resolution:* Separation in Space & Structure (Porous pyrolytic graphite micro-lattice with directional anisotropic heat conductivity: conduct heat longitudinally to probe tip while insulating radially).

---

**Next:** [03-separation-principles.md](03-separation-principles.md) — The 4 Separation Operators.  
**Index:** [README.md](README.md)
