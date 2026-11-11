# AgentIndexed payments check (2026-11-10, read-only)

## How payments actually work on the live site (verified)
- Live production deploy = GitHub caseybattle/agentindexed @ 3173a1b (Oct 24), static site built by gen.py.
- Buttons go straight to Stripe-hosted **Payment Links** (no server code involved):
  - Featured $49 one-time: https://buy.stripe.com/3cI28r4Wm0Z4bnS0T79oc0a
  - Pro $19/mo:           https://buy.stripe.com/14A00j88yazEajOatH9oc0b
  - Homepage Sponsor $99/mo: https://buy.stripe.com/3cI5kD60qazE2Rm8lz9oc0c
  - /submit/ opens Featured/Pro links with prefilled_email + client_reference_id.
- Fulfillment is MANUAL: buyer emails details to casbattle19@gmail.com; Casey matches the Stripe payment.
  => Stripe collects the money even with NO webhook. A webhook is not needed for this site to get paid.

## Problem found
- The webhook Casey pointed at **agentindexed.com/api/stripe-webhook returns 404 NOT_FOUND** (verified on the
  live production deployment 2026-11-10 23:10 UTC). There is no /api code in the site at all.
- Effect: every Stripe event to that endpoint fails; Stripe retries for ~3 days, emails failure warnings, and
  may auto-disable the endpoint. It does NOT block payments.
- Fix options: (a) delete/disable that webhook endpoint in Stripe (recommended — nothing uses it), and turn on
  Stripe email notifications for successful payments so Casey hears about every sale; or (b) build a real
  /api/stripe-webhook (auto-fulfillment) — more work, not needed to start making money.

## Stripe account check (live, read-only, 2026-11-10)
- **BLOCKER: bank account Chase ••6198 status = `tokenized_account_number_deactivated`.** Payouts will likely FAIL
  until Casey re-links/updates the bank in Stripe Dashboard → Settings → Payouts (this is the Oct 30
  "[Action Required] Update Your Stripe Bank Account" email). charges_enabled/payouts_enabled still true;
  no other requirements due. Payouts weekly Monday. Balance $0.
- Payment Links all ACTIVE, correct prices, redirect to agentindexed.com/thanks/: Featured $49 one-time,
  Pro $19/mo, Homepage Sponsor $99/mo. => checkout itself is correctly connected.
- Nov 7 "2 checkouts" = 2 sessions opened Nov 6 (09:50 & 10:35 ET) on the $99 Homepage Sponsor link,
  expired Nov 7, no email entered, priced in Chinese yuan (visitor located in/through China). Not Casey,
  not a test; likely an outside visitor or bot. Nothing purchased.
- History: 11 checkout sessions opened since Jul 19 (Featured/Pro/Sponsor); **0 ever completed**; $0 collected.
- Webhook we_1UVC2g… → agentindexed.com/api/stripe-webhook, created Oct 27 by the "AgentIndexed replacement"
  (ChatGPT-built) project — the live site has no such route (404). Events stuck pending_webhooks=1.
  Second webhook (viral-score-analyzer.vercel.app) unrelated.
- No coupons/promo codes; payment links have allow_promotion_codes=false (a $0 self-test needs: enable promo
  codes on the link + create a 100%-off code — Stripe writes, need Casey's OK).
- Inconsistency: Nov 8 API edit changed Featured/Pro product descriptions to "Paid placement; links do not pass
  search-ranking credit", but the live pricing page still says "Every listing includes a dofollow backlink".

## Update 2026-11-11: bank fixed
Casey added Chase ••5628 manually (routing 061092387). Verified via API: default for USD, status 'new' (normal
for a manually entered account; it becomes validated once a payout succeeds). Old tokenized ••6198 is gone.

## Update 2026-11-11 02:54 UTC: email capture LIVE
- caseybattle/agentindexed PR #2 merged (2fa3300); production agentindexed.com = dpl_351TruLdS5ZwQEKqePgYsq44itJK.
- Pricing buttons → /submit/?plan=… → lead saved to private Vercel Blob store `agentindexed-leads`
  (store_NAEGD1Kt6u6vHbIk) via /api/lead → then Stripe with email pre-filled.
- Owner leads page: /api/leads?key=<LEADS_ADMIN_KEY in Vercel env> (&format=csv). Health: /api/lead?check=1.
- Verified end-to-end with Casey's real test (featured, saved 02:52:42 UTC, landed on Stripe $49 page).
- Webhook we_1UVC2g… disabled. Vercel API token saved on cloud env "CB" (proxy-injected for api.vercel.com).
