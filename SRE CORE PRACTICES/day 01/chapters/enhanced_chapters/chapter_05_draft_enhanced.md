# Chapter 5: Patterns to Avoid Like Volcanoes

## Chapter Overview

Welcome to the SRE equivalent of a disaster movie: "Patterns to Avoid Like Volcanoes." This chapter is a guided tour through the hellscape of observability anti-patterns, starring dashboards that actively sabotage you, alerts that are more riddle than rescue, and the eternal blame game ("It's always the network!"). If you've ever found yourself screaming at a wall of unlabeled graphs while executives breathe down your neck, this chapter is your group therapy session—minus the soothing platitudes. In banking, these sins don't just torch your uptime—they invite regulatory eruptions that make operational pain look gentle by comparison. Read on, or prepare to roast marshmallows in the fiery crater of your next audit.

## Learning Objectives

- **Identify** the most common—and most lethal—observability anti-patterns in financial systems.
- **Diagnose** dashboard chaos and implement sane information architecture that actually helps under pressure.
- **Enforce** evidence-based investigation instead of guessing games and cross-team finger-pointing.
- **Establish** clear metric and alert governance, from ownership to documentation to retirement.
- **Detect** and **eliminate** telemetry that lies by omission, ensuring logs and metrics are actually useful.
- **Redefine** success using customer-centric observability (because 100% uptime means nothing if no one can pay their bills).
- **Crush** default blame patterns with bias-free, data-driven incident investigations.
- **Assess** and **raise** observability maturity to meet both business needs and regulatory demands.

## Key Takeaways

- Dashboard sprawl without structure is like giving your pilots a cockpit full of unlabeled switches—expect a crash, not a landing.
- If your incident response starts with "It's probably the network," congratulations: you’re wasting everyone's time and torching team trust.
- Ownerless metrics and orphaned alerts are the operational equivalent of yelling "fire" in a crowded theater—everyone panics, nobody acts.
- Logs that “exist” but tell you nothing are worse than no logs at all; at least with silence, you know you’re blind.
- Measuring uptime instead of customer success? You’re just winning at losing—efficiently failing while congratulating yourself.
- Default blame isn’t investigation, it’s superstition. The only thing it fixes is your illusion of competence.
- Regulatory auditors don’t care about your intentions—only your documentation and evidence. Miss the mark, and watch the lava flow.
- Observability isn’t a nice-to-have—ignore these sins, and you’re not just risking downtime, you’re betting the bank (literally) on not getting caught.
- Every anti-pattern here has a body count in lost transactions, angry customers, and compliance nightmares. Don’t be next.

---

## Panel 1: Dashboard Chaos - Information Architecture
## Scene Description

**Dashboard Chaos** – Wanjiru is overwhelmed by a Geneos dashboard that has 24 panels, none of them labeled. "Which one tells me why the payments aren't working?"

*Expanded narrative: The operations center is chaos. Customer calls are pouring in—payments across the region are failing to process. Wanjiru stares helplessly at the primary monitoring dashboard: 24 different panels, most unlabeled, showing graphs and numbers with no clear meaning. "Which one actually tells me why the payments aren't working?" she asks desperately. No one answers. The dashboard is comprehensive but incomprehensible—designed to show everything but revealing nothing.*

## Teaching Narrative

This scene illustrates a fundamental observability anti-pattern: dashboard proliferation without information architecture. When faced with a critical incident, Wanjiru encounters what should be a powerful tool, but instead finds a confusing collection of unlabeled metrics that provide no actionable insight. This pattern reveals how quantity without organization actively hinders understanding.

## Information Architecture Explained

Information Architecture in observability is the deliberate organization of telemetry data for human understanding:

1. **Hierarchical Organization**: Arranging metrics and indicators in logical groups and hierarchies

2. **Visual Prioritization**: Using layout, size, and prominence to direct attention to what matters most

3. **Contextual Labeling**: Providing clear, consistent naming and context for all data points

4. **Navigational Clarity**: Creating intuitive pathways from high-level indicators to detailed diagnostic information

In financial services, effective information architecture is particularly critical. During a payment processing outage, every minute spent deciphering dashboards represents lost transactions, frustrated customers, and potential regulatory issues.

## The Cognitive Overload Problem

Wanjiru's experience demonstrates how poorly organized dashboards create cognitive overload during incidents. The human brain can only process a limited amount of information simultaneously; when presented with 24 unlabeled panels, it becomes overwhelmed, leading to analysis paralysis rather than insight.

