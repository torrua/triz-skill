# Behavioral Evaluation Protocol

The existing unit tests lint document structure and required safety language. They do not establish that an LLM's proposed solution is feasible. This directory defines a separate **blind** evaluation protocol.

## Running an Evaluation

1. Give each case prompt to the target model with and without `triz-universal`.
2. Store raw outputs without exposing the expected outcome to the model or evaluators.
3. Randomize and blind the outputs before expert review.
4. Have domain-qualified reviewers score constraint handling, factual support, feasibility, risk disclosure, and novelty independently.
5. Record disagreements, environment, model/version, prompt version, and any tool access.

## Passing Rubric

An answer passes only when it:

- preserves each hard constraint or explicitly proves the relevant limit;
- avoids every `disallowed_claim` in the case;
- identifies assumptions and gives evidence/confidence;
- supplies a measurable verification plan and residual risks;
- is judged feasible by expert review for the relevant domain.

Phrase matching is intentionally insufficient. A response that merely says “Physical Contradiction”, “VPR”, and “Separation” must fail if it makes an unsupported guarantee.

## Reporting

Report pass rate by case and model, plus the number of unsupported absolute claims, missed hard constraints, and reviewer disagreements. Do not generalize results from these four seed cases; expand the corpus with blinded holdout cases before making efficacy claims.
