# Chapter 2: The Anatomy of Banking Incidents

## Panel 1: The Severity Spectrum - Classifying Banking Incidents
**Scene Description**: A bustling incident response war room where multiple screens display different banking systems in various states of alert. In the center, a diverse team huddles around a large digital board with a color-coded incident classification matrix. One engineer points to a flashing red alert on a payment gateway while another adjusts the incident severity level based on a structured checklist. A clock prominently shows 09:37 AM, and a counter indicates "Customer Impact: 12,450 transactions affected."

### Teaching Narrative
Understanding the anatomy of banking incidents begins with proper classification. Unlike traditional IT monitoring which often uses technical thresholds to determine severity (CPU > 90% = High), SRE incident classification in banking must integrate both technical signals and business impact. The Severity Spectrum framework provides a structured approach to incident classification that accounts for the unique nature of financial services disruptions.

In the banking domain, incidents fall across a spectrum from P1 (critical/all-hands) to P5 (minor/informational). This classification isn't arbitrary - it's an evidence-based assessment combining:
1. Functional impact (which banking services are affected)
2. Customer reach (how many users or transactions are impacted)
3. Financial exposure (actual or potential monetary impact)
4. Regulatory implications (compliance or reporting requirements triggered)
5. Duration and trend (is the situation stable, improving, or degrading)

This multi-dimensional approach transforms vague terms like "major incident" into precise, actionable classifications that drive appropriate response protocols. When transitioning from production support to SRE, mastering this classification framework is essential to ensure proportional response and resource allocation.

## Panel 2: Transaction Flow Mapping - Understanding Banking System Interconnections
**Scene Description**: An SRE team is gathered around a large interactive display showing a complex transaction flow diagram. The visualization traces a customer payment journey across multiple systems: from the mobile app, through the API gateway, authentication service, payment processor, core banking system, to partner banks and finally the central bank settlement. Color-coded paths show the normal flow in green, with one segment highlighted in red indicating an incident area. A senior engineer uses hand gestures to expand a section, revealing detailed dependency relationships between components.

### Teaching Narrative
Traditional monitoring focuses on individual components - databases, servers, or applications. In contrast, SRE incident analysis requires understanding the complete transaction flow across interconnected banking systems. This systemic view is crucial because banking incidents rarely exist in isolation; they cascade through integrated services.

Transaction Flow Mapping is a critical SRE practice for understanding banking incidents. It transforms abstract technical failures into visible disruptions of specific financial journeys. By mapping how transactions traverse systems, SREs can quickly:
1. Identify upstream and downstream dependencies
2. Recognize failure points in customer journeys
3. Determine the true scope of an incident
4. Predict cascade effects before they occur

When a banking incident occurs, the flow map becomes the central investigation tool, revealing how a localized issue (like an authentication service slowdown) impacts broader business functions (payment processing, account access). For former production support engineers, developing this systemic visualization skill marks a key evolution toward SRE thinking, moving beyond component-level troubleshooting to transaction-level analysis.

## Panel 3: Impact Quantification - Measuring What Matters in Banking Incidents
**Scene Description**: A dashboard meeting room where business and technical teams face each other across a table. The wall displays show dual metrics: technical graphs (error rates, latency, CPU) on one side and business metrics (transaction value affected, customer impact count, revenue at risk) on the other. An SRE is drawing connecting lines between specific technical failures and their corresponding business impacts, while a banking business analyst nods in understanding. A calculator application on a tablet shows financial impact formulas being utilized in real-time.

### Teaching Narrative
A fundamental shift in moving from production support to SRE is mastering the art of impact quantification. Traditional monitoring focuses on technical metrics like availability percentages or system errors. SRE incident analysis requires translating these technical signals into business impact metrics that banking executives, regulators, and customers care about.

Impact quantification in banking requires developing a "bilingual" capability - speaking both technical and financial languages. This means converting:
- Error rates into affected transaction values
- Latency spikes into customer experience degradation
- Failed API calls into financial exposure figures
- System availability into regulatory compliance status

