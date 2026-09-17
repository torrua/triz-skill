---
description: >-
  Curated heuristic lookup for AI agents: 39 TRIZ parameters mapped to software/AI/business equivalents
  and 30 software-oriented principle prompts. It is not a complete reproduction of any contradiction matrix.
metadata:
  tags: [contradiction-matrix, 39-parameters, altshuller-matrix, matrix-2003, lookup]
  source: Curated adaptation; see SOURCES.md and CLAIMS.md
---

# 11. Curated Contradiction Lookup & Parameter Mapping

When a **Technical Contradiction** has been identified (improving Parameter A degrades Parameter B), use this curated heuristic lookup to generate candidate **Inventive Principles**. It does not prove feasibility, provide a complete 39×39 or Matrix 2003 dataset, or replace the Physical Contradiction and VPR steps.

---

## The 39 TRIZ Parameters (Multi-Domain Mapping)

| # | Classical Parameter | Software / AI Equivalent | Business Equivalent |
|---|---|---|---|
| 1 | Weight of moving object | Memory footprint of active process | Variable cost per transaction |
| 2 | Weight of stationary object | Storage footprint at rest | Fixed cost / infrastructure overhead |
| 3 | Length of moving object | Request payload size | Customer journey length |
| 4 | Length of stationary object | Codebase size / schema width | Organizational hierarchy depth |
| 5 | Area of moving object | Network bandwidth consumed | Market reach per campaign |
| 6 | Area of stationary object | Disk / storage area allocated | Office / infrastructure footprint |
| 7 | Volume of moving object | Data volume in transit | Batch size per operation |
| 8 | Volume of stationary object | Data volume at rest | Inventory / backlog size |
| 9 | Speed | Throughput / requests per second | Time-to-market / cycle time |
| 10 | Force (intensity) | CPU/GPU compute intensity | Marketing spend / sales pressure |
| 11 | Stress or pressure | System load / queue depth | Deadline pressure / workload |
| 12 | Shape | Data schema / API contract shape | Org structure / team topology |
| 13 | Stability of object's composition | Code stability / backward compat | Team retention / culture stability |
| 14 | Strength | Fault tolerance / resilience | Brand strength / competitive moat |
| 15 | Duration of action (moving) | Request latency / response time | Service delivery time |
| 16 | Duration of action (stationary) | Uptime / availability | Contract duration / retention |
| 17 | Temperature | System thermal load / CPU temp | Market "heat" / competitive intensity |
| 18 | Illumination intensity | Observability / logging verbosity | Transparency / reporting detail |
| 19 | Use of energy by moving object | CPU cycles per request | Cost per acquisition (CPA) |
| 20 | Use of energy by stationary object | Idle resource consumption | Overhead cost / maintenance spend |
| 21 | Power | Processing power / FLOPS | Revenue generation capacity |
| 22 | Loss of energy | Wasted compute / dropped packets | Customer churn / revenue leakage |
| 23 | Loss of substance | Data loss / information decay | Talent attrition / knowledge loss |
| 24 | Loss of information | Signal degradation / precision loss | Communication loss / misalignment |
| 25 | Loss of time | Latency / wait time / blocking | Lead time waste / bureaucratic delay |
| 26 | Quantity of substance | Number of components / services | Headcount / inventory quantity |
| 27 | Reliability | MTBF / error rate / data integrity | Service reliability / promise keeping |
| 28 | Measurement accuracy | Monitoring precision / metric granularity | KPI accuracy / forecast precision |
| 29 | Manufacturing precision | Build reproducibility / CI determinism | Process consistency / quality control |
| 30 | Object-affected harmful factors | Attack surface / vulnerability exposure | Regulatory risk / compliance burden |
| 31 | Object-generated harmful factors | Side effects / pollution / noise | Negative externalities / tech debt |
| 32 | Ease of manufacture | Development velocity / time to code | Ease of onboarding / hiring speed |
| 33 | Ease of operation | UX simplicity / API ergonomics | Ease of use / customer effort score |
| 34 | Ease of repair | Debuggability / MTTR | Issue resolution speed / support cost |
| 35 | Adaptability / versatility | Extensibility / plugin architecture | Pivot capability / market flexibility |
| 36 | Device complexity | Architectural complexity / LoC | Org complexity / process complexity |
| 37 | Difficulty of detecting/measuring | Debugging difficulty / root cause analysis | Problem detection / early warning |
| 38 | Extent of automation | CI/CD maturity / auto-scaling | Process automation / self-service |
| 39 | Productivity | Output per unit of compute/time | Revenue per employee / ROI |

---

## How to Use the Matrix

### Step-by-Step Lookup