## Banking Implementation Guidance

To implement effective information architecture in financial systems:

1. **User-Centered Dashboard Design**: Create dashboards based on the specific questions operators need to answer

2. **Critical Path Highlighting**: Ensure the most business-critical metrics are immediately visible and clearly labeled

3. **Progressive Disclosure**: Organize information in layers, from high-level status to detailed diagnostics

4. **Consistent Visual Language**: Establish uniform conventions for colors, layouts, and nomenclature

Financial institutions must recognize that during incidents, dashboards serve as primary decision-making tools. A dashboard that requires interpretation during a crisis isn't just inefficient—it's dangerous. Well-designed information architecture doesn't just make dashboards prettier—it makes them functional when it matters most.
## Panel 2: The Blame Begins - Evidence-Based Investigation
## Scene Description

**The Blame Begins** – Daniel mutters, "Must be the network again." Njeri's death stare says otherwise.

*Expanded narrative: Daniel glances at the situation and immediately offers a diagnosis: "Must be the network again." Njeri, the network engineer, turns slowly to face him with a death stare that could melt steel. Her thought bubble reveals network monitoring graphs showing perfectly normal operations across all links. Meanwhile, the blame game escalates around them: "It's the database!" "No, it's the application code!" "Security issue?" "Configuration problem!" Minutes tick by with no actual investigation.*

## Teaching Narrative

This scene exposes another critical anti-pattern: speculation-based troubleshooting. Rather than gathering evidence, the team immediately jumps to conclusions based on history, assumptions, or team biases. This pattern not only wastes precious time during incidents but actively damages cross-team relationships and undermines future collaboration.

## Evidence-Based Investigation Explained

Evidence-Based Investigation is a systematic approach to problem-solving that prioritizes data over assumptions:

1. **Hypothesis Suspension**: Deliberately delaying conclusions until sufficient evidence is gathered

2. **Data-First Approach**: Collecting relevant telemetry before forming theories about what's wrong

3. **Confirmation Prevention**: Actively avoiding the tendency to look only for evidence that supports initial assumptions

4. **Cross-Domain Verification**: Checking multiple telemetry sources across different system components before making claims

In financial services, evidence-based investigation is essential for both operational and cultural reasons. Technically, it leads to faster resolution by focusing effort on actual issues rather than familiar scapegoats. Culturally, it prevents the team fragmentation that occurs when groups feel unfairly blamed for problems.

## The Default Blame Pattern

Daniel's assumption about the network represents a common default blame pattern in IT operations. Certain components—typically networks, databases, or "the infrastructure"—become default scapegoats based on historical incidents or organizational politics rather than current evidence.

## Banking Implementation Guidance

To implement evidence-based investigation in financial systems:

1. **Structured Incident Response**: Create explicit protocols that require evidence collection before hypothesis formation

2. **Multi-Source Verification**: Require checking multiple telemetry types (logs, metrics, traces) before making claims

3. **Assumption Documentation**: Explicitly record and test initial assumptions during incident response

4. **Blameless Culture Reinforcement**: Actively discourage speculation and reward evidence-based approaches

Njeri's death stare represents the human cost of assumption-based troubleshooting—damaged relationships and eroded trust between teams. In financial environments, where complex issues often require cross-functional collaboration, this erosion creates significant operational risk. Evidence-based approaches maintain the collaborative capacity needed to resolve complex financial system failures.
## Panel 3: The Five Sins - Anti-Pattern Recognition
## Scene Description

**The Five Sins** – Hector Alavaz slams down a whiteboard with the five sins of banking observability. "Every one of these has ruined a production system I've seen."

*Expanded narrative: Hector Alavaz enters and immediately takes control. He places a pre-prepared whiteboard against the wall with dramatic emphasis. The heading reads: "THE FIVE DEADLY SINS OF BANKING OBSERVABILITY" with detailed illustrations for each. "Every one of these has ruined a production system I've seen," he announces grimly. "And every one has triggered a regulatory finding. Let's see which ones are killing your payment network right now." The room falls silent as everyone recognizes patterns they've perpetuated.*

## Teaching Narrative

This moment represents a pivotal shift in the scene: from chaos to structure, from reactivity to analysis. Hector Alavaz's introduction of the "Five Deadly Sins" framework transforms a confusing incident into a diagnostic opportunity. By categorizing common anti-patterns, he provides the team with a mental model for understanding not just what's happening, but why it's happening.

## Anti-Pattern Recognition Explained

