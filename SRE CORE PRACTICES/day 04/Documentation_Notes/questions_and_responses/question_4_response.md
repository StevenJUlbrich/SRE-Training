# Audience Analysis for Traces and Distributed Tracing Training

## 1. Knowledge Gaps for Production Support Professionals

### Technical Understanding Gaps:
- Limited understanding of request flow across distributed systems architecture
- Unfamiliarity with trace data structures (spans, context propagation, parent-child relationships)
- Minimal experience with sampling concepts and trade-offs
- Lack of knowledge about instrumentation approaches and standards like OpenTelemetry
- Limited exposure to correlation between different observability signals (logs, metrics, traces)

### Process Gaps:
- Experience primarily with point-solution troubleshooting rather than end-to-end transaction flows
- Focus on component status rather than service dependencies and interactions
- Reactive performance analysis vs. proactive bottleneck identification
- Minimal exposure to defining and measuring customer-centric SLIs using trace data
- Limited understanding of trace-based capacity planning and analysis

## 2. Existing Skills to Leverage

### Technical Skills:
- Strong understanding of application components in their supported systems
- Experience with log analysis and traditional monitoring tools
- Familiarity with alert response and incident management
- Knowledge of banking technical environments and integrations
- Understanding of critical banking transactions and their technical components

### Process Skills:
- Troubleshooting methodology and investigative approaches
- Experience with on-call rotations and incident response
- Understanding of business impact when systems fail
- Knowledge of banking regulatory and compliance requirements
- Experience communicating technical issues to business stakeholders

## 3. Necessary Mindset Shifts

### From Reactive to Proactive:
- Shift from "responding to alerts" to "proactively identifying patterns"
- Move from "component-level monitoring" to "service-level observability"
- Transition from "is it working?" to "how well is it working?"
- Change from "time to resolve" to "time to detect" as a primary metric
- Evolve from "fixing symptoms" to "addressing systematic issues"

### System Thinking Changes:
- From seeing individual components to understanding service relationships
- From point-in-time checks to continuous transaction flow visibility
- From siloed responsibility to end-to-end service ownership
- From threshold-based alerting to anomaly detection
- From fixed runbooks to evidence-based investigation

## 4. Terminology and Example Adjustments

### Terminology Approach:
- Introduce new distributed tracing terms alongside familiar monitoring concepts
- Use banking-specific analogs for trace concepts (e.g., "transaction journey" for trace, "processing step" for span)
- Define technical terms in context of production support activities they already understand
- Use consistent terminology across chapters to build progressive understanding
- Avoid academic discussions of observability theory in favor of practical applications

### Example Adjustments:
- Begin with simple examples of familiar banking transactions before introducing complex microservice scenarios
- Use real-world banking systems they regularly support as the foundation for examples
- Connect trace concepts directly to daily support activities they currently perform
- Show side-by-side comparisons of how issues appear in traditional monitoring vs. distributed tracing
- Create examples that highlight the limitations of their current tools and how tracing addresses those gaps

### Application to Curriculum:
- Add an early chapter on "Traces from a Production Support Perspective" to bridge current knowledge
- Incorporate "From Logs to Traces" sections showing the evolution of troubleshooting approaches
- Include "Day in the Life" scenarios comparing traditional support vs. trace-based approaches
- Develop practical exercises based on common banking support scenarios they face regularly
- Create a transition glossary mapping familiar monitoring terms to distributed tracing concepts

These adjustments will help make the training material directly relevant to production support professionals in banking, building on their existing knowledge while guiding them toward the SRE mindset and tracing capabilities they need to develop.