"""Shared helpers for the ingest pipeline."""
from __future__ import annotations
import json, re, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
KNOWLEDGE = ROOT / "knowledge"
RAW, NORMALIZED, CHUNKS, CONCEPTS = (KNOWLEDGE / d for d in ("raw", "normalized", "chunks", "concepts"))


def load_sources(ids: list[str] | None = None) -> list[dict]:
    data = yaml.safe_load((KNOWLEDGE / "sources.yaml").read_text())
    srcs = [s for s in data["sources"] if s.get("status") != "skipped"]
    if ids:
        srcs = [s for s in srcs if s["id"] in ids]
        missing = set(ids) - {s["id"] for s in srcs}
        if missing:
            sys.exit(f"unknown source ids: {sorted(missing)}")
    return srcs


def school_name(code: str) -> str:
    return yaml.safe_load((KNOWLEDGE / "sources.yaml").read_text())["schools"].get(code, code)


def read_jsonl(path: Path):
    with path.open() as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def write_jsonl(path: Path, rows) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with path.open("w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
            n += 1
    return n


def slugify(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return re.sub(r"-{2,}", "-", s)[:60]
