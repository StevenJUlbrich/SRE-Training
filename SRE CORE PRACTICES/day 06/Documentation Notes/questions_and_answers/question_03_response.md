# SRE Training Material: Service-Level Indicators, Objectives, and Error Budgets

## High-Level Chapter Outline

### Chapter 1: From Monitoring to Observability - The SRE Mindset Shift
This chapter introduces the fundamental shift from traditional monitoring to observability-driven reliability engineering. It explores how production support professionals typically approach system health through alert-based monitoring and contrasts this with the SRE approach of measuring what matters to users. The chapter establishes the mental model transition needed when moving from reactive support to proactive reliability engineering, setting the foundation for understanding SLIs, SLOs, and Error Budgets.

### Chapter 2: Understanding Service-Level Indicators (SLIs) - Measuring What Matters
This chapter defines SLIs as the direct measures of customer experience and explains why they are the foundational metrics for reliability engineering. It demonstrates how to identify appropriate SLIs for different banking services by focusing on customer journeys and critical user transactions. The chapter guides readers through the process of transitioning from conventional IT metrics (CPU, memory, disk) to meaningful service performance indicators that directly impact customer experience in banking applications.

### Chapter 3: The Anatomy of Quality Metrics - Building Effective SLIs
This chapter dives deeper into the technical aspects of constructing well-defined SLIs for banking systems. It explores the four golden signals (latency, traffic, errors, saturation) and how they translate to banking contexts like payment processing, account management, and trading systems. The chapter provides frameworks for identifying good vs. poor SLIs, addressing common pitfalls in metric selection, and ensuring metrics truly reflect customer experience in financial services.

### Chapter 4: Implementing SLIs - From Theory to Practice
This chapter bridges theoretical understanding of SLIs to practical implementation in banking environments. It covers the technical approaches to collecting SLI data through logs, metrics, and traces in complex financial systems. The chapter addresses the challenges of implementing SLIs in heterogeneous banking infrastructures with both legacy and modern components, providing concrete examples of SLI implementation for core banking functions.

### Chapter 5: Service-Level Objectives (SLOs) - Setting Reliability Targets
This chapter introduces SLOs as target values for SLIs that define the boundary between reliable and unreliable service from the customer perspective. It explains how to set appropriate reliability targets for different types of banking services, considering business criticality, user expectations, and regulatory requirements. The chapter demonstrates the transition from implicit reliability assumptions in production support to explicit, measurable objectives in SRE practice.

### Chapter 6: SLO Engineering - Designing for Reliability
This chapter explores the nuanced process of engineering SLOs that balance user expectations with technical and business realities in banking environments. It covers time windows, aggregation methods, and multiple burn rates when establishing SLOs for different banking services. The chapter addresses how to align SLOs with business priorities, regulatory requirements, and the specific reliability needs of financial services, including considerations for critical financial processing windows.

### Chapter 7: Error Budgets - The Currency of Reliability
This chapter introduces error budgets as the practical implementation of SLOs that create a reliability "currency" for engineering teams. It demonstrates how error budgets quantify the acceptable level of unreliability and provide an objective framework for making engineering decisions in banking systems. The chapter explores how error budgets help balance innovation speed with reliability requirements, addressing the common tension between development velocity and system stability in financial services.

### Chapter 8: Error Budget Policies - Creating Reliability Frameworks
This chapter guides readers through the development and implementation of error budget policies that govern how reliability is managed across banking services. It covers the creation of decision frameworks for responding to error budget consumption, establishing alerting thresholds, and defining escalation procedures. The chapter addresses how to integrate error budget policies with change management processes in highly regulated banking environments, ensuring compliance while enabling engineering agility.

### Chapter 9: SLO-Based Alerting - From Threshold Alerts to Customer Impact
This chapter demonstrates the transformation from traditional threshold-based alerting to SLO-based alerting strategies that focus on customer impact. It provides frameworks for designing alert systems based on error budget consumption rates rather than raw metric values in banking applications. The chapter shows how to reduce alert fatigue while increasing meaningful signal detection, addressing the common challenges of excessive alerting in production support roles transitioning to SRE.

### Chapter 10: Multi-Dimensional SLOs - Advanced Reliability Engineering
This chapter explores advanced approaches to SLOs that capture complex service quality definitions through multi-dimensional objectives. It demonstrates how to design SLOs that consider multiple aspects of reliability simultaneously, addressing the complex interdependencies in banking systems. The chapter covers critical financial use cases like transaction processing where multiple dimensions of reliability (correctness, performance, consistency) must be considered together.

### Chapter 11: Quantifying Business Impact - The Economics of Reliability
This chapter addresses the critical connection between technical reliability metrics and business outcomes in financial services. It demonstrates methodologies for quantifying the business impact of reliability issues, including financial losses, customer attrition, and regulatory penalties. The chapter guides readers through approaches for communicating reliability in business terms to non-technical stakeholders, helping production support professionals develop the business translation skills needed in SRE roles.

### Chapter 12: SLI/SLO Maturity Models - The Reliability Journey
This chapter presents a maturity model for evolving SLI and SLO implementations as organizations progress in their reliability engineering practice. It covers the progression from basic SLIs to sophisticated reliability measurements across banking service portfolios. The chapter provides roadmaps for reliability evolution based on organizational maturity, helping readers understand how to progressively improve reliability practices and advocate for advancement within their banking institutions.

### Chapter 13: Reliability in Complex Financial Systems - Real-World Challenges
This chapter addresses the practical challenges of implementing reliability engineering in complex financial ecosystems with multiple dependencies and components. It explores approaches for managing SLOs across service boundaries, addressing third-party dependencies, and handling reliability in distributed banking systems. The chapter provides frameworks for understanding service topologies and dependencies, with particular focus on the unique challenges in modern interconnected financial platforms.

### Chapter 14: The Operational Cadence - Living with SLOs and Error Budgets
This chapter outlines the day-to-day practices and operational rhythms for teams managing services through SLOs and error budgets. It covers regular SLO reviews, error budget reports, and continuous improvement processes in banking technology organizations. The chapter demonstrates how to incorporate reliability data into sprint planning, incident reviews, and quarterly business reviews, establishing the operational framework that sustains effective reliability engineering in financial services.

### Chapter 15: Future of Financial Services Reliability - Emerging Trends and Practices
This concluding chapter explores emerging trends in reliability engineering for financial services, including AI-driven reliability prediction, regulatory technology integration, and advanced observability practices. It addresses how banking-specific reliability practices are evolving with new technologies and regulatory frameworks. The chapter provides perspective on how SREs in financial services can prepare for future reliability challenges and opportunities, setting a vision for continued professional development beyond the course material.