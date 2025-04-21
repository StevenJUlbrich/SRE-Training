# 📊 Effective Querying Techniques: Splunk & Grafana Loki

*Intermediate SRE Logging Module: Deep Search Mastery for Observability Tools*

*With Johan as your query coach – no fluff, just fields.*

---

> **Johan's Thought:**
> *"Keyword search is for lost car keys, not production systems. Use your fields."*

---

## 🧭 Module Purpose

This section trains SREs to query logs like pros, not tourists. You’ll learn to:
- Move beyond keyword matches
- Write precise structured queries using SPL and LogQL
- Combine boolean logic for real-world problems
- Extract and use fields with regex
- Perform progressive triage across time, services, and severity

Covered tools:
- **Splunk (SPL)**
- **Grafana Loki (LogQL)**

---

## 🛠️ Structured vs. Unstructured Searching

**Structured logs** let you filter logs by fields. This is faster, more reliable, and reduces noise.

Unstructured:
```text
"error checkout payment"
```

Structured:
```spl
index=app_logs service="checkout" level="error"
```

> **Johan’s Prompt:**
> “What do you trust more in an incident—wildcard search or a field match with `trace_id`?”

---

## 🔎 Field-Based Filtering in Practice

Structured log fields may include:
- `level`
- `service`
- `trace_id`
- `env`
- `user_id`

### SPL Example:
```spl
index=prod_logs sourcetype=json_logs service="cart" level="warn"
```

### LogQL Example:
```logql
{app="payments", level="error"} |= "timeout"
```

### Field Aliasing:
- In SPL: `eval new_field=old_field`
- In Loki: `label_replace()` for field transformation

> **🧪 Practice:** Write a query that filters logs for the `auth` service, with level `warn`.

---

## 🔗 Boolean Logic: AND, OR, NOT

### Scenario:
You're looking for failed requests to the payment service, but NOT retries.

### SPL:
```spl
index=prod_logs service="payment" AND level="error" NOT message="retry"
```

### LogQL:
```logql
{job="payment", level="error"} |= "error" != "retry"
```

> **Self-Check:**
> “What does this query do?
> ```spl
> (service="api" OR service="gateway") AND level="error"
> ```”
>
> ✅ *Finds all errors from both services.*

> **🧪 Practice:** Write a SPL query that finds errors in `inventory` or `billing`, excluding those with status code `200`.

---

## ⏲️ Time Filtering & Context Windows

**Use time windows** to:
- Zoom in on incident windows
- Reduce query cost
- Improve relevance

### SPL:
```spl
index=logs earliest=-1h latest=now service="checkout"
```

### LogQL:
Set in Grafana UI or wrap in a query:
```logql
{service="checkout"} |= "failed"
```

> **🧰 Visual Aid:**
> Imagine a funnel: the top is all logs. Time filtering is the first narrowing ring. Field filters narrow it more. Final search terms filter the output stream.

---

## 🎯 Deep Debugging Walkthrough

> **Incident:** Checkout failures are rising. A trace ID (`abc123`) ties a request to the payment service.

1. **Find Logs by Trace ID**
```spl
index=prod_logs trace_id="abc123"
```

2. **Filter to Relevant Span/Service**
```spl
service="payment" trace_id="abc123" AND level="error"
```

3. **Check Retry Patterns**
```spl
"retry" OR "attempt" trace_id="abc123"
```

4. **Cross-Service Correlation**
```spl
(trace_id="abc123") AND (service="api" OR service="payment")
```

5. **Regex Extraction (SPL):**
```spl
| rex "status=(?<http_status>\d{3})"
```

---

## 🔍 Regex Matching and Extraction

Use regex to extract structured data from logs.

### 🔠 Named Capture Group Explained:
```spl
| rex field=_raw "user=(?<user_id>\d+)"
```
- `(?<user_id>\d+)` = create a field named `user_id`, capturing digits only

### LogQL Example:
```logql
{job="cart"} |~ "user=\d+"
```

### Common Patterns:
- Email: `email=(\S+)`
- Status Code: `status=(\d{3})`
- Latency: `latency=(\d+ms)`

> **🧪 Practice:** Write a regex to extract a `request_id` from a log line that looks like `req_id=XYZ123`

---

## 🔬 Tool Comparison Table

| Feature | Splunk SPL | Grafana LogQL |
|---------|------------|----------------|
| Field Filtering | ✅ | ✅ |
| Regex Extraction | ✅ (`rex`) | ✅ (`|~`) |
| Time Range Control | ✅ (`earliest`, `latest`) | ✅ (UI + inline) |
| Live Tail | ✅ | ✅ |
| Saved Queries | ✅ | ✅ |

---

## 📦 Scenario-Based Drill – Auth Failures

> **🧪 Scenario:** Users in EU region report authentication failures. Trace IDs show involvement from both `auth` and `proxy` services.
>
> Craft a query that:
> - Filters the last hour
> - Matches error-level logs
> - Involves either service
> - Shows only non-200 status codes

**Sample SPL Solution:**
```spl
index=auth_logs earliest=-1h latest=now (service="auth" OR service="proxy") level="error" NOT status="200"
```

**Revised LogQL Solution:**
```logql
{service=~"auth|proxy", level="error"} |= "status" != "status=200"
```

> **Explanation:** `|= "status"` matches lines that include the string "status". `!= "status=200"` excludes exact status match logs. It’s safer to extract and filter explicitly when logs are unstructured.

---

## 📘 Glossary

| Term | Definition |
|------|------------|
| **SPL** | Splunk Processing Language |
| **LogQL** | Grafana's query language for logs |
| **Field filter** | Search using specific key-value pairs |
| **Regex** | Pattern-matching language for strings |
| **Named capture group** | A syntax in regex for extracting named fields: `(?<fieldname>pattern)` |
| **Trace ID** | Identifier linking logs across services in one request |

---

> **Johan’s Final Thought:**
> *“Logs aren’t strings—they’re structured signals. Query like your uptime depends on it.”*

---

📅 **End of Module – Effective Querying Techniques**

