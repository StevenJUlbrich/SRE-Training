# Observability 101+ Curriculum Structure (Led by Hector Alavaz Alvarez)

This is a Hector Alavaz-led narrative training track focused entirely on **Observability** for production support professionals, especially those transitioning from tools like **ITRS Geneos** into modern SRE practice. The content is dramatically grounded, brutally practical, and always tied to **real banking system impact**.

## PART I: OBSERVABILITY FOUNDATIONS – Beginner Tier

### Chapter 1: **"The Site Is Down" Isn't a Root Cause**

- Introduce Hector Alavaz and his anti-fluff attitude
- Observability vs Monitoring (with Geneos context)
- Why banking uptime requires understanding *why*, not just *what*
- 🧱 Banking scenario: A payment processor goes offline
- 🔥 Hector Alavaz scorches a rainbow dashboard with no causality

#### Panel-by-Panel Beat Map

1. **The Pager Screams** – Hector Alavaz gets paged in the middle of the night while the rainbow dashboard shows all green. Visual: chaos behind him, dashboard glowing like a rave.
2. **Wanjiru Panics** – Wanjiru stares at metrics she doesn't understand while a VP yells about failing transactions. Visual: Slack alerts, Geneos blinking, her mouse hovering uncertainly.
3. **What’s Actually Broken?** – A terminal screenshot reveals `payment-service` 500s. Katherine says "CPU looks fine though."
4. **The Dashboard Is Lying** – Hector Alavaz walks in holding coffee, asks: "Did you check logs, or are we just admiring the colors?"
5. **Context is Missing** – Juana shows the logs: missing trace IDs, vague errors. “Nice. It broke, and it didn’t even tell us who it killed.”
6. **Monologue from Hector Alavaz** – He points to each pillar (Logs, Metrics, Traces) and explains what they could’ve revealed. Dramatic diagram in background.
7. **Lesson Locked In** – Wanjiru says, "So… green doesn’t mean good." Hector Alavaz: “Green means the system’s lying. Now let’s teach it to confess.”

- **Min Panels**: 7

### Chapter 2: **The Problem Isn’t Always the Problem**

- What production support knows that devs forget
- Teaching telemetry: logs, metrics, and traces
- Wanjiru and Katherine get burned by an untraceable config push
- Juana shows what *should* have been in the logs

#### Panel-by-Panel Beat Map

1. **The Mystery Crash** – A customer service agent reports failed wire transfers. Katherine is already looking at CPU usage.
2. **Dashboard Deceit, Part II** – CPU and memory are stable. Wanjiru shrugs. “Geneos isn’t showing anything weird.”
3. **The Missing Trace** – Juana suggests tracing the request path. No trace data is found. “No trace ID in logs. Classic.”
4. **What They Missed** – We flash back to a config push. Visual: a developer unchecked 'enableTracing=true'.
5. **The Blame Game Begins** – Teams point fingers. The ops lead blames the app; the devs blame the platform.
6. **Hector Alavaz Steps In** – “Observability isn’t magic. It’s preparation. And you didn’t prepare.” He slams a diagram down.
7. **The Corrected View** – Juana overlays what *should* have been captured: key spans, context IDs, and log correlation.
8. **Team Realization** – Wanjiru: “We didn’t *see* the problem. We *caused* it and logged nothing.”
9. **Closing Shot** – Hector Alavaz sipping coffee: “The system didn’t hide the truth. You just didn’t teach it how to talk.”

- **Min Panels**: 9

### Chapter 3: **Logs That Talk, Metrics That Matter**

- How to move from passive dashboards to diagnostic instrumentation
- Exposing flawed dashboards ("Everything green, everything broken")
- Practical logging formats, field selection, and metric taxonomy for banking services
- Leonel logs too much; Hector Alavaz responds with dry fury

#### Panel-by-Panel Beat Map

