# Audience Analysis for Integration & Triage Training

## 1. Knowledge Gaps for Production Support Professionals

Production support professionals transitioning to SRE roles likely have the following knowledge gaps regarding Integration & Triage:

- **Systems Thinking**: Limited experience viewing infrastructure as interconnected systems rather than isolated components, making it challenging to understand how signals correlate across different services in a banking ecosystem.

- **Signal Theory**: Lack of formal understanding about the differences between metrics, logs, traces, and events as distinct signal types with different analytical approaches.

- **Statistical Analysis**: Limited exposure to statistical methods for anomaly detection, trend analysis, and pattern recognition that form the foundation of advanced triage.

- **Hypothesis Testing**: Unfamiliarity with structured approaches to testing theories about system behavior through controlled experiments and evidence gathering.

- **Automation Principles**: Gaps in understanding how to design and implement automated triage systems that can scale beyond manual processes.

- **Service Level Objectives**: Limited experience defining and working with SLOs as a framework for prioritization during triage activities.

- **Distributed Systems Failure Modes**: Insufficient knowledge of how distributed systems (increasingly common in banking) fail in ways different from monolithic applications.

## 2. Existing Skills to Leverage

Production support professionals bring valuable skills that can be leveraged in learning Integration & Triage:

- **Alert Response Experience**: Familiarity with handling and responding to system alerts, even if the approach has been reactive rather than systematic.

- **Tool Proficiency**: Working knowledge of specific monitoring tools used in banking environments, such as ITRS Geneos, Splunk, or Dynatrace.

- **Banking Domain Knowledge**: Deep understanding of banking processes, transaction flows, and business impacts that provides crucial context for effective triage.

- **Communication Protocols**: Experience with escalation pathways and stakeholder communication during technical incidents.

- **Troubleshooting Fundamentals**: Basic troubleshooting skills such as log examination, error message interpretation, and configuration checking.

- **Customer Impact Assessment**: Ability to translate technical issues into business and customer impact terms, essential for prioritization.

- **System Access Knowledge**: Familiarity with access methods and credentials for various banking systems, which expedites investigation during triage.

## 3. Necessary Mindset Shifts

Key mindset shifts required for the transition from reactive production support to proactive SRE Include:

- **From Fixing to Preventing**: Moving beyond simply resolving current issues to identifying patterns that could prevent future occurrences.

- **From Following Playbooks to Designing Investigations**: Transitioning from executing predefined steps to designing custom investigation approaches based on evidence.

- **From Individual Components to Service Chains**: Shifting focus from isolated system components to entire service delivery chains and their interdependencies.

- **From Time-to-Resolution to Quality-of-Resolution**: Balancing the urgency of fixes with the thoroughness of root cause identification to prevent recurrence.

- **From Metrics Observation to Signal Interpretation**: Moving beyond watching dashboards to actively interpreting what signals mean about system health.

- **From Reactive to Anticipatory**: Developing the ability to recognize early warning signals before they become customer-impacting incidents.

- **From Technology Focus to Business Service Focus**: Reframing technical issues in terms of impact on core banking services and customer experience.

## 4. Terminology and Example Adjustments

To effectively reach production support professionals in banking, the training should adjust terminology and examples as follows:

- **Connect to Familiar Tools**: Frame new concepts in relation to tools they already use, such as "While ITRS Geneos shows you threshold breaches, here's how we integrate that with log data to provide deeper context."

- **Bridge Terminology Gaps**: Introduce new terms by connecting them to familiar concepts, such as "Think of traces as transaction logs that follow a request across multiple systems."

- **Use Banking-Specific Scenarios**: Create examples based on common banking incidents, such as payment processing delays, online banking access issues, or trading platform performance problems.

- **Emphasize Regulatory Relevance**: Connect triage practices to regulatory requirements they already understand, such as incident reporting obligations under PSD2 or data protection requirements under GDPR.

- **Showcase Career Progression**: Include examples from the career journeys of former production support professionals who successfully transitioned to SRE roles in banking.

- **Reference Familiar Systems**: Use examples involving core banking platforms they commonly support, such as "When triaging an issue with the payment gateway's connection to the core banking system..."

- **Gradually Introduce Complexity**: Start with simple on-premise infrastructure examples before progressing to more complex hybrid cloud architectures that may be less familiar.

By addressing these specific audience needs, the training materials can more effectively bridge the knowledge gap for production support professionals while building on their existing strengths and gradually shifting their mindset toward SRE practices.