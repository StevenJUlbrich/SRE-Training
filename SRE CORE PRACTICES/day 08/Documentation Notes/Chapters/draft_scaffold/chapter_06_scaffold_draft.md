# Chapter 6: Cardinality Management

## Panel 1: The Dimension Explosion
### Scene Description

 A banking SRE team huddles around a massive dashboard covered in red alerts. Their manager bursts into the room waving an invoice. "Our observability costs just increased TEN TIMES overnight!" On the screens, metrics graphs are frozen, query times have skyrocketed, and the team looks bewildered as they scroll through thousands of new metric combinations that appeared after yesterday's deployment. One engineer points to a small code change where a developer added customer account numbers as labels to every transaction metric.

### Teaching Narrative
Cardinality is the silent killer of observability budgets and performance. In the metrics world, cardinality refers to the number of unique time series being tracked. A single metric like `http_requests_total` is just one time series. But add a dimension like `status_code` with 5 possible values, and you now have 5 time series. Add another dimension like `endpoint` with 10 values, and you now have 5 × 10 = 50 time series. Each dimension multiplies the number of time series exponentially.

In banking systems, the temptation to add high-cardinality dimensions is particularly strong. Customer IDs, account numbers, transaction IDs - these unique identifiers create millions or billions of unique time series when added as labels. What starts as a simple change – "Let's track performance by customer ID" – can explode overnight into millions of unique time series, overwhelming your observability platform and exploding costs.

The core challenge of cardinality management is balancing the value of dimensional data against its exponential cost. Every dimension you add multiplies your metric count, storage requirements, and ultimately, your observability bill. Unlike logs which scale linearly with volume, metrics with high cardinality dimensions scale multiplicatively, making them particularly dangerous from a cost perspective.


## Panel 2: The Unbounded Label Trap
### Scene Description

 Two SREs are investigating why their metrics platform keeps crashing. On a whiteboard, they've traced the problem to a fraud detection service that's adding transaction-specific fields as labels to metrics. At the same time, a developer is demonstrating a new feature that adds geolocation data down to precise coordinates as metric labels. The SRE looks horrified as she calculates the cardinality: "That's potentially 37 billion unique combinations for a single metric!" On a monitor nearby, their budget dashboard shows costs rapidly approaching the monthly limit while it's only the 3rd day of the month.

### Teaching Narrative
The most dangerous label is the unbounded one – a dimension with potentially unlimited unique values. While adding country codes (with roughly 200 possible values) creates manageable cardinality, adding fields like User IDs, Session IDs, or precise coordinates creates effectively infinite cardinality. In banking systems, transaction IDs alone can generate billions of unique values annually.

Unbounded labels create multiple critical problems. First, they overwhelm the indexed databases that power observability platforms, causing performance degradation or outright crashes. Second, they generate enormous storage costs as each unique combination must be indexed and stored separately. Third, they make visualization and alerting nearly impossible as dashboards attempt to render millions of time series. Finally, they make queries extremely slow and resource-intensive, hampering your ability to troubleshoot during outages.

The irony is that unbounded labels rarely provide useful aggregate insights. While it might seem valuable to track metrics by individual customer ID, the resulting data is often too granular for practical use in dashboards or alerts. The proper approach is to use logs or traces for instance-specific details while keeping metrics focused on aggregatable dimensions with bounded cardinality.


## Panel 3: The Cardinality Budget
### Scene Description

 A virtual war room where a financial services platform team is establishing governance rules. On a large screen, they're documenting a hierarchy of allowed dimensions for different types of metrics. A governance lead is presenting a dashboard showing each service's current cardinality usage as a percentage of their allocated "cardinality budget." Teams with efficient metric design have plenty of room for new instrumentation, while a poorly-designed fraud detection service is shown at 250% of its allocation, with an automated warning system preventing new deployments until cardinality is reduced.

### Teaching Narrative
Just as financial institutions implement strict budget controls, effective observability requires establishing cardinality budgets. A cardinality budget establishes the maximum number of unique time series each service or team can create. This forces teams to prioritize which dimensions truly deliver value and discourages the casual addition of high-cardinality labels.

Implementing cardinality budgets requires understanding the natural hierarchy of dimensions in your system. In banking applications, this hierarchy typically flows from coarse-grained to fine-grained: region → data center → service → endpoint → status. Each level adds meaningful segmentation while keeping cardinality manageable. The key is determining which dimensions provide actionable insights for troubleshooting and business understanding versus those that merely explode cardinality.

Effective governance requires not just establishing these budgets, but implementing automated enforcement through validation in CI/CD pipelines. By automatically detecting when new code would exceed cardinality limits, you prevent cost explosions before they reach production. This approach balances development velocity with cost control by embedding cardinality awareness into your engineering culture.


## Panel 4: The Aggregation Hierarchy
### Scene Description

 An architect is leading a design review for a new payment gateway system's metrics design. On a whiteboard, she's created a pyramid diagram showing metric aggregation levels. At the pyramid's wide base are customer transaction events flowing into logs. In the middle tier, these are aggregated into bounded-cardinality metrics with key dimensions like payment processor, country, and response code. At the narrow top are highly aggregated SLIs tracking overall system health. Next to this, a developer has sketched how they can automatically roll these metrics up into increasingly aggregated forms for longer-term storage.

### Teaching Narrative
The antidote to cardinality explosion is strategic aggregation. Rather than tracking everything at the finest granularity, effective metric design creates an aggregation hierarchy that captures insights at multiple levels of detail. This approach recognizes that the value of granular data diminishes over time, while the cost of storing it remains constant.

