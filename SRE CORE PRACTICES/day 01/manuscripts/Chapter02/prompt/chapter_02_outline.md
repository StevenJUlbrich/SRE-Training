## Chapter 2 – “The Problem Isn’t Always the Problem”

### 🧠 Primary Concept

**Telemetry isn’t automatic—it's intentional.** If you don’t instrument the question, you won’t log the answer.

______________________________________________________________________

### 🧩 Key Terms Introduced

- Trace ID
- Context propagation
- Config-based observability regression
- Span / service graph
- Observability contract

______________________________________________________________________

### 📊 Teaching Objective

Learner should walk away understanding:

- That observability can regress quietly
- That “stable metrics” can mislead without context
- That distributed traces must be actively maintained

______________________________________________________________________

### 🧱 Banking Anchor

- International wire transfers silently fail
- Root cause: tracing disabled by config push
- Dashboards show green, but customers never see confirmations

______________________________________________________________________

## 🧪 Teaching Sequence 1 – The Untraceable Outage

### Teaching Moment

- **Concept**: Failure without traceability is indistinguishable from magic
- **Context**: Wanjiru and Katherine are looking at clean metrics; users are screaming

### Graphic Panel: “The Mystery Crash”

- Agent call transcript + green dashboard + `curl` returns 200 but no confirmation
- No trace ID in logs

### Widget: Hector Alavaz Quote

```markdown
:::Hector Alavaz quote
You didn’t build telemetry—you built denial. And now it’s trying to teach you something.
:::
```

### Artifact

- `curl -v` + logs with no trace ID

______________________________________________________________________

## 🧪 Teaching Sequence 2 – Regression by Config

### Teaching Moment

- **Concept**: Observability is a feature; config can kill it
- **Context**: A developer unchecked `enableTracing=true`

### Graphic Panel: “What They Missed”

- Flashback: diff of config file before/after

### Widget: Incident Flashback

```markdown
:::incident flashback
Dev toggled `enableTracing=false` for performance tests and forgot to re-enable it before merging to prod.
:::
```

### Artifact

- Git diff of config file
- Commit message: “minor perf fix”

______________________________________________________________________

## 🧪 Teaching Sequence 3 – Blame Without Visibility

### Teaching Moment

- **Concept**: If no one can see the root cause, everyone gets blamed
- **Context**: Ops blames dev, dev blames infra

### Graphic Panel: “The Blame Game Begins”

- Each team points at the other’s “green” graphs

### Widget: Reflection

```markdown
:::reflection
Who gets blamed first when your observability fails? Who should?
:::
```

### Artifact

- Screenshot of multiple dashboards with no useful correlation

______________________________________________________________________

## 🧪 Teaching Sequence 4 – Hector Alavaz’s Debrief

### Teaching Moment

- **Concept**: Traces reveal *sequence*, not just state
- **Context**: Juana overlays missing spans; team sees the actual outage path

### Graphic Panel: “The Corrected View”

- Before/after span graph

### Widget: Debug Pattern

```markdown
:::debug pattern
**Pattern Name:** Missing Span Syndrome
**Description:** Logs and metrics show failure, but lack the request path context.
**Example Fix:** Inject trace context via middleware, and log trace ID at every hop.
:::
```

### Artifact

- Before/after trace tree diagram

______________________________________________________________________

## 👤 Character Learning Beat

- **Wanjiru**: struggles to explain the failure without traces
- **Katherine**: trusts CPU/memory; learns observability regression is a risk
- **Juana**: shows how it *should’ve* worked
- **Hector Alavaz**: defines tracing as the postmortem you can run live

______________________________________________________________________

## 🧪 Mini Assessment Hook Summary

- `:::reflection` → Who gets blamed when traces vanish?
- `:::debug pattern` → Missing Span Syndrome
- `:::try this` → Add a trace ID to one log line and connect it to a span

______________________________________________________________________

## 📋 Panel Beat-to-Concept Map

| Beat # | Panel Title             | Teaching Goal                                    |
| ------ | ----------------------- | ------------------------------------------------ |
| 1      | The Mystery Crash       | No visibility despite user pain                  |
| 2      | Dashboard Deceit, Pt II | Misleading confidence via metrics                |
| 3      | The Missing Trace       | Traces missing = no request context              |
| 4      | What They Missed        | Dev config regression kills telemetry            |
| 5      | The Blame Game Begins   | Absence of trace breeds finger-pointing          |
| 6      | Hector Alavaz Steps In  | Observability is a preparation discipline        |
| 7      | The Corrected View      | Juana restores trace view for clarity            |
| 8      | Team Realization        | Learners own the failure                         |
| 9      | Closing Shot            | Hector Alavaz summarizes: telemetry must confess |
