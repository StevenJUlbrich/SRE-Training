# ⚙️ Prompt: *Follow-the-Sun Chronicles* – Day 7: Mina & the Revenge of the Query Plan

> You are continuing the character-driven, regionally handed-off SRE training series called **The Follow-the-Sun Chronicles**, where each day is taught by a fictional global expert.
>
> For **Day 7**, your character is:
> - **Name:** Mina  
> - **Location:** Nigeria (Lagos)  
> - **Time:** 08:00 WAT  
> - **Role:** Performance tuning engineer and index strategist  
> - **Personality:** Blunt, no-nonsense, obsessed with execution plans. Calm in crisis but quietly judges bad indexes from across the room. Speaks with authority earned from rescuing countless queries from performance disasters.
>
> You are rewriting **ONLY Day 7** of the SRE Database Training Module (not Day 8), focusing on:
> - Indexing strategies (B-tree, Bitmap, Composite, etc.)  
> - Query performance fundamentals (response time, throughput, resource use)  
> - Reading execution plans  
> - Understanding table access paths (full scan vs index scan vs index-only scan)  
> - SQL dialect differences in indexing  
>
> **Constraints & Style:**
> 1. Begin with a **brief incident vignette**: a reporting query that took 7 hours to run and turned out to be scanning 9 million rows unindexed. Mina intervened, index drop-kicked it into performance, and now uses this story to introduce performance fundamentals.
> 2. Preserve the **original Day 7 module's technical content and structure**:
>    - The 10 core concepts already outlined in the material
>    - The "Observe, Test, Evaluate, and Take Action" framework
>    - Tiered learning objectives (🔍Beginner, 🧩Intermediate, 💡Advanced/SRE)
>    - SQL examples and system comparisons (Oracle focus, with PostgreSQL and SQL Server)
> 3. Narrate **everything** from **Mina's point of view**:
>    - She should speak in first person throughout: "Let me show you how this works" or "I've seen this mistake a thousand times"
>    - Her voice should be present in EVERY section, including technical explanations
>    - She explains performance like it's a discipline, not a suggestion
>    - She occasionally critiques past incidents where someone forgot an index
>    - She's obsessed with measuring things: rows scanned, blocks read, buffer cache hit ratios
> 4. For each of the 10 core concepts, include:
>    - Mina's personal experience with this concept (e.g., "I once fixed a query that was 300x slower than it should be because...")
>    - Her judgment of common mistakes ("This is where most people go wrong...")
>    - A practical lesson she learned the hard way
> 5. Use **Mermaid diagrams** from the original material but enhance them where possible:
>    - Visualizing index structures (B-tree, composite key traversal)
>    - Flow of a query through parse → optimize → execute → fetch
>    - Show table access methods (Full Scan vs Index Scan vs Index-Only Scan)
>    - All `sequenceDiagram` blocks must use `autonumber`  
>    - Use `&commat;` in place of `@` for all email addresses  
> 6. For each index type (especially B-tree, Bitmap, and composite), include:  
>    - A practical analogy from Mina (e.g., "A Bitmap index is like a punch card with checkboxes")  
>    - The existing Mermaid visual (enhanced if possible)
>    - At least one SQL example
>    - System impact analysis written from Mina's perspective
>    - Common misuse case that Mina has encountered (e.g., indexing low-cardinality columns with B-tree)  
> 7. Include a **sequenceDiagram** showing Mina tracing a slow query step by step:
>    - Getting the alert
>    - Running `EXPLAIN PLAN`
>    - Identifying the missing index
>    - Creating the index
>    - Verifying via `DBMS_XPLAN`
>    - Watching query times drop dramatically
> 8. Add a **flowchart** decision tree titled "Mina's Index Decision Tree: Do I need an index?" with checks for:
>    - Query patterns
>    - Table size
>    - Filter selectivity
>    - Read vs. write workload balance
>    - Cardinality considerations
> 9. Include a new section on **"Reading Execution Plans Like Mina"** with:
>    - A side-by-side execution plan comparison showing:
>      * Bad estimate (optimizer thinks 10 rows, gets 10K)
>      * Real impact (plan changes from Index Scan to Full Table Scan)
>    - Clear examples differentiating:
>      * `TABLE ACCESS FULL` and why it's not *always* bad
>      * `INDEX RANGE SCAN` vs `INDEX FULL SCAN` with when to use each
>    - Oracle-specific examples using `V$SQL_PLAN` to trace live plan usage
>    - PostgreSQL examples using `pg_stat_statements` for similar tracking
>    - Mina's commentary on plan-reading strategy
> 10. Add a comprehensive **"Mina's Table of Indexing Anti-Patterns"**:
>     
>     | Anti-Pattern | Why It's Bad | Mina's Take |
>     |--------------|--------------|-------------|
>     | No index on filter columns | Full scans everywhere | "This is DBA malpractice." |
>     | Index on low-cardinality columns | Waste of space, hurts inserts | "Don't index booleans." |
>     | Composite in wrong order | Index never gets used | "Like alphabetizing by first name." |
>     | Too many indexes on one table | Slows down all writes | "Death by a thousand cuts." |
>     | Index without analyzing data distribution | Can be worse than no index | "Like bringing a knife to a gunfight." |
>     | Using wrong index type | Poor performance or overhead | "Right tool, wrong job." |
> 
> 11. Include a visual diagram titled **"Index Sprawl: The Slow Death of Writes"** showing:
>     - A bloated table with too many indexes
>     - Arrows indicating how each DML operation gets progressively slower
>     - Performance metrics showing write degradation
>     - Mina's commentary on finding the right balance
> 12. Include Mina's commentary on:
>    - Index bloat ("I've seen databases where 40% of the storage was unused indexes!")
>    - Over-indexing ("Every unnecessary index is a performance tax on writes") 
>    - Index usage statistics monitoring ("If you're not measuring, you're guessing")
> 13. Include the existing 3 troubleshooting scenarios but reframed as Mina's personal war stories:
>     - "Let me tell you about the time I saved an e-commerce search function..."
>     - "I once dealt with a write bottleneck caused by 17 indexes on a single table..."
>     - "A developer came to me confused why their composite index wasn't being used..."
> 14. Keep the existing hands-on exercises but introduce them as "Mina's Training Drills" at each tier
> 15. Reformat the FAQ section as "Questions People Are Too Afraid To Ask Mina (But Should)"
> 16. Create "Mina's Query Tuning Commandments" with 5-7 rules like:
>     - "Thou shalt not perform a full table scan on millions of rows"
>     - "Thou shalt not create an index without measuring its impact"
> 17. End with a **handoff to Elijah in Cape Town**, who will take over Day 8 and dive into advanced query optimization, monitoring dashboards, and performance incident triage.
>
> **Tone:**  
> - Confident, direct, occasionally scolding but ultimately helpful
> - Deeply technical with high clarity
> - Occasional dry humor about performance disasters she's witnessed
> - Speaks like someone who has fixed every bad query with her bare hands and a keyboard
> - Slightly impatient with excuses but patient with genuine learning
>
> This is not a tutorial, blog post, or generic training document—it's a **structured technical training told through the voice and experience of Mina**, who lives and breathes query performance and has strong opinions about proper indexing that she's eager to share.

I've made the following enhancements to address your feedback:

1. **Added a detailed Execution Plan Reading section** (Point #9)
   - Side-by-side comparison showing bad estimates and their impact
   - Differentiation between TABLE ACCESS FULL and why it's not always bad
   - Comparison of INDEX RANGE SCAN vs INDEX FULL SCAN
   - Oracle-specific examples with V$SQL_PLAN
   - PostgreSQL examples with pg_stat_statements

2. **Added a comprehensive Anti-Patterns Table** (Point #10)
   - Includes six key anti-patterns
   - For each: what it is, why it's problematic, and Mina's pithy take
   - Formatted as a reference table that could be used as a cheat sheet

3. **Added an Index Sprawl visualization** (Point #11)
   - Titled "Index Sprawl: The Slow Death of Writes"
   - Shows the performance impact on write operations
   - Includes Mina's commentary on finding the right balance

These additions make the prompt more comprehensive while maintaining Mina's distinctive voice and expertise throughout the technical content. The result will be a much richer training document that combines her character's perspective with genuinely helpful, deeper technical insights.