1. **Death by Verbose Logging** – Leonel shows off a beautiful but bloated log stream. “We log everything!” he grins. Sofia raises an eyebrow.
2. **The Metrics Don’t Match** – Meanwhile, Katherine notes the latency graph looks clean… but user complaints are rising.
3. **The Unreadable Log** – Wanjiru attempts to find a user error but is blocked by irrelevant debug logs and missing correlation IDs.
4. **Hector Alavaz Steps In** – He draws three overlapping circles labeled Logs, Metrics, Traces. “If they don’t intersect, they don’t help.”
5. **Metric Hygiene Clinic** – Clara points out a metric labeled `service_latency_time_chart_thing`. Hector Alavaz winces audibly.
6. **Refactoring the Noise** – Team collaboratively rewrites a log format and reduces cardinality on a critical metric.
7. **The Ah-Ha Graph** – A new dashboard emerges: minimal, relevant, clear. It shows a real correlation between auth failures and DB retries.
8. **Lesson Locked In** – Hector Alavaz’s dry monologue over the scene: “Logs are your system’s mouth. Metrics are its mood. Don’t confuse ranting with reasoning.”

- **Min Panels**: 8

### Chapter 4: **You’re Not Alerting — You’re Alarming**

- Burn rate alerts vs static thresholds
- Alert fatigue and dashboard-overload incidents
- Juana mentors Daniel on writing real alerts
- Aisha reframes alert impact in terms of banking operations

#### Panel-by-Panel Beat Map

1. **The All-Night Alarm** – Daniel is half-asleep, watching a Geneos alert that has fired 37 times in 12 minutes. His face says: “Please make it stop.”
2. **False Positives Everywhere** – Juana walks by and glances at the alert rules. “You’re getting paged for CPU > 85%? Who trained you—Geneos circa 2009?”
3. **Looking for Symptoms, Not Signals** – Aisha shows a past incident where high CPU had no user impact, while an unnoticed error rate spike broke login.
4. **Burn Rate Awakening** – Hector Alavaz enters with a diagram showing error budget burn across services. “You don’t alert on thresholds. You alert on *threats.*”
5. **Fixing the Noise** – Clara helps Daniel rewrite the alert using a time-sliced burn rate policy with log links and trace context.
6. **Test Fire Drill** – The team simulates a new incident using the updated alert logic — results are quieter, clearer, and lead directly to the source.
7. **Lesson Locked In** – Hector Alavaz’s monologue: “Bad alerts make good engineers quit. Let’s not build alarms. Let’s build clarity.”

- **Min Panels**: 7

### Chapter 5: **Patterns to Avoid Like Volcanoes**

- Common anti-patterns in Geneos dashboards and alerting configs
- Hector Alavaz lists 5 banking observability sins:
  - Metrics with no owners
  - Alerts without runbooks
  - Logs that lie by omission
  - Uptime without user success
  - “It’s always the network” syndrome
- Visual case study: a chaotic dashboard meltdown during an ATM outage

#### Panel-by-Panel Beat Map

1. **Dashboard Chaos** – Wanjiru is overwhelmed by a Geneos dashboard that has 24 panels, none of them labeled. “Which one tells me why the ATMs aren’t working?”
2. **The Blame Begins** – Daniel mutters, “Must be the network again.” Njeri’s death stare says otherwise.
3. **The Five Sins** – Hector Alavaz slams down a whiteboard with the five sins of banking observability. “Every one of these has ruined a production system I’ve seen.”
4. **Sin #1: Ownerless Metrics** – Clara shows a graph of `latency_avg_all` and nobody can say who owns it. “Guess who gets paged? Everyone.”
5. **Sin #2: Orphaned Alerts** – Juana responds to a noisy alert only to discover there’s no runbook. “Awesome. It’s a riddle now.”
6. **Sin #3: Logs That Lie** – Katherine highlights a 500 error log… with no trace ID, no request path, and no helpful message. “This might as well be in Morse code.”
7. **ATM Outage Replay** – The scene flashes back to a real outage. Metrics showed normal, logs were incomplete, alerts fired late.
8. **Lesson Locked In** – Hector Alavaz’s closing line: “Avoid these sins or prepare for the volcano. And I mean a real one—because the auditors are coming.”

