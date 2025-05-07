# Traces and Distributed Tracing 101+ Curriculum: A Hybrid Graphic Novel Approach

## Project Vision

The Traces and Distributed Tracing Curriculum is an innovative educational initiative that transforms complex Site Reliability Engineering (SRE) concepts into an engaging hybrid graphic novel format. This curriculum aims to bridge the gap between traditional IT operations monitoring (like ITRS Geneos) and modern Traces and Distributed Tracing practices for production support professionals in the banking industry.

## Core Project Goals

Transform Technical Learning: Replace dry, abstract technical documentation with narrative-driven, visually engaging content that makes Traces and Distributed Tracing concepts memorable and applicable.
Banking Industry Focus: Ground all examples, scenarios, and case studies in real banking system impacts to ensure immediate practical relevance for financial sector professionals.
Character-Driven Education: Utilize a diverse cast of characters with different backgrounds and technical proficiencies to represent various learning perspectives and challenges in adopting Traces and Distributed Tracing practices.
Progressive Skill Building: Structure content in three distinct tiers (Foundations, Intermediate, Advanced) to guide learners from basic monitoring concepts to sophisticated Traces and Distributed Tracing strategies.
Visual Reinforcement: Employ carefully crafted panel sequences and consistent visual language to illustrate technical concepts, system behaviors, and problem-solving approaches.

## Format Innovation

This curriculum pioneers a hybrid approach that combines:

Narrative Teaching: Conversational, story-driven explanations of technical concepts
Visual Panels: Sequential art depicting real-world scenarios and technical visualizations
Technical Depth: Substantial prose sections with banking-specific examples and practical applications
Character Development: Consistent characterization of Hector and supporting cast to create emotional investment in the learning journey

## Target Outcomes

The curriculum aims to transform how banking professionals approach system reliability by:

Building a deep understanding of the differences between monitoring and Traces and Distributed Tracing
Developing practical skills in interpreting logs, metrics, and traces
Creating a mental framework for identifying and addressing system reliability issues proactively
Establishing a shared vocabulary and approach to metric across technical teams

This hybrid format combines the depth of written instruction with the visual engagement of graphic novels to create a uniquely effective educational experience for technical professionals in the banking sector.


## Within Each Panel includes 

- Teaching Narrative

- Common Example of the Problem.

- SRE Best Practice: Evidence-Based Investigation

- Banking or Releated Area Impact

- Correction or Implementation Guidance


### Example 

# Chapter 1: From Monitoring to Observability - The Logging Evolution

## Panel 1: The Midnight Alert - Limitations of Traditional Monitoring
**Scene Description**: A dimly lit operations center at 2 AM. A banking support engineer stares anxiously at multiple monitoring dashboards showing green status indicators while simultaneously fielding angry calls from customers unable to complete wire transfers. Confusion and frustration are evident as the disconnect between monitoring and reality creates chaos.

### Teaching Narrative
Traditional monitoring has created a dangerous illusion in banking systems: the belief that green dashboards equal customer satisfaction. This "monitoring mindset" focuses primarily on system health metrics (CPU, memory, disk space) while missing the true measure of reliability—customer experience. In banking, this disconnect is particularly perilous, as transaction processing systems can experience subtle failures that traditional threshold-based monitoring completely misses. What begins here as confusion will evolve throughout our journey into a fundamentally different approach to understanding system behavior through comprehensive logging practices.

### Common Example of the Problem
A major retail bank recently experienced a critical failure during end-of-month processing when their international wire transfer system began silently rejecting transactions with specific currency combinations. The operations dashboard showed all systems green—CPU utilization was normal, memory consumption within thresholds, network connectivity stable, and all service health checks passing. Yet the customer support lines were flooded with high-value clients unable to complete urgent transfers. The monitoring system, focused entirely on infrastructure metrics and basic ping tests, completely missed that the currency validation service was returning successful responses while incorrectly flagging legitimate transactions as potentially fraudulent. Without proper logging of the actual transaction outcomes and validation decisions, engineers spent over four hours searching for a problem that was invisible to their monitoring tools.

### SRE Best Practice: Evidence-Based Investigation
SRE teams must implement outcome-based monitoring that focuses on customer experience rather than just system health. This requires shifting from infrastructure-centric metrics to transaction-centric logging that captures the actual success or failure of business operations. Evidence-based investigation starts with comprehensive logging of business outcomes: success rates for different transaction types, detailed error information when operations fail, and context-rich event recording that captures not just that something happened but why it happened.

Rather than relying on dashboards to infer system health, SREs should directly validate business functionality through synthetic transactions that simulate actual customer journeys. When incidents occur, the investigation should begin with customer impact assessment through outcome logs rather than system health checks. By collecting evidence of what customers are actually experiencing rather than what internal systems are reporting about themselves, SREs can bridge the gap between technical monitoring and business reality.

### Banking Impact
The business consequences of this monitoring gap are severe and multifaceted. Direct financial impacts include failed transactions that may be lost entirely if customers abandon the process, potentially representing millions in lost transaction revenue. Customer experience deteriorates rapidly, with each minute of undetected issues causing exponential increases in support calls and customer frustration.

For high-net-worth clients attempting significant international transfers, these failures damage trust and can lead to relationship termination—with average customer lifetime value losses of $25,000 to $250,000 per lost relationship. Regulatory consequences are equally concerning, as undetected processing issues may result in compliance failures for time-sensitive transactions like securities settlements or tax payments. Perhaps most critically, reputational damage compounds with duration—studies show that 38% of retail banking customers who experience transaction failures without prompt notification and resolution consider switching providers within 90 days.

### Implementation Guidance
1. Implement transaction-outcome logging that records the success or failure of every business operation, not just system health.
2. Create customer journey maps for critical banking functions and ensure logging covers each step from the customer's perspective.
3. Develop synthetic transaction monitors that simulate actual customer operations and verify business outcomes, not just technical availability.
4. Establish business-aligned monitoring dashboards that prominently display success rates for key transaction types alongside traditional infrastructure metrics.
5. Implement correlation identifiers that connect customer actions across multiple systems to enable end-to-end visibility.
6. Establish baseline metrics for normal transaction success rates and volumes, with automated alerting for deviations that might indicate silent failures.
7. Create incident response playbooks that begin with assessment of customer impact logs rather than system health metrics.