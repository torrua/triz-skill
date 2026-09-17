---
description: >-
  Claim register for safety-critical, performance, and compliance-sensitive assertions in triz-universal.
  Each entry records its scope, confidence, and required validation.
metadata:
  tags: [claims, evidence, confidence, verification, safety]
  source: internal register
---

# Claim Register & Evidence Levels

Use this register when a resolution depends on a claim that could change feasibility, safety, cost, or compliance. Add a row before promoting a hypothesis to an established recommendation.

| Claim ID | Claim | Level | Scope / limit | Required validation |
|---|---|---|---|---|
| `C-MVCC-01` | MVCC can provide snapshot reads while writers commit versions. | Established | Database-version and isolation-level specific; does not imply replica freshness. | Cite the deployed database documentation and test the selected isolation level. |
| `C-CDC-01` | Outbox plus CDC can atomically persist a local record and publish an event for asynchronous consumers. | Pattern | Delivery and cross-service convergence are not instantaneous global consistency. | Test duplicates, replay, lag, compensation, and outage recovery. |
| `C-MMAP-01` | File-backed mappings can change access patterns for data on storage. | Pattern | Durability, memory pressure, and flush behavior depend on OS and filesystem. | Benchmark the target OS/filesystem with explicit flush policy. |
| `C-KYC-01` | Risk-based onboarding can defer some friction until a later product state. | Hypothesis | Only where law, licence, product permissions, and consent allow it. | Obtain legal/privacy approval and test the approved state machine. |
| `C-PASSKEY-01` | Passkeys can reduce password friction while using phishing-resistant cryptography. | Pattern | Recovery, accessibility, device support, and required MFA factors vary. | Verify against deployed FIDO/WebAuthn support and policy. |

## Required Resolution Fields

Every final answer for a high-impact domain must state:

1. `Evidence & Confidence`: claim IDs and Established, Pattern, or Hypothesis status.
2. `Verification Plan`: baseline, environment, test method, success threshold, and accountable owner.
3. `Residual Risks`: remaining laws, failure modes, cost, privacy, and operational dependencies.

**Related:** [SOURCES.md](SOURCES.md) and [10-testing-scenarios.md](10-testing-scenarios.md).