- **Min Panels**: 8

______________________________________________________________________

## PART II: INTERMEDIATE INSTRUMENTATION & ANALYSIS – Tier 2

### Chapter 6: **Metrics Aren’t Just Numbers — They’re Clues**

- Sofia walks the team through a high-cardinality metric problem
- Clara challenges poor metric naming and field bloat
- How Hector Alavaz tunes metrics to highlight "real-time symptoms, not artifacts"
- Banking example: Slow balance lookup traced to a cache metric drift

#### Panel-by-Panel Beat Map

1. **The Phantom Spike** – A metric chart shows high CPU, but the system feels fine. Sofia frowns: “Is that real?”
2. **Cardinality Explosion** – Clara pulls up metrics with thousands of user-tagged variations. Hector Alavaz mutters, “The dashboard’s bleeding context.”
3. **The Naming Nightmare** – Daniel shows a widget called `agg_metric_report_perf_multi_v2`. Nobody knows what it means.
4. **Metric Hygiene Time** – Hector Alavaz redraws the metric stack on a whiteboard, replacing them with business KPIs and SLO-aligned graphs.
5. **Symptoms vs Signals** – Wanjiru points out a real issue: cache miss rate spiked. It correlates with latency, but isn’t on the dashboard.
6. **Dashboard Cleanup Begins** – Team removes unnecessary panels and renames core metrics. Clara adds a timeline overlay.
7. **Reality Revealed** – The newly trimmed panel layout clearly shows that a cache drift caused the balance lookup issue.
8. **Lesson Locked In** – Hector Alavaz: “Metrics are medical charts. If you don’t know how to read them, you’re just looking at patient doodles.”
9. **Epilogue Panel** – Sofia: “We made it less noisy.” Hector Alavaz: “No. You made it *speak.*”

- **Min Panels**: 9

### Chapter 7: **Tracing the Money Trail**

- Njeri and Daniel trace a broken multi-service banking transaction
- Juana explains root causes through span-level context
- Introduces OpenTelemetry and Hector Alavaz’s sarcastic history with vendor lock-in
- Visual path: request → auth → ledger → customer notification

#### Panel-by-Panel Beat Map

1. **The Silent Delay** – A customer’s wire transfer takes 12 seconds. The frontend looks fine. Wanjiru notices a sharp drop in user completion rate.
2. **Span-Free Zone** – Daniel pulls logs but finds no trace ID. Juana groans: “We deployed without span instrumentation again, didn’t we?”
3. **The Blame Bounces** – The dev team blames the DB. Infra blames the network. Njeri traces it manually using request headers.
4. **The Ghost Span Appears** – Hector Alavaz walks in, drops a hand-annotated span diagram. “Your request went here, here, here, and exploded here.”
5. **OpenTelemetry Unleashed** – Daniel instrumenting real spans. Juana explains what a `parent_span_id` is while pointing at the new trace view.
6. **Trace ID Threading** – Njeri adds tracing context to logs and updates correlation logic. Traces now surface slowness in `auth` → `ledger` hops.
7. **Root Cause Found** – A rogue retry loop in `ledger-service` delayed all downstream services. Traces light up with red bars.
8. **Lesson Locked In** – Hector Alavaz: “Tracing is the chalk outline. You want to see where the body dropped. Now you can.”

- **Min Panels**: 8

### Chapter 8: **The Lie Detector Test: Postmortem Telemetry**

- Students revisit a simulated incident using observability tools
- Clara and Omar debate how telemetry helped (and failed)
- Hector Alavaz demands a better logging contract across services
- Teaches "Write telemetry like you’re going to debug a ghost at 3 a.m."

#### Panel-by-Panel Beat Map

