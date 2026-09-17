---
description: >-
  7 resolution strategies for Physical Contradictions: 4 classical Separation Operators +
  Satisfy, Bypass, and Alternative System Transition. Includes diagnostic questions
  (Zlotin/Zusman) and recommended Inventive Principles per strategy.
metadata:
  tags: [separation-principles, physical-contradiction, space, time, condition, structure, satisfy, bypass, litvin, zlotin-zusman, multi-domain]
  source: TRIZ-Classical (Litvin, Zlotin/Zusman)

# 03. Resolution Strategies for Physical Contradictions

When an atomic Physical Contradiction ($X$ must be $P$ and $\neg P$) has been formulated, apply these 7 strategies. Start with Diagnostic Questions to narrow the search, then try each applicable strategy.

## Diagnostic Questions (Zlotin/Zusman Navigation)

| Question | If YES → Try Strategy | Rationale |
|---|---|---|
| **WHERE** must $X$ be $P$ and $\neg P$? In different locations? | → **1. Separation in Space** | Spatial boundary exists |
| **WHEN** must $X$ be $P$ and $\neg P$? At different times? | → **2. Separation in Time** | Temporal boundary exists |
| **UNDER WHAT CONDITION** must $X$ be $P$ and $\neg P$? | → **3. Separation by Condition** | Conditional trigger exists |
| Do **parts** need $P$ while the **whole** needs $\neg P$? | → **4. Separation by Structure** | Micro/macro boundary exists |
| Can one resource deliver **both** $P$ and $\neg P$ at once? | → **5. Satisfy** | No separation needed |
| Can the problem be **reformulated** so $P$ vs $\neg P$ vanishes? | → **6. Bypass** | Contradiction is artificial |
| Can the **entire system** be replaced? | → **7. Alternative System** | System is fundamentally wrong |

## Recommended Inventive Principles per Strategy

| Strategy | Primary Principles (from 40) |
|---|---|
| 1. Space | 1 (Segmentation), 2 (Taking Out), 3 (Local Quality), 4 (Asymmetry), 7 (Nested Doll), 17 (Another Dimension) |
| 2. Time | 9 (Preliminary Anti-Action), 10 (Preliminary Action), 11 (Beforehand Cushioning), 15 (Dynamics), 16 (Partial/Excessive Action), 21 (Skipping) |
| 3. Condition | 28 (Mechanics Substitution), 31 (Porous Materials), 35 (Parameter Changes), 36 (Phase Transitions), 38 (Strong Oxidants), 39 (Inert Atmosphere) |
| 4. Structure | 1 (Segmentation), 5 (Merging), 6 (Universality), 22 (Blessing in Disguise), 33 (Homogeneity), 40 (Composite Materials) |
| 5. Satisfy | 13 (The Other Way Around), 22 (Blessing in Disguise), 25 (Self-Service), 35 (Parameter Changes) |
| 6. Bypass | 12 (Equipotentiality), 13 (The Other Way Around), 22 (Blessing in Disguise), 27 (Cheap Short-Living) |
| 7. Alternative | 34 (Discarding and Recovering), 25 (Self-Service), 28 (Mechanics Substitution) |

## Strategy Map

