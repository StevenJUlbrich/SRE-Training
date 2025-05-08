# Banking Context for SLI/SLO/Error Budget Training Materials

## 1. Banking-Specific Examples for Each Chapter

### Chapter 1: From Monitoring to Observability
- **Example**: A major retail bank's mobile app shows all server metrics as normal (CPU, memory, network), but customers complain about failed transfers
- **Example**: An investment platform's core trading system passes all health checks while subtle order execution delays impact high-frequency traders

### Chapter 2: Understanding Service-Level Indicators
- **Example**: Contrasting database uptime metrics with successful payment transaction rates for a payment gateway
- **Example**: Using funds settlement completion times versus network availability for an interbank transfer system

### Chapter 3: The Anatomy of Quality Metrics
- **Example**: Building effective SLIs for ATM networks that capture both machine availability and successful cash dispensing operations
- **Example**: Designing quality metrics for credit card authorization systems that balance fraud prevention with transaction approval rates

### Chapter 4: Implementing SLIs
- **Example**: Implementing SLIs across a hybrid banking architecture with mainframe core banking and cloud-based digital channels
- **Example**: Capturing SLI data from a payment processing system spanning multiple technology stacks and third-party providers

### Chapter 5: Service-Level Objectives
- **Example**: Setting differentiated SLOs for a wealth management platform based on customer tiers and transaction values
- **Example**: Establishing appropriate SLOs for month-end financial close processes versus real-time transaction systems

### Chapter 6: SLO Engineering
- **Example**: Engineering SLOs for foreign exchange trading platforms with different reliability needs during market hours versus off-hours
- **Example**: Designing tiered SLOs for mortgage processing systems based on application stages and regulatory deadlines

### Chapter 7: Error Budgets
- **Example**: Calculating and tracking error budgets for a bank's online bill payment system during a major platform migration
- **Example**: Using error budgets to manage the reliability cost of feature deployments in a mobile banking application

### Chapter 8: Error Budget Policies
- **Example**: Creating error budget policies for a Treasury Management System that align with financial reporting requirements
- **Example**: Developing escalation frameworks based on error budget consumption rates for a mission-critical trading settlement system

### Chapter 9: SLO-Based Alerting
- **Example**: Transitioning from threshold-based to SLO-based alerting for a credit card fraud detection system
- **Example**: Designing burn rate alerts for an international wire transfer service with regulatory time guarantees

### Chapter 10: Multi-Dimensional SLOs
- **Example**: Creating multi-dimensional SLOs for a securities trading platform that consider execution speed, price accuracy, and order completion
- **Example**: Designing complex SLO structures for real-time fraud detection that balance false positives with detection efficacy

### Chapter 11: Quantifying Business Impact
- **Example**: Translating payment gateway reliability metrics into revenue impact and customer retention metrics
- **Example**: Connecting trading platform availability to specific profit and loss implications for various market conditions

### Chapter 12: SLI/SLO Maturity Models
- **Example**: Tracing the reliability evolution of a digital banking platform from basic uptime metrics to sophisticated customer journey SLOs
- **Example**: Mapping the maturity journey of a global bank's payment infrastructure reliability program

### Chapter 13: Reliability in Complex Financial Systems
- **Example**: Managing SLOs across a complex mortgage origination process spanning multiple systems and third-party providers
- **Example**: Implementing reliability engineering in an investment management platform with numerous downstream dependencies

### Chapter 14: The Operational Cadence
- **Example**: Structuring weekly SLO reviews for a retail banking platform during a major digital transformation
- **Example**: Integrating error budget discussions into quarterly business reviews for trading systems

### Chapter 15: Future of Financial Services Reliability
- **Example**: Exploring reliability implications of central bank digital currencies and instant payment networks
- **Example**: Addressing emerging challenges in reliability for AI-powered credit decisioning systems

## 2. Relevant Banking Regulations and Compliance Factors

- **Payment Card Industry Data Security Standard (PCI DSS)**: Reliability requirements for credit card processing systems
- **Basel Committee on Banking Supervision (BCBS 239)**: Risk data aggregation and reporting principles
- **Financial Conduct Authority (FCA) Operational Resilience Framework**: Requirements for identifying important business services and setting impact tolerances
- **Markets in Financial Instruments Directive II (MiFID II)**: Transaction reporting and best execution requirements
- **Payment Services Directive 2 (PSD2)**: Requirements for payment service availability and performance
- **General Data Protection Regulation (GDPR)**: Data access reliability requirements
- **Dodd-Frank Act**: Requirements for financial system stability and risk reporting
- **Sarbanes-Oxley Act (SOX)**: Controls for financial reporting systems
- **Federal Financial Institutions Examination Council (FFIEC)**: IT examination handbook guidelines on system reliability
- **Bank Secrecy Act (BSA)/Anti-Money Laundering (AML)**: Reliability of monitoring and reporting systems

## 3. Key Banking Systems for SLI/SLO/Error Budget Application

