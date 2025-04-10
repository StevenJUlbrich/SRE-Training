Below is a set of 20 quiz questions following the instructions in day-7_8_quiz_questions.md . They are distributed into Days 7 and 8 topics, with the correct mix of difficulty levels, question types, and relevant database performance tuning and monitoring concepts. Each question is clearly labeled with difficulty, topic, and format.

---

# Day 7 (10 Questions)

## Question 1: [Index Types & Structures]  
🔍 Beginner | Multiple Choice  

Which statement best describes a **B-tree index** in most relational databases, including Oracle, PostgreSQL, and SQL Server?

A. A data structure that stores a bit for every possible value, making it ideal for low-cardinality columns  
B. A hierarchical structure with root, branch, and leaf nodes, where each node can contain multiple sorted keys  
C. A minimal index type used only for unique constraints, never for range queries  
D. A hashing structure that directly maps a key value to an approximate data location  

---

## Question 2: [Basic Query Plan Interpretation]  
🔍 Beginner | Multiple Choice  

When a query plan indicates a **“Full Table Scan”** on a large table, which of the following is most likely true?

A. The database has detected highly selective conditions and thus avoids using an index  
B. The database is reading every row in the table because no suitable index exists or the optimizer chose not to use one  
C. A unique index scan is being performed on the primary key for quick lookups  
D. The table is partitioned, and only one partition is scanned  

---

## Question 3: [EXPLAIN Plan Basics]  
🔍 Beginner | Multiple Choice  

In an **Oracle EXPLAIN PLAN** output, you see this line:

```
INDEX RANGE SCAN | employees_idx_name | cost=12 | cardinality=50
```

What does this indicate about how the database accesses the data?

A. It performs a full table scan on the employees table  
B. It uses a bitmap index to scan a low-cardinality column  
C. It scans only a subset of index entries based on a range condition  
D. It creates a temporary index just for this query and drops it afterward  

---

## Question 4: [Multi-Column Index Behavior]  
🔍 Beginner | True/False  

A multi-column (composite) index on `(last_name, first_name)` in a table will always be used by the optimizer for any query referencing just `first_name` in the WHERE clause.

A. True  
B. False  

---

## Question 5: [Cardinality Estimation]  
🔍 Beginner | True/False  

In most relational databases, **cardinality** refers to the estimated number of rows that a query or execution plan step will process.

A. True  
B. False  

---

## Question 6: [Statistics & Optimization]  
🔍 Beginner | Fill-in-the-Blank  

Complete the following statement regarding database optimizer statistics:

“Accurate ________ are crucial for generating efficient query execution plans, as they help the optimizer estimate table sizes and data distribution.”

A. Index Key Lengths  
B. System Privileges  
C. Data Dictionary Snapshots  
D. Table and Index Statistics  

---

## Question 7: [Index Maintenance Basics]  
🔍 Beginner | Multiple Choice  

Which of the following is generally recommended as part of **basic index maintenance** in an Oracle or PostgreSQL database?

A. Rebuilding all indexes every night, regardless of fragmentation levels  
B. Dropping and recreating every index on a weekly basis  
C. Monitoring index usage and selectively rebuilding or reorganizing only those that are heavily fragmented or unused  
D. Avoiding any form of index maintenance once the index is created  

---

## Question 8: [Composite Index Ordering]  
🧩 Intermediate | Multiple Choice (Day 7)  

You have a composite index on columns `(country, city)` for a table storing location data. Which of the following queries is **most likely** to benefit fully from that index?

A. `SELECT * FROM locations WHERE city = 'Paris'`  
B. `SELECT * FROM locations WHERE country = 'France'`  
C. `SELECT * FROM locations WHERE city = 'Paris' AND country = 'France'`  
D. `SELECT * FROM locations WHERE country LIKE '%Fra%'`  

---

## Question 9: [Index Implementation Detail]  
🧩 Intermediate | Multiple Choice (Day 7)  

You notice queries filtering on a function-based expression, `UPPER(email)`, in a PostgreSQL database. Which type of index could you consider to improve performance for these queries?

A. A unique constraint on the email column  
B. A standard B-tree index on `email` without any function usage  
C. A function-based or expression index on `UPPER(email)`  
D. A partial index that excludes all NULL emails  

---

## Question 10: [Execution Plan Terminology]  
🧩 Intermediate | Fill-in-the-Blank (Day 7)  

Complete the following statement:

“In many query optimizers, a ________ indicates a join method that uses an index on one table to look up matching rows for each row in the driving table.”

A. Materialized Lookup  
B. Nested Loop  
C. Parallel Hash  
D. Cost-Based Merge  

---

# Day 8 (10 Questions)