```
                  ┌─────────────────────────────────────────┐
                  │ PHYSICAL CONTRADICTION: X is P and NOT-P│
                  └────────────────────┬────────────────────┘
                                       │
          ┌────────────┬───────────────┼───────────────┬────────────┐
          ▼            ▼               ▼               ▼            ▼
   [1. In Space]  [2. In Time]  [3. By Condition] [4. By Structure]│
    Zone 1: P      Time 1: P     Cond 1: P        Subsystem: P    │
    Zone 2: ¬P     Time 2: ¬P    Cond 2: ¬P       Supersystem: ¬P │
                                                          ┌────────┘
          ┌───────────────────┬───────────────────┐       │
          ▼                   ▼                   ▼       ▼
   [5. Satisfy]          [6. Bypass]        [7. Alternative System]
    Both P and ¬P         Reformulate        Replace system
    simultaneously        the problem         entirely
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

## 5. Satisfy — Meet Both Requirements Simultaneously (Litvin)

### Heuristic Rule:
Find a single resource, mechanism, or design that delivers **both** $P$ and $\neg P$ at the same time, without any separation. The contradiction dissolves because the element inherently satisfies both needs.

### Key Probing Questions:
- Is there a known resource that naturally combines properties $P$ and $\neg P$?
- Can we transform the element so it exhibits both properties as a single state?

### Multi-Domain Patterns:
* **Software & Systems:**
  - *Memory-mapped files:* Data is simultaneously **on disk** (persistent, crash-safe) AND **in RAM** (fast random access) — the OS page cache makes both true at once.
  - *Append-only logs (LSM trees):* Writes are **sequential** (fast I/O) AND **durable** (persisted immediately) — no trade-off between write speed and durability.
* **AI Agents & LLMs:**
  - *FIDO2/Passkeys:* Authentication is **cryptographically strong** (256-bit key, phishing-resistant) AND **frictionless** (fingerprint touch, zero passwords) — both security and UX maximized simultaneously.
* **Business & Strategy:**
  - *Freemium with network effects:* Product is **free** (maximum adoption) AND **profitable** (every free user makes the product better for paid users via data/network effects).
* **Physical Engineering:**
  - *Aerogel insulation:* Material is **extremely light** (99.8% air) AND **extremely insulating** (lowest thermal conductivity of any solid) — both properties coexist inherently.

---

## 6. Bypass — Reformulate to Eliminate the Contradiction (Litvin)

### Heuristic Rule:
The contradiction exists because of how the **problem was framed**, not because of physical laws. Redefine the goal, the system boundary, or the function so that the conflicting requirements no longer apply.

### Key Probing Questions:
- Why do we need element $X$ at all? Can its function be performed another way?
- Are we solving the **right problem**, or are we optimizing a symptom?
- Would moving one level up in the system hierarchy make this contradiction irrelevant?

### Multi-Domain Patterns:
* **Software & Systems:**
  - *"You need a faster cache" → "You need fewer cache misses" → Pre-compute and embed results in the response itself.* The contradiction (cache size vs memory) vanishes because there's no cache.
  - *"Database must be consistent AND fast" → "Do we need a database? Can we use a compiled static site?"* — Bypass: remove the database entirely.
* **AI Agents & LLMs:**
  - *"Model must be large (smart) AND small (fast)" → "Does the user need the model at all? Pre-generate the top-100 answers and serve from a lookup table."* — Most queries are repetitive.
* **Business & Strategy:**
  - *"We need expensive senior engineers AND must cut costs" → "Do we need engineers for THIS task? Can a no-code tool or AI agent replace the engineering work?"* — Eliminate the need.
* **Physical Engineering:**
  - *"Bridge must be long (span the river) AND short (cheap)" → "Do we need a bridge? A tunnel, cable car, or ferry might bypass the constraint entirely."*

---

## 7. Alternative System Transition (Zlotin/Zusman)

### Heuristic Rule:
When the physical contradiction is inherent to the **system type itself**, resolve it by transitioning to a fundamentally different system that doesn't have this contradiction. This is the most radical strategy.

### Key Probing Questions:
- Does another system type solve the same problem without this trade-off?
- Is the current system approaching the end of its S-curve evolution?
- What would a next-generation system look like?

### Multi-Domain Patterns:
* **Software & Systems:**
  - *Monolith → Serverless:* Instead of optimizing a monolith's scaling vs complexity trade-off, transition to an event-driven serverless architecture where the contradiction doesn't exist.
  - *SQL → Event Sourcing:* Instead of balancing read/write performance in a relational DB, transition to a system where reads and writes are fundamentally different operations.
* **AI Agents & LLMs:**
  - *Single LLM → Multi-Agent Swarm:* Instead of making one model smart AND fast, transition to a system of specialized agents where each is optimized for one dimension.
* **Business & Strategy:**
  - *Ownership → Platform:* Instead of solving "must own inventory (control) AND not own inventory (low risk)", transition to a marketplace model where the contradiction vanishes (Airbnb, Uber).
* **Physical Engineering:**
  - *Internal combustion → Electric:* Instead of optimizing fuel efficiency vs power, transition to electric motors where the torque-efficiency trade-off is fundamentally different.

---

## Comparison: Litvin vs Zlotin/Zusman Frameworks

| Aspect | Litvin | Zlotin/Zusman |
|---|---|---|
| **Strategies** | 6 (Space, Time, Parts/Whole, Condition, Satisfy, Bypass) | 5 (Space, Time, Condition, Parts/Whole, Alternative System) |
| **Navigation** | Sequential by frequency | Diagnostic questions (Where? When? Under what condition?) |
| **Unique strengths** | Satisfy and Bypass | Diagnostic questions and Alternative System |
| **Best for** | Clear contradictions with known system boundaries | Unclear contradictions needing rapid diagnosis |

**Recommendation:** Use Zlotin/Zusman diagnostic questions first (quick navigation), then try Litvin's Satisfy and Bypass if classical separation fails.

---

**Next:** [04-ariz-lite-algorithm.md](04-ariz-lite-algorithm.md) — The ARIZ-AI Operational Protocol.
**Related:** [11-contradiction-matrix.md](11-contradiction-matrix.md) — Lookup recommended principles by parameter pair.
**Index:** [README.md](README.md)
