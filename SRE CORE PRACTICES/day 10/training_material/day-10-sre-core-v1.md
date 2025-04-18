**Day 10. The Capstone.**  
You’ve taught them how to measure, how to monitor, how to observe, and how to respond.  
Now it’s time to let them try—not by guessing on a quiz, but by **facing a complete, complex incident**.  
This is the final synthesis: **a chaotic, realistic, multi-signal scenario** where everything they've learned is tested.

And of course, everyone’s here: Hector, Mina, Felix, and Asha—**the full SRE ensemble**—guiding, reacting, and pushing learners through their final test.

---

# 🧱 **Day 10: Capstone – Incident Simulation & Observability Deep Dive**

**Characters:**  
- Hector (commander)  
- Mina (triage)  
- Felix (metrics and SLOs)  
- Asha (logs, pipeline, trace correlation)  

**Vibe:** “This is your war room. Welcome to the chaos.”

---

## 🎯 Learning Objectives

### 🔍 Beginner
- Practice basic signal analysis across metrics, logs, and traces  
- Identify failure symptoms and correlate with user impact

### 🧩 Intermediate
- Build an incident timeline from multiple signals  
- Propose an SLO violation diagnosis using available data  
- Simulate communications and handoffs

### 💡 Advanced / SRE-Level
- Coordinate a full incident lifecycle  
- Prioritize mitigation over noise  
- Conduct a blameless postmortem with structured learnings and follow-up items

---

## 💥 Incident Scenario: **“The Black Friday Bottleneck”**

> 11:03 AM — Alert fires: `Checkout latency > 500ms`  
> 11:05 AM — Traces show delay in `tax-service`  
> 11:07 AM — Logs reveal retry storms from `frontend-service`  
> 11:10 AM — Prometheus shows cache evictions spiking  
> 11:13 AM — SLO budget hit 50% for the day  
> 11:15 AM — Customer support tickets begin to pile up  
> 11:16 AM — SRE team paged  
> 11:30 AM — Incident declared: SEV-1

---

## 🔬 Provided Assets (Simulation Bundle)

- **Metrics Dashboard** (PNG/Markdown table)
    - `request_duration_seconds_bucket{le="0.5"}` dropping  
    - `rate(5xx_errors_total[5m])` rising  
    - SLO burn rate chart: ~3x threshold

- **Trace Screenshot** (span 3 shows 1.2s delay)
    - `frontend-service` → `checkout-service` → `tax-service`  
    - `tax-service` span = bottleneck

- **Structured Logs** (sample lines)
```json
{"timestamp":"...","service":"frontend","status":500,"request_id":"abc123","trace_id":"xyz789","msg":"checkout failed"}
{"timestamp":"...","service":"tax-service","status":200,"duration":1230,"cache":"MISS"}
```

- **SLO Dashboard Snippet**
    - Target: 99.9% requests < 500ms
    - Budget left: 32 minutes
    - Consumed: 18 minutes in 90 minutes

---

## 🧪 Simulation Flow

Learners must complete:

### 🔹 Incident Timeline

| Time | Event | Signal | Action |
|------|-------|--------|--------|
| 11:03 | Alert fired | Metric | Notify IC |
| 11:05 | Trace span 3 shows latency | Trace | Identify tax-service as bottleneck |
| ...  | ... | ... | ... |

> 👩‍🏫 **Exercise:** Fill out timeline with 6–8 events and responsible roles.

---

### 🔹 SLO Violation Assessment

- Calculate % of failing requests  
- Determine burn rate  
- Estimate time to full budget depletion

---

### 🔹 Root Cause Discovery

📌 Using:
- Trace delays  
- Logs (`cache: MISS`)  
- Cache eviction metrics

Learners must conclude:
> “Tax-service degraded due to cache eviction and downstream cold responses under load. Retry storms created cascading latency.”

---

### 🔹 Action Items

Must include:
- Technical fix (e.g., cache capacity or load shedding)  
- Observability improvement (e.g., add `cache_status` as metric label)  
- Culture/process improvement (e.g., runbook for tax-service caching)

---

## 🛠 Capstone Artifacts (All Optional)

- Incident doc (template)  
- Postmortem doc (template)  
- PDF or Markdown submission with filled simulation exercise  
- Team debrief format (for workshops)

---

## 🕳️ Common Pitfalls (Capstone Edition)

- Focusing only on metrics and missing trace gaps  
- Blaming infra without evidence  
- Failure to identify **user impact** vs system anomaly  
- Getting lost in logs without correlation ID

---

## 📜 Final Commandments (Team Edition)

🗣️ *From Hector:* “Chaos is the real audit.”  
🗣️ *From Mina:* “If the trace breaks, so does the truth.”  
🗣️ *From Felix:* “A burned budget isn’t a failure. It’s a signal.”  
🗣️ *From Asha:* “You’ll always see more with less—if it’s structured right.”

---

## 🎓 Completion Reflection

> “You now know how to:
> - Observe across signals  
> - Correlate across systems  
> - Respond under pressure  
> - Design for failure  
> - Recover with clarity  
> - Learn as a team  
> …and teach others to do the same.”

---

## 📦 Day 10 Artifacts

- ✅ Capstone simulation materials:
    - Timeline shell
    - Logs, traces, metrics
    - Budget math
- ✅ Postmortem Template
- ✅ Final Reflection Prompt
- ✅ Team Retrospective Format

---

**You did it.**  
This is a complete, 10-day SRE Core Curriculum.  
Narrative-driven. Tool-agnostic. Simulation-first.  
Designed for realism, not checkbox learning.

Want help bundling this into:
- Markdown files for each day?  
- Mermaid → PNGs for Kroki?  
- A PDF export for internal curriculum docs?

Or do you want to talk **certification, capstone assessment, or leveling rubrics** next?

You’ve got a program here. A real one. Let’s package it right.