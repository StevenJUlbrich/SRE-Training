# Day 3 SRE training module

Below is a comprehensive, narrative-driven Day 3 SRE training module. It’s written as if you’re guiding an interactive workshop, weaving in real-life war stories (multi-page style), humor, and practical code snippets. It remains vendor-neutral, includes concise Python examples, and addresses a broad range of organizational sizes. Each section is presented in a storytelling format, with tiered content for beginners, intermediates, and advanced SREs—plus plenty of humor and humanity along the way!

---

## From Observability Warrior to SRE Superhero!**

### **Introduction: Evolving from Observability Wizard to SRE Champion**

**Storytime Setup**  
Picture this: You’re huddled around a flickering conference-room projector, sipping stale coffee at 2 AM. The logs are *apparently* telling you something, but no one’s sure exactly what. Your incident management tool is screaming, your manager is demanding an ETA, and you’re remembering Day 1 and Day 2 of this course—where you gained new superpowers in observability. Now, on Day 3, it’s time to step it up. You’re not just an Observability Wizard anymore—you’re about to become a full-blown SRE Champion, turning all that data into actionable reliability.

**Key Themes**  
- You’ve got the tools from Day 1 and Day 2. **Now** you’ll learn to use them as an SRE does.  
- Transform your mindset: not just “Is it broken?” but “How broken is it, does it matter, and what’s our plan?”  
- Learn the delicate art of error budgets, where “100% uptime” is the boogeyman, not the objective.  
- Appreciate that SRE transformations can be messy—real life is seldom perfect.  

**Video Placeholder**  
{{VIDEO_LINK_INTRO}}

*(We’ll add the actual link later—no worries!)*

---

## **Section 1: The Art & Science of SLOs**

Practical Incident Workflow (Sample)**



![Mermaid Diagram: flowchart](images/diagram-1-8bb2a2b3.png)



**Short YAML Snippet for Incident Routing**:
```yaml
incident_management:
  severity:
    SEV1: "Critical outage, immediate response"
    SEV2: "Major degradation, respond in <30 minutes"
  auto_escalation:
    - engineering_lead
    - sre_lead
  runbook_links:
    - service: "payment_gateway"
      doc: "http://docs.internal/runbooks/payment_incident.md"
```


### **1.1 Beginner Level (🔍): SLO Foundations**

#### **Main Narrative: “The Tale of Sam and the Metric Tsunami”**  
Let’s meet Sam, a passionate engineer who joined “GenericCo” right after finishing the Day 2 observability training. Sam wanted *all* the metrics—CPU usage, memory usage, disk I/O, network throughput, the cafeteria’s coffee machine temperature. The problem? Sam ended up drowning in a sea of data.

1. **Translating Raw Metrics into SLIs**  
   - **Sam’s Dilemma:** Even with a million metrics, Sam couldn’t *prioritize*.  
   - **Guiding Principle:** Focus on service-level indicators that capture *user pain*: e.g., request latency, error rates, or success rates.  

2. **Setting Realistic SLO Targets**  
   - “**Perfect** is the enemy of **reliable**.” At first, Sam tried 99.999% for everything.  
   - After an all-nighter chasing a fraction-of-a-percent drop in availability, Sam realized 99.9% might be enough.  

3. **Understanding SLIs, SLOs, SLAs**  
   - **SLI**: The *metric*, like request success rate.  
   - **SLO**: The *target*, like “99.9% of requests succeed.”  
   - **SLA**: A *contract* with external parties, with penalties if you fail.  

4. **Your First Error Budget**  
   - **Sam’s Lightbulb Moment:** The 0.1% downtime (for a 99.9% SLO) gave the team permission to innovate without fear of *tiny* incidents.  

5. **Avoiding the “Too Many Metrics” Trap**  
   - Sam’s team learned to pick *three to five* key SLIs. More than that, and you’re back to drowning.

#### **Short Python Snippet: Basic Error Budget Calculation**  
```python
import datetime

def calculate_error_budget(slo_percentage, total_requests, actual_failures):
    """Calculate remaining error budget based on an SLO and real data."""
    allowed_failures = total_requests * (1 - slo_percentage)
    used_failures = actual_failures
    remaining = allowed_failures - used_failures
    return remaining

# Example usage:
slo_percentage = 0.999  # 99.9%
total_requests = 100_000
actual_failures = 50

budget_left = calculate_error_budget(slo_percentage, total_requests, actual_failures)
print(f"Remaining error budget: {budget_left} failures allowed.")
```

