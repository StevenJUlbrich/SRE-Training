Yes. Let’s go full beast mode. 🏋️‍♂️

This is **Day 2 – Advanced Metrics Tier**.  
This is **no longer about watching dashboards**—this is about **owning what goes on them**.

This is Marisol in her final form: sharp marker, IDE open, Grafana zoomed, and an app instrumented to expose the metrics *she* defined, not ones she inherited from some chaos engineer in 2017.

---
# 💡 Day 2 – Advanced Metrics:  
*“Custom Metrics, SLIs, and Building Dashboards That Explain Production”*  
🎙 Hosted by Marisol Vieira – Data architect of your uptime, destroyer of vanity panels

---

## 🎯 Goal

Equip engineers to:
- Define and expose meaningful, domain-specific metrics from services
- Use metrics to power SLIs and reliability goals
- Architect dashboards as **narrative tools**, not chart graveyards
- Scale Prometheus-aware systems (handling cardinality, federation, long-term storage)
- Own observability from code to visual to action

This isn’t “make a dashboard.” This is “define how your service tells its story.”

---

## 🧠 Who This Is For

You’ve:
- Written real PromQL
- Built dashboards for teams or systems
- Lived through a broken alert and thought, *“we should measure that differently”*
- Started asking, *“how should this service *prove* it’s healthy?”*

Welcome. You’re ready for Advanced.

---

## 🧪 Writing Custom Metrics in Code

### What’s a custom metric?
Metrics *you* define in code—tailored to your system’s behavior.

Example:
```python
# Python (prometheus_client)
from prometheus_client import Counter

checkout_failures = Counter(
    'checkout_failures_total',
    'Number of failed checkouts',
    ['reason', 'region']
)

checkout_failures.labels(reason='timeout', region='us-east-1').inc()
```

> 🔥 This is observability ownership. You’re no longer reacting to system metrics. You’re building the signals that explain the user experience.

### Metric Type Decision Guide

| Use Case                     | Metric Type  |
|------------------------------|--------------|
| Count of events              | Counter      |
| Current value (e.g. queue)   | Gauge        |
| Distribution over time       | Histogram    |
| Percentiles needed           | Histogram*   |

> ❗ *Avoid **summary** unless you know exactly why. Histograms + PromQL are more flexible and recommended for most use cases.*

---

## 📏 SLIs from Metrics

**SLI = Service Level Indicator**  
A precise, quantitative measure of system behavior that affects users.

Examples:
- ✅ Uptime: availability of `200` responses
- ⏱ Latency: % of requests under 300ms
- 🛑 Error Rate: fraction of `5xx` responses
- 🚫 Saturation: queue length or CPU above threshold

### How to Define One (Example: Login Latency)

1. Metric: `login_duration_seconds_bucket` (a Prometheus histogram)
2. Goal: 95% of logins under 400ms
3. Query:
```promql
histogram_quantile(0.95, sum(rate(login_duration_seconds_bucket[5m])) by (le))
```
4. Compare against threshold. Alert if it breaches for 5 mins.

### Mapping Metric to SLI to Alert

- **Metric**: `http_requests_total`
- **SLI**: % of requests returning 2xx/3xx
- **SLO**: 99.9% over 30 days
- **Alert**: If error rate > 0.1% for 5m, trigger page

---

## 📉 Scaling Prometheus

You’re beyond just dashboards. Now you’re planning observability systems.

### 💾 Federation

- Break up scrape workloads by region/env
- Useful for multi-team, multi-tenancy setups

### 🗃 Long-Term Storage (Thanos / Cortex)

- Store metrics for months/years
- Use cases:
  - SLA reporting
  - Historical regression analysis
  - Long tail reliability tracking

### ⚠ AlertManager Routing Strategy

- Group alerts by service
- Use routing trees by severity, team, on-call
- Add *playbooks* to alert messages!

---

## 🎨 Dashboard as Narrative

> “A dashboard is an argument for or against system health.”  
> — Marisol, after deleting 12 donut charts from staging

### 🧰 Structure for Operational Dashboards

| Section | Metrics (SLI-aligned) |
|---------|-----------------------|
| Top     | Uptime %, success rate, error budget burn |
| Middle  | p95/p99 latency, retry rate, queue length  |
| Bottom  | Resource metrics, alerts summary, deploy markers |

### Dashboard Patterns to Use

- **Heatmaps** for latency distributions
- **Bar charts** for comparisons (e.g., top N slow endpoints)
- **Single-stat** for high-level KPIs
- **Graph + Alert annotation** combo for incident reviews

---

## 🧪 Advanced Exercises

### 1. Create a Custom Metric
- Use any language w/ `prometheus_client`
- Implement:
```text
orders_queued_total{priority="high"}
```
- Simulate updates
- Expose on `/metrics` (the default Prometheus endpoint), validate in browser or curl

> ⚠️ **Tip:** Be mindful of label cardinality when designing custom metrics. Too many unique label values can overload your monitoring system.

---

### 2. Define an SLI for a Critical Path
- Use your app’s real data or mock metric
- Pick an SLI (latency, error, etc.)
- Write the query
- Define SLO target (e.g., 99.95%)
- Draft the alert rule

---

### 3. Build a Dashboard That Tells a Story
- Goal: Show “Is `checkout-service` working right now?”
- Must include:
  - Latency distribution
  - Error rate (non-2xx)
  - Throughput (requests/sec)
  - Uptime or health check indicator
- Bonus: Add deployment markers

---

## ✅ What You Should Know Now

You now:
- Understand how to define and expose new metrics from your service
- Can turn raw data into SLIs and meaningful alerts
- Know how to scale observability infrastructure with Prometheus
- Can build dashboards that communicate operational health clearly and concisely

---

## 🧱 You’ve Reached the Top Brick

Marisol’s parting words:
> “Metrics aren’t data. Metrics are **proof**. Proof that your service works. Or doesn’t.”

Next up? Apply this to an incident, a postmortem, or SLO rollout.

Or, you know, go delete a panel titled “Panel Title.” You’ve earned it.


