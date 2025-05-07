# Chapter 2: The Four Golden Signals

## Panel 1: Why Is Everyone Calling?

**Scene Description**: Call center overwhelmed with complaints about slow transactions. Visual shows a distribution graph comparing p50 latency (acceptable) versus p99 latency (terrible) with customer faces expressing different experiences.

### Teaching Narrative
Latency measures how long it takes to service a request. In SRE practice, we distinguish between successful request latency and failed request latency, as they tell different stories about system health. Percentile measurements (p50, p90, p99) are critical for understanding the customer experience, as averages hide important distribution details.

### Common Example of the Problem
An investment platform's average response time looks acceptable at 300ms, but customer complaints about sluggish performance are increasing during market volatility. The operations team is confused because their average latency metrics show no problems. They don't realize that while most transactions complete quickly, a significant percentage of users are experiencing multi-second delays precisely when they need the platform most.

### SRE Best Practice: Evidence-Based Investigation
Always measure and alert on tail latency (high percentiles like p90 and p99) in addition to averages. Segment latency by request type, customer tier, and geographic region to identify patterns. Implement distributed tracing to identify which components contribute most to slow requests. Compare successful vs. failed request latency to identify timeout issues.

### Banking Impact
In investment platforms, latency has a direct correlation with abandonment rates, trading losses, and customer satisfaction. During market volatility, even moderate latency increases can prevent customers from executing time-sensitive trades, potentially costing them significant amounts of money. High-value customers experiencing delays may permanently move their business to competitor platforms.

### Implementation Guidance
1. Implement percentile-based latency measurements (p50, p90, p99) for all critical services
2. Create separate latency SLOs for different transaction types based on customer expectations
3. Deploy distributed tracing across services to identify latency contributions
4. Establish latency budgets for each component in critical paths
5. Implement real-user monitoring to correlate actual customer experience with synthetic tests

## Panel 2: The Unexpected Holiday

**Scene Description**: On-call engineer puzzled by traffic spike on non-payday Friday. Visual shows traffic graphs with overlay of calendar events and news headlines about government stimulus payments.

### Teaching Narrative
Traffic measures the demand placed on your system, typically represented as requests per second. Understanding traffic patterns is essential for capacity planning and anomaly detection. In banking systems, traffic often follows predictable patterns tied to business cycles, but can also show unexpected variations due to external events outside the organization's control.

### Common Example of the Problem
A bank's payment processing system experiences unexpected load spikes that cause transaction slowdowns. The operations team has sized the system for typical workloads and known peak times like paydays, but cannot explain or predict these irregular surges. Without proper traffic analysis, they're constantly in reactive mode, scrambling to add capacity after problems occur.

### SRE Best Practice: Evidence-Based Investigation
Analyze traffic patterns across multiple time dimensions (hourly, daily, weekly, monthly) to identify cyclical patterns. Correlate traffic spikes with external events (market announcements, promotional activities, social media mentions). Implement anomaly detection that accounts for multiple seasonality patterns. Segment traffic by user type, service, and geographic region.

### Banking Impact
Unpredictable traffic patterns in banking can lead to transaction processing delays, incomplete batch operations, or even system outages during critical financial events. When payment processing slows during unexpected high-volume periods like government stimulus payments, merchants lose sales, consumers face declined transactions, and the bank's reputation suffers. Regulatory reporting may be required for processing delays that affect settlement times.

### Implementation Guidance
1. Develop traffic forecasting models that incorporate business calendars and external events
2. Implement auto-scaling based on leading traffic indicators rather than resource utilization
3. Create traffic dashboards that overlay historical patterns with current traffic
4. Establish alerting on traffic anomalies, not just absolute thresholds
5. Build communication channels with business teams to get advance notice of marketing campaigns or expected traffic-driving events

## Panel 3: The Silent Failure

**Scene Description**: SRE investigating why fund transfers are missing. Visual shows error logs with successful HTTP 200 responses but failed database commits, resulting in money appearing to leave accounts but not arriving at destination.

### Teaching Narrative
Errors represent the rate of failed requests. In SRE practice, we define errors as any request that fails to meet its SLO, not just technical failures. This includes requests that return error codes, timeout, return incorrect data, or technically succeed but fail to satisfy the user's need. In banking systems, error detection is particularly critical as it directly impacts financial transactions.

