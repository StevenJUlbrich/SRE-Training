# Chapter 1

### 🎯 Learning Objective  
Contrast reactive heroics with measurable reliability and introduce the contract compass.

### ✅ Takeaway  
Host-centric charts make you feel safe until a single user‐journey fails; only user-level metrics reveal the truth.

### Teaching Narrative  
:::wisdom  
**SRE Wisdom:** “Stability isn’t green graphs—it’s silent customers.”  
:::  

**Scene (30 %)** Nairobi sunrise: indigo tinted towers. Ava lifts her *Reliability you can measure* mug.

**Technical (70 %)**

1. **Compass pattern**

   ```text
   Teaching Narrative ─▶ Image Embed ─▶ Teaching Narrative ─▶ …
   ```

   Contract enforces this to avoid wall-of-text or comic without context.

2. **Why user-journey metrics**

   *Symptom:* gRPC API returns `DeadlineExceeded` at client, while NOC sees 0 % errors.  
   *Root cause:* dashboard watches `grpc_server_finished_total{grpc_code="OK"}`— but retries mask 502s.

3. **Immediate fix**

   ```promql
   # Success from the user's lens (includes retries)
   sum(rate(grpc_client_finished_total{grpc_code="OK"}[5m]))
   /
   sum(rate(grpc_client_finished_total[5m]))
   ```

4. **Mini-exercise**

   :::exercise  
   Export `grpc_client_finished_total` from one micro-service, add the query above to Grafana, and record the delta vs. server-side success for 24 h.  
   :::

### Image Embed  
Image Embed:  
```yaml
panel_id: 1
```  
![Ava greets you on a Nairobi rooftop at sunrise](images/ch01_p01_rooftop_intro.png){width=550px}

---

### 🎯 Learning Objective  
Show banking’s expectation shift from branch queues to 24 × 7 mobile journeys.

### ✅ Takeaway  
Latency perceived at the client is the new line length; every 100 ms over p99 costs measurable revenue.

### Teaching Narrative  
**Scene (25 %)** Split illustration: velvet-rope branch in 1985; mobile app spinner failing in 2025.

**Technical (75 %)**

* **Cost curve:** Internal Matunda analysis shows mobile basket-abandon probability `P_abandon ≈ 1 – e^(–0.8*(t − 1.2 s))` for `t > 1.2 s`.  
* **Target derivation:** To keep churn < 3 %, we need p99 < 1.8 s.  
* **Measurement technique**

  ```mermaid
  sequenceDiagram
    autonumber
    participant SDK
    participant API
    Note over SDK: t0
    SDK->>API: POST /loan
    API-->>SDK: 200 json
    Note over SDK: t1; latency = t1−t0
  ```

* **Prometheus histogram choice**

  ```yaml
  buckets: [0.2,0.4,0.8,1.2,1.6,1.8,2,3,5]
  ```

  Avoid default 10 s bucket; it flattens the critical 1–2 s range.

### Image Embed  
Image Embed:  
```yaml
panel_id: 2
```  
![Split scene of bank queue vs phone payment failure](images/ch01_p02_branch_split.png){width=550px}

---

### 🎯 Learning Objective  
Prove hero culture’s hidden costs and introduce MTBU (Mean Time Between Unacceptable behaviour).

### ✅ Takeaway  
Chasing MTTR trophies without MTBU targets drains teams and budgets.

### Teaching Narrative  
**Scene (30 %)** Red pager lights; uptime banner; Ava wrist-slap.

**Technical (70 %)**

* **Metric definition**

  ```text
  MTBU = (observation window) ÷ (# of user-visible incidents)
  Acceptable target: 30 d / 1 = 30 days
  ```

* **Post-incident checklist**

  1. Identify **unacceptable behaviour** (SLO breach, not host alert).  
  2. Record start/stop via SLO burn-rate.  
  3. Log change-causality (git SHA, K8s rollout, infra patch).  

* **Alert fatigue math**

  ```python
  alerts_per_engineer_per_shift = total_alerts / (oncall * shifts)
  if alerts_per_engineer_per_shift > 6:
      raise "Desensitisation risk"
  ```

* **Widget**

  :::slap  
  *Wrist-Slap Moment:* “Average latency? Amateur hour—show p95/p99.”  
  :::

### Image Embed  
Image Embed:  
```yaml
panel_id: 3
```  
![War-room burnout, Ava wrist-slaps uptime banner](images/ch01_p03_hero_burnout.png){width=550px}

---

### 🎯 Learning Objective  
Map the SRE staircase and connect each riser to a measurable signal.

### ✅ Takeaway  
Progress only counts when each new habit adds an SLI or removes alert noise.

