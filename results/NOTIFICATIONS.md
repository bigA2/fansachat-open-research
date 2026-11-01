# Run notifications and status: Zapier, Make, n8n, and what FansaChat should do

Sources: `results/sources/notifications/`, `results/autofix/`, plus web search where the crawl failed.
Not reached: https://www.make.com/en/help/scenarios/scenario-settings (crawl failed, `sources/notifications/04.md`)
and https://www.make.com/en/help/errors/automatic-retry-of-incomplete-executions (redirected to the Make help home
page, `autofix/06.md`). make.com is blocked by this session's network, so Make facts come from search results.

## Short answer

- **Notifications:** yes, all three tell you about **failed** runs, mainly **by email** (Zapier, Make) or through a
  workflow you build yourself (n8n). None of the sources describes a live in-app toast for each run.
- **Status on hover:** **not found in any source.** Zapier and Activepieces show run status **per step** when you
  open a run; n8n shows **controls** when you hover a node (run, deactivate, delete), not run status. A hover status on
  an app dot would be our own idea, not a copy.

## Zapier

- **Run list with status:** "Each Zap run in the list displays the Zap run status to confirm whether your Zap ran
  successfully." You can filter by date, Zap name, apps, folder, owner and status
  (https://help.zapier.com/hc/en-us/articles/8496291148685).
- **Status per step in the editor:** pick a run in the editor sidebar and "The editor displays the Zap run status for
  each step in the workflow"; each step shows a timestamp and the data it received and sent (same page).
- **Statuses named in the docs:** filtered, held, stopped, success, playing, waiting (same page); errored, and
  Stopped/Handled for error handlers (https://help.zapier.com/hc/en-us/articles/22495436062605).
- **Error emails:** "When errors occur in your Zaps, Zapier will send notifications to your Zapier account email
  address by default", and you can change how often, for all Zaps or per app
  (https://help.zapier.com/hc/en-us/articles/8496277613325). Per-Zap custom error notifications:
  https://help.zapier.com/hc/en-us/articles/15666606859661. "Alerts" is listed as new on paid plans
  (https://zapier.com/pricing; announcement https://help.zapier.com/hc/en-us/articles/29206590194445).
- **Error handler runs send no email:** "Zapier will not send any error notification emails when an error handler
  runs" (https://help.zapier.com/hc/en-us/articles/22495436062605).
- **Auto turn-off:** "Your Zap will automatically turn off if 95% of its runs result in errors in the last 7 days."
  Team plans get an email to the account owner and a 24-hour grace period, Enterprise 72 hours
  (https://help.zapier.com/hc/en-us/articles/8496037690637).
- **In-editor notices:** if an app has an outage, "a notification will appear in the affected step"; a Status
  section in the sidebar lists issues that block publishing (same page).
- **Task limit:** Zapier "sends email notifications as you approach and reach your limit"
  (https://help.zapier.com/hc/en-us/articles/8496181445261).
- **Replay:** a "notification window will open to show that the Zap run is replaying", where you can monitor the
  replay job (https://help.zapier.com/hc/en-us/articles/8496241726989). This is the only in-app popup described.

## Make (from web search; make.com not reached directly)

- Unhandled errors send an email; a scenario that fails on several runs in a row has its schedule turned off, with
  another notice (https://www.make.com/en/help/errors/introduction-to-errors-and-warnings-in-make, as summarised by
  search).
- Warnings (for example when "store incomplete executions" is on) show as a yellow caution sign on the module and do
  not count as consecutive errors (same page, via search).
- Not verified: exact email settings and any hover behaviour.

## n8n

- **Error workflow:** "For each workflow, you can set an error workflow in Workflow Settings. It runs if an execution
  fails. This means you can, for example, send email or Slack alerts when a workflow execution errors." It starts with
  an Error Trigger that receives the execution id, URL and error message
  (https://docs.n8n.io/flow-logic/error-handling/).
- **Executions list** per workflow or across all workflows; failed runs can be loaded into the editor with
  "Debug in editor" (https://docs.n8n.io/workflows/executions/debug/).
- **Hover on a node** shows controls: execute step, deactivate, delete, context menu
  (https://docs.n8n.io/workflows/components/nodes/).
- So n8n has no built-in failure email in these pages; the user builds the alert.

## Activepieces (our engine)

- Runs list in the dashboard; open a run to see "the builder in a view-only mode, each step will show succeeded or
  failed", and each step's input and output (https://www.activepieces.com/docs/flows/debugging-runs).

## What FansaChat should do

1. **Toast within seconds of a run finishing** while the user is in the app: "Invoice email sent" (green) or
   "Failed at Gmail: not connected. Fix" (red). One toast per workflow at a time; group bursts ("12 runs, 1 failed").
   Only failures stay until closed. This goes beyond what the sources show for Zapier, Make and n8n (email-first).
2. **Status on hovering (or tapping, on phones) an app dot:** last run time, result, and for a failure the step's
   error in plain words plus a "Retry" button. Colour the dot: green = last run ok, red = failed, grey = not run yet.
   Keep the full input/output in the run view (like Zapier and Activepieces), not in the hover card.
3. **Failure email by default,** with frequency choices (immediately / hourly summary / off), the same idea as Zapier's
   notification settings. On Team and Scale, also email the department admin.
4. **Warn before turning a workflow off.** If we auto-pause after repeated failures, send the warning first and give a
   grace period (Zapier: 24 hours on Team).
5. **Usage alerts** at 80% and 100% of runs and AI builds, like Zapier's task-limit emails.
6. **Measure it:** log time from run end to toast shown; target a few seconds. Track how many failed runs get a retry
   or fix within a day before and after the change.
