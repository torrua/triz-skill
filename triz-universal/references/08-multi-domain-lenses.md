---
description: >-
  Multi-domain translation lenses for applying TRIZ across Software, AI Systems, Business Strategy, and Physical Engineering.
metadata:
  tags: [multi-domain, software, ai-agents, business-strategy, physical-engineering, otsm-triz]
  source: TRIZ-Modern & OTSM
---

# 08. Multi-Domain TRIZ Lenses (Making TRIZ Truly Universal)

> *"The laws of evolution and the mechanisms for resolving contradictions are invariant across all purposeful artificial systems — whether composed of atoms, bits, human incentives, or neural network tokens."* — OTSM-TRIZ (Nikolai Khomenko)

To ensure that `triz-universal` functions as a genuinely universal skill, this reference provides translation lenses mapping TRIZ concepts across four core domains:
1. **Software & Distributed Systems Engineering**
2. **AI Agents & Cognitive Architecture**
3. **Product Management & Business Strategy**
4. **Physical, Mechanical & Hardware Systems**

---

## 1. Domain Lens Matrix: The 4 Invariant Pillars

| TRIZ Core Concept | Software & Systems | AI Agents & LLMs | Business & Product | Physical & Mechanical |
|---|---|---|---|---|
| **Element $X$** | Data buffer, mutex lock, API endpoint, database row. | Context window, prompt tokens, system instructions, tool calls. | Pricing tier, onboarding flow, feature gate, organizational unit. | Turbine blade, cooling pipe, chassis, structural joint. |
| **Property $P$** | Synchronous, in-memory, locked, persistent, typed. | Deterministic, verbose, constrained, reasoning-heavy, active. | Friction-heavy, exclusive, centralized, high-margin, bespoke. | Rigid, heavy, opaque, heated, conductive. |
| **Opposing $\neg P$** | Asynchronous, zero-copy, lock-free, ephemeral, dynamic. | Probabilistic, concise, unconstrained, fast-pass, passive. | Frictionless, self-serve, decentralized, freemium, automated. | Flexible, lightweight, transparent, cooled, insulating. |
| **Harmful Factor $H$** | Latency, OOM crash, deadlock, race condition, tech debt. | Hallucination, token exhaustion, cognitive drift, prompt injection. | Customer churn, fraud, regulatory fine, high CAC, burnout. | Thermal wear, friction, fracture, material fatigue, corrosion. |
| **Useful Function $F$** | Data integrity, throughput, consistency, sub-ms retrieval. | Accurate reasoning, tool execution, grounded synthesis. | Revenue growth, retention, conversion, compliance security. | Load bearing, energy transfer, containment, speed. |
| **Free Resource (ВПР)** | Idle CPU cycles, struct padding, natural data ordering, OS kernel. | Attention mask, user input keywords, structured JSON schemas, cache. | User referral intent, dormant customer data, partner distribution. | Ambient air, gravity, waste heat, thermal gradients, friction. |

---

## 2. Lens 1: AI Agents & Cognitive Systems

LLM agents operate under unique constraints governed by token budgets, context degradation, attention decay, and RLHF compromise bias.

### Common Contradictions in AI Architecture:
1. **The Context Depth vs Attention Saturation Dilemma:**
   - *Technical Contradiction:* If we inject 100 pages of domain documentation into context, the agent possesses complete domain knowledge, but prompt token cost surges, latency spikes, and middle-context attention drifts ("lost in the middle").
   - *Physical Contradiction:* The documentation must be **present in the prompt** (to ground generation) and must **NOT be present in the prompt** (to preserve low latency, cheap token spend, and sharp focus).
   - *Separation in Space & Condition:* Progressive Disclosure via Tier-2 skills. Root `SKILL.md` (<150 lines) acts as a high-precision router; deep reference modules are loaded into context *only when a specific symptom is triggered*.
2. **Deterministic Constraint vs Emergent Creativity:**
   - *Physical Contradiction:* The agent's output must be **strictly rigidly constrained** (to prevent hallucination and schema violation) and must be **unconstrained** (to synthesize novel inventive solutions).
   - *Separation by Structure:* Subsystem (Grammar / Constrained Decoding / JSON schema validation) guarantees rigid structural invariants; internal reasoning tokens (thought scratchpad) retain unconstrained semantic entropy.

---

## 3. Lens 2: Business, Strategy & Product Management

Business dilemmas are frequently mishandled through cowardly compromises (e.g., "let's sacrifice user experience slightly to enforce fraud compliance"). TRIZ eliminates these trade-offs.

### Common Contradictions in Business Strategy:
1. **Security / Compliance vs Conversion Friction:**
   - *TC:* If we enforce 5-step KYC/MFA verification, fraud drops to 0%, but onboarding conversion drops by 45%.
   - *Sharpened PC:* The verification process must be **exhaustive and intrusive** (to eliminate fraud risk) and must be **completely absent** (to deliver 1-click instantaneous conversion).
   - *Separation in Time & Condition (Progressive Frictionless Compliance):* User experiences zero friction ($0$ steps) during initial onboarding (Separation in Time). Behavioral biometrics, IP reputation, and device fingerprinting run silently in the background (Free Resource). Strict MFA is triggered dynamically *only when a high-risk financial transaction threshold is crossed* (Separation by Condition).
2. **Custom Enterprise Flexibility vs Scalable SaaS Simplicity:**
   - *Sharpened PC:* The product must be **custom-built for Enterprise Client A** and must be **a single standardized multitenant codebase**.
   - *Separation by Structure (Plugin / Extension Marketplace):* Core system remains 100% immutable and uniform (Principle 33); client-specific customizations run as sandboxed Wasm / headless webhook extensions at the periphery (Principle 1 & 7).

---

## 4. Lens 3: Physical, Mechanical & Material Engineering

In classical physical engineering, Altshuller's original parameters and physical laws apply directly.

### Common Contradictions in Physical Systems:
1. **Thermal Dissipation vs Aerodynamic Drag:**
   - *PC:* The cooling surface must be **infinitely large** (to dissipate 50kW of heat) and must be **infinitely small / zero** (to maintain laminar aerodynamic flow).
   - *Separation in Space & Structure:* Heat-pipe micro-channels embedded flush within the structural skin of the vehicle (Principles 31 & 40). The vehicle skin itself becomes the heat radiator with zero added aerodynamic frontal area.
2. **Mechanical Strength vs Structural Weight:**
   - *PC:* The structural beam must be **solid and thick** (to prevent buckling under load) and must be **hollow / weightless** (to meet payload limits).
   - *Separation by Structure:* Internal 3D isotropic lattice / honeycomb foam (Principle 31 - Porous Materials; Principle 8 - Counterweight; Principle 40 - Composite Materials).

---

## 5. OTSM-TRIZ: The ENV (Element - Name of Feature - Value of Feature) Model

When working across non-standard domains, classical terminology can cause semantic friction. Nikolai Khomenko's **ENV Model** provides a domain-agnostic dialectical formulation:

$$\text{System} = \{ \text{Elements } (E_i) \}$$
$$\text{Each Element possesses Features } (N_j) \text{ with Values } (V_k)$$

### The Universal Contradiction Formula in OTSM:
- **Requirement 1:** $V(N_1) = \text{Value } A \implies \text{Produces Benefit } B_1 \text{ but causes Harm } H_2$.
- **Requirement 2:** $V(N_1) = \text{Opposite Value } \neg A \implies \text{Eliminates Harm } H_2 \text{ but loses Benefit } B_1$.
- **Resolution:** Change the relationship between $N_1$ and $V(N_1)$ through Space, Time, Condition, or Structure so that Benefit $B_1$ is achieved while Harm $H_2$ is impossible.

---

**Next:** [09-su-field-and-standards.md](09-su-field-and-standards.md) — Su-Field Analysis & 76 Standards.  
**Index:** [README.md](README.md)
