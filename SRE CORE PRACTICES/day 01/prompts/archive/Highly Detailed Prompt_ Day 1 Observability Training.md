## **Highly Detailed Prompt: Day 1 Observability Training Module (v2)**

**Role**

You are an expert SRE instructor creating a comprehensive, Day 1 training module on the fundamentals of observability. Your materials build expertise from 🔍 Beginner to 🧩 Intermediate and end with 💡 Advanced/SRE. Your focus is on practical observability implementation with appropriate references to different tools and platforms (Prometheus, ELK Stack, Jaeger, etc.). Encourage humor or empathy when describing real-world issues.

**Objective**

Create a comprehensive, visually engaging, and practical Day 1 module on the Three Pillars of Observability (Metrics, Logs, Traces) that:

* Explains the fundamental concepts of metrics, logs, and traces with rich, detailed visuals and clear, actionable, step-by-step explanations.  
* Provides clear explanations of how each pillar contributes to overall observability.  
* Shows implementation examples with the specific practical Python code samples provided below.  
* Includes realistic examples of how observability solves real-world problems.  
* Emphasizes visual learning aids using the specific Mermaid diagrams provided below.  
* Incorporates real-world SRE principles around reliability and incident response.  
* Ensures smooth transitions between complexity tiers with explicit knowledge scaffolding ("brick by brick" approach).  
* Adheres strictly to the specified structure, content requirements, diagram definitions, code examples, and formatting rules outlined in this prompt.

**Target Audience**

Beginner 🔍 Beginner to 🧩Intermediate and 💡Advanced/SREand DevOps practitioners (ages 23-58, with 2-20 years of experience) who need to understand observability concepts to effectively implement monitoring and troubleshooting strategies. This is the first day of a comprehensive observability training program.

**Required Structure & Content:**

1. **Introduction: Observability 101**  
   * Enthusiastic welcome explaining why observability matters for modern systems.  
   * Explain observability using the "Observe, Test, Evaluate, Take Action" framework. Clarify how observability differs from monitoring.  
   * Brief explanation of the journey from basic monitoring to comprehensive observability (Include **Observability Maturity Model Diagram** here).  
   * Clear explanation of the three pillars: metrics, logs, and traces.  
   * **Visual:** Include the **Three Pillars Overview Diagram** exactly as defined below.  
   * **Incident Story:** Provide a real-world scenario story demonstrating how proper observability helps resolve incidents (e.g., "an alert was firing; logs were unclear; metrics saved the day").  
   * **Learning Objectives by Tier:** Include 4 measurable objectives for each tier (🔍 Beginner, 🧩 Intermediate, 💡 Advanced/SRE) covering different aspects of the three pillars.  
2. **Core Concept: Metrics (The Quantified View)**  
   * **Beginner 🔍:** Analogy (car dashboard), Definition, types (counters, gauges, histograms \- use **Metric Types Comparison Diagram**), purpose. Prometheus basics.  
   * **Intermediate 🧩:** RED method, custom metrics, basic visualization (referencing Grafana).  
   * **Advanced/SRE 💡:** How metrics enable monitoring/alerting, alert tuning, cardinality concerns, data pipeline issues, system performance impact.  
   * **Common Misconceptions:** Explicit warnings.  
   * **Visuals:**  
     * Include the **Metrics Collection Flow Diagram** exactly as defined below.  
     * Include the **Metric Types Comparison Diagram** exactly as defined below.  
   * **Implementation Comparison Table:** Show how metrics work in different platforms (e.g., Prometheus, Datadog, InfluxDB).  
   * **Horror Story:** Provide an example related to metrics (e.g., cardinality explosion brought Prometheus to its knees).  
   * **Video Placeholder:** {{VIDEO\_LINK\_METRICS}}.  
3. **Core Concept: Logs (The Narrative Thread)**  
   * **Beginner 🔍:** Analogy (journey journal), Definition, structure, log levels (use **Log Levels Hierarchy Diagram**), basic logging.  
   * **Intermediate 🧩:** Structured JSON logs, log aggregation (e.g., ELK/EFK). Use **Structured vs. Unstructured Logs Diagram**.  
   * **Advanced/SRE 💡:** How logs enable debugging/troubleshooting, querying logs for trace IDs, correlating error chains, system performance impact.  
   * **Common Misconceptions:** Explicit warnings.  
   * **Visuals:**  
     * Include the **Log Processing Pipeline Diagram** exactly as defined below.  
     * Include the **Structured vs. Unstructured Logs Comparison Diagram** exactly as defined below.  
     * Include the **Log Levels Hierarchy Diagram** exactly as defined below.  
   * **Implementation Comparison Table:** Show how logging works in different platforms (e.g., ELK Stack, Splunk, Graylog).  
   * **Horror Story:** Provide an example related to logging (e.g., grepping unstructured logs for hours due to missing request IDs).  
   * **Video Placeholder:** {{VIDEO\_LINK\_LOGS}}.  
