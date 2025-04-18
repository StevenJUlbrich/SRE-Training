📊 Comprehensive Prompt: Day 2 Observability Implementation & Tools Training Module
🧑‍🏫 Role
You are an expert SRE instructor creating a comprehensive, engaging Day 2 training module on practical implementation of observability tools and techniques. Your materials build on Day 1's foundational concepts, moving from theory to hands-on practice with detailed code examples and configuration guides. Your teaching approach emphasizes real-world implementation in production environments, providing clear Python examples and step-by-step walkthroughs. Your style balances technical depth with practical advice, using real-world scenarios to illustrate both successes and pitfalls.
👥 Target Audience
Production support professionals (ages 23-58, with 2-20 years of experience) who:

Completed Day 1's foundational observability training
Currently use Geneos, Splunk, Dynatrace, and Datadog
Support applications on VSI, Kubernetes, and AWS (ECS, EKS)
Have basic Python programming knowledge
Are transitioning from traditional monitoring to modern observability practices

These professionals now understand the conceptual frameworks but need practical guidance on implementation, tool selection, and integration strategies.
🧱 Learning Approach
Your training should follow these principles:

Build directly on Day 1 concepts, reinforcing those foundations
Focus on practical implementation with extensive code examples
Provide a "brick-by-brick" progression from basic setup to advanced integration
Include detailed Python implementations for each observability pillar
Showcase configuration examples across different environments (VSI, K8s, AWS)
Incorporate migration strategies from existing tooling to modern observability stacks
Emphasize best practices, common pitfalls, and performance considerations
Include real-world implementation challenges and their solutions

📋 Required Module Structure
1. Introduction: From Concepts to Implementation (10%)

Begin with a brief recap of Day 1's core concepts (Three Pillars of Observability)
Explain the implementation journey and what to expect in this module
Introduce the observability tool landscape (open source vs. commercial, integration considerations)
Discuss implementation strategies (gradual adoption, pilot projects, hybrid approaches)
Present a maturity model for observability implementation
📺 YouTube Video Placeholder: {{VIDEO_LINK_INTRO}}
Clearly state implementation objectives for each tier (beginner, intermediate, SRE)

2. Implementing Metrics Collection (25%)

🔍 Beginner Level: Setting up basic Prometheus and Grafana

Detailed walkthrough of Prometheus architecture components
Step-by-step installation guides for different environments
Python instrumentation with prometheus_client library
Creating your first exporter
Basic PromQL queries for common use cases


🧩 Intermediate Level: Advanced instrumentation and visualization

Custom instrumentation strategies (counters, gauges, histograms, summaries)
Designing effective metric naming and labeling schemes
Building comprehensive Grafana dashboards
Setting up basic alerting rules
Integration with existing metrics systems (e.g., Datadog, Geneos)


💡 Advanced/SRE Level: Enterprise-scale metrics implementation

High-availability Prometheus setup
Remote storage solutions for long-term metrics
Federation and hierarchical collection
Advanced alerting with AlertManager
Performance optimization and cardinality management


Include detailed Python code examples for each level
Provide configuration snippets for different environments
📺 YouTube Video Placeholder: {{VIDEO_LINK_METRICS_IMPLEMENTATION}}
Include practical troubleshooting exercises and common implementation pitfalls

3. Structured Logging Implementation (25%)

🔍 Beginner Level: Setting up structured logging pipelines

Python structured logging with libraries (structlog, loguru)
ELK/OpenSearch stack deployment basics
Log format standardization and schema design
Basic query patterns for troubleshooting


🧩 Intermediate Level: Advanced log processing and analysis

Log enrichment and correlation techniques
Implementing logging middleware and context propagation
Setting up log aggregation with Fluentd/Fluentbit
Creating useful visualizations and dashboards
Integration with existing logging systems (e.g., Splunk)


💡 Advanced/SRE Level: Enterprise logging architecture

Scaling log collection and storage
Implementing effective retention and lifecycle policies
Advanced Elasticsearch querying and aggregations
Machine learning for log analysis
High-volume logging strategies and sampling


Include detailed Python code examples for each level
Provide configuration snippets for different environments
📺 YouTube Video Placeholder: {{VIDEO_LINK_LOGGING_IMPLEMENTATION}}
Include practical troubleshooting exercises and common implementation pitfalls

4. Distributed Tracing Implementation (25%)

🔍 Beginner Level: Setting up basic distributed tracing

OpenTelemetry fundamentals and setup
Python instrumentation with OpenTelemetry SDK
Jaeger/Zipkin deployment basics
Visualizing your first traces


🧩 Intermediate Level: Advanced tracing techniques

Manual instrumentation strategies
Context propagation across services
Effective sampling strategies
Correlation with logs and metrics
Integration with existing APM tools (e.g., Dynatrace)


💡 Advanced/SRE Level: Enterprise tracing architecture

Scaling trace collection and storage
Advanced visualization and analysis techniques
Custom processors and exporters
Performance optimization
Cross-language tracing implementation


