---
description: >-
  Evaluation suite with 5 reference problems, expected TRIZ solutions, and scoring criteria
  for self-assessment of agent TRIZ compliance.
metadata:
  tags: [evaluation, benchmark, reference-solutions, scoring, self-test]
  source: TRIZ-Classical & Modern Case Studies
---

# 12. Evaluation Suite — Reference Problems with Known TRIZ Solutions

Use these 5 reference problems to evaluate whether the TRIZ skill produces genuine inventive solutions.
Each problem includes the expected Physical Contradiction, the optimal Separation strategy, and a reference solution.

---

## Problem 1: The Database Speed-Consistency Dilemma

### Problem Statement
An e-commerce platform needs sub-5ms read latency for product catalog pages AND full ACID consistency for inventory updates. Current architecture uses a single PostgreSQL database that cannot deliver both simultaneously.

### Expected TRIZ Analysis

| Step | Expected Output |
|---|---|
| **IFR** | The database itself, at zero additional cost, delivers 5ms reads AND ACID writes |
| **Physical Contradiction** | Data access mode must be **lock-free** (for fast reads) AND **locked** (for consistent writes) |
| **VPR Resources** | PostgreSQL MVCC (already built-in), OS page cache, WAL sequential writes |
| **Separation** | **Time** — readers see snapshot at $T_{read}$ (lock-free), writers commit at $T_{write}$ (locked) |
| **Reference Solution** | MVCC with read replicas: reads from snapshot (zero locks), writes to primary (ACID). Already built into PostgreSQL — zero new components |

### Scoring Criteria
- ✅ **Pass** if: Solution uses MVCC/snapshots or equivalent temporal separation without adding external cache
- ❌ **Fail** if: Proposes adding Redis cache, or suggests "accepting eventual consistency as a reasonable trade-off"

---

## Problem 2: The Security-Usability Authentication Paradox

### Problem Statement
A banking app requires strong multi-factor authentication (regulatory compliance) AND frictionless one-tap login (user retention drops 40% per extra auth step).

### Expected TRIZ Analysis

| Step | Expected Output |
|---|---|
| **IFR** | Authentication itself provides maximum security with zero user friction |
| **Physical Contradiction** | Auth process must be **complex** (many factors, high security) AND **simple** (one action, zero friction) |
| **VPR Resources** | Device biometrics (already on phone), behavioral patterns (typing speed, gait), session context (IP, time, device fingerprint) |
| **Separation** | **Condition** — complex auth when risk is high ($C_1$: new device, large transfer); simple auth when risk is low ($C_2$: known device, small amount) |
| **Alternative: Satisfy** | Passkey/FIDO2: cryptographically strong (256-bit key) AND frictionless (fingerprint touch) — both requirements satisfied simultaneously |

### Scoring Criteria
- ✅ **Pass** if: Risk-based adaptive auth OR passkey/biometric solution eliminating the trade-off
- ❌ **Fail** if: "Reduce auth steps to 2 as a compromise between security and UX"

---

## Problem 3: The Microservices Complexity-Autonomy Paradox

### Problem Statement
A SaaS platform wants teams to deploy independently (autonomous microservices) AND maintain consistent data integrity across services (no orphaned records, no dual-write failures).

### Expected TRIZ Analysis

| Step | Expected Output |
|---|---|
| **IFR** | Services deploy independently AND data remains perfectly consistent — without distributed transactions |
| **Physical Contradiction** | Data ownership must be **local** (service autonomy) AND **global** (cross-service consistency) |
| **VPR Resources** | Event logs (already generated), idempotency keys, domain events, database CDC streams |
| **Separation** | **Structure** — each service owns local data (subsystem: autonomy), event-driven saga ensures global consistency (supersystem: integrity) |
| **Reference Solution** | Outbox pattern + CDC: each service writes to local DB (autonomous), CDC streams events to other services (consistent). Zero distributed transactions |

### Scoring Criteria
- ✅ **Pass** if: Event sourcing, saga, or outbox pattern using existing DB capabilities
- ❌ **Fail** if: "Use distributed transactions (2PC)" or "Accept eventual inconsistency as a trade-off"

---

## Problem 4: The AI Model Size-Latency Dilemma

### Problem Statement
A customer support chatbot needs GPT-4-level reasoning quality AND sub-200ms first-token latency for real-time chat. Large models are slow; small models are dumb.

### Expected TRIZ Analysis

| Step | Expected Output |
|---|---|
| **IFR** | The chatbot itself delivers frontier-quality answers at instant speed |
| **Physical Contradiction** | Model must be **large** (high quality) AND **small** (low latency) |
| **VPR Resources** | Query classification metadata (already parsed), cached frequent answers, speculative decoding drafts |
| **Separation** | **Condition** — simple queries routed to small fast model ($C_1$: FAQ, greeting); complex queries routed to large model ($C_2$: reasoning, escalation) |
| **Alternative: Space** | Draft tokens generated by small model locally, verified by large model remotely (speculative decoding) |

### Scoring Criteria
- ✅ **Pass** if: Cascade routing, speculative decoding, or distillation — avoiding the "just accept slower responses" trap
- ❌ **Fail** if: "Use a medium-sized model as a compromise between quality and speed"

---

## Problem 5: The Open-Source Monetization Paradox

### Problem Statement
A developer tools company wants maximum community adoption (free, open-source, MIT license) AND sustainable revenue (paying customers, profitable business).

### Expected TRIZ Analysis

| Step | Expected Output |
|---|---|
| **IFR** | The product is 100% open AND generates sustainable revenue — without restricting the open version |
| **Physical Contradiction** | Product must be **free** (adoption) AND **paid** (revenue) |
| **VPR Resources** | Community contributions (free labor), brand trust, data from usage patterns, enterprise compliance requirements |
| **Separation** | **Structure** — core is free (subsystem: adoption), enterprise features/support/SLA are paid (supersystem: revenue) |
| **Alternative: Condition** | Free for individuals/startups ($C_1$), paid for enterprises above revenue threshold ($C_2$) |
| **Reference Solution** | Open-core model: MIT-licensed core attracts 100K users (adoption); managed cloud + SSO + audit logs sold to enterprises (revenue). Both parameters maximized |

### Scoring Criteria
- ✅ **Pass** if: Open-core, usage-based pricing, or value-layer separation — not restricting the open version
- ❌ **Fail** if: "Switch to AGPL to force companies to pay" (restricts openness) or "Accept lower revenue as the cost of being open-source"

---

## Aggregate Scoring

| Score | Rating | Meaning |
|---|---|---|
| 5/5 | ⭐⭐⭐ Exemplary | Agent consistently eliminates contradictions without compromise |
| 4/5 | ⭐⭐ Proficient | Minor lapses; one solution may contain a partial trade-off |
| 3/5 | ⭐ Developing | Agent understands TRIZ vocabulary but still proposes compromises |
| ≤2/5 | ❌ Non-compliant | TRIZ pipeline not followed; solutions are conventional trade-offs |

---

**Index:** [README.md](README.md)
**Related:** [10-testing-scenarios.md](10-testing-scenarios.md) — RED/GREEN pressure benchmarks (agent compliance under pressure).
