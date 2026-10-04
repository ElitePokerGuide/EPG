---
name: merge-concepts
description: Build cross-school consensus cards from single-source concept cards. Use after extraction when several schools cover the same idea, when asked to compute consensus_score, find contradictions between schools, or prepare schools-disagree content.
---

# Merge concepts across schools

Goal: turn N single-source cards about the same idea into ONE consensus card with a real `consensus_score`, explicit `stance` per school and a `contradictions` list. Consensus cards are what the generator prefers; single cards stay as evidence.

## Procedure
1. `python3 pipeline/ingest/consensus_candidates.py --format <format>` lists clusters of cards from different schools that share topic and tags/title words. Clusters are coarse: a big cluster usually contains several distinct ideas. Split them by hand; ignore pairs that are not really the same idea.
2. Read the full cards in each true group (`knowledge/concepts/<format>/*.yaml`).
3. For each group write ONE consensus card into `knowledge/concepts/<format>/_consensus.yaml` (a YAML list):
   - `kind: consensus`, `id: c-<format>-x-<slug>-<nnn>` (x = cross-school), `merged_from: [ids]`
   - `title`, `claim`, `why` rewritten to express the shared idea; where schools differ, say so in `claim` or `why` in one sentence
   - `source_refs`: one entry per school with `stance: supports | nuances | contradicts` and a short `note` of the school's angle (internal only)
   - `consensus_score` = (supports + 0.5 * nuances) / total schools in the group. Round to 2 decimals. 1 school = 0.5 by convention
   - `contradictions`: one line per real disagreement, phrased as "Some coaches ... while others ..." (no school names)
   - keep `numbers` that at least two schools agree on; conflicting numbers go into `contradictions`
   - `hook_ideas`: 2-3, at least one using the schools-disagree archetype when `contradictions` is non-empty
   - `status: draft`
4. Do not modify or delete the single-source cards. (A later review step sets their status.)
5. Validate with `python3 pipeline/ingest/validate_cards.py` until clean.
6. Report: number of consensus cards, score distribution, and the 5 strongest disagreements (best material for the schools-disagree format).

## Judgement rules
- Same idea = a player would apply the same rule at the table. "C-bet small on ace-high boards" (RIO) and "ace-high flops need little protection so check more" (2CC) are related but NOT the same rule: the first is about size, the second about frequency. Two cards, possibly cross-linked in `why`.
- A micro-stakes exploitative coach and a solver-based coach "disagreeing" is often a difference in opponent model, not theory. Say that in `contradictions` ("against passive recreational pools ... against regulars ...").
