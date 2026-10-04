#!/usr/bin/env python3
"""Render all concept cards as one readable markdown digest for owner review.

Usage: python3 pipeline/ingest/cards_digest.py [--format cash-6max] > docs/review/cards-<format>.md
Source refs are summarised as school codes only (never lesson text).
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import yaml
from common import CONCEPTS

TOPIC_ORDER = ["fundamentals", "preflop-ranges", "cbet-strategy", "turn-play", "river-play", "bluffing", "value-betting",
               "check-raising", "defending", "exploits", "bet-sizing", "board-textures", "blockers", "multiway",
               "bankroll-moving-up", "mental-game", "study-methods", "table-selection", "hand-reading", "tools-software"]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--format"); a = ap.parse_args()
    cards = []
    for f in sorted(CONCEPTS.rglob("*.yaml")):
        if a.format and f.parent.name != a.format:
            continue
        cards += yaml.safe_load(f.read_text()) or []
    by_topic = defaultdict(list)
    for c in cards:
        by_topic[c["topic"]].append(c)
    schools = Counter(r["school"] for c in cards for r in c.get("source_refs", []))
    print(f"# Concept cards digest{' - ' + a.format if a.format else ''}\n")
    print(f"{len(cards)} cards | by status: {dict(Counter(c['status'] for c in cards))} | source refs by school: {dict(schools)}\n")
    print("Review legend: ✅ approve as is · ✏️ approve with edit · ❌ reject (say why: wrong / obvious / not content-worthy / duplicate)\n")
    for topic in TOPIC_ORDER + sorted(set(by_topic) - set(TOPIC_ORDER)):
        if topic not in by_topic:
            continue
        print(f"\n## {topic}  ({len(by_topic[topic])})\n")
        for c in sorted(by_topic[topic], key=lambda c: (-c.get("consensus_score", 0), c["id"])):
            sch = ",".join(sorted({r["school"] for r in c.get("source_refs", [])}))
            meta = " · ".join(x for x in (c.get("level"), c.get("street"), c.get("pot_type"), c.get("position")) if x)
            print(f"### {c['title']}")
            print(f"`{c['id']}` · {meta} · consensus {c.get('consensus_score', 0):.2f} · sources: {sch} · **{c['status']}**\n")
            print(f"**Claim.** {c['claim']}\n")
            print(f"**Why.** {c['why']}\n")
            if c.get("common_mistake"):
                print(f"**Common mistake.** {c['common_mistake']}\n")
            if c.get("numbers"):
                print("**Numbers.** " + " · ".join(c["numbers"]) + "\n")
            if c.get("example_hand"):
                eh = c["example_hand"]
                print("**Example.** " + " | ".join(f"{k}: {v}" for k, v in eh.items()) + "\n")
            if c.get("contradictions"):
                print("**Schools disagree.** " + " / ".join(c["contradictions"]) + "\n")
            if c.get("hook_ideas"):
                print("**Hooks.** " + " · ".join(f"_{h}_" for h in c["hook_ideas"]) + "\n")
            print("Review: [ ]\n")


if __name__ == "__main__":
    main()
