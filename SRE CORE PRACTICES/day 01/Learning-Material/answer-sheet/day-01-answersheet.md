# 📘 Day 1 Observability Learning Quiz – Answer Sheet


## Answer 1: [Three Pillars Overview]

🔍 Beginner | Multiple Choice

**Question:** Which of the following best describes the Three Pillars of Observability?

A. Debugging, Logging, and Uptime\
B. Metrics, Logs, and Traces\
C. Alerts, Incidents, and Postmortems\
D. Dashboards, Reports, and Alarms

**Correct Answer:** B

**Explanation:** The Three Pillars—metrics, logs, and traces—offer complementary views of system behavior. Metrics track performance, logs show events and errors, and traces follow request journeys. Together, they support effective detection, investigation, and resolution.

**Why others are wrong:**
- **A:** Made-up trio with a buzzword energy. Uptime is an outcome, not a pillar.
- **C:** Incident response terms, not telemetry sources.
- **D:** Those are tools layered *on top* of the pillars.

---

## Answer 2: [Metrics Insight]

🔍 Beginner | True/False

**Question:** Metrics can help identify performance trends over time and are often visualized in dashboards.

A. True\
B. False

**Correct Answer:** A

**Explanation:** Metrics are numeric values collected over time. They're essential for trend analysis (like response time over the past week) and alerting (e.g., when CPU > 90%). These are usually shown in dashboards like Grafana or DataDog.

**Why B is wrong:** Metrics aren’t just passive data—they’re how you catch fire *before* the building burns down.

---

## Answer 3: [Trace Utility]

🔍 Beginner | Multiple Choice

**Question:** What is the primary purpose of a **trace** in observability?

A. Show numeric trends of system health\
B. Highlight configuration errors in logs\
C. Visualize the path and timing of requests across services\
D. Trigger CPU alerts when latency spikes

**Correct Answer:** C

**Explanation:** Traces show the lifecycle of a request as it moves through multiple systems, which helps you figure out where latency or errors occur.

**Why others are wrong:**
- **A:** That’s a metric’s job.
- **B:** That’s logs.
- **D:** Alerts come from metrics, not traces.

---

## Answer 4: [Log Reading Practice]

🔍 Beginner | Fill-in-the-Blank

**Question:** Complete this sentence: "Logs are great for understanding ___________."

A. why something happened and where it occurred

**Correct Answer:** A

**Explanation:** Logs give you context: errors, stack traces, user IDs, and timestamps.

**Why the other options fail:**
- Those are metric-focused insights (e.g., totals, usage, scaling).

---

## Answer 5: [Monitoring vs Observability]

🔍 Beginner | True/False

**Question:** Monitoring and observability are identical terms used interchangeably.

A. True\
B. False

**Correct Answer:** B

**Explanation:** Monitoring is about known questions. Observability is about answering unknown ones.

**Why A is wrong:** Monitoring ≠ Observability. One’s a checklist. The other is an investigation toolkit.

---

## Answer 6: [Pillar Matching]

🔍 Beginner | Matching

**Question:** Match each use case to the most relevant observability pillar:

1. Debugging a failed login flow\
2. Analyzing long-term error rates\
3. Tracing user request across services

**Correct Matches:**\
1 → Logs\
2 → Metrics\
3 → Traces

**Explanation:**
- **Logs:** show events and errors in detail.
- **Metrics:** track trends like error rates.
- **Traces:** show request journeys end-to-end.

---

## Answer 7: [Alert Analysis]

🔍 Beginner | Multiple Choice

**Question:** Which of the following would be considered a **bad alert**?

A. CPU usage over 90% for 10 minutes on 3+ nodes\
B. API error rate spike linked to user-facing service\
C. Memory spike with no context or affected services listed\
D. Service latency over 2s sustained across regions

**Correct Answer:** C

**Explanation:** An alert with no context is just noise.

**Why others are wrong:**
- **A:** Actionable system health alert.
- **B:** Directly tied to customer experience.
- **D:** Significant performance degradation indicator.

---

## Answer 8: [Correlation Workflow]

🧩 Intermediate | Multiple Choice

**Question:** You get a latency alert from DataDog. You check logs in Splunk and find timeout errors. Then a trace shows delay in `payment-service`. What have you just done?

**Correct Answer:** B – Investigated a backend failure using correlation

**Explanation:** Triangulating across data types reveals the true story.

**Why others are wrong:**
- **A:** No fix was deployed.
- **C:** Restarting wasn’t mentioned.
- **D:** Historical log cleanup? Not even close.

---

## Answer 9: [Saved Search Purpose]

🧩 Intermediate | Fill-in-the-Blank

**Question:** Saved searches in Splunk are useful because they __________.

**Correct Answer:** C – automate common queries and can power alerts

**Explanation:** Repeatability + automation = less toil.

