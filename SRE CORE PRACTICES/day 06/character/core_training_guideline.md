# SRE Core Curriculum: Reliability Metrics & Error Budgets
*Featuring Ava Kimani from Nairobi*

---

## Beginner Tier (3-4 Days)

### Day 1: Foundations of Reliability Engineering

#### Module 1: Introduction to SRE
- What is Site Reliability Engineering?
- SRE vs. Traditional Production Support
- Key SRE Principles and Practices

**Ava's Insight:** *"Welcome to your journey from production support to SRE! In Nairobi, we say 'The first step of the journey is the most important.' Today, we're taking that first step together. Remember, SRE isn't about eliminating all failures—it's about managing them intelligently."*

#### Module 2: Understanding Service Level Concepts
- SLAs: Service Level Agreements
  - Definition and purpose
  - Typical SLAs in banking environments
  - SLAs vs. customer expectations
- SLOs: Service Level Objectives
  - Definition and purpose
  - Relationship to user experience
  - Basic SLO formulation
- SLIs: Service Level Indicators
  - Definition and measurement methods
  - Common SLIs in banking applications
  - Data sources for SLIs

**Practical Exercise:** "Banking App Response Time Analysis"
- Analyze sample response time data from a banking application
- Identify potential SLIs from the data
- Draft simple SLOs based on the identified SLIs

**Ava's Commentary:** *"Notice how I didn't ask you to achieve 100% reliability? That's because perfect reliability is a vanity metric! *wrist slap* In banking, we need reliability—but we need to measure the right things. A 99.99% available API that can't process transactions correctly is worthless to customers trying to pay their bills."*

### Day 2: Error Budgets & Basic Monitoring

#### Module 3: Introduction to Error Budgets
- What are error budgets?
- Calculating basic error budgets
- Error budget consumption and tracking
- Using error budgets for decision-making

**Ava's Insight:** *"Your error budget isn't just permission to fail—it's your innovation currency. In banking, we're conservative by nature, but that doesn't mean we can't innovate. Error budgets give us a measured, controlled way to take risks while protecting customer experience."*

#### Module 4: Basic Monitoring Implementation
- Introduction to Prometheus and Grafana
- Setting up basic metrics collection
- Creating simple SLI dashboards
- Introduction to Splunk for log-based SLIs

**Practical Exercise:** "Setting Up Your First SLI Dashboard"
- Install Prometheus and Grafana (guided lab environment)
- Configure basic metrics collection for a sample banking application
- Build a dashboard showing API response times and success rates
- Set up alerting based on simple thresholds

**Ava's Commentary:** *"A monitoring system without clear SLIs is like a gauge that doesn't tell you what it's measuring. Is it fuel? Temperature? In banking systems, we need to know exactly what we're measuring and why it matters to customers. Your dashboard should tell the story of your customers' experience."*

### Day 3: Basic SLO Implementation

#### Module 5: Implementing Your First SLO
- Choosing appropriate SLIs for banking services
- Setting realistic SLO targets
- Documenting and communicating SLOs
- Basic error budget calculation methods

**Practical Exercise:** "Banking Service SLO Development"
- Using provided banking transaction data:
  - Analyze historical performance
  - Identify appropriate SLIs for different services (transfers, payments, account lookups)
  - Develop initial SLOs with targets
  - Calculate error budgets for each SLO

**Ava's Commentary:** *"Always remember that in banking, different operations have different reliability requirements. A customer checking their balance might tolerate occasional slowness, but a failed payment transfer? That's a problem that will send them straight to your competitors!"*

#### Module 6: From Reactive to Proactive Support
- Shifting mindset from incident response to prevention
- Using SLOs to guide improvements
- Basic alerting based on SLOs
- Communicating reliability concepts to team members

**Practical Exercise:** "Error Budget Alert Planning"
- Design an alerting strategy based on error budget consumption
- Role-play exercise: Explaining SLOs to stakeholders
- Development of a basic error budget policy

**Ava's Insight:** *"In production support, we're heroes running from fire to fire. In SRE, we're strategic firefighters who also build fire prevention systems. Your alerts should give you time to act before customers are impacted—not just tell you that they already are!"*

---

## Intermediate Tier (3-4 Days)

### Day 1: Advanced SLI Development

#### Module 1: Developing Meaningful SLIs
- Advanced SLI methodologies
- The four golden signals in banking context
- Custom SLIs for banking-specific operations
- Multi-component service SLIs

**Ava's Insight:** *"The best SLIs are like good bank security—invisible to customers when working properly, but their absence would be immediately noticed! Let's go beyond basic response time and availability to measure what really matters to banking customers."*

#### Module 2: SLI Implementation with Prometheus
- PromQL for advanced metrics
- Custom exporters for banking applications
- Capturing business-relevant metrics
- SLI histograms and quantiles