Anti-Pattern Recognition is the identification and categorization of recurring harmful practices:

1. **Pattern Language Development**: Creating a shared vocabulary for common failure modes

2. **Historical Learning Codification**: Transforming past experiences into structured knowledge

3. **Comparative Analysis**: Using known anti-patterns to diagnose current issues

4. **Preventative Education**: Teaching teams to recognize and avoid established failure patterns

In financial services, anti-pattern recognition serves multiple purposes. Operationally, it accelerates diagnosis by matching current symptoms to known issues. Organizationally, it enables knowledge transfer between teams and across incidents. Regulatorily, it provides structured evidence that the institution understands and addresses systemic weaknesses.

## The Regulatory Connection

Hector Alavaz's specific mention that each sin has "triggered a regulatory finding" highlights a critical dimension of observability in financial services. Poor observability practices don't just create operational problems—they create compliance risks, potentially leading to formal findings, fines, or restrictions from financial regulators.

## Banking Implementation Guidance

To implement anti-pattern recognition in financial systems:

1. **Observability Anti-Pattern Catalog**: Create and maintain a documented library of common observability failures

2. **Pattern-Based Diagnosis Tools**: Develop checklists and flowcharts that help teams quickly identify known anti-patterns

3. **Post-Incident Categorization**: Include anti-pattern identification in incident retrospectives

4. **Pre-Implementation Pattern Screening**: Evaluate new systems and changes for known observability anti-patterns

Hector Alavaz's prepared whiteboard illustrates an important principle: anti-pattern recognition shouldn't happen only during incidents. By documenting and teaching these patterns proactively, organizations can help teams avoid creating the same problems repeatedly. This preventative approach is particularly valuable in financial services, where the cost of learning through failure is exceptionally high.
## Panel 4: Sin #1: Ownerless Metrics - Metric Governance
## Scene Description

**Sin #1: Ownerless Metrics** – Clara shows a graph of `latency_avg_all` and nobody can say who owns it. "Guess who gets paged? Everyone."

*Expanded narrative: Clara points to a metric on the dashboard labeled simply `latency_avg_all`. "Who owns this metric?" she asks. The application team looks at the platform team. The platform team looks at the database team. Everyone shrugs. "What does it actually measure? What's a normal value? What's the threshold for concern?" Still no answers. Clara shakes her head. "Guess who gets paged when it spikes? Everyone. And guess who investigates? No one—because no one knows what it means."*

## Teaching Narrative

This scene exposes a prevalent but often overlooked observability anti-pattern: metrics without clear ownership or meaning. Clara's example perfectly illustrates how ambiguous, collectively owned telemetry creates confusion rather than clarity. This pattern represents a fundamental governance failure that undermines the entire observability system.

## Metric Governance Explained

Metric Governance is the systematic management of metrics throughout their lifecycle:

1. **Clear Ownership Assignment**: Explicitly designating which team or individual is responsible for each metric

2. **Definition Documentation**: Maintaining precise explanations of what each metric represents and how it's calculated

3. **Purpose Specification**: Documenting why the metric exists and what decisions it should inform

4. **Lifecycle Management**: Establishing processes for creating, reviewing, and retiring metrics

In financial services, metric governance addresses both operational and regulatory needs. Operationally, it ensures that metrics serve their intended diagnostic purpose. Regulatorily, it provides the documentation and accountability required by financial oversight bodies.

## The Collective Responsibility Problem

Clara's observation about who gets paged (everyone) versus who investigates (no one) highlights a classic problem with shared responsibility—when everyone owns something, no one actually takes responsibility for it. This pattern creates both technical confusion and organizational dysfunction.

## Banking Implementation Guidance

To implement effective metric governance in financial systems:

1. **Metric Registry**: Create a centralized catalog that documents ownership, definition, and purpose for all metrics

2. **Creation Standards**: Establish requirements for new metrics, including mandatory ownership and documentation

3. **Regular Audits**: Conduct periodic reviews to identify and address ownerless or poorly documented metrics

4. **Alert Ownership Alignment**: Ensure that alerts trigger for the specific teams that own the underlying metrics

The vague metric name in Clara's example—`latency_avg_all`—exemplifies poor governance. It fails to specify what service, operation, or timeframe is being measured, creating fundamental ambiguity. In financial systems, where precise understanding of performance and reliability is essential, this ambiguity represents significant operational risk.
## Panel 5: Sin #2: Orphaned Alerts - Alert Lifecycle Management
## Scene Description

