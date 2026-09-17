---
description: >-
  Substance-Field (Su-Field / Веполь) analysis, MATChEM field taxonomy, and the 5 Classes of Standard Inventive Solutions adapted for modern systems.
metadata:
  tags: [su-field, vepol, 76-standards, MATChEM, interactions, system-pathology]
  source: TRIZ-Classical & Modern
---

# 09. Substance-Field (Su-Field / Веполь) Analysis & Standard Solutions

> *"Any minimal working technical system consists of two interacting substances and a field connecting them. If an interaction is harmful or insufficient, the Su-Field model dictates the exact structural standard to fix it."* — Genrich Altshuller

---

## 1. The Canonical Su-Field Model (Веполь)

Every minimal functional unit is represented as a triangular graph containing two substances ($S_1, S_2$) and at least one field ($F$):

```
       [Field F]
      /         \
     ▼           ▼
[Substance S1] <---> [Substance S2]
```

Where:
- **$S_1$ (Target / Article):** The object or data being acted upon, shaped, measured, or transformed.
- **$S_2$ (Tool / Agent):** The component, worker, or active mechanism acting upon $S_1$.
- **$F$ (Field / Carrier):** The energy transmission medium, protocol, or interaction mechanism.

### The MATChEM Field Taxonomy:
In modern TRIZ, fields span physical, informational, and computational media:
- **M - Mechanical:** Physical force, pressure, CPU cycle execution, memory pointer indirection, physical movement.
- **A - Acoustic / Oscillatory:** Sound, vibration, network heartbeat pulses, polling intervals, frequency oscillation.
- **T - Thermal:** Heat dissipation, CPU thermal throttle, ambient thermal energy, system load intensity.
- **C - Chemical:** Molecular interaction, battery oxidation, state transition, cryptographic hash mutation.
- **E - Electric / Electronic:** Voltage, current, digital circuit signaling, bit-level register flipping.
- **M - Magnetic / Informational:** Magnetic storage, electromagnetic fields, vector embeddings, data flow protocols, semantic attention masks.

---

## 2. The 4 System Pathologies in Su-Field Analysis

| Pathology | Su-Field Graph | Diagnostic Symptom | Standard Fix Strategy |
|---|---|---|---|
| **1. Incomplete Model** | $S_1$ or $F$ missing | The desired useful action does not occur at all. | Synthesize a complete Su-Field by introducing the missing substance or field from existing resources (Class 1). |
| **2. Harmful Action** | $S_2 \xrightarrow{F_{\text{harm}}} S_1$ | The tool achieves a benefit but damages $S_1$ (e.g., lock contention, thermal degradation, memory corruption). | Introduce an intermediate substance $S_3$, modify $S_1$ or $S_2$, or apply an opposing counter-field $F_2$ (Class 1.2). |
| **3. Insufficient / Weak Action** | $S_2 \xrightarrow{F_{\text{weak}}} S_1$ | The useful action occurs, but throughput or efficacy is unacceptably low. | Transition to micro-level, introduce ferromagnetic/porous structure, or introduce resonance/feedback (Class 2). |
| **4. Uncontrollable / Unmeasurable** | $S_2 \xrightarrow{?} S_1$ | Cannot detect state changes or regulate the interaction dynamically. | Introduce measurement field, self-monitoring markers, or transition to a double Su-Field (Class 4). |

---

## 3. The 5 Classes of Standard Inventive Solutions (Adapted from 76 Standards)

Altshuller cataloged 76 Standard Inventive Solutions, organized into 5 universal classes:

### Class 1: Composition and Decomposition of Su-Fields
- **Standard 1.1 (Synthesizing Missing Field):** If $S_1$ and $S_2$ do not interact effectively, introduce a free internal field (e.g., exploit existing HTTP keep-alive connection instead of creating new TCP handshakes).
- **Standard 1.2 (Eliminating Harmful Action):**
  - **1.2.1 (Intermediary $S_3$):** Insert a third substance between $S_1$ and $S_2$ (e.g., API Gateway, message queue buffer, non-blocking cache).
  - **1.2.2 (Modified $S_1$ or $S_2$):** Change the surface, state, or structure of the existing tool (e.g., using an immutable read-only view of a record).
  - **1.2.3 (Opposing Field $F_2$):** Neutralize the harmful field with an equal and opposite force (e.g., reactive stream backpressure to cancel upstream overflow).

### Class 2: Evolution and Enhancement of Su-Fields
- **Standard 2.1 (Transition to Complex Su-Fields):** Chain multiple fields in series (e.g., batching + compression + pipelining).
- **Standard 2.2 (Transition to Micro-Level):** Replace macroscopic monolithic components with microscopic entities (e.g., vector SIMD instructions, bitmasks, serverless micro-lambdas).
- **Standard 2.3 (Phase / State Transitions):** Transition components between mutable and immutable phases, or between in-memory and disk states based on access frequency.

### Class 3: Transitions to Supersystems and Micro-Levels
- **Standard 3.1 (Bi-System and Poly-System):** Combine two identical or complementary systems to achieve emergent capabilities (e.g., dual-core processing, active-active multi-region failover).
- **Standard 3.2 (Dynamization):** Make static interfaces elastic and responsive to live environment changes (e.g., adaptive PID autoscaling, dynamic thread pool sizing).

### Class 4: Standards for Measurement and Detection
- **Standard 4.1 (Indirect Measurement):** If measuring a metric directly causes observer effect latency, measure an existing proxy or secondary symptom (e.g., tracking packet round-trip time instead of measuring server queue depth directly).
- **Standard 4.2 (Measurement Fields):** Introduce lightweight telemetry markers (e.g., OpenTelemetry correlation IDs injected into existing trace headers).

### Class 5: Helper Standards (Applying Resources & Substances)
- **Standard 5.1 (Using Existing Vacuum / Emptiness):** Exploit "empty" spaces (e.g., struct padding bytes, idle CPU slots, off-peak network windows).
- **Standard 5.2 (Self-Restoring Substances):** Make components self-healing or self-cleaning without external human intervention (e.g., generational garbage collection, Kubernetes self-restarting control loops).

---

## 4. Operational Checklist for Su-Field Resolution

When analyzing a system bottleneck:
1. Identify $S_1$ (what is harmed or needs improvement?), $S_2$ (what is acting on it?), and $F$ (how is the interaction carried out?).
2. Diagnose the pathology: Incomplete? Harmful? Insufficient? Uncontrollable?
3. Select the matching Standard Class (Class 1-5).
4. Verify that the resolution mobilizes existing internal substances/fields rather than importing expensive new dependencies.

---

**Next:** [10-testing-scenarios.md](10-testing-scenarios.md) — Testing & Pressure Verification Suites.  
**Index:** [README.md](README.md)
