# NOW — working memory (survives compaction, /clear and new sessions)

> The agent rewrites this file at every checkpoint. Keep it short (< 60 lines).
> It is automatically re-injected after every compact / clear / resume.

## Current task
_none active_. DECIDED 2026-11-11 ~03:45 UTC: Casey KEEPS agentindexed.com on the ChatGPT site (Option C, no extra spend). No DNS change. Stripe webhook stays ENABLED. Optional for Casey: paste cro/prompts/agentindexed-chatgpt-email-capture.md into ChatGPT. Vercel Site B left parked (not on domain).

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

## Email capture BUILT (2026-11-11 ~02:30 UTC)
- caseybattle/agentindexed draft PR #2 (branch capture-emails-before-checkout, 79ca3c4). Pricing buttons -> /submit/?plan=; form POSTs to LEADS_URL then Stripe same-tab w/ prefilled_email. Playwright 6/6 pass. Safe to merge before setup (mailto fallback).
- Casey must: create Google Sheet + paste ops/leads-apps-script.gs into Extensions→Apps Script → Deploy web app (Me / Anyone) → send URL. Then I set LEADS_URL in Vercel (project prj_glhh8XXdae9q6C4TnOaUgdtwTOkx, team team_TAkgSX0aGkwjFWeBLtAvo2e7) + merge PR #2 + verify live.

## 2026-11-11 ~02:45 UTC — switched to Vercel Blob (Casey: no Google Sheets, 'go ahead')
- Vercel MCP is READ-ONLY (403 on create blob store + create env). Code pushed to agentindexed PR #2 (api/lead.js, api/leads.js, package.json @vercel/blob 2.8.2). Local e2e all pass.
- Casey must in Vercel dashboard: agentindexed → Storage → Create → Blob → Private → name agentindexed-leads → connect (Production+Preview). Optional env LEADS_ADMIN_KEY (value in my scratchpad leadskey.txt) for /api/leads viewer; else view blobs in Storage browser.
- Then: Casey test-submits on preview URL; merge PR #2.

## 2026-11-11 ~02:55 UTC — Vercel token saved (env CB, host api.vercel.com, proxy-injected)
- Blob store store_NAEGD1Kt6u6vHbIk 'agentindexed-leads' private, connected to agentindexed (prod/preview/dev, BLOB_READ_WRITE_TOKEN). LEADS_ADMIN_KEY env set (value in scratchpad leadskey.txt — give Casey the leads page link). Redeploy dpl_4wxJ4YsaDm7cEnooK6Drbj6QneZo building; then verify check=1 → storage:true, POST test lead via API? (container can't reach *.vercel.app; use Vercel sandbox or Casey test), merge PR #2.

## Next step (AgentIndexed)
- On hold per Casey: $49 Featured upgrade email to ~200 past submitters. Offer when Casey ready.
- Optional: add new leads to morning brief; delete Casey's TEST lead; backlink wording mismatch (site says dofollow, Stripe product says no ranking credit).

## 2026-11-11 ~03:35 UTC Fable advisor
- Only GitHub repo is caseybattle/agentindexed (Site B); Site A code lives only in ChatGPT Sites.
- Advisor: Vercel Hobby forbids commercial → Site B needs Vercel Pro $20/mo (+spend cap) or Cloudflare Pages free (rewrite). Recommends Site B on Vercel Pro. See cro/research/2026-11-11-agentindexed-hosting-advisor.md. Awaiting Casey: A) Vercel Pro $20, B) Cloudflare free (I rebuild), C) keep ChatGPT site.

## Decisions made (don't re-ask)
- 2026-11-11: AgentIndexed stays on ChatGPT Sites; no Vercel Pro, no Cloudflare move, no DNS change. Don't re-propose unless Casey asks.
- 2026-11-11: HOLD the $49 upgrade outreach to ~200 submitters until email capture is in place.
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
