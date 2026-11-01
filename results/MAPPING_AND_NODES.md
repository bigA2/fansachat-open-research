# Field mapping and nodes: Zapier, n8n, Activepieces, and what FansaChat needs

Sources: crawled copies in `results/sources/mapping/` and `results/sources/nodes/`. One page did not load:
https://help.zapier.com/hc/en-us/articles/8495961813389 returns "The page you were looking for doesn't exist"
(`sources/mapping/02.md`): **source not reached**.

## 1. Zapier field mapping

Source: https://help.zapier.com/hc/en-us/articles/8496343026701 ("Send data between steps by mapping fields").

- **What it is:** "Field mapping is a way to connect two fields so data flows between them. When you map fields, your
  Zap will automatically take the output of the first field and enter it as an input in the second field."
- **How you do it:** click the plus icon in a field of an action step, then pick one or more fields from an earlier
  step in a dropdown. A mapped field shows as a "colored pill". Typed text is a static value used on every run.
- **Where the fields come from:** "The fields available for mapping come from the sample or test data in previous
  steps." If a field is missing, you re-test the trigger or use a recent run as the test record.
- **Enhanced field mapping:** shows data as a tree (arrays, objects, nested lists), shows the data type of each field,
  and lets you map a single value, a whole array or a whole object. "Get all values" maps line items.
- **Whole step output:** "All steps return the entire output of a step in a single value via the _Step Output_ field",
  useful for AI steps.
- **Limits:** you can only map from earlier steps to later steps; if you change the app or app version of a step, you
  must re-map, and outdated mappings show "a yellow warning indicator"; an errored step produces no output.
- Each action step can have up to 1,000 fields (https://help.zapier.com/hc/en-us/articles/8496181445261).

## 2. n8n nodes, the node panel and the data-mapping UI (ideas only)

n8n is under the **Sustainable Use License**: "You may use or modify the software only for your own internal business
purposes or for non-commercial or personal use" (https://raw.githubusercontent.com/n8n-io/n8n/master/LICENSE.md). Files
with ".ee." need an n8n Enterprise License. **We copy no code, styling or assets.** Only the general ideas below, which
are common to many tools, are described.

- **Node:** "Nodes are the key building blocks of a workflow." They start the workflow, fetch and send data, and process
  data (https://docs.n8n.io/workflows/components/nodes/). Each node has operations of two kinds: triggers and actions
  (https://docs.n8n.io/integrations/builtin/node-types/). "Core nodes" give logic, scheduling and generic API calls.
- **Node panel:** "Select Add first step. n8n opens the nodes panel, where you can search or browse trigger nodes." Then
  you add more nodes with an Add node button (https://docs.n8n.io/workflows/components/nodes/).
- **Hover controls on a node:** execute step, deactivate, delete, and a context menu (rename, pin, copy, duplicate, ...).
- **Per-node settings:** "Retry On Fail", and "On Error" with "Stop Workflow", "Continue", or "Continue (using error
  output)" (same page).
- **Data mapping:** "Data mapping means referencing data from previous nodes." You map either with the expressions
  editor or "by dragging and dropping data from the INPUT pane into node parameters. This generates the expression for
  you" (https://docs.n8n.io/data/data-mapping/data-mapping-ui/). Referencing does not change the data
  (https://docs.n8n.io/data/data-mapping/).
- **Debugging:** load a past (failed) execution's data into the editor, fix the workflow and re-run with that data
  (https://docs.n8n.io/workflows/executions/debug/).

## 3. How Activepieces passes data (our engine)

Source: https://www.activepieces.com/docs/flows/passing-data.

- A flow is a trigger plus action steps. "Data flows from parent steps to the children (Children steps have access to
  the output data of the parent steps)." Some triggers produce no data, like schedules.
- **Data selector panel:** place the cursor in any input and a panel "shows the accessible steps and their data"; click
  an item to insert it.
- **Testing:** "we require you to test each step you add before moving to the next step", so later steps can see real
  sample data.
- **Reference syntax (exact, from the docs):** `{{step_name['output']['path']['to']['property']}}`. Right-click a step
  and "Copy reference" gives `{{step_name['output']}}`. The brief writes this as `{{step.field}}`; the docs use the
  bracket form above, so our generator should emit that form (or check which forms the engine version we run accepts).
- Dropdown inputs can be switched to "dynamic" to accept data from earlier steps. Files pass by reference, not copied.

## 4. What FansaChat lacks

Our step JSON today is `{id, type: trigger|action|router|ai|wait, app, label, after, branch}`. It says **which** app runs
and in **what order**, but:

1. **No action or trigger name** (for example Gmail "send email" vs "create draft"). Without it there are no input fields.
2. **No input values.** Nothing says "To = trigger's sender, Subject = ...".
3. **No references between steps**, so an action cannot use data from the trigger. In practice every workflow needs
   this. All 60 requests in `results/PERSONA_REQUESTS.md` use something from the trigger in a later step (my reading:
   "save to Dropbox" needs the attachment, "alert Slack" needs the text). 12 of the 60 also have a condition on a value,
   such as "drops 20%" (#13) or "payment late" (#49), so the router needs a field to test.
4. **No sample data** to show the user what each step will receive.
5. **No field view in the UI**, so a user cannot check or fix what the AI picked.

## 5. Smallest design that adds it

Add three optional keys per step. Old workflows stay valid.

```json
{
  "id": "s2", "type": "action", "app": "gmail", "label": "Email the client",
  "after": "s1", "branch": null,
  "action": "send_email",
  "inputs": {
    "to":      "{{trigger['output']['from']}}",
    "subject": "Re: {{trigger['output']['subject']}}",
    "body":    "{{s1['output']['text']}}"
  },
  "needs": ["trigger", "s1"]
}
```

- `action`: the piece's action or trigger name, chosen by the builder from that app's real list.
- `inputs`: one value per required field: plain text, or a reference in the Activepieces form. The builder fills
  required fields only; optional ones stay empty.
- `needs`: which earlier steps the inputs use. A check rejects a reference to a later step or a missing step (the same
  rule Zapier states: map only from earlier steps).
- **Router conditions** use the same reference form: `{"if": "{{trigger['output']['amount']}}", "op": ">", "value": 500}`.

UI, smallest version: tap a step to open a side panel with its fields. Mapped values show as pills
("Trigger > From"). Tapping a pill shows the earlier steps' fields as a tree (the idea Zapier and Activepieces both
describe). Red dot on a step with a required field still empty. No drag-and-drop in the first version.

Build order: (1) `action` + `inputs` in the generator, validated against the piece's schema; (2) a check that blocks
turning on a workflow with empty required fields; (3) the side panel; (4) sample data from a test run.

## 6. How much it helps

I have **no measured numbers** and will not guess one. What we can say:

- Without `inputs`, a built workflow cannot run without a person filling every field in the engine UI. So today the
  "one sentence -> working workflow" promise depends on this.
- **How to measure:** take the 60 persona requests and the top 30 automations in `results/BUYERS.md`. Build each with
  the current generator and with the new one. Count: (a) workflows that pass a test run with no human edits,
  (b) required fields left empty, (c) wrong references (field does not exist in the earlier step's output). Report
  both versions side by side.
