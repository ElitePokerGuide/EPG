# Phase 0 checklist (weeks 1-2)

Owner = you. Engine = Claude Code sessions in this repo.

## Knowledge
- [x] Drive inbox folder `Courses Content Combined` (48 files, 4 schools)
- [x] Source manifest, taxonomy, card schema, ingest pipeline
- [x] Batch 1 (Cash 6-max, 4 courses) split into lessons and chunks
- [ ] First ~100 concept cards extracted -> `docs/review/cards-cash-6max.md`  **(owner: review, mark ✅/✏️/❌)**
- [ ] Cross-school consensus pass on batch 1 (`consensus_candidates.py` -> merged cards with `consensus_score`)
- [ ] Batch 2 (remaining Cash 6-max courses, 23 files) ingested and extracted
- [ ] RIO archives > 15 MB: split on Drive into yearly files, or fetch with rclone **(owner)**

## Brand & voice
- [x] `content/voice.md`, `content/rules.md`, `content/hooks.yaml`
- [ ] Brand kit for the renderer: palette from the EPG logo, 2 fonts, table/replayer style frame **(engine, after cards review)**
- [ ] ElevenLabs voice chosen (1 EN voice, consistent across all shorts) **(owner picks from 3 samples)**

## Accounts (owner)
- [ ] Instagram Business account for the engine + linked Facebook Page (required for the API)
- [ ] TikTok Business account
- [ ] YouTube channel (Shorts + long-form later)
- [ ] Threads (comes with the IG account)
- [ ] Telegram channel + bot token for the review flow
- [ ] 3-5 manual warm-up posts on each account, bios filled, 18+ note
- [ ] Postiz: VPS (Hetzner CX22 or similar), docker-compose, Meta/TikTok/Google OAuth apps, accounts connected
- [ ] `POSTIZ_API_KEY`, `ELEVENLABS_API_KEY`, `ANTHROPIC_API_KEY`, `TELEGRAM_BOT_TOKEN` stored as secrets in the Claude Code environment

## Engine milestones
- [ ] 10 test scripts in 5 formats from approved cards (text only) -> owner taste check
- [ ] Hand replayer renders one spot to mp4 (ffmpeg/Remotion), captions, TTS -> owner visual check
- [ ] 30 posts rendered into `content/queue/`, reviewed in Telegram, >= 80% approved without edits
- [ ] First scheduled post via Postiz on each platform
- [ ] Routines: `plan-week` (Sun), `produce` (daily), `measure` (daily), `report` (Mon)

Exit criteria for Phase 0: pipeline runs end-to-end, cost per post <= 2 EUR, zero rule violations in 30 posts.
