---
description: >-
  Guide for identifying and exploiting hidden Substance-Field Resources (VPR / ВПР) across software, AI systems, and business operations.
metadata:
  tags: [vpr, resources, zero-cost, memory-audit, temporal-audit, multi-domain]
  source: TRIZ-Classical & Modern
---

# 07. Substance-Field & Latent Resource Audit (ВПР)

> *"The highest art of invention is to solve a problem using the very thing that caused the problem."* — Genrich Altshuller

In classical TRIZ, **Substance-Field Resources (ВПР)** are substances and fields present in or around the system that can be mobilized for free ($0.00). In digital, software, AI, and organizational systems, resources are abundant, but engineers and managers suffer from "resource blindness."

---

## 1. The Multi-Domain Resource Matrix

| Resource Category | What It Is | How to Mobilize for $0.00 | Real-World Multi-Domain Examples |
|---|---|---|---|
| **Temporal Resources** | Idle CPU slots, wait intervals, latency gaps, off-peak hours. | Execute speculative computation or background warming during unavoidable wait states. | • *Software:* Pre-fetching next page during user reading time.<br>• *AI:* Running chain-of-thought planning during token streaming idle phases.<br>• *Business:* Off-peak batch data reconciliation at 3:00 AM. |
| **Spatial / Memory Resources** | Unused bits, struct alignment padding, cache lines, whitespace. | Pack bitflags or metadata into unused structural padding without allocating extra memory. | • *Software:* Pointer tagging using the 16 unused bits in 64-bit virtual memory addresses (V8 / LuaJIT).<br>• *AI:* Reusing attention key-value cache across identical system prompt prefixes.<br>• *Business:* Repurposing empty delivery van backhauls to carry partner cargo. |
| **Informational Resources** | Natural data ordering, timestamps, hashes, idempotency tokens. | Leverage inherent mathematical properties of the data stream instead of building auxiliary index tables. | • *Software:* Using monotonically increasing database autoincrement IDs as natural time fences.<br>• *AI:* Inherent token probability distributions used directly as confidence scores.<br>• *Business:* Using credit card billing postal codes for automatic localized sales tax calculation. |
| **Problem-Generated Waste** | Error logs, discarded packets, backpressure signals, cache misses. | Convert the harmful byproduct into a useful control signal, feedback loop, or training dataset. | • *Software:* Using cache-miss frequency to dynamically trigger JIT compilation.<br>• *AI:* Failed tool executions automatically formatted into negative few-shot correction examples.<br>• *Business:* Failed customer onboarding drop-off logs automatically triggering localized UX simplifications. |
| **Supersystem Resources** | Operating system kernel, cloud network fabric, client hardware. | Offload computation from application user-space to OS kernel or client device. | • *Software:* Zero-copy file transfers using Linux `sendfile` / `splice`.<br>• *AI:* Offloading token filtering and grammar verification to local client WebAssembly engines.<br>• *Business:* Leveraging existing corporate distribution channels (e.g., Slack App Directory). |
| **Differential Resources** | Gradients of read vs write traffic, hot vs cold data, peak vs off-peak. | Apply asymmetric architectures tuned precisely to the operational gradient. | • *Software:* CQRS separating read paths from write paths based on 100:1 asymmetry.<br>• *AI:* Routing 90% of simple requests to 3B model, reserving 400B model for 10% complex queries.<br>• *Business:* Freemium self-serve tier subsidizing high-touch enterprise sales pipeline. |

---

## 2. The 4-Step Resource Extraction Procedure

When executing Step 3 of ARIZ-AI, run through these 4 diagnostic probes:

### Probe 1: What is already free inside the Operational Zone?
- Look at the variables or elements already in scope. Can an existing field carry a second function (Principle 6 - Universality)?
- Look at memory or physical layout. Is there unused padding, unused bits, or empty capacity?

### Probe 2: What is already occurring in the Operational Time?
- What is the CPU core or worker thread doing while waiting for network I/O?
- Can we perform work *before* the request arrives (Principle 10 - Preliminary Action)?

### Probe 3: What is the supersystem doing?
- Can the underlying database engine compute this aggregation via a window function instead of transferring 50,000 rows into application memory?
- Can the client device execute validation locally instead of dispatching an HTTP round-trip?

### Probe 4: How can the harm itself be converted into the solution (Principle 22)?
- If lock contention or high error rates are occurring, can the failing thread immediately batch and execute pending transactions from other waiting threads (Group Commit)?

---

**Next:** [08-multi-domain-lenses.md](08-multi-domain-lenses.md) — Multi-Domain Translation Lenses.  
**Index:** [README.md](README.md)
