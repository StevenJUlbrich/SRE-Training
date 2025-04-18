# 🖥️ Prompt: *Follow-the-Sun Chronicles* – Day 8: Elijah & the Latency that Lurks

> You're continuing the **Follow-the-Sun Chronicles**, a serialized global SRE training series where each day is led by a fictional character from a different region. This follows Day 7, which covered performance tuning fundamentals and indexing basics.
>
> For **Day 8**, your character is:
> - **Name:** Elijah  
> - **Location:** South Africa (Cape Town)  
> - **Time:** 08:00 SAST  
> - **Role:** Senior SRE and database telemetry specialist  
> - **Personality:** Tactical, ultra-composed, with dry humor. Thinks in query stats. Can diagnose slow write paths by examining I/O patterns without needing to see code.
>
> You're rewriting the **Day 8 SRE Database Training Module** on Advanced Performance Tuning & Monitoring, which covers:
> - Query optimization beyond indexes (rewrites, hints, statistics management)
> - Database configuration parameters and their impact on performance
> - Transaction log management in production environments
> - Performance monitoring dashboards and alert design
> - Wait events analysis and diagnostic approaches
> - Scaling and maintenance strategies for high-volume systems
>
> **Constraints & Style:**
> 1. Begin with a realistic incident: Elijah gets paged about a high-traffic database experiencing random query latency spikes. Investigation reveals a combination of suboptimal query plans, outdated statistics, and insufficient memory configuration.
>
> 2. Narrate from **Elijah's point of view** throughout the entire document:
>    - He approaches performance like a crime scene investigation
>    - Treats metrics and telemetry as "witnesses" to performance issues
>    - After explaining each concept, include an "Elijah's Field Note" with observations from real incidents
>    - Use phrases like "In my experience...", "When I see this pattern...", and "Here's what this tells us..."
>
> 3. Use **Mermaid diagrams** extensively:
>    - Query optimization flowcharts
>    - Monitoring dashboard layouts
>    - Database maintenance workflows
>    - Execution plan comparisons (before/after optimization)
>    - All `sequenceDiagram` blocks must use `autonumber`
>    - Use `&commat;` in place of `@` in any emails
>
> 4. For each core concept from the original Day 8 module (beyond indexing):
>    - Add an analogy from Elijah's perspective
>    - Include a Mermaid diagram visualizing the concept
>    - Provide SQL examples relevant to Oracle environments
>    - Explain the SRE impact and monitoring approach
>    - Share a war story about what happens when this goes wrong
>
> 5. For **Query Optimization Beyond Indexes** section:
>    - Explain query rewriting techniques with before/after examples
>    - Discuss subquery optimization and join order considerations
>    - Provide Oracle-specific hints with real examples
>    - Show how Elijah validates improvements using EXPLAIN PLAN
>    - **Include a side-by-side comparison of a bad query and its rewrite:**
>      ```sql
>      -- BEFORE
>      SELECT * FROM orders WHERE customer_id IN (SELECT customer_id FROM blacklist);
>      
>      -- AFTER
>      SELECT o.* FROM orders o JOIN blacklist b ON o.customer_id = b.customer_id;
>      ```
>    - Show the EXPLAIN PLAN output for both versions, highlighting the performance difference
>
> 6. For **Statistics Management** section:
>    - Detail how optimizer statistics affect execution plans
>    - Explain histogram analysis for data skew detection
>    - Include a flowchart for statistics refresh strategy
>    - Demonstrate how Elijah tracks plan stability after stats updates
>
> 7. For **Configuration Parameters** section:
>    - Discuss memory allocation, connections, and parallelism
>    - Show a decision tree for parameter tuning
>    - Include Elijah's rules for safe parameter changes in production
>    - Explain the monitoring feedback loop for configuration changes
>
> 8. For **Monitoring and Diagnostics** section:
>    - Detail performance metrics hierarchy from system to query level
>    - Show dashboard design principles with example layouts
>    - Include a triage flowchart: CPU vs. I/O vs. lock contention vs. plan issues
>    - Explain Elijah's personal monitoring toolkit and workflow
>    - **Include a "Wait Event Classification Map" as a Mermaid diagram:**
>      ```mermaid
>      flowchart LR
>          IO["I/O Waits"] -->|"db file sequential read"| Disk
>          Lock["Lock Waits"] -->|"row lock contention"| App
>          CPU["CPU Waits"] -->|"spinlock contention"| DB
>          Network["Network Waits"] -->|"SQL*Net message from client"| ClientApp
>          Config["Configuration Waits"] -->|"log file sync"| LogSystem
>      ```
>    - Use this diagram to show how Elijah classifies wait events for faster diagnosis
>
> 9. Include a comprehensive **SRE Scenario**:
>    - A detailed performance incident with timestamps
>    - Elijah's step-by-step investigation process as a `sequenceDiagram`
>    - The multi-pronged resolution strategy (query rewrites, stats refresh, memory tuning)
>    - Post-incident monitoring setup to prevent recurrence
>
> 10. For **Advanced/SRE level content**:
>     - Automating performance monitoring with real-time alerts
>     - Analyzing wait events and profiling data for bottleneck identification
>     - Strategies for large-scale partitioning and sharding
>     - Implementing capacity planning based on historical performance data
>     - **Add specific capacity planning example:**
>       "I track storage growth rate (MB/day) and query load (queries/sec) over 3 months. If both exceed 30%+ growth, I begin planning for shard expansion. When CPU utilization consistently exceeds 65% during normal operations, that's my signal to evaluate either vertical scaling or query optimization efforts. Latency above P95 SLO for more than 10% of a week triggers automatic tuning advisor runs."
>
> 11. End with **Elijah's Performance Monitoring Go-Bag**:
>     - Essential SQL queries for quick diagnostics
>     - Key metrics and their alert thresholds
>     - Favorite tools ready for deployment
>     - Dashboard templates for common scenarios
>
> 12. Conclude with a handoff to Chloé in France, who will cover Day 9 on SQL vs NoSQL architecture decisions and operational tradeoffs.
>
> **Tone:**
> - Professional but conversational—like a senior colleague walking you through their thought process
> - Measured and methodical, reflecting Elijah's composed demeanor
> - Occasionally slipping into dry humor when discussing "interesting" performance patterns
> - Focuses on evidence and metrics rather than hunches
>
> This should read like an expert SRE's field guide to performance management—filled with real-world wisdom, practical tools, and a methodical approach to problem-solving that blends technical rigor with years of operational experience.