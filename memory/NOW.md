# NOW — working memory (survives compaction, /clear and new sessions)

> The agent rewrites this file at every checkpoint. Keep it short (< 60 lines).
> It is automatically re-injected after every compact / clear / resume.

## Current task
Verify AgentIndexed (agentindexed.com) Stripe checkout + webhook is wired end-to-end WITHOUT Casey paying, and find out what the 2 checkouts on Nov 7 were.

## What Casey said (verbatim-ish)
- Honkle (Google Play): ALREADY submitted for production and access granted. -> mark done in PROJECTS.md.
- Agent Indexed / LuckPanda price change: Casey doesn't know what it is. "It's a payment... figure out what's going on." -> investigate Gmail, explain, DRAFT any reply/acceptance; don't accept/pay without Casey's OK.
- BattleLabs Prompts: Casey doesn't remember it ("something old, don't know where it came from"). -> explain what it is from the chat/session.
- PR #4 (Stripe setup guide): "if you want it, I guess you can" merge it. -> check it's safe/mergeable, then merge.
- Bash Kings: YES, push the small-ramps branch to main. -> relay to the Bash Kings chat (or do it).
- KDP pilot / KDP research: Casey doesn't know what's going on. -> summarize KDP status plainly.

## Casey said 2026-11-10 ~23:00 UTC
- Stripe email was about the WEBHOOK; Casey re-pointed it to agentindexed.com/api/stripe-webhook; appears to work.
- No purchases yet. Stripe shows 2 checkout attempts on Nov 7 — unknown if test/Codex/real buyers.
- Live site checkout link opened a real payment page on his phone; he stopped before paying (doesn't want to be charged).
- Wants it confirmed connected correctly so the site can make money. Frustrated: saw Alex Finn's site already at $1,100.

## Findings
- Live site = static, Stripe Payment Links; webhook URL agentindexed.com/api/stripe-webhook = 404 (no API code). Payments still work without it. See cro/research/2026-11-10-agentindexed-payments-check.md.
- Stripe check DONE: BANK ACCOUNT DEACTIVATED (Chase ••6198) → payouts will fail; Casey must re-link in Stripe Settings → Payouts. Links active+correct. Nov 7 = China visitor/bot, $99 sponsor, abandoned. 0 sales ever (11 opens). Webhook is leftover from ChatGPT 'replacement' site → disable. Backlink wording mismatch site vs Stripe.

## Casey 2026-11-10 ~23:20 UTC
- Upset: visitors reach checkout and leave without email -> nobody to follow up. Wants the '2 cheap fixes' (capture email before checkout + abandoned-checkout recovery). 'We gotta fix that.'

## Casey 2026-11-11 ~01:30 UTC
- Says Stripe dashboard shows bank connected & fine. I re-verified via Stripe API myself: Chase ••6198 (routing 028000121) default USD, status=tokenized_account_number_deactivated; payouts_enabled=true; no requirements due; 0 payouts ever. Stripe docs: tokenized numbers can be deactivated/revoked and then can't be used for transfers. Advice: replace by MANUAL entry of real account+routing number (not Chase login/instant verify).

## 2026-11-11 ~01:40 UTC — BANK FIXED (verified via API)
- New default USD bank: Chase ••5628, routing 061092387, holder CASEY L BATTLE, status=new (normal for manual add). Old tokenized ••6198 removed. payouts_enabled=true, nothing due.
- Still open: disable dead webhook (agentindexed.com/api/stripe-webhook); Casey to pick email-capture storage (recommended Google Sheet); outreach to ~200 submitters.

## Decisions made (don't re-ask)
- Bash Kings: small-ramps -> main. Approved by Casey 2026-11-10.
- PR #4: OK to merge.
- Memory system done; PR #3 waiting on Casey to merge.

## Done so far
- PR #4 (Stripe guide) marked ready + squash-merged (485a72d). Repo default branch = claude/find-remote-jobs-egrQO.
- PROJECTS.md: Honkle moved to done; PR #4 merged; Bash Kings decision recorded.
- LuckPanda researched → cro/research/2026-11-10-agentindexed-luckpanda.md: NO payment owed; AgentIndexed is Casey's own directory. Flag: Stripe 'update bank account' email 30 Oct.
- BattleLabs/KDP/Bash Kings researched → cro/research/2026-11-10-battlelabs-kdp-bashkings.md.
- Relay to Bash Kings chat FAILED: desktop session, cloud can't message it without Casey's trusted-device approval. Casey to type answer there himself.
- Background agents (done): (1) LuckPanda/Agent Indexed Gmail read-only; (2) BattleLabs/KDP/Bash Kings session summaries + Bash Kings session id.

## Next step
- Casey: type 'push small-ramps to main' in the Bash Kings chat; re-login Claude Code on the KDP computer + retry; decide on BattleLabs (finish = ~1h: 8 Vercel env vars + merge PR #2 in promptlibrary); check Stripe 'update bank account' email in dashboard; merge PR #3.

## Open questions for Casey
-

_Last updated: 2026-11-10_