**Practical Exercise:** "Advanced Banking SLI Implementation"
- Implement RED method metrics (Rate, Errors, Duration) for banking APIs
- Create custom metrics for financial transaction success rates
- Develop histograms for transaction processing time
- Configure Prometheus alerts based on SLO burn rates

**Ava's Commentary:** *"*wrist slap* I see you measuring average response time again! In banking, averages hide the truth. Your customer doesn't care that most transactions are fast if theirs is the slow one. Always use percentiles for latency SLIs!"*

### Day 2: Error Budget Management

#### Module 1: Advanced Error Budget Practices
- Error budget policies
- Error budget-based decision making
- Managing competing priorities with error budgets
- Communicating error budget status to stakeholders

**Practical Exercise:** "Error Budget Policy Development"
- Draft an error budget policy for a banking platform
- Design a decision-making framework based on error budget status
- Create a communication template for different error budget states

**Ava's Commentary:** *"An error budget without a policy is like a bank account without rules—quickly drained with nothing to show for it! Your policy turns the abstract concept into a practical tool for making decisions."*

#### Module 2: SLO-Based Alerting Strategies
- Alert fatigue reduction
- Multi-window, multi-burn-rate alerts
- Configuring meaningful alerts in Prometheus/Grafana
- Integration with on-call systems

**Practical Exercise:** "Implementing SLO-Based Alerts"
- Configure multi-burn-rate alerts in Prometheus
- Set up Grafana dashboards for error budget visualization
- Integrate alerts with notification systems
- Test and refine alert sensitivity

**Ava's Insight:** *"In Nairobi, we say 'The lion that roars too often is ignored.' The same is true for your alerts! SLO-based alerting means you only get woken up when there's a real threat to customer experience—not for every minor fluctuation."*

### Day 3: Reliability in AWS and Kubernetes Environments

#### Module 1: AWS-Specific SLIs and SLOs
- AWS CloudWatch metrics for banking applications
- Custom SLIs across AWS services
- Reliability considerations for banking workloads in AWS
- Error budget implementation in cloud environments

**Practical Exercise:** "AWS Banking Platform SLIs"
- Configure CloudWatch metrics for banking services
- Export CloudWatch metrics to Prometheus
- Develop SLOs for AWS-hosted banking applications
- Create error budget tracking for cloud resources

**Ava's Commentary:** *"The cloud doesn't excuse you from measuring reliability! In fact, with AWS, you have more metrics available than ever before—but that doesn't mean they're all useful. Focus on the metrics that reflect your customers' actual experience."*

#### Module 2: Kubernetes Reliability Patterns
- Kubernetes-based SLIs
- Reliability patterns for containerized banking applications
- Prometheus Operator and custom resources
- Service mesh observability

**Practical Exercise:** "Kubernetes Banking Service Reliability"
- Configure Prometheus Operator for K8s monitoring
- Implement RED method for microservices
- Set up service mesh observability
- Create SLOs for containerized banking services

**Ava's Insight:** *"Kubernetes doesn't make your services more reliable automatically—it just gives you more ways to implement reliability. Without proper SLOs and measurement, you're just moving your reliability problems to a new platform!"*

### Day 4: Applied SRE for Banking Services

#### Module 1: SLOs for Critical Banking Functions
- Transaction processing SLOs
- Account management service reliability
- Payment system SLIs and SLOs
- Regulatory considerations in banking SLOs

**Practical Exercise:** "Banking Service SLO Workshop"
- Analyze real-world banking service data
- Identify critical customer journeys
- Develop comprehensive SLOs for end-to-end banking experiences
- Incorporate regulatory requirements into SLO framework

**Ava's Commentary:** *"In banking, reliability isn't just good business—it's often a regulatory requirement! But regulations only set the floor, not the ceiling. Your SLOs should exceed regulatory minimums to deliver truly great customer experiences."*

#### Module 2: SLO Visualization and Reporting
- Advanced Grafana dashboards
- Executive-level SLO reporting
- Customer-facing reliability metrics
- Telling the reliability story with data

**Practical Exercise:** "Building an Executive SLO Dashboard"
- Create multi-level Grafana dashboards
- Develop executive summary views of reliability
- Configure automated SLO reports
- Design customer-facing reliability metrics

**Ava's Insight:** *"Your dashboards should answer the key question for each audience. Executives want to know: 'Are we meeting our promises to customers?' Engineers need to know: 'Where should we focus our reliability efforts?' Build dashboards that answer the right questions for each group."*

---

## Advanced Tier (3-4 Days)

### Day 1: SRE Excellence in Banking

#### Module 1: Advanced Statistical Approaches to SLOs
- Statistical validity in SLO measurement
- Long-tail latency analysis
- Seasonality in banking workloads
- Adaptive SLOs based on user behavior

**Ava's Insight:** *"Banking traffic isn't random—it follows patterns. Paydays, holidays, fiscal year-ends... true reliability means understanding these patterns and adapting your measurement accordingly."*

#### Module 2: Multi-Team SLO Management
- SLO standardization across teams
- Building an SLO platform
- Cross-service dependencies and SLO implications
- SLO governance in large organizations

