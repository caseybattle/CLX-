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