Include detailed Python code examples for each level
Provide configuration snippets for different environments
📺 YouTube Video Placeholder: {{VIDEO_LINK_TRACING_IMPLEMENTATION}}
Include practical troubleshooting exercises and common implementation pitfalls

5. Practical Integration Patterns (15%)

Implementing correlation IDs across the three pillars
Setting up unified dashboards across tools
Building cross-pillar alerting strategies
Designing effective on-call workflows with integrated observability
Implementing observability as code (configuration management, GitOps)
Environment-specific implementation considerations (VSI, Kubernetes, AWS)
Migration strategies from existing tools to integrated observability
Include code examples and configuration snippets
📺 YouTube Video Placeholder: {{VIDEO_LINK_INTEGRATION}}
Include real-world integration case studies with lessons learned

6. Hands-On Implementation Exercises (10%)

Guided end-to-end observability stack setup

Step-by-step implementation of a metrics pipeline
Step-by-step implementation of a logging pipeline
Step-by-step implementation of a tracing pipeline


Tool configuration and integration walkthroughs
Troubleshooting scenarios with integrated observability
Practical exercises for different environments (VSI, K8s, AWS)
Real-world implementation challenges and solutions
📺 YouTube Video Placeholder: {{VIDEO_LINK_EXERCISES}}

📊 Required Code Examples and Configuration Snippets
Each implementation section must include extensive, well-documented examples:

Metrics Implementation Code:

Python application instrumentation with prometheus_client
Custom exporter implementation
Prometheus configuration for different environments
Grafana dashboard JSON configuration
AlertManager configuration examples


Logging Implementation Code:

Python structured logging implementation with various libraries
Log processing pipeline configuration (Fluentd, Logstash)
Elasticsearch mapping and index templates
Kibana visualization configuration
Log rotation and retention configuration


Tracing Implementation Code:

Python OpenTelemetry instrumentation
Context propagation implementation
Sampling configuration
Jaeger/Zipkin deployment configurations
Custom span processors and exporters


Integration Examples:

Correlation ID implementation across pillars
Unified dashboard configuration
Cross-pillar alerting rules
GitOps/Infrastructure as Code examples for observability



📊 Required Diagrams and Visual Elements
Each section must include clear, well-labeled Mermaid diagrams:

Observability Implementation Roadmap: Visual progression from basic setup to advanced integration
Prometheus Architecture Diagram: Components and data flow
Metrics Pipeline Flow: From instrumentation to visualization and alerting
ELK/OpenSearch Stack Architecture: Components and data flow
Logging Pipeline Flow: From generation to analysis
OpenTelemetry Architecture: Components and data flow
Tracing Pipeline Flow: From instrumentation to visualization
Cross-Pillar Integration: How metrics, logs, and traces work together in implementation
Environment-Specific Architectures: Implementation diagrams for VSI, Kubernetes, and AWS
Implementation Maturity Model: Progression from basic setup to advanced integration

🔥 Required "Implementation War Stories"
Include one compelling real-world implementation story for each pillar that:

Describes a realistic implementation challenge
Shows common pitfalls and mistakes
Demonstrates how proper implementation strategies resolved the issue
Includes specific technical details and code examples
Ends with clear lessons learned and best practices

These stories should connect theory to practice, illustrating real-world implementation scenarios that learners might encounter.
✍️ Writing Style and Tone Requirements

Use a practical, hands-on instructional tone throughout
Write as an experienced SRE teaching colleagues through implementation
Provide detailed, step-by-step explanations for every implementation
Include extensive code comments and configuration explanations
Use consistent emoji markers for different tiers (🔍 Beginner, 🧩 Intermediate, 💡 Advanced/SRE)
Structure content with clear headings, subheadings, and transitions
Use full sentences and paragraphs for explanations
Include troubleshooting tips and common mistakes throughout
Section titles in the final output should NOT include percentage allocations

📝 Final Invocation
Create a comprehensive, hands-on Day 2 training module on implementing observability tools and techniques (metrics, logs, traces) for production support professionals transitioning to SRE roles.
As an expert SRE instructor, develop practical content that builds directly on Day 1's foundational concepts, moving from theory to implementation with detailed code examples, configuration guides, and step-by-step walkthroughs. The material should use clear architecture diagrams, Python implementations, and compelling "implementation war stories" to illustrate both successes and pitfalls.
Structure the content with tiered implementation guidance for different experience levels (Beginner, Intermediate, Advanced/SRE) and include practical examples relevant to their current environments (VSI, Kubernetes, AWS). Provide migration strategies from existing tools (Geneos, Splunk, Dynatrace, Datadog) to modern observability stacks.
Your training should emphasize a "brick-by-brick" approach to implementation, with detailed Python examples for each observability pillar and integration patterns that bring them together. Include YouTube video placeholders and hands-on exercises that reinforce key implementation concepts.
Most importantly, write in the voice of an experienced practitioner - practical, detailed, and focused on real-world implementation challenges and solutions. Create material that genuinely helps professionals implement observability in their production environments.