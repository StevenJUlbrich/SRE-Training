# **Day 9 – SQL vs NoSQL Architecture Decisions**  Answer Sheet

**Comprehensive Answer Sheet**

---

## Answer 1: Database Paradigms Overview  
🔍 Beginner‑Level | Multiple Choice  

**Question:**  
Chloé compares SQL databases to a meticulously organized library and NoSQL databases to an eclectic bookstore. Which statement best summarizes this analogy?

A. SQL provides strict rules and structure, while NoSQL offers more flexibility but potential disorder.  
B. SQL is always faster than NoSQL because of its rigid approach.  
C. NoSQL systems are chaotic and inherently unscalable.  
D. SQL databases are obsolete due to the rise of NoSQL.  

**Correct Answer:** A  

**Explanation:**  
The “library vs. bookstore” analogy highlights that relational systems enforce a well‑defined catalog (tables, columns, keys), whereas NoSQL systems allow freer arrangement of “books” (documents, key‑value pairs, columns) that can evolve quickly. Flexibility brings agility but, without discipline, can drift into disorder.

**Why other options are incorrect:**  
- **B:** Speed depends on workload, indexing, and infrastructure—not purely on rigidity.  
- **C:** Well‑designed NoSQL systems (e.g., DynamoDB, Cassandra) scale predictably.  
- **D:** SQL remains dominant in countless mission‑critical applications.

**Database Comparison Note:**  
PostgreSQL, Oracle, and SQL Server exemplify the “library” model; MongoDB and Cassandra exemplify the “bookstore,” each optimized for different needs.

**Knowledge Connection:**  
Chloé opens Day 9 with this analogy to frame all later trade‑offs.

**SRE Perspective:**  
Knowing which model your workload maps to prevents operational surprises when scaling or changing schemas.

**Additional Insight:**  
Hybrid platforms (e.g., PostgreSQL + JSONB) can offer “library shelves” that also store “bookstore boxes,” blending both paradigms.

---

## Answer 2: SQL vs NoSQL Decision  
🔍 Beginner‑Level | Multiple Choice  

**Question:**  
According to Chloé, which factor is the most important when deciding whether to choose SQL or NoSQL?

A. Whether you like typed versus dynamic languages  
B. Your preference for code syntax  
C. Your data shape, consistency needs, scale requirements, and team skills  
D. The brand name or marketing popularity of the database  

**Correct Answer:** C  

**Explanation:**  
Chloé’s “Rules of Engagement” stress evaluating data shape (relational vs. flexible), consistency guarantees (ACID vs. eventual), scalability, and team expertise. These evidence‑based factors outweigh aesthetics or marketing.

**Why other options are incorrect:**  
- **A/B/D:** Personal preference and branding do not dictate operational success.

**Database Comparison Note:**  
Teams fluent in distributed systems may favor Cassandra for petabyte horizontal scale, whereas a financial team skilled in Oracle might keep ACID.

**Knowledge Connection:**  
The weighted‑scoring table later in the day operationalizes these factors.

**SRE Perspective:**  
Selecting a paradigm misaligned with scale or skill invites outages.

**Additional Insight:**  
Revisit the decision periodically—business requirements evolve.

---

## Answer 3: ACID vs BASE  
🔍 Beginner‑Level | True/False  

**Question:**  
Chloé mentions that ACID properties emphasize strong consistency and atomic transactions, whereas BASE properties focus on eventual consistency and high availability.

A. True  
B. False  

**Correct Answer:** True  

**Explanation:**  
ACID (Atomicity, Consistency, Isolation, Durability) ensures transactions behave as indivisible units. BASE (Basically Available, Soft‑state, Eventually consistent) relaxes immediate consistency for availability and partition tolerance.

**Database Comparison Note:**  
Oracle, PostgreSQL, and SQL Server are ACID; DynamoDB/Cassandra default to tunable BASE.

**Knowledge Connection:**  
This dichotomy underpins all later trade‑offs (banking vs. social feeds).