## Question 11: [Advanced Query Optimization]  
🧩 Intermediate | Multiple Choice  

When **rewriting subqueries** for better performance, which scenario often yields faster execution plans in Oracle or SQL Server?

A. Replacing an `EXISTS` subquery with a `COUNT(*)` subquery in the SELECT list  
B. Using correlated subqueries instead of joins whenever possible  
C. Converting correlated subqueries into standard join operations, reducing repeated lookups  
D. Wrapping every subquery in a view to isolate it from the main query  

---

## Question 12: [Database Configuration Parameters]  
🧩 Intermediate | Multiple Choice  

You are tuning a SQL Server instance with 64GB of RAM for heavy OLTP workloads. Which parameter or setting is most critical to **proper memory usage** for caching and buffering?

A. The `tempdb` file autogrowth setting  
B. The max server memory configuration for the SQL Server instance  
C. The maximum number of concurrent connections allowed  
D. The transaction isolation level  

---

## Question 13: [Performance Metrics & Monitoring]  
🧩 Intermediate | Matching  

Match each **performance metric** in Column A with its primary meaning or use in Column B.

Column A:  
1. CPU Utilization  
2. Buffer Cache Hit Ratio  
3. IOPS (Input/Output Operations per Second)  
4. Wait Events  

Column B:  
A. Determines how often the database is accessing data from memory versus disk  
B. Represents the rate at which the database engine performs read/write operations  
C. Provides insight into how much processing capacity is consumed by database tasks  
D. Indicates specific points in execution where sessions spend time waiting  

---

## Question 14: [Alert Thresholds]  
🧩 Intermediate | Fill-in-the-Blank  

Complete the following statement:

“To effectively monitor a production database, you should set an alert threshold on ________ to detect an abnormal rise that might indicate pending blocking or deadlocks.”

A. The Database Version Number  
B. Active Session Count  
C. Backup Completion Percentage  
D. SQL*Net Roundtrip Count  

---

## Question 15: [Optimizer Hints & Directives]  
💡 Advanced/SRE | Multiple Choice  

Which of the following is a potential **drawback** of relying heavily on **optimizer hints** in Oracle or PostgreSQL?

A. The database engine automatically adjusts hints to reflect changing data distributions  
B. Hints remain valid across major version upgrades and never cause plan regressions  
C. Hard-coded hints can lead to suboptimal plans if data or system conditions change over time  
D. Hinting is only supported in NoSQL databases, making it irrelevant in relational systems  

---

## Question 16: [Scalability & Partitioning]  
💡 Advanced/SRE | Multiple Choice  

In a large Oracle data warehouse, **table partitioning** can improve performance primarily by:

A. Converting all B-tree indexes into bitmap indexes  
B. Allowing queries to scan only relevant partitions instead of the entire table  
C. Preventing database statistics from ever becoming stale  
D. Disabling all write operations on non-active partitions  

---

## Question 17: [Connection Pooling & Resource Usage]  
💡 Advanced/SRE | True/False  

**Statement**: Configuring a connection pool to reuse database connections can significantly reduce overhead by avoiding repeated connection setups, which is especially beneficial under high-concurrency workloads.

A. True  
B. False  

---

## Question 18: [Maintenance Operations]  
💡 Advanced/SRE | Matching  

Match each **database maintenance operation** in Column A with its primary outcome in Column B.

Column A:  
1. Index Rebuild  
2. Statistics Update  
3. Table Partition Split  
4. Vacuum/Auto-Vacuum (PostgreSQL)  

Column B:  
A. Improves query planner accuracy by refreshing table metadata on row counts and data distribution  
B. Reclaims or repacks unused space and can help reduce bloat or fragmentation  
C. Physically reorganizes index pages to reduce fragmentation and optimize lookups  
D. Divides an existing partition into two smaller partitions for more fine-grained data management  

---

## Question 19: [Performance Issue Diagnosis Workflow]  
💡 Advanced/SRE | Ordering  

Arrange the following **troubleshooting steps** in the correct order to diagnose a sudden performance issue on a high-traffic database:

A. Identify the most resource-intensive queries or processes in the monitoring dashboard  
B. Review system logs and alert histories for recent changes or errors  
C. Generate or examine updated execution plans for the suspect queries  
D. Check if any database configuration parameters were recently modified  

---

## Question 20: [Scaling Strategies]  
💡 Advanced/SRE | Ordering  

Arrange these **database scaling actions** in the sequence that typically occurs as a system grows from smaller to larger scale:

A. Implement read replicas to offload reporting queries  
B. Deploy caching layers (e.g., Redis) for frequently accessed data  
C. Shard the data horizontally across multiple database instances  
D. Rely on a single primary database with basic indexing and standard configuration  

---

**End of Quiz**