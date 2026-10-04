# Knowledge layer

The only part of this system that cannot be copied. Everything else is tooling.

```
knowledge/
  sources.yaml        manifest of every course transcript we own (Drive file id, school, course, tags, status)
  taxonomy.yaml       controlled vocabulary: formats, topics, concepts, levels
  schema/             JSON schema for concept cards
  raw/                (gitignored) course transcripts exactly as delivered, one file per course
  normalized/         (gitignored) one JSONL per course: lesson_id, title, text
  chunks/             (gitignored) one JSONL per course: ~1 500-word chunks with lesson refs
  concepts/           COMMITTED. Atomic concept cards (YAML), grouped by format. This is the product.
  index/              (gitignored) embeddings
```

## Pipeline

```
raw/*.txt  --split_lessons-->  normalized/*.jsonl  --chunk-->  chunks/*.jsonl  --extract_concepts-->  concepts/<format>/*.yaml
```

See `pipeline/README.md` for commands.

## Rules that protect us

1. Nothing under `raw/`, `normalized/` or `chunks/` is ever committed, published or quoted.
2. A concept card contains OUR explanation of an idea, never the source text. Max quote length: 8 words.
3. `source_refs` are internal bookkeeping. They never appear in generated content.
4. Cards with `consensus_score < 0.6` or `status != approved` are not eligible for auto-publishing.