This translation capability transforms incident response from a technical exercise to a business-aligned function. When quantifying impact, precision matters - "approximately 2,000 payment transactions worth €1.2M failed during the 23-minute incident window" is significantly more valuable than "the payment system had issues." 

For banking SREs, this quantification becomes the foundation for incident prioritization, resource allocation, and postmortem analysis. It drives decisions about whether to wake additional teams at 3AM or implement potentially risky mitigations during trading hours.

## Panel 4: Temporal Analysis - The Lifecycle of Banking Incidents
**Scene Description**: A timeline visualization stretches across a wall, showing the complete lifecycle of a banking incident from initial detection to full resolution. The timeline is marked with key events: first alert, incident declaration, investigation milestones, mitigation attempts (both successful and failed), communication points, and final resolution. A small team reviews the timeline while adding annotations at various points. One engineer uses a laser pointer to highlight patterns in the temporal data, particularly focusing on the gap between first symptoms and incident declaration.

### Teaching Narrative
Banking incidents unfold over time, and understanding their temporal dynamics is crucial for effective SRE response. Unlike production support, which often focuses on point-in-time troubleshooting, SRE incident analysis requires comprehensive temporal mapping - understanding how incidents evolve from initial symptoms through escalation, response, mitigation, and resolution.

Temporal analysis transforms incident response from reactive firefighting to strategic management. By mapping the incident lifecycle, SREs can identify:
1. Detection gaps - how long between first symptoms and alert triggering
2. Response efficiency - time from alert to appropriate action
3. Escalation patterns - how quickly and effectively was the incident escalated
4. Mitigation effectiveness - which actions improved or worsened the situation
5. Resolution pathways - what ultimately solved the problem

In banking systems, where timing is often critically important (trading hours, payment processing windows, end-of-day settlements), temporal analysis provides essential context. A 5-minute outage during peak trading hours may have more significant impact than a 30-minute outage during off-hours. Similarly, incidents that span critical financial boundaries (crossing midnight for settlement systems or crossing quarter-end for reporting systems) have unique implications that must be understood.

## Panel 5: Incident Archaeology - Reconstructing Banking System Failures
**Scene Description**: A digital forensics lab environment where SREs are conducting a detailed incident reconstruction. Multiple screens display timeline-synchronized logs, metrics, and traces from various banking systems. One engineer manipulates a 3D visualization showing the propagation of failures across services. Another examines a "digital dig" table where system state snapshots are arranged in chronological layers. A third team member is constructing a narrative document titled "Incident Reconstruction: Market Data Latency Cascade Event" with precise timestamps and service correlations.

### Teaching Narrative
When banking incidents occur, they leave digital evidence across systems - logs, metrics, traces, and state changes. Traditional production support might examine individual log files or error messages, but SRE incident analysis requires methodical "archaeology" - reconstructing what happened by synthesizing evidence from multiple sources.

Incident Archaeology transforms incident response from opinion-based debates ("I think the database was slow") to evidence-based investigation ("The database read latency increased by 240ms at 14:23:05, seven seconds after the cache eviction event"). This methodical reconstruction involves:

1. Evidence collection - gathering logs, metrics, and state changes across systems
2. Timeline correlation - aligning events from different systems with precise timestamps
3. Causal chain identification - mapping how failures propagated through systems
4. State reconstruction - understanding what the system state was at key moments
5. Gap analysis - identifying missing information needed for complete understanding

For banking systems, where transactions may flow through dozens of services and multiple organizational boundaries, this archaeological approach is essential. It allows SREs to differentiate between root causes, contributing factors, and coincidental issues - preventing the common trap of addressing symptoms rather than causes.

The skill of incident archaeology marks a key evolution from production support to SRE thinking - moving from "what's broken now" to "how did this failure emerge and propagate through our financial systems."

