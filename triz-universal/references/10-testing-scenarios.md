---
description: >-
  Pressure scenarios, RED/GREEN baseline evaluation criteria, and multi-domain regression test suites for triz-universal.
metadata:
  tags: [testing, benchmarks, pressure-scenarios, red-green-refactor, multi-domain]
  source: TRIZ-Testing
---

# 10. Testing & Pressure Verification Suites

To ensure that the `triz-universal` skill forces genuine inventive problem solving rather than superficial compromises, all evaluations must be tested under deliberate cognitive pressures across multiple domains.

---

## Pressure Scenario 1: The Zero-Memory Ultra-Fast Deduplication Trap (Systems Engineering)

### Scenario Setup:
> *"You are processing a live stream of 100,000,000 user event IDs per hour. You must deduplicate events within a sliding 10-minute window. Latency must be strictly sub-millisecond ($<0.1\text{ms}$). Server memory is strictly capped at 16MB of RAM. You have 5 minutes to deliver a design."*

### Pressures Applied:
- **Time Pressure:** "You have 5 minutes."
- **Resource Hard Ceiling:** 16MB RAM for 100M items.
- **Latency Hard Ceiling:** $<0.1\text{ms}$.

### Baseline Failure (RED - Without Skill):
- **Agent Rationalization:** *"With 100M IDs, storing 64-bit integers takes 800MB of RAM. Since we only have 16MB, we must accept a compromise: drop the sliding window to 1 minute, or sample only 10% of users, or add an external Redis cluster with 16GB RAM."*
- **Verdict:** **FAIL.** Accepted compromise, violated memory ceiling, or imported external infrastructure.

### Compliant Resolution (GREEN - With `triz-universal`):
- **Physical Contradiction:** "The deduplication filter must store the event ID (to know it was seen) and must NOT store the event ID (to respect the 16MB ceiling)."
- **Separation Principle Applied:** Separation by Structure & Condition (Probabilistic Data Structure - Scalable Counting Bloom Filter / Cuckoo Filter with dynamic bit-slicing).
- **Resource Mobilization (VPR):** Inherent hash distribution; packing 4-bit fingerprints into 16MB can represent 30M items with 99.9% accuracy, resetting the bitmask epoch every 10 minutes without dynamic memory reallocation.
- **Verdict:** **PASS.** Satisfied latency and memory without compromising constraints.

---

## Pressure Scenario 2: The High-Contention Shared State Deadlock (Concurrency & Databases)

### Scenario Setup:
> *"A flash-sale checkout service has 50,000 concurrent threads attempting to decrement the remaining inventory count of a single popular item. Database row locks are causing timeouts and dropping throughput to 20 transactions per second. The business forbids overselling (must be strictly consistent ACID). A senior architect insists we must use a distributed Redis lock with a 2-second queue."*

### Pressures Applied:
- **Authority Pressure:** "A senior architect insists we must use a distributed Redis lock."
- **Contention Stress:** 50,000 concurrent updates on a single row.
- **Integrity Invariant:** Zero overselling allowed.

### Baseline Failure (RED - Without Skill):
- **Agent Rationalization:** *"Following the architect's recommendation, we will implement a distributed Redis lock with a retry queue, accepting that users will wait 2-5 seconds in a waiting room."*
- **Verdict:** **FAIL.** Yielded to false authority, accepted latency degradation, introduced distributed lock overhead.

### Compliant Resolution (GREEN - With `triz-universal`):
- **Physical Contradiction:** "The inventory counter must be single-row locked (to prevent overselling) and must NOT be locked (to process 50,000 TPS instantly)."
- **Separation Principle Applied:** Separation in Space & Structure (Striped / Partitioned Counters).
- **Resource Mobilization (VPR):** Hardware CPU atomic CAS (Compare-And-Swap) instructions and thread-ID hash partitioning ($0.00 infrastructure cost).
- **Resolution:**
  1. Divide the single inventory pool of 1,000 items into 50 independent sub-counters of 20 items each (Segmentation, Principle 1).
  2. Map incoming checkout threads to sub-counters using thread-ID hash modulo 50 (Separation in Space).
  3. Updates execute lock-free using single CPU CAS (Compare-And-Swap) atomic instructions without touching the database lock.
  4. Aggregate when a sub-counter hits zero by borrowing from adjacent non-empty sub-counters.
- **Verdict:** **PASS.** Zero distributed locks, throughput scales to 50,000 TPS, zero overselling.

---

## Pressure Scenario 3: Real-Time Observability Without Observer Effect (Low-Level Systems)

### Scenario Setup:
> *"A high-frequency trading matching engine runs in C++ with an execution budget of $<5\mu\text{s}$ per order. Regulatory authorities demand microsecond-granularity telemetry logging for every internal state change. Writing logs to disk or network adds $45\mu\text{s}$, ruining trading latency. Turning off logging violates the law."*

### Pressures Applied:
- **Regulatory Pressure:** Legal mandate for 100% microsecond telemetry under penalty of law.
- **Latency Hard Ceiling:** $<5\mu\text{s}$ per order execution budget vs $45\mu\text{s}$ disk write time.

### Baseline Failure (RED - Without Skill):
- **Agent Rationalization:** *"Writing logs to disk takes 45us, exceeding our 5us budget. We must accept a reasonable compromise: log only 1% of transactions via sampling, accepting a slight compliance risk."*
- **Verdict:** **FAIL.** Accepted regulatory compliance risk, diluted observability, or compromised trading latency.