**Sin #2: Orphaned Alerts** – Juana responds to a noisy alert only to discover there's no runbook. "Awesome. It's a riddle now."

*Expanded narrative: Juana pulls up the alert that triggered the incident response: "CRITICAL: PAYMENT_SVC_ERROR_RATE > threshold." She clicks the runbook link. Error 404—page not found. She searches the wiki. Nothing. She checks the documentation repository. Empty. "Awesome," she deadpans. "It's not an alert anymore. It's a riddle." She turns to the team. "An alert without a runbook is just a puzzle you're solving at 3 AM while customers get angrier."*

## Teaching Narrative

This scene highlights another destructive anti-pattern: alerts without context or guidance. Juana's experience demonstrates how alerts become orphaned from their purpose when they lack associated runbooks or documentation. This pattern transforms what should be clear operational guidance into confusing technical puzzles.

## Alert Lifecycle Management Explained

Alert Lifecycle Management is the systematic governance of alerts throughout their existence:

1. **Creation Standards**: Requiring complete documentation, including runbooks, for all new alerts

2. **Documentation Integration**: Ensuring that alerts directly link to relevant guidance and context

3. **Regular Review**: Periodically assessing alert effectiveness, accuracy, and documentation

4. **Retirement Processes**: Systematically removing alerts that no longer serve their purpose

In financial services, proper alert lifecycle management is essential for effective incident response. Banking operations require rapid, consistent handling of issues affecting money movement, account access, and regulatory compliance. Orphaned alerts directly undermine this capability.

## The 3 AM Factor

Juana's comment about "a puzzle you're solving at 3 AM" highlights a critical aspect of alert design: the human context in which alerts are received. Alerts often trigger during off-hours when cognitive capacity is reduced and support resources are limited. In this context, missing documentation doesn't just create inefficiency—it can render alerts completely ineffective.

## Banking Implementation Guidance

To implement alert lifecycle management in financial systems:

1. **Runbook Requirements**: Make runbooks mandatory for all production alerts

2. **Knowledge Integration**: Embed links to relevant documentation directly in alert notifications

3. **Alert Testing**: Regularly verify that runbooks and documentation remain accurate and accessible

4. **Documentation Ownership**: Assign clear responsibility for maintaining alert documentation

The broken link Juana encounters represents a common breakdown in alert management. As systems evolve, documentation often fails to keep pace, creating gradually increasing disconnects between alerts and their context. Financial institutions must treat alert documentation as critical operational infrastructure, not optional reference material.
## Panel 6: Sin #3: Logs That Lie - Telemetry Integrity
## Scene Description

**Sin #3: Logs That Lie** – Katherine highlights a 500 error log… with no trace ID, no request path, and no helpful message. "This might as well be in Morse code."

*Expanded narrative: Katherine finally locates log entries from the failing payment transactions. He projects them onto the screen: `ERROR 500: Request failed.` Nothing more—no transaction details, no customer information, no error codes from downstream systems. "This might as well be in Morse code," he says in frustration. "It tells us something failed but nothing about what, why, or how to fix it. The logs exist but tell us nothing useful—they lie by omission."*

## Teaching Narrative

This scene exposes yet another critical anti-pattern: logs that create the illusion of visibility while providing no actionable information. Katherine's discovery demonstrates how minimal error messages without context create a dangerous situation—the appearance of logging without the substance of observability.

## Telemetry Integrity Explained

Telemetry Integrity is the practice of ensuring that logs and metrics actually serve their intended purpose:

1. **Content Completeness**: Including all context needed to understand and act on the information

2. **Contextual Honesty**: Providing accurate representations of what actually occurred

3. **Diagnostic Adequacy**: Ensuring telemetry contains sufficient information to support troubleshooting

4. **Omission Awareness**: Actively identifying and addressing information gaps

In financial services, telemetry integrity is particularly critical. When payment transactions fail, logs must provide sufficient information to identify affected customers, transaction details, and failure points. Without this context, teams cannot effectively respond to incidents or meet regulatory requirements for transaction visibility.

## The Lie of Omission

Katherine's characterization of logs "lying by omission" highlights a subtle but critical distinction. Logs can be technically present and accurate but still fundamentally dishonest in their practical effect. When logs omit essential context, they create a false impression of visibility while actually obscuring understanding.

## Banking Implementation Guidance

To maintain telemetry integrity in financial systems:

1. **Contextual Requirements**: Define mandatory context fields for all log entries (transaction IDs, customer information, request details)

