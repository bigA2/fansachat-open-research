# Research summary, 1 Nov 2026

Public data only. Every claim about another product is sourced in the linked files.

## Top findings

1. **O*NET data is current.** We use 31.0, the newest release (August 2026). Nothing newer exists to download.
   -> [ONET_RECENCY.md](ONET_RECENCY.md)
2. **About a quarter of real tasks are a strong fit; many more are partial.** Of 804 person-tasks (88 people), major /
   minor fits are Starter 14% / 37%, Pro 22% / 42%, Team 10% / 48%, Scale 26% / 43%. The most common automations are
   scheduled reports, AI first drafts, approvals, keeping records up to date, meeting notes, and complaints to
   tickets. Laya scores often disagree with a human reading, so use them as a hint only.
   -> [BUYERS.md](BUYERS.md)
3. **No competitor limits workflows on paid plans** (Zapier, n8n, Activepieces all say unlimited). Our runs per dollar
   are close to n8n's. **Our team tiers name no team features**, while every competitor names shared connections,
   roles and projects/folders. Relay.app shut down in September 2026. Make's pages could not be reached.
   -> [TIER_AUDIT.md](TIER_AUDIT.md)
4. **The biggest product gap is field mapping.** Our step JSON has no action name, no input values and no references
   between steps, so a built workflow cannot run without manual setup. Every one of the 60 persona requests needs
   data from the trigger.
   -> [MAPPING_AND_NODES.md](MAPPING_AND_NODES.md)
5. **Competitors notify by email, not with live toasts.** Zapier and Activepieces show status per step inside a run
   view. No source shows status on hover, so this would be our own feature.
   -> [NOTIFICATIONS.md](NOTIFICATIONS.md)
6. **"Vertex AI Agent Builder" is now Gemini Enterprise Agent Platform**, and Google Application Integration already
   offers "Gemini to build integrations" from plain language. It is built for technical teams on Google Cloud.
   -> [VERTEX.md](VERTEX.md)
7. **Injection risks are mapped to OWASP 2025 with defences.** The 120-case test file was **not produced** in this
   run (see the file for why). -> [INJECTION.md](INJECTION.md)
8. **Superpowers is MIT; andrej-karpathy-skills says "MIT" in its README but has no LICENSE file.** Both teach think
   first, ask when unclear, plan, verify. Neither publishes results, so we need our own A/B test.
   -> [SUPERPOWERS.md](SUPERPOWERS.md)

## Recommendations (founder decides)

1. **Build field mapping first:** add `action`, `inputs` (Activepieces `{{step['output']...}}` references) and `needs`
   to the step JSON, plus a check that blocks turning on a workflow with empty required fields.
2. **Keep workflows unlimited; meter runs and AI.** Add one safety limit of 50 steps per workflow on all plans. Count
   AI steps above one run (Activepieces charges 2-20 credits per AI step).
3. **Team ($149):** departments, personal vs shared connections, admin/editor/viewer roles, failed-run alerts. Fix
   the conflict between "2-10 people" and "unlimited users".
4. **Scale ($299):** departments inside one account with usage per department and an owner view; SSO next.
5. **Notifications:** toast within seconds of a run, status card on hover or tap of an app dot, failure email by
   default, warning before auto-pause, usage alerts at 80% and 100%.
6. **Safety:** schema-check builder output, least privilege per workflow, approval for risky actions, input
   normalisation, AI spend caps. Build the injection eval set through a reviewed red-team process.
7. **Prompt method:** A/B test a short "plan, ask only when unclear, verify" block on the 60 persona requests and the
   top 30 automations before adopting it.

## Sources not reached

make.com (pricing, teams, scenario settings, retry docs); two Zapier team help pages and one Zapier mapping page
(they return "page doesn't exist"); the O*NET publication schedule; a LICENSE file in andrej-karpathy-skills (404).
