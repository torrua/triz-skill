---
description: >-
  Provenance policy, canonical bibliography with exact editions/pages, and clean-room license notice
  for triz-universal. Distinguishes classical TRIZ material, formal bounds, and software patterns from illustrative examples.
metadata:
  tags: [sources, provenance, confidence, triz, bibliography, software, compliance]
  source: internal registry
---

# Sources & Provenance Policy

`triz-universal` is a methodological reasoning aid, not an authority for empirical performance, security, legal, or compliance claims. Every recommendation must carry a source class, scope, and confidence level (`Established`, `Pattern`, or `Hypothesis`) before it is presented to a user.

## Source Classes

| Class | Examples | Permitted Use |
|---|---|---|
| **Primary / Normative** | Statutes, regulator guidance, formal mathematical proofs, database/OS specifications | Facts about the cited system, theorem, or jurisdiction within version and assumption scope |
| **Classical & Modern TRIZ** | Canonical Altshuller, Zlotin/Zusman, Litvin/Gerasimov, and Khomenko publications | Methodological vocabulary, contradiction sharpening, ARIZ-85-V steps, and ideation heuristics |
| **Engineering Pattern** | Vendor documentation, peer-reviewed systems papers, maintained architecture patterns | Candidate implementation pattern with stated workload and operational assumptions |
| **Illustrative** | Pedagogical examples written in this skill | Teaching only; never treated as empirical proof of latency, throughput, or legal compliance |

## Canonical Bibliography & Registered Sources

