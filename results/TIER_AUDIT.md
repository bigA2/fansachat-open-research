# Tier audit: FansaChat plans vs Zapier, Make, n8n, Activepieces, Lindy, Relay (1 Nov 2026)

All competitor facts come from public pages, with the URL next to each one. Crawled copies are in `results/sources/`.
Prices are monthly in USD unless a page gives another currency. **The founder decides**: this file only recommends.

## Source status

| product | page | status |
|---|---|---|
| Zapier | https://zapier.com/pricing | read (`sources/pricing/00.md`) |
| Zapier | https://help.zapier.com/hc/en-us/articles/8496181445261 (Zap limits) | read (`sources/notifications/02.md`) |
| Zapier | team help pages 8496270839565 and 8496307853709 | **source not reached**: both return "The page you were looking for doesn't exist" (`sources/teams/00.md`, `01.md`). Team facts below come from the pricing page instead. |
| Make | https://www.make.com/en/pricing, https://www.make.com/en/help/general/teams | **source not reached** (crawl failed and make.com is blocked by this session's network). Only secondary sources found by web search are used and marked "secondary". |
| n8n | https://n8n.io/pricing/ | read (`sources/pricing/02.md`) |
| n8n | https://docs.n8n.io/user-management/rbac/projects/ | read (`sources/teams/02.md`) |
| Activepieces | https://www.activepieces.com/pricing | read (`sources/pricing/03.md`) |
| Lindy | https://www.lindy.ai/pricing | read (`sources/pricing/04.md`) |
| Relay | https://relay.app/pricing | read: **Relay has shut down** (`sources/pricing/05.md`) |

## 1. Side-by-side

### FansaChat (from the brief)

| plan | price | runs / mo | AI builds / mo | users | workflows |
|---|---|---|---|---|---|
| Starter | $15 | 2,000 | 100 | unlimited | unlimited |
| Pro | $45 | 10,000 | 400 | unlimited | unlimited |
| Team | $149 | 30,000 | 1,500 | 2-10 people | unlimited |
| Scale | $299 | 100,000 | 5,000 | unlimited | unlimited |

Note: Team says "2-10 people" and "unlimited users" at the same time. Those two claims conflict; pick one.

### Zapier (https://zapier.com/pricing)

| plan | price | tasks | users | workflows / steps | team features |
|---|---|---|---|---|---|
| Free | $0 | 100 tasks/mo | 1 seat | "Unlimited Zaps", two-step Zaps only | - |
| Professional | "Starting from $19.99/month" | task tier chosen with a slider (100 to 2M tasks/mo); the crawled text does not say which tier the starting price is | 1 seat | unlimited Zaps, multi-step | - |
| Team | "Starting from $69/month" | same slider | 25 seats | unlimited Zaps, multi-step | "Shared Zaps and folders", "Shared app connections", "SAML SSO", shared workspace, folder permissions, approval requests (beta) |
| Enterprise | contact sales | annual task limits | unlimited | multi-step | advanced admin permissions, app access controls, audit log, SCIM, "Workspaces" (new) |

