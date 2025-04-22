# 🧠 End-of-Series Quiz: Advanced Logging for SREs

*Test your understanding across the advanced logging modules. Choose the best answer or provide the most accurate explanation based on your training.*

---

## 📘 Section 1: Log Levels, Filtering, and Sampling

**1.** Which log level is typically NOT recommended in production?
- A) INFO
- B) WARN
- C) DEBUG
- D) ERROR

**2.** True or False: Filtering logs at the agent level reduces ingestion cost and helps improve backend performance.

**3.** What is the purpose of log sampling?
- A) To prioritize errors
- B) To delete older logs
- C) To reduce volume by logging a percentage of high-frequency events
- D) To identify data corruption

**4.** Given the line below, which Fluent Bit feature would you use to exclude it?
```
GET /healthz
```
- A) Parser
- B) Sampler
- C) Grep filter
- D) Multiline handler

**5.** Match the log level to its purpose:
- 1. DEBUG
- 2. INFO
- 3. ERROR
- 4. WARN

| Level | Purpose                        |
|-------|---------------------------------|
| A     | Unexpected, recoverable issue  |
| B     | Detailed diagnostic data       |
| C     | High-level operational info    |
| D     | Failure requiring investigation |

---

## 💸 Section 2: Retention & Storage Strategy

**6.** Fill in the blank: `Hot storage` is best used for _______.

**7.** A 1TB log archive costs ~$150/month in Elasticsearch (hot). What is the estimated cost if moved to S3 (cold)?
- A) $300
- B) $100
- C) $30
- D) $10

**8.** Which retention policy would best balance cost and searchability for non-critical INFO logs?
- A) Retain for 90 days in hot tier
- B) Retain 7 days hot, 30 days cold
- C) Keep 100% in archive only
- D) Retain 3 years in hot storage

---

## 🔗 Section 3: Trace ID & Correlation

**9.** A `trace_id` links together:
- A) Only metrics from the same time window
- B) Logs from different services involved in a request
- C) All users in the same session
- D) Logs and config changes

**10.** What is a “span” in tracing?
- A) A visual dashboard component
- B) A type of structured log
- C) A unit of work inside a trace
- D) A metric tag

**11.** True or False: Every span has a `trace_id`, but not every log automatically includes one.

**12.** You see an error in service B, but no trace ID. What’s your best next step?
- A) Wait for another error
- B) Check timestamps in service A for similar activity
- C) Restart the service
- D) Raise a Sev-1

**13.** Fill in the blank: A metric points to where to look, a log shows what happened, and a _______ reveals the full journey.

---

## 🔐 Section 4: Security & Audit Logging

**14.** Which of the following should **never** be logged?
- A) user_id
- B) error message
- C) password
- D) service name

**15.** A log like this:
```
email=user@example.com password=12345
```
is:
- A) Safe because it’s encrypted
- B) Useful for debugging
- C) A compliance violation
- D) Normal in dev logs

**16.** Which practice ensures that audit logs are trustworthy?
- A) Rotating them every hour
- B) Allowing only read-write access
- C) Making them immutable
- D) Storing them in plaintext

---

## 🔁 Section 5: Putting It All Together

**17.** What strategy combines correlation and cost control?
- A) Logging at DEBUG everywhere
- B) Linking trace_id across sampled logs
- C) Filtering metrics before logging
- D) Logging all request bodies in real time

**18.** When is it most helpful to switch a log level from INFO to DEBUG in production?
- A) During routine health checks
- B) During incident investigation
- C) During team meetings
- D) During low traffic hours

**19.** Select all that apply: Which fields are most helpful for log enrichment?
- [ ] timestamp
- [ ] team
- [ ] user password
- [ ] trace_id
- [ ] service

**20.** Final question (short answer):
You’re asked to reduce log cost without losing critical visibility. Name **three** strategies you’d recommend based on this training.

---

📅 **End of Quiz – Advanced Logging for SREs**