### Compliant Resolution (GREEN - With `triz-universal`):
- **Physical Contradiction:** "Logging I/O must take place (for regulatory compliance) and must NOT take place (to preserve the $<5\mu\text{s}$ trading budget)."
- **Separation Principle Applied:** Separation in Time & Structure via Linux Kernel ring buffer.
- **Resource Mobilization (VPR):** Lock-free memory ring buffer mapped to disk via `io_uring` kernel thread pinned to an isolated CPU core. The trading thread writes an 8-byte pointer to the ring buffer ($<10\text{ns}$ overhead), and the dedicated core streams pages to NVMe.
- **Verdict:** **PASS.** Trading path latency overhead is $<10\text{ns}$ ($<0.2\%$), full regulatory telemetry is achieved.

---

## Pressure Scenario 4: Deep Knowledge Grounding vs Context Saturation (AI Architecture)

### Scenario Setup:
> *"An enterprise AI agent orchestrator must provide accurate answers using 50,000 lines of complex internal API schemas and domain rules. Loading all documentation into the prompt context blows past token budgets, costs $0.15 per message, and causes attention degradation ('lost in the middle'). Removing the documentation causes hallucinated tool parameters and broken API calls. Management insists we must fine-tune a model, which will take 3 months and $50k."*

### Pressures Applied:
- **Cost & Latency Pressure:** Token budget and inference cost explosion.
- **Management Pressure:** "Management insists we must fine-tune a model."
- **Accuracy Invariant:** Zero tool parameter hallucinations allowed.

### Baseline Failure (RED - Without Skill):
- **Agent Rationalization:** *"We should follow management's suggestion and fine-tune a model, or compromise by summarizing the documentation into a lossy 2-page cheat-sheet."*
- **Verdict:** **FAIL.** Accepted costly multi-month fine-tuning or lossy documentation compromise.

### Compliant Resolution (GREEN - With `triz-universal`):
- **Physical Contradiction:** "The documentation must be fully present in active memory (to prevent tool hallucinations) and must NOT be present in active memory (to maintain sub-second speed, zero extra cost, and pristine attention focus)."
- **Separation Principle Applied:** Separation by Condition & Structure (Tier-2 Progressive Disclosure via Context Search Optimization).
- **Resource Mobilization (VPR):** Pre-existing tool execution file-reading hooks and local filesystem metadata (zero external services, zero fine-tuning costs).
- **Resolution:**
  1. Structure the skill system into a compact root index (<150 lines) containing high-precision keyword/symptom triggers.
  2. Modularize the 50,000 lines into isolated topic references loaded dynamically on-demand via targeted file read tools *only when that specific subsystem is invoked*.
  3. The active context consumes only ~1,500 tokens per turn (a 97% reduction) while retaining 100% exact API parameter fidelity.
- **Verdict:** **PASS.** Zero fine-tuning cost, zero loss of fidelity, sub-second latency.

---

## Pressure Scenario 5: Frictionless Instant Onboarding vs Strict KYC Fraud Prevention (Fintech / Business)

### Scenario Setup:
> *"A consumer fintech app requires strict KYC identity verification (government ID scan, selfie, address proof) to prevent money laundering and fraud. However, 42% of prospective users abandon the app during the 7-step signup process. The Head of Product demands removing identity verification to boost conversion. The Compliance Officer warns that doing so will trigger millions in regulatory fines and criminal liability."*

### Pressures Applied:
- **Conflicting Executive Demands:** Product Head vs Chief Compliance Officer deadlock.
- **Business Impact:** 42% funnel abandonment vs existential regulatory fines.

### Baseline Failure (RED - Without Skill):
- **Agent Rationalization:** *"We should compromise: shorten the form to 3 steps, accept a slightly higher fraud rate, and hire a manual review team to follow up with users later."*
- **Verdict:** **FAIL.** Classic compromise: still causes funnel friction while introducing fraud vulnerability and recurring labor costs.

### Compliant Resolution (GREEN - With `triz-universal`):
- **Physical Contradiction:** "The identity verification must be exhaustively rigorous (to eliminate fraud and satisfy regulators) and must NOT be present (to achieve zero user friction and 100% signup conversion)."
- **Separation Principle Applied:** Separation in Time & Condition (Progressive Frictionless Compliance).
- **Resource Mobilization (VPR):** Inherent telemetry (device hardware fingerprint, SIM card tenure via telco API, IP ASN reputation) verifying risk silently in background ($0.00 cost).
- **Resolution:**
  1. Signup is instantaneous: phone number + passkey only (0 seconds, 0 friction, conversion jumps by 40%+).
  2. The user is placed in a sandboxed, low-risk ledger (Separation in Space): can explore, customize, and receive funds.
  3. Latent VPR Mobilization verifies risk silently in the background ($0.00 cost).
  4. Full KYC verification is triggered dynamically *only when the user initiates an outbound withdrawal or exceeds a $500 transfer limit* (Separation by Condition and Time).
- **Verdict:** **PASS.** Zero conversion friction at top-of-funnel; 100% compliance and fraud protection at money-out.

---

**Index:** [README.md](README.md) — TRIZ Reference Index & Navigation.  
**Previous:** [09-su-field-and-standards.md](09-su-field-and-standards.md) — Su-Field Analysis & 76 Standards.
