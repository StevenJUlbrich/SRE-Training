# Chapter 3: Service Level Indicators, Objectives, and Agreements

## Panel 1: What Really Matters?

**Scene Description**: Team brainstorming session on whiteboard defining critical signals for ATM services. Visual journey from raw metrics to meaningful indicators about customer experience.

### Teaching Narrative
Service Level Indicators (SLIs) are the foundation of effective reliability engineering. These carefully selected metrics directly measure customer experience, not just system health. For banking services, SLIs must reflect what truly matters to customers - can they complete their banking transactions successfully, quickly, and consistently? Raw technical metrics only become meaningful SLIs when they connect to these fundamental customer needs.

### Common Example of the Problem
A bank's ATM operations team tracks dozens of technical metrics (network connectivity, cash dispenser status, card reader function) but lacks a cohesive view of customer experience. When issues occur, there's disagreement about severity—is an ATM with a working cash dispenser but failing receipt printer "operational" or "degraded"? Customer complaints focus on issues the team doesn't even measure, like accurate cash counting or deposit recognition.

### SRE Best Practice: Evidence-Based Investigation
Define a small set of meaningful SLIs that directly reflect customer experience. For ATM services, this means tracking complete transaction success rates rather than individual component health. Gather data from customer support to identify what customers actually care about. Create composite SLIs that combine multiple technical metrics into meaningful customer journey measurements. Regularly review and refine SLIs based on changing business needs.

### Banking Impact
For ATM services, poorly chosen SLIs can significantly impact customer trust and operational efficiency. Cash availability, transaction success rates, and service uptime directly affect customer experience and branch operations. Regulatory requirements for ATM availability add compliance dimensions that technical teams often overlook. Without customer-focused SLIs, teams optimize for metrics that don't improve customer satisfaction.

### Implementation Guidance
1. Create composite SLIs that assess complete customer journeys (card insertion to cash dispensed)
2. Develop weighted availability metrics that consider location and time-of-day importance
3. Implement business-hour vs. off-hours SLIs that align with customer expectations
4. Build dashboards that show SLI performance against objectives in customer terms
5. Establish regular reviews of SLI effectiveness with business stakeholders

## Panel 2: The Impossible Promise

**Scene Description**: SRE negotiating with product team on realistic objectives for payment systems. Visual shows trade-off graph with reliability vs. velocity/cost and "five nines" highlighted.

### Teaching Narrative
Service Level Objectives (SLOs) transform SLIs into target performance levels that define success. While SLIs tell you what's happening, SLOs define what "good enough" looks like. In banking, SLOs must balance customer expectations, technical feasibility, and economic reality. The critical insight is that different banking services require different reliability targets based on their criticality and customer impact.

### Common Example of the Problem
A bank's payment processing team insists on "five nines" reliability (99.999%, or 5 minutes downtime per year) for all payment systems without differentiation. This demand fails to consider the vastly different costs of achieving this reliability level for different payment types. High-value wire transfers might justify this target, but applying it to non-critical informational APIs creates unsustainable engineering burden and slows innovation.

### SRE Best Practice: Evidence-Based Investigation
Implement tiered SLO frameworks that match reliability requirements to business criticality and transaction types. Use historical data to establish realistic baselines before setting targets. Create clear financial models showing the cost of incremental reliability improvements. Introduce error budgets that allow for calculated risk-taking and innovation. Educate stakeholders about the reliability/innovation trade-off.

### Banking Impact
Unrealistic reliability targets in payment systems create multiple problems: excessive spending on over-engineering non-critical systems, innovation paralysis due to fear of any change, and paradoxically, lower actual reliability as teams game metrics or focus on the wrong improvements. When all payment types have identical SLOs regardless of criticality, resources are misallocated and truly critical systems may receive insufficient attention.

### Implementation Guidance
1. Create a tiered SLO framework for different payment types based on criticality
2. Develop cost models demonstrating the exponential investment required for reliability increments
3. Implement error budgets that balance reliability with innovation velocity
4. Establish different SLOs for different aspects of the same service (availability vs. latency)
5. Create education programs for business stakeholders about reliability economics

## Panel 3: The Regulatory Review

**Scene Description**: Meeting with compliance team about service guarantees. Visual shows hierarchy diagram with internal SLOs supporting external SLAs and regulatory requirements.

### Teaching Narrative
Service Level Agreements (SLAs) are the contractual commitments made to customers or partners about service performance. In banking, these agreements exist within a complex regulatory framework that adds additional requirements and consequences. The relationship between internal SLOs and external SLAs is critical—SLOs must be stricter than SLAs to provide buffer against unexpected issues and ensure contractual and regulatory compliance.

