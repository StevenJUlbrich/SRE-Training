# 📊 Comprehensive Prompt: Day 1 Observability Training Module

## 🎯 Purpose & Overview

This prompt will guide the creation of a comprehensive, engaging, and practical Day 1 training module on the Three Pillars of Observability: Metrics, Logs, and Traces. The resulting material should serve as production-ready onboarding content that builds expertise from beginner to SRE-level through a practical, step-by-step approach centered around real-world incidents and their resolutions.

## 👥 Target Audience

Beginner to Intermediate SREs and DevOps practitioners (ages 23-58, with 2-20 years of experience) who need to understand observability concepts to effectively implement monitoring and troubleshooting strategies. This is the first day of a comprehensive observability training program.

## 🧱 Learning Approach

Use a "brick-by-brick" teaching methodology that:
- Starts with fundamentals and progressively builds complexity
- Makes concepts tangible through real-world incidents and "horror stories with happy endings"
- Reinforces learning with visual aids (diagrams), code examples, and hands-on exercises
- Offers tiered content for different experience levels (🔍 Beginner, 🧩 Intermediate, 💡 Advanced/SRE)
- Encourages empathy and humor when describing real-world operational challenges
- Centers learning around actual incident scenarios rather than abstract theory

## 📋 Content Requirements

### Required Module Structure

1. **Introduction: Observability 101**
   - Begin with a compelling incident story that highlights the consequences of poor observability
   - Explain observability using the "Observe, Test, Evaluate, Take Action" framework
   - Clearly distinguish between monitoring and observability
   - Provide an overview of the Three Pillars (metrics, logs, traces) and their relationships
   - Introduce a fictional company ("TechNow") and recurring characters that will appear throughout the module
   - Visual: Include a Three Pillars Overview Diagram showing relationships between pillars and outcomes
   - Video Placeholder: {{VIDEO_LINK_INTRO}}
   - Learning Objectives: List 4 measurable objectives for each tier (Beginner, Intermediate, Advanced/SRE)

2. **Core Concept: Metrics (The Quantified View)**
   - **Incident First**: Begin with a real metrics-related incident at "TechNow" that shows:
     - The initial alert/detection of a problem
     - The confusion without proper metrics
     - The resolution once proper metrics were implemented
   - 🔍 Beginner: Provide an intuitive analogy (e.g., car dashboard), define metrics types (counters, gauges, histograms)
   - 🧩 Intermediate: Explain practical implementation, visualization techniques, RED/USE methods
   - 💡 Advanced/SRE: Discuss advanced concerns like cardinality issues, alerting strategies, and system performance impact
   - Visual: Include diagrams showing metrics collection flow and comparison of metric types
   - Implementation Comparison: Table comparing metrics in different platforms (Prometheus, Datadog, InfluxDB)
   - **Horror Story Framework**:
     - Setting: Brief context of "TechNow" during a specific event
     - Crisis: The metrics-related incident that occurred
     - Confusion: Initial troubleshooting challenges
     - Discovery: The 'aha moment' using metrics
     - Resolution: How the issue was fixed
     - Lesson: Key takeaway about metrics-based observability
   - Video Placeholder: {{VIDEO_LINK_METRICS}}

3. **Core Concept: Logs (The Narrative Thread)**
   - **Incident First**: Begin with a log-related incident at "TechNow" involving the same characters and systems from the metrics section
   - 🔍 Beginner: Provide an intuitive analogy (e.g., journey journal), explain log levels and basic logging
   - 🧩 Intermediate: Teach structured JSON logs, log aggregation techniques
   - 💡 Advanced/SRE: Show advanced log querying, correlation with metrics and traces, performance considerations
   - Visual: Include diagrams showing log processing pipeline and structured vs. unstructured logs comparison
   - Implementation Comparison: Table comparing logging in different platforms (ELK Stack, Splunk, Graylog)
   - **Horror Story Framework**:
     - Setting: Follow-up incident at "TechNow" (reference previous metrics incident)
     - Crisis: A logging-related issue that compounds or relates to previous incident
     - Confusion: Challenges due to poor logging practices
     - Discovery: How proper logging revealed the root cause
     - Resolution: Implementation of better logging
     - Lesson: Key takeaway about the importance of quality logs
   - Video Placeholder: {{VIDEO_LINK_LOGS}}

