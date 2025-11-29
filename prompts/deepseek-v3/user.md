Word: {{WORD}}

Candidate senses:
{{SENSES}}

Output requirements:
- Output ONLY one JSON object.
- Do NOT wrap it in ```json ... ``` or any Markdown fences.
- Do NOT output any extra text.

Your tasks:
1. Choose the most common and general everyday sense.
2. Keep the original WordNet definition unchanged.
3. Write a simplified definition in learner-friendly English.
4. Generate 2–3 natural example sentences.
5. Provide a natural Chinese translation of the meaning.
6. Output ONLY this JSON structure:

{
  "word": "",
  "synset": "",
  "pos": "",
  "definition": "",
  "definition_simple": "",
  "hypernyms": [],
  "hyponyms": [],
  "synonyms": [],
  "examples_wordnet": [],
  "examples_ai": [],
  "chinese": ""
}