### Teaching Narrative  
**Scene (25 %)** Team climbing labelled stairs.

**Technical (75 %)**

| Riser | New habit | Required metric | Quick start |
|-------|-----------|-----------------|-------------|
| Incident Response | On-call rota | Alert-ack ≤ 5 min | — |
| Monitoring | RED/USE dashboards | `http_requests_total`, `node_cpu_seconds_total` | kube-prom-stack |
| Testing | Load + chaos tests | Error-budget burn in staging | Litmus Chaos |
| Prevention | Blameless RCAs | MTBU trending up | Incident.io export |
| Design for Reliability | SLO gates in CI/CD | `slo:cli verify` step | Sloth |

* **CI example**

  ```yaml
  - name: verify-slo
    run: slo verify --input slis.yaml --window 30d
  ```

* **Try This**

  :::exercise  
  Add a `verify-slo` stage to one GitHub Actions workflow; fail build if error-budget usage > 20 %.  
  :::

### Image Embed  
Image Embed:  
```yaml
panel_id: 4
```  
![Ava leads team up metric-labelled staircase](images/ch01_p04_sre_stairs.png){width=550px}

---

### 🎯 Learning Objective  
Define SLIs rigorously and compute p99 latency with exemplars.

### ✅ Takeaway  
An SLI is worthless until you can query it, alert on it, and link it to user impact.

### Teaching Narrative  
**Scene (20 %)** Phone overlay with thermometer; red latency bar.

**Technical (80 %)**

* **SLI schema (Sloth)**

  ```yaml
  - name: payment_latency_lt_1800ms
    description: p99 latency for loan-payment journey < 1.8s
    sli: |
      histogram_quantile(0.99,
        sum(rate(journey_latency_bucket[5m])) by (le))
    objectives:
      - target: 99.0
        time_window: 30d
  ```

* **Client-side RUM beacon**

  ```javascript
  window.addEventListener('load', () => {
    const t = performance.timing;
    fetch('/rum', {method:'POST',
      body: JSON.stringify({dur: t.loadEventEnd - t.navigationStart})});
  });
  ```

* **Grafana transformation**  
  Panel → “Error Budget Meter” plugin; bind to SLO burn.

* **Nairobi proverb widget**

  :::proverb  
  *“Mti ulio na matunda ndiyo hupigwa mawe.”*  
  (The tree with fruit is the one that gets stoned.)  
  — Valuable services attract load; SLI them first.  
  :::

### Image Embed  
Image Embed:  
```yaml
panel_id: 5
```  
![Phone overlay shows SLI thermometer and red latency bar](images/ch01_p05_sli_phone_overlay.png){width=550px}

---

Below is **Part B** of **chapter01.md** (Units 6 – 10) plus the chapter self-check table.  
It follows the updated contract: “Teaching Narrative” heading, 70 % technical / 30 % scene, widgets within whitelist, Image Embed stanza with `panel_id`, and immediate Markdown image line.

---

### 🎯 Learning Objective  
Translate service-level **objectives** into enforceable, business-aligned promises.

### ✅ Takeaway  
An SLO is a contract: target + window + measurement method. Omit one, and lawyers (or customers) fill in the blanks.

### Teaching Narrative  
**Scene (25 %)** Executive boardroom; Ava writes “99.9 % in 30 d” on digital whiteboard.

**Technical (75 %)**

* **3-part SLO formula**  

  `Target` (e.g., 99.9 %)   ×  `Time-window` (rolling 30 d)   ×  `SLI` query.

* **PromQL windowed numerator/denominator**

  ```promql
  # Good events (latency < 1.8 s)
  good = sum_over_time(journey_latency_count{le="1.8"}[30d])
  total = sum_over_time(journey_latency_count[30d])
  objective = good / total
  ```

* **CI gate**

  ```bash
  burn=$(sloctl burn-rate --slo payment_latency --window 30d)
  if (( $(echo "$burn > 0.90" | bc -l) )); then exit 1; fi
  ```

* **Error-Budget meter widget**

  :::budget  
  Burn rate = 0.35 × → 65 % budget remaining.  
  :::

### Image Embed  
Image Embed:  
```yaml
panel_id: 6
```  
![Contract icon and stopwatch as Ava sets an SLO](images/ch01_p06_slo_contract.png){width=550px}

---

### 🎯 Learning Objective  
Operationalise **error budgets** as a throttle on deployment velocity.

### ✅ Takeaway  
Velocity and reliability are not foes; the error-budget dial reconciles them.

### Teaching Narrative  
**Scene (30 %)** Ava tip-toes a tight-rope labelled “Innovation ↔ Stability,” piggy-bank net below.

**Technical (70 %)**

