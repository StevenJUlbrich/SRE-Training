# 📊 Day 2 – Metrics 101 (Beginner Tier, Grafana-Centric)  
>*“So You’ve Seen a Dashboard—Let’s Talk About What It’s Actually Telling You”*  
🎙 With Marisol Vieira – São Paulo SRE, Dashboard Whisperer, Champion of Clean Visuals

---

## 🎯 Goal

By the end of this session, you will:
- Understand what a **metric** actually is in observability
- Know how metrics show up in **Grafana dashboards**
- Recognize the parts of a metric: name, value, labels, timestamp
- Differentiate metric types (e.g., counters vs gauges)
- Read time series graphs with clarity
- Begin writing or adjusting queries to answer real questions

---

## 🧠 Who This Is For

This is for engineers and support folks who:
- Have seen and used **Grafana dashboards**
- Can click around panels and select time ranges
- Want to go deeper—understanding *why* a line goes up, what’s behind the data, and how to make better use of what they’re seeing

---

## 🔍 What Is a Metric?

Let’s start from zero. A **metric** is a number that changes over time. It’s a single measurement of something happening inside your system.

> 🧱 Imagine each metric as a **brick in the wall** of system visibility. One by itself doesn’t say much. But when combined with others, you get a full picture.

### 📏 Example Metric Ideas:
- Number of HTTP requests your app receives
- CPU usage of a server
- Memory in use by a container
- Error rate for a service

Metrics are collected automatically at regular intervals (like every 15 seconds), stored in a backend system, and **visualized through dashboards**—usually in **Grafana**.

You don’t see raw metrics. You see them **graphed**, compared, and turned into answers.

---

## 📦 Anatomy of a Metric

Every metric you see on a dashboard has 4 parts:

| Part        | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| **Name**    | What is being measured. E.g. `cpu_usage`, `http_requests_total`            |
| **Value**   | The number at that moment. E.g. 87% CPU                                      |
| **Labels**  | Extra info that adds detail. E.g. `job="web"`, `status="500"`, `region="us-west"` |
| **Timestamp** | When the number was recorded                                              |

> ### 🧠 Think of **labels** as filters or tags. They help you slice the data:
> - All 500 errors
> - Just requests from `auth-service`
> - CPU usage from servers in `eu-west-1`

---

## 💡 Where Do Metrics Come From?

While Grafana shows the dashboards, it doesn’t store the data itself.  
Your system collects metrics using tools (called **exporters**) that expose numbers on a special endpoint. A collector (like **Prometheus**, though it may be hidden from you) scrapes those numbers and sends them to be visualized.

You don’t need to configure this right now—just know:
- **Grafana is the window**
- **Your system is the storyteller**
- **The metrics are the message**

---

## 📈 Types of Metrics

Different kinds of metrics behave differently. You’ve probably seen lines go up, down, flat, or spike. Let’s explain what’s behind that:

| Type       | What It Means                      | Example                           |
|------------|------------------------------------|-----------------------------------|
| **Counter** | Increases over time (never goes down) | Total number of requests           |
| **Gauge**   | Goes up and down                   | Current memory usage, temperature |
| **Histogram** | Groups values into buckets        | Response times grouped by speed   |
| **Summary**   | Pre-computed statistics (less used) | Response duration percentiles     |

### Real Examples You’ve Probably Seen:
- `cpu_usage` → a **gauge** that goes up/down as usage changes  
- `http_requests_total` → a **counter** that counts every request since startup  
- `request_duration_seconds_bucket` → a **histogram** used to track latency

---

## 🔍 Reading Dashboards with More Confidence

You already know where the dashboards are. Now it’s time to **read them with intention.**

> ## Ask: “What question does this panel answer?”

Bad:  
> ## “Here’s a pretty line graph.”

Better:  
> ## “This shows checkout errors over time, by region.”

### Key Tips:
- Make sure you understand what the **unit** is (ms? %, count?)  
- Look at **label filters**—are you seeing the full picture or just one service?  
- Don’t trust a flat line until you confirm the **time range**

---

## 🧪 Quick Exercises

### 1. Panel Breakdown
Pick a panel from a dashboard you use. Answer:
- What’s the metric name?
- What kind of metric is it (counter/gauge)?
- What does it tell you?
- What would *you* ask next after seeing this graph?

### 2. Metric Lookup
In the Grafana query editor, type:
```text
http
```
Use autocomplete to explore which metrics start with `http_`. Pick one and see how many labels it has. Try filtering by one:
```promql
http_requests_total{status="500"}
```

What do you notice?

### 3. Build a Mini Panel
Make a new panel showing:
- CPU usage over time
- Filtered to one host or container
- Time range: Last 30m
- Bonus: Add a threshold line at 85%

---

## 🧠 Common Pitfalls (Marisol’s Rants)

- **Flat line doesn’t mean nothing’s happening** → Could be wrong time range or wrong metric  
- **"Total" metrics without `rate()`** → You’re looking at accumulation, not behavior  
- **High-cardinality labels** → e.g., `user_id="1234"` — don’t do this unless you want to set dashboards on fire

---

## ✅ What You Should Know Now

You now:
- Understand what metrics are, how they’re structured, and how they get to Grafana
- Can read and interpret time series graphs more confidently
- Know metric types: counter, gauge, histogram
- Can explore and filter metrics using the query editor
- Are one step closer to building dashboards that *answer questions*

---

## ⏭️ Next Brick: Intermediate Metrics – Querying with PromQL, Reducing Dashboard Noise, and Measuring What Matters

Coming up:
- How to ask better questions with queries
- Why some dashboards fail during incidents
- Starting to define metrics that matter for users, not just systems


