---
description: >-
  Detailed heuristics and multi-domain patterns for applying the 4 Separation Principles to Physical Contradictions.
metadata:
  tags: [separation-principles, physical-contradiction, space, time, condition, structure, multi-domain]
  source: TRIZ-Classical & Modern
---

# 03. The 4 Separation Principles (Multi-Domain Heuristics)

When an atomic Physical Contradiction ($X$ must be $P$ and $\neg P$) has been formulated, it is guaranteed to be resolvable through one of four universal separation operators:

```
                  ┌─────────────────────────────────────────┐
                  │ PHYSICAL CONTRADICTION: X is P and NOT-P│
                  └────────────────────┬────────────────────┘
                                       │
     ┌───────────────────┬─────────────┴─────┬───────────────────┐
     ▼                   ▼                   ▼                   ▼
[1. In Space]       [2. In Time]     [3. By Condition]   [4. By Structure]
 Zone 1: P           Time 1: P        Condition 1: P      Subsystem: P
 Zone 2: NOT-P       Time 2: NOT-P    Condition 2: NOT-P  Supersystem: NOT-P
```

---

## 1. Separation in Space (Разделение в пространстве)

### Heuristic Rule:
Requirement $P$ and requirement $\neg P$ are assigned to different physical, logical, geographic, or architectural locations.

### Key Probing Questions:
- Is property $P$ genuinely needed everywhere across the entire system, or only within a localized boundary?
- Can we carve out a protected zone where $P$ operates, while $\neg P$ holds across the rest of the space?

### Multi-Domain Patterns:
* **Software & Systems:**
  - *CQRS (Command Query Responsibility Segregation):* Write path (isolated, strict validation, high consistency) occupies a separate logical service from Read path (denormalized, high throughput, zero locks).
  - *Database Sharding & Memory Tiering:* Hot mutable rows partitioned to in-memory L1 cache/stack (Zone 1); cold historical rows stored in compressed Parquet/NVMe (Zone 2).
* **AI Agents & LLMs:**
  - *Zoned Memory Architecture:* Short-term working scratchpad in local token context (Zone 1); massive long-term domain knowledge stored externally in indexed vector/document stores (Zone 2).
* **Business & Strategy:**
  - *Market Segment Tiering:* High-touch bespoke services for Enterprise accounts ($P$ in Enterprise Zone); self-serve automated freemium for individual users ($\neg P$ in Retail Zone).
* **Physical Engineering:**
  - *Bimetallic Thermostats & Icebreaker Hulls:* Hull is narrow and razor-sharp at the water cut-line (to slice ice), but wide and flat above the waterline (to carry cargo).

---

## 2. Separation in Time (Разделение во времени)

### Heuristic Rule:
Requirement $P$ is active during time interval $T_1$, and requirement $\neg P$ is active during time interval $T_2$.

### Key Probing Questions:
- Does property $P$ need to operate continuously, or only at specific discrete moments?
- Can the conflicting actions take place sequentially rather than concurrently?

### Multi-Domain Patterns:
* **Software & Systems:**
  - *MVCC (Multi-Version Concurrency Control):* Readers read historical snapshots at timestamp $T_{\text{snapshot}}$ with zero locks, while writers write new versions at $T_{\text{commit}}$.
  - *Static Pre-Computation (SSG / JIT):* Heavy CPU rendering executed during build time ($T_1$); runtime request serving ($T_2$) is an instant static memory read.
* **AI Agents & LLMs:**
  - *Phased Deliberation (Fast vs Slow Thinking):* Fast reactive token streaming during interactive conversation ($T_1$); asynchronous deep planning and tool execution during scheduled background cycles ($T_2$).
* **Business & Strategy:**
  - *Surge & Off-Peak Pricing:* Peak commute hours prioritize throughput and high margins ($T_1$); off-peak night hours prioritize fleet utilization and deep discounts ($T_2$).
* **Physical Engineering:**
  - *Retractable Aircraft Landing Gear:* Wheels exist and absorb shock during takeoff and touchdown ($T_1$), and vanish into the fuselage during cruise flight to eliminate aerodynamic drag ($T_2$).

---

## 3. Separation by Condition / Relation (Разделение по условию / в отношениях)

### Heuristic Rule:
Element $X$ exhibits property $P$ under environmental/contextual condition $C_1$, and automatically exhibits $\neg P$ under condition $C_2$ (or relative to observer $A$ vs observer $B$).

### Key Probing Questions:
- Can an external trigger, load threshold, risk score, or caller identity dynamically switch the element's behavior?
- Is property $P$ required for all requests, or only when an anomaly occurs?

### Multi-Domain Patterns:
* **Software & Systems:**
  - *Circuit Breakers & Adaptive Caching:* Execute live network calls when upstream health is normal ($C_1$); switch to instant cached fallbacks when error rates cross 5% ($C_2$).
  - *Optimistic vs Pessimistic Concurrency:* Update lock-free under low contention ($C_1$); escalate to pessimistic locks only when hot-key collision rate spikes ($C_2$).
* **AI Agents & LLMs:**
  - *Speculative Decoding & Cascade Routing:* Route simple user queries to tiny 3B model ($C_1$); escalate only complex reasoning tasks to 400B frontier model ($C_2$).
* **Business & Strategy:**
  - *Dynamic Risk-Based KYC:* Allow 1-click zero-friction checkout for known loyal customers ($C_1$); inject multi-factor biometric authentication only when geolocation or transaction amount is suspicious ($C_2$).
* **Physical Engineering:**
  - *Photochromic Eyeglasses & Non-Newtonian Fluids:* Glass remains clear indoors ($C_1$) but darkens into sunglasses under intense UV light ($C_2$). Body armor fluid remains flexible during normal motion ($C_1$) but instantly hardens into rigid armor upon high-velocity ballistic impact ($C_2$).

---

## 4. Separation by Structure / System Transition (Системный переход)

### Heuristic Rule:
At the micro-level (subsystems or individual components), property $P$ is present; at the macro-level (the aggregated whole or supersystem), emergent property $\neg P$ is manifested (or vice versa).

### Key Probing Questions:
- Can a collection of elements with property $P$ combine to produce an overall system with emergent property $\neg P$?
- Can we offload property $\neg P$ to the supersystem while keeping individual components minimal?

### Multi-Domain Patterns:
* **Software & Systems:**
  - *Raft / Paxos Consensus Clusters:* Individual server nodes are unreliable and fail frequently ($P$); the distributed cluster as a collective whole is 99.999% available and fault-tolerant ($\neg P$).
  - *Actor Concurrency (Erlang / Akka):* Each individual actor is strictly single-threaded with zero lock complexity ($P$); the system of 100,000 actors executing concurrently achieves massive parallel throughput ($\neg P$).
* **AI Agents & LLMs:**
  - *Multi-Agent Swarm Orchestration:* Each individual subagent has a narrow, single-purpose context with zero complexity ($P$); the synthesized collective agent network solves massive enterprise workflows ($\neg P$).
* **Business & Strategy:**
  - *Franchise & Decentralized Autonomous Organizations (DAOs):* Individual franchise owners have 100% entrepreneurial local autonomy ($P$); the global franchise brand enforces uniform global quality and supply chain pricing ($\neg P$).
* **Physical Engineering:**
  - *Bicycle Chains & Carbon Nanotubes:* Each individual steel link is completely rigid and inflexible ($P$); the linked assembly is entirely flexible and pliable ($\neg P$).

---

**Next:** [04-ariz-lite-algorithm.md](04-ariz-lite-algorithm.md) — The ARIZ-AI Operational Protocol.  
**Index:** [README.md](README.md)
