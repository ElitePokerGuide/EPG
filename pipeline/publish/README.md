# publish

Thin wrapper around the Postiz CLI (`npm i -g postiz`). Postiz is self-hosted on our VPS and holds the OAuth connections to Instagram, TikTok, YouTube, Threads, Telegram.

Planned flow (Phase 0 step 4):

```
content/queue/<post-id>/{script.md, caption.txt, final.mp4|slides/*.png, meta.json}   (status: approved)
  -> postiz upload <media>            # every file must go through upload; raw paths are rejected
  -> postiz integrations:settings <id> # honour per-platform rules (TikTok: content_posting_method DIRECT_POST)
  -> postiz posts:create -c "<caption>" -m "<uploaded url>" -i "<integration>" --date <iso>
  -> meta.json gets postiz post id + scheduled time; folder moves to content/published/
```

Rules:
- Never post the same video to two of our accounts on one platform.
- Only `status: approved` posts leave the queue. The review bot sets that flag.
- Scheduling windows (EN audience): 12:00 and 19:00 America/New_York; staggered 10-20 min between platforms.
- Postiz analytics are pulled by `pipeline/measure` at +24h, +72h, +7d.
