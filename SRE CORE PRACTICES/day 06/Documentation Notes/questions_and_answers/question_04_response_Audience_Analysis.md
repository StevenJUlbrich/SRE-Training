# Audience Analysis: Production Support to SRE Transition

## 1. Knowledge Gaps in SLI, SLO, and Error Budget Concepts

Production support professionals transitioning to SRE roles likely have these specific knowledge gaps:

- **Customer-Centric Metrics**: Limited experience with metrics that directly measure user experience rather than system health
- **Statistical Thinking**: Gaps in understanding percentiles, distributions, and aggregation methods critical for SLOs
- **Quantitative Reliability**: Unfamiliarity with expressing reliability as mathematical targets rather than binary up/down status
- **Trade-off Analysis**: Limited framework for making data-driven decisions about reliability vs. velocity
- **Product Lifecycle View**: Gaps in understanding how reliability fits into the broader product development lifecycle
- **Business Translation**: Difficulty connecting technical metrics to business outcomes and communicating them to stakeholders
- **Proactive Measurement**: Limited experience with designing measurement systems before problems occur
- **SLO Engineering**: Lack of experience in designing appropriate objectives that balance user expectations and technical realities
- **Error Budget Mechanics**: Unfamiliarity with calculating, tracking, and operationalizing error budgets

## 2. Existing Skills to Leverage

Production support professionals bring valuable skills that can be leveraged when learning SRE concepts:

- **System Knowledge**: Deep understanding of banking systems and their failure modes
- **Alert Response**: Experience responding to and resolving system issues
- **Troubleshooting**: Strong diagnostic skills for complex technical problems
- **User Impact Assessment**: Experience assessing incident impact on users and business
- **Stakeholder Communication**: Experience communicating technical issues to various stakeholders
- **Technical Documentation**: Familiarity with documenting technical processes and incidents
- **Monitoring Systems**: Hands-on experience with monitoring tools and dashboards
- **Banking Domain Knowledge**: Understanding of financial transactions, regulations, and processing requirements
- **Cross-team Collaboration**: Experience working across organizational boundaries during incidents

## 3. Necessary Mindset Shifts

The transition from production support to SRE requires several critical mindset shifts:

- **From Reactive to Proactive**: Shifting from responding to failures to preventing them through design
- **From Binary to Probabilistic**: Moving from "working/not working" to statistical reliability targets
- **From Component to Service View**: Focusing on end-to-end service health rather than individual components
- **From Uptime to User Experience**: Prioritizing what users experience over internal system metrics
- **From Blame to Learning**: Embracing blameless postmortems and continuous improvement
- **From Manual to Automated**: Valuing automation over heroic manual interventions
- **From Perfect to Good Enough**: Accepting appropriate reliability targets rather than pursuing 100% reliability
- **From Separate Teams to Shared Responsibility**: Seeing reliability as a shared concern across development and operations
- **From Incident Response to Engineering**: Using data from incidents to drive system improvements

## 4. Terminology and Example Adjustments

To effectively communicate with production support professionals, we should adjust:

### Terminology Adaptations
- **Connect New to Familiar**: Map SRE terms to existing monitoring concepts (e.g., "SLIs are like your critical monitor checks, but focused on user experience")
- **Reduce Abstraction**: Use concrete language rather than abstract reliability theory
- **Progressive Introduction**: Introduce specialized terminology gradually, building from familiar concepts
- **Consistent Definitions**: Provide clear, consistent definitions throughout with banking-specific examples
- **Visual Glossaries**: Include visual representations of key concepts to aid understanding
- **Practical Before Theoretical**: Present practical applications before deep theoretical explanations

### Example Adjustments
- **Start with Known Systems**: Use examples based on systems they already monitor (payment processors, core banking platforms)
- **Progressive Complexity**: Begin with simple examples and progressively introduce more complex scenarios
- **Real Banking Scenarios**: Use authentic banking situations like transaction processing, fund transfers, and trading execution
- **Contrast Old vs. New**: Show how the same situation would be handled in traditional monitoring vs. SRE approaches
- **Regulatory Connection**: Include examples that connect reliability to regulatory requirements familiar to banking professionals
- **Technical Diversity**: Cover both mainframe/legacy and modern microservice architectures common in banking
- **Incident Reframing**: Reframe familiar past incidents through the lens of SLIs, SLOs, and error budgets
- **Tool Translation**: Show how to implement concepts using both familiar tools (like ITRS Geneos) and new SRE platforms

These adjustments will help create training materials that effectively bridge the knowledge gap for production support professionals transitioning to SRE roles in banking environments.