### Common Example of the Problem
A bank implements customer-facing SLAs for transaction processing times without proper internal SLOs to support them. When degradation occurs, the bank violates customer agreements and triggers regulatory reporting requirements. The disconnect occurs because technical teams set internal targets based on average performance, while SLAs and regulations are based on worst-case performance and hard deadlines for specific transaction types.

### SRE Best Practice: Evidence-Based Investigation
Map internal SLIs and SLOs to regulatory requirements and customer SLAs with appropriate buffers. Implement specific metrics for compliance-related functions. Create clear visibility into regulatory reporting thresholds and automate notifications to compliance teams. Involve legal and compliance stakeholders in SLO design to ensure alignment with external obligations. Create a unified framework that connects technical operations to business commitments.

### Banking Impact
Regulatory misalignment in service level definitions creates significant compliance risks for financial institutions. Penalties for missed reporting deadlines or inadequate incident documentation can exceed the direct impact of the technical issue itself. Customer-facing SLAs that aren't supported by appropriate internal SLOs may create contractual liabilities or trigger regulatory scrutiny. The reputational damage from missed SLAs can far outweigh the technical severity.

### Implementation Guidance
1. Create a regulatory mapping document connecting technical metrics to compliance requirements
2. Implement automated reporting that triggers when incidents approach regulatory thresholds
3. Establish joint review processes with compliance, legal, and SRE teams for service level definitions
4. Set internal SLOs at least 10% stricter than external SLAs to provide safety margin
5. Create clear escalation paths to compliance teams based on metric thresholds

## Panel 4: The Error Budget Negotiation

**Scene Description**: Development and operations teams reviewing a graph showing recent service performance against SLOs. Visual highlights remaining error budget and proposed feature deployment schedule.

### Teaching Narrative
Error budgets transform reliability from a binary "working/broken" model to a quantitative approach that allows for calculated risk-taking. By defining how much unreliability is acceptable over time, error budgets create a shared framework for balancing reliability and innovation. This concept is particularly powerful in banking, where different services have dramatically different reliability requirements.

### Common Example of the Problem
A bank's mobile app team is caught in a cycle of reliability conflicts. Operations teams resist any changes that might impact stability, while development teams push for rapid feature deployment to meet competitive demands. Without a quantitative framework for making these trade-offs, decisions become political rather than data-driven. High-profile outages lead to overcorrection and innovation paralysis, while gradual degradation goes unaddressed.

### SRE Best Practice: Evidence-Based Investigation
Implement error budgets based on agreed SLOs for each service. Track budget consumption over time and use it to guide deployment decisions. Create different error budgets for different aspects of performance (availability, latency) and different customer impacts. Establish clear policies for what happens when budgets are exhausted or have excess. Use error budget reviews to drive continuous improvement in both reliability and deployment processes.

### Banking Impact
In financial services, error budgets create a sustainable approach to innovation while protecting critical customer experiences. They allow appropriate risk-taking for competitive features while ensuring core financial functions remain reliable. When implemented effectively, they reduce both unnecessary caution and reckless deployment, optimizing the balance between stability and innovation for each banking service based on its specific requirements.

### Implementation Guidance
1. Calculate error budgets based on service criticality and customer impact
2. Create dashboards showing budget consumption rates and projections
3. Implement budget-based deployment gates for different risk levels
4. Establish policies for budget exhaustion that balance business and technical needs
5. Use excess error budget to drive controlled experimentation and learning

## Panel 5: The SLI Workshop

**Scene Description**: Cross-functional team evaluating potential SLIs for a new banking service. Visual shows evaluation criteria: measurable, customer-focused, controllable, and predictive of issues.

### Teaching Narrative
Choosing the right Service Level Indicators (SLIs) is both an art and a science. Effective SLIs must be measurable, directly related to customer experience, within the team's control to improve, and predictive of issues before they become severe. This selection process requires collaboration between technical, business, and customer experience teams to ensure the metrics truly reflect what matters.

### Common Example of the Problem
A bank launches a new wealth management platform and struggles to define appropriate SLIs. Technical teams focus on system metrics like database response time, business teams want to measure customer portfolio performance, and support teams care about issue resolution speed. Without a structured approach to SLI selection, they create dozens of disconnected metrics that don't provide a cohesive view of service health or guide improvement efforts.

