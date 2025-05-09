## Chapter 5 – “Patterns to Avoid Like Volcanoes”

### 🧠 Primary Concept

**Anti-patterns kill quietly, then all at once.** Observability debt isn’t abstract—it compounds into blind spots that blow up under pressure.

______________________________________________________________________

### 🧩 Key Terms Introduced

- Ownerless metrics
- Runbook gap
- Log omission
- Success vs. uptime
- Observability bias (“blame the network” syndrome)

______________________________________________________________________

### 📊 Teaching Objective

Learners should walk away understanding:

- What the most common observability anti-patterns are in real systems
- How each one delays resolution or worsens user experience
- How to design around or prevent these failures

______________________________________________________________________

### 🧱 Banking Anchor

- ATM outage strikes across a region
- Dashboards give no answers
- False confidence in uptime metrics masks system unavailability

______________________________________________________________________

## 🧪 Teaching Sequences (Per Panel)

### Panel 1 – Dashboard Chaos

- **Scene**: Wanjiru stares at 24 unlabeled panels
- **Teaching Moment**: More panels ≠ better observability
- **Widget**: Reflection — “Which dashboard do you trust least—and why?”
- **Artifact**: Screenshot of cluttered Geneos dashboard

### Panel 2 – The Blame Begins

- **Scene**: Daniel says "network again"; Njeri glares
- **Teaching Moment**: Bias replaces investigation when data is ambiguous
- **Widget**: Hector Quote — “Assumptions are the first thing to fail.”
- **Artifact**: Infra, DB, and app graphs showing no real spike

### Panel 3 – The Five Sins

- **Scene**: Hector unveils a whiteboard of five sins
- **Teaching Moment**: These are the recurring observability killers
- **Widget**: Diagram — Five Observability Sins table
- **Artifact**: Labeled whiteboard with sins illustrated by icon

### Panel 4 – Sin #1: Ownerless Metrics

- **Scene**: Clara asks who owns `latency_avg_all`. Silence.
- **Teaching Moment**: Unowned metrics are unactionable
- **Widget**: Debug Pattern — Metric with No Owner
- **Artifact**: Metric graph + zero ownership doc or alert mapping

### Panel 5 – Sin #2: Orphaned Alerts

- **Scene**: Juana finds alert with 404 runbook
- **Teaching Moment**: Alert without action = useless noise
- **Widget**: Try This — Audit alert-to-runbook links
- **Artifact**: Screenshot of broken runbook URL + fix example

### Panel 6 – Sin #3: Logs That Lie

- **Scene**: Katherine shows useless 500 error: no trace, no ID
- **Teaching Moment**: Omission is a form of telemetry failure
- **Widget**: Debug Pattern — Incomplete Log Entry
- **Artifact**: Log before/after with missing/requested fields

### Panel 7 – Sin #4: Uptime Without Success

- **Scene**: Aisha compares uptime = 100%, but zero ATM transactions
- **Teaching Moment**: Service ≠ value unless users succeed
- **Widget**: Reflection — “Which metrics make you feel good but tell you nothing?”
- **Artifact**: Split graph: uptime vs. actual transaction rate

### Panel 8 – Sin #5: “It’s Always the Network” Syndrome

- **Scene**: Njeri shows 90% of network-blamed incidents were app bugs
- **Teaching Moment**: Historical data debunks lazy thinking
- **Widget**: Incident Flashback — “Blame Drift” example
- **Artifact**: Table showing top misattributed incident types

### Panel 9 – ATM Outage Replay

- **Scene**: Hector walks team through root cause flow
- **Teaching Moment**: Connect all five sins to this incident timeline
- **Widget**: Diagram — Failure Flow: What Was Missed and When
- **Artifact**: Mermaid diagram timeline with failure annotations

### Panel 10 – Lesson Locked In

- **Scene**: Hector warns of audits, hands off action items
- **Teaching Moment**: Design observability as compliance and clarity
- **Widget**: Hector Quote — “Volcanoes don’t care if your metrics are clean.”
- **Artifact**: Observability checklist written on whiteboard

______________________________________________________________________

## 👤 Character Learning Beat

- **Wanjiru**: Overwhelmed by signal clutter
- **Daniel**: Learns blame isn’t diagnosis
- **Njeri**: Vindicates network but demands better data
- **Clara**: Drives metric ownership clarity
- **Juana**: Advocates for actionable alerts
- **Aisha**: Brings customer-centric signal definition
- **Hector**: Pushes maturity and audit readiness

______________________________________________________________________

## 🧪 Mini Assessment Hook Summary

- `:::reflection` → What’s your most un-actionable metric?
- `:::debug pattern` → Metric with No Owner, Incomplete Log Entry
- `:::try this` → Build a runbook index by alert type
- `:::incident flashback` → Past incident misdiagnosed by false assumption

______________________________________________________________________

## 📋 Panel Beat-to-Concept Map

| Beat # | Panel Title | Teaching Goal |
| ------ | ----------------- | ------------------------------------------- |
| 1 | Dashboard Chaos | Visual overload hides signal |
| 2 | The Blame Begins | Bias wins without clear data |
| 3 | The Five Sins | Introduce recurring failure modes |
| 4 | Ownerless Metrics | No ownership = no action |
| 5 | Orphaned Alerts | Alerts must include how to act |
| 6 | Logs That Lie | Logs must say who/what/where |
| 7 | Uptime ≠ Success | Availability isn't usefulness |
| 8 | Blame the Network | Over-assigning root cause distorts learning |
| 9 | ATM Outage Replay | Map the sins onto one real-world failure |
| 10 | Lesson Locked In | Avoid the volcano—or answer to the auditors |
