#!/usr/bin/env python3
"""List groups of concept cards from DIFFERENT schools that likely cover the same idea.

Grouping key: same topic, and (same street or pot_type) and >=1 shared concept tag or >=3 shared title words.
Output is a markdown list for a reviewer (or the merge-concepts skill) to turn into consensus_score updates,
`stance` annotations and `contradictions`.

Usage: python3 pipeline/ingest/consensus_candidates.py [--format cash-6max] [--min-schools 2]
"""
from __future__ import annotations
import argparse, itertools, re
from collections import defaultdict
import yaml
from common import CONCEPTS

STOP = set("the a an in on of to and or vs with for as at by is are be your you when from into out not".split())


def words(s: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9-]+", (s or "").lower()) if w not in STOP and len(w) > 2}


def load(fmt: str | None):
    for f in sorted(CONCEPTS.rglob("*.yaml")):
        if fmt and f.parent.name != fmt:
            continue
        for c in yaml.safe_load(f.read_text()) or []:
            c["_file"] = f.name
            c["_schools"] = {r["school"] for r in c.get("source_refs", [])}
            yield c


def related(a, b) -> bool:
    if a["topic"] != b["topic"] or a["_schools"] == b["_schools"]:
        return False
    if a.get("street") and b.get("street") and a["street"] != b["street"]:
        return False
    shared_tags = set(a.get("concepts", [])) & set(b.get("concepts", []))
    shared_words = words(a["title"]) & words(b["title"])
    return len(shared_tags) >= 1 or len(shared_words) >= 3


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--format")
    ap.add_argument("--min-schools", type=int, default=2)
    a = ap.parse_args()
    cards = list(load(a.format))
    # union-find over related pairs
    parent = {c["id"]: c["id"] for c in cards}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x

    by_topic = defaultdict(list)
    for c in cards:
        by_topic[c["topic"]].append(c)
    for group in by_topic.values():
        for x, y in itertools.combinations(group, 2):
            if related(x, y):
                parent[find(x["id"])] = find(y["id"])
    clusters = defaultdict(list)
    for c in cards:
        clusters[find(c["id"])].append(c)
    out = [cl for cl in clusters.values() if len({s for c in cl for s in c["_schools"]}) >= a.min_schools]
    out.sort(key=lambda cl: -len({s for c in cl for s in c["_schools"]}))
    print(f"# Consensus candidates\n\n{len(cards)} cards, {len(out)} cross-school clusters\n")
    for i, cl in enumerate(out, 1):
        schools = sorted({s for c in cl for s in c["_schools"]})
        print(f"## {i}. {cl[0]['topic']}  ({', '.join(schools)})")
        for c in sorted(cl, key=lambda c: sorted(c["_schools"])):
            print(f"- `{c['id']}` [{','.join(sorted(c['_schools']))}] {c['title']}")
        print()


if __name__ == "__main__":
    main()