**Practical Exercise:** "Building an SLO Platform"
- Design an SLO specification format
- Implement a central SLO registry
- Create cross-team SLO dashboards
- Develop SLO review processes

**Ava's Commentary:** *"As your SRE practice grows, consistency becomes crucial. An SLO platform isn't just a technical tool—it's how you scale reliability culture across your organization. In large banks, this is how you maintain consistency across hundreds of services."*

### Day 2: Advanced Error Budget Frameworks

#### Module 1: Sophisticated Error Budget Policies
- Error budget-based feature freezes
- Automated policy enforcement
- Investment models based on reliability data
- Risk management through error budgets

**Practical Exercise:** "Error Budget Economics"
- Create investment models based on reliability data
- Develop automated error budget enforcement systems
- Design incentive structures for teams
- Create error budget negotiation frameworks

**Ava's Insight:** *"Error budgets are the currency of reliability. Like financial currency, they need robust policies, governance, and management. A sophisticated error budget framework turns reliability from a technology concern into a business tool."*

#### Module 2: SLO-Driven Development
- Integrating SLOs into the development lifecycle
- Pre-production SLO validation
- Canary analysis with SLOs
- Feature flags tied to error budgets

**Practical Exercise:** "SLO-Driven CI/CD"
- Implement SLO checks in CI/CD pipelines
- Configure canary deployments with SLO gates
- Design feature flag systems tied to error budgets
- Develop reliability test suites

**Ava's Commentary:** *"Reliability isn't something you add after development—it's something you build in from the start. SLO-driven development puts reliability guardrails around your innovation, allowing you to move fast without breaking customer trust."*

### Day 3: Reliability Forecasting and Modeling

#### Module 1: Predictive Reliability Engineering
- Forecasting error budget consumption
- Modeling reliability improvements
- Capacity planning based on SLO projections
- Chaos engineering within error budget constraints

**Practical Exercise:** "Reliability Forecasting Models"
- Build error budget forecasting models
- Develop reliability improvement ROI calculations
- Design chaos engineering experiments
- Create capacity planning models based on SLOs

**Ava's Insight:** *"The most advanced SREs don't just react to reliability problems—they predict and prevent them. Like good financial forecasting in banking, reliability forecasting helps you invest resources where they'll have the biggest impact."*

#### Module 2: SLOs for Next-Generation Banking
- Reliability for AI/ML banking components
- Mobile banking experience SLOs
- Blockchain and distributed financial service reliability
- Cross-channel banking experience measurement

**Practical Exercise:** "Next-Gen Banking SLOs"
- Develop SLOs for AI-powered banking features
- Create mobile experience SLIs and SLOs
- Design reliability frameworks for blockchain-based services
- Implement cross-channel customer journey SLOs

**Ava's Commentary:** *"Banking is evolving rapidly, and our reliability measurement must evolve with it. The principles remain the same—measure what matters to customers—but the implementation changes with new technologies and customer expectations."*

### Day 4: Building a World-Class SRE Practice

#### Module 1: SRE Cultural Transformation
- Moving from production support to strategic reliability
- Building reliability advocacy skills
- Mentoring and growing SRE talent
- Creating a learning organization

**Practical Exercise:** "SRE Transformation Roadmap"
- Assess current reliability culture
- Develop SRE transformation strategy
- Create reliability advocacy materials
- Design SRE career development frameworks

**Ava's Insight:** *"The hardest part of SRE isn't the technology—it's the cultural change. Moving from heroes who fix outages to engineers who prevent them requires a fundamental shift in how we think about our work and value."*

#### Module 2: The Future of Banking Reliability
- Regulatory trends affecting banking SRE
- Emerging reliability challenges
- Building antifragile banking systems
- Continuous reliability improvement frameworks

**Final Capstone Project:** "Banking SRE Strategy"
- Synthesize a comprehensive SRE strategy for a banking organization
- Develop implementation roadmap with clear milestones
- Create executive presentation on reliability as competitive advantage
- Design continuous improvement framework

**Ava's Final Commentary:** *"Reliability isn't a destination—it's a journey of continuous improvement. The best banking SREs are never satisfied, always measuring, always improving. Your customers don't just want reliability today—they expect it to get better tomorrow. That's the promise and the challenge of banking SRE."*

---

## Assessment and Certification

Each tier concludes with:
1. A knowledge assessment covering key concepts
2. A practical implementation project
3. A peer review exercise

Certification is awarded for each completed tier, with portfolio projects that demonstrate concrete skills in:
- SLI/SLO development
- Error budget implementation
- Reliability visualization and communication

---

**Ava's Parting Wisdom:** *"Reliability you can measure is the only reliability that matters. As you return to your teams, remember that SRE isn't about perfect systems—it's about making explicit promises and keeping them consistently. Your journey from production support to SRE is just beginning. Measure well, learn constantly, and never stop improving the reliability that your banking customers depend on every day."*