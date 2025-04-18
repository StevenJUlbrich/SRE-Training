# 🧩 Observability 101 – Intermediate Level: "I Can Actually Find the Root Cause Now"

🎙 Narrated by Hector Alvarez – uptime historian, postmortem survivor, and dashboard realist.

> "You don’t find the root cause. You reconstruct it like a crime scene. And half your clues are hiding in plain sight."

---

## 🎯 Goal

Build on foundational knowledge to begin diagnosing real incidents. Learn how to correlate telemetry data across tools, evaluate alert quality, and build basic queries, dashboards, and visualizations that don’t insult anyone’s intelligence.

---

## 🧠 Learning Objectives

- Correlate observability data across tools (e.g., logs in Splunk with metrics from DataDog or Geneos)
- Evaluate alerts for accuracy, noise, and actionability
- Build or refine **Splunk saved searches** and **Geneos dashboards**
- Understand basics of **Prometheus queries** and **OpenTelemetry traces**
- Identify gaps in observability coverage and know what signals might be missing

> **Hector’s Monologue:** "If you’re only looking at one tool during an incident, you’re probably looking in the wrong place. The truth lives in the overlap."

---

## 🔄 Data Correlation: Putting the Puzzle Together

> 🧠 Hector: "The root cause doesn’t live in logs. Or metrics. Or traces. It lives in how they connect."

In production, you rarely find root cause in a single pane of glass (unless your dashboards are run by wizards).

You need to:
1. See the metric spike.
2. Check for relevant log entries.
3. Trace the path of a request across services.

> 🔍 *Example:*  
> You get a latency alert from DataDog.  
> - Metric shows spike at 12:03 UTC.  
> - Splunk logs show increased timeout errors.  
> - Trace shows delay in `payment-service`.  
> Now you have a story, not just symptoms.

> **Hector’s Monologue:** "Correlating data is like reconstructing a bar fight with security cam footage, chat logs, and someone’s blurry TikTok. Do it right, and the cause becomes obvious."

---

## 🔔 Alert Evaluation: Good vs Garbage

> **Good Alert:**
> - Tells you something user-facing is broken
> - Is specific enough to guide investigation
> - Doesn’t fire 600 times during one incident

> **Garbage Alert:**
> - Says “HIGH CPU” and nothing else
> - Fires when no one cares
> - Has no metadata or links to supporting telemetry

> **Hector’s Monologue:** "If an alert fires and the first thing you do is open three dashboards and say 'huh?', that’s not an alert. That’s a cry for help."

🧠 Pro Tip: Alerts should answer “What’s broken?” and “What should I look at first?”

---

## 🧪 Tool Skills: Splunk, Geneos, Prometheus (Intro Edition)

### 🔎 Splunk (Logs + Saved Searches)

- Search for log events using `index=`, `source=`, and fields like `error`, `status`, `user_id`
- Build **saved searches** to detect specific conditions or patterns
- Convert saved searches into **alerts**

> Example Splunk query:
```spl
index=prod_logs "payment failed"
| stats count by service_name
```

### 📊 Geneos (Dashboards + Metrics)

- Understand Netprobes and gateways
- Create dashboard panels showing CPU, memory, request rate
- Set thresholds and alarm rules based on custom metrics

> Geneos Example: Display memory usage over time for all app servers, with alert at 85%

### 📈 Prometheus (Metrics Query Language)

> Prometheus uses PromQL to query time-series data.

> Basic example:
```promql
rate(http_requests_total{status="500"}[5m])
```
This shows the **rate of 500 errors** over the last 5 minutes.

> **Hector’s Monologue:** "Never alert on a raw counter. That’s like judging speed by the odometer. Use `rate()` or expect confusion."

---

## 🧩 OpenTelemetry (The Teaser Trailer)

- OpenTelemetry allows you to **instrument apps** for traces and metrics
- Eventually, you’ll use this in Python, Java, or whatever your team likes to argue about
- Right now, focus on **understanding how traces are collected and what data they contain**

**Trace Example Flow:**
```
[frontend] —> [auth-service] —> [cart-service] —> [payment-service]
      |                 |                |                  |
     10ms             40ms             90ms             1500ms 🔥
```

> **Hector’s Monologue:** "A trace isn’t a graph. It’s a confession. Listen closely."

---

## 🧪 Exercises

1. **Simulated Incident Investigation**  
   Given:
   - Metric alert from DataDog
   - Logs from Splunk
   - Basic trace diagram  
   → Determine: Which service is the problem and why?

2. **Saved Search Tune-Up**  
   Take an existing saved search in Splunk and reduce its noise:
   - Add `status!="200"`
   - Limit to specific services or hostnames
   - Add aggregation to make it dashboard-friendly

3. **Dashboard Sketch**  
   Plan a Geneos or DataDog dashboard with:
   - 1 business KPI (e.g., payment volume)
   - 1 system KPI (e.g., CPU usage)
   - 1 service-level metric (e.g., error rate)
   - Use clear visual elements: no rainbow spaghetti

4. **Prometheus Query Warm-Up**  
   Write and explain:
```promql
rate(payment_failures_total[1m])
```
   - What does it show?
   - Why would you alert on this?

> **Hector’s Monologue:** "If your dashboard answers a question no one asked, congratulations. You’ve wasted everyone’s time."

---

## ✅ What You Should Know Now

By now, you should:
- Understand how to connect metrics, logs, and traces across systems
- Know the difference between good and bad alerts (and how to improve them)
- Be able to write a basic log search in Splunk and read a Geneos dashboard
- Have a mental model for incident triage using observability data

---

## ⏭️ Next Brick: Tracing in Action & Writing SLIs

Coming up:
- Following full user requests across systems
- Defining SLIs that reflect actual user experience
- Mapping telemetry to reliability goals

> **Hector’s Monologue:** "A broken service that no one notices isn’t reliable. It’s *undiscovered*. That’s worse."

---

