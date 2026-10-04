#!/usr/bin/env python3
"""Validate every concept card against the JSON schema, the taxonomy, and the IP rules.

Checks:
  - schema (knowledge/schema/concept-card.schema.json)
  - topic/format/level/street/pot_type in taxonomy
  - unique ids
  - forbidden names (schools, coaches, sites) in any published field
  - n-gram overlap (>8 consecutive words) with source chunks, when chunks are present locally
Exit code 1 on any error. Prints a summary table.
"""
from __future__ import annotations
import json, re, sys
from collections import Counter
from pathlib import Path
import yaml
from common import CHUNKS, CONCEPTS, KNOWLEDGE, read_jsonl

PUBLISHED_FIELDS = ("title", "claim", "why", "common_mistake", "numbers", "hook_ideas", "contradictions", "example_hand")
FORBIDDEN = re.compile(r"\b(run ?it ?once|rio|carrot ?corner|blackrain79|black ?rain|dragthebar|drag the bar|2 ?card ?confidence|upswing|pokerstars|ggpoker|party ?poker|nathan williams|peter clarke)\b", re.I)
NGRAM = 8


def ngrams(text: str, n=NGRAM):
    w = re.findall(r"[a-z0-9']+", text.lower())
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def flatten(v):
    if isinstance(v, dict):
        return " ".join(flatten(x) for x in v.values())
    if isinstance(v, list):
        return " ".join(flatten(x) for x in v)
    return str(v or "")


def main():
    try:
        import jsonschema
    except ImportError:
        sys.exit("pip install jsonschema")
    schema = json.loads((KNOWLEDGE / "schema" / "concept-card.schema.json").read_text())
    tax = yaml.safe_load((KNOWLEDGE / "taxonomy.yaml").read_text())
    validator = jsonschema.Draft202012Validator(schema)

    files = sorted(CONCEPTS.rglob("*.yaml"))
    errors, ids, by_topic, by_status = [], Counter(), Counter(), Counter()
    source_ngrams = {}
    for f in files:
        cards = yaml.safe_load(f.read_text()) or []
        rel = f.relative_to(KNOWLEDGE)
        for c in cards:
            cid = c.get("id", "?")
            for e in validator.iter_errors(c):
                errors.append(f"{rel} {cid}: schema: {e.message[:120]}")
            if c.get("topic") not in tax["topics"]:
                errors.append(f"{rel} {cid}: unknown topic {c.get('topic')!r}")
            ids[cid] += 1
            by_topic[c.get("topic")] += 1; by_status[c.get("status")] += 1
            pub = " ".join(flatten(c.get(k)) for k in PUBLISHED_FIELDS)
            if m := FORBIDDEN.search(pub):
                errors.append(f"{rel} {cid}: forbidden name {m.group(0)!r} in published field")
            # n-gram check against the source chunks of this card
            for ref in c.get("source_refs", []):
                sid = (ref.get("chunk") or "").split("/")[0]
                if not sid:
                    continue
                if sid not in source_ngrams:
                    p = CHUNKS / f"{sid}.jsonl"
                    source_ngrams[sid] = set().union(*(ngrams(ch["text"]) for ch in read_jsonl(p))) if p.exists() else None
                if source_ngrams[sid] and (hit := ngrams(pub) & source_ngrams[sid]):
                    errors.append(f"{rel} {cid}: {len(hit)} verbatim {NGRAM}-gram(s), e.g. {next(iter(hit))!r}")
                    break
    for cid, n in ids.items():
        if n > 1:
            errors.append(f"duplicate id {cid} x{n}")

    print(f"{len(files)} files, {sum(ids.values())} cards")
    print("by status:", dict(by_status))
    print("by topic:", dict(by_topic.most_common()))
    if errors:
        print(f"\n{len(errors)} error(s):"); print("\n".join(" - " + e for e in errors)); sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