4. **Core Concept: Traces (The Request's Journey)**
   - **Incident First**: Begin with a complex distributed systems issue at "TechNow" that metrics and logs couldn't solve alone
   - 🔍 Beginner: Provide an intuitive analogy (e.g., GPS tracking), explain spans, trace IDs, and visualization
   - 🧩 Intermediate: Demonstrate trace context propagation and implementation in distributed systems
   - 💡 Advanced/SRE: Discuss sampling strategies, overhead considerations, and complex debugging techniques
   - Visual: Include diagrams showing distributed trace flow, span hierarchy, and trace context propagation
   - Implementation Comparison: Table comparing tracing in different platforms (Jaeger, Zipkin, AWS X-Ray)
   - **Horror Story Framework**:
     - Setting: Major incident at "TechNow" affecting multiple services
     - Crisis: Complex, intermittent failures in a distributed system
     - Confusion: Metrics and logs providing incomplete picture
     - Discovery: How tracing revealed the complex interaction failure
     - Resolution: Cross-service fixes implemented
     - Lesson: Key takeaway about end-to-end visibility
   - Video Placeholder: {{VIDEO_LINK_TRACES}}

5. **Integrating the Three Pillars**
   - Begin with a complex incident that requires all three pillars working together
   - Provide a practical incident response framework that shows:
     - How alerts from metrics trigger initial response
     - How logs provide immediate context during triage
     - How traces help pinpoint exact failure points
     - The communication flow during incidents
   - Provide a decision framework for implementing all three pillars together
   - Show how metrics, logs, and traces correlate using shared IDs and timestamps
   - Demonstrate a workflow for investigating incidents using all three pillars
   - Identify common integration patterns and anti-patterns
   - Visual: Include diagrams showing three pillars integration and incident investigation flow
   - Video Placeholder: {{VIDEO_LINK_INTEGRATION}}

6. **Hands-On Exercises / Tiered Challenges**
   - Structure exercises as incident simulations rather than abstract tasks
   - 🔍 Beginner: Investigate a simulated incident using basic metrics; implement simple metrics in Flask
   - 🧩 Intermediate: Debug a problem using structured logs; create meaningful dashboards
   - 💡 Advanced/SRE: Solve a complex distributed systems issue using all three pillars
   - Provide clear setup instructions and success criteria for each exercise

7. **Code Implementation Examples**
   - Frame each implementation example as a solution to a specific incident type
   - **Beginner Implementation**: Basic Metrics with Python Flask to detect performance issues
   - **Intermediate Implementation**: Adding Structured Logging to debug error patterns
   - **Advanced Implementation**: Adding Distributed Tracing to solve complex service interaction issues
   - Each example should build on the previous one, showing the progression of a complete observability solution

8. **Real-World Scenarios**
   - **Scenario 1**: Detecting and Diagnosing a Performance Issue
   - **Scenario 2**: Tracking Down an Intermittent Error
   - Each scenario should continue the "TechNow" narrative and involve the recurring characters
   - Show practical application of all three pillars to solve a realistic problem

9. **War Room Simulation**
   - Conclude the training with a comprehensive "War Room Simulation" that:
     - Presents a complex, realistic incident scenario at "TechNow"
     - Guides learners through the detection, investigation, and resolution process
     - Requires the use of all three pillars in concert
     - Includes decision points with consequences
     - Provides a realistic timeline pressure element
   - Include a post-incident review template and analysis
   - Show how observability data drives permanent improvements

### Narrative Framework Requirements

1. **Consistent Company and Characters**
   - Create a fictional but realistic company ("TechNow") with:
     - A clear business model (e.g., e-commerce platform, SaaS provider)
     - A defined architecture (microservices, databases, etc.)
     - Recurring characters with distinct roles:
       - Junior SRE learning observability
       - Experienced team lead
       - Developer who struggles with ops concepts
       - Business stakeholder affected by incidents
   - Reference these characters consistently throughout all incidents and examples
   - Show their growth and learning as observability improves

2. **Connected Incident Narrative**
   - Make each incident story connect to previous ones:
     - Reference past incidents when introducing new problems
     - Show how previous solutions helped detect new issues faster
     - Build complexity throughout the narrative
     - Demonstrate incremental improvements in observability practices

3. **Horror Story Framework**
   - For each pillar, include a narrative that follows this pattern:
     - Setting: Brief context of "TechNow" and the system state
     - Crisis: The incident that occurred (with business impact)
     - Confusion: Initial troubleshooting challenges
     - Discovery: The 'aha moment' using the relevant observability pillar
     - Resolution: How the issue was fixed
     - Lesson: Key takeaway about observability

### Required Code Examples

For each pillar, include fully functional Python code examples that learners can run themselves:

**1. Beginner Implementation: Basic Metrics with Python Flask**
```python
from flask import Flask, request
import time
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

# Define metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total request count', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency in seconds', ['endpoint'])

@app.before_request
def before_request():
    # Store request start time
    request.start_time = time.time()

@app.after_request
def after_request(response):
    # Record request metrics
    request_latency = time.time() - request.start_time
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()
    REQUEST_LATENCY.labels(endpoint=request.path).observe(request_latency)
    return response

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**2. Intermediate Implementation: Adding Structured Logging**
```python
import structlog
import logging
import time
import uuid
from flask import Flask, request, g
from prometheus_client import Counter, Histogram, generate_latest

# Configure structured logging
logging.basicConfig(level=logging.INFO)
structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
)

