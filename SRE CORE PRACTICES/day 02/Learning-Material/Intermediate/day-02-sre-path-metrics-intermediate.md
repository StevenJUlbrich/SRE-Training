# 🧩 Day 2 – Intermediate Metrics:  
>*“From Graph Watcher to Data Operator”*  
🎙 With Marisol Vieira – Metrics maximalist, dashboard demolisher, São Paulo's finest

---

## 🎯 Goal

Help learners become fluent in the *metrics-to-action* pipeline by:
- Writing robust, readable, and high-signal PromQL queries
- Understanding performance tradeoffs (rate vs irate, sum vs avg)
- Reducing dashboard noise without losing visibility
- Modeling service health with accurate metrics
- Laying the foundation for SLOs and SLIs

This isn’t just about syntax. This is **SRE fluency with metrics.**

---

## 🧠 Who This Is For

This module is for engineers who:
- Can navigate Grafana and adjust queries
- Know a counter from a gauge but still fumble with `by (label)`
- Want to stop being dashboard spectators and start being metric authors

---

## 🔍 PromQL Deep Dive

PromQL is powerful, flexible, and easy to misuse. You don’t need to memorize it—you need to **understand what it’s *doing***.

### ⚙ Core Query Types

#### 1. **Counters (with `rate()` or `irate()`)**
```promql
rate(http_requests_total[5m])
```
- Use `rate()` to show trend over time (smooth, ideal for dashboards)
- Use `irate()` for sharper accuracy (useful for alerting on spikes)

📌 **Best Practice**: Always use `rate()` with counters. A raw counter without `rate()` will just show a slope—not activity.

#### 2. **Grouping + Aggregation**
```promql
sum by (service) (
  rate(http_requests_total{status=~"5.."}[5m])
)
```
- Groups data across labels
- Great for top-level dashboards (“Which service is failing most?”)

#### 3. **Filtering with Labels**
```promql
rate(http_requests_total{method="POST", job=~"api-.*"}[1m])
```
- Use exact match `=` for known values
- Use regex `=~` for patterns—but know it’s expensive

🧠 Pro Tip: Avoid using unbounded labels like `path`, `user_id`, or `session_id` unless you’re trying to destroy Prometheus on purpose.

---

## 💣 High-Cardinality Metrics: The Hidden Flame

Let’s talk cardinality. It’s what happens when you collect *too much detail*, and suddenly your queries are slow, your dashboard is a war crime, and your Prometheus server cries in YAML.

### 🔥 Cardinality Red Flags:
- Labels with unique IDs: `pod_id`, `transaction_id`, `customer_id`
- Too many combinations: 5 labels with 20 values each = 3.2 million series
- `count by (instance)` on 12k nodes = dashboard death spiral

🧠 Rule: **Only label what you’d actually group or alert on.**  
If no one is ever going to say “show me error rate by container_hash” — cut it.

---

## 📉 Dashboard Strategy: Signal vs Vanity

**Vanity dashboards** have:
- Dozens of panels with no purpose
- Duplicate data split by unnecessary labels
- Cute but meaningless metrics (“Number of cron runs in the past hour”)

**High-signal dashboards** show:
- Request success rate (`1 - rate(http_requests_total{status=~"5.."})`)
- Latency by percentile (`histogram_quantile(0.95, rate(duration_bucket[5m]))`)
- Capacity and resource saturation
- Impact metrics (“Are users getting what they came for?”)

### ✍ Marisol's Dashboard Layout Template:

| Section            | Panels (What to Measure)                              |
|--------------------|------------------------------------------------------|
| Top bar (exec view)| Uptime %, request success rate, user transactions/min |
| Mid (system health)| p95 latency, CPU usage, memory, error rate by service |
| Bottom (debug view)| Slowest endpoints, retry counts, queue depth          |

📌 Each panel should answer a question. If it doesn’t—it’s noise.

---

## 💬 Real-World Metrics Use Cases

### 1. **Incident Diagnosis**
```promql
rate(http_requests_total{status=~"5.."}[5m])
```
→ Are errors increasing?  
Pair with:
```promql
histogram_quantile(0.95, sum(rate(request_duration_seconds_bucket[5m])) by (le, service))
```
→ Where is the latency bottleneck?

### 2. **Resource Bottleneck Triage**
```promql
rate(node_cpu_seconds_total{mode="idle"}[5m])
```
→ Flip to show busy CPU:
```promql
1 - avg by (instance)(rate(node_cpu_seconds_total{mode="idle"}[5m]))
```

Pair with memory usage, IO saturation, and see if performance issues are infra or app.

### 3. **User-Impact Metrics**
```promql
sum(rate(http_requests_total{status="200"}[1m])) by (region)
```
→ Throughput by geography—are users getting responses?

```promql
rate(login_failures_total[5m])
```
→ Security/performance concern?

---

## 🧪 Hands-On PromQL Challenges

### 🧠 Challenge 1: Simplify This
Given:
```promql
rate(http_requests_total{status=~"2.."}[1m]) + rate(http_requests_total{status=~"3.."}[1m])
```
✅ Rewrite to:
- Show total *non-error* traffic
- Group by job
- Include only `method="GET"`

Answer:
```promql
sum by (job)(
  rate(http_requests_total{status!~"4..|5..", method="GET"}[1m])
)
```

---

### 🧠 Challenge 2: Build a Reliable Alert
> Alert: "Payment API is failing more than 1% of requests for 3 minutes"

Your query:
```promql
(
  sum(rate(http_requests_total{status=~"5..", service="payment-api"}[1m]))
/
  sum(rate(http_requests_total{service="payment-api"}[1m]))
) > 0.01
```
🧠 Wrap that in an alert rule with `for: 3m`, and you’ve got production-quality signal.

---

### 🧠 Challenge 3: Build a Business-Facing Panel
- Metric: `order_created_total`
- Filters: `region`, `env="prod"`
- Query:
```promql
sum by (region)(
  rate(order_created_total{env="prod"}[5m])
)
```
Title: “Orders per Region – Last 5 Minutes”

🧠 Bonus: Add annotation for deploys.

---

## ✅ What You Should Know Now

You now:
- Can write effective PromQL queries for different metric types
- Know how to group, filter, and aggregate without creating chaos
- Understand the dangers of high cardinality
- Can redesign noisy dashboards into clean, high-impact visuals
- Have the muscle to support incident response with metrics

---

## ⏭️ Next Brick: 💡 Advanced Metrics  
*“Custom Metrics, SLIs, and Building Dashboards That Explain Production”*

Coming up:
- Instrumenting services to expose new metrics
- SLI definitions using raw telemetry
- Real-world dashboards for SLAs and postmortem retros

