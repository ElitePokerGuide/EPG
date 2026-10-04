# Review queue

`cards-cash-6max.md` is a generated digest of every concept card in `knowledge/concepts/cash-6max/`. Regenerate with:

```bash
python3 pipeline/ingest/cards_digest.py --format cash-6max > docs/review/cards-cash-6max.md
```

## How to review (owner)

Part 1 (27 consensus cards) is the priority. These are what the first scripts will be written from. Part 2 (330 single-source cards) can be skimmed by topic; cards marked **needs-review** carry a note explaining why.

For each card mark the `Review: [ ]` line:
- `[✅]` approve as is
- `[✏️ <what to change>]` approve with an edit
- `[❌ <why>]` reject: wrong / obvious / not content-worthy / duplicate / too advanced for the audience

Then commit the file (or paste the marked lines back into the chat). The next engine run reads the marks, sets `status` on the YAML cards, and only `approved` cards flow into script generation.

Things worth your eye in particular:
- Any claim you believe is wrong for current 6-max games.
- Cards whose source is heads-up oriented (notes say "HU"): keep, re-tag or drop.
- The exploitative micro-stakes cards (school code br79): they assume passive recreational opponents. The consensus cards say this explicitly; the single cards do not.
