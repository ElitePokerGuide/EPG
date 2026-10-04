---
name: extract-concepts
description: Extract atomic concept cards from course transcript chunks into knowledge/concepts/. Use when asked to extract, mine or build concept cards from a lesson, course or chunk file, or when ANTHROPIC_API_KEY is unavailable and pipeline/ingest/extract_concepts.py cannot run.
---

# Extract concept cards (agent mode)

You are doing by hand what `pipeline/ingest/extract_concepts.py` does with the API. Same prompt, same output.

## Read first (in this order)
1. `pipeline/ingest/prompts/extract_concepts.md`  (the extraction rules; they are binding)
2. `knowledge/schema/concept-card.schema.json`     (field list and limits)
3. `knowledge/taxonomy.yaml`                       (allowed values for format/topic/level/street/pot_type)
4. `content/voice.md` and `content/rules.md`       (forbidden words, no school/coach names)

## Procedure
1. Load the chunks of the assigned lesson(s):
   `python3 -c "import json;[print(json.dumps(r)) for r in map(json.loads, open('knowledge/chunks/<source>.jsonl')) if r['lesson_id']=='<lesson_id>']"`
   Read every chunk of the lesson fully before writing cards (ideas often span chunks).
2. Write cards for the lesson as ONE YAML list to
   `knowledge/concepts/<format>/<lesson_id with "/" replaced by "__">.yaml`
   - `id`: `c-<format>-<lessoncode>-<slug>-<nnn>` where `<lessoncode>` is a 2-5 char code unique to the lesson (e.g. `gp23`, `cc07`, `br3`, `tcc16`) so ids never collide across files. `nnn` starts at 001.
   - Every card has at least one `source_refs` entry with `school`, `course`, `lesson` (= lesson_id), `chunk` (= chunk_id), `stance: supports`.
   - `consensus_score: 0.5`, `status: draft`, `created: <today ISO date>`.
   - 2-3 `hook_ideas` per card.
   - Aim for 8-15 cards per 5 000 words of real strategy content. Skip fluff.
3. Validate: `python3 pipeline/ingest/validate_cards.py`. Fix every error in YOUR files (schema, unknown topic, forbidden names, verbatim 8-grams). Re-run until your files are clean.
4. Report: number of cards, topics covered, anything the coach said that contradicts common advice (useful for the schools-disagree format).

## Never
- Copy sentences or distinctive phrasing. Rephrase. The validator rejects 8-word overlaps.
- Name the school, coach, course, site, or any player in published fields.
- Invent numbers the coach did not give. If the coach gives a frequency or size, keep it in `numbers`.
- Commit anything under `knowledge/raw|normalized|chunks`.