**SRE Perspective:**  
Misjudging the needed consistency level leads to data inaccuracies or unnecessary latency.

**Additional Insight:**  
Modern NoSQL platforms sometimes offer per‑operation consistency controls (e.g., DynamoDB “strongly consistent read”)—choose wisely.

---

## Answer 4: Schema‑on‑Write vs Schema‑on‑Read  
🔍 Beginner‑Level | Fill‑in‑the‑Blank  

**Question:**  
Under the ________ approach, changes to the data structure require a formal migration before being written, ensuring immediate consistency in the stored format.

A. schema‑on‑read  
B. schema‑on‑write  
C. no‑schema approach  
D. ephemeral schema  

**Correct Answer:** B – schema‑on‑write  

**Explanation:**  
Schema‑on‑write enforces structure at insertion time, guaranteeing each row/document fits the defined format. Relational databases embody this.

**Why other options are incorrect:**  
- **A:** Evaluates schema when reading, not at write.  
- **C/D:** Not formal approaches described by Chloé.

**Database Comparison Note:**  
PostgreSQL and Oracle require DDL migrations; MongoDB can store varying docs and impose schema at query or via validators.

**Knowledge Connection:**  
Chloé contrasts migration overhead (write) with agility (read).

**SRE Perspective:**  
Strict schemas reduce runtime surprises but increase deploy friction.

**Additional Insight:**  
Tools such as Liquibase or Flyway automate migrations, easing schema‑on‑write burdens.

---

## Answer 5: Basic NoSQL Category  
🔍 Beginner‑Level | Multiple Choice  

**Question:**  
Which NoSQL category stores JSON‑like structures that can nest data?

A. Key‑value store  
B. Document store  
C. Column‑family store  
D. Graph store  

**Correct Answer:** B  

**Explanation:**  
Document stores (e.g., MongoDB, Couchbase) persist hierarchical JSON/BSON docs, allowing embedded arrays/objects.

**Why other options are incorrect:**  
- **A:** Stores opaque values.  
- **C:** Stores sparse columns in wide rows.  
- **D:** Stores nodes and edges.

**Database Comparison Note:**  
Some relational DBs (PostgreSQL JSONB) emulate document patterns but still differ in indexing and query semantics.

**Knowledge Connection:**  
Chloé’s table of five models aligns JSON docs with document stores.

**SRE Perspective:**  
Deeply nested documents complicate indexing; monitor query patterns.

**Additional Insight:**  
Schema versioning inside documents (e.g., `_schemaVersion`) eases evolution.

---

## Answer 6: “Bad Polyglot Story” Context  
🔍 Beginner‑Level | True/False  

**Question:**  
Chloé’s cautionary tale describes cron‑script synchronization that produced data mismatches across SQL Server, Redis, and MongoDB.

A. True  
B. False  

**Correct Answer:** True  

**Explanation:**  
Manual ETL scripts lacked atomic guarantees, drifting replicas by six minutes or more—Chloé’s archetype of “what not to do.”

**Database Comparison Note:**  
Regardless of engines, ad‑hoc sync without idempotent events invites divergence.

**Knowledge Connection:**  
Leads into her advocacy for event buses like Kafka.

**SRE Perspective:**  
Cron‑based “dual‑write” pipelines cause silent data corruption—monitor lag and use CDC/event streaming instead.

**Additional Insight:**  
Always design for idempotency and replay if ingesting events.

---

## Answer 7: Data Model Analogy  
🔍 Beginner‑Level | Fill‑in‑the‑Blank  

**Question:**  
Chloé likens a key‑value store to a ________ for quick lookups.

A. recipe box  
B. dictionary  
C. random pile  
D. kiosk  

**Correct Answer:** B – dictionary  

**Explanation:**  
A dictionary provides O(1) lookups by key—mirroring key‑value DB access.

**Why other options are incorrect:**  
Other metaphors don’t capture direct key lookup semantics.

