#!/usr/bin/env python3
"""Split combined course transcript files into one lesson per record.

Input format (as delivered):
    ================================================================================
    FILE_PATH: 4. Gameplan\\2. 3bet Pots\\Checking as the Preflop Raiser Run It Once.txt
    ================================================================================
    <transcript text>

Output: knowledge/normalized/<source-id>.jsonl, one line per lesson:
    {source_id, school, course, lesson_id, lesson_path, section, title, order, words, text}
"""
from __future__ import annotations
import hashlib, re, sys
from common import RAW, NORMALIZED, load_sources, write_jsonl, slugify

HEADER = re.compile(r"^=+\s*\nFILE_PATH:\s*(.+?)\s*\n=+\s*\n", re.M)
NOISE_SUFFIXES = (" run it once", " run it once.txt", ".txt", ".mp4", "_mp4")


def clean_title(path: str) -> tuple[str, str]:
    parts = [p for p in re.split(r"[\\/]+", path) if p]
    title = parts[-1]
    low = title.lower()
    for suf in NOISE_SUFFIXES:
        if low.endswith(suf):
            title, low = title[: -len(suf)], low[: -len(suf)]
    title = re.sub(r"[_]+", " ", title).strip()
    section = " / ".join(parts[:-1])
    return title, section


def normalize_text(t: str) -> str:
    t = t.replace("\r", "")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def split(src: dict) -> list[dict]:
    raw = (RAW / src["file"]).read_text(errors="replace")
    matches = list(HEADER.finditer(raw))
    if not matches:
        # whole file is one lesson
        return [dict(lesson_path=src["file"], text=raw)]
    out = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
        out.append(dict(lesson_path=m.group(1), text=raw[m.end():end]))
    return out


def main(ids):
    for src in load_sources(ids or None):
        path = RAW / src["file"]
        if not path.exists():
            if src.get("status") != "pending":
                print(f"skip {src['id']}: {path.name} not in knowledge/raw/", file=sys.stderr)
            continue
        rows, seen, dupes = [], set(), 0
        for order, lesson in enumerate(split(src), 1):
            title, section = clean_title(lesson["lesson_path"])
            text = normalize_text(lesson["text"])
            if len(text.split()) < 50:
                continue
            # combined files sometimes contain the same lesson twice (re-packs); keep the first copy
            h = hashlib.sha1(text[:5000].encode()).hexdigest()
            if h in seen:
                dupes += 1
                continue
            seen.add(h)
            rows.append(dict(
                source_id=src["id"], school=src["school"], course=src["course"],
                lesson_id=f"{src['id']}/{order:03d}-{slugify(title)}",
                lesson_path=lesson["lesson_path"], section=section, title=title,
                order=order, words=len(text.split()), text=text,
            ))
        n = write_jsonl(NORMALIZED / f"{src['id']}.jsonl", rows)
        print(f"{src['id']}: {n} lessons, {sum(r['words'] for r in rows):,} words" + (f", {dupes} duplicate lesson(s) dropped" if dupes else ""))


if __name__ == "__main__":
    main(sys.argv[1:])
