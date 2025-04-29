# Appendix – Practical Worksheets & Resources

---

## A. SLI / SLO Worksheets  

| File                      | Purpose                               | Link                                                                         |
| ------------------------- | ------------------------------------- | ---------------------------------------------------------------------------- |
| **Blank template**        | Copy-start YAML for any service SLO.  | [Download the YAML template](sandbox:/mnt/data/slo_blank.yaml)               |
| **Fund-transfer example** | Real, contract-compliant latency SLO. | [Download the example YAML](sandbox:/mnt/data/slo_example_fund_latency.yaml) |

**How to use**

1. Download *slo_blank.yaml*.  
2. Fill in `<service-name>`, objective, time-window, and PromQL queries.  
3. Commit to `slo/` and run `sloth generate` to produce Prometheus rules.

---

## B. Error-Budget Calculators  

| File                     | Format                         | Link                                                             |
| ------------------------ | ------------------------------ | ---------------------------------------------------------------- |
| Calculator (spreadsheet) | `.xlsx` with editable formulas | [Download Excel](sandbox:/mnt/data/error_budget_calculator.xlsx) |
| Quick-calc (CSV)         | Plain values & formula text    | [Download CSV](sandbox:/mnt/data/error_budget_calculator.csv)    |

Open **Excel** ► enter:

* **A2** – SLO objective (e.g., 99.9)  
* **B2** – window in days  
* **C2** – total requests in window  

Cells **D2** & **E2** auto-compute remaining requests / seconds you can afford to fail—use them in burn-rate rules.

---

## C. Tool-Configuration Examples  

```yaml
# --- Prometheus scrape & recording rule (excerpt) ---
scrape_configs:
  - job_name: fund-transfer
    static_configs: [{targets: ['fund-api:443']}]

recording_rules.yml:
- record: fund_latency_p99
  expr: histogram_quantile(0.99,
        sum(rate(fund_transfer_latency_seconds_bucket[5m])) by (le))
```

```yaml
# --- Sloth SLO YAML ➜ Prom rules ---
service: fund-transfer
slo:
  name: "p99 latency <= 300 ms"
  objective: 99.9
  time_window: 30d
  sli:
    events:
      total_query: sum(rate(http_requests_total[5m]))
      error_query: sum(rate(latency_gt_300ms_total[5m]))
```

```yaml
# --- Alertmanager webhook & Slack template ---
receivers:
- name: sre-oncall
  slack_configs:
    - channel: '#sre-oncall'
      title: '{{ .CommonLabels.alertname }}'
      text: |
        *Budget left*: {{ .CommonAnnotations.budget_left }}
        <{{ .CommonAnnotations.trace_url }}|View trace>
      send_resolved: true
  webhook_configs:
    - url: 'https://autosre.bank/webhook'
```

---

## D. Further Learning Resources  

| Resource                          | Type          | Link                                     |
| --------------------------------- | ------------- | ---------------------------------------- |
| *Site Reliability Workbook*       | Book (Google) | https://sre.google/books/                |
| *Practical Monitoring* (L. Gregg) | Book          | https://practicalmonitoring.com          |
| SREcon EMEA playlist              | Conf. Talks   | https://www.usenix.org/conference/srecon |
| Google Coursera SRE course        | Free MOOC     | https://www.coursera.org/learn/sre       |

---

### Learner Prompt  

Download **slo_blank.yaml**, write an SLO for your most critical API, and run `sloth generate`. Post the resulting Prom rules for peer review.

---

## Appendix Audit ✔️

* All four downloadable resources exist and are linked.  
* YAML templates follow contract field names.  
* Spreadsheet formulas auto-calculate budgets.  
* Examples referenced earlier in Chapters 3, 7, 9.  
* No contract-required image panels; appendix is exempt.

The appendix is ready for publication.