# Decision log

| # | Date | Decision | Why |
|---|---|---|---|
| 1 | 2026-10-04 | First language: **EN** | Biggest market, best RPM. RU second in Phase 2. |
| 2 | 2026-10-04 | First niche for concept cards: **Cash 6-max** | Most courses, most searched, cleanest theory. |
| 3 | 2026-10-04 | Presentation: **faceless + own hand replayer** | Fully automatable, scales across languages. Avatar tested in Phase 2. |
| 4 | 2026-10-04 | Transcript storage: **Google Drive folder "Courses Content Combined"** as inbox, pipeline fetches by file id from `knowledge/sources.yaml`. Raw text never committed. | Owner already uses Drive; keeps copyrighted material out of git. |
| 5 | 2026-10-04 | Room affiliates: **not now**. Revisit after launch. | Platform policy risk during account warm-up. |
| 6 | 2026-10-04 | Owner keeps posting manually to existing groups. **A dedicated EPG channel set is created for the automated engine.** | Clean A/B between manual and automated; no risk to existing communities. |
| 7 | 2026-10-04 | No external legal review of the concept-card approach. **Risk accepted by owner.** Mitigation: hard rules in `content/rules.md`, n-gram check, no school names. | Owner decision. |
| 8 | 2026-10-04 | Human-in-the-loop for first 4-6 weeks via Telegram approve/reject bot. | Learn taste, catch theory errors before autonomy. |