### Common Example of the Problem
A banking platform shows a low error rate in monitoring because it only counts HTTP 500 responses as errors. However, customers are reporting failed transfers that the system doesn't capture. Investigation reveals that many failed business operations return HTTP 200 status codes with error messages in the response body, while others time out at the client but appear successful in server logs. Money seems to leave accounts but doesn't arrive at destinations.

### SRE Best Practice: Evidence-Based Investigation
Define errors from the customer perspective, not just technical failure modes. Implement business-level error tracking that captures failed operations regardless of HTTP status code. Create a comprehensive error taxonomy that distinguishes between different failure types (system errors, validation errors, business rule failures). Track error budgets based on customer impact.

### Banking Impact
Undetected errors in fund transfer systems can lead to serious financial and regulatory consequences. Transfer errors may result in missing transactions, reconciliation failures, or incorrect account balances. Repeated small-scale errors erode customer confidence and increase support costs, while major errors can trigger regulatory scrutiny and penalties. The financial impact compounds when errors affect customer finances directly.

### Implementation Guidance
1. Implement client-side error tracking to capture user-perceived failures
2. Define custom error metrics that align with business operations, not just technical responses
3. Create error budgets for each critical service and track consumption over time
4. Establish error taxonomies that help prioritize different failure types
5. Build comprehensive dashboards that show error rates by service, operation type, and customer segment

## Panel 4: The Creeping Slowdown

**Scene Description**: Team investigating gradually increasing latency over weeks. Visual shows connection pool graphs with increasing wait times as utilization approaches 80% during month-end batch processing.

### Teaching Narrative
Saturation measures how "full" your system is, indicating how close you are to capacity limits. Unlike utilization which shows average resource usage, saturation helps identify bottlenecks before they cause failures. In complex systems, resource constraints often appear gradually and in unexpected places, making them particularly dangerous if not monitored properly.

### Common Example of the Problem
A banking system experiences gradually increasing response times over several weeks, despite no significant changes in traffic or error rates. The operations team focuses on CPU and memory metrics, which show moderate utilization. They miss the real issue: database connection pool saturation that occurs when connections aren't being properly released, eventually causing transactions to queue during month-end processing periods.

### SRE Best Practice: Evidence-Based Investigation
Monitor saturation for all limited resources: memory, CPU, disk I/O, network bandwidth, connection pools, thread pools, and queue depths. Establish leading indicators that show saturation building before it impacts customers. Use the USE method (Utilization, Saturation, Errors) to systematically identify resource constraints. Trend saturation metrics over time to identify slow-building problems.

### Banking Impact
In banking systems, saturation problems often appear during peak processing times, causing cascading failures across dependent systems. When core banking databases approach saturation, transaction processing slows, batch processes fail to complete in their windows, regulatory reporting is delayed, and customer-facing applications become unresponsive. Recovery often requires extensive reconciliation work to ensure financial consistency.

### Implementation Guidance
1. Identify all limited resources in your architecture and implement saturation metrics for each
2. Create dashboards that show saturation trends over multiple time frames
3. Establish alerting thresholds at 70-80% saturation to provide response time before customer impact
4. Implement circuit breakers and graceful degradation modes for when resources approach saturation
5. Conduct regular capacity planning reviews that incorporate saturation trends

## Panel 5: The Resource Detective

**Scene Description**: Infrastructure team using USE method to troubleshoot virtual server farm. Visual shows USE checklist being systematically applied to infrastructure components supporting core banking batch processing.

### Teaching Narrative
The USE Method provides a systematic approach to performance analysis and troubleshooting by examining three key aspects of every resource: Utilization (how busy it is), Saturation (how much queueing is occurring), and Errors (failure count). This methodology helps identify bottlenecks in complex systems by focusing on resource constraints rather than symptoms.

### Common Example of the Problem
A banking batch processing system that reconciles daily transactions is increasingly missing its completion window. The operations team focuses on application-level metrics but cannot identify the cause. They've added more CPU and memory to the servers, but the problem persists because they haven't systematically examined all resources using the USE method to find the actual constraint: disk I/O during peak write periods.

### SRE Best Practice: Evidence-Based Investigation
Apply the USE method to every resource in the system: for each resource, check utilization, saturation, and errors. Start with the most constrained resources. Use visualization tools to correlate utilization and saturation metrics across components. Compare resource constraints during normal operation versus during incidents to identify patterns.

