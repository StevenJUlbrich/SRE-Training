# Audience Analysis for Cost-Aware Observability Training

## 1. Knowledge Gaps for Production Support Professionals

Production support professionals transitioning to SRE roles likely have several significant knowledge gaps related to cost-aware observability:

They often lack understanding of the economic models behind modern observability platforms, which typically charge based on data ingestion volume rather than the fixed licensing costs of traditional monitoring tools they're familiar with. This creates a fundamental gap in how they perceive the relationship between telemetry collection and cost implications.

Many production support professionals have limited exposure to dimensional metrics and high-cardinality data models that drive significant cost factors in modern observability. They're typically accustomed to pre-defined dashboards with fixed metrics rather than dynamic, high-dimensional data exploration that can rapidly increase costs.

There's often a significant gap in understanding the concept of observability sampling strategies. Traditional monitoring usually captures all data points, while cost-effective observability requires strategic decisions about what to collect at full fidelity versus what to sample or aggregate, particularly in high-volume banking transaction systems.

Production support teams typically have limited experience with observability governance frameworks and the organizational dynamics of cost allocation across teams. They're used to centralized monitoring platforms without transparent cost attribution to specific services or teams, creating a gap in understanding cost ownership principles.

They frequently lack experience with the statistical methods used to validate that reduced data collection still provides sufficient insight. Without this mathematical foundation, they may struggle to confidently implement cost-reduction strategies while maintaining system visibility.

## 2. Existing Skills to Leverage

Production support professionals bring valuable skills that can serve as foundations for learning cost-aware observability:

They typically have strong expertise in interpreting alerts and dashboard data to identify operational issues, which provides a solid foundation for understanding what signals are truly valuable. This intuition about "what matters" can be redirected toward cost-efficient signal selection.

Many have developed deep system knowledge of banking applications and their failure modes during on-call rotations. This domain expertise is invaluable for making intelligent decisions about which transactions require comprehensive observability versus which can be monitored more economically.

Production support professionals often have experience managing monitoring tool configurations across large banking environments. This experience with deployment, update management, and configuration governance creates transferable skills for observability implementation.

They typically have strong troubleshooting workflows that can be applied to observability data analysis. Their methodical approach to investigating issues provides a framework for evaluating which observability signals deliver the most troubleshooting value relative to their cost.

Many have experience communicating technical issues to non-technical stakeholders during incidents, which provides a foundation for developing cost-justification narratives and ROI explanations for observability investments.

## 3. Necessary Mindset Shifts

The transition from reactive to proactive operations requires several fundamental mindset shifts:

From "collect everything just in case" to "strategically instrument what matters." Production support teams are accustomed to enabling all available monitoring as a safety net, but SREs must develop a more disciplined approach that balances comprehensive visibility with cost efficiency.

From "incident response" to "system design for observability." Rather than viewing telemetry as something added to troubleshoot problems, they need to shift toward designing systems with built-in, cost-effective observability from the ground up.

From treating monitoring as "overhead cost" to viewing observability as "business investment." This requires developing comfort with ROI calculations and business value articulation rather than seeing observability purely as a technical necessity.

From "standard monitoring for all services" to "tiered observability based on service criticality." This means moving away from uniform monitoring approaches toward differentiated strategies that invest more observability resources in business-critical services while applying more cost-conscious approaches to less critical components.

From "reactive tool selection" to "strategic observability platform evaluation." Instead of simply using whatever monitoring tools are provided, they must develop framework-based approaches to selecting and implementing observability solutions with explicit consideration of long-term cost implications.

## 4. Terminology and Example Adjustments

To effectively reach this audience, several adjustments to terminology and examples are needed:

Bridge familiar monitoring concepts to new observability terminology by explicitly connecting them in examples. For instance, relate traditional "thresholds" to modern "service level indicators," showing how the latter provides more cost-effective visibility when implemented correctly.

Use banking-specific metrics examples that production support teams would recognize, such as payment transaction success rates or trading platform response times, then show how these can be instrumented more cost-effectively with modern approaches compared to traditional monitoring methods.

Develop case studies that start with familiar scenarios from production support (like a payment gateway incident) and demonstrate how both better resolution and lower costs could be achieved with properly implemented cost-aware observability.

Gradually introduce the statistical terminology around sampling and cardinality by relating it to concrete banking examples—for example, explaining how sampling customer journey data at different rates based on transaction value can reduce costs while maintaining visibility into high-value activities.

Explicitly translate cloud provider and observability platform billing concepts into terms familiar to enterprise IT by relating them to the budget structures production support teams already understand, such as capital versus operational expenses or project-based versus operational funding.

Create parallel examples showing how the same banking system incident would be addressed using traditional monitoring approaches versus cost-aware observability practices, highlighting both the technical and financial advantages of the latter.

These adjustments will help create training materials that meet production support professionals where they are while guiding them toward the more sophisticated and cost-conscious observability practices required in SRE roles within banking environments.