4. **Core Concept: Traces (The Request's Journey)**  
   * **Beginner 🔍:** Analogy (GPS tracking), Definition, spans (use **Span Hierarchy Diagram**), trace IDs, visual timelines.  
   * **Intermediate 🧩:** Adding tracing to Flask with OpenTelemetry. Context propagation (use **Trace Context Propagation Diagram**).  
   * **Advanced/SRE 💡:** How traces enable performance analysis/debugging across microservices (use **Distributed Trace Flow Diagram**), system performance impact, sampling strategies.  
   * **Common Misconceptions:** Explicit warnings.  
   * **Visuals:**  
     * Include the **Distributed Trace Flow Diagram** exactly as defined below.  
     * Include the **Span Hierarchy Diagram** exactly as defined below.  
     * Include the **Trace Context Propagation Diagram** exactly as defined below.  
   * **Implementation Comparison Table:** Show how tracing works in different platforms (e.g., Jaeger, Zipkin, AWS X-Ray).  
   * **Horror Story:** Provide an example related to tracing (e.g., 5s checkout traced to a forgotten microservice timeout).  
   * **Video Placeholder:** {{VIDEO\_LINK\_TRACES}}.  
5. **Integrating the Three Pillars**  
   * Decision framework for implementing all three pillars.  
   * Show how metrics, logs, and traces correlate (via IDs, timestamps). Use the **Three Pillars Integration Diagram**.  
   * Demonstrate the investigation process using the **Incident Investigation Flow Diagram**.  
   * Common integration patterns and anti-patterns.  
   * **Visuals:**  
     * Include the **Three Pillars Integration Diagram** exactly as defined below.  
     * Include the **Incident Investigation Flow Diagram** exactly as defined below.  
   * **Tip Box:** Mention linking dashboards using shared metadata (e.g., trace\_id).  
   * **Video Placeholder:** {{VIDEO\_LINK\_INTEGRATION}}.  
6. **Hands-On Exercises / Tiered Challenges**  
   * **Beginner 🔍:** Identify which pillar to use for specific questions; Instrument Flask with Prometheus metrics (referencing Code Example 1).  
   * **Intermediate 🧩:** Evaluate existing implementations; Add JSON logs (referencing Code Example 2\) and build Kibana queries.  
   * **Advanced/SRE 💡:** Design comprehensive observability strategies; Correlate a trace (referencing Code Example 3\) from Jaeger with matching logs and metrics.  
   * **Bonus:** Suggest injecting a bug and tracing it across the stack.  
7. **Code Implementation Examples (Use these exact code blocks and explanations)**  
   * **7.1 Beginner Implementation: Basic Metrics with Python Flask** 🔍  
     * Provide the Python code example below for implementing basic metrics.  
     * Include step-by-step explanation of how the code works.  
     * Explain expected output and how to interpret metrics data from the /metrics endpoint.  
     * Include the **Request Metrics Sequence Diagram** (defined below) showing timing and counting.  
     * *(Optional: Include a simple component diagram showing Flask App \-\> Prometheus Client \-\> /metrics endpoint)*

   \# Code Example 1: Basic Metrics  
       from flask import Flask, request  
       import time  
       from prometheus\_client import Counter, Histogram, generate\_latest

       app \= Flask(\_\_name\_\_)

       \# Define metrics  
       REQUEST\_COUNT \= Counter('app\_requests\_total', 'Total request count', \['method', 'endpoint'\])  
       REQUEST\_LATENCY \= Histogram('app\_request\_latency\_seconds', 'Request latency in seconds', \['endpoint'\])

       @app.before\_request  
       def before\_request():  
           \# Store request start time  
           request.start\_time \= time.time()

       @app.after\_request  
       def after\_request(response):  
           \# Record request metrics  
           request\_latency \= time.time() \- request.start\_time  
           REQUEST\_COUNT.labels(method=request.method, endpoint=request.path).inc()  
           REQUEST\_LATENCY.labels(endpoint=request.path).observe(request\_latency)  
           return response

       @app.route('/')  
       def hello():  
           return "Hello World\!"

       @app.route('/metrics')  
       def metrics():  
           return generate\_latest()

       if \_\_name\_\_ \== '\_\_main\_\_':  
           app.run(host='0.0.0.0', port=5000)

   * **7.2 Intermediate Implementation: Adding Structured Logging** 🧩  
     * Build on the previous example by adding structured logging using the code below.  
     * Explain the importance of structured logging and request IDs for correlation.  
     * Show how logs and metrics can be correlated via common identifiers (like a request ID).  
     * Include the **Log Processing Pipeline Diagram** (defined below).  
     * *(Optional: Include a sequence diagram showing log generation during request handling)*

   \# Code Example 2: Adding Structured Logging  
       import structlog  
       import logging  
       import time  
       import uuid  
       from flask import Flask, request, g  
       from prometheus\_client import Counter, Histogram, generate\_latest

       \# Configure structured logging  
       logging.basicConfig(level=logging.INFO, format="%(message)s") \# Basic config for stdlib  
       structlog.configure(  
           processors=\[  
               structlog.stdlib.add\_log\_level,  
               structlog.stdlib.ProcessorFormatter.wrap\_for\_formatter,  
           \],  
           logger\_factory=structlog.stdlib.LoggerFactory(),  
           wrapper\_class=structlog.stdlib.BoundLogger,  
           cache\_logger\_on\_first\_use=True,  
       )  
       formatter \= structlog.stdlib.ProcessorFormatter(  
           processor=structlog.processors.JSONRenderer(),  
           foreign\_pre\_chain=\[structlog.stdlib.add\_log\_level\],  
       )  
       handler \= logging.StreamHandler()  
       handler.setFormatter(formatter)  
       root\_logger \= logging.getLogger()  
       root\_logger.addHandler(handler)  
       root\_logger.setLevel(logging.INFO)

       logger \= structlog.get\_logger()

       app \= Flask(\_\_name\_\_)

       \# Define metrics (same as before)  
       REQUEST\_COUNT \= Counter('app\_requests\_total', 'Total request count', \['method', 'endpoint'\])  
       REQUEST\_LATENCY \= Histogram('app\_request\_latency\_seconds', 'Request latency in seconds', \['endpoint'\])

       @app.before\_request  
       def before\_request():  
           \# Generate request ID for correlation  
           request.request\_id \= str(uuid.uuid4())  
           \# Store request start time  
           request.start\_time \= time.time()  
           \# Create request-scoped logger  
           g.logger \= logger.bind(request\_id=request.request\_id, endpoint=request.path)  
           g.logger.info("Request started", method=request.method, path=request.path)

       @app.after\_request  
       def after\_request(response):  
           \# Record request metrics  
           request\_latency \= time.time() \- request.start\_time  
           REQUEST\_COUNT.labels(method=request.method, endpoint=request.path).inc()  
           REQUEST\_LATENCY.labels(endpoint=request.path).observe(request\_latency)

           g.logger.info("Request completed",  
                         status\_code=response.status\_code,  
                         duration\_ms=request\_latency\*1000)  
           return response

       @app.route('/')  
       def hello():  
           g.logger.info("Processing hello request")  
           return "Hello World\!"

       @app.route('/metrics')  
       def metrics():  
           return generate\_latest()

       if \_\_name\_\_ \== '\_\_main\_\_':  
           app.run(host='0.0.0.0', port=5000)

   * **7.3 Advanced Implementation: Adding Distributed Tracing** 💡  
     * Complete the observability picture by adding tracing using the code below.  
     * Show how trace context propagates through the application using OpenTelemetry.  
     * Demonstrate the correlation between all three pillars (metrics, logs, traces) using the trace\_id.  
     * Include the **Distributed Trace Flow Diagram** (defined below).  
     * Include the **Three Pillars Integration Diagram** (defined below) to show the full picture.

\# Code Example 3: Adding Distributed Tracing  
import time  
import uuid  
import structlog  
import logging  
from flask import Flask, request, g  
from prometheus\_client import Counter, Histogram, generate\_latest

\# OpenTelemetry Imports  
from opentelemetry import trace  
from opentelemetry.exporter.jaeger.thrift import JaegerExporter  
from opentelemetry.sdk.resources import SERVICE\_NAME, Resource  
from opentelemetry.sdk.trace import TracerProvider  
from opentelemetry.sdk.trace.export import BatchSpanProcessor  
from opentelemetry.instrumentation.flask import FlaskInstrumentor

\# Configure structured logging (same as Intermediate example)  
logging.basicConfig(level=logging.INFO, format="%(message)s")  
structlog.configure(  
    processors=\[  
        structlog.stdlib.add\_log\_level,  
        structlog.stdlib.ProcessorFormatter.wrap\_for\_formatter,  
    \],  
    logger\_factory=structlog.stdlib.LoggerFactory(),  
    wrapper\_class=structlog.stdlib.BoundLogger,  
    cache\_logger\_on\_first\_use=True,  
)  
formatter \= structlog.stdlib.ProcessorFormatter(  
    processor=structlog.processors.JSONRenderer(),  
    foreign\_pre\_chain=\[structlog.stdlib.add\_log\_level\],  
)  
handler \= logging.StreamHandler()  
handler.setFormatter(formatter)  
root\_logger \= logging.getLogger()  
root\_logger.addHandler(handler)  
root\_logger.setLevel(logging.INFO)  
logger \= structlog.get\_logger()

\# Configure OpenTelemetry tracing  
resource \= Resource(attributes={SERVICE\_NAME: "example-flask-app-tracing"})  
trace.set\_tracer\_provider(TracerProvider(resource=resource))  
jaeger\_exporter \= JaegerExporter(  
    agent\_host\_name="localhost", \# Assumes Jaeger agent running locally  
    agent\_port=6831,  
)  
span\_processor \= BatchSpanProcessor(jaeger\_exporter)  
trace.get\_tracer\_provider().add\_span\_processor(span\_processor)  
tracer \= trace.get\_tracer(\_\_name\_\_)

app \= Flask(\_\_name\_\_)  
FlaskInstrumentor().instrument\_app(app) \# Auto-instrument Flask

\# Define metrics (same as before)  
REQUEST\_COUNT \= Counter('app\_requests\_total', 'Total request count', \['method', 'endpoint'\])  
REQUEST\_LATENCY \= Histogram('app\_request\_latency\_seconds', 'Request latency in seconds', \['endpoint'\])

@app.before\_request  
def before\_request():  
    \# Get trace context from OpenTelemetry instrumentation  
    span \= trace.get\_current\_span()  
    trace\_id \= format(span.get\_span\_context().trace\_id, '032x') if span.get\_span\_context().is\_valid else "N/A"  
    span\_id \= format(span.get\_span\_context().span\_id, '016x') if span.get\_span\_context().is\_valid else "N/A"

    \# Use trace ID for correlation if available, otherwise generate UUID  
    request.request\_id \= trace\_id if trace\_id \!= "N/A" else str(uuid.uuid4())

    \# Store request start time  
    request.start\_time \= time.time()

    \# Create request-scoped logger with trace context  
    g.logger \= logger.bind(  
        request\_id=request.request\_id, \# Use trace\_id if possible  
        trace\_id=trace\_id,  
        span\_id=span\_id,  
        endpoint=request.path  
    )  
    g.logger.info("Request started", method=request.method, path=request.path)

@app.after\_request  
def after\_request(response):  
    \# Record request metrics  
    request\_latency \= time.time() \- request.start\_time  
    REQUEST\_COUNT.labels(method=request.method, endpoint=request.path).inc()  
    REQUEST\_LATENCY.labels(endpoint=request.path).observe(request\_latency)

    g.logger.info("Request completed",  
                  status\_code=response.status\_code,  
                  duration\_ms=request\_latency\*1000)  
    return response

@app.route('/')  
def hello():  
    \# Example of creating a custom span within a route  
    with tracer.start\_as\_current\_span("process\_hello\_route") as span:  
        span.set\_attribute("custom.tag", "inside\_hello\_route")  
        g.logger.info("Processing hello request within custom span")  
        \# Simulate some work  
        time.sleep(0.01)  
        return "Hello World\!"

@app.route('/metrics')  
def metrics():  
    return generate\_latest()

if \_\_name\_\_ \== '\_\_main\_\_':  
    app.run(host='0.0.0.0', port=5000)

8. **Real-World Incident Walkthroughs**  
   * **Scenario 1: Detecting and Diagnosing a Performance Issue**  
     * Detailed walkthrough: Use metrics (latency spike) to detect, logs (DB timeouts, specific errors with request IDs) for context, and traces (long span in DB query or specific service call) to pinpoint root cause.  
     * Include specific examples from the code/tools.  
     * **Visual:** Include the **Incident Investigation Flow Diagram** (defined below).  
     * **Video Placeholder:** {{VIDEO\_LINK\_SCENARIO1}}.  
   * **Scenario 2: Tracking Down an Intermittent Error**  
     * Detailed walkthrough: Use metrics (low-level steady error rate) to reveal pattern, logs (NPE, specific user agent, correlated request IDs) for error context, and traces (failure path only occurs under specific conditions, e.g., certain user session type) to show failure path.  
     * Include specific examples from the code/tools.  
     * **Visual:** Include the **Incident Investigation Flow Diagram** (defined below, can be reused or adapted).  
     * **Video Placeholder:** {{VIDEO\_LINK\_SCENARIO2}}.  
9. **Required Mermaid Diagrams (Use these exact definitions)**  
   * **9.1 Three Pillars Overview Diagram:**  
     flowchart TD  
         subgraph "The Three Pillars"  
             M\["Metrics\<br/\>\<i\>What is happening?\</i\>"\]  
             L\["Logs\<br/\>\<i\>Why is it happening?\</i\>"\]  
             T\["Traces\<br/\>\<i\>Where is it happening?\</i\>"\]  
         end  
         subgraph "Observability Outcomes"  
             D\["Detection\<br/\>(Know something is wrong)"\]  
             I\["Investigation\<br/\>(Find the cause)"\]  
             R\["Resolution\<br/\>(Fix the issue)"\]  
             P\["Prevention\<br/\>(Avoid recurrence)"\]  
         end  
         M \--\> D  
         L \--\> I  
         T \--\> I  
         D \--\> I  
         I \--\> R  
         R \--\> P  
         P \--\> M

   * **9.2 Observability Maturity Model Diagram:**  
     flowchart TD  
         A\["Level 0:\<br/\>Basic Logging"\] \--\>|"Add structured logs"| B\["Level 1:\<br/\>Structured Logging"\]  
         B \--\>|"Add metrics"| C\["Level 2:\<br/\>Metrics & Logs"\]  
         C \--\>|"Add tracing"| D\["Level 3:\<br/\>Complete Three Pillars"\]  
         D \--\>|"Add correlation"| E\["Level 4:\<br/\>Correlated Observability"\]  
         E \--\>|"Add SLOs"| F\["Level 5:\<br/\>SLO-Driven Observability"\]

   * **9.3 Metrics Collection Flow Diagram:**  
     flowchart LR  
         subgraph "Application"  
             A\["Flask App"\] \--\> B\["Prometheus Client Library"\]  
             B \--\> C\["/metrics Endpoint"\]  
         end  
         subgraph "Collection & Storage"  
             D\["Prometheus Server"\]  
             C \-- "Scrape\<br/\>(e.g., Every 15s)" \--\> D  
             D \-- "Store Time\<br/\>Series Data" \--\> D  
         end  
         subgraph "Visualization & Alerting"  
             E\["Grafana Dashboard"\]  
             F\["Alertmanager"\]  
             D \--\>|"Query (PromQL)"| E  
             D \-- "Evaluate\<br/\>Alert Rules" \--\> F  
             F \-- "Send\<br/\>Notifications" \--\> G\["(Email/Slack/PagerDuty)"\]  
         end

   * **9.4 Metric Types Comparison Diagram:**  
     flowchart TD  
         subgraph "Counter"  
             C1\["Only Increases (or resets to 0 on restart)"\]  
             C2\["Example: app\_requests\_total"\]  
             C3\["Use Case: Counting events"\]  
         end  
         subgraph "Gauge"  
             G1\["Can Go Up or Down"\]  
             G2\["Example: memory\_usage\_bytes"\]  
             G3\["Use Case: Current state values"\]  
         end  
         subgraph "Histogram"  
             H1\["Distribution of Values (buckets)"\]  
             H2\["Example: app\_request\_latency\_seconds"\]  
             H3\["Use Case: Latency, request sizes"\]  
         end  
          subgraph "Summary (Alternative to Histogram)"  
             S1\["Client-side Quantiles"\]  
             S2\["Example: app\_request\_latency\_quantiles"\]  
             S3\["Use Case: Precise percentile calculation"\]  
         end

   * **9.5 Request Metrics Sequence Diagram:** (For Code Example 1\)  
     sequenceDiagram  
         participant C as Client  
         participant F as Flask App  
         participant P as Prometheus Client Lib

         C-\>\>F: HTTP Request (e.g., GET /)  
         activate F  
         F-\>\>F: Record request.start\_time  
         F-\>\>F: Process request logic  
         F-\>\>P: REQUEST\_COUNT.labels(...).inc()  
         F-\>\>P: REQUEST\_LATENCY.labels(...).observe(latency)  
         F--\>\>C: HTTP Response  
         deactivate F

         Note right of P: Metrics stored in memory

         participant Pr as Prometheus Server  
         Note over C,Pr: Later...  
         Pr-\>\>F: GET /metrics  
         activate F  
         F-\>\>P: generate\_latest()  
         P--\>\>F: Formatted Metrics Text  
         F--\>\>Pr: HTTP Response with Metrics  
         deactivate F

   * **9.6 Log Processing Pipeline Diagram:**  
     flowchart LR  
         subgraph "Application"  
             A\["Generate Log Event\<br/\>(e.g., using structlog)"\]  
             B\["Format as JSON\<br/\>(or other structured format)"\]  
             C\["Write to stdout/stderr/file"\]  
         end  
         subgraph "Collection"  
             D\["Log Agent/Shipper\<br/\>(e.g., Fluentd, Filebeat)"\]  
             E\["Log Aggregator/Processor\<br/\>(e.g., Logstash, Fluentd)"\]  
         end  
         subgraph "Storage & Search"  
             F\["Indexing & Storage\<br/\>(e.g., Elasticsearch, Loki)"\]  
             G\["Search & Visualization UI\<br/\>(e.g., Kibana, Grafana)"\]  
         end  
         A \--\> B  
         B \--\> C  
         C \--\> D  
         D \--\> E  
         E \--\> F  
         F \--\> G

   * **9.7 Structured vs. Unstructured Logs Comparison Diagram:**  
     flowchart TB  
         subgraph "Unstructured Log Example"  
             U\["ERROR: Request failed for user 123 at 2025-04-07 19:46:00"\]  
         end  
         subgraph "Structured Log Example (JSON)"  
             S\["{\<br/\>  \\"timestamp\\": \\"2025-04-07T19:46:00Z\\",\<br/\>  \\"level\\": \\"ERROR\\",\<br/\>  \\"message\\": \\"Request failed\\",\<br/\>  \\"user\_id\\": 123,\<br/\>  \\"request\_id\\": \\"abc-123\\",\<br/\>  \\"component\\": \\"payment-service\\"\<br/\>}"\]  
         end  
         U \--\> UA\["- Harder to parse automatically\<br/\>- Inconsistent format\<br/\>- Limited search/filtering\<br/\>- Difficult correlation"\]  
         S \--\> SA\["+ Machine-readable\<br/\>+ Consistent schema\<br/\>+ Rich querying & filtering\<br/\>+ Easy correlation"\]

   * **9.8 Log Levels Hierarchy Diagram:**  
     flowchart TD  
         E\["ERROR\<br/\>Critical failures, prevents normal operation"\]  
         W\["WARN\<br/\>Potential issues, unexpected situations"\]  
         I\["INFO\<br/\>Normal operational messages, milestones"\]  
         D\["DEBUG\<br/\>Detailed information for diagnosing problems"\]  
         T\["TRACE\<br/\>Very granular details, step-by-step execution"\]  
         E \--\> W  
         W \--\> I  
         I \--\> D  
         D \--\> T  
         style E fill:\#ffcccc,stroke:\#cc0000,stroke-width:2px  
         style W fill:\#ffffcc,stroke:\#cca300,stroke-width:2px  
         style I fill:\#ccffcc,stroke:\#009900,stroke-width:2px  
         style D fill:\#cce6ff,stroke:\#0066cc,stroke-width:2px  
         style T fill:\#e6ccff,stroke:\#9900cc,stroke-width:2px

   * **9.9 Distributed Trace Flow Diagram:**  
      flowchart LR  
         subgraph "User Request"  
             U\["Browser/Client"\]  
         end  
         subgraph "Service A (API Gateway)"  
             A1\["Receive Request\<br/\>Span A1 (Root)"\]  
             A2\["Auth Check\<br/\>Span A2"\]  
             A3\["Call Service B\<br/\>Span A3"\]  
             A4\["Return Response\<br/\>(Completes Span A1)"\]  
         end  
         subgraph "Service B (Order Service)"  
             B1\["Receive Request\<br/\>Span B1 (Child of A3)"\]  
             B2\["Query Database\<br/\>Span B2"\]  
             B3\["Call Service C\<br/\>Span B3"\]  
             B4\["Return Response\<br/\>(Completes Span B1)"\]  
         end  
          subgraph "Service C (Inventory Service)"  
             C1\["Receive Request\<br/\>Span C1 (Child of B3)"\]  
             C2\["Check Stock\<br/\>Span C2"\]  
             C3\["Return Response\<br/\>(Completes Span C1)"\]  
         end  
         subgraph "Database"  
             DB1\["Execute Query\<br/\>Span DB1 (Child of B2)"\]  
         end

         U \-- "TraceID: T1" \--\> A1  
         A1 \--\> A2  
         A2 \--\> A3  
         A3 \-- "TraceID: T1\<br/\>ParentSpan: A3" \--\> B1  
         B1 \--\> B2  
         B2 \-- "TraceID: T1\<br/\>ParentSpan: B2" \--\> DB1  
         DB1 \-- "Result" \--\> B2  
         B1 \--\> B3  
         B3 \-- "TraceID: T1\<br/\>ParentSpan: B3" \--\> C1  
         C1 \--\> C2  
         C2 \-- "Result" \--\> C1  
         C1 \-- "Result" \--\> B3  
         B4 \-- "Result" \--\> A3  
         A3 \--\> A4  
         A4 \-- "Final Response" \--\> U

         style A1 fill:\#f9f,stroke:\#333,stroke-width:2px  
         style B1 fill:\#ccf,stroke:\#333,stroke-width:2px  
         style C1 fill:\#cfc,stroke:\#333,stroke-width:2px

   * **9.10 Span Hierarchy Diagram:**  
     graph TD  
         A\["Trace T1: Handle /checkout Request (Root Span, 250ms)"\]  
         B\["Span B: Validate User (Child of A, 50ms)"\]  
         C\["Span C: Process Order (Child of A, 180ms)"\]  
         D\["Span D: DB Query \- Get Items (Child of C, 120ms)"\]  
         E\["Span E: Call Inventory Service (Child of C, 40ms)"\]  
         F\["Span F: Check Stock (Child of E, 30ms)"\]

         A \--\> B  
         A \--\> C  
         C \--\> D  
         C \--\> E  
         E \--\> F

         style A fill:\#f9f,stroke:\#333,stroke-width:2px  
         style C fill:\#ccf,stroke:\#333,stroke-width:2px  
         style E fill:\#cfc,stroke:\#333,stroke-width:2px

   * **9.11 Trace Context Propagation Diagram:**  
     sequenceDiagram  
         participant C as Client  
         participant G as API Gateway  
         participant S1 as Service 1  
         participant S2 as Service 2  
         participant DB as Database

         C-\>\>G: Request /order  
         activate G  
         Note over G: Generate Trace Context\<br/\>trace\_id: T1\<br/\>span\_id: S1 (root)  
         G-\>\>S1: Call /process (HTTP Header: traceparent=T1-S1-...)  
         activate S1  
         Note over S1: Start Span S2 (child of S1)  
         S1-\>\>S2: Call /validate (HTTP Header: traceparent=T1-S2-...)  
         activate S2  
         Note over S2: Start Span S3 (child of S2)  
         S2-\>\>DB: Query user data (Context in RPC metadata)  
         activate DB  
         Note over DB: Start Span S4 (child of S3)  
         DB--\>\>S2: Result  
         deactivate DB  
         Note over S2: End Span S3  
         S2--\>\>S1: Response (Validated)  
         deactivate S2  
         Note over S1: End Span S2  
         S1--\>\>G: Response (Processed)  
         deactivate S1  
         Note over G: End Span S1  
         G--\>\>C: Complete Response  
         deactivate G

   * **9.12 Three Pillars Integration Diagram:**  
     flowchart TD  
         subgraph "Request Flow & Data Generation"  
             A\["Incoming Request"\] \--\> B\["Generate/Propagate\<br/\>Trace ID (T1)\<br/\>Request ID (R1)"\]  
             B \--\> C\["Process Request\<br/\>(Generates Spans, Logs, Metrics)"\]  
             C \--\> D\["Return Response"\]  
         end

         subgraph "Observability Data"  
             M\["Metrics\<br/\>(e.g., request\_count{...}, latency{...})\<br/\>Labels may include endpoint, status"\]  
             L\["Logs (Structured)\<br/\>(e.g., JSON with level, msg, timestamp,\<br/\>\<b\>trace\_id=T1\</b\>, \<b\>request\_id=R1\</b\>)"\]  
             T\["Traces/Spans\<br/\>(Span Name, Duration, Tags,\<br/\>\<b\>trace\_id=T1\</b\>, parent\_id, span\_id)"\]  
         end

         C \-- "Emit Metrics" \--\> M  
         C \-- "Write Logs" \--\> L  
         C \-- "Record Spans" \--\> T

         subgraph "Storage & Analysis Systems"  
             PM\["Prometheus / Mimir\<br/\>(Metrics Storage)"\]  
             ES\["Elasticsearch / Loki\<br/\>(Log Storage)"\]  
             J\["Jaeger / Tempo\<br/\>(Trace Storage)"\]  
         end

         M \--\> PM  
         L \--\> ES  
         T \--\> J

         subgraph "Visualization & Correlation"  
             V\["Unified UI (e.g., Grafana)"\]  
             PM \--\>|Query| V  
             ES \--\>|Query/Link via TraceID| V  
             J \--\>|Query/Link via TraceID| V  
         end

         style V fill:\#lightblue,stroke:\#333,stroke-width:4px

   * **9.13 Incident Investigation Flow Diagram:**  
     flowchart TD  
         A\["Alert Triggered\!\<br/\>(e.g., High Error Rate on Service A)"\] \--\> B{View Metrics Dashboard\<br/\>(Grafana/Kibana)}  
         B \-- "Latency Spike?\<br/\>Error Count Increase?" \--\> C{Identify Time Window &\<br/\>Affected Components/Endpoints}  
         C \--\> D{Search Logs\<br/\>(Kibana/Loki/Splunk)}  
         D \-- "Filter by:\<br/\>- Time window\<br/\>- Service Name\<br/\>- ERROR level\<br/\>- Status Code (e.g., 5xx)" \--\> E{Analyze Error Logs\<br/\>(Stack traces, messages)}  
         E \-- "Found relevant logs?" \--\> F{"Extract Trace IDs\<br/\>from error logs"}  
         F \--\> G{View Traces\<br/\>(Jaeger/Tempo/Zipkin)}  
         G \-- "Filter by Trace ID" \--\> H{"Analyze Trace Spans:\<br/\>- Look for long durations\<br/\>- Look for error tags\<br/\>- Identify failing service call"}  
         H \--\> I(Identify Root Cause)  
         I \--\> J(Implement & Deploy Fix)  
         J \--\> K(Verify Fix via Metrics/Logs/Traces)

         subgraph "Pillars Used"  
             M1\["Metrics"\]  
             L1\["Logs"\]  
             T1\["Traces"\]  
         end  
         A \--\> M1  
         B \--\> M1  
         C \--\> M1  
         D \--\> L1  
         E \--\> L1  
         F \--\> L1  
         G \--\> T1  
         H \--\> T1  
         K \--\> M1 & L1 & T1

         style I fill:\#ccffcc,stroke:\#006600  
         style K fill:\#ccffcc,stroke:\#006600

10. **Mermaid Diagram Generation Guidelines (Apply these when generating diagrams)**  
    * Always enclose node labels in quotes if they contain special characters like (), :, or HTML tags like \<br/\>. Example: A\["Node with (Parentheses)"\].  
    * Use self-closing \<br/\> tags for line breaks within node labels, inside the quotes. Example: B\["First Line\<br/\>Second Line"\].  
    * Always wrap subgraph titles in quotes. Example: subgraph "My Subgraph".  
    * Place each connection/arrow (--\>, \---) on its own line for clarity.  
    * Do not add raw text immediately after a subgraph declaration; put text inside nodes.  
    * Keep characters like \#, ? inside quotes if needed within labels.  
    * Simplify complex diagrams or break them down if necessary. Test rendering.  
11. **Formatting Requirements**  
    * Use emojis consistently to indicate different sections and concept tiers (Beginner 🔍, Intermediate 🧩, Advanced/SRE 💡).  
    * Create clear Mermaid diagrams for visual representation using the exact code provided above. Format Mermaid code blocks properly using \`\`\`mermaid syntax.  
    * Ensure all tables (like Implementation Comparison) have consistent column widths and properly aligned headers.  
    * Use consistent formatting for code blocks, including \`\`\`python syntax highlighting for Python code provided above.  
    * Include clear transitions between sections.  
    * Organize content with hierarchical headings (H1, H2, H3...) for easy navigation.

**Invocation Summary**

Generate a comprehensive Day 1 SRE training module focused on the Three Pillars of Observability (metrics, logs, and traces), adhering strictly to all sections, content points, code examples, Mermaid diagram definitions, formatting rules, and guidelines specified in this prompt. Follow the "brick by brick" learning approach, introducing fundamental concepts (🔍) and building to advanced SRE-level techniques (💡). Each core concept section must include tiered learning objectives, its specific Python/Flask code example from above, its specific Mermaid diagrams defined above, a "horror story" with a fix, and a YouTube video placeholder. Ensure detailed, actionable explanations suitable for learners with diverse experience levels (ages 23-58, experience 2-20 years). The goal is real training material ready for production onboarding, reflecting the detail and structure outlined herein.