**Why others are wrong:**
- **A:** Deleting logs isn’t Splunk’s default job.
- **B:** They *enable* searching, not restrict it.
- **D:** CPU load has nothing to do with it.

---

## Answer 10: [RED Method Basics]

🧩 Intermediate | True/False

**Question:** RED dashboards track Request rate, Errors, and Duration.

**Correct Answer:** A – True

**Explanation:** That’s literally what RED stands for. 

**Why B is wrong:** You’re either trolling or not paying attention.

---

## Answer 11: [Prometheus Logic]

🧩 Intermediate | Multiple Choice

**Question:** What does the following query do?
```promql
rate(http_requests_total{status="500"}[5m])
```

**Correct Answer:** C – Calculates error rate over 5 minutes

**Explanation:** `rate()` tells you how fast something’s changing—in this case, 500 errors.

**Why others are wrong:**
- **A:** Doesn’t show CPU.
- **B:** Doesn’t deal with network.
- **D:** Tracks errors, not log volume.

---

## Answer 12: [Geneos Dashboard]

🧩 Intermediate | Multiple Choice

**Question:** A Geneos dashboard panel showing CPU usage per node with alert at 85% is an example of:

**Correct Answer:** B – Metric visualization

**Explanation:** It’s a numeric trend on a graph. Textbook metric.

**Why others are wrong:**
- **A:** Not trace-related.
- **C:** Not summarizing logs.
- **D:** That’s not a real thing.

---

## Answer 13: [Trace Propagation]

🧩 Intermediate | Fill-in-the-Blank

**Question:** In distributed tracing, each service must forward the ________ headers to continue trace context.

**Correct Answer:** C – Trace context

**Explanation:** Without these, each trace gets orphaned.

**Why others are wrong:**
- **A:** Configuration is unrelated.
- **B:** Billing? No.
- **D:** Authorization is security, not tracing.

---

## Answer 14: [Logs vs Metrics Use]

🧩 Intermediate | Matching

**Question:** Match each type with its strength:

1. Logs\
2. Metrics

**Correct Matches:**\
1 → A (Text-based details and error context)\
2 → B (Numeric trends over time)

**Explanation:**
- Logs are verbose, contextual.
- Metrics are compact, aggregate-friendly.

---

## Answer 15: [Trace Architecture]

💡 Advanced | Multiple Choice | Diagram-Based

**Question:** What is the role of the **Tracing Backend**?

**Correct Answer:** B – Store and visualize trace data

**Explanation:** It's your request breadcrumb museum.

**Why others are wrong:**
- **A:** No self-healing magic here.
- **C:** It doesn’t block anything.
- **D:** Traces ≠ metrics.

---

## Answer 16: [Log Explosion Scenario]

💡 Advanced | Fill-in-the-Blank

**Question:** One common observability issue is log growth causing ________ of the log pipeline, leading to missing data.

**Correct Answer:** B – Saturation

**Explanation:** Like stuffing too many clowns into a car—something’s going to fall out.

**Why others are wrong:**
- **A:** Over-provisioning would solve the problem.
- **C:** Encryption is irrelevant here.
- **D:** Rotation is local, not ingest-related.

---

## Answer 17: [High-Cardinality Metrics]

💡 Advanced | Multiple Choice

**Question:** What’s a good platform approach for analyzing per-customer metrics in AWS?

**Correct Answer:** C – Use Prometheus with dimensional labels

**Explanation:** Prometheus handles labeled data well *if* you manage your cardinality.

**Why others are wrong:**
- **A:** Local-only = siloed + useless.
- **B:** No metrics = no insight.
- **D:** Frontend-only? Good luck.

---

## Answer 18: [Sampling Rates]

💡 Advanced | True/False

**Question:** 100% sampling in distributed tracing is always the best strategy.

**Correct Answer:** B – False

**Explanation:** More data ≠ better. Controlled sampling balances insight and cost.

**Why A is wrong:** It’ll kill your storage. 

---

## Answer 19: [Tool-to-Pillar Mapping]

💡 Advanced | Matching

**Question:** Match each tool to the pillar it primarily supports:

1. Splunk\
2. Prometheus\
3. Jaeger

**Correct Matches:**\
1 → Logs\
2 → Metrics\
3 → Traces

**Explanation:** Each tool maps neatly to one pillar.

---

## Answer 20: [Unified Stack Insight]

💡 Advanced | Multiple Choice

**Question:** In a Kubernetes observability stack with Prometheus, Elasticsearch, and Jaeger feeding Grafana, what’s the primary goal?

**Correct Answer:** B – Centralize visualization across logs, metrics, and traces

**Explanation:** Grafana becomes your all-seeing eye. Just don’t blink.

**Why others are wrong:**
- **A:** Grafana pulls—it doesn’t receive pushes.
- **C:** Prometheus does *not* convert logs or traces.
- **D:** Elasticsearch doesn’t deploy sidecars—it hoards JSON.

---

