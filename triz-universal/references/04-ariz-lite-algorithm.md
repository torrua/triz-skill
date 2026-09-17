---
description: >-
  Detailed operational protocol for running ARIZ-AI (distilled 5-step algorithm) with end-to-end case studies across domains.
metadata:
  tags: [ariz, ariz-ai, algorithm, inventive-step, execution, case-studies]
  source: TRIZ-Classical & Modern
---

# 04. The ARIZ-AI Operational Protocol

ARIZ-AI is a deterministic execution protocol designed for AI agents. It compresses the cognitive bureaucracy of Altshuller's ARIZ-85B into a 5-step recursive contraction that prevents LLM context drift while maintaining dialectical rigor.

---

## The 5-Step Execution Workflow

```
[Step 1: Demarcation] ──► [Step 2: Sharpening] ──► [Step 3: Mobilization]
         │                          │                         │
  • Mini-Problem             • Dual TCs                • Define OZ / OT
  • IFR Statement            • Extreme Limits          • VPR Inventory
  • Scope Fence              • Canonical PC            • Waste Utilization
                                                              │
[Step 5: Verification] ◄── [Step 4: Transformation] ◄───────┘
         │                          │
  • Zero Degradation Check   • Space Separation
  • Anti-Harm Audit          • Time Separation
  • 9-Screens Future Check   • Condition Separation
                             • Structure Separation
```

---

## Detailed Step-by-Step Instructions

### Step 1: Mini-Problem & IFR Formulation
1. **Define the Mini-Problem:** Describe the existing system without introducing any new hardware, servers, dependencies, staff, or budget.
2. **Formulate the IFR:** State that the required function must be delivered with $0.00 extra cost and zero added architectural complexity by utilizing the system's own properties.
3. **Fence the Problem:** Explicitly reject conventional external "solutions" (e.g., "We will NOT solve this by adding an external cache, another microservice, or hiring manual reviewers").

### Step 2: Sharpening the Physical Contradiction (PC)
1. **Formulate Dual $\text{TC}_1$ and $\text{TC}_2$:**
   - $\text{TC}_1$: Improving metric $A$ degrades metric $B$.
   - $\text{TC}_2$: Preserving metric $B$ prevents metric $A$ from reaching its target.
2. **Isolate Conflicting Element $X$:** Find the single operational component where the requirements collide.
3. **Drive to Extremes:** State metric $A \to \infty$ and metric $B \to 0$.
4. **Formulate Canonical PC:**
   $$\text{Element } X \text{ must be } [P] \text{ to satisfy } [R_1] \text{ AND } [\neg P] \text{ to satisfy } [R_2]$$

### Step 3: Substance-Field Resource Audit (ВПР)
1. **Operational Zone (OZ):** Pinpoint the exact memory address, CPU register, database row, network packet, prompt context window, or checkout screen where the contradiction occurs.
2. **Operational Time (OT):** Pinpoint the exact duration before, during, and after the conflict.
3. **Audit Latent Resources:**
   - What fields or cycles are already allocated but idle?
   - Can the error signal or waste byproduct be used to trigger the fix?
   - What supersystem capabilities (OS kernel, client GPU, user intent) exist for free?

### Step 4: Apply the 4 Separation Operators
Apply the 4 separation heuristics systematically:
1. **Separation in Space:** (Partition, zone separation, local path optimization).
2. **Separation in Time:** (Pre-compute, asynchronous delay, phase transition).
3. **Separation by Condition:** (Threshold-based branching, dynamic context routing).
4. **Separation by Structure:** (Subsystem vs Supersystem emergent property).

### Step 5: Verification & Secondary Harm Audit
1. **Check Parameter $A$:** Did target performance achieve the goal?
2. **Check Parameter $B$:** Is there zero regression in the opposing constraint?
3. **Secondary Harm:** Did the change introduce a new bottleneck, security vulnerability, or technical debt? If yes, apply ARIZ-AI recursively to the secondary contradiction.

---

## End-to-End Case Studies Across Domains

### Case Study 1 (Systems Engineering): High-Frequency Audit Logging
- **Context:** Payment processor must log 50,000 transaction audit records per second with cryptographic verification.
- **Sharpened PC:** The audit logging must be **synchronous and blocking** (to guarantee zero audit loss on crash) and must be **asynchronous and non-blocking** (to guarantee zero added latency to the payment write path).
- **VPR Mobilized:** Linux kernel memory-mapped ring buffer (`mmap` / `io_uring`) and sequential WAL offsets.
- **Separation Applied:** Separation in Time & Structure. Application thread writes an 8-byte pointer to an in-memory ring buffer ($<10\mu\text{s}$); OS kernel asynchronously commits dirty pages to disk.
- **Outcome:** Payment latency overhead is $<10\mu\text{s}$ ($0.01\text{ms}$); zero audit records lost even during hard power-loss.

### Case Study 2 (AI Cognitive Systems): Deep API Grounding vs Context Saturation
- **Context:** An AI coding assistant needs accurate knowledge of 500 API endpoints across 12 services, but injecting the full schema consumes 80,000 tokens, degrading response latency and reasoning focus.
- **Sharpened PC:** The API documentation must be **present in context** (to avoid tool call hallucinations) and must **NOT be present in context** (to prevent token saturation and preserve fast inference).
- **VPR Mobilized:** The agent's existing tool-calling mechanism and file system metadata.
- **Separation Applied:** Separation by Condition & Structure (Tier-2 Progressive Disclosure). The agent loads a concise dispatcher table ($<100$ lines). Detailed schemas are fetched on-demand via targeted read tools only when the specific tool name is invoked.
- **Outcome:** Context consumption drops by 98% (from 80k to 1.5k tokens); API hallucination drops to zero.

### Case Study 3 (Business Strategy / Fintech): Frictionless Fraud Prevention
- **Context:** An e-commerce platform suffers \$2M/year in credit card chargebacks. Adding 3D-Secure 2.0 OTP verification eliminates fraud but causes a 35% drop in checkout conversion.
- **Sharpened PC:** The authentication barrier must be **maximally intrusive and strict** (to block 100% of stolen card fraud) and must be **completely non-existent** (to achieve instantaneous 1-click conversion).
- **VPR Mobilized:** Inherent user telemetry: device hardware fingerprint, typing cadence, IP ASN reputation, and transaction history.
- **Separation Applied:** Separation by Condition. 98% of clean transactions pass through seamless 1-click checkout with zero OTP steps; intrusive 2FA is triggered only when the anomaly score exceeds 0.85.
- **Outcome:** 1-click conversion preserved for 98% of legitimate buyers; fraudulent transactions blocked with zero loss.

---

**Next:** [05-40-principles-catalog.md](05-40-principles-catalog.md) — The 40 Inventive Principles Catalog.  
**Index:** [README.md](README.md)