1. **Identify the improving parameter** — what you want to make better (row)
2. **Identify the worsening parameter** — what degrades as a result (column)
3. **Find the matching curated pair** — it lists 2-4 candidate Inventive Principles
4. **Read each principle** from [05-40-principles-catalog.md](05-40-principles-catalog.md)
5. **Apply** each principle to your specific physical contradiction

### Example

> *"We want faster API response (Parameter 9: Speed) but adding caching increases memory usage (Parameter 1: Weight of moving object)"*

Matrix cell [9, 1] → Principles: **2 (Taking Out)**, **28 (Mechanics Substitution)**, **13 (The Other Way Around)**, **38 (Strong Oxidants / Accelerated Processing)**

- **Principle 2 (Taking Out):** Extract only hot-path data into cache; leave cold data on disk
- **Principle 28:** Replace in-memory cache with computed/derived values (memoization of functions, not data)
- **Principle 13:** Instead of caching responses, pre-reject invalid requests earlier in the pipeline
- **Principle 38:** Evaluate OS page cache before an application-level cache; it still consumes memory and requires workload measurement.

---

## Top-30 Software Contradiction Pairs

| Improving ↓ | Worsening → | Recommended Principles |
|---|---|---|
| 9 Speed | 1 Memory | 2, 28, 13, 38 |
| 9 Speed | 27 Reliability | 10, 35, 28, 21 |
| 9 Speed | 36 Complexity | 1, 28, 15, 35 |
| 9 Speed | 25 Time Loss | 10, 28, 38, 34 |
| 27 Reliability | 9 Speed | 21, 35, 11, 28 |
| 27 Reliability | 36 Complexity | 13, 35, 1, 25 |
| 27 Reliability | 32 Dev Velocity | 11, 13, 1, 35 |
| 39 Productivity | 36 Complexity | 1, 28, 15, 35 |
| 39 Productivity | 27 Reliability | 10, 35, 28, 37 |
| 33 Ease of Use | 35 Adaptability | 15, 34, 1, 16 |
| 33 Ease of Use | 36 Complexity | 2, 5, 13, 16 |
| 14 Resilience | 19 Cost/Request | 3, 35, 10, 40 |
| 14 Resilience | 36 Complexity | 13, 35, 1, 25 |
| 32 Dev Velocity | 27 Reliability | 1, 35, 11, 10 |
| 32 Dev Velocity | 29 CI Precision | 28, 35, 10, 23 |
| 35 Adaptability | 13 Stability | 15, 35, 1, 28 |
| 35 Adaptability | 36 Complexity | 15, 1, 28, 35 |
| 38 Automation | 36 Complexity | 28, 15, 10, 37 |
| 38 Automation | 33 Ease of Use | 25, 2, 13, 35 |
| 30 Security | 33 Ease of Use | 22, 35, 13, 24 |
| 30 Security | 9 Speed | 24, 28, 35, 30 |
| 34 Debuggability | 36 Complexity | 1, 13, 25, 28 |
| 34 Debuggability | 9 Speed | 10, 28, 35, 37 |
| 24 Info Integrity | 9 Speed | 10, 28, 35, 24 |
| 26 Num Components | 36 Complexity | 2, 6, 13, 1 |
| 16 Uptime | 19 Cost/Request | 35, 10, 28, 3 |
| 22 Waste | 9 Speed | 35, 28, 2, 10 |
| 31 Tech Debt | 32 Dev Velocity | 10, 35, 13, 2 |
| 28 Metric Accuracy | 25 Time Loss | 28, 6, 35, 10 |
| 12 API Shape | 13 Stability | 15, 35, 28, 1 |

---

## Relationship to Classical and 2003 Matrices

| Aspect | Classical Altshuller matrix | Matrix 2003 family |
|---|---|---|
| **Use in this skill** | Vocabulary source for the 39 parameter labels | Context only; no complete Matrix 2003 data is bundled |
| **Dataset included here** | No full matrix; only 30 curated software pairs | No Matrix 2003 cells or statistics |
| **Recommendation strength** | Candidate ideation prompts, not prescriptions | Consult a licensed, versioned primary source before claiming an exact lookup |
| **Domain bias** | Mechanical patent history | Varies by the specific published edition |

**Use note:** The mappings above are software/business analogies. Treat them as hypotheses to test, and record the source and confidence of any claim in the final resolution.

---

**Index:** [README.md](README.md)
**Related:** [02-contradictions.md](02-contradictions.md) — How to sharpen Technical → Physical Contradictions before matrix lookup.
**Related:** [05-40-principles-catalog.md](05-40-principles-catalog.md) — Detailed descriptions of all 40 Inventive Principles.
**Provenance:** [SOURCES.md](SOURCES.md) and [CLAIMS.md](CLAIMS.md).
