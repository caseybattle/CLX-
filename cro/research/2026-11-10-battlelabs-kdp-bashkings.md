# BattleLabs Prompts, KDP, Bash Kings — status (researched 2026-11-10)
Desktop chats' transcripts are only readable from Casey's trusted device; details marked from summaries.

## BattleLabs Prompts (paid prompt library) — ~1 hour from taking money
- What: Next.js site "BattleLabs Prompts" on Vercel (project prompt-library), repo caseybattle/promptlibrary,
  Supabase login + Stripe. ~36 pages, 23 paid prompts gated. Started ~September 2026; chats from 2026-10-11.
- Price: 3 Months $39 (sub), Yearly $99 (sub), Lifetime $149 (one-time). Site shows "$149 founding vs $249"
  countdown ending Nov 10 (stale now).
- Domain promptbattle.site bought (Namecheap) and live.
- Payment code is in PR #2 (Stripe checkout, magic-link login, gated copying; 9 tests pass) — NOT merged as of
  Oct 11, so buy buttons do nothing on the live site.
- Left: (1) confirm 8 env vars in Vercel → prompt-library → Settings → Environment Variables (Prod + Preview):
  NEXT_PUBLIC_SUPABASE_URL, NEXT_PUBLIC_SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY, STRIPE_SECRET_KEY,
  STRIPE_WEBHOOK_SECRET, STRIPE_PRICE_QUARTERLY, STRIPE_PRICE_YEARLY, STRIPE_PRICE_LIFETIME;
  (2) merge PR #2; (3) test buy with card 4242…; (4) switch Stripe to live; (5) fix expired countdown.
- Unknown: traffic/demand, whether PR #2 merged after Oct 11.
- Chats: "BattleLabs Prompts domain launch" (desktop), "Prompt library site launch" (cloud, session_018YuwoAutmemQ5wWtQxwXjy).

## KDP (Amazon books)
- "kdp" chat (Nov 2, desktop): last turn failed Nov 4 because the login on that computer EXPIRED
  ("401 OAuth access token has expired") — not a content problem. Re-login to Claude Code on that computer + retry.
  What "the full pull" was: unknown (transcript unreadable).
- Old "kdp" chat (Oct 10 – Nov 2, archived): spec for a "murder word search" puzzle book (mystery told through
  word-search puzzles) in SPEC-WORDSEARCH.md on Casey's computer; no pages built. Open choice: new village setting
  for a 3-mystery pilot vs keep "Hotel Larkspur". Also a 96-page scene book PDF built, and an earlier book in KDP
  review. Titles/sales unknown; no KDP repo on GitHub.

## Bash Kings
- Desktop chat session_015gnkW4rs3ggB1eKvhCNKUp, repo caseybattle/bash-kings, branch small-ramps (2 unpushed
  commits + some uncommitted changes) → main. Casey decided 2026-11-10: push small-ramps to main.
