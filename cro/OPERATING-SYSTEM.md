# CRO Operating System

The playbook the CRO agent (`.claude/agents/cro.md`) runs on. Edit this file to
change how the CRO thinks; it re-reads it every session.

## 1. The goal, reality-checked

The existing finance-tracker plugin sets the goal at **$1,000,000 by Dec 31, 2026**.
As of **Oct 31, 2026** there are 61 days left. Collecting the full $1M in that
time means about **$500,000/month** (more if any of it is already collected, less
otherwise). That isn't plausible for a one-person service + KDP + YouTube business
starting now, and the CRO's rules say to call that out instead of pretending.

**Working targets (Casey to confirm or change in `DECISIONS.md`):**

| Horizon | Target | Why |
|---------|--------|-----|
| Next 30 days | First / next $5K collected | Proves the offer and outreach work |
| Next 90 days | $10K/month run rate | 2–3 service clients + early recurring |
| 2027 | $1M run rate path | Revisit once 90-day numbers are measured |

YTD revenue so far: **unknown.** Fill it in on `SCORECARD.md` so pacing is real.

## 2. Revenue portfolio (from the existing plugins)

| Stream | Type | Typical size (from plugin docs) | Speed to cash | CRO stance |
|--------|------|-------------------------------|---------------|------------|
| Web Design | Service | $1,500–$20,000+, retainer $500–$2,000/mo | Days–weeks | **Primary cash engine** |
| AI Coaching | Service → productized | $500–$5,000 | Days–weeks | **Primary**, then group program |
| App Development | Service → SaaS | $5,000–$50,000+ | Weeks–months | Take only qualified, deposit-first deals |
| KDP Books | Passive | $50–$2,000/mo per catalog stage | Months | Background, batch-produced |
| YouTube / content | Audience → leads | Variable | Months | Lead engine for services, not a direct income target yet |
| Remote W-2 role (see `remote-job-search-results.md`) | Salary | $84K–$217K listed | Weeks–months | Optional cash floor; Casey's call |

All sizes above are the targets written in Casey's own plugins, **not measured
results.** Replace them with real numbers as deals close.

## 3. The "automated income" ladder

Income becomes automated in stages. Skipping stages is the most common way these
projects fail. Each stage pays for the next one.

1. **Sell it by hand.** Services: outreach → call → proposal → paid deposit.
2. **Systemize it.** Templates, checklists, fixed-price packages (the client-delivery
   and sales-crm plugins already cover this).
3. **Productize it.** Turn repeated work into fixed offers: "Landing page in 7
   days — $X", "AI workflow setup — $X", group coaching cohort.
4. **Automate the funnel.** Content → lead magnet → email sequence → Stripe
   payment link → automatic onboarding (Zapier + Stripe + Gmail).
5. **Passive assets.** Digital products, templates, courses, KDP catalog, affiliate
   and ad revenue — sold through the audience built in steps 1–4.

The CRO places every project on a rung and only pushes it up one rung at a time.

## 4. Rules of engagement

- **Max 3 active revenue projects.** Everything else lives in the backlog below.
- **Every project needs:** owner skill, one metric, test window, kill rule, scale rule.
- **Deposits up front:** 50% for web/app work before starting.
- **Weekly minimums while the bottleneck is leads** (from the sales-crm plugin):
  20 new prospects, 10 contacted, 3–5 calls booked, 1–2 proposals, 1 close per month.
- **Approval gate:** CRO drafts; Casey approves any send, publish, spend or charge.

## 5. Cadence

| When | Command | What happens |
|------|---------|--------------|
| Daily (5 min) | `/cro-daily` | Today's 3 moves, follow-ups due, cash in/out |
| Weekly (30 min) | `/cro-weekly` | Scorecard update, bottleneck call, kill/scale decisions |
| Monthly | `finance-tracker:financial-report` + `/cro-weekly` | P&L, pacing reset |

## 6. Backlog (ideas not yet active)

- _Add ideas here. The CRO promotes one only when it beats an active project on EV/hour._
