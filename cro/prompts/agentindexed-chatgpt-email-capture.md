# Paste this into the ChatGPT chat that built the AgentIndexed site (agentindexed.com)

I want AgentIndexed to capture every interested visitor's email BEFORE they have to sign in or pay,
so nobody who shows buying intent leaves without us being able to follow up. Please make these changes:

1. **Pricing page (/pricing/)** — on the Featured ($49), Pro ($19/mo) and Homepage Sponsor ($99/mo) cards,
   replace the "Manage … / Ask about sponsor availability" buttons with a short inline form:
   email (required), agent/product name (required), website URL (optional), and the chosen plan
   (pre-selected from the card). Button text: "Continue →".

2. **On submit, save the lead first** (before any sign-in or Stripe step) to the site's own storage, with:
   timestamp (UTC), plan, email, name, URL, page it came from. Then:
   - Featured / Pro → continue to the existing dashboard/sign-in flow with the email pre-filled,
     or straight to Stripe Checkout with the email pre-filled if the listing doesn't need review first.
   - Sponsor → show "Thanks — we'll email you within 24 hours about sponsor availability."
   Add a hidden honeypot field and ignore submissions where it's filled (bot protection).
   Validate the email format; clip long inputs.

3. **Submit page (/submit/)** — add the same email + name form above "Open listing dashboard", saving a
   lead with plan "free" before sending them to sign in, so we keep the email even if they never finish sign-in.

4. **Owner view** — give me (casbattle19@gmail.com) a private, signed-in-only page in the dashboard listing
   all captured leads, newest first, with a CSV download. Escape any cell starting with = + - @ in the CSV.

5. **Do not change** the Stripe webhook at /api/stripe-webhook or the existing payment verification.
   Keep the privacy policy accurate: add that we store the email and details entered in these forms to
   follow up about the listing or an unfinished checkout.

When done, tell me exactly which pages changed and how to test it without paying.