### SRE Best Practice: Evidence-Based Investigation
Conduct structured SLI workshops with cross-functional representation. Evaluate potential SLIs against specific criteria: direct customer impact, technical feasibility, controllability, and predictive value. Start with customer journeys and work backward to technical implementation. Limit SLIs to a small number (3-5) per service to maintain focus. Test SLIs against historical incidents to verify their effectiveness at detecting problems.

### Banking Impact
For banking services, poorly chosen SLIs create significant blind spots and misdirected efforts. When wealth management platforms measure the wrong things, teams may optimize for speed at the expense of accuracy, or focus on rare edge cases while missing common customer pain points. Regulatory requirements may be overlooked, creating compliance risks. Customer trust erodes when the bank's internal view of performance doesn't match customer experience.

### Implementation Guidance
1. Map critical customer journeys for each banking service
2. Identify potential failure modes and their customer impact
3. Define SLIs that directly measure successful journey completion
4. Test SLI sensitivity by analyzing historical incidents
5. Create balanced SLI sets that cover availability, latency, and accuracy

## Panel 6: The SLO Review

**Scene Description**: Quarterly SLO review meeting showing performance trends across critical banking services. Visual highlights services meeting targets, those consuming error budgets rapidly, and recommendations for adjustment.

### Teaching Narrative
Service Level Objectives aren't set-and-forget targets; they require regular review and adjustment based on changing business needs, customer expectations, and technical capabilities. The SLO review process turns reliability management from a reactive to a proactive discipline, identifying trends before they become problems and ensuring alignment with business priorities.

### Common Example of the Problem
A bank sets SLOs for its online banking platform but never revisits them. Over time, several problems emerge: some services consistently miss their targets, creating alert fatigue and reduced urgency; others easily exceed targets, potentially indicating wasted engineering effort; and changing customer expectations (like faster mobile payments) aren't reflected in outdated targets. Without regular reviews, the SLO framework loses credibility and effectiveness.

### SRE Best Practice: Evidence-Based Investigation
Implement quarterly SLO reviews with technical and business stakeholders. Analyze performance trends against targets and identify systematic gaps. Adjust targets based on changing business priorities and technical capabilities. Review and refine error budget policies based on actual usage patterns. Use the review process to drive continuous improvement in both reliability engineering and service design.

### Banking Impact
For banking services, regular SLO reviews ensure reliability engineering remains aligned with customer needs and business priorities. They provide early warning of degrading systems before customers notice, create accountability for persistent reliability issues, and prevent overinvestment in services that already exceed requirements. The review process also creates valuable dialogue between technical and business teams about reliability trade-offs.

### Implementation Guidance
1. Schedule quarterly SLO reviews with cross-functional participation
2. Prepare trend analyses showing performance against targets over time
3. Identify services consistently missing or exceeding targets for adjustment
4. Create action plans for services with negative trends
5. Document decisions and rationale for target adjustments

## Panel 7: The Dashboard Translation

**Scene Description**: SRE team creating executive SLO dashboards from technical metrics. Visual shows the progression from raw technical data to business-relevant reliability visualization.

### Teaching Narrative
The technical implementation of SLIs and SLOs must be translated into business-relevant visualizations to be effective across the organization. This translation process connects technical reality to business outcomes, enabling executives to understand service health, make informed decisions about reliability investments, and communicate effectively with customers and regulators.

### Common Example of the Problem
A bank implements comprehensive SLI/SLO frameworks at the technical level, but executives and business stakeholders can't interpret the resulting dashboards. During major incidents, technical teams struggle to explain impact in business terms, leading to miscommunication with customers and regulators. Investment decisions about reliability improvements lack clear business justification, resulting in either underinvestment or misdirected resources.

### SRE Best Practice: Evidence-Based Investigation
Create multi-level dashboards that translate technical SLIs into business impact visualizations. Develop different views for different audiences: detailed technical data for engineers, service health summaries for managers, and business impact overviews for executives. Use consistent visualization approaches that clearly show performance against objectives. Incorporate business context such as customer counts, transaction values, and regulatory thresholds.

### Banking Impact
For financial institutions, effective SLO visualization directly impacts decision quality and communication effectiveness. During incidents, clear business-impact dashboards enable appropriate response scaling, accurate customer and regulatory communications, and effective resource allocation. For strategic planning, they connect reliability investments to business outcomes, ensuring resources flow to the most critical services and most impactful improvements.

### Implementation Guidance
1. Create role-based dashboard views for different stakeholders
2. Translate technical metrics into business terms (e.g., "failed transactions" rather than "API errors")
3. Incorporate financial impact estimates for reliability shortfalls
4. Use consistent visualization patterns across services
5. Include trend indicators to show improvement or degradation over time