**Database Comparison Note:**  
Redis exemplifies “dictionary” access with in‑memory hashing.

**Knowledge Connection:**  
Chloé’s analogies steer mental models for performance expectations.

**SRE Perspective:**  
Knowing access patterns guides cache vs. persistent store choices.

**Additional Insight:**  
Key‑value stores trade relational querying for speed—ensure your workload matches.

---

## Answer 8: ACID vs BASE Trade‑offs  
🧩 Intermediate‑Level | Multiple Choice  

**Question:**  
Which scenario best fits a fully ACID‑compliant database?

A. Social network feeds  
B. Ephemeral event logs  
C. Banking transactions  
D. Gaming leaderboard  

**Correct Answer:** C  

**Explanation:**  
Monetary transfers need atomicity and isolation; eventual consistency risks misbalances.

**Why other options are incorrect:**  
A, B, and D tolerate slight delays or convergent consistency.

**Database Comparison Note:**  
Banks favor Oracle or PostgreSQL with strict isolation; BASE systems would need compensating logic.

**Knowledge Connection:**  
Chloé’s ACID “bank transfer” versus BASE “social post” examples.

**SRE Perspective:**  
Selecting BASE for finances leads to costly reconciliations.

**Additional Insight:**  
Even within ACID DBs, choose adequate isolation (e.g., SERIALIZABLE) for correctness.

---

## Answer 9: Schema Evolutions  
🧩 Intermediate‑Level | Multiple Choice  

**Question:**  
Which statement best captures schema‑on‑read?

A. Only for SQL  
B. Data is stored as‑is; structure applied during query  
C. Schema‑on‑write never needs migrations  
D. Schema‑on‑read freezes formats permanently  

**Correct Answer:** B  

**Explanation:**  
In schema‑on‑read systems (e.g., S3 + Athena, MongoDB), data may vary; readers impose structure when retrieving.

**Why other options are incorrect:**  
- **A:** Most common in NoSQL or lakehouses, not SQL.  
- **C:** Schema‑on‑write always needs migrations.  
- **D:** Data can evolve; readers adapt.

**Database Comparison Note:**  
Cassandra tables require some schema but are more flexible than RDBMS constraints.

**Knowledge Connection:**  
Chloé shows pros/cons of both approaches when data evolves rapidly.

**SRE Perspective:**  
Schema‑on‑read can mask “garbage in” until runtime—add data‑quality checks.

**Additional Insight:**  
Tools like Iceberg or Delta Lake add ACID layers to lakes, merging both worlds.

---

## Answer 10: Graph Database Scenario  
🧩 Intermediate‑Level | Multiple Choice  

**Question:**  
Graph DB best suits:

A. Time‑series metrics  
B. Social network relationships  
C. Session caching  
D. Sparse wide‑column data  

**Correct Answer:** B  

**Explanation:**  
Graph engines like Neo4j excel at traversing relationships (friends‑of‑friends, shortest paths).

**Why other options are incorrect:**  
Other workloads align with time‑series, key‑value, or column‑family stores.

**Database Comparison Note:**  
Relational recursive CTEs can emulate but scale poorly at large graph depth.

**Knowledge Connection:**  
Chloé stresses “choose the model that mirrors your queries.”

**SRE Perspective:**  
Graph queries can explode—monitor path length and query shapes.

**Additional Insight:**  
Indexes on node labels and relationship types are critical for performance.

---

## Answer 11: Migrations and Consistency  
🧩 Intermediate‑Level | Matching  

**Question:**  
Match items:

1. ACID – **A**  
2. BASE – **C**  
3. Schema‑on‑Write – **D**  
4. Schema‑on‑Read – **B**

**Explanation:**  
- ACID ensures atomic transactions.  
- BASE offers eventual consistency.  
- Schema‑on‑write enforces structure before insert.  
- Schema‑on‑read defers structure.

**Database Comparison Note:**  
Even NoSQL vendors add optional schema validators to mix models.

