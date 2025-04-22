# ✅ Answer Key: Advanced Logging for SREs

Use this answer sheet to assess learner understanding. Each question includes the correct answer, explanation, and reasoning for incorrect options.

---

## 📘 Section 1: Log Levels, Filtering, and Sampling

**1. Which log level is typically NOT recommended in production?**  
✅ C) DEBUG  
**Explanation:** DEBUG is too verbose for production and often contains sensitive or unnecessary detail.  
- A) INFO → Often used in production to log general activity.  
- B) WARN → Used to indicate recoverable but important conditions.  
- D) ERROR → Essential for surfacing failures.

**2. True or False: Filtering logs at the agent level reduces ingestion cost and helps improve backend performance.**  
✅ True  
**Explanation:** Reduces the volume sent to log stores, saving cost and improving system performance.

**3. What is the purpose of log sampling?**  
✅ C) To reduce volume by logging a percentage of high-frequency events  
**Explanation:** Sampling allows for reduced volume while still capturing representative data.  
- A) Prioritizing errors is useful, but not related to sampling.  
- B) Deleting older logs is part of retention, not sampling.  
- D) Identifying data corruption is not the goal of sampling.

**4. Given the line below, which Fluent Bit feature would you use to exclude it?**
```
GET /healthz
```
✅ C) Grep filter  
**Explanation:** Grep filters match log content and exclude unwanted entries.  
- A) Parser → Used to structure log fields.  
- B) Sampler → Controls log volume but not based on pattern.  
- D) Multiline handler → Handles stack traces or line grouping.

**5. Match the log level to its purpose:**
- 1. DEBUG → B) Detailed diagnostic data  
- 2. INFO → C) High-level operational info  
- 3. ERROR → D) Failure requiring investigation  
- 4. WARN → A) Unexpected, recoverable issue  
**Explanation:** These definitions align with standard logging practices and help teams prioritize log severity.

---

## 💸 Section 2: Retention & Storage Strategy

**6. Fill in the blank: `Hot storage` is best used for _______.**  
✅ Real-time search, monitoring, or alerting  
**Explanation:** Hot storage is optimized for speed, not for long-term retention.

**7. A 1TB log archive costs ~$150/month in Elasticsearch (hot). What is the estimated cost if moved to S3 (cold)?**  
✅ C) $30  
**Explanation:** S3 cold storage is roughly 5x–10x cheaper than hot storage.  
- A/B) Too expensive.  
- D) Glacier may be cheaper, but not typical for cold-tier access.

**8. Which retention policy would best balance cost and searchability for non-critical INFO logs?**  
✅ B) Retain 7 days hot, 30 days cold  
**Explanation:** Preserves recent logs for quick search while archiving older data affordably.  
- A) Too expensive.  
- C) Archive-only loses accessibility.  
- D) 3 years hot is excessive for INFO logs.

---

## 🔗 Section 3: Trace ID & Correlation

**9. A `trace_id` links together:**  
✅ B) Logs from different services involved in a request  
**Explanation:** Enables multi-service observability.  
- A) Metrics are correlated by time/labels.  
- C) Session ID handles user scope, not tracing.  
- D) Configs don’t relate to tracing.

**10. What is a “span” in tracing?**  
✅ C) A unit of work inside a trace  
**Explanation:** A span captures timing and metadata about an operation.  
- A) Dashboard components are visualizations.  
- B) Logs are separate from spans.  
- D) Metrics use tags, not spans.

**11. True or False: Every span has a `trace_id`, but not every log automatically includes one.**  
✅ True  
**Explanation:** Without instrumentation, logs won’t include trace context.

**12. You see an error in service B, but no trace ID. What’s your best next step?**  
✅ B) Check timestamps in service A for similar activity  
**Explanation:** Timestamps help trace flows manually.  
- A) Waiting delays response.  
- C) Restarting may worsen the issue.  
- D) Not Sev-1 without scope.

**13. Fill in the blank: A metric points to where to look, a log shows what happened, and a _______ reveals the full journey.**  
✅ Trace  
**Explanation:** Traces connect services and span relationships.

---

## 🔐 Section 4: Security & Audit Logging

**14. Which of the following should **never** be logged?**  
✅ C) password  
**Explanation:** Exposing passwords violates all major compliance policies.  
- A) user_id → OK if anonymized.  
- B) error message → Acceptable if scrubbed.  
- D) service name → Generally safe.

**15. A log like this:**
```
email=user@example.com password=12345
```
**is:**  
✅ C) A compliance violation  
**Explanation:** This would be flagged by any security audit.  
- A) Encryption is irrelevant post-log.  
- B) “Helpful” is not safe.  
- D) Even dev logs need hygiene.

**16. Which practice ensures that audit logs are trustworthy?**  
✅ C) Making them immutable  
**Explanation:** Immutability supports legal and forensic use.  
- A) Rotation improves retention, not trust.  
- B) Read-write invites tampering.  
- D) Plaintext is insecure.

---

## 🔁 Section 5: Putting It All Together

**17. What strategy combines correlation and cost control?**  
✅ B) Linking trace_id across sampled logs  
**Explanation:** Balances observability with data reduction.  
- A) DEBUG logs are too noisy.  
- C) Filtering metrics before logging doesn’t address correlation.  
- D) Logging bodies inflates volume and may violate compliance.

**18. When is it most helpful to switch a log level from INFO to DEBUG in production?**  
✅ B) During incident investigation  
**Explanation:** Helps during RCA without leaving DEBUG on all the time.  
- A/C/D) Provide no diagnostic value.

**19. Select all that apply: Which fields are most helpful for log enrichment?**  
✅ timestamp, team, trace_id, service  
❌ Incorrect: user password → Never log sensitive fields

**20. Final question (short answer):**  
✅ Sample acceptable answers (any 3 of the following):
- Implement sampling for high-frequency events
- Adjust log levels to exclude DEBUG in prod
- Filter `/healthz` or non-critical endpoints at the agent
- Store logs with tiered retention (hot → cold → archive)
- Mask/redact sensitive data at log ingestion

---

📘 **End of Answer Sheet**

