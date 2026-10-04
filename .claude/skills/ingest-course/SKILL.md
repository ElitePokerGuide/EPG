---
name: ingest-course
description: Fetch course transcripts from the Google Drive folder "Courses Content Combined" into knowledge/raw/ and run the ingest pipeline (split lessons, chunk). Use when new transcripts were added to Drive, when knowledge/sources.yaml has sources with status pending, or when asked to ingest a course.
---

# Ingest a course from Google Drive

## Steps
1. Open `knowledge/sources.yaml`. Pick the sources to ingest (by `id`, or all with `status: pending` in the requested batch).
2. For each source, download by `drive_id` with the Google Drive MCP tool `download_file_content`. The result is saved to a tool-results file as JSON `{content: <base64>, title}`. Decode:
   `jq -r '.content' <result-file> | base64 -d > "knowledge/raw/<file from sources.yaml>"`
   Files above ~15 MB may not fit through the connector. For those, ask the owner to split the file on Drive, or fetch with rclone from a machine with Drive access: `rclone copy "gdrive:Courses Content Combined/<file>" knowledge/raw/`.
3. If a new file appears in the Drive folder that is not in `sources.yaml`, add an entry (id, drive_id, file, school, course, formats, size_bytes, batch, status: fetched). Never leave a Drive file unlisted.
4. Run `python3 pipeline/ingest/split_lessons.py <ids>` then `python3 pipeline/ingest/chunk.py <ids>`. Check the lesson list for duplicates and junk (intro/welcome/promo lessons are fine to leave; extraction skips them).
5. Update `status` in `sources.yaml` to `normalized`.
6. Then run the `extract-concepts` skill (or `pipeline/ingest/extract_concepts.py` with an API key) for the new lessons.

## Never
- Commit anything under `knowledge/raw`, `knowledge/normalized`, `knowledge/chunks` (gitignored, but check `git status` before committing).