| ID | Canonical Citation (Edition & Pages) | Scope in `triz-universal` | Constraints & Notes |
|---|---|---|---|
| `TRIZ-ALT-79` | Г. С. Альтшуллер, *Творчество как точная наука: Теория решения изобретательских задач* (М.: Советское радио, 1979, 184 с.; English trans. *Creativity as an Exact Science*, Gordon & Breach, 1984), pp. 42–94 (TC/PC, IFR, VPR), pp. 95–138 (40 Inventive Principles & 39 Parameters), pp. 139–165 (Su-Field Analysis). | 40 Inventive Principles, 39 engineering parameters, IFR/VPR definitions, Su-Field triads | Classical mechanical examples do not automatically transfer quantitative guarantees to software. |
| `TRIZ-ALT-86` | Г. С. Альтшуллер, *Найти идею: Введение в ТРИЗ — теорию решения изобретательских задач* (Новосибирск: Наука, 1-е изд. 1986, 209 с.; 2-е изд. 1991; 3-е изд. Альпина Бизнес Букс, 2007, 400 с.), pp. 125–178 (76 Standard Solutions & Laws of Evolution), Приложение 1, pp. 215–265 (Канонический текст АРИЗ-85-В, Части 1–9, Таблица 2). | Canonical ARIZ-85-V (Parts 1–9), MMC operator, Step Back from IFR, Table 2 rules, 76 Standards | Tier-3 protocols adapt ARIZ-85-V structure for AI reasoning; physical particle rules are heuristic analogies in digital systems. |
| `TRIZ-ZZ-89` | Г. С. Альтшуллер, Б. Л. Злотин, А. В. Зусман, В. И. Филатов, *Поиск новых идей: от озарения к технологии (Теория и практика решения изобретательских задач)* (Кишинев: Картя Молдовеняскэ, 1989, 381 с.), Гл. 2–4, pp. 64–182 (Диагностика ФП, классификация ВПР, свертывание, ранний диверсионный анализ). | Diagnostic questions (WHERE/WHEN/CONDITION/STRUCTURE), VPR taxonomy, Alternative System | Used for rapid strategy selection in Step 4. |
| `TRIZ-ZZ-01` | B. Zlotin, A. Zusman, *Directed Evolution: Philosophy, Theory and Practice* (Southfield, MI: Ideation International, 2001, 203 pp.), Ch. 3–5, pp. 55–140; and *Anticipatory Failure Determination (AFD)* methodology. | Subversion Analysis / AFD (`ariz-deep/06-subversion-analysis-afd.md`) | Inverted failure search is a structured risk-discovery heuristic, not a formal verification proof. |
| `TRIZ-LIT-91` | С. С. Литвин, В. М. Герасимов, *Развитие приемов разрешения физических противоречий и функционально-стоимостной анализ / Свертывание* (Ленинградская школа ТРИЗ, метод. материалы 1987–1992; *Журнал ТРИЗ*, 1991, № 2.1, с. 31–44). | Satisfy & Bypass strategies (Strategies 5–6); Functional Trimming Rules A, B, C (`ariz-deep/05-trimming-algorithm.md`) | Bypass and Trimming require verifying that removed components do not drop mandatory safety/compliance functions. |
| `TRIZ-OTSM-00` | Н. Н. Хоменко, *ОТСМ-ТРИЗ: Общая теория сильного мышления — Модель «Элемент–Имя признака–Значение признака» (ЭИЗ / ENV)* (Минск / Джонатан Ливингстон, рабочие материалы 1997–2007). | Domain-agnostic ENV contradiction formulation (`08-multi-domain-lenses.md`) | Used to translate TRIZ contradictions into non-mechanical domains. |
| `CS-CAP-02` | S. Gilbert, N. Lynch, *"Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services"*, ACM SIGACT News, Vol. 33, Issue 2, 2002, pp. 51–59. | Formal definition of the CAP theorem limit (atomic linearizable read/write register under asynchronous network partition) | Applies strictly when network partitions occur and linearizability + total availability on every node are simultaneously demanded. |
| `CS-AMDAHL-67` | G. M. Amdahl, *"Validity of the single processor approach to achieving large scale computing capabilities"*, AFIPS Spring Joint Computer Conference Proceedings, Vol. 30, 1967, pp. 483–485. | Formal speedup bound for a fixed problem size with irreducible serial fraction $s$ | Can be bypassed when problem size scales (Gustafson's law) or when the serial algorithm is replaced. |
| `POSTGRES-DOCS` | PostgreSQL Global Development Group, *PostgreSQL Documentation: Concurrency Control (MVCC, Transaction Isolation, WAL)* (current deployed major version, Ch. 13 & Ch. 30). | Snapshot isolation, MVCC lock-free reads, WAL durability | Replica lag, fsync latency, and serialization anomalies must be measured in the target deployment. |
| `FIDO-SPEC` | W3C & FIDO Alliance, *Web Authentication: An API for accessing Public Key Credentials (Level 2 / Level 3)* (W3C Recommendation). | Passkey / FIDO2 cryptographic authentication properties | Account recovery, device availability, accessibility, and regulatory MFA rules remain deployment-specific. |
| `REGULATOR-LOCAL` | Applicable jurisdictional statutes, financial/data-protection regulator guidance, and counsel-approved compliance policy. | KYC/AML, GDPR/privacy, consent, financial licensing, audit retention | Mandatory for any regulated recommendation; this repository never supplies legal advice. |

## Clean-Room & License Provenance Notice

1. **Original Clean-Room Text:** All prompts, algorithms, domain mappings, benchmark scenarios, and scripts in `torrua/triz-skill` are original clean-room formulations authored for this repository and released under the [MIT License](../../LICENSE).
2. **Conceptual Inspiration Only:** External repositories listed in the README Acknowledgments (`truinorva/triz-skills`, `jenson500/triz-prompt-engineering`, *Heinrich: The Inventing Machine*) served solely as high-level conceptual inspiration (e.g., the utility of including a contradiction lookup table, evaluation rubrics, and dual strategy sets). No text, tables, or code were copied from those projects.
3. **Public Domain / Canonical Method Names:** The 40 Inventive Principles, 39 Engineering Parameters, and ARIZ-85-V step titles are canonical scientific terminology created by G. S. Altshuller; their software/AI/business adaptations in this repository are original work.

## Citation Rules

1. Use **Established (`Факт`)** only for a claim supported by a versioned primary/normative source, mathematical proof under verified assumptions, or empirical user benchmark.
2. Use **Pattern (`Паттерн`)** for a known engineering or business design pattern whose quantitative outcome depends on workload, environment, or implementation details.
3. Use **Hypothesis (`Гипотеза`)** for an untested inventive proposal; always attach a concrete verification experiment and a measurable success threshold.
4. Label built-in skill examples **Illustrative** unless a reproducible benchmark and target environment are recorded.
5. Never call a third-party API, vendor signal, user data source, or added infrastructure "free" without documenting its boundary, cost, permission, and reliability.

**Related:** [CLAIMS.md](CLAIMS.md), [11-contradiction-matrix.md](11-contradiction-matrix.md).
