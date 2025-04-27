Below is an updated **Answer Sheet** in a narrative format—each numbered item repeats the original quiz question, then gives the answer, Mei’s quick rationale, and a short explanation with concrete file-path or scenario references.

---

### 1 . In the 5-Question Drill, which question must you answer **before** contacting an escalation team?  
**Answer — OWNER?**  
*Mei:* “Page the right human—​not *any* human.”  
**Why:** Without the `owner` label you may wake the wrong rota and waste time. (Beginner §3.3)

---

### 2 . **True or False:** A P2 alert in production with `impact=error_spike` should route directly to **sre-primary**.  
**Answer — False**  
*Mei:* “Local problems → local teams.”  
**Why:** The routing matrix (Intermediate §3.1) sends a P2 + `error_spike` to `team-$service`, reserving `sre-primary` for P1 outages.

---

### 3 . What is the very first habit Mei recommends at the start of every shift?  
**Answer — Check the recent deploy feed.**  
*Mei:* “Find the breadcrumb before the trail goes cold.”  
**Why:** 70-80 % of incidents correlate with a fresh deploy. (Beginner §2)

---

### 4 . Name **two** common Tool Integrations that production-support engineers rely on.  
**Answer (any two):** Monitoring systems, Alerting platforms, Ticketing systems, Knowledge bases, Communication tools.  
*Mei:* “Tools must integrate so people can collaborate.”  
**Why:** Listed under Tool Integration bullets.

---

### 5 . In Grafana Jsonnet templates, which three RED metrics are typically visualized?  
**Answer — Rate, Errors, Duration (p95).**  
*Mei:* “RED keeps the signal simple.”  
**Why:** Shown in `red.jsonnet` template (Intermediate §1.3).

---

### 6 . Which metadata **label** is required in every alert to support routing and deduplication?  
**Answer — `service`**  ( `owner` is also acceptable).  
*Mei:* “No service tag, no smart grouping.”  
**Why:** `service` groups alerts and feeds the routing matrix. (Intermediate §3.1)

---

### 7 . You see `checkout_latency_p95` spike and a deploy feed shows `checkout-service v2.4.0` four minutes earlier. According to the Beginner workflow, what’s your **next** step after confirming the recent change?  
**Answer — Determine scope/impact of the alert.**  
*Mei:* “Know how many users bleed before you apply the bandage.”  
**Why:** Step 3 of the 5-Question Drill is SCOPE. (Beginner §3.4 example)

---

### 8 . What **file path** would you place a Datadog dashboard template in, according to the Intermediate IaC matrix?  
**Answer — `infra/datadog/dashboard_checkout.tf`.**  
*Mei:* “Templates live where code reviewers can see them.”  
**Why:** IaC matrix shows HCL files in `infra/datadog/`. (Intermediate §1.2)

---

### 9 . **Fill-in-the-blank:** A *Spike* load test is designed to create a sudden **5×** increase in traffic.  
**Answer — 5×**  
*Mei:* “Short shock, big reveal.”  
**Why:** Load-test type table (SRE §3.1).

---

### 10 . Which OpenTelemetry key allows Prometheus, Splunk, and Datadog to correlate data in a single Grafana panel?  
**Answer — `trace_id`.**  
*Mei:* “One ID to join them all.”  
**Why:** Mixed-datasource panel uses `$trace`. (Intermediate §2.2)

---

### 11 . List **one** mitigation strategy for **Secret Rotation** in self-healing automation.  
**Answer example:** Store PagerDuty/Grafana tokens in a CI vault and rotate them monthly via job `rotate-pd-key.yml`.  
*Mei:* “Rotate keys before attackers do.”  
**Why:** Secret-rotation row in SRE challenges table (SRE §4).

---

### 12 . During a chaos drill, what metric forms the **Steady State** for the checkout flow in the template example?  
**Answer — `checkout_latency_p95`.**  
*Mei:* “Measure what the customer feels.”  
**Why:** Chaos experiment template lists that steady-state metric. (SRE §2.1)

---

### 13 . Why must all self-healing remediation scripts be **idempotent**?  
**Answer — So repeated runs don’t create new failures or double-rollbacks.**  
*Mei:* “A fix that breaks on retry isn’t a fix.”  
**Why:** Idempotency rule with Redis lock example. (SRE §1.4)

---

### 14 . **True or False:** A Redis lock on `rollback:$env` is used to guarantee only one rollback runs at a time.  
**Answer — True.**  
*Mei:* “Concurrency kills safety; locks restore it.”  
**Why:** Listed under Idempotent Rollbacks mitigation. (SRE §4)

---

### 15 . Which monthly CI job trends max RPS versus CPU to avoid “Capacity Trend Blindness”?  
**Answer — `capacity-trend.yml`.**  
*Mei:* “Graphs reveal slow rot.”  
**Why:** k6 script section references the job name. (SRE §3.2)

---

### 16 . Give **one** reason why dashboards stored only in a UI (not Git) are risky.  
**Answer example:** Silent drift—pixel edits aren’t diffed or reviewed.  
*Mei:* “If it isn’t in Git, it isn’t under control.”  
**Why:** Risks listed in Intermediate §1.1.

---

### 17 . In the Beginner priority matrix, what immediate action is required for a **P3** alert?  
**Answer — Schedule investigation / create a ticket.**  
*Mei:* “Minor now, but don’t lose the thread.”  
**Why:** P3 row in matrix (Beginner §3.2).

---

### 18 . What is the main purpose of the **Blast Radius** field in a chaos experiment?  
**Answer — Limit customer impact by constraining the experiment’s scope (e.g., 5 % traffic, one region).**  
*Mei:* “Blow up a sandbox, not the stadium.”  
**Why:** Chaos template field definition (SRE §2.1).

---

### 19 . According to Mei, what is the ultimate measure of MTTR success for self-healing alerts?  
**Answer — The alert resolves without paging a human.**  
*Mei:* “Zero-page incidents: sleep gained, MTTR near zero.”  
**Why:** Stated as “ultimate win” in SRE §1.

---

### 20 . When writing a blameless PIR, list any **three** sections besides the timeline.  
**Answer (any three):** Detection, Mitigation, Root Cause(s), Action Items.  
*Mei:* “Timeline shows what; sections show why and how we’ll improve.”  
**Why:** PIR template fields (SRE §4.1).

---

*End of enhanced answer sheet – with Mei’s on-call wisdom baked in.*