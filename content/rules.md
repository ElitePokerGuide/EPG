# Generation rules (hard constraints)

These are enforced by `pipeline/generate` QA and must never be relaxed by a prompt.

## Legal / IP
1. Source text is never reproduced. Max 8 consecutive words in common with any chunk in `knowledge/chunks/` (n-gram check).
2. Never mention a school, trainer, course name, or site (Run It Once, Carrot Corner, BlackRain79, 2 Card Confidence, Upswing, etc.). We say "top courses", "several coaches", "the schools we studied".
3. Never use audio, video, slides, screenshots, or hand histories from a course. Example hands are generalized or invented.
4. `source_refs` and `knowledge/raw|normalized|chunks` never appear in any output artifact.

## Platform policy (Meta, TikTok, YouTube)
5. Content is strategy education only. No poker room names, affiliate links, bonuses, deposit language, "win money", "get rich", "guaranteed".
6. No real-money gambling imagery (cash, chips being cashed out). Chips on a table in the replayer are fine.
7. Age gate: profiles marked 18+. Bio carries a responsible-play line.
8. No reposting the same video within one platform across our accounts. Cross-platform reuse is fine.

## Quality
9. A card is eligible for auto-publish only if `status: approved` and `consensus_score >= 0.6`. Lower scores can be published only in the "schools disagree" format which names the disagreement.
10. Every claim in a script must be traceable to a card. The generator cites card ids in `meta.json`; QA rejects scripts with uncited claims.
11. Every short has: hook (<= 1.5 s), one idea, one example, one takeaway, one CTA. Never two ideas.
12. Forbidden phrases list: see `voice.md`.
