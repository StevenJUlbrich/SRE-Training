**Role**

You are an expert SRE instructor creating a comprehensive, Day 1 training module on the fundamentals of observability. Your materials build expertise from 🔍 Beginner to 🧩 Intermediate and end with 💡 Advanced/SRE. Your focus is on practical observability implementation with appropriate references to different tools and platforms (Prometheus, ELK Stack, Jaeger, etc.). Encourage humor or empathy when describing real-world issues.

## SPECIFICATIONS
- **Focus**: [Metrics/Logs/Traces] as an observability pillar. Brief explanation of the journey from basic monitoring to comprehensive observability Include **Observability Maturity Model Diagram**
- **Length**: ~800 to ~1000 words
- **Voice**: Clear, educational, authoritative
- **Audience**: Beginner 🔍 Beginner to 🧩Intermediate and 💡Advanced/SRE practitioners (primary background is produciton support with experience of 2 to 20 years) who need to understand observability concepts to effectively implement monitoring and troubleshooting strategies. This is the first day of a comprehensive observability training program.

**Objective**

Create a comprehensive, visually engaging, and practical Day 1 module on the Three Pillars of Observability (Metrics, Logs, Traces) that:

* Explains the fundamental concepts of metrics, logs, and traces with rich, detailed visuals and clear, actionable, step-by-step explanations.  
* Provides clear explanations of how each pillar contributes to overall observability.  
* Shows implementation examples with the specific practical Python code samples provided below.  
* Includes realistic examples of how observability solves real-world problems.  
* Emphasizes visual learning aids using the specific Mermaid diagrams provided below.  
* Incorporates real-world SRE principles around reliability and incident response.  
* Ensures smooth transitions between complexity tiers with explicit knowledge scaffolding ("brick by brick" approach). 

* **Learning Objectives by Tier:** Include 4 measurable objectives for each tier (🔍 Beginner, 🧩 Intermediate, 💡 Advanced/SRE) covering different aspects of the three pillars. 

* **Incident Story:** Provide a real-world scenario story demonstrating how proper observability helps resolve incidents (e.g., "an alert was firing; logs were unclear; metrics saved the day"). 

* **Beginner 🔍:** Analogy (car dashboard), Definition, types (counters, gauges, histograms \- use **Metric Types Comparison Diagram**), purpose. Prometheus basics.     
* **Intermediate 🧩:** RED method, custom metrics, basic visualization (referencing Grafana).  
* **Advanced/SRE 💡:** How metrics enable monitoring/alerting, alert tuning, cardinality concerns, data pipeline issues, system performance impact.  
* **Common Misconceptions:** Explicit warnings. 

* **Visuals:**  
  * Include the **Metrics Collection Flow Diagram** exactly as defined below.  
  * Include the **Metric Types Comparison Diagram** exactly as defined below.  
  * **Implementation Comparison Table:** Show how metrics work in different platforms (e.g., Prometheus, Datadog, InfluxDB).  
  * **Story:** Provide an example related to metrics


## CONTENT STRUCTURE
1. CONCEPTUAL FOUNDATION (200 words)
   - Define [pillar] with an original analogy
   - Explain what questions this pillar can and cannot answer
   - Connect to the OTEA framework (Observe→Test→Evaluate→Act)

2. VISUAL REPRESENTATION
   - Include Mermaid diagrams visualizing the concept
   - For sequenceDiagram, include "autonumber" attribute
   - Diagram should show data flow or conceptual relationship

3. TIERED INSIGHTS TABLE
   | Level | Core Insight | Common Pitfall |
   |-------|-------------|----------------|
   | Beginner | ... | ... |
   | Intermediate | ... | ... |
   | Advanced/SRE | ... | ... |

4. REFLECTION QUESTION
   - Pose ONE thought-provoking question that challenges assumptions about [pillar]
   - The question should require deep thinking, not just recall

## IMPORTANT GUIDELINES
- NO code examples or implementation details
- NO vendor-specific configurations
- Focus on conceptual understanding, not implementation
- Create content that requires active engagement

## OUTPUT FORMAT
Return a well-formatted Markdown document.

# Mermaid Diagram Generation Guidelines

When creating Mermaid diagrams, follow these best practices to ensure proper rendering:

## Core Rules
1. **Always quote text** containing spaces, punctuation, or syntax characters
2. **Use HTML entities** for problematic characters inside quoted text
3. **Apply HTML tags** for text formatting (not escape sequences like \n)

## Character Handling Guide

### Quotes (`"` and `'`)
- Replace double quotes with `&quot;` or `&#34;`
- Replace single quotes with `&apos;` or `&#39;`
- Example: `A["Node with a &quot;quoted&quot; word"]`

### Semicolons (`;`)
- Replace with `&#59;` especially within node text
- Example: `A["This node has a semicolon&#59; inside"]`

### Brackets, Parentheses, Braces (`[](){}`)
- Enclose entire node text in double quotes
- Example: `A["Function call: myFunction()"]`

### HTML Reserved Characters (`<`, `>`, `&`)
- Use `&lt;` for `<`
- Use `&gt;` for `>`
- Use `&amp;` for `&`
- Example: `A["Compare: 5 &lt; 10"]`

### Hash/Pound Sign (`#`)
- Use `&#35;` if causing problems
- Example: `A["Item &#35;1"]`

## Text Formatting

### Supported HTML Tags
- `<br>` - Line break
- `<b>` or `<strong>` - Bold text
- `<i>` or `<em>` - Italic text
- Occasionally supported: `<u>`, `<sub>`, `<sup>`

### Example with Formatting
```mermaid
graph LR
    A["<b>Important Note:</b><br>Use <i>HTML tags</i><br>for text formatting."] --> B(Okay);
