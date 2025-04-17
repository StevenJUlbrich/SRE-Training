
# 🧱 Observability 101 – Day 1 (Beginner Level)


> 🎯 Goal: Understand the fundamentals of observability and how it differs from traditional monitoring. Learn the Three Pillars, explore existing tools, and build a mindset for investigating issues like an SRE-in-training.

---

## 🔍 What is Observability?

> **“Observability is a measure of how well internal states of a system can be inferred from knowledge of its external outputs.”**  
> — *Google SRE Book*


In plain English: observability helps you *see inside* a system by examining what it produces—metrics, logs, traces—without poking at it like a malfunctioning toaster.


It’s the difference between **guessing what’s wrong** and **actually knowing**.

---

## 🔄 Monitoring vs Observability

| Concept        | What It Means                                  | Analogy                                                |
|----------------|-------------------------------------------------|---------------------------------------------------------|
| Monitoring     | Asking questions you already know to ask        | Is the CPU over 80%? Are errors above threshold?        |
| Observability  | Getting answers to unknown questions            | Why are logins failing only for users in Australia?     |

Monitoring is *reactive*—alerts, thresholds, dashboards.  
Observability is *exploratory*—it gives you the tools to dig into unknown failures.

---

## 🧱 The Three Pillars of Observability

Observability relies on three primary types of telemetry data. Each tells a different story.

---

### 📜 Logs

- Timestamped text records from services or infrastructure
- Can be structured (JSON) or unstructured (human-readable chaos)
- Great for understanding **what happened** and **where** it happened

**Example:**
```
[ERROR] AuthService - Token validation failed for userID 11235
```

**Use Logs To:**
- Investigate exceptions
- Audit flows
- Search for specific error messages

---

### 📈 Metrics

- Numeric data points measured over time
- Typically used to detect trends, monitor performance, and trigger alerts

**Example:**
```
http_requests_total{service="checkout"} = 12,345
```

**Common Metrics:**
- Request count
- Latency (e.g., p95 response time)
- CPU/memory usage
- Error rates

**Use Metrics To:**
- Alert when thresholds are crossed
- Visualize trends in dashboards
- Track service-level performance

---

### 🧵 Traces

- A full timeline of a single request through multiple services or components
- Helps visualize **where time is being spent** or **where failure occurred**

**Example:**
```
Trace ID 234a → Auth (30ms) → Cart (90ms) → Payment (1.2s) → Error
```

**Use Traces To:**
- Identify performance bottlenecks
- Diagnose issues in distributed systems
- Understand user experience across services

---

## 🔍 Activity – What Would You Miss?

> ❓ If you only had **logs**, what kind of failures would be invisible to you?

Reflect and jot down:
- Can you detect **slow performance** from logs alone?
- Do logs show **trends over time**?
- What happens if logs are missing or unstructured?

🧠 *Hint:* Logs are great for error snapshots—but useless for spotting gradual degradation or service-wide latency.

---

## 🧪 Mini Quiz – Pick the Pillar

Match each scenario to the most helpful observability pillar:

| Scenario                                                 | Answer          |
|----------------------------------------------------------|-----------------|
| Debugging a slow API                                     | 🧵 Traces        |
| Tracking a spike in memory usage                         | 📈 Metrics       |
| Investigating why a null pointer exception was thrown    | 📜 Logs          |
| Diagnosing a multi-service login failure                 | 🧵 Traces + 📜 Logs |
| Measuring Black Friday traffic patterns                  | 📈 Metrics       |
| Understanding why alerts didn’t fire                     | 🧵 + 📈 + 📜 All  |

---

## ✅ What You Should Know Now

By the end of Day 1, you should:
- Know what observability is (and what it’s not)
- Understand the Three Pillars: Logs, Metrics, Traces
- Recognize when each type of telemetry is useful
- Begin looking at your tools (Geneos, Splunk, DataDog) with observability goggles on

---

## ⏭️ Next Brick: Tool Mapping & Alert Anatomy

Coming up:
- How your current tools (Geneos, Splunk, DataDog) map to logs, metrics, and traces
- What makes an alert *useful* vs “please make it stop”


---