01. **Incident Playback Begins** – Juana pulls up logs, traces, and metrics from last week’s login outage. “Let’s find the failure story.”
02. **Everyone Blames the Logs** – Clara points out timestamps don’t align. Omar can’t correlate user activity. “Telemetry gaps everywhere.”
03. **The Noise vs. Signal Chart** – Hector Alavaz draws a 3x3 grid on the whiteboard. “Useful vs Useless. Timely vs Delayed.” The team starts sorting their telemetry.
04. **The Misleading Metric** – Sofia finds a metric that dipped during the outage but was excluded from the dashboard. “It was right here all along.”
05. **The Ghost Error** – Juana discovers a silent `403` response path that wasn’t logged. Wanjiru adds, “No one even knew that handler existed.”
06. **Blame Isn’t the Goal** – Hector Alavaz shuts down the noise: “You’re not hunting villains. You’re building timelines.”
07. **Telemetry Rewrite Planning** – The team builds a table of missing log fields, mismatched metrics, and non-correlated spans.
08. **The New Standard** – Clara proposes a new format for logs and a trace ID injection policy. Hector Alavaz nods. “Now we’re getting somewhere.”
09. **Lesson Locked In** – Hector Alavaz’s monologue: “You don’t debug ghosts with flashlights. You build haunted house diagrams—with receipts.”
10. **Reflection Panel** – Omar: “This wasn’t postmortem. It was confession.” Hector Alavaz: “Good. Now teach the system how to confess sooner.”

- **Min Panels**: 10

### Chapter 9: **What Good Looks Like (And What It Covers Up)**

- Banking telemetry benchmarks: normal vs suspicious vs real outage
- Leonel builds the most beautiful dashboard you’ve ever seen — and Hector Alavaz deletes it
- Builds a “quiet dashboard” that only glows when the user is in pain
- Juana shares what *real* signal compression looks like in production

#### Panel-by-Panel Beat Map

01. **The Pretty Dashboard** – Leonel presents a stunning dashboard to the team: rainbow gauges, graphs, gradients galore. Everyone stares in polite confusion.
02. **The Misleading Calm** – Sofia compares it to user metrics. “It looks clean… but logins are down 6%.”
03. **The Anti-Signal** – Hector Alavaz calls it “dashboard theatre.” “You made something pretty. Can it stop a fire?”
04. **Dashboard Autopsy** – Clara highlights 3 charts showing downward trends during last week’s outage. None are visible in Leonel’s view.
05. **Redesign Begins** – Juana and Omar help reduce panels to just 5: request rate, error rate, latency, business KPI, trace-linked event summary.
06. **Signal Highlighting** – They add change annotations, zoomed time windows, and trace IDs directly into the visuals.
07. **Before & After** – A side-by-side of Leonel’s old vs new version. The “quiet dashboard” has two red blips—and they correlate directly with user complaints.
08. **Hector Alavaz’s Standard** – He scribbles on the whiteboard: “3 graphs: What broke. When it broke. Why it broke.”
09. **Final Reflection** – Leonel: “You don’t want pretty. You want accurate.” Hector Alavaz: “You want clarity when everything’s on fire.”
10. **Lesson Locked In** – Juana: “Less dashboard. More insight.” Hector Alavaz: “Now it tells the truth—whether you like it or not.”

- **Min Panels**: 10

______________________________________________________________________

______________________________________________________________________

## PART III: ADVANCED STRATEGY & SYSTEM THINKING – Tier 3

### Chapter 10: **Signals, Saturation, and Strategic Silence**

- Clara teaches the team to recognize telemetry saturation in noisy environments
- Njeri introduces signal decomposition in high-volume fraud detection pipelines
- Hector Alavaz explains why systems don’t need to tell you *everything* — just *the right thing, at the right time*
- Juana demonstrates golden signal mapping for Tier-1 banking services

#### Panel-by-Panel Beat Map

