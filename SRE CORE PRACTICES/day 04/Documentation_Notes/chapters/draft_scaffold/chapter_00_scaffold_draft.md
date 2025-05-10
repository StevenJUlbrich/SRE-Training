# Chapter 0: From Production Support to Observability Thinking

## Panel 1: The Invisible Customer Journey - Beyond Component Health
### Scene Description

 A banking support center where two teams work side by side. The monitoring team stares at dashboards showing all green system metrics (CPU, memory, network) for payment processing systems. Meanwhile, the customer service team's phones light up with complaints about failed mobile transfers despite receiving success messages. The disconnect between system metrics and customer reality is visibly frustrating both teams.

### Teaching Narrative
Production support traditionally focuses on component health—ensuring servers are running, databases are responding, and networks are connected. However, this approach creates dangerous blind spots for customer journeys that span multiple systems. In banking especially, a transaction can appear successful in one system while failing silently in another, leaving customers with a broken experience despite all monitoring dashboards showing green. Observability thinking shifts our focus from isolated components to end-to-end customer journeys.

## Panel 2: Reactive to Proactive - Anticipating Issues Before Impact
### Scene Description

 Split screen showing two approaches to the same trading platform incident. On the left, a production support engineer responds to urgent escalations after customers report trade failures. On the right, an SRE engineer investigates an anomaly in settlement system response patterns noticed during routine analysis, addressing the issue before any customer impact occurs.

### Teaching Narrative
The fundamental mindset shift from production support to SRE is moving from reactive firefighting to proactive system improvement. Traditional support waits for alerts to trigger or customer complaints to escalate before investigating issues. Observability thinking enables engineers to identify unusual patterns, emerging bottlenecks, and potential failures before they impact customers. This shift is particularly valuable in financial services, where preventing a single outage can preserve millions in transactions and maintain institutional trust.

## Panel 3: Question-Driven Investigation - Beyond Known Failure Modes
### Scene Description

 A banking support team struggles with a new mobile banking problem not covered in existing runbooks. A whiteboard shows their approach evolving from "Which component is failing?" to more nuanced questions: "How does a successful login flow differ from a failing one?", "What changed in the authentication service behavior over the past hour?", and "What other services are affected by this pattern?"

### Teaching Narrative
Production support relies heavily on predefined runbooks and known failure modes—effective for familiar problems but limiting for novel issues. Observability thinking embraces a question-driven approach, enabling engineers to explore system behavior through progressive hypothesis testing. Rather than jumping to conclusions based on alert thresholds, SRE engineers follow evidence trails and adapt their investigation based on what the data reveals. This exploratory mindset is essential for troubleshooting complex, interconnected banking systems where issues rarely follow predefined patterns.

## Panel 4: From Silos to System Views - Connecting Related Signals
### Scene Description

 An incident room where a legacy approach is being transformed. Initially, separate teams examine isolated data: database logs, application server metrics, network traces, and customer reports—all disconnected. A new observability approach shows these same signals correlated by transaction ID on a unified timeline, revealing how a database slowdown cascades into API timeouts, multiple retries, and ultimately failed payments.

### Teaching Narrative
Traditional production support often operates in technology silos, with separate teams examining their own components in isolation. Observability breaks down these barriers by connecting related signals across the technology stack. By correlating events using shared identifiers, engineers can see how issues propagate through distributed systems and understand true cause-effect relationships. In banking, where transactions flow through dozens of specialized systems, this connected perspective is essential for understanding complex failures that cross organizational boundaries.

## Panel 5: Evidence Over Opinion - Data-Driven Decisions
### Scene Description

 A post-incident review meeting where team members debate the cause of a failed batch processing job. Instead of the traditional "blame game" with competing opinions, an engineer presents a timeline visualization showing exactly how configuration changes, increased transaction volume, and database lock contention combined to create the failure. The evidence transforms the discussion from finger-pointing to collaborative problem-solving.

### Teaching Narrative
Production support environments often rely on expert intuition and experience-based opinions when diagnosing complex issues. While valuable, this approach can lead to confirmation bias and incomplete analysis. Observability thinking prioritizes evidence over opinion, creating a culture where decisions are driven by data rather than hierarchy or persuasiveness. This evidence-based approach reduces unproductive blame, accelerates problem resolution, and enables continuous learning. For banking teams with complex stakeholder environments and stringent reliability requirements, this cultural shift leads to more effective incident management and system improvement.

## Panel 6: Breaking the Binary - Understanding System Gray Areas
### Scene Description

 A monitoring dashboard shows a credit card authorization service as "100% Available" with a binary green status. Next to it, an observability view reveals a more nuanced reality: while technically available, 15% of transactions take over 3 seconds (frustrating customers), 8% require multiple authorization attempts, and mobile transactions are completing 40% slower than web transactions.

### Teaching Narrative
Traditional monitoring enforces a binary view—systems are either "up" or "down," "healthy" or "failing." Observability embraces the reality that modern systems operate in shades of gray with degraded states that affect customers without triggering traditional alerts. By measuring customer experience across multiple dimensions (latency, error rates, success percentages, etc.), SRE teams can identify and address "gray failures" that traditional monitoring would miss. This nuanced perspective is crucial for banking services where subtle degradations can significantly impact customer satisfaction and transaction completion rates.

## Panel 7: Building the Bridge - Evolving from Support to SRE
### Scene Description

 A learning journey visualization showing a production support engineer gradually incorporating observability practices. The journey begins with basic monitoring dashboard checks, progresses through investigating logs for patterns, then to analyzing metrics for trends, and finally to using distributed traces to understand complex interactions. Small wins and incremental improvements mark each stage of the journey.

### Teaching Narrative
The transition from production support to SRE observability thinking is not a binary switch but a progressive journey. Each step builds on existing skills while introducing new perspectives. Support engineers already possess valuable system knowledge, troubleshooting instincts, and customer impact understanding—all essential foundations for effective observability. By gradually incorporating new tools, techniques, and thought patterns, engineers can evolve their approach without abandoning what already works. This incremental adoption reduces resistance while delivering increasing value to both engineering teams and banking customers.