**Knowledge Connection:**  
These four pillars repeat across Chloé’s talk.

**SRE Perspective:**  
Understanding where each applies prevents mismatched expectations.

**Additional Insight:**  
Hybrid services may need both ACID (core) and BASE (edge cache).

---

## Answer 12: NoSQL Query Pitfalls  
🧩 Intermediate‑Level | Multiple Choice  

**Question:**  
Efficient NoSQL practice:

A. Cross‑collection joins  
B. Denormalize for direct lookups  
C. Full‑table scans  
D. No indexes  

**Correct Answer:** B  

**Explanation:**  
Denormalization aligns storage with access paths, avoiding heavy joins.

**Why other options are incorrect:**  
A/C/D negate NoSQL strengths, causing hot partitions or scans.

**Database Comparison Note:**  
In DynamoDB, single‑table designs or GSI help fetch by partition key.

**Knowledge Connection:**  
Chloé’s examples of `$lookup` and `scan()` fiascos.

**SRE Perspective:**  
Bad NoSQL patterns surface as CPU spikes and throttling.

**Additional Insight:**  
Maintain duplication discipline with version fields to track updates.

---

## Answer 13: Weighted Decision Framework  
🧩 Intermediate‑Level | True/False  

**Question:**  
Weighted scoring removes dogma.

A. True  
B. False  

**Correct Answer:** True  

**Explanation:**  
Scoring quantifies trade‑offs (transactions, scale, expertise) and surfaces a rational choice.

**Database Comparison Note:**  
Useful whether debating PostgreSQL vs. MongoDB or MySQL vs. DynamoDB.

**Knowledge Connection:**  
Chloé’s scoring table (SQL 76 % vs. NoSQL 58 %).

**SRE Perspective:**  
Evidence‑based selection reduces blame when scaling later.

**Additional Insight:**  
Review weights quarterly as requirements evolve.

---

## Answer 14: Polyglot Persistence Diagram  
🧩 Intermediate‑Level | Diagram‑Based  

**Question:**  
Diagram shows SQL DB and NoSQL DB publishing to an event bus.

**Correct Answer:** B  

**Explanation:**  
Events decouple producers (SQL, NoSQL) from consumers (analytics), ensuring reliable async integration—Chloé’s recommended pattern.

**Why other options are incorrect:**  
A: Disallowed cron scripts.  
C: Analytics engine consumes, not rewrites.  
D: Diagram shows NoSQL publishes too.

**Database Comparison Note:**  
Kafka, Pulsar, or AWS Kinesis are common buses.

**Knowledge Connection:**  
Addresses failure of “bad polyglot story” by using CDC/event streams.

**SRE Perspective:**  
Central bus provides observability (lag metrics) across systems.

**Additional Insight:**  
Use idempotent consumers to handle event replays.

---

## Answer 15: Team Skill Factor  
🧩 Intermediate‑Level | Fill‑in‑the‑Blank  

**Question:**  
Chloé emphasizes that a team’s ________ affects database success.

A. location | B. budget | **C. skill level** | D. syntax preference  

**Correct Answer:** C – skill level  

**Explanation:**  
A highly skilled Cassandra team might thrive where an Oracle‑only team struggles.

**Why other options are incorrect:**  
Budget and location matter but skills dictate operational excellence.

**Database Comparison Note:**  
Managed services (Atlas, DynamoDB) lower skill barriers but don’t erase them.

**Knowledge Connection:**  
Factor appears explicitly in her weighted table.

**SRE Perspective:**  
Skill gaps manifest as slow incident response and poor schema design.

**Additional Insight:**  
Invest in training before adopting an unfamiliar paradigm.

---

## Answer 16: Consistency and Reliability  
💡 Advanced‑Level | Multiple Choice  

**Question:**  
SRE fix for banking use case plagued by eventual consistency.

A. Stay BASE | B. Single server | **C. Switch to ACID/strong consistency** | D. Manual daily logs  

**Correct Answer:** C  

