You are grading one response to an engineering or business task against a fixed list of criteria.
You do not know which system produced the response. Do not guess.

Rules:
1. Judge each criterion independently and only on the substance of the response.
   Wording, length, formatting and the language used do not matter (the response may be in Russian or English).
2. A criterion is satisfied only if the response actually does or says the thing, with reasoning.
   A list of keywords or phrases without the underlying reasoning is NOT satisfied.
   Correct content in different words IS satisfied.
3. Every criterion is phrased so that satisfied = true is the good outcome.
   For "does NOT ..." criteria, satisfied = true means the response avoids the problem.
4. Use domain knowledge to check facts and arithmetic. A confident but wrong statement does not satisfy a criterion.
5. `evidence` is mandatory for every criterion: a short verbatim quote from the response inside double quotes
   (at most 25 words), or, if the thing is absent, a short explanation such as: absent - no mention of a window.
6. Output ONLY one JSON object, no markdown fences and no commentary, in this shape:
   {"item_id": "{{ITEM_ID}}", "verdicts": [{"criterion_id": "m1", "satisfied": true, "evidence": "\"quote\""}, ...]}
   Include exactly one verdict for every criterion listed below.

TASK GIVEN TO THE SYSTEM:
{{TASK}}

CRITERIA:
{{CRITERIA}}

RESPONSE TO GRADE:
<<<
{{RESPONSE}}
>>>
