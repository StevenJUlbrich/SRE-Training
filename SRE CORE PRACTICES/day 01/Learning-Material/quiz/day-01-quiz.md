# 📘 Day 1 Observability Learning Quiz

Below are 20 quiz questions derived from Beginner, Intermediate, and Advanced-level content on Observability 101. Format follows the Day-01-Quiz template. Questions include MCQs, true/false, fill-in-the-blank, and diagram-based formats.

---

## 1. [Three Pillars Overview]  
🔍 Beginner | Multiple Choice

Which of the following best describes the Three Pillars of Observability?

A. Debugging, Logging, and Uptime  
B. Metrics, Logs, and Traces  
C. Alerts, Incidents, and Postmortems  
D. Dashboards, Reports, and Alarms

---

## 2. [Metrics Insight]  
🔍 Beginner | True/False

Metrics can help identify performance trends over time and are often visualized in dashboards.

A. True  
B. False

---

## 3. [Trace Utility]  
🔍 Beginner | Multiple Choice

What is the primary purpose of a **trace** in observability?

A. Show numeric trends of system health  
B. Highlight configuration errors in logs  
C. Visualize the path and timing of requests across services  
D. Trigger CPU alerts when latency spikes

---

## 4. [Log Reading Practice]  
🔍 Beginner | Fill-in-the-Blank

Complete this sentence: "Logs are great for understanding ______________."

A. why something happened and where it occurred  
B. the total number of requests made  
C. memory usage per pod  
D. cluster scaling metrics

---

## 5. [Monitoring vs Observability]  
🔍 Beginner | True/False

Monitoring and observability are identical terms used interchangeably.

A. True  
B. False

---

## 6. [Pillar Matching]  
🔍 Beginner | Matching

Match each use case to the most relevant observability pillar:

1. Debugging a failed login flow  
2. Analyzing long-term error rates  
3. Tracing user request across services

A. Logs  
B. Metrics  
C. Traces

---

## 7. [Alert Analysis]  
🔍 Beginner | Multiple Choice

Which of the following would be considered a **bad alert**?

A. CPU usage over 90% for 10 minutes on 3+ nodes  
B. API error rate spike linked to user-facing service  
C. Memory spike with no context or affected services listed  
D. Service latency over 2s sustained across regions

---

## 8. [Correlation Workflow]  
🧩 Intermediate | Multiple Choice

You get a latency alert from DataDog. You check logs in Splunk and find timeout errors. Then a trace shows delay in `payment-service`. What have you just done?

A. Deployed a hotfix automatically  
B. Investigated a backend failure using correlation  
C. Restarted the database  
D. Cleaned out historical logs

---

## 9. [Saved Search Purpose]  
🧩 Intermediate | Fill-in-the-Blank

Saved searches in Splunk are useful because they __________.

A. delete logs older than 24 hours  
B. convert logs into traces  
C. automate common queries and can power alerts  
D. throttle logs based on CPU load

---

## 10. [RED Method Basics]  
🧩 Intermediate | True/False

RED dashboards track Request rate, Errors, and Duration.

A. True  
B. False

---

## 11. [Prometheus Logic]  
🧩 Intermediate | Multiple Choice

What does the following query do?  
```promql
rate(http_requests_total{status="500"}[5m])
```

A. Shows CPU usage of the frontend  
B. Alerts on network bandwidth  
C. Calculates error rate over 5 minutes  
D. Tracks log volume growth

---

## 12. [Geneos Dashboard]  
🧩 Intermediate | Multiple Choice

A Geneos dashboard panel showing CPU usage per node with alert at 85% is an example of:

A. Trace instrumentation  
B. Metric visualization  
C. Log summarization  
D. Alert fatigue simulation

---

## 13. [Trace Propagation]  
🧩 Intermediate | Fill-in-the-Blank

In distributed tracing, each service must forward the ________ headers to continue trace context.

A. DNS  
B. Billing  
C. Trace context  
D. Health check

---

## 14. [Logs vs Metrics Use]  
🧩 Intermediate | Matching

Match each type with its strength:

1. Logs  
2. Metrics

A. Text-based details and error context  
B. Numeric trends over time

---

## 15. [Trace Architecture]  
💡 Advanced | Multiple Choice | Diagram-Based

```mermaid
flowchart LR
  A[Frontend: Start Trace] --> B[API Service]
  B --> C[Tracing Backend: Jaeger]
  C --> D[Trace UI]
```

What is the role of the **Tracing Backend**?

A. Automatically debug your application code  
B. Store and visualize trace data  
C. Generate metrics from logs  
D. Restart failing services

---

## 16. [Log Explosion Scenario]  
💡 Advanced | Fill-in-the-Blank

One common observability issue is log growth causing __________ of the log pipeline, leading to missing data.

A. Overwriting  
B. Saturation  
C. Encryption  
D. Tracing

---

## 17. [High-Cardinality Metrics]  
💡 Advanced | Multiple Choice

What’s a good platform approach for analyzing per-customer metrics in AWS?

A. Use local logs only  
B. Avoid collection entirely  
C. Use Prometheus with dimensional labels  
D. Push to frontend dashboards only

---

## 18. [Sampling Rates]  
💡 Advanced | True/False

100% sampling in distributed tracing is always the best strategy.

A. True  
B. False

---

## 19. [Tool-to-Pillar Mapping]  
💡 Advanced | Matching

Match each tool to the pillar it primarily supports:

1. Splunk  
2. Prometheus  
3. Jaeger

A. Metrics  
B. Traces  
C. Logs

---

## 20. [Unified Stack Insight]  
💡 Advanced | Multiple Choice

In a Kubernetes observability stack with Prometheus, Elasticsearch, and Jaeger feeding Grafana, what’s the primary goal?

A. Route all data through logs  
B. Centralize visualization across logs, metrics, and traces  
C. Skip dashboards for reduced cost  
D. Replace traces with metrics only

---

**End of Day 1 Quiz**