#!/usr/bin/env python3
"""Chunk normalized lessons into ~TARGET-word, sentence-aligned pieces with overlap.

Output: knowledge/chunks/<source-id>.jsonl
    {chunk_id, source_id, school, course, lesson_id, title, section, idx, n_chunks, words, text}
"""
from __future__ import annotations
import re, sys
from common import NORMALIZED, CHUNKS, load_sources, read_jsonl, write_jsonl

TARGET, OVERLAP, MIN_TAIL = 1500, 150, 400
SENT = re.compile(r"(?<=[.!?])\s+")


def chunk_text(text: str):
    sents = SENT.split(text)
    chunks, cur, cur_n = [], [], 0
    for s in sents:
        n = len(s.split())
        if cur_n + n > TARGET and cur:
            chunks.append(" ".join(cur))
            # overlap: keep trailing sentences up to OVERLAP words
            tail, tail_n = [], 0
            for t in reversed(cur):
                if tail_n + len(t.split()) > OVERLAP:
                    break
                tail.insert(0, t); tail_n += len(t.split())
            cur, cur_n = tail, tail_n
        cur.append(s); cur_n += n
    if cur:
        if chunks and cur_n < MIN_TAIL:
            chunks[-1] = chunks[-1] + " " + " ".join(cur)
        else:
            chunks.append(" ".join(cur))
    return chunks


def main(ids):
    for src in load_sources(ids or None):
        path = NORMALIZED / f"{src['id']}.jsonl"
        if not path.exists():
            continue
        rows = []
        for lesson in read_jsonl(path):
            pieces = chunk_text(lesson["text"])
            for i, p in enumerate(pieces, 1):
                rows.append(dict(
                    chunk_id=f"{lesson['lesson_id']}#{i:02d}", source_id=src["id"], school=src["school"],
                    course=src["course"], lesson_id=lesson["lesson_id"], title=lesson["title"],
                    section=lesson["section"], idx=i, n_chunks=len(pieces), words=len(p.split()), text=p,
                ))
        n = write_jsonl(CHUNKS / f"{src['id']}.jsonl", rows)
        print(f"{src['id']}: {n} chunks")


if __name__ == "__main__":
    main(sys.argv[1:])