- A task is counted "each time an action step in your Zap runs successfully. Trigger, filter, and certain built-in tool steps do not count" (https://help.zapier.com/hc/en-us/articles/8496181445261).
- Every Zap is limited to **100 steps**; each action step to 1,000 fields (same page).
- At the task limit, runs are "held, not lost" and can be replayed, or pay-per-task billing takes over (same page and https://zapier.com/pricing FAQ).
- Paid plans include "Custom error notifications" and "Alerts (New)" (https://zapier.com/pricing).

### Make (secondary sources only; make.com not reached)

- Credits replaced operations; one credit is one module action (https://www.jetadmin.io/blog/make-pricing/, https://latenode.com/blog/make-com-pricing).
- Free: 1,000 credits/mo and **2 active scenarios**. Core, Pro and Teams start at 10,000 credits/mo (same sources).
- Most-quoted annual-billing prices: Core $9, Pro $16, Teams $29 per month (https://latenode.com/blog/make-com-pricing). Other articles quote different numbers; **not verified on make.com**.
- Teams plan adds team roles and shared templates (https://www.jetadmin.io/blog/make-pricing/). Not verified on make.com.

### n8n cloud (https://n8n.io/pricing/)

| plan | price | executions | users | workflows | team features |
|---|---|---|---|---|---|
| Starter | 20€/mo billed annually | 2.5K executions "with unlimited steps" | unlimited | unlimited active | 1 shared project, project admins only, credential sharing, error workflows |
| Pro | 50€/mo billed annually | 10K | unlimited | unlimited active | 3 shared projects, admin roles, project editors, workflow history |
| Business | 667€/mo billed annually (self-hosted only) | 40K | unlimited | unlimited | 6 shared projects, SSO/LDAP, environments, Git |
| Enterprise | contact sales | custom | unlimited | unlimited | unlimited projects, project viewers, custom roles, log streaming |

- n8n counts a whole run as one execution: "only pay when a workflow runs from start to finish".
- Projects "group workflows and credentials, and assigns roles to users in each project". Members can use their own
  personal credentials in a team project without sharing them (https://docs.n8n.io/user-management/rbac/projects/).

### Activepieces cloud (https://www.activepieces.com/pricing)

| plan | price | credits | users | flows | team features |
|---|---|---|---|---|---|
| Free | $0 | 1,000/mo (resets daily) | up to 5 | unlimited | - |
| Plus | $20 flat | 10,000/mo | up to 5 | unlimited | bring your own AI keys |
| Team | $200 flat | 50,000/mo | 25 included | unlimited | unlimited projects, SSO, standard roles, global connections, email support |
| Ultimate | custom | sized | unlimited | unlimited | SCIM, custom roles, Git sync, audit logs, credit usage by project |

- "A run is one credit however many steps it has"; AI steps cost 2, 10 or 20 credits by model. Overage $0.007/credit.

### Lindy (https://www.lindy.ai/pricing)

- Free: $50 in credits for 7 days. Team: from $49.99/mo for 5,000 credits, and "every active user in your workspace is
  billed, from $49.99 a month for 5,000 credits each". Credits pool across the team; admins can set credit allocations per seat.
- Anything with outside impact "waits for approval" (FAQ). Enterprise adds SSO, SCIM, audit logs.
- Lindy is an AI assistant priced per seat, not a run-metered workflow tool, so it is a weaker comparison.

### Relay (https://relay.app/pricing)

- "Relay.app shut down in September 2026. All accounts, workflows, and run history have been permanently deleted."
  No current pricing exists. **Remove Relay from competitor lists.**

## 2. What the comparison shows

1. **Nobody limits workflows on paid plans.** Zapier ("Unlimited Zaps"), n8n ("Max active workflows: Unlimited"),
   Activepieces ("Flows: Unlimited") all say so. Only free plans limit: Zapier free is two-step only; Make free has
   2 active scenarios (secondary source).
2. **The meter differs.** Zapier counts every action step. n8n and Activepieces count a whole run once. FansaChat
   counts runs, like n8n and Activepieces, which is simpler for buyers.
3. **Our runs per dollar are in the same range.** Starter $15 / 2,000 runs vs n8n Starter 20€ / 2,500 executions.
   Pro $45 / 10,000 runs vs n8n Pro 50€ / 10K and Activepieces Plus $20 / 10,000 credits. Activepieces is cheapest per
   run; we are close to n8n.
4. **Team features are where we are thin.** Every competitor team tier names concrete features: shared connections
   (Zapier, Activepieces "global connections", n8n credential sharing), roles (all), projects or folders (all), SSO
   (Zapier Team, Activepieces Team). Our plan text names none of these.
5. **Seat counts:** Zapier Team 25 seats, Activepieces Team 25 users, n8n unlimited users. Our Team cap of 10 is low
   next to these, but the brief's "2-10 people" target buyer (`results/TEAMS.md`, 10-person agency) fits it.

## 3. Recommendations (founder decides)

### Starter ($15) and Pro ($45): should they limit active workflows, steps or apps?

**Active workflows: a soft cap is fine, but set it high.**
- Our data: the 14 Starter people have 73 tasks marked major or minor (about 5 each); the 14 Pro people have 91 (about
  6.5 each) (`results/BUYERS.md`, summary table). Real users need a handful of live workflows, not hundreds.
- Proposal: **Starter 20 active workflows, Pro 100 active**, drafts unlimited. That is roughly 4x and 15x what our
  personas need, so almost nobody hits it, but it stops one cheap account from running a large agency's workload.
- Risk: competitors say "unlimited" on every paid plan, so a cap reads worse than it is. If the run quota already
  protects cost, keep "unlimited" and limit nothing. Runs are the real cost driver; workflow count is mostly marketing.
  **My lean: keep workflows unlimited, cap runs and AI builds only.**

**Steps per workflow: one generous safety limit on all plans, not a tier lever.**
- Zapier uses one limit for everyone: 100 steps per Zap. Nobody uses steps to separate paid tiers.
- Proposal: **50 steps per workflow on every plan** (our persona requests use 2-3 apps each; see
  `results/PERSONA_REQUESTS.md`). It protects the AI builder and the run engine from runaway flows.

**Apps per workflow: do not limit.** No competitor page limits it, and it would break normal 3-app workflows.

**Do limit what costs us money:** AI builds (already limited) and AI steps at run time. Activepieces charges 2-20
credits per AI step by model; we should count an AI step as more than one run, or include an AI-step quota, before
heavy AI users eat the margin.

### Team ($149): what it needs

1. **Departments (folders or projects)** with members. Every competitor has one: Zapier folders with folder
   permissions, n8n projects, Activepieces projects.
2. **Shared vs personal connections.** Default: a connection is personal; the owner can share it with a department.
   n8n's model is the clearest public example: personal credentials usable in a team project without sharing them
   (https://docs.n8n.io/user-management/rbac/projects/).
3. **Three roles:** admin (billing, members), editor (build and turn on), viewer (see runs). n8n has admin, editor and
   viewer roles; Activepieces Team has "standard roles"; Zapier Team has owner access.
4. **Failed-run alerts** to the workflow owner and the department admin, by email and in-app, with a one-click replay.
   Zapier paid plans have "Custom error notifications" and "Alerts"; n8n has "Error workflows" on every plan.
5. **Fix the seat text:** "2-10 people" or "unlimited users", not both.

### Scale ($299): separate department workspaces?

**Yes, but as departments inside one account, not separate accounts.** Brightpath (`results/TEAMS.md`) has six
departments of 5-10 people. They need: own workflows and connections per department, one shared run pool with
**usage by department** (Activepieces Ultimate lists "Credit usage by project"), and an owner who sees everything.
Fully separate workspaces (Zapier lists "Workspaces" only on Enterprise) add billing and support work we do not need
yet. Add SSO next, since Zapier and Activepieces include it at their team tier.

## 4. What is missing on each tier (versus competitors)

| tier | missing (not in our plan text) | who has it |
|---|---|---|
| Starter | run history with step input/output; failed-run email; replay | Activepieces runs view (https://www.activepieces.com/docs/flows/debugging-runs); Zapier held runs and replay (https://help.zapier.com/hc/en-us/articles/8496181445261) |
| Pro | version history; bring-your-own AI key; what happens at the run limit (pause, hold, or overage) | n8n Pro workflow history; Activepieces Plus BYO AI keys and $0.007 overage |
| Team | departments, shared/personal connections, roles, failed-run alerts, SSO | Zapier Team, n8n Pro, Activepieces Team (URLs above) |
| Scale | usage by department, audit log, SSO, admin view across departments | Activepieces Ultimate, Zapier Enterprise, n8n Enterprise |
| All | clear rule for what counts as a run when AI steps are inside | Activepieces publishes AI credit costs; Zapier publishes task usage rates (https://zapier.com/pricing/rates) |

I could not check FansaChat's actual product here (no product code in this repo), so "missing" means "not stated in
our plan descriptions". The founder should cross out anything the app already has.