01. **Signal Storm** – Wanjiru opens a dashboard with over 200 metrics firing at once. “Everything’s blinking, but nothing’s helping.”
02. **Clara Diagnoses the Noise** – She highlights 8 metrics that contradict each other. “We’ve got telemetry saturation.”
03. **Hector Alavaz’s Silence Lesson** – Hector Alavaz turns off the screen. “Now you’re forced to think. Most of this data is comfort, not clarity.”
04. **Enter the Fraud Funnel** – Njeri overlays signal decomposition from a fraud detection pipeline. “Three metrics matter. The rest are context, not answers.”
05. **Missed Signals** – Juana points out an error spike in ACH transaction reversals that no one caught because it wasn’t on a dashboard.
06. **Metric Reduction War Room** – Team meets to audit all metrics for a Tier-1 banking service. Sofia proposes a ‘must-have’ vs ‘nice-to-have’ model.
07. **Rebuilding the Noise Floor** – Clara creates visual filters to gray out low-signal graphs. Hector Alavaz crosses out five and says, “Those never helped us.”
08. **A Golden Mapping** – Juana presents a cleaned dashboard: latency, error rate, fraud rate, user complaints. “Everything else is decoration.”
09. **Strategic Silence** – Hector Alavaz: “A wise system only speaks when it needs to. Your job is to teach it wisdom.”
10. **Lesson Locked In** – Wanjiru: “Fewer graphs. More truth.” Hector Alavaz: “You just learned observability minimalism. I’m proud. Don’t make it weird.”

- **Min Panels**: 10

### Chapter 11: **Hector Alavaz’s Law: “All Dashboards Are Lying Until Proven Otherwise”**

- Real-time narrative of a service degradation masked by healthy graphs
- Omar leads incident comms; Wanjiru discovers misaligned SLI assumptions
- Team audits each dashboard layer — logs, metrics, traces — and fixes visualization lies
- Zuri challenges the team to build a new standard for dashboard validation

#### Panel-by-Panel Beat Map

01. **The Green Mirage** – A dashboard lights up green while user complaints flood in. Omar frowns: “That’s not possible. Is this thing even connected?”
02. **The Wrong SLI** – Wanjiru digs into the configuration. “We’re measuring latency for the cache—not the actual transaction.”
03. **Misaligned Assumptions** – Clara reviews other dashboards. All of them reference the wrong backend. “We’ve been staring at the wrong truth.”
04. **Hector Alavaz Breaks the Spell** – Hector Alavaz quietly deletes the dashboard in front of everyone. “Start over. This isn’t observability. It’s denial.”
05. **Rooted in Reality** – Zuri pulls real user metrics: mobile logins, payment confirmation delays. They match none of the current graphs.
06. **The Redesign Debate** – The team argues over which metrics actually matter. Sofia builds a quick prototype with mobile-first telemetry.
07. **Dashboard Autopsy** – Hector Alavaz forces a side-by-side postmortem: “Here’s what we measured. Here’s what failed. See the gap?”
08. **Validation Layers** – Njeri adds alerts tied to real SLIs. Juana tags trace IDs to validate graph spikes against logs.
09. **Lesson Locked In** – Hector Alavaz: “A dashboard is guilty until it proves its truth. Build for the trial, not the praise.”
10. **Reflection Panel** – Omar: “We weren’t monitoring systems. We were admiring ideas.” Hector Alavaz: “And the users noticed.”

- **Min Panels**: 10

### Chapter 12: **Teaching Systems to Confess**

- Hector Alavaz walks through instrumentation rewrite of a legacy wire-transfer service
- Sofia leads tracing and error detection mapping across four interdependent services
- Team agrees to ship telemetry before they ship code
- Malik closes with a practical checklist: what observability must do in regulated banking
- Final learner reflections and personal observability principles
- **Min Panels**: 12

## Core Themes Throughout:

- ☕ Hector Alavaz is always the main instructor — dry, efficient, unsentimental
- 🏦 Every chapter centers on a **banking-specific reliability challenge**
- 🔄 Practical exercises are built in ("Try logging this", "Trace that transaction")
- 🚫 Rainbow dashboards are treated as comedic red flags
- 💥 Anti-patterns are treated with Hector Alavaz’s signature intensity: instructional, but a little terrifying

______________________________________________________________________

Would you like to continue into **Part II: Intermediate (Instrumentation & Analysis)** next, or expand any section above with learner cast tie-ins?