* **Budget arithmetic**  

  `Allowed error minutes = (1 – target) × window_duration`  

* **Burn-rate alert (multi-window)**  

  ```yaml
  - alert: PaymentLatency_Burn
    expr: sli:ratio_rate5m < 0.999
    for: 2m
  - alert: PaymentLatency_Burn_Slow
    expr: sli:ratio_rate1h < 0.999
    for: 1h
  ```

  PagerDuty triggers only when both fire → noise down 80 %.

* **Auto-deploy hook**

  ```bash
  if sloctl budget --remain < 0.2; then
      gh workflow disable deploy.yml
  fi
  ```

* **Widget**

  :::slap  
  “Deploying while budget is 0 % is like driving on E with no spare—stop.”  
  :::

### Image Embed  
Image Embed:  
```yaml
panel_id: 7
```  
![Ava balances on tight-rope with piggy-bank net](images/ch01_p07_error_budget_tightrope.png){width=550px}

---

### 🎯 Learning Objective  
Explain banking-specific reliability constraints and regulatory ties.

### ✅ Takeaway  
For financial systems, “good enough” is codified by regulators—SLOs must meet or exceed those thresholds.

### Teaching Narrative  
**Scene (20 %)** Towering stacks of compliance binders dwarf Ava.

**Technical (80 %)**

* **Example: CBK Risk Management Guideline 5.2** – “Payment systems must be available ≥ 99.9 %, measured monthly.”  
* **Mapping to SLO**

  ```yaml
  - target: 99.95   # stretch above legal min
    time_window: 30d
    sli: availability_ratio
  ```

* **Deployment calendar** – freeze windows on fiscal close (end-month + tax deadlines).  
* **Auditable log**

  ```sql
  INSERT INTO sla_compliance(slo_id, period_end, achieved)
  VALUES('payment_latency_99p','2025-04-30',0.9993);
  ```

* **Proverb widget**

  :::proverb  
  *“Hasira, hasara.”* (Anger is loss.)  
  Rushing a deploy during close period costs twice.  
  :::

### Image Embed  
Image Embed:  
```yaml
panel_id: 8
```  
![Ava dwarfed by banking regulations binders](images/ch01_p08_compliance_tower.png){width=550px}

---

### 🎯 Learning Objective  
Introduce the SRE **tooling toolbox** and show a minimal stack.

### ✅ Takeaway  
Choose one source of truth per telemetry type: Prometheus (metrics), Loki (logs), Tempo (traces).

### Teaching Narrative  
**Scene (25 %)** Workshop bench with labelled tools; Ava hands a PromQL wrench to a junior.

**Technical (75 %)**

| Pillar | OSS Tool | 15-min quick-start |
|--------|----------|--------------------|
| Metrics | **Prometheus** | `docker run prom/prometheus` |
| Dashboards | **Grafana** | `helm install grafana grafana/grafana` |
| Logs | **Loki** | `helm install loki grafana/loki-distributed` |
| Traces | **Tempo** | `helm install tempo grafana/tempo-distributed` |
| K8s SLO operator | **Sloth** | `kubectl apply -f sloth.yaml` |

* **Diagram widget**

  :::diagram  
  ```mermaid
  graph TD
    App -->|metrics| Prom
    App -->|logs| Loki
    App -->|traces| Tempo
    Prom --> Grafana
    Loki --> Grafana
    Tempo --> Grafana
  ```  
  :::

### Image Embed  
Image Embed:  
```yaml
panel_id: 9
```  
![Workshop of labelled SRE tools](images/ch01_p09_toolbench.png){width=550px}

---

### 🎯 Learning Objective  
Lay out the roadmap for Chapters 2 – 12 and connect each to learner outcomes.

### ✅ Takeaway  
Readers should anticipate progression: metrics → SLO governance → tracing → incident command → culture.

### Teaching Narrative  
**Scene (30 %)** Road sign with milestones; Ava points forward.

**Technical (70 %)**

*Upcoming chapters*  

1. **Metrics Deep-Dive** – RED/USE, histogram hygiene.  
2. **SLO Governance** – error-budget policy.  
3. **Tracing Mastery** – Tempo + exemplars.  
4. **Incident Command** – IM protocol, ChatOps.  
5. **Culture & Ownership** – blameless RCA patterns.

* **Try This widget**

  :::exercise  
  Open your backlog; tag any ticket that lacks a measurable SLI reference. Aim for 100 % linkage before Chapter 3.  
  :::

### Image Embed  
Image Embed:  
```yaml
panel_id: 10
```  
![Roadmap sign with upcoming chapter milestones](images/ch01_p10_roadmap.png){width=550px}

---