logger = structlog.get_logger()
app = Flask(__name__)

# Define metrics (same as before)
REQUEST_COUNT = Counter('app_requests_total', 'Total request count', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency in seconds', ['endpoint'])

@app.before_request
def before_request():
    # Generate request ID for correlation
    request.request_id = str(uuid.uuid4())
    # Store request start time
    request.start_time = time.time()
    # Create request-scoped logger
    g.logger = logger.bind(request_id=request.request_id, endpoint=request.path)
    g.logger.info("Request started", method=request.method, path=request.path)

@app.after_request
def after_request(response):
    # Record request metrics
    request_latency = time.time() - request.start_time
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()
    REQUEST_LATENCY.labels(endpoint=request.path).observe(request_latency)
    
    g.logger.info("Request completed", 
                 status_code=response.status_code, 
                 duration_ms=request_latency*1000)
    return response

@app.route('/')
def hello():
    g.logger.info("Processing hello request")
    return "Hello World!"

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**3. Advanced Implementation: Adding Distributed Tracing**
```python
import time
import uuid
import structlog
import logging
from flask import Flask, request, g
from prometheus_client import Counter, Histogram, generate_latest
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Configure structured logging (same as before)
logging.basicConfig(level=logging.INFO)
structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
)
logger = structlog.get_logger()

# Configure OpenTelemetry tracing
resource = Resource(attributes={SERVICE_NAME: "example-flask-app"})
trace.set_tracer_provider(TracerProvider(resource=resource))
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)
tracer = trace.get_tracer(__name__)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

# Define metrics (same as before)
REQUEST_COUNT = Counter('app_requests_total', 'Total request count', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency in seconds', ['endpoint'])

@app.before_request
def before_request():
    # Get trace context
    span = trace.get_current_span()
    trace_id = format(span.get_span_context().trace_id, '032x')
    span_id = format(span.get_span_context().span_id, '016x')
    
    # Generate request ID (using trace ID)
    request.request_id = trace_id
    # Store request start time
    request.start_time = time.time()
    
    # Create request-scoped logger with trace context
    g.logger = logger.bind(
        request_id=request.request_id,
        trace_id=trace_id,
        span_id=span_id,
        endpoint=request.path
    )
    g.logger.info("Request started", method=request.method, path=request.path)

@app.after_request
def after_request(response):
    # Record request metrics
    request_latency = time.time() - request.start_time
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()
    REQUEST_LATENCY.labels(endpoint=request.path).observe(request_latency)
    
    g.logger.info("Request completed", 
                 status_code=response.status_code, 
                 duration_ms=request_latency*1000)
    return response

@app.route('/')
def hello():
    with tracer.start_as_current_span("process_hello") as span:
        span.set_attribute("custom.tag", "example")
        g.logger.info("Processing hello request")
        # Simulate some work
        time.sleep(0.01)
        return "Hello World!"

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Required Diagram Types

Include these Mermaid diagrams to enhance understanding of the concepts:

**1. Three Pillars Overview Diagram**
```mermaid
flowchart TD
    subgraph "The Three Pillars"
        M["Metrics<br/>What is happening?"]
        L["Logs<br/>Why is it happening?"]
        T["Traces<br/>Where is it happening?"]
    end
    
    subgraph "Observability Outcomes"
        D["Detection<br/>(Know something is wrong)"]
        I["Investigation<br/>(Find the cause)"]
        R["Resolution<br/>(Fix the issue)"]
        P["Prevention<br/>(Avoid recurrence)"]
    end
    
    M --> D
    L --> I
    T --> I
    D --> I
    I --> R
    R --> P
    P --> M
```

**2. Metrics Collection Flow Diagram**
```mermaid
flowchart LR
    subgraph "Application"
        A["Flask App"] --> B["Prometheus Client"]
        B --> C["/metrics Endpoint"]
    end
    
    subgraph "Collection & Storage"
        D["Prometheus Server"]
        C -->|"Scrape<br/>Every 15s"| D
        D -->|"Store Time<br/>Series Data"| D
    end
    
    subgraph "Visualization & Alerting"
        E["Grafana Dashboard"]
        F["Alert Manager"]
        D -->|"Query"| E
        D -->|"Evaluate Alert Rules"| F
        F -->|"Send<br/>Notifications"| G["Email/Slack/PagerDuty"]
    end
```

**3. Log Processing Pipeline Diagram**
```mermaid
flowchart LR
    subgraph "Application"
        A["Generate Log"] --> B["Format as JSON"]
        B --> C["Write to stdout"]
    end
    
    subgraph "Collection"
        D["Log Agent/Shipper<br/>(Filebeat/Fluentd)"]
        E["Log Aggregator<br/>(Logstash)"]
    end
    
    subgraph "Storage & Search"
        F["Index & Store<br/>(Elasticsearch)"]
        G["Search Interface<br/>(Kibana)"]
    end
    
    C --> D
    D --> E
    E --> F
    F --> G
```

**4. Distributed Trace Flow Diagram**
```mermaid
flowchart LR
    subgraph "Service A"
        A1["Receive Request"]
        A2["Process Data"]
        A3["Call Service B"]
        A4["Return Response"]
    end
    
    subgraph "Service B"
        B1["Receive Request"]
        B2["Query Database"]
        B3["Return Response"]
    end
    
    subgraph "Database"
        D1["Execute Query"]
    end
    
    subgraph "Tracing Context"
        T["Trace ID: abc-123"]
    end
    
    A1 --> A2
    A2 --> A3
    A3 --> B1
    B1 --> B2
    B2 --> D1
    D1 --> B3
    B3 --> A4
    
    T --- A1
    T --- A2
    T --- A3
    T --- B1
    T --- B2
    T --- D1
    T --- B3
    T --- A4
```

**5. Three Pillars Integration Diagram**
```mermaid
flowchart TD
    subgraph "Request Processing"
        A["Incoming Request"] --> B["Generate trace_id/request_id"]
        B --> C["Process Request"]
        C --> D["Return Response"]
    end
    
    subgraph "Observability Pillars"
        M["Metrics<br/>- Request count<br/>- Latency histogram"]
        L["Logs<br/>- Structured JSON<br/>- Contains trace_id"]
        T["Traces<br/>- Request path<br/>- Span timing"]
        
        B -->|"trace_id"| L
        B -->|"trace_id"| T
        C -->|"metrics"| M
        C -->|"events"| L
        C -->|"spans"| T
    end
    
    subgraph "Storage & Analysis"
        PM["Prometheus"]
        ES["Elasticsearch"]
        J["Jaeger"]
        
        M --> PM
        L --> ES
        T --> J
    end
    
    subgraph "Visualization"
        G["Grafana"]
        K["Kibana"]
        JU["Jaeger UI"]
        
        PM --> G
        ES --> K
        J --> JU
        
        G <-->|"Cross-reference<br/>by time"| K
        K <-->|"Link via<br/>trace_id"| JU
        JU <-->|"Performance<br/>metrics"| G
    end
```

**6. Incident Investigation Flow Diagram**
```mermaid
flowchart TD
    A["Alert Triggered:<br/>High Error Rate"] -->|"View"| B["Metrics Dashboard"]
    B -->|"Find affected<br/>time period"| C["Log Search"]
    C -->|"Filter by error<br/>status codes"| D["Error Log Entries"]
    D -->|"Extract trace IDs<br/>from logs"| E["Trace View"]
    E -->|"Analyze trace<br/>for errors"| F["Root Cause<br/>Identification"]
    F -->|"Implement fix"| G["Verify via Metrics"]
```

**7. War Room Communication Flow**
```mermaid
flowchart LR
    subgraph "Incident Detection"
        A["Alert Triggered"] --> B["On-Call Engineer<br/>Acknowledges"]
    end
    
    subgraph "Initial Response"
        C["Create Incident Channel"]
        D["Notify Stakeholders"]
        E["Begin Investigation"]
    end
    
    subgraph "Incident Management"
        F["Assign Incident Commander"]
        G["Divide Investigation Tasks"]
        H["Regular Status Updates"]
    end
    
    subgraph "Resolution"
        I["Identify Root Cause"]
        J["Implement Fix"]
        K["Verify Resolution"]
        L["Post-Incident Review"]
    end
    
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I --> J
    J --> K
    K --> L
```

### Diagram Creation Guidelines

When creating Mermaid diagrams for the training module, follow these formatting rules to ensure proper rendering:

1. Always enclose node labels in quotes if they contain special characters like `()`, `:`, or HTML tags like `<br/>`. Example: `A["Node with (Parentheses)"]`.
2. Use self-closing `<br/>` tags for line breaks within node labels, inside the quotes. Example: `B["First Line<br/>Second Line"]`.
3. Always wrap subgraph titles in quotes. Example: `subgraph "My Subgraph"`.
4. Place each connection/arrow (`-->`, `---`) on its own line for clarity.
5. Do not add raw text immediately after a subgraph declaration; put text inside nodes.
6. Keep characters like `#`, `?` inside quotes if needed within labels.
7. Simplify complex diagrams or break them down if necessary.

## ✅ Format & Style Guidelines

1. **Section Structure**
   - Use consistent headings and subheadings for easy navigation
   - Include clear transitions between sections that maintain the narrative flow
   - Organize content from fundamental to advanced concepts
   - Connect each new concept to the ongoing "TechNow" storyline

2. **Visual Elements**
   - Use emojis consistently to indicate different sections and concept tiers (🔍 Beginner, 🧩 Intermediate, 💡 Advanced/SRE)
   - Format Mermaid code blocks properly using the ```mermaid syntax
   - Ensure all tables have consistent column widths and properly aligned headers
   - Include visuals of "TechNow" systems where appropriate

3. **Code Examples**
   - Use consistent formatting for code blocks, including syntax highlighting for Python
   - Include step-by-step explanations for each code example
   - Show the progressive evolution of code from basic to advanced implementations
   - Frame each code example as a solution to a specific incident type

4. **Narrative Elements**
   - Include realistic "horror stories with happy endings" for each pillar following the specified framework
   - Use the same fictional company ("TechNow") and recurring characters throughout all examples
   - Build a progressive narrative where each incident connects to previous ones
   - Use empathy and occasional humor to make technical content more relatable
   - Emphasize practical problem-solving rather than theory alone

## 🔥 Implementation Suggestions

1. **Real-World Integration**
   - Show how the three pillars work together in practice through incident scenarios
   - Provide examples of correlation between metrics, logs, and traces in resolving actual issues
   - Demonstrate incident investigation workflows using all three pillars
   - Include communication patterns and team dynamics during incidents

2. **Learning Reinforcement**
   - Include knowledge check questions at the end of each section tied to the narrative
   - Provide hands-on exercises as incident simulations that apply concepts incrementally
   - Offer extension activities for those who want to go deeper
   - Include debriefing questions after each incident story

3. **Accessibility**
   - Use analogies and visualizations to make abstract concepts concrete
   - Ensure explanations are clear for those with minimal prior exposure
   - Provide reference links for additional learning resources
   - Use the recurring characters to represent different learning styles and backgrounds

4. **Incident Response Framework**
   - Include a complete incident response framework that shows:
     - How alerts from metrics trigger initial response
     - How logs provide immediate context during triage
     - How traces help pinpoint exact failure points
     - The communication flow during incidents
     - Post-incident analysis and improvement using all three pillars

## 📝 Final Invocation

Create a comprehensive Day 1 SRE training module on the Three Pillars of Observability (metrics, logs, and traces) that follows a narrative-driven, incident-centric approach. Build around a fictional but realistic company ("TechNow") with recurring characters whose story progresses throughout the module. Each concept should be introduced through a real incident scenario that demonstrates its practical value, following the "horror story with happy ending" framework.

The module should include:
- Detailed explanations of each pillar with tiered learning objectives
- Practical Python code examples for implementation
- Clear Mermaid diagrams illustrating key concepts and workflows
- Realistic incident narratives that demonstrate the value of observability
- Hands-on exercises structured as incident simulations
- A War Room simulation that brings all concepts together
- Video placeholders for multimedia integration

The resulting training material should be comprehensive enough to serve as a standalone learning resource while maintaining accessibility for learners with diverse experience levels. Most importantly, it should teach observability through the lens of real operational problems and their solutions, making the concepts both engaging and immediately applicable.