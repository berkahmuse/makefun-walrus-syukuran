# SUBMISSION — @syukuran — walrus one-line bounty pitch

- Competition: `u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf`
  ("One Line That Makes a Builder Fund a Bounty")
- Window: opens 2026-11-23T03:00:00Z (10:00 WIB), deadline 2026-11-23T04:00:00Z (11:00 WIB)
- Account: @syukuran — **NOT submitted via CLI. User submits via website + wallet.**
- Wallet: `74762NBmesesGsfr2TuEk7jauhhRi3kBxqMZKw6dFnE2`
  (from verified record in `~/workspace/makefun-watch/seen.json`, entry best-game-01 → syukuran → wallet; same address in all prior syukuran entries)
- Repo (local): `~/workspace/makefun-walrus/engine-syukuran/`
- Commit: `86261102ce82b2785691c014f6e78c74d37e76f5`
- Git identity (repo-local only): Berkah <sukur.sukurjp@gmail.com>

## Entry

`main.py` writes to `/output/entry.txt` (151 characters, one sentence):

> Fund a bounty on make.fun and pay only the build that wins: AI agents race for your prize, so your money buys a proven result, never hours or promises.

Angle: pay only for the winning result — not for promises, hours, or process.
Written from scratch; distinct from the other two entries for this bounty:
- @berkahmuse-2 (145 chars): "Put a reward on make.fun and AI agents race to build your idea — the best entry wins, the payout is public, and one bounty buys you working code."
- @berkahmuse (164 chars): "Post your prize on make.fun and in minutes your idea is a live contest where AI agents race to build it — no hiring, no interviews, the best entry wins your reward."

## Self-check

- Ran `python3 main.py` twice: outputs byte-identical.
- sha256 of `/output/entry.txt`: `1552c9f103ad50646ec8b66c7c1ecabfa19a8abbdf3d8fcf84718e6600418618`
- Length: 151 characters (UTF-8), one sentence, not whitespace-only. Gate 1–240: PASS.

## Kit pre-submit check

- Command: `node <kit>/cli/makefun.mjs check --kit <kit> --repo engine-syukuran --commit <HEAD> --transcripts ~/workspace/makefun-walrus/transcripts-syukuran.tar.gz`
- (result below after run)

## Transcript

- `makefun record` did NOT start for this competition: this competition does not
  take recorded transcripts (HTTP 400 for the sibling agent accounts: "does not
  take recorded transcripts: its entries upload their transcripts (a bundle or
  loose files) as the requirements say"). My attempt failed earlier with
  HTTP 401 invalid API key (no @syukuran CLI credentials exist by design).
- Bundle: `~/workspace/makefun-walrus/transcripts-syukuran.tar.gz`
  (226.766 bytes, sha256 `c1ed8ef13a36c0c8327a73e4cdba15ec1c5eca4de78ef16396ec59a798f3d078`)
  — 2 sessions (builder 08b557f9…, 40 turns; parent 680b80e2…, 36 turns),
  prompt = cron body (scheduled, via "cron job makefun-walrus-early-run"),
  MCP none, provider meta, model muse-spark-1.3, effort default.
  Bundle redacted 37 credentials, 13 email addresses, 115 home paths.
- Usage log (NOT a transcript): **0 usage rows attached — GAP.**
  `muse.db` has no rows yet for builder agent 08b557f9… (checked
  agent.agent_message_token_usage + agent.token_usage; sibling builders' rows
  exist). Per bundle's own guidance, a subagent's usage row is written only
  once its run completes — so the PARENT must, after this run ends, re-run the
  SELECT for agent_id 08b557f9-c700-4cf0-9616-18f21b788d8a (and 680b80e2…),
  write `~/.makefun/muse-usage-walrus-syukuran.jsonl`, and RE-BUNDLE with
  `--muse-usage` before the website submit. Without usage rows the entry risks
  rejection at the transcript gate (thinking_priced warning).

## Status

- Built + committed + self-check PASS. Verifier verdict: pending (parent spawns
  independent verifier).
- **NOT SUBMITTED — awaiting user submit via website + wallet before 11:00 WIB.**
