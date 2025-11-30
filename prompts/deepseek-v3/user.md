Word: {{WORD}}

Candidate senses:
{{SENSES}}

Output requirements:
- Output ONLY one JSON object.
- Do NOT wrap it in Markdown or code fences.
- Do NOT output any extra text.

Your tasks:

1. From all candidate senses, choose ONE primary everyday sense for this word.
   - This is the main sense that most learners should memorize first.
   - It can be any POS (n, v, adj, adv), but must be the most common and general everyday meaning.
   - This primary sense will populate the top-level fields:
     "synset", "pos", "definition", "definition_simple",
     "hypernyms", "hyponyms", "synonyms",
     "examples_dict", "examples_ai", "chinese".

2. For other POS (different from the primary POS), you may add at most ONE additional sense per POS
   into the "other_pos" array.
   - Example: if the primary sense is a verb (v), you may add one noun (n) sense, one adjective (adj) sense, etc.
   - For each such extra POS sense, you only need to provide:
     - pos
     - definition (a concise dictionary-style definition in English)
     - examples_dict (at most 1–2 examples from the candidate senses, use [] if none)
     - examples_ai (1–2 short learner-friendly examples, use [] if none)

3. Keep the original WordNet definition for the primary sense in "definition".
4. Write a simplified learner-friendly definition in "definition_simple" for the primary sense.
5. For the primary sense:
   - "examples_dict" should be a list of examples from the candidate senses (if any).
   - "examples_ai" should be 2–3 natural example sentences for learners.
   - "chinese" should be a natural Chinese translation of the primary meaning.

6. Output ONLY one JSON object with this structure:

{
  "word": "{{WORD}}",
  "synset": "",
  "pos": "",
  "definition": "",
  "definition_simple": "",
  "hypernyms": [],
  "hyponyms": [],
  "synonyms": [],
  "examples_dict": [],
  "examples_ai": [],
  "other_pos": [],
  "chinese": ""
}

- "other_pos" MUST be an array (possibly empty).
- Each item in "other_pos" MUST be:

{
  "pos": "",
  "definition": "",
  "examples_dict": [],
  "examples_ai": []
}

Do NOT change field names.
Do NOT wrap the JSON in any Markdown.
Do NOT output any explanations.
