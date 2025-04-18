We're building **Day 1: Observability 101** and nothing else. No fancy extras, no SLO manifestos, no code snippets of mystical YAML prophecies. Just day one. One brick. Very brick. Much foundational.

---

## 📚 **Day One: Observability 101**  
*Subtitle: “Stop Looking for Logs in All the Wrong Places”*  
**Duration:** ~60–90 minutes (depending on how much sarcasm is in the delivery)

---

## 🔍 Section 1: What Even *Is* Observability?

**Goal:** Learners understand what observability *actually* means—not just the buzzword.

### Content:
- Definition (Google SRE style):  
  > “A measure of how well internal states of a system can be inferred from knowledge of its external outputs.”
- Monitoring vs Observability  
  - *Monitoring*: You ask questions you already know to ask  
  - *Observability*: You get answers to questions you didn’t know you had
- The "Three Pillars":
  - **Logs**: Textual bread crumbs
  - **Metrics**: Numbers and counts (things you *measure*)
  - **Traces**: Contextual journey of a request through systems

### Activity/Prompt:
- Ask learners: “If you only had logs, what kind of failures would be invisible to you?”
- Short quiz-style interaction: Which pillar is most useful for…  
  - Debugging a slow API? *(Trace)*  
  - Tracking CPU spikes? *(Metrics)*  
  - Investigating why an exception was thrown? *(Logs)*

---

## 🧰 Section 2: The Tools You Already Use (Whether You Like It or Not)

**Goal:** Translate existing tools (Geneos, Splunk, DataDog) into the language of observability.

### Content:
| Tool       | Pillar(s)     | Example Use          |
|------------|----------------|----------------------|
| **Geneos**   | Metrics, Alerts | CPU usage, heartbeat checks |
| **Splunk**   | Logs, Metrics (via saved searches) | Log search, event patterns |
| **DataDog**  | Metrics, Logs, Traces | Dashboards, APM, synthetic tests |

- Diagram: “How an alert moves from system → Splunk/DataDog → Geneos”
- Dashboards = *observability storytelling*. Are they telling you a bedtime story or a horror movie?

### Exercise:
- Navigate to an alert in Geneos → track its source → view related data in Splunk
- Identify what *pillar* that alert came from
- Screenshot or describe one dashboard and explain what it’s “saying”

---

## 🧠 Section 3: Anatomy of a Good Alert

**Goal:** Learners start to develop a nose for garbage alerts.

### Content:
- The Alert Lifecycle (Trigger → Notification → Triage → Resolution)
- Characteristics of a *useful* alert:
  - Tied to a user-facing issue
  - Actionable (clear remediation)
  - Not noisy (low false-positive rate)
  - Contextual (comes with breadcrumbs)

- Common sins:
  - Alert on *every* warning log. (Congratulations, your inbox is now an inferno.)
  - CPU > 90% for 2 seconds. (Wow, what a drama queen.)
  - Missing tags/context (e.g., “Alert on service xyz” — *which node?* *which region?*)

### Activity:
- Review 3 sample alerts (real or mocked up)
  - Identify what's missing or excessive
  - Rewrite one to make it more useful

---

## 🧩 Section 4: Beginner Troubleshooting Flow

**Goal:** Introduce a simple mental model for alert triage using observability.

### Content:
- “Red Alert Flowchart”:
  1. What’s the alert saying?
  2. What’s the related system/service?
  3. Check dashboard: Any anomalies in metrics?
  4. Check logs: Any error patterns?
  5. Check traces (if available): Any slow services?
- Start basic incident investigation

### Exercise:
- Given an alert:  
  > “API latency above 1s for service `payments-gateway`”  
  Learner walks through:
  - Which pillar(s) would you check first?
  - What questions would you ask?
  - Where would you go in the tooling?

---

## 🎯 End-of-Day Wrap-Up

**Review Questions:**
- What’s the difference between observability and monitoring?
- What are the three pillars?
- Which tools map to which data types?
- What makes a bad alert?
- How do you start investigating an alert using observability?

**Optional mini-quiz (4–5 questions):**  
Can be built later in BitBucket/Confluence, or Google Forms if you’re feeling dangerously modern.

---

## 🛠️ Materials Checklist (To Build After This)
- Slide deck outline (optional if you want to present this live)
- Example alerts (real or fake)
- Dashboard screenshots
- One small sample incident log bundle (can be fake)

---

That’s your Day One. No scope creep. Just the first brick.

Now, do you want:
- Help formatting this into a Confluence-friendly structure?
- The example alerts/dashboard descriptions mocked up?
- A follow-up guide for instructors/trainers to deliver it?

Pick your poison. I’ll be here, grumbling cheerfully.