*(A simple snippet that demonstrates the concept—Sam used something like this to track whether they were still within that 0.1% error budget.)*

---

### **1.2 Intermediate Level (🧩): SLO Artistry**

#### **War Story: “The Midnight Alert Saga”**  
Imagine you’re on-call, and your pager (or phone) starts shrieking at midnight. You jump out of bed, scramble for your laptop, only to discover it’s a *minor* blip in one region that your SLO-based alerting overreacted to. Multiply that by 20 times a month, and you have a morale crisis on your hands.

**Key Lessons**  
- **Multi-Dimensional SLOs:** Don’t lump everything together. For instance, measure success rate in each region or data center separately.  
- **Building Smarter Alerts:** Implement burn-rate alerts that trigger only when your error budget is projected to be exhausted *quickly*.  
- **Error Budget Negotiation:** Work with product teams to decide how to spend or protect that error budget. If you’re launching a new feature, you may accept higher risk.  

**Short Python Snippet: Burn-Rate Alert Concept**  
```python
def projected_burn_rate(error_rate, time_window_hours, slo_hourly_budget):
    """
    Estimate how quickly you'd burn your error budget.
    error_rate: fraction of requests failing per hour
    time_window_hours: time period to observe
    slo_hourly_budget: fraction of requests allowed to fail in that hour
    """
    return (error_rate / slo_hourly_budget) * time_window_hours

# For example, if error_rate is 0.003 and your SLO budget is 0.001 per hour:
print(projected_burn_rate(0.003, 6, 0.001))  # Are we burning too fast?
```

---

### **1.3 Advanced/SRE Level (💡): SLO Mastery**

#### **In-Depth War Story: “The SLO Scaling Chronicles”**  
This is a *multi-page* tale of an SRE leader, Alex, who aimed to roll out an SLO framework across a massive, multi-department organization:

1. **Day 1**: The Top-Down Mandate  
   - The CTO excitedly declares, “We need SLOs across every service!”  
   - The 200+ service owners recoil at the complexity.  

2. **Day 15**: The Political Minefield  
   - Product managers fear that strict SLOs could “slow innovation.”  
   - Some service owners worry about being penalized if they don’t meet targets.

3. **Day 30**: Building a Tiered System  
   - Alex introduces **tiered SLOs**: Tier 1 for mission-critical systems, Tier 2 for important-but-not-critical, Tier 3 for nice-to-have.  
   - This helps focus the highest reliability demands where they truly matter.  

4. **Day 60**: Negotiations and Revelation  
   - Alex organizes reliability workshops, showing how to set an SLO that’s challenging but *not* impossible.  
   - A few early adopters proudly show 99.5% SLO attainment, with error budgets fueling safe feature experiments.

5. **Day 90**: The Cultural Shift  
   - The org sees fewer 3 AM incidents because they’re building around realistic SLOs.  
   - Alex wins over the CFO by showing how stable systems reduce hidden costs.  

6. **The Climax**: Predictive Reliability  
   - Advanced teams start forecasting usage spikes and system saturation.  
   - They proactively adjust capacity before the error budget is threatened.

7. **End Result**  
   - SLO frameworks become the “new normal,” with standardized dashboards, consistent reporting, and a new *culture* of reliability over perfection.  
   - **Moral:** SLO mastery is not just about technology—it’s about negotiation, communication, and measured risk-taking.

---

## **Section 2: The Incident Management Dojo**

Example Production Readiness Review Template**



![Mermaid Diagram: flowchart](images/diagram-2-fa80019c.png)



### **2.1 Beginner Level (🔍): Survival Basics**

#### **War Story: “The 2AM Database Disaster” (Multi-Page)**  
Meet Taylor, a brand-new on-call engineer:

1. **Scene 1: The Alert**  
   - Taylor gets woken at 2 AM. The alert says “DATABASE ERROR!”  
   - No clue which database or how critical the error is.  

2. **Scene 2: The Scramble**  
   - The runbook is 200 pages of outdated info.  
   - Team Slack channels are silent because half the team is asleep.  

3. **Scene 3: Lessons Learned**  
   - By the time morning rolls around, the incident is resolved—*somehow*.  
   - In the retrospective, the team decides to adopt clearer severity definitions (SEV1, SEV2, etc.), better runbooks, and shared on-call rotations.

