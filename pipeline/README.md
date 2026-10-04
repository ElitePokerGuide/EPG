# Pipeline

```
ingest/    transcripts -> lessons -> chunks -> concept cards
generate/  concept card + format -> script, caption, replayer spec      (Phase 0 step 3)
render/    script -> TTS -> replayer animation -> captions -> mp4/png   (Phase 0 step 5)
publish/   queue -> Postiz (IG, TikTok, YT, Threads, Telegram)          (Phase 0 step 4)
measure/   Postiz analytics -> metrics -> hook/topic weights            (Phase 1)
review/    Telegram approve/reject bot                                   (Phase 0 step 6)
```

## Ingest

```bash
pip install -r pipeline/requirements.txt

# 1. Put raw course files into knowledge/raw/ (names must match knowledge/sources.yaml `file`).
#    From Claude Code: the `ingest-course` skill downloads them from Drive by id.
#    From a laptop: rclone copy "gdrive:Courses Content Combined" knowledge/raw/

# 2. Split combined course files into lessons
python3 pipeline/ingest/split_lessons.py            # all sources with status != skipped
python3 pipeline/ingest/split_lessons.py rio-game-plan cc-grade-0

# 3. Chunk lessons (~1500 words, sentence-aligned, 150-word overlap)
python3 pipeline/ingest/chunk.py

# 4. Extract concept cards (needs ANTHROPIC_API_KEY). Writes knowledge/concepts/<format>/<source>-<lesson>.yaml
python3 pipeline/ingest/extract_concepts.py --source rio-game-plan --limit 5

# 5. Validate everything under knowledge/concepts against the schema + taxonomy
python3 pipeline/ingest/validate_cards.py
```

Without an API key (e.g. inside a Claude Code session) step 4 is done by the `extract-concepts` skill: Claude reads chunks and writes cards following the same prompt in `ingest/prompts/extract_concepts.md`.
