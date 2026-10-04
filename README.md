# Elite Poker Guide

Elite Poker Guide is a discovery and commerce hub for poker education.

Instead of browsing dozens of separate training sites, players can search a catalog of 1000+ poker training titles from 40+ schools across cash games, MTTs, PLO, Spin & Go, heads-up, live poker, mental game, software, books, and five language sections.

Selected listings reach up to 97% off original prices, with instant digital delivery and weekly catalog updates.

FOREVER LICENSE = lifetime access, no recurring subscription.

https://elitepokerguide.io/

---

## EPG Social Content Engine

This repository also hosts the autonomous educational content engine (Instagram, TikTok, YouTube) built on the knowledge inside the course catalog.

| Path | What |
|---|---|
| `docs/strategy/` | Strategy, roadmap, monetization, risks |
| `docs/decisions.md` | Decision log |
| `knowledge/` | Knowledge layer: source manifest, taxonomy, schema, **concept cards** (the product). Raw transcripts are gitignored. |
| `content/` | Voice, hard rules, hook bank, format templates, post queue |
| `pipeline/` | ingest -> generate -> render -> publish -> measure -> review |
| `.claude/skills/` | Claude Code skills that run the pipeline (`ingest-course`, `extract-concepts`) |

Start with `docs/strategy/social-content-automation-strategy.md`, then `pipeline/README.md`.
