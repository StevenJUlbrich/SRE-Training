## Chapter 1 – “The Site Is Down” Isn’t a Root Cause

### 🧠 Primary Concept
**Observability ≠ Monitoring**
- Monitoring tells you what is happening.
- Observability helps you understand why it’s happening.

### 🧩 Key Terms Introduced
- Shallow metrics
- Dashboards vs telemetry
- Logs, metrics, traces (three pillars)
- False negatives
- Observability debt

### 📊 Teaching Objective
Learner should walk away understanding:
- Why dashboards alone can’t diagnose failures
- Why correlation is key (trace → log → metric)
- How observability enables cause, not just confirmation

### 🧱 Banking Anchor
- Payment processor fails silently
- Dashboards wired to replica DBs, not primaries
- Customers see “service unavailable” while SREs see green graphs

---

## 🧪 Teaching Sequence 1 – Observability vs Monitoring

### Teaching Moment (Concept Bridge)
- **Concept**: Monitoring answers “what happened?” Observability helps you ask “why?”
- **Banking Analogy**: Monitoring says "The ATM is online." Observability reveals that 87% of deposit attempts fail because of a locked table in the backend DB.

### Graphic Panel: “The Pager Screams”
- Pager blares at 2:57 AM.
- Dashboards show solid green.
- Slack channel lights up: "Transfers failing. No deposits landing."
- **Caption**: “The system says it’s fine. The users say otherwise.”

### Reflection Widget
```markdown
:::reflection
Have you ever investigated an incident where the dashboard was green—but the users were furious?
:::
```

### Tech + Artifact
- `curl` returns HTTP 500
- `kubectl logs deployment/payment-service | grep ERROR`
- Log line lacks `trace_id`
- Dashboards wired to read-replica only
- No alert triggered (because error rate tile not present)

### Call-to-Action Prompt
```markdown
:::try this
Identify a dashboard in your system that reports health based on replica nodes or unused probes. What failure would it miss?
:::
```

---

## 🧪 Teaching Sequence 2 – Missing Context is the Real Problem

### Teaching Moment
- **Concept**: Dashboards show health, not correctness.
- **Bridge**: Logs may show `ERROR`, but lack the who/when/where to investigate cause.

### Graphic Panel: “Juana’s Discovery”
- Juana reviews logs: 20 lines of WriteTimeoutException.
- Logs have timestamps, but no `trace_id`, no user context.
- **Caption**: “Nice. It broke, and it didn’t even tell us who it killed.”

### Widget: Debug Pattern
```markdown
:::debug pattern
**Pattern Name:** Green Wall Fallacy

**Description:** Dashboards wired to replicas report healthy metrics even when primaries fail.

**Example Fix:** Point dashboards to live traffic + add error stream overlays by service.
:::
```

### Tech + Artifact
- Log format missing context keys
- Span-based tracing missing from backend
- Placeholder `mermaid` diagram showing trace gap

---

## 🧪 Teaching Sequence 3 – Dashboard ≠ Reality

### Teaching Moment
- **Concept**: Dashboards measure liveness, not customer trust.
- **Bridge**: Katherine interprets "CPU looks fine" as "the system is fine."

### Graphic Panel: “Dashboard Dissonance”
- Wanjiru shares her screen with the team.
- All tiles green. Katherine frowns: “Everything looks fine… right?”
- **Caption**: “The deeper the green, the louder the lie.”

### Widget: Hector Quote
```markdown
:::hector quote
Green means the system’s lying. Now let’s teach it to confess.
:::
```

### Tech + Artifact
- Screenshot of Geneos dashboard with no error metrics
- Missing error rate overlay on key service
- CPU and memory within normal ranges

### Call-to-Action
```markdown
:::try this
Look at your own dashboards. Are any of them green by default? What signals are being excluded?
:::
```

---

## 🧪 Teaching Sequence 4 – The Three Pillars Matter

### Teaching Moment
- **Concept**: Observability = Logs + Metrics + Traces
- **Bridge**: No single pillar can carry the diagnostic load alone.

### Graphic Panel: “Hector’s Diagram”
- Hector sketches the observability Venn diagram on a whiteboard.
- He overlays the service graph and shows where each tool breaks down.
- **Caption**: “Logs tell the story. Metrics show the pattern. Traces reveal the path.”

### Widget: Diagram
```markdown
:::diagram
```mermaid
vennDiagram
    title Three Pillars of Observability
    A[Logs] B[Metrics] C[Traces]
    A & B & C: True Root Cause Detection
```
:::
```

### Tech + Artifact
- Example span entry with user ID and DB lock timestamp
- Log with injected trace ID post-hotfix

---

## 🧪 Teaching Sequence 5 – Making the System Speak

### Teaching Moment
- **Concept**: Observability must be retrofit when missing—retro-instrumentation is a recovery skill.
- **Bridge**: You don't always get a perfect pipeline—you build while burning.

### Graphic Panel: “Trace Synthesis”
- Juana redeploys a sidecar to add trace IDs to logs.
- Wanjiru sees the trace ID appear in the error logs for the first time.
- **Caption**: “A log without a trace is a rumor. A trace makes it evidence.”

### Tech + Artifact
- Fluent Bit config snippet (trace_id injection)
- Resulting log line with full context

### Widget: Try This
```markdown
:::try this
Inject a `trace_id` field into one of your existing log formats using your logging pipeline—can you search it by trace yet?
:::
```

---

## 👤 Character Learning Beat
- **Wanjiru** panics: tools show green, but customer complaints are real.
- **Katherine** focuses on CPU/memory: “Should we fail over to a bigger node?”
- **Juana**: reads vague logs, frustrated by lack of trace IDs.
- **Hector**: teaches the “green wall fallacy,” explains how telemetry should confess, not conceal.

---

## 🧪 Mini Assessment Hook Summary
- `:::reflection` → What metric or dashboard do you trust too easily?
- `:::debug pattern` → Green Wall Fallacy
- `:::try this` → Find a log line in your system that lacks correlation ID

---

## 📋 Panel Beat-to-Concept Map

| Beat # | Panel Title          | Teaching Goal                                  |
| ------ | -------------------- | ---------------------------------------------- |
| 1      | Pager Screams        | Monitoring ≠ experience                        |
| 2      | Dashboard Dissonance | Wanjiru learns that green doesn't mean healthy |
| 3      | Juana’s Discovery    | Logs without trace context are dead ends       |
| 4      | Hector’s Diagram     | Three pillars: logs, metrics, traces           |
| 5      | Trace Synthesis      | A visible fix, post-instrumentation            |
| 6      | Reflection Panel     | Learners articulate observability gaps         |
| 7      | Lesson Locked In     | Correlated telemetry restores control          |