**Explanation:**  
Mission‑critical balances need immediate consistency. Either move to ACID DB or configure NoSQL for strong consistency.

**Why other options are incorrect:**  
A: Repeats error. B: Sacrifices availability/scale. D: Delayed reconciliation still wrong.

**Database Comparison Note:**  
DynamoDB offers strongly consistent reads; Cassandra can use QUORUM/LOCAL_QUORUM.

**Knowledge Connection:**  
Chloé’s banking vs. social feed examples.

**SRE Perspective:**  
Choosing the right consistency model prevents costly outages.

**Additional Insight:**  
Strong consistency often costs throughput—benchmark first.

---

## Answer 17: Multi‑Database Monitoring  
💡 Advanced‑Level | Multiple Choice  

**Question:**  
Best‑practice monitoring.

A blame | B isolated tools | **C centralized dashboard** | D no logs  

**Correct Answer:** C  

**Explanation:**  
Aggregating logs/metrics enables correlation (e.g., Oracle wait spikes vs. Mongo replication lag).

**Why other options are incorrect:**  
A/B/D hinder root‑cause analysis.

**Database Comparison Note:**  
Prometheus exporters for both DBs feed Grafana; ELK stack unifies logs.

**Knowledge Connection:**  
Chloé insists on unified visibility to avoid “blind spots.”

**SRE Perspective:**  
Cross‑system alerts cut MTTR in polyglot stacks.

**Additional Insight:**  
Include event‑bus lag metrics alongside DB metrics.

---

## Answer 18: Polyglot Consistency Incident  
💡 Advanced‑Level | Diagram‑Based  

**Question:**  
Sequence diagram analysis.

**Correct Answer:** B  

**Explanation:**  
Oracle committed successfully; NoSQL lagged. Fix lies in speeding replication/consumer throughput.

**Why other options are incorrect:**  
A/C/D contradict evidence: Oracle shows success; remedy is pipeline, not rollback.

**Database Comparison Note:**  
Common to any CDC pipeline—monitor consumer offsets.

**Knowledge Connection:**  
Mirrors her incident checklist: validate logs → inspect event bus → resolve lag.

**SRE Perspective:**  
Event lag dashboards pre‑empt such incidents.

**Additional Insight:**  
Apply back‑pressure alerts when lag exceeds SLA.

---

## Answer 19: Steps to Decide SQL vs NoSQL  
💡 Advanced‑Level | Ordering  

**Question:**  
Order: **B, A, C, D**

1. Identify requirements (B)  
2. Build weighted table (A)  
3. Compare fit (C)  
4. Choose or polyglot (D)

**Explanation:**  
Requirements drive weighted criteria; scoring surfaces best fit; comparison informs final decision.

**Database Comparison Note:**  
Process‑agnostic; repeat for each project.

**Knowledge Connection:**  
Directly mirrors Chloé’s decision framework flowchart.

**SRE Perspective:**  
Documented rationale aids future audits or migrations.

**Additional Insight:**  
Keep historical decision logs; revisit when scale or requirements shift.

---

## Answer 20: Troubleshooting Cross‑Database Incidents  
💡 Advanced‑Level | Ordering  

**Question:**  
Order: **A, B, C, D**

1. Check DB logs/events (A)  
2. Observe backlog vs. deeper mismatch (B)  
3. Validate event bus/bridge (C)  
4. Fix, retest, document (D)

**Explanation:**  
Start with facts (logs), determine scope (backlog or corruption), inspect integration layer, then remediate and document.

**Database Comparison Note:**  
Applies to any event‑driven polyglot architecture.

**Knowledge Connection:**  
Parallels Chloé’s incident sequence diagram and run‑book steps.

**SRE Perspective:**  
Systematic triage avoids knee‑jerk fixes that mask root cause.

**Additional Insight:**  
Post‑incident reviews update run‑books and alert thresholds to catch similar issues earlier.

---

**End of Day 9 Answer Sheet**