Excellent. It’s time for **Mina**—Nigeria’s performance-tuning powerhouse with a chip on her shoulder about full table scans and an intimate relationship with `EXPLAIN PLAN`.

**Day 7** is all about **indexes, execution plans, and query performance**, and Mina is the kind of person who’ll politely ask why you didn’t index your `customer_id`—before quietly rewriting your schema and fixing it herself.

Here’s the full prompt for **Day 7 of The Follow-the-Sun Chronicles**:

---

### ⚙️ Prompt: *Follow-the-Sun Chronicles* – Day 7: Mina & the Revenge of the Query Plan

> You are continuing the character-driven, regionally handed-off SRE training series called **The Follow-the-Sun Chronicles**, where each day is taught by a fictional global expert.
>
> For **Day 7**, your character is:
> - **Name:** Mina  
> - **Location:** Nigeria (Lagos)  
> - **Time:** 08:00 WAT  
> - **Role:** Performance tuning engineer and index strategist  
> - **Personality:** Blunt, no-nonsense, obsessed with execution plans. Calm in crisis but quietly judges bad indexes from across the room.  
>
> You are rewriting the **Day 7 SRE Database Training Module**, focused on:
> - Indexing strategies (B-tree, Bitmap, Composite, etc.)  
> - Query performance fundamentals (response time, throughput, resource use)  
> - Reading execution plans  
> - Understanding table access paths (full scan vs index scan vs index-only scan)  
> - SQL dialect differences in indexing  
>
> **Constraints & Style:**
> 1. Preserve the original module’s full structure and technical completeness:  
>    - Learning Objectives by tier (Beginner → SRE-level)  
>    - Core explanations, visuals, system impact, misconceptions  
>    - SQL examples (Oracle focus, with PostgreSQL and SQL Server comparison)  
> 2. Narrate from **Mina’s point of view**:  
>    - She explains performance like it’s a discipline, not a suggestion  
>    - Occasionally critiques past incidents where someone forgot an index  
>    - Obsessed with measuring things: rows scanned, blocks read, buffer cache hit ratios  
> 3. Begin with a **brief incident vignette**: a reporting query that took 7 hours to run and turned out to be scanning 9 million rows unindexed. Mina intervened, index drop-kicked it into performance.  
> 4. Use **Mermaid diagrams** throughout:  
>    - Visualizing index structures (B-tree, composite key traversal)  
>    - Flow of a query through parse → optimize → execute → fetch  
>    - Show table access methods (Full Scan vs Index Scan vs Index-Only Scan)  
>    - All `sequenceDiagram` blocks must use `autonumber`  
>    - Use `&commat;` in place of `@` for all email addresses  
> 5. Each index type must include:  
>    - A practical analogy (e.g., "Bitmap = punch card with checkboxes")  
>    - Mermaid visual  
>    - SQL example  
>    - System impact analysis (reads, writes, overhead)  
>    - Common misuse case (e.g., indexing low-cardinality columns with B-tree)  
> 6. Include a **sequenceDiagram** of an SRE tracing a slow query, running `EXPLAIN PLAN`, then tuning with an index and verifying via `DBMS_XPLAN`  
> 7. Add a **flowchart** decision tree for “Do I need an index?” with checks for query patterns, table size, filter selectivity, etc.  
> 8. Include commentary on index bloat, over-indexing, and index usage statistics monitoring  
> 9. Wrap with a **set of query tuning commandments**, as Mina would phrase them (e.g., “Thou shalt not sort 5M rows without an index”)  
> 10. End with a **handoff to Elijah in Cape Town**, who will take over Day 8 and dive into advanced query optimization, monitoring dashboards, and performance incident triage.
>
> **Tone:**  
> - Confident, direct, occasionally scolding  
> - Deeply technical, high clarity  
> - Speaks like someone who has fixed every bad query with her bare hands and a keyboard
