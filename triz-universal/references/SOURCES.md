---
description: >-
  Provenance policy and source registry for triz-universal. Distinguishes classical TRIZ material,
  software patterns, and regulated-domain guidance from illustrative examples.
metadata:
  tags: [sources, provenance, confidence, triz, software, compliance]
  source: internal registry
---

# Sources & Provenance Policy

`triz-universal` is a reasoning aid, not an authority for performance, security, legal, or compliance claims. A recommendation must carry a source, scope, and confidence level before it is presented as established fact.

## Source Classes

| Class | Examples | Permitted use |
|---|---|---|
| **Primary / normative** | Statutes, regulator guidance, product specifications, database documentation | Facts about the cited system or jurisdiction, within version scope |
| **Classical TRIZ** | Altshuller material on contradictions, IFR, 40 principles, and Su-Field analysis | Method vocabulary and ideation structure |
| **Engineering pattern** | Vendor documentation, peer-reviewed work, maintained standards | Candidate implementation pattern with stated assumptions |
| **Illustrative** | Examples written in this skill | Teaching only; never evidence of performance or compliance |

## Registered Sources

| ID | Source | Scope | Notes |
|---|---|---|---|
| `TRIZ-ALT` | G. Altshuller, published works on TRIZ and the 40 Inventive Principles | Classical terminology and methods | Do not infer software guarantees from mechanical patent examples. |
| `TRIZ-MODERN` | Modern TRIZ publications cited by the project maintainer | Extensions and facilitation methods | Add the exact edition/page before making a quantitative claim. |
| `POSTGRES-DOCS` | PostgreSQL documentation for the deployed major version | MVCC, replication, WAL | Replication topology and lag must be measured in the target deployment. |
| `FIDO-SPEC` | FIDO Alliance / WebAuthn specifications for the deployed platform | Authentication protocol capabilities | Recovery, device support, accessibility, and policy remain deployment-specific. |
| `REGULATOR-LOCAL` | Applicable regulator and counsel-approved policy | KYC/AML, privacy, consent, data retention | Mandatory for any regulated recommendation; this repository does not supply jurisdictional advice. |

## Citation Rules

1. Use **Established** only for a claim supported by a versioned primary or normative source.
2. Use **Pattern** for a known design approach whose feasibility depends on workload or context.
3. Use **Hypothesis** for an untested proposal; include an experiment and a success threshold.
4. Label examples **Illustrative** unless a reproducible benchmark and environment are recorded.
5. Never call a third-party API, vendor signal, user data source, or extra infrastructure "free" without a documented boundary, cost, permission, and reliability assessment.

**Related:** [CLAIMS.md](CLAIMS.md), [11-contradiction-matrix.md](11-contradiction-matrix.md), and [12-evaluation-suite.md](12-evaluation-suite.md).