2. **Error Detail Standards**: Create specific guidelines for error logging that require actionable information

3. **Propagation Verification**: Regularly test that context is properly maintained across service boundaries

4. **Log Quality Monitoring**: Implement processes to detect and address deterioration in log quality

The generic "ERROR 500: Request failed" message Katherine discovers represents a complete telemetry integrity failure. In financial systems, this failure has consequences beyond operational inefficiency—it creates regulatory exposure by preventing proper documentation and understanding of transaction failures.
## Panel 7: Sin #4: Uptime Without User Success - Customer-Centric Observability
## Scene Description

**Sin #4: Uptime Without User Success** – Split screen shows 100% uptime for payment service but customers unable to complete transactions. "Congratulations, your metrics are perfect. Too bad they're measuring the wrong thing."

*Expanded narrative: Aisha displays a troubling comparison on the main screen. On the left: service uptime graphs showing 100% availability for the payment processing service. On the right: successful transaction rate showing near-zero completions. "Your metrics say everything's perfect," she notes. "Meanwhile, not a single customer can complete their transaction." Hector Alavaz nods grimly. "Congratulations, your metrics are perfect. Too bad they're measuring the wrong thing. Uptime without user success is just efficiently failing."*

## Teaching Narrative

This scene illustrates perhaps the most dangerous observability anti-pattern: confusing technical availability with business success. The stark contrast between perfect uptime metrics and failed transactions reveals how traditional infrastructure monitoring can create a completely false picture of system health. This pattern represents a fundamental misalignment between technical measurements and business reality.

## Customer-Centric Observability Explained

Customer-Centric Observability focuses on actual user outcomes rather than technical indicators:

1. **Success Metrics**: Measuring whether users can complete their intended tasks, not just whether systems are running

2. **Journey Instrumentation**: Tracking complete user paths rather than individual service health

3. **Outcome Alignment**: Ensuring that technical metrics directly connect to business outcomes

4. **Experience Integration**: Incorporating user perception and feedback into observability systems

In financial services, this approach is essential for both operational and business reasons. Banking systems exist to facilitate financial transactions—a system that's technically "up" but prevents customers from moving money has fundamentally failed its purpose, regardless of what infrastructure metrics claim.

## The Efficient Failure

Hector Alavaz's observation that "uptime without user success is just efficiently failing" perfectly captures the absurdity of this anti-pattern. Technical uptime becomes not just meaningless but actively misleading when disconnected from business outcomes.

## Banking Implementation Guidance

To implement customer-centric observability in financial systems:

1. **Transaction Success Rates**: Monitor the completion rates of key financial transactions by type and channel

2. **Journey Completion Metrics**: Track full customer journeys (login → account selection → transaction initiation → confirmation)

3. **Outcome-Based SLOs**: Define Service Level Objectives based on customer success rather than technical availability

4. **User Perception Correlation**: Regularly compare technical metrics with customer feedback and support tickets

The split screen visualization in this scene provides a powerful reminder of how easily traditional monitoring can mislead. Financial institutions must recognize that technical metrics only matter insofar as they reflect actual customer experience. A payment service with 100% uptime that processes 0% of transactions isn't succeeding—it's just failing with perfect reliability.
## Panel 8: Sin #5: "It's Always the Network" Syndrome - Bias-Free Investigation
### Scene Description
**Sin #5: "It's Always the Network" Syndrome** – Njeri presents historical data showing 90% of "network issues" were actually application problems. "Stop blaming my network for your code."

*Expanded narrative: Njeri presents her analysis with barely controlled frustration. Her graphs show that over the past year, 90% of incidents initially attributed to "network issues" were ultimately identified as application bugs, configuration errors, or database problems. "Stop blaming my network for your code," she states firmly. "Every minute we spend chasing network ghosts is a minute we're not fixing the actual problem. This isn't troubleshooting—it's superstition."*
### Teaching Narrative
This scene exposes a pervasive cultural anti-pattern in IT operations: default blame assignment based on history or bias rather than evidence. Njeri's data reveals how the common practice of blaming networks first creates not just inefficiency but active harm—delaying resolution by misdirecting investigation efforts. This pattern represents a failure of both process and culture.
#### Bias-Free Investigation Explained
Bias-Free Investigation is the practice of diagnosing issues based solely on evidence, not assumptions:

1. **Assumption Suspension**: Deliberately avoiding premature conclusions about root causes

2. **Data-Led Diagnosis**: Following evidence rather than historical patterns or team biases