- **Payment Processing Systems**: Card authorization, ACH, wire transfers, real-time payments
- **Core Banking Platforms**: Account management, ledger systems, interest calculation
- **Trading and Market Data Systems**: Order management, execution, market data distribution
- **Digital Banking Channels**: Mobile apps, online banking portals, API gateways
- **ATM Networks**: Cash dispensing, deposit processing, network management
- **Fraud Detection Systems**: Real-time transaction scoring, neural network models
- **Regulatory Reporting Systems**: Financial reporting, compliance monitoring
- **Settlement Systems**: Clearing, reconciliation, nostro/vostro management
- **Customer Relationship Management (CRM) Systems**: Customer data management, interaction tracking
- **Wealth Management Platforms**: Portfolio management, investment advice, reporting
- **Loan Origination Systems**: Application processing, underwriting, approval workflows
- **Treasury Management Systems**: Liquidity management, cash forecasting

## 4. Connecting SLIs/SLOs/Error Budgets to Banking Business Metrics

### Direct Financial Impact Connections
- **Revenue Loss Quantification**: Translating transaction success rates to direct revenue impact (e.g., fees, foreign exchange margins)
- **Customer Attrition Metrics**: Connecting reliability incidents to customer churn rates and lifetime value reduction
- **Operational Cost Metrics**: Linking system reliability to incident management costs and manual intervention expenses
- **Regulatory Fine Exposure**: Relating reliability to compliance breaches and potential penalties
- **Opportunity Cost Calculation**: Measuring trading platform reliability impact on missed market opportunities

### Operational Efficiency Connections
- **Straight-Through Processing (STP) Rates**: Connecting system reliability to automation efficiency
- **Settlement Efficiency**: Linking settlement system reliability to capital efficiency and funding costs
- **Staff Productivity Metrics**: Relating system reliability to staff efficiency and capacity allocation
- **Cycle Time Impacts**: Connecting system performance to loan processing times and customer onboarding metrics

### Customer Experience Connections
- **Net Promoter Score (NPS) Correlation**: Mapping reliability metrics to customer satisfaction scores
- **Digital Adoption Rates**: Connecting system reliability to customer migration from branches to digital channels
- **Feature Utilization Metrics**: Linking system performance to feature adoption rates
- **Transaction Abandonment Analysis**: Correlating performance metrics with abandoned financial transactions

### Risk Management Connections
- **Fraud Detection Efficacy**: Connecting system reliability to fraud losses and prevention rates
- **Compliance Effectiveness**: Linking monitoring system reliability to regulatory compliance rates
- **Credit Decision Quality**: Relating system performance to credit decisioning accuracy and portfolio quality
- **Liquidity Risk Metrics**: Connecting treasury system reliability to liquidity management effectiveness

## 5. Tailoring to Audience Analysis Concerns

### Addressing Knowledge Gaps
- **Introduce Statistical Concepts Progressively**: Start with simple availability percentages before introducing percentiles, distribution analysis, and burn rates
- **Bridge from Familiar to New**: Connect traditional monitoring metrics to SLIs through explicit mapping exercises
- **Provide Calculation Frameworks**: Include concrete formulas and worked examples for error budget calculations
- **Visualize Abstract Concepts**: Use banking-specific visuals to illustrate the relationship between metrics, objectives, and error budgets

### Leveraging Existing Skills
- **Build on Troubleshooting Experience**: Frame SLI selection as an extension of root cause analysis skills
- **Connect to Existing Dashboards**: Show how current monitoring tools can be adapted for SLI measurements
- **Extend Impact Assessment Skills**: Build on existing incident impact assessment frameworks to develop SLO-based approaches
- **Enhance Documentation Practices**: Evolve familiar documentation patterns to incorporate SLO definitions and error budget policies

### Supporting Mindset Shifts
- **Illustrate Through Contrasts**: Provide side-by-side examples of reactive monitoring versus proactive reliability engineering
- **Progressive Responsibility Expansion**: Show how production support roles can incrementally adopt SRE practices
- **Risk-Based Decision Frameworks**: Connect error budget concepts to familiar risk management principles in banking
- **Emphasize Service Focus**: Use end-to-end service examples to shift thinking from component-level to service-level reliability

### Terminology and Example Refinements
- **Financial Services Glossary**: Provide banking-specific definitions of SRE terms
- **Familiar Tools Context**: Show how to implement concepts using both existing banking monitoring tools and newer platforms
- **Regulatory Framework Alignment**: Connect reliability concepts to familiar regulatory frameworks like operational resilience
- **Legacy System Integration**: Include examples spanning both modern microservices and traditional banking platforms
- **Incident Retrospectives**: Reframe familiar banking incidents through the lens of SLIs, SLOs, and error budgets

This tailored approach will help production support professionals in banking environments more effectively bridge the gap to SRE roles by connecting new concepts to their existing knowledge and experience while addressing their specific knowledge gaps and necessary mindset shifts.