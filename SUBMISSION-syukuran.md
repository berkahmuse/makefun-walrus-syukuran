# SUBMISSION — @syukuran — walrus one-line bounty pitch

- Competition: `u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf`
  ("One Line That Makes a Builder Fund a Bounty")
- Window: opens 2026-11-23T03:00:00Z (10:00 WIB), deadline 2026-11-23T04:00:00Z (11:00 WIB)
- Account: @syukuran — **NOT submitted via CLI. User submits via website + wallet.**
- Wallet: `74762NBmesesGsfr2TuEk7jauhhRi3kBxqMZKw6dFnE2`
  (from verified record in `~/workspace/makefun-watch/seen.json`, entry best-game-01 → syukuran → wallet; same address in all prior syukuran entries)
- Repo (local): `~/workspace/makefun-walrus/engine-syukuran/`
- Commit: `23485de35e99ae4ab8d7f2efde9ba086c3eda3b9` (HEAD at check time;
  a later commit only updates this SUBMISSION file, not the entry)
- Git identity (repo-local only): Berkah <sukur.sukurjp@gmail.com>

## Entry

`main.py` writes to `/output/entry.txt` (151 characters, one sentence):

> Fund a bounty on make.fun and pay only the build that wins: AI agents race for your prize, so your money buys a proven result, never hours or promises.

Angle: pay only for the winning result — not for promises, hours, or process.
Written from scratch; distinct from the other two entries for this bounty:
- @berkahmuse-2 (145 chars): "Put a reward on make.fun and AI agents race to build your idea — the best entry wins, the payout is public, and one bounty buys you working code."
- @berkahmuse (164 chars): "Post your prize on make.fun and in minutes your idea is a live contest where AI agents race to build it — no hiring, no interviews, the best entry wins your reward."

## Self-check

- Ran `python3 main.py` twice, before and after a second edit that added the
  1–240 gate check: outputs byte-identical every time.
- sha256 of `/output/entry.txt`: `1552c9f103ad50646ec8b66c7c1ecabfa19a8abbdf3d8fcf84718e6600418618`
- Length: 151 characters (UTF-8), one sentence, not whitespace-only. Gate 1–240: PASS.

## Kit pre-submit check

- Command: `node <kit>/cli/makefun.mjs check --kit <kit> --repo engine-syukuran --commit 23485de35e99ae4ab8d7f2efde9ba086c3eda3b9 --transcripts ~/workspace/makefun-walrus/transcripts-syukuran.tar.gz`
- Result (2026-11-23T03:36:38Z): **13 passed, 1 failed, 5 skipped, 5 checked at submission.**
- Passes incl: competition_open, snapshot, license_osi (MIT), entrypoint
  (main.py → python3.13), transcripts_present/recorded, thinking_wellformed,
  thinking_in_window, thinking_reproduces (85/89 lines, 95.5%; main.py 22
  authored lines), thinking_turns (74), thinking_revised (main.py from 2
  messages — fixed by the gate-check edit), transcripts_run_record,
  thinking_own_work.
- **FAIL: thinking_priced only** — 0 usage rows attached (see Transcript).
  Fix is parent-side after this run completes (see below).
- At-submission checks (for the website submit step): repo_public, repo_owner
  (owner.json already committed), repo_created_after_open (GitHub repo must be
  created after 03:00:00Z), commit_in_repo (push), duplicate_snapshot.

## Transcript

- `makefun record` did NOT start for this competition: this competition does not
  take recorded transcripts (HTTP 400 for the sibling agent accounts: "does not
  take recorded transcripts: its entries upload their transcripts (a bundle or
  loose files) as the requirements say"). My attempt failed earlier with
  HTTP 401 invalid API key (no @syukuran CLI credentials exist by design).
- Bundle: `~/workspace/makefun-walrus/transcripts-syukuran.tar.gz`
  (234.126 bytes, sha256 `3f402f5e28cc244e07e172066fa4e34320f9788dc6eea8307b173ea60bf30c51`)
  — re-bundled after the gate-check edit; 2 sessions (builder 08b557f9…,
  parent 680b80e2…), prompt = cron body (scheduled, via "cron job
  makefun-walrus-early-run"), MCP none, provider meta, model muse-spark-1.3,
  effort default. Bundle redacted credentials automatically.
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

- Built + committed + self-check PASS + kit check 13/14 (only thinking_priced
  fails, parent-side fix). Verifier verdict: pending (parent spawns
  independent verifier).
- **NOT SUBMITTED — awaiting user submit via website + wallet before 11:00 WIB.**

## What the parent / user still must do before website submit

1. **Usage rows (BLOCKER for the transcript gate):** after this builder run
   completes, run in muse.db:
   `SELECT u.agent_id AS agent_id, u.message_id AS message_id, u.created_at AS created_at, u.input_tokens AS input_tokens, u.output_tokens AS output_tokens, a.model AS model FROM agent.agent_message_token_usage u JOIN agent.agents a ON a.agent_id = u.agent_id WHERE u.agent_id IN ('08b557f9-c700-4cf0-9616-18f21b788d8a','680b80e2-b433-4126-9d99-5a89c1d3c2ad') ORDER BY u.created_at DESC LIMIT 500`
   → write rows unchanged to `~/.makefun/muse-usage-walrus-syukuran.jsonl`,
   then re-bundle with `--muse-usage` added (same flags as before) and re-run
   `check` — thinking_priced must pass.
2. **GitHub repo:** create a NEW public repo (after 03:00:00Z — now is fine),
   push the final commit, set README badges + About (repo must be public,
   owner = berkahmuse GitHub login; owner.json already names the @syukuran
   wallet).
3. **Verifier:** independent verifier must rerun 2× byte-identical + PASS
   before the user submits.
4. **User submit via website + Phantom** (wallet
   `74762NBmesesGsfr2TuEk7jauhhRi3kBxqMZKw6dFnE2`) before **11:00 WIB**,
   uploading the final `transcripts-syukuran.tar.gz` (no bundle download
   needed at submit time — the file is ready in ~/workspace/makefun-walrus/).
