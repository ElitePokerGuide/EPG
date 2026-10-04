#!/usr/bin/env python3
"""Extract concept cards from chunks with the Claude API.

Usage:
    ANTHROPIC_API_KEY=... python3 pipeline/ingest/extract_concepts.py --source rio-game-plan [--lesson 023] [--limit N] [--model MODEL]

Writes one YAML file per lesson: knowledge/concepts/<format>/<lesson_id with / -> __>.yaml
Idempotent: skips lessons that already have a file unless --force.
"""
from __future__ import annotations
import argparse, os, sys
from collections import defaultdict
from pathlib import Path
import yaml
from common import CHUNKS, CONCEPTS, KNOWLEDGE, ROOT, load_sources, read_jsonl

PROMPT = (Path(__file__).parent / "prompts" / "extract_concepts.md").read_text()
DEFAULT_MODEL = os.environ.get("EPG_EXTRACT_MODEL", "claude-sonnet-5-5")


def call_claude(client, model: str, user: str) -> str:
    resp = client.messages.create(
        model=model, max_tokens=8000, temperature=0.2,
        system="You output only valid YAML. No prose, no code fences.",
        messages=[{"role": "user", "content": user}],
    )
    return "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")


def parse_cards(text: str) -> list[dict]:
    text = text.strip().removeprefix("```yaml").removeprefix("```").removesuffix("```").strip()
    data = yaml.safe_load(text) or []
    return data if isinstance(data, list) else [data]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--lesson", help="lesson order prefix, e.g. 023")
    ap.add_argument("--limit", type=int, default=0, help="max lessons")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    try:
        import anthropic
    except ImportError:
        sys.exit("pip install anthropic")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set. Inside Claude Code use the extract-concepts skill instead.")
    client = anthropic.Anthropic()

    src = load_sources([a.source])[0]
    fmt = src["formats"][0]
    by_lesson = defaultdict(list)
    for ch in read_jsonl(CHUNKS / f"{a.source}.jsonl"):
        by_lesson[ch["lesson_id"]].append(ch)

    done = 0
    for lesson_id, chunks in sorted(by_lesson.items()):
        order = lesson_id.split("/")[1][:3]
        if a.lesson and order != a.lesson:
            continue
        out = CONCEPTS / fmt / (lesson_id.replace("/", "__") + ".yaml")
        if out.exists() and not a.force:
            continue
        cards, n = [], 1
        for ch in chunks:
            user = PROMPT.format(**{k: ch.get(k, "") for k in ("source_id", "school", "course", "title", "section", "chunk_id", "text")})
            for c in parse_cards(call_claude(client, a.model, user)):
                c["id"] = f"c-{fmt}-{c['id'].split('-', 2)[-1].rsplit('-', 1)[0]}-{n:03d}"; n += 1
                c.setdefault("status", "draft"); c.setdefault("consensus_score", 0.5)
                for ref in c.get("source_refs", []):
                    ref.setdefault("chunk", ch["chunk_id"])
                cards.append(c)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(yaml.safe_dump(cards, sort_keys=False, allow_unicode=True, width=100))
        print(f"{lesson_id}: {len(cards)} cards -> {out.relative_to(ROOT)}")
        done += 1
        if a.limit and done >= a.limit:
            break


if __name__ == "__main__":
    main()