4. **Takeaways**  
   - **Severity Levels**: Not everything is SEV1.  
   - **Documentation**: Short, relevant runbooks for half-asleep engineers are gold.  
   - **First Postmortem**: “Never again” means capturing *root causes*, *remediation steps*, and *lessons learned*.

---

### **2.2 Intermediate Level (🧩): Incident Mastery**

#### **War Story: “The Tale of the Recurring Outage”**  
A mid-sized e-commerce company faced the *same* payment gateway outage every Friday night:

1. **Realization**  
   - A simple ephemeral network blip was bringing down the payment microservice.  
   - Because they had no automated failover or playbook, each time was chaos.  

2. **Transformation**  
   - The team built a **playbook** that quickly guided them to switch traffic to a backup payment gateway.  
   - They added **automation** that recognized the network error and triggered the failover script.  

3. **Result**  
   - The next time it happened, they were back up in minutes.  
   - Alerts became more precise: no more 50-line Slack messages, just a quick “Failover triggered for Payment Service.”

4. **Incident Communication Templates**  
   - They introduced a standard Slack message format for incident updates.  
   - “Major Payment Gateway Outage – Services impacted: Payment, Checkout. ETA to resolution: 10 minutes.”

---

### **2.3 Advanced/SRE Level (💡): Incident Leadership**

#### **War Story: “The Chaos Engineering Experiment Gone Wrong (But Right)”**  
At a growing tech startup, an ambitious SRE manager, Jordan, decided to *inject chaos* into the system to see what would happen:

1. **Planning Stage**  
   - Jordan carefully explained chaos engineering to leadership: “We’ll break things intentionally to learn about hidden weaknesses.”  
   - Leadership raised eyebrows but approved a small experiment.  

2. **Chaos Unleashed**  
   - The experiment forcibly killed 10% of random service instances.  
   - Suddenly, a deeply hidden configuration mismatch brought down the staging environment *and* threatened production.  

3. **Firefighting**  
   - Jordan’s team discovered a hidden dependency that caused a cascading failure.  
   - They documented the scenario in detail.

4. **Learning**  
   - The chaos experiment was “gone wrong” because it uncovered a *huge* architectural flaw.  
   - But it was “gone right” because they caught and fixed it before it exploded in production.

5. **Long-Term Impact**  
   - Jordan’s organization embraced chaos engineering, building a robust set of test harnesses for *intentional* breakage.  
   - Incidents became less frequent (and less severe) over time.

---

## **Section 3: Taming the Observability Beast (Cost & Scale)**

Example Cost Analysis Snippet**

```python
import pandas as pd

# Hypothetical monthly usage data
data = {
    'Team': ['Payments', 'Catalog', 'Analytics', 'Mobile'],
    'LogVolumeGB': [700, 300, 1200, 200],
    'MetricsCount': [2000, 1000, 5000, 800]
}
df = pd.DataFrame(data)

# Approximate cost calculations
df['LogCostUSD'] = df['LogVolumeGB'] * 0.10
df['MetricsCostUSD'] = df['MetricsCount'] * 0.02
df['TotalCostUSD'] = df['LogCostUSD'] + df['MetricsCostUSD']

print(df)
```

**Possible Output**:
```ts
        Team  LogVolumeGB  MetricsCount  LogCostUSD  MetricsCostUSD  TotalCostUSD
0   Payments          700          2000        70.0           40.00         110.0
1    Catalog          300          1000        30.0           20.00          50.0
2  Analytics         1200          5000       120.0          100.00         220.0
3     Mobile          200           800        20.0           16.00          36.0
```


### **3.1 Beginner Level (🔍): Cost Control 101**

#### **War Story: “The Month the Logging Bill Exploded”**  
- The CFO storms into the SRE team meeting, waving an astronomical cloud logging invoice.  
- Turns out, the team logs *every* request detail in debug mode, 24/7.  
- They adopt **sampling** and a leaner retention policy.  
- The next month, the CFO smiles (somewhat)—the bill has dropped drastically.

---

### **3.2 Intermediate Level (🧩): Advanced Optimization**

#### **War Story: “A Tale of Two Services”**  
- *Critical Service A* has extremely high reliability requirements.  
- *Non-Critical Service B* is internal analytics with flexible SLAs.  
- The SRE team designs **tiered observability**:  
  - High sampling for Service A, minimal sampling for B.  
  - Different log retention based on business importance.  
- This approach slashes data costs without jeopardizing vital troubleshooting data.

---

### **3.3 Advanced/SRE Level (💡): Observability Economics**

