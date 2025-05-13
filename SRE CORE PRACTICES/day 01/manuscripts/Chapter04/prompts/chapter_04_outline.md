## Chapter 4 – “You’re Not Alerting — You’re Alarming”

### 🧠 Primary Concept

**Alerting must prioritize user impact, not machine behavior.** Thresholds don’t protect customers—intentional alert design does.

______________________________________________________________________

### 🧩 Key Terms Introduced

- Burn rate
- SLO-based alerting
- Alert fatigue
- Error budget consumption
- Multi-window alerting

______________________________________________________________________

### 📊 Teaching Objective

Learners should walk away understanding:

- Why static thresholds generate alert noise
- How burn rate measures actual risk to customers
- How to create multi-window alerts that reflect true system health

______________________________________________________________________

### 🧱 Banking Anchor

- Alerts fire on CPU, but user login failure goes unnoticed
- Customer complaint volume rises while dashboards stay calm
- A high-priority alert overhaul improves accuracy and sleep

______________________________________________________________________

## 🧪 Teaching Sequences (Per Panel)

### Panel 1 – The All-Night Alarm

- **Scene**: Daniel bleary-eyed, hit by 37 alerts for CPU
- **Teaching Moment**: Static thresholds ≠ impact
- **Widget**: Reflection — “When did your alert wake you up for nothing?”
- **Artifact**: PagerDuty alert + no user impact log

### Panel 2 – False Positives Everywhere

- **Scene**: Juana mocks Daniel’s threshold-based alert
- **Teaching Moment**: Alert volume =/= alert validity
- **Widget**: Hector Alavaz Quote — “Geneos rules don’t fix modern risk.”
- **Artifact**: Screenshot of alert rules from 2009

### Panel 3 – Looking for Symptoms, Not Signals

- **Scene**: Aisha compares real outage (no alert) to CPU alert (no user pain)
- **Teaching Moment**: Alert on outcomes, not inputs
- **Widget**: Debug Pattern — Missing Symptom Coverage
- **Artifact**: Error rate graph vs. CPU utilization chart

### Panel 4 – Burn Rate Awakening

- **Scene**: Hector Alavaz shows burn rate slope visual
- **Teaching Moment**: SLO alerting is about **speed of degradation**
- **Widget**: Diagram — Burn rate slope visual
- **Artifact**: Service A: 10% in 5m, Service B: 30% in 30m

### Panel 5 – Fixing the Noise

- **Scene**: Clara and Daniel rewrite alert: 10% burn in 5 min with links
- **Teaching Moment**: Alert criteria = clarity + correlation
- **Widget**: Try This — Rewrite one alert with business impact in mind
- **Artifact**: Before/after alert config (YAML or PromQL)

### Panel 6 – Test Fire Drill

- **Scene**: Team simulates alert; new version works
- **Teaching Moment**: Runbooks + logs + trace = alert success
- **Widget**: Reflection — “What info do you want with a 3 AM alert?”
- **Artifact**: Sample alert body with trace + log link + severity

### Panel 7 – Lesson Locked In

- **Scene**: Hector Alavaz summarizes new alert standards
- **Teaching Moment**: Alerts should answer: what’s broken, who’s affected, what’s next?
- **Widget**: Hector Alavaz Quote — “Let’s not build alarms. Let’s build clarity.”
- **Artifact**: Screenshot of alert with embedded links and triggers

______________________________________________________________________

## 👤 Character Learning Beat

- **Daniel**: Overwhelmed by alert fatigue; learns to focus on user impact
- **Juana**: Mentor role, encourages meaningful thresholds and minimalism
- **Aisha**: Reframes alerts around business context and customer experience
- **Clara**: Drives YAML cleanup and alert correlation logic
- **Hector Alavaz**: Brings SLO awareness and alert criteria philosophy

______________________________________________________________________

## 🧪 Mini Assessment Hook Summary

- `:::reflection` → What was your worst false positive alert?
- `:::debug pattern` → Missing Symptom Coverage
- `:::try this` → Convert one threshold alert to burn rate logic

______________________________________________________________________

## 📋 Panel Beat-to-Concept Map

| Beat # | Panel Title                | Teaching Goal                          |
| ------ | -------------------------- | -------------------------------------- |
| 1      | The All-Night Alarm        | Static alert ≠ meaningful incident     |
| 2      | False Positives Everywhere | Alert fatigue breeds distrust          |
| 3      | Looking for Symptoms       | User pain must trigger alerts          |
| 4      | Burn Rate Awakening        | Burn rate reveals risk slope           |
| 5      | Fixing the Noise           | Criteria = correlation + clarity       |
| 6      | Test Fire Drill            | Good alerts = actionable context       |
| 7      | Lesson Locked In           | System-wide alerting standards defined |