A well-designed aggregation hierarchy starts with collecting detailed event data in logs or traces. These events are then aggregated into metrics with carefully selected dimensions that balance analytical power against cardinality. For banking systems, this typically means aggregating individual transactions into metrics by service, endpoint, status, and perhaps customer segment – but not individual customer ID.

This aggregation hierarchy should extend to storage retention as well. Recent metrics may retain moderate dimensionality for detailed troubleshooting, while older data is progressively aggregated to reduce storage costs. For example, per-minute metrics with endpoint and status code dimensions might be stored for 7 days, then aggregated to hourly metrics with only service-level dimensions for 30 days, and finally to daily metrics with minimal dimensions for longer retention.


## Panel 5: Strategic Dimension Selection
### Scene Description

 A monitoring architect is training a team of developers for a trading platform. She displays a matrix on the screen with potential metric dimensions on one axis and evaluation criteria on the other. For each dimension (endpoint, customer tier, account type, region, exact trade value), she's scoring its troubleshooting value, business insight value, cardinality impact, and query performance impact. The team is working through which dimensions to keep based on these scores. On a second screen, sample Prometheus metric definitions show how to implement these decisions in code.

### Teaching Narrative
Not all dimensions are created equal, and effective cardinality management requires strategic selection of which dimensions to include in your metrics. This selection process should balance four key factors: troubleshooting utility, business insight value, cardinality impact, and query performance.

Dimensions with high troubleshooting value help rapidly identify the source of issues. In banking systems, these typically include status codes, service names, and endpoint paths. Business-valuable dimensions provide insights into customer impact and may include customer segments, product types, or payment channels – but rarely individual customer identifiers.

The cardinality impact assessment quantifies how many new time series each dimension would create. For example, adding HTTP status codes typically adds only 5-10 values, while adding individual transaction IDs could add millions. Query performance impact addresses how the dimension affects dashboard load times and alert evaluation speed.

This strategic approach leads to consistent decisions about which dimensions to include directly in metrics, which to capture in logs or traces, and which to avoid entirely. By documenting these decisions in metric naming conventions and instrumentation standards, you create consistency across your organization.


## Panel 6: Isolation Strategies for High-Cardinality Use Cases
### Scene Description

 A risk analytics team and SRE are collaborating on a solution for monitoring individual high-value transactions without causing cardinality explosion. On their shared screen, they're designing a specialized metrics subsystem isolated from the main monitoring platform. It has its own storage, retention policies, and budget. Another tab shows a custom sampling algorithm that will only instrument a statistically significant percentage of transactions, with logic to ensure all high-value transactions are included in the sample. A dashboard shows the dramatic cost difference between sampling all transactions and their strategic approach.

### Teaching Narrative
Some banking use cases legitimately require higher-cardinality metrics – fraud detection, risk analysis, and compliance monitoring may genuinely need transaction-level visibility. Rather than allowing these specialized needs to destroy your observability budget, implement isolation strategies that quarantine high-cardinality metrics.

The first isolation approach is architectural: create separate storage backends for standard metrics versus high-cardinality metrics. This prevents high-cardinality data from impacting the performance of your core observability platform. These specialized subsystems can implement different retention periods, query controls, and cost models appropriate to their use case.

The second approach is statistical: apply intelligent sampling algorithms that capture a representative subset of high-cardinality data rather than every instance. These algorithms can be weighted to ensure critical transactions (like high-value trades or suspicious activities) are always captured while sampling more routine transactions at lower rates.

The third approach is temporal: implement dynamic retention policies that keep high-cardinality data for only as long as its value justifies its cost. This might mean retaining detailed transaction-level metrics for 24 hours for immediate troubleshooting, then aggregating to remove high-cardinality dimensions for longer-term storage.


## Panel 7: Implementing Guardrails and Automated Protection
### Scene Description

 An SRE is demonstrating a new guardrail system during a company tech talk. On one screen, she shows a CI/CD pipeline failing a deployment because a new metric would create excessive cardinality. On another, a runtime cardinality limiter is automatically dropping excessive label values when a service unexpectedly generates too many unique combinations. A third screen shows an alert triggered by a sudden cardinality increase in the payment service, allowing the team to intervene before costs escalate. On a final screen, the monthly observability cost graph shows how these guardrails have flattened what was previously an exponential curve.

### Teaching Narrative
Even with careful design, cardinality explosions can occur unexpectedly – a bug might cause a service to instrument every user ID, or an unforeseen edge case might generate millions of unique label values. Effective cardinality management requires implementing automated guardrails that prevent these issues from impacting cost and performance.

The first layer of protection is preventative: instrumentation validation in CI/CD pipelines can analyze metric definitions to identify potential cardinality issues before code reaches production. This catches obvious issues like adding unbounded user IDs or transaction IDs as labels.

The second layer is runtime protection: cardinality limiters in your metrics pipeline can automatically cap the number of unique label combinations per metric, dropping excessive cardinality rather than allowing it to overwhelm your observability platform. While this results in some data loss, it preserves system stability and cost predictability.

The third layer is detective: automated anomaly detection should monitor cardinality growth rates and alert when metrics suddenly generate more unique time series than expected. This allows teams to investigate and address the root cause before costs spiral out of control.

These guardrails should be complemented by clear visibility into cardinality usage through dashboards that show each service's contribution to the total metric count. By making cardinality visible, you create accountability and encourage teams to optimize their instrumentation.