# 💻 Observability 101 – Junior SRE Edition  
*Day 1: “How to Start Understanding Systems Without Panicking”*

🎙 Narrated by Hector Alvarez – uptime mechanic, log whisperer, and reluctant mentor.

> **Hector’s Monologue:** “Everybody loves a blinking dashboard—until it blinks and you don’t know why. Let’s fix that.”

---

## 🎯 Goal

Help junior SREs move from reactive ticket-clicking to proactive system investigation.  
Learn how to navigate telemetry data, understand the Three Pillars of Observability, and start forming mental models for investigating real-world issues.

---

## 🧠 Who This Is For

You’ve done some support work. You’ve seen alerts. You may have clicked through dashboards without knowing if you were supposed to *feel something*. You're now entering the SRE journey—and this is your first step toward diagnosing, debugging, and improving system reliability.

> **Hector’s Monologue:** “You don’t need to know everything. But you do need to know where to look when it breaks.”

---

## 🔍 What Is Observability?

> **“Observability is how well you can understand what's going on inside a system based on the information it gives you.”**  
> — *SRE Translation Service, Junior Edition*

It’s not just about reacting to alerts—it’s about being able to **ask your system intelligent questions** when things go wrong, and actually *get answers* without guessing.

> **Hector’s Monologue:** “If monitoring is like a security alarm, observability is the security camera footage. It tells you what happened, not just that it did.”

---

## 🧱 The Three Pillars of Observability

You’ll see these everywhere. They are the building blocks of how we observe complex systems.

### 📜 Logs

- Text records of what your services are doing.
- Can include errors, events, debug info.
- Usually what you read when someone says “go check Splunk.”

**Example:**
```spl
2024-04-17 10:32:12 [ERROR] AuthService - Invalid token for user_id=4412
```

> 🧠 Logs are great for answering:  
> - What happened?  
> - Where did it happen?  
> - Was there an error?

> **Hector’s Monologue:** “Logs are your witnesses. They don’t always speak clearly—but they remember everything.”

---

### 📈 Metrics

- Numbers that are measured over time.
- These live in dashboards like Geneos or DataDog.
- Metrics tell you how things are **performing**.

**Example:**
```
CPU usage = 92%
Request latency (p95) = 1.2s
Error rate = 3.4%
```

> 🧠 Metrics help you:  
> - Detect spikes or drops  
> - Monitor trends  
> - Trigger alerts when thresholds are crossed

> **Hector’s Monologue:** “Metrics tell you something’s weird. They don’t tell you *why*. That’s someone else’s job—or yours.”

---

### 🧵 Traces

- Like a GPS map of a user request traveling through your system.
- Shows how long each service took and where problems happened.
- Often found in APM tools like DataDog or OpenTelemetry dashboards.

**Example:**  
A user login request took:
- 30ms in frontend
- 90ms in auth
- 600ms in database (💥 bottleneck)

> 🧠 Traces help you:  
> - Understand **where** delays happen  
> - Follow requests across **microservices**  
> - See full end-to-end behavior of your system

> **Hector’s Monologue:** “Traces are like detective work—but faster, and nobody slams the table.”

---

## 🔄 Monitoring vs Observability

Let’s make this painfully clear:

| 🔧 Monitoring           | 🔬 Observability                |
|------------------------|--------------------------------|
| Predefined alerts       | Asking new questions during incidents |
| “If X > 80%, page me”   | “Why is X > 80%, and what else broke?” |
| Mostly reactive         | Both reactive *and* investigative |

> 🧠 Monitoring tells you *something’s wrong*.  
> Observability helps you figure out *why* it’s wrong.

> **Hector’s Monologue:** “Monitoring is a doorbell. Observability is looking through the peephole.”

---

## 🔔 Alerts – Learning to Read the Screaming

You’ve seen alerts. Some are helpful. Most are chaos.

Here’s what you’re looking for in a **good alert**:
- It points to a **real problem**, not just “CPU spiked for 3 seconds.”
- It includes enough context to help you start investigating.
- It doesn’t fire constantly for no reason (hello, alert fatigue).

**Example Alert:**
> "Payment API p95 latency > 2s for 5 minutes – related service: `order-service`, region: `us-east-1`"

**Not helpful alert:**
> “Disk warning: /dev/sda1 at 85%”

> **Hector’s Monologue:** “If the alert doesn’t tell you what to check, it’s not an alert—it’s background noise.”

---

## 🧪 Quick Activity: Match the Tool to the Pillar

Which of these tools help with which observability data?

| Tool     | Logs | Metrics | Traces |
|----------|------|---------|--------|
| Geneos   | ❌   | ✅      | ❌     |
| Splunk   | ✅   | ✅ (via saved searches) | ❌     |
| DataDog  | ✅   | ✅      | ✅     |

> 🧠 Optional: Open each tool (if you have access) and find an example of each type of data.

---

## 🧠 Triage Mindset: What Do I Look at First?

When you get an alert, try following this flow:

1. **What is the alert telling me?**
2. **Is this affecting users?** (high latency, errors, etc.)
3. **Check the dashboard:** Look for patterns or spikes
4. **Check logs:** Are there any error bursts?
5. **Check traces (if available):** Where is time being spent?

> **Hector’s Monologue:** “You’re not hunting for bugs. You’re looking for *cause*. Don’t stop at the first error that looks guilty.”

---

## 🧪 Exercises

### 1. Alert to Investigation
Pick a recent alert from your environment (Geneos, DataDog, etc).  
Ask:
- What kind of data is it based on?
- What’s your first move to investigate?

### 2. Splunk Log Search (Guided)
Use a basic Splunk query to find errors:

```spl
index=prod_logs "error" OR "exception"
| stats count by service_name
```
What’s the top offending service?

### 3. Dashboard Reading Practice
Find a dashboard in Geneos or DataDog:
- What metric is being shown?
- What’s the time window?
- Is there anything unusual?

---

## ✅ What You Should Know Now

You should now:
- Understand the difference between monitoring and observability
- Know the three types of telemetry data: logs, metrics, traces
- Be able to identify these in Splunk, Geneos, and DataDog
- Start building a mental model for how alerts → investigation → resolution

> **Hector’s Monologue:** “You can’t fix what you can’t see. And you can’t learn if you never look. Let’s change that.”

---

## ⏭️ Next Brick: Correlating Logs, Metrics, and Traces

> In the next session:  
> We’ll learn how to combine these signals to find **root cause** and not just guess based on vibes.

