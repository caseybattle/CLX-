# AgentIndexed hosting — Fable advisor recommendation (2026-11-11)
(Facts from search excerpts of official pages; advisor could not fully load vercel.com. Nothing changed.)

- Vercel Hobby (free) = non-commercial personal use only → selling placements isn't allowed there.
  Cheapest compliant: Vercel Pro $20/mo (1 seat + $20 usage credit). Default spend alert at $200 is NOT a hard
  stop → set Spend Management limit with "pause projects".
- ChatGPT Sites: OpenAI help says selling via third-party processor (Stripe) is allowed; public beta, Plus limits unverified.
- Site A (live, ChatGPT Sites) requires a Sites account + listing + review before paying → very likely hurting sales;
  page says "replacement design preview". Code not in GitHub (only editable via ChatGPT).
- Recommendation: point agentindexed.com to Site B (GitHub/Vercel) on Vercel Pro with a spend cap.
  Free fallback: Cloudflare Pages + Functions + KV (rewrite /api/lead, /api/leads; Casey creates CF account).
- Next steps: (1) Casey upgrades Vercel to Pro + spend cap; (2) screenshot Namecheap DNS, switch A @ + www CNAME,
  Claude verifies + test checkout; (3) Claude drafts $49 Featured email to ~200 submitters for Casey's approval.
Sources: vercel.com/docs/limits/fair-use-guidelines, /docs/plans/hobby, /docs/plans/pro-plan,
help.openai.com/en/articles/20001339-creating-and-managing-chatgpt-sites, developers.cloudflare.com/pages/functions/pricing