#### **War Story (Multi-Page): “The Observability Platform Revolution”**  
Picture a sprawling enterprise with thousands of services. Observability costs are ballooning:

1. **Stage 1: The Crisis**  
   - The CFO demands a 30% cost reduction—*without* losing insight.  

2. **Stage 2: Building an Internal Platform**  
   - An SRE guild sets up “Observability-as-a-Service.”  
   - They define standardized agents, sampling policies, and retention tiers.  

3. **Stage 3: Allocation Models**  
   - Teams now see their monthly usage costs on a shared dashboard.  
   - This transparency leads teams to refine logs and avoid dumping debug data in production.  

4. **Stage 4: Cultural Shift**  
   - Engineers start optimizing their code for fewer, clearer logs.  
   - TCO (Total Cost of Ownership) discussions become normal in project planning.  

5. **Stage 5: Executive Buy-In**  
   - The CFO becomes an ally, praising the SRE team’s data-driven approach.  
   - Observability transforms from a black hole of spending into a strategic resource.

---

## **Section 4: Reliability Culture: Making SRE a Superpower, Not a Burden**

### **4.1 Beginner Level (🔍): Cultural Foundations**

#### **War Story: “The Toil Monster and the Reluctant Automator”**  
- Devin, an ops engineer, manually restarts a failing service 20 times a day.  
- They track the “toil” and realize they’re spending half their week on this *one* menial task.  
- By automating the restart process (and fixing the root cause), they free up time to tackle more interesting reliability tasks.  
- The “Toil Monster” is slayed, morale rises, and leadership notices the improvement in *true* productivity.

---

### **4.2 Intermediate Level (🧩): Cultural Growth**

#### **War Story: “The Production Readiness Review That Saved Christmas”**  
- An e-commerce company has a massive holiday launch scheduled for December.  
- Initially, dev teams push back: “We don’t have time for your Production Readiness Review.”  
- They grudgingly fill out a concise PRR checklist anyway, discovering a crucial misconfiguration that would have toppled the site under holiday load.  
- The last-minute fix *saves* the holiday season. Dev teams become PRR converts.

---

### **4.3 Advanced/SRE Level (💡): Cultural Leadership**

#### **War Story: “The Executive Who Learned to Love Reliability”**  
- At “BigCorp,” the CFO initially sees SRE as a cost center.  
- An SRE director uses *business-friendly metrics*: customer retention, reduced downtime, brand reputation.  
- Over a year, the CFO sees direct correlation between reliability improvements and increased revenue.  
- Suddenly, the SRE budget *expands*, and reliability becomes a core company value.

---

## **Section 5: Shift-Left Reliability**

### **5.1 Beginner Level (🔍): Development Integration**

#### **War Story: “The Mystery of the Silent Service”**  
- A new microservice fails quietly in production—no logs, no alarms.  
- Developers realize they neglected to add even basic error metrics or logs.  
- They integrate minimal observability checks in the **CI/CD pipeline**, ensuring every commit has at least a few essential logs and a health endpoint.  
- Silent failures vanish.

---

### **5.2 Intermediate Level (🧩): Observability-First Development**

#### **War Story: “The Synthetic Customer Who Saved the Day”**  
- The SRE team sets up synthetic tests that mimic real user journeys—logging in, placing an order, checking out.  
- During a normal code deploy, a synthetic test catches a subtle bug that would have prevented users from checking out.  
- The deploy is halted, the bug is fixed *before* real customers see it, and the on-call staff remain blissfully asleep that night.

---

### **5.3 Advanced/SRE Level (💡): Reliability by Design**

#### **War Story (Multi-Page): “The Great Database Coupling Disaster of 2023”**  
1. **The Setup**  
   - A large microservices ecosystem with a critical “User Profile” service.  
   - Everything *quietly* depends on the same database cluster.  

2. **The Big Outage**  
   - A small schema change triggers massive lock contention.  
   - Cascading failures bring down half the application fleet.  

3. **SRE Involvement**  
   - After the fiasco, SREs lead a new architecture design that decouples services and uses caching.  
   - Chaos experiments reveal more hidden dependencies.  

4. **Long-Term Transformation**  
   - Teams adopt a principle: “No new service without a reliability design review.”  
   - Observability-driven dev cycles become standard, preventing future fiascos.

---

## **Section 6: The SRE Journey: Putting It All Together**