3. **Systematic Elimination**: Methodically ruling out potential causes based on telemetry, not intuition

4. **Cross-Team Collaboration**: Working jointly across functional boundaries rather than assigning blame

In financial services, bias-free investigation directly impacts incident resolution time. When teams default to blaming networks, databases, or other common scapegoats, they waste critical minutes during outages—minutes that translate to failed transactions, frustrated customers, and potential regulatory issues.
#### The Superstition Factor
Njeri's characterization of default blame as "superstition" highlights its irrational nature. Like genuine superstitions, default blame patterns persist despite contradicting evidence because they provide psychological comfort—they transform complex, uncertain situations into simple, familiar ones, even when that simplicity is false.
### Banking Implementation Guidance
To implement bias-free investigation in financial systems:

1. **Evidence Requirements**: Establish formal processes requiring telemetry evidence before making causal claims

2. **Attribution Tracking**: Document and analyze initial blame assignments versus actual root causes

3. **Cross-Functional Diagnosis**: Form incident response teams that include representatives from all potential problem areas

4. **Blameless Postmortems**: Conduct retrospectives that focus on process and telemetry improvements rather than team blame

Njeri's 90% statistic powerfully illustrates how persistent "network blame" can be despite contradicting evidence. Financial institutions must recognize that these default blame patterns aren't just cultural quirks—they're significant operational risks that directly impact service restoration time and customer experience.
## Panel 9: Lesson Locked In - Observability Maturity
### Scene Description
**Lesson Locked In** – Hector Alavaz's closing line: "Avoid these sins or prepare for the volcano. And I mean a real one—because the auditors are coming."

*Expanded narrative: As the team implements fixes and payment service restoration begins, Hector Alavaz delivers his final assessment. "Today was expensive—in customer trust, operational costs, and reputation. But the regulatory audit next month will be much worse if these sins aren't addressed." He taps the whiteboard. "Avoid these sins or prepare for the volcano. And I mean a real one—because the auditors are coming." The team looks at each other with new understanding—their observability practices aren't just technical challenges but business and regulatory imperatives.*
### Teaching Narrative

This closing scene connects technical practices to their business and regulatory consequences. Hector Alavaz's volcano metaphor and explicit mention of auditors transforms observability from an engineering concern to a business imperative. This shift in framing helps the team understand that addressing these anti-patterns isn't optional—it's essential for the organization's regulatory standing and business continuity.

#### Observability Maturity Explained
Observability Maturity is the systematic development of observability capabilities aligned with business needs. The key stages of observability maturity can be summarized as follows:

```text
[ Observability Maturity Checklist ]
1. Capability Assessment:
   - Evaluate current practices against standards.
   - Identify strengths and weaknesses.

2. Gap Prioritization:
   - Rank issues based on impact and urgency.
   - Focus resources on critical shortcomings.

3. Continuous Improvement:
   - Regularly refine observability practices.
   - Implement feedback loops for sustained growth.

4. Regulatory Alignment:
   - Ensure compliance with industry regulations.
   - Maintain visibility into sensitive system behaviors.
```

In financial services, observability maturity has direct regulatory implications. Banking regulators increasingly expect financial institutions to maintain comprehensive visibility into system behavior, transaction flows, and failure modes. Mature observability practices aren't just operationally valuable—they're regulatory requirements.

#### The Audit Perspective
Hector Alavaz's explicit reference to auditors highlights an often-overlooked aspect of observability in regulated industries: external validation. Financial institutions must be able to demonstrate to regulators that they have appropriate controls and visibility into system behavior—particularly for systems handling customer funds or sensitive data.
### Banking Implementation Guidance
To develop observability maturity in financial systems:

1. **Maturity Assessment Framework**: Create a structured model for evaluating observability capabilities against industry standards

2. **Regulatory Mapping**: Explicitly connect observability practices to specific regulatory requirements

3. **Improvement Roadmap**: Develop a prioritized plan for addressing observability gaps over time

4. **Validation Mechanisms**: Implement processes to verify that observability improvements actually deliver expected capabilities

Hector Alavaz's volcano metaphor provides a powerful image of the consequences of ignoring observability sins—sudden, catastrophic failure. In financial services, this metaphor is particularly apt. Poor observability creates accumulated risk that may remain hidden until a major incident or audit reveals the full extent of the problem. By addressing the five sins proactively, teams can avoid both the operational volcanoes of major outages and the regulatory volcanoes of audit findings.