## Panel 6: Stakeholder Impact Mapping - The Human Side of Banking Incidents
**Scene Description**: A collaborative workshop where SREs are creating a comprehensive stakeholder impact map for a recent incident. The room features a large touchscreen wall displaying concentric circles representing different stakeholder groups: inner circles show direct internal teams (operations, development, risk), middle circles show business units and partners, and outer circles represent customers and regulators. Each segment is color-coded by impact severity. Team members are adding detailed impact notes for each stakeholder group, with particular attention to regulatory reporting requirements highlighted with compliance reference numbers.

### Teaching Narrative
Banking incidents don't just affect systems - they affect people. Traditional monitoring focuses primarily on technical components, but SRE incident analysis must comprehensively map human stakeholder impacts. This stakeholder-centric view transforms incident handling from a purely technical exercise into a business-aligned, customer-focused discipline.

Stakeholder Impact Mapping creates a comprehensive view of who is affected by an incident and how. In banking environments, this typically includes:

1. Internal technical teams - operations, development, infrastructure
2. Business units - retail banking, trading, lending, treasury
3. Customers - segmented by type, region, or impact level
4. Partners - payment processors, correspondent banks, service providers
5. Regulators - financial authorities, central banks, data protection agencies

For each stakeholder group, SREs must understand:
- What specific impact they experience
- When and how they should be notified
- What information they need during the incident
- What follow-up they require after resolution

This comprehensive stakeholder mapping is particularly crucial in banking, where incidents trigger specific regulatory reporting requirements, potentially with strict timelines. For example, certain payment system outages must be reported to central banks within specific timeframes, with detailed impact assessments.

For engineers transitioning from production support to SRE, developing this stakeholder consciousness represents a significant evolution - expanding focus from technical systems to the human ecosystem surrounding those systems.

## Panel 7: Incident Typing - Patterns and Archetypes in Banking System Failures
**Scene Description**: A knowledge management session where an experienced SRE team is developing a banking incident taxonomy. The room has walls covered with categorized incident summaries on digital cards. Team members are grouping similar incidents into clusters labeled with archetypal patterns: "Payment Gateway Timeout Cascade," "Settlement Reconciliation Drift," "Identity Verification Bottleneck," and others. One engineer is annotating each pattern with common characteristics, while another updates a reference handbook titled "Banking Incident Pattern Library." A visualization shows how specific incidents map to these archetypal patterns.

### Teaching Narrative
As banking SREs gain experience with incidents, patterns emerge. Traditional production support might treat each incident as a unique occurrence, but SRE incident analysis benefits from pattern recognition - identifying common archetypes that share characteristics, causes, and resolution approaches. This pattern-based approach transforms incident response from perpetual firefighting to systematic pattern matching and resolution.

Incident Typing develops a banking-specific "pattern library" of common failure modes. These archetypal patterns include:

1. **Capacity Threshold Breaches** - when volume exceeds system capabilities (payment processing overload during peak periods)
2. **Data Synchronization Failures** - when critical financial data becomes inconsistent (settlement vs. clearing discrepancies)
3. **Dependency Chain Collapses** - when third-party service failures cascade (payment processor outages)
4. **Configuration Drift Incidents** - when systems gradually move out of alignment (trading parameter mismatches)
5. **Release Transition Failures** - when new deployments introduce issues (core banking system upgrades)
6. **Data Quality Degradation** - when information integrity issues affect processing (duplicate transaction IDs)
7. **Timing Sensitivity Failures** - when temporal factors create issues (end-of-day processing collisions)

For each pattern, experienced SREs develop standard investigation approaches, common questions, typical telemetry signals, and proven resolution strategies. This pattern library becomes an invaluable knowledge base, allowing teams to leverage collective experience rather than rediscovering solutions.

For banking professionals transitioning from production support to SRE, developing this pattern recognition capability represents a key evolution from treating each incident as a unique emergency to recognizing familiar patterns and applying proven approaches.