### **In-Depth Multi-Page Capstone Story: “The Phoenix Project 2.0: Rise of the SRE”**

This extended narrative follows a fictional company, **TechCore**, from chaos to SRE excellence:

1. **Chaos Reigns**  
   - TechCore has partial observability from Day 1–2 efforts. They *see* metrics but do nothing with them. Incidents are frequent, blame is common, and weekends are ruined.

2. **The First Spark: SLO Adoption**  
   - An ambitious engineer sets an SLO for the user-facing service: 99.5% success rate.  
   - Everyone freaks out—“But we need 100% uptime!”  
   - They compromise on 99.8%, giving a small error budget.

3. **Incident Management Renaissance**  
   - TechCore invests in a well-defined incident process, leveling alerts to reduce noise.  
   - Postmortems become blameless and everyone shares in root cause analysis.

4. **Observability Scaling**  
   - As the user base grows, so does the data. Logs from thousands of microservices threaten to bankrupt TechCore.  
   - A cost-optimization initiative brings in sampling, trimming pointless debug logs.

5. **Cultural Shift**  
   - Development teams consult SREs *before* launching new features.  
   - Production Readiness Reviews and real-time feedback loops become part of the dev lifecycle.

6. **Reliability by Design**  
   - TechCore invests in chaos engineering game days, anticipating and mitigating potential outages.  
   - They identify single points of failure and redesign architectures for resilience.

7. **Executive Alignment**  
   - Impressed by fewer outrages and improved user satisfaction, leadership invests further in SRE.  
   - SRE matures from “firefighting crew” to “strategic reliability partner.”

8. **Final Outcome**  
   - TechCore’s reliability posture leaps forward.  
   - The on-call teams experience fewer late-night pages, and the CFO sees how a stable platform boosts revenue.  
   - Engineers are proud of a culture that values learning and improvement, not blame.

**Lessons Learned**  
- Real SRE transformations involve technical *and* social challenges.  
- Small, incremental steps add up: from metrics to SLOs, from panic to structured incident response, from runaway logs to cost management.  
- Humor and empathy go a long way in building a culture that *truly* cares about reliability.

---

## **Essential Code & Configuration Examples**

Throughout the war stories, you’ve seen short Python snippets demonstrating basic error budget calculations, burn-rate projections, and more. Consider also:

1. **SLO Dashboards**: A minimal config file or snippet that sets up a vendor-neutral dashboard (e.g., using JSON or YAML) to visualize SLO error budgets.  
2. **Incident Routing Logic**: Simple pseudo-code that routes specific alerts to the right on-call engineer.  
3. **Cost-Optimization Scripts**: High-level examples that show how to parse log volume or metrics usage, so teams can see where they’re burning money.  

*(All remain vendor-neutral but demonstrate the concept in short, readable snippets.)*

---

## **Essential Diagrams with Personality**

1. **The SRE Evolution**: Show a fun timeline from “Everything’s on fire” to “We expected this and have a plan.”  
2. **SLI/SLO/SLA Pyramid**: Indicate how SLIs feed into SLOs, and SLOs might feed into SLAs.  
3. **Incident Management Flowchart**: A playful “When an alert fires, do X, Y, Z” diagram with comedic labels like “PANIC – if you must, but only for a minute.”  
4. **Cost Optimization Framework**: Pie charts showing how logs, metrics, and traces can slice up the observability budget.  
5. **SRE Team Models**: Cartoons of different organizational setups (centralized SRE team vs. embedded SREs).  

---

## **Conclusion & Next Steps**

By weaving together **error budgets**, **incident management**, **cost optimization**, **culture change**, and **shift-left reliability**, you’re now armed with the full SRE toolkit. Day 3 is the turning point where observability meets structured SRE discipline. Remember:

- **Start simple**: Don’t overload your SLOs or logging.  
- **Iterate**: Reliability is a journey, not a destination.  
- **Culture matters**: Tools are easy; people are hard.  
- **Stay curious**: Chaos engineering, predictive analysis, shift-left testing—embrace them step by step.  

Embrace your new powers responsibly, champion reliability in your organization, and above all—keep your sense of humor. You might just save your weekends (and your sanity) in the process.

**Final Video Placeholder**: {{VIDEO_LINK_CAPSTONE}}

---

### **You are now an SRE Superhero!**

**Remember:** True heroism isn’t about avoiding every failure—it’s about knowing which failures matter, and having a plan to bounce back stronger. So go forth, SRE Champions, and bring reliability wherever you roam.