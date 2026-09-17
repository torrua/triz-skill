---
description: >-
  Sub-topic index and navigation guide for triz-universal reference modules.
metadata:
  tags: [triz, references, index, navigation]
  source: internal
---

# TRIZ Reference Index & Navigation

This directory contains modular reference components for the `triz-universal` skill. Load only the specific reference needed for your current problem phase to optimize context token efficiency.

## Component Index

| Reference Module | Purpose & Core Content | When to Consult |
|---|---|---|
| **[01-ikr-ideality.md](01-ikr-ideality.md)** | Ideality calculus, 3 canonical IFR templates, anti-bloat checklist. | Step 1: Defining the target state and zero-cost boundary. |
| **[02-contradictions.md](02-contradictions.md)** | Pipeline from Administrative $\to$ Technical $\to$ Physical Contradictions. Limit sharpening rules. | Step 2: Sharpening vague trade-offs into atomic physical conflicts. |
| **[03-separation-principles.md](03-separation-principles.md)** | Deep heuristics for the 4 Separation Operators: Space, Time, Condition, Structure. | Step 4: Finding the structural transformation that satisfies $P$ and $\neg P$. |
| **[04-ariz-lite-algorithm.md](04-ariz-lite-algorithm.md)** | Full 5-step operational walkthrough of ARIZ-AI with detailed case studies. | When executing an end-to-end inventive resolution. |
| **[05-40-principles-catalog.md](05-40-principles-catalog.md)** | Complete high-density catalog of all 40 Inventive Principles mapped across software, business, and physical domains. | When separation principles need specific inventive mechanism ideas. |
| **[06-system-operator-9screens.md](06-system-operator-9screens.md)** | Altshuller's 9-screen matrix (Subsystem/System/Supersystem across Past/Present/Future) + Anti-System audit. | Step 5: Verification, tech debt prevention, supersystem impact. |
| **[07-resource-audit-vpr.md](07-resource-audit-vpr.md)** | Substance-Field Resources (ВПР): Temporal, Spatial, Informational, Differential, and Harm-as-Resource. | Step 3: Finding free internal resources instead of adding external tools. |
| **[08-multi-domain-lenses.md](08-multi-domain-lenses.md)** | Multi-domain translation adapters: Software & Algorithms, AI Agents & LLMs, Business & Product Strategy, Physical & Hardware Engineering. | When applying TRIZ outside classical software (making the skill truly universal). |
| **[09-su-field-and-standards.md](09-su-field-and-standards.md)** | Substance-Field (Su-Field / Веполь) Analysis and the 5 Classes of Standard Inventive Solutions (Altshuller's 76 Standards adapted). | When dealing with harmful, deficient, or uncontrollable interactions between components. |
| **[10-testing-scenarios.md](10-testing-scenarios.md)** | Benchmark pressure verification suites (RED baseline failures vs GREEN compliant resolutions). | When verifying agent compliance under time, authority, and sunk-cost pressure. |
| **[11-contradiction-matrix.md](11-contradiction-matrix.md)** | Curated 39-parameter software/AI/business mapping and top-30 candidate pairs. | When generating principle hypotheses after a Physical Contradiction is formed. |
| **[12-evaluation-suite.md](12-evaluation-suite.md)** | 5 reference problems with expected TRIZ solutions and pass/fail scoring criteria. | When self-evaluating TRIZ compliance or benchmarking agent quality. |
| **[13-perception-mapping.md](13-perception-mapping.md)** | Perception Mapping for organizational/people contradictions: Leads-To networks, conflict pairs, TRIZ extraction. | When resolving team conflicts, strategic deadlocks, or organizational change resistance. |
| **[SOURCES.md](SOURCES.md)** | Provenance policy and registered source classes. | Before presenting a sensitive claim as established fact. |
| **[CLAIMS.md](CLAIMS.md)** | Claim register, confidence levels, and validation requirements. | When a recommendation affects performance, security, privacy, finance, or compliance. |

## Tier-3: Deep Algorithmic Protocols (`references/ariz-deep/`)

These protocols contain exhaustive, deterministic step-by-step procedures for complex problems (Levels 4–5), deadlock escape, microscopic modeling, and adversarial stress-testing.

| Protocol Module | Purpose & Core Algorithm | When to Consult |
|---|---|---|
| **[ariz-deep/01a-ariz-85v-analysis.md](ariz-deep/01a-ariz-85v-analysis.md)** | ARIZ-85-V Parts 1–4: Mini-problem de-specialization ("child's language"), Article-Tool isolation, $T_1/T_2$ demarcation, Macro/Micro-PC, IKR-2, 6 Article rules. | When facing an intractable trade-off or when ARIZ-Lite yields insufficient depth. |
| **[ariz-deep/01b-ariz-85v-resolution.md](ariz-deep/01b-ariz-85v-resolution.md)** | ARIZ-85-V Parts 5–9: Information fund synthesis, Part 6 Deadlock Breakthrough protocol, multi-cycle check ($N \to \infty$), 4 secondary problem classes, Part 9 reflection. | When stuck in an inventive deadlock or verifying solution sustainability. |
| **[ariz-deep/02-mmc-operator-protocol.md](ariz-deep/02-mmc-operator-protocol.md)** | Modeling with Little People (ММЧ) structured role-prompting: Groups A/B/C, 4 troop reorganizations, reverse translation to code/architecture. | When resolving race conditions, lock contention, multi-agent conflicts, or microscopic deadlocks. |
| **[ariz-deep/03-step-back-from-ifr.md](ariz-deep/03-step-back-from-ifr.md)** | Step Back from IFR: Synthesis of assembly, deployment, zero-downtime migration, and serverless cold start via single minimal defect self-elimination. | When the ideal operating state is clear, but deployment, delivery, or cold boot appears impossible. |
| **[ariz-deep/04-physical-contradiction-tree.md](ariz-deep/04-physical-contradiction-tree.md)** | ARIZ Table 2 Decision Tree: Exact branching by space/time overlap ($Z_1/Z_2, T_1/T_2$), Particle Rules 8–10, bistability, vacuum/void mobilization. | When selecting physical/systemic mechanisms for an atomic Micro-PC. |
| **[ariz-deep/05-trimming-algorithm.md](ariz-deep/05-trimming-algorithm.md)** | Functional Trimming Protocol: Functional modeling, component candidate selection, Rules A, B, and C, secondary contradiction pruning. | When reducing architectural complexity, pruning microservices/queues, or maximizing ideality. |
| **[ariz-deep/06-subversion-analysis-afd.md](ariz-deep/06-subversion-analysis-afd.md)** | Anticipatory Failure Determination (AFD): Inverted saboteur role-play, internal amplifier audit, worst-case synthesis, zero-cost preventive barriers. | When stress-testing system reliability, finding Byzantine failures, or hardening AI agent pipelines. |