### Banking Impact
In banking systems, unidentified resource constraints can cause critical processing delays that impact regulatory reporting, customer statement generation, and financial reconciliation. When batch processes miss their windows, it can delay market opening, prevent customers from accessing accounts, or create compliance issues with financial regulators requiring timely reporting.

### Implementation Guidance
1. Create resource inventory identifying all potentially constraining resources in each system
2. Implement standard USE dashboards for each resource type
3. Establish baseline utilization and saturation levels during normal operation
4. Conduct regular USE analysis during performance testing and after incidents
5. Develop runbooks that guide teams through systematic USE analysis during incidents

## Panel 6: Container Confusion

**Scene Description**: New SRE confused by pod metrics vs. node metrics in Kubernetes. Visual shows nested boxes illustrating the relationship between pods, nodes, and clusters in a payment microservices architecture.

### Teaching Narrative
Modern banking infrastructures often include container orchestration platforms like Kubernetes, which add additional layers of resource abstraction and management. Understanding the relationship between container metrics, pod metrics, and node metrics is essential for effective monitoring and troubleshooting in these environments.

### Common Example of the Problem
A bank's payment microservices architecture running on Kubernetes experiences intermittent performance issues. The new SRE team monitors pod CPU and memory metrics, which look normal, but fails to examine node-level resources. They miss the fact that noisy neighbors on the same nodes are causing resource contention, while namespace quotas are preventing proper scaling of critical payment pods during peak periods.

### SRE Best Practice: Evidence-Based Investigation
Implement multi-level resource monitoring that covers containers, pods, nodes, and clusters. Understand the relationship between different metric levels and how they affect each other. Establish baselines for normal operation at each level. Use resource quotas and limits appropriately to prevent contention. Monitor control plane metrics in addition to workload metrics.

### Banking Impact
In payment microservices, resource contention issues can cause transaction delays or failures that directly impact customers and merchants. Improper quota settings may prevent critical services from scaling during peak periods, leading to declined transactions. Control plane instability can affect multiple services simultaneously, creating widespread outages that trigger regulatory reporting requirements.

### Implementation Guidance
1. Create hierarchical dashboards showing relationships between container, pod, and node metrics
2. Implement appropriate resource quotas and limits based on service criticality
3. Monitor Kubernetes control plane health alongside workload metrics
4. Establish pod quality of service classes appropriate for different banking functions
5. Use node affinity and anti-affinity rules to prevent critical workloads from competing

## Panel 7: Through the Customer's Eyes

**Scene Description**: UX team collaborating with SREs to understand performance. Visual shows customer journey map with RED metrics (Rate, Error, Duration) overlaid at each step of the digital account opening process.

### Teaching Narrative
The RED Method focuses on service-level metrics that directly impact customers: Request Rate (traffic), Error Rate (failures), and Duration (latency). This approach aligns technical measurements with user experience, making it particularly valuable for customer-facing banking applications where the customer journey spans multiple services and interactions.

### Common Example of the Problem
A bank's digital account opening process shows acceptable technical metrics when viewed service by service, but customers are abandoning the process at high rates. The UX team blames technical performance, while engineering points to the design. Without an end-to-end view using customer-centric metrics, neither team can identify that the identity verification step creates a duration spike that causes most abandonments.

### SRE Best Practice: Evidence-Based Investigation
Implement consistent RED metrics for all user-facing services and customer journeys. Build dashboards that show customer impact first, with drill-down capability into technical details. Segment RED metrics by user type, transaction type, and channel to identify specific impact patterns. Use RED metrics to drive incident response priorities and communication.

### Banking Impact
For digital banking applications, the RED method creates clear visibility into customer experience across channels. When issues occur, teams can immediately quantify impact in business terms: number of affected customers, transaction success rates, and processing delays. This clarity allows for appropriate prioritization of incidents based on customer impact rather than technical severity.

### Implementation Guidance
1. Standardize RED metrics implementation across all customer-facing services
2. Create customer journey dashboards that show RED metrics at each interaction step
3. Establish RED-based alerting thresholds aligned with customer experience goals
4. Implement customer segmentation in RED metrics to identify high-value customer impact
5. Train support teams to use RED metrics for accurate customer communication during incidents