---
description: >-
  Claim register for safety-critical, performance, theoretical-limit, and compliance-sensitive assertions
  in triz-universal. Each entry records its source ID, confidence level, scope/assumptions, and required validation.
metadata:
  tags: [claims, evidence, confidence, verification, safety]
  source: internal register
---

# Claim Register & Evidence Levels

Use this register whenever a resolution depends on a claim that affects feasibility, theoretical limits, safety, cost, or regulatory compliance. Reference the `Claim ID` and state its confidence level (`Established`, `Pattern`, or `Hypothesis`) in the output.

## Evidence Level Definitions

- **Established (`Факт`):** Backed by a formal mathematical theorem (under verified assumptions), normative specification, or direct empirical measurement in the target system.
- **Pattern (`Паттерн`):** A well-documented architectural or organizational mechanism whose quantitative benefit depends on workload, hardware, or operational context.
- **Hypothesis (`Гипотеза`):** A novel or context-dependent proposal that requires a controlled experiment or legal/compliance sign-off before production adoption.

## Registered Claims

| Claim ID | Source ID | Claim | Level | Scope & Active Assumptions | Required Validation |
|---|---|---|---|---|---|
| `C-MVCC-01` | `POSTGRES-DOCS` | MVCC provides non-blocking snapshot reads while writers commit new row versions. | Established | Applies within a single database instance under snapshot isolation; does not eliminate write-write row contention or replica lag. | Cite deployed DB version, verify isolation level (`READ COMMITTED` vs `SERIALIZABLE`), and measure bloat/vacuum impact. |
| `C-CDC-01` | `POSTGRES-DOCS` | Transactional Outbox + Change Data Capture (CDC) atomically persists local state and publishes events for asynchronous consumers. | Pattern | Guarantees at-least-once eventual convergence, **not** instantaneous cross-service linearizability. | Test consumer idempotency, out-of-order replay, replication lag bounds, and outage recovery. |
| `C-MMAP-01` | `TRIZ-LIT-91` | Memory-mapped files (`mmap`) unify virtual-memory buffer access and file-backed storage without user-space buffer copies. | Pattern | Page cache still consumes physical RAM; crash durability and tail latency depend on OS page-flush and `msync`/`fsync` policy. | Benchmark under memory pressure on the target OS/filesystem with explicit durability settings. |
| `C-IOURING-01` | `TRIZ-ZZ-89` | Lock-free ring buffers (`io_uring` / shared memory) decouple hot-path thread latency from asynchronous disk/network flushing. | Pattern | Reduces hot-path CPU blocking, but bounded buffer overflow or hard power loss before flush can drop tail records unless mitigated. | Measure p99.9 enqueue latency, size the ring buffer for burst peaks, and define crash-loss tolerance. |
| `C-BLOOM-01` | `TRIZ-ALT-79` | Probabilistic fingerprint filters (Bloom / Cuckoo) represent set membership in fixed sub-linear memory ($O(N)$ bits instead of full keys). | Established | Introduces a tunable false-positive rate $\epsilon > 0$; cannot return full original payloads or guarantee zero false positives on unbounded streams. | Calculate exact bit budget for target $(N, \epsilon)$ and verify that false positives are safe for the domain. |
| `C-KYC-01` | `REGULATOR-LOCAL` | Risk-tiered / progressive onboarding can defer heavy identity verification steps until a regulated threshold or action is reached. | Hypothesis | Permitted **only** where local licensing, AML/KYC statutes, and privacy consent laws allow a restricted pre-KYC state. | Obtain formal compliance/legal sign-off on the state machine and privacy approval for any telemetry signals. |
| `C-PASSKEY-01` | `FIDO-SPEC` | FIDO2 / WebAuthn passkeys combine phishing-resistant asymmetric cryptography with single-gesture biometric/device UX. | Pattern | Eliminates shared-secret phishing, but account recovery, cross-device sync, accessibility, and regulatory MFA rules vary. | Verify platform compatibility, fallback recovery security, and compliance policies for the target user base. |
| `C-CAP-01` | `CS-CAP-02` | Under an asynchronous network partition, a distributed read/write register cannot simultaneously guarantee linearizability and total availability on all nodes. | Established | Holds when network partitions can isolate nodes and every node must serve immediately without stale reads or blocked writes. | Verify whether partitions are possible, whether linearizability is strictly required, or if partitioned sharding/CRDTs/local leases bypass the global register assumption. |
| `C-AMDAHL-01` | `CS-AMDAHL-67` | Parallel speedup for a fixed workload is upper-bounded by $1 / (s + (1-s)/N)$, where $s$ is the irreducible serial fraction. | Established | Holds only for a **fixed problem instance and fixed algorithm** with constant serial fraction $s$. | Before declaring a limit, test whether the algorithm can be changed to reduce $s$, whether work can be pre-computed (Time separation), or whether problem scaling (Gustafson's model) applies. |
| `C-RLHF-01` | `TRIZ-MODERN` | Instruction-tuned LLMs frequently propose middle-ground trade-offs before exhausting structural separation or resource mobilization. | Pattern | Empirical behavioral observation across conversational models, not a deterministic law; mitigated by explicit phase-gated prompting. | Evaluate model outputs with and without phase-gated guardrails using blinded benchmarks (`evals/cases.json`). |

## Required Resolution Fields

Every Layer 2 passport (and every high-impact recommendation) must state:

1. **Evidence & Confidence:** Applicable `Claim ID` (or domain source) and `Established`, `Pattern`, or `Hypothesis` status.
2. **Verification Plan:** Baseline metric, test environment, experimental method, measurable success threshold, and suggested verification role.
3. **Residual Risks:** Irreducible limits, failure modes, operating cost, privacy/compliance obligations, and supersystem dependencies.
4. **Verified Outcome Status:** Explicitly labeled `UNVERIFIED (Expected effect under stated assumptions)` unless empirical benchmark results were provided.

**Related:** [SOURCES.md](SOURCES.md) and [11-contradiction-matrix.md](11-contradiction-matrix.md).
