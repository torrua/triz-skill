---
description: >-
  Contradiction Matrix lookup for AI agents: 39 TRIZ parameters mapped to software/AI/business equivalents,
  top-50 parameter-pair recommendations, and Matrix 2003 guidance.
metadata:
  tags: [contradiction-matrix, 39-parameters, altshuller-matrix, matrix-2003, lookup]
  source: TRIZ-Classical & Matrix 2003
---

# 11. Contradiction Matrix & Parameter Lookup

When a **Technical Contradiction** has been identified (improving Parameter A degrades Parameter B), use this matrix to find the most promising **Inventive Principles** from the 40.

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
3. **Find the intersection** — it lists 2-4 recommended Inventive Principles
4. **Read each principle** from [05-40-principles-catalog.md](05-40-principles-catalog.md)
5. **Apply** each principle to your specific physical contradiction

### Example

> *"We want faster API response (Parameter 9: Speed) but adding caching increases memory usage (Parameter 1: Weight of moving object)"*

Matrix cell [9, 1] → Principles: **2 (Taking Out)**, **28 (Mechanics Substitution)**, **13 (The Other Way Around)**, **38 (Strong Oxidants / Accelerated Processing)**

- **Principle 2 (Taking Out):** Extract only hot-path data into cache; leave cold data on disk
- **Principle 28:** Replace in-memory cache with computed/derived values (memoization of functions, not data)
- **Principle 13:** Instead of caching responses, pre-reject invalid requests earlier in the pipeline
- **Principle 38:** Use OS page cache (already exists, zero new memory allocation) instead of application-level cache

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

## Matrix 2003 vs Classical Altshuller Matrix

| Aspect | Altshuller (1971) | Matrix 2003 |
|---|---|---|
| **Data source** | ~40,000 patents (pre-1970s) | ~400,000+ patents (through 2003) |
| **Parameters** | 39 | 48 (added 9 new: information, adaptability, etc.) |
| **Coverage** | 1,263 cells filled (83%) | ~2,500 cells filled |
| **Recommendations** | 2-4 principles per cell | Up to 7 principles per cell |
| **Domain bias** | Mechanical engineering | More balanced across domains |

**When to use Matrix 2003:** When the classical matrix returns empty cells or when the problem involves information-heavy systems (software, AI).

---

**Index:** [README.md](README.md)
**Related:** [02-contradictions.md](02-contradictions.md) — How to sharpen Technical → Physical Contradictions before matrix lookup.
**Related:** [05-40-principles-catalog.md](05-40-principles-catalog.md) — Detailed descriptions of all 40 Inventive Principles.
