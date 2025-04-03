# Day 2 DML Quiz Answer Sheet

Below is a comprehensive answer sheet for the Day 2 quiz questions focusing on Data Manipulation Language (DML) with Oracle as the primary focus. Each answer includes explanations, Oracle-specific details, SRE insights, and additional tips to reinforce the concepts learned. citeturn2file0 citeturn2file1

---

## Answer 1: INSERT Basics

🟢 Beginner | Multiple Choice

**Question:** Which statement best describes the primary use of the INSERT command in Oracle?

A. To delete unwanted rows from a table  
B. To modify data in existing rows of a table  
C. To add new rows of data into a table  
D. To apply transaction control after a commit

**Correct Answer:** C

**Explanation:**  
The INSERT command is designed to add new rows into an existing table in Oracle. This operation is fundamental to expanding the dataset, often used when bringing in new records such as customer orders or employee information. It does not modify or remove existing rows; rather, it appends new data. Oracle enforces integrity constraints (like NOT NULL and foreign key constraints) at insert time. Ensuring each column aligns with the defined schema is essential.

**Why other options are incorrect:**  

- Option A (Delete unwanted rows) describes the DELETE command, not INSERT.  
- Option B (Modify data) is performed by the UPDATE command.  
- Option D (Transaction control) typically involves COMMIT or ROLLBACK, not INSERT.

**Oracle Comparison Note:**  
In PostgreSQL and SQL Server, INSERT also adds new rows, though each has slight variations in syntax (e.g., INSERT INTO ... VALUES vs. using RETURNING/OUTPUT for capturing inserted rows).

**Knowledge Connection:**  
Links to Day 2’s discussion on core DML operations, specifically the importance of structured data entry.

**SRE Perspective:**  
Large INSERT operations can affect performance and concurrency if performed during peak load. Plan batch inserts carefully.

**Additional Insight:**  
Always validate data before inserting to avoid integrity constraint errors, which can cause transaction rollbacks or partial failures.

---

## Answer 2: Data Dictionary Views

🟢 Beginner | True/False

**Question:** True/False: The Oracle data dictionary views (e.g., V$SESSION, V$LOCK) can be used to monitor DML operations and identify which sessions hold specific locks.

A. True  
B. False

**Correct Answer:** True (A)

**Explanation:**  
Oracle’s data dictionary views, especially V$SESSION and V$LOCK, give detailed insight into current connections, locking states, and the sessions holding or waiting on locks. This is crucial for diagnosing blocking sessions and long-running DML statements. By correlating session information with lock data, DBAs and SREs can quickly identify performance bottlenecks.

**Oracle Comparison Note:**  
PostgreSQL and SQL Server have analogous views (e.g., pg_stat_activity in PostgreSQL and sys.dm_tran_locks in SQL Server) to monitor sessions and lock states.

**Knowledge Connection:**  
Day 2 covers Oracle-specific performance monitoring; V$SESSION and V$LOCK are integral to diagnosing locking issues.

**SRE Perspective:**  
Monitoring locks is vital for system reliability—blocked transactions can degrade user experience and cause cascading failures.

**Additional Insight:**  
Regularly querying these views or setting automated alerts helps detect lock contention before it impacts production.

---

## Answer 3: Truncate vs. Delete

🟢 Beginner | Fill-in-the-Blank

**Question:** "A TRUNCATE operation in Oracle is considered a ________ statement, whereas a DELETE operation is a DML statement."

A. Constraint  
B. DDL  
C. COMMIT  
D. Index

**Correct Answer:** B – DDL

**Explanation:**  
TRUNCATE is a Data Definition Language (DDL) statement because it deallocates data space and resets the table’s high-water mark in Oracle. This means the operation is more akin to structural changes (like dropping and re-creating the table) than to row-by-row manipulations that define DML. DELETE, conversely, removes rows but does not free the allocated table space.

**Why other options are incorrect:**  

- Option A (Constraint) is not the correct category.  
- Option C (COMMIT) is a transaction control statement, not a type of SQL command.  
- Option D (Index) is also a structure, but not relevant to the statement classification.

**Oracle Comparison Note:**  
PostgreSQL and SQL Server also treat TRUNCATE as DDL or a special category that can’t be easily rolled back.

**Knowledge Connection:**  
This directly ties to the Day 2 concept distinguishing DML vs. DDL operations and how Oracle handles table space.

**SRE Perspective:**  
TRUNCATE is faster and uses fewer resources than DELETE for clearing an entire table but can have irreversible effects, impacting reliability if not carefully done.

**Additional Insight:**  
Always confirm you truly want to remove all rows. TRUNCATE can’t be rolled back once executed (unless it’s in a transactional wrapper in certain special circumstances), making it a high-risk operation.

---

## Answer 4: Transaction Control

🟢 Beginner | Multiple Choice

**Question:** Which of the following commands in Oracle makes all changes since the last COMMIT statement permanent?

A. SAVEPOINT  
B. ROLLBACK  
C. MERGE  
D. COMMIT

**Correct Answer:** D

**Explanation:**  
A COMMIT in Oracle finalizes all changes made in the current transaction, making them visible to other sessions. Until COMMIT is issued, modifications stay local to the transaction, allowing rollback or further modifications. COMMIT is integral to ensuring data persistence.

**Why other options are incorrect:**  

- Option A (SAVEPOINT) sets a partial transaction marker, not a final confirmation.  
- Option B (ROLLBACK) undoes changes since the last COMMIT.  
- Option C (MERGE) is a DML operation that can do inserts/updates based on a join, unrelated to transaction finalization.

**Oracle Comparison Note:**  
PostgreSQL and SQL Server also use COMMIT for finalizing changes, but the default transaction behavior might differ (e.g., autocommit in certain configurations).

**Knowledge Connection:**  
Day 2 covers transaction control statements (COMMIT, ROLLBACK, SAVEPOINT) extensively.

**SRE Perspective:**  
Excessive uncommitted transactions can lead to high undo/rollback usage and potential performance or locking issues.

**Additional Insight:**  
Frequent small commits reduce the risk of large rollbacks but can also fragment data if overused.

---

## Answer 5: Impact of a Missing WHERE Clause

🟢 Beginner | Multiple Choice

**Question:** What happens if you issue an UPDATE statement in Oracle without a WHERE clause?

A. Only rows inserted in the last transaction are updated  
B. Only rows in the current session are updated  
C. All rows in the table are updated  
D. The statement fails with an error

**Correct Answer:** C

**Explanation:**  
In Oracle, omitting the WHERE clause on an UPDATE statement applies the update to every row in the table, because no condition restricts which rows should be modified. This often leads to significant data corruption if done unintentionally.

**Why other options are incorrect:**  

- Option A (Only rows inserted in the last transaction) is not how Oracle restricts updates.  
- Option B (Only rows in the current session) is incorrect—Oracle does not differentiate rows by sessions in this manner.  
- Option D (Fails with an error) is incorrect as Oracle will successfully run the UPDATE.

**Oracle Comparison Note:**  
Same behavior occurs in PostgreSQL and SQL Server; the absence of a WHERE clause updates all rows.

**Knowledge Connection:**  
Reinforces the Day 2 emphasis on carefully scoping DML statements.

**SRE Perspective:**  
Always test or confirm your WHERE clause in a non-production environment to avoid mass data corruption.

**Additional Insight:**  
Use a SELECT with the same WHERE criteria to verify you’re targeting the intended rows before issuing the UPDATE.

---

## Answer 6: Oracle Locking

🟢 Beginner | True/False

**Question:** When you run an UPDATE statement in Oracle, the database acquires row-level locks on the rows being updated.

A. True  
B. False

**Correct Answer:** True (A)

**Explanation:**  
Oracle uses row-level locking for DML statements like UPDATE. This means only the specific rows being updated are locked, which improves concurrency by avoiding table-level locks. Once the transaction is committed or rolled back, these locks are released.

**Oracle Comparison Note:**  
PostgreSQL also uses row-level locking, while SQL Server has several locking granularities but often defaults to row locks.

**Knowledge Connection:**  
This question references Day 2’s transaction control and concurrency section.

**SRE Perspective:**  
Row-level locks help with high concurrency but can still cause performance issues if large numbers of rows are locked for a prolonged period.

**Additional Insight:**  
Monitoring lock contention is essential in high-transaction environments to avoid system-wide performance degradation.

---

## Answer 7: Basic DELETE Statement

🟢 Beginner | Ordering

**Question:** Arrange the following steps in the correct order to perform a basic DELETE in Oracle:

A. Confirm the correct rows are targeted by SELECT  
B. Issue the DELETE statement  
C. COMMIT the transaction  
D. Check the number of rows affected

**Correct Order:** A → B → D → C

**Explanation:**  
You first confirm the rows you intend to delete (A) by using a SELECT. Then you execute the actual DELETE statement (B). Next, verify how many rows were affected (D) to ensure it matches expectations. Finally, COMMIT (C) to make the deletion permanent.

**Oracle Comparison Note:**  
All major RDBMS systems (PostgreSQL, SQL Server) follow a similar process for transactional deletes, though autocommit settings can change some steps.

**Knowledge Connection:**  
Directly relates to Day 2’s DML fundamentals and transaction control, underscoring best practices.

**SRE Perspective:**  
Confirming row counts can prevent accidental mass deletions. Proper transaction control ensures data consistency.

**Additional Insight:**  
Always keep an eye on your WHERE clause and row counts before committing.

---

## Answer 8: INSERT ALL

🟡 Intermediate | Multiple Choice

**Question:** Which Oracle-specific feature allows inserting multiple rows into a table using a single SQL statement?

A. INSERT ALL  
B. MERGE  
C. Multi-table UPDATE  
D. TRUNCATE

**Correct Answer:** A

**Explanation:**  
INSERT ALL lets you add multiple rows in a single statement, which can be more efficient than issuing multiple separate INSERT statements. This feature improves performance for bulk inserts in certain scenarios, especially when dealing with varied sets of data.

**Why other options are incorrect:**  

- Option B (MERGE) is for conditional updates/inserts based on matching join conditions.  
- Option C (Multi-table UPDATE) is not a standard Oracle feature name; Oracle typically uses MERGE for multi-table logic.  
- Option D (TRUNCATE) is a DDL command for removing all rows from a table.

**Oracle Comparison Note:**  
PostgreSQL can perform multi-row inserts with the VALUES syntax, while SQL Server can use the VALUES clause or table-valued parameters.

**Knowledge Connection:**  
Day 2 includes advanced Oracle-specific DML features like INSERT ALL.

**SRE Perspective:**  
In high-throughput systems, minimizing statement overhead by using INSERT ALL can improve performance.

**Additional Insight:**  
When rows have varying column sets, consider using conditional clauses within INSERT ALL.

---

## Answer 9: Conditional Update

🟡 Intermediate | True/False

**Question:** Including a WHERE clause in an UPDATE statement will allow you to conditionally modify only specific rows in Oracle.

A. True  
B. False

**Correct Answer:** True (A)

**Explanation:**  
The WHERE clause in an UPDATE statement is used to specify which rows to modify. Without it, Oracle applies the update to all rows. By carefully crafting the condition in the WHERE clause, you can target exactly the rows that need changing.

**Oracle Comparison Note:**  
Same behavior in PostgreSQL and SQL Server; the WHERE clause is crucial for scoping updates.

**Knowledge Connection:**  
Builds on Day 2’s focus on preventing unintentional data modifications.

**SRE Perspective:**  
Conditionally updating data helps maintain data integrity and reduces locking overhead by touching fewer rows.

**Additional Insight:**  
Always double-check the WHERE condition with a SELECT before executing the UPDATE.

---

## Answer 10: SAVEPOINT Usage

🟡 Intermediate | Fill-in-the-Blank

**Question:** "A ________ allows you to rollback a portion of a transaction in Oracle without affecting all previously executed statements."

A. COMMIT  
B. SAVEPOINT  
C. FOREIGN KEY  
D. FLASHBACK

**Correct Answer:** B – SAVEPOINT

**Explanation:**  
SAVEPOINT creates a marker within a transaction so you can roll back only to that point if something goes wrong, rather than undoing the entire transaction. This allows more granular control over transactional changes, useful for complex operations.

**Why other options are incorrect:**  

- Option A (COMMIT) finalizes all changes.  
- Option C (FOREIGN KEY) is a constraint, not related to partial rollbacks.  
- Option D (FLASHBACK) is a separate Oracle feature for viewing/reverting data states.

**Oracle Comparison Note:**  
PostgreSQL and SQL Server also have savepoint functionality, though syntax might slightly differ.

**Knowledge Connection:**  
Relates to Oracle’s transaction control statements (COMMIT, ROLLBACK, SAVEPOINT) discussed on Day 2.

**SRE Perspective:**  
SAVEPOINT can be critical for large scripts where partial success is acceptable.

**Additional Insight:**  
Naming SAVEPOINTs is a best practice for clarity when rolling back.

---

## Answer 11: MERGE Statement

🟡 Intermediate | Multiple Choice

**Question:** Which of the following best describes the function of the Oracle MERGE statement?

A. It creates a new table based on an existing query  
B. It terminates multiple blocking sessions at once  
C. It synchronizes data between two tables, combining INSERT and UPDATE operations  
D. It performs a transaction rollback if more than one table is updated

**Correct Answer:** C

**Explanation:**  
The MERGE statement in Oracle is used for "upserts." It checks whether rows in a source table match rows in a target table based on a join condition. If matched, the MERGE can update existing rows; if not matched, it can insert new rows. This capability is highly valuable in data warehousing or synchronization tasks.

**Why other options are incorrect:**  

- Option A references CREATE TABLE AS SELECT, not MERGE.  
- Option B is about session termination, which is an administrative task, not a DML function.  
- Option D references transaction rollback, which is handled by ROLLBACK, not MERGE.

**Oracle Comparison Note:**  
SQL Server has a MERGE statement with slightly different syntax and caution around concurrency. PostgreSQL requires a combination of INSERT ... ON CONFLICT or multiple statements.

**Knowledge Connection:**  
Day 2 advanced DML features highlight MERGE for multi-table synchronization.

**SRE Perspective:**  
MERGE can reduce overhead by combining multiple DML steps into one. However, it can escalate locks if not carefully managed.

**Additional Insight:**  
Always specify clear join conditions to avoid unintentional merges.

---

## Answer 12: Monitoring Blocking Sessions

🟡 Intermediate | Multiple Choice

**Question:** Which Oracle view would you query to find sessions that are currently blocking others during a DML operation?

A. DBA_OBJECTS  
B. V$SQL  
C. V$LOCK  
D. USER_INDEXES

**Correct Answer:** C

**Explanation:**  
V$LOCK contains information about the locks held by sessions in Oracle, allowing you to see which sessions are blocking others. By joining V$LOCK with V$SESSION, DBAs or SREs can pinpoint which SID or serial# is causing the bottleneck.

**Why other options are incorrect:**  

- Option A (DBA_OBJECTS) lists database objects, not locks.  
- Option B (V$SQL) shows SQL statements in the library cache, not the locking state.  
- Option D (USER_INDEXES) lists indexes owned by the current user, unrelated to active locks.

**Oracle Comparison Note:**  
PostgreSQL uses pg_locks, while SQL Server provides sys.dm_tran_locks.

**Knowledge Connection:**  
Day 2’s coverage of performance monitoring and troubleshooting underscores using Oracle’s dynamic performance views.

**SRE Perspective:**  
Blocking sessions can degrade performance or cause timeouts. Proactive monitoring is essential.

**Additional Insight:**  
Combine V$LOCK data with V$SESSION for comprehensive blocking session diagnostics.

---

## Answer 13: DML Error Logging

🟡 Intermediate | Matching

**Question:** Match each item in Column A with the appropriate description in Column B.

**Column A:**  

1. LOG ERRORS  
2. DBMS_OUTPUT  
3. ROLLBACK  
4. COMMIT  

**Column B:**  
A. Displays messages during PL/SQL execution  
B. Records problematic rows without stopping the entire DML operation  
C. Makes all changes since the last transaction statement permanent  
D. Reverts all changes in the current transaction since the last COMMIT

**Correct Matches:**  
1 → B  
2 → A  
3 → D  
4 → C

**Explanation:**  

- LOG ERRORS (1) is used in Oracle to capture error rows during bulk operations, preventing the entire statement from failing.  
- DBMS_OUTPUT (2) provides a built-in package for printing messages in PL/SQL.  
- ROLLBACK (3) undoes all changes since the last COMMIT.  
- COMMIT (4) finalizes all changes.

**Oracle Comparison Note:**  
Not all RDBMS have a direct equivalent of LOG ERRORS. PostgreSQL and SQL Server typically require error-handling logic or advanced features like try/catch blocks.

**Knowledge Connection:**  
Relates to Oracle-specific DML error handling and transaction control from Day 2.

**SRE Perspective:**  
LOG ERRORS is particularly important in large ETL or continuous integration pipelines to isolate invalid rows.

**Additional Insight:**  
Review the error logging table after bulk operations to fix or reprocess problematic data.

---

## Answer 14: Isolation Levels

🟡 Intermediate | Ordering

**Question:** Arrange the following Oracle isolation levels in increasing order of strictness:

A. SERIALIZABLE  
B. READ COMMITTED  
C. READ ONLY  
D. READ UNCOMMITTED (Not fully supported by Oracle, but included for comparison)

**Correct Order:** D → B → C → A

**Explanation:**  

- **READ UNCOMMITTED (D)** is the least strict; Oracle does not fully implement it but includes it conceptually.  
- **READ COMMITTED (B)** is Oracle’s default, allowing non-repeatable reads.  
- **READ ONLY (C)** disallows modifications, further increasing consistency for queries.  
- **SERIALIZABLE (A)** is the strictest, preventing phenomena like phantom reads.

**Oracle Comparison Note:**  
SQL Server and PostgreSQL support a variety of isolation levels but may differ in naming and behaviors (e.g., PostgreSQL’s REPEATABLE READ vs. Oracle’s SERIALIZABLE).

**Knowledge Connection:**  
Important for understanding concurrency and transaction behavior in Day 2.

**SRE Perspective:**  
Higher isolation levels can reduce concurrency and slow performance; SREs often balance consistency needs with performance.

**Additional Insight:**  
Use consistent isolation levels to avoid unexpected anomalies in production.

---

## Answer 15: Bulk Data Loading

🔴 SRE-Level | Multiple Choice

**Question:** Which tool is best suited for high-volume data insertion into Oracle databases?

A. Data Pump Export  
B. Data Pump Import  
C. SQL*Loader  
D. RMAN

**Correct Answer:** C

**Explanation:**  
SQL*Loader is specifically designed for efficiently loading large volumes of external data into Oracle tables. It can handle a variety of file formats, perform direct-path loads for faster throughput, and apply constraints selectively, which is key in many enterprise ETL scenarios.

**Why other options are incorrect:**  

- Option A (Data Pump Export) extracts data from Oracle to external files.  
- Option B (Data Pump Import) imports data dumps, not general external CSV or text files.  
- Option D (RMAN) is for backup and recovery of Oracle databases.

**Oracle Comparison Note:**  
In PostgreSQL, a comparable tool is COPY; in SQL Server, bcp (bulk copy) is used.

**Knowledge Connection:**  
Day 2’s coverage of bulk loading and Oracle-specific DML tools includes SQL*Loader.

**SRE Perspective:**  
Efficient bulk data loading is crucial for reliability, as it shortens downtime during major data imports.

**Additional Insight:**  
Use direct path load mode whenever feasible for substantial performance gains.

---

## Answer 16: Undo Space Management

🔴 SRE-Level | Multiple Choice

**Question:** Which of the following statements about Oracle undo space is correct?

A. Undo segments are used only for read consistency and never for rollback  
B. Large DML operations can exhaust undo space, leading to "snapshot too old" errors  
C. Oracle databases do not require undo segments if using COMMIT frequently  
D. Undo space is only consumed by DDL operations, not DML operations

**Correct Answer:** B

**Explanation:**  
Undo segments store before images of data, providing both read consistency (for queries) and the ability to roll back changes if necessary. Large transactions can fill these segments, triggering "snapshot too old" errors if the undo data is overwritten before a query completes.

**Why other options are incorrect:**  

- Option A is incorrect because undo segments are also critical for rolling back data.  
- Option C is incorrect; Oracle always requires undo segments.  
- Option D is incorrect; DML consumes undo space, not just DDL.

**Oracle Comparison Note:**  
PostgreSQL uses Multi-Version Concurrency Control (MVCC), storing row versions differently. SQL Server uses tempdb for similar functionality in certain isolation levels.

**Knowledge Connection:**  
Relates to Oracle’s transaction and undo management, covered extensively in Day 2 for concurrency and performance.

**SRE Perspective:**  
Monitoring undo space is essential to avoid errors that disrupt critical operations.

**Additional Insight:**  
Size undo tablespace properly and consider committing in batches for massive DML tasks.

---

## Answer 17: Deadlock Detection

🔴 SRE-Level | True/False

**Question:** Oracle automatically detects and resolves deadlocks by rolling back one of the conflicting transactions.

A. True  
B. False

**Correct Answer:** True (A)

**Explanation:**  
Oracle’s deadlock detection mechanism identifies mutually conflicting locks and automatically chooses one "victim" transaction to roll back, thus breaking the deadlock. This prevents a permanent freeze of processes.

**Oracle Comparison Note:**  
SQL Server and PostgreSQL have similar automatic deadlock resolution strategies.

**Knowledge Connection:**  
Builds on Day 2’s discussion of concurrency control and transaction locking.

**SRE Perspective:**  
Deadlocks can hamper reliability. Monitoring deadlock frequency helps SREs diagnose poorly designed queries or data access patterns.

**Additional Insight:**  
Examine trace files or system logs after deadlocks to identify and optimize queries.

---

## Answer 18: Flashback Query

🔴 SRE-Level | Matching

**Question:** Match each flashback technology to its primary purpose:

**Column A:**  

1. Flashback Query  
2. Flashback Transaction  
3. Flashback Table  
4. Flashback Database

**Column B:**  
A. Revert an entire table to a previous point in time  
B. Allows viewing data as it existed at a specific time without reverting changes  
C. Rolls back an entire database to a previous point in time  
D. Reverses the effects of a specific transaction

**Correct Matches:**  
1 → B  
2 → D  
3 → A  
4 → C

**Explanation:**  

- Flashback Query (1) provides a historical view of data without changing current data.  
- Flashback Transaction (2) replays or reverses a given transaction’s changes.  
- Flashback Table (3) rewinds a table’s data to a prior state.  
- Flashback Database (4) rewinds the entire database.

**Oracle Comparison Note:**  
These features are unique to Oracle’s Flashback technology. PostgreSQL offers point-in-time recovery, but not as many granular flashback features.

**Knowledge Connection:**  
Day 2 covers Oracle-specific recovery methods, showing how Flashback reduces downtime.

**SRE Perspective:**  
Flashback can mitigate data loss after accidental deletions or incorrect mass updates.

**Additional Insight:**  
Ensure sufficient undo/flashback logs are configured to utilize these features effectively.

---

## Answer 19: Lock Contention Troubleshooting

🔴 SRE-Level | Fill-in-the-Blank

**Question:** "To identify the sessions that are blocking others in Oracle, you would typically query __________."

A. V$LOCK  
B. DICTIONARY  
C. DBA_SEGMENTS  
D. USER_TRIGGERS

**Correct Answer:** A – V$LOCK

**Explanation:**  
V$LOCK displays information about the locks within Oracle, including which session holds a lock, the lock mode, and which session is waiting. This is essential in diagnosing blocking scenarios and resolving contention.

**Why other options are incorrect:**  

- B (DICTIONARY) lists available dictionary views, not lock states.  
- C (DBA_SEGMENTS) gives storage details on segments, unrelated to locking.  
- D (USER_TRIGGERS) lists triggers, also unrelated to blocking sessions.

**Oracle Comparison Note:**  
PostgreSQL uses pg_locks; SQL Server uses sys.dm_tran_locks.

**Knowledge Connection:**  
Relates to Day 2 discussion on performance monitoring for DML.

**SRE Perspective:**  
Proper lock contention analysis ensures high availability and reliability in production.

**Additional Insight:**  
Join V$LOCK with V$SESSION and V$PROCESS to get the session username, host, and other vital info for faster resolution.

---

## Answer 20: Advanced Transaction Flow

🔴 SRE-Level | Ordering

**Question:** Order the following steps to process and recover from an erroneous DML transaction in an SRE scenario:

A. Use Flashback Query/Transaction to view or revert changes  
B. Investigate DML performance impact with V$SESSION and V$SQL  
C. Identify blocking locks and potential deadlocks  
D. Run large batch UPDATE on a high-traffic table

**Correct Order:** D → C → B → A

**Explanation:**  
You start by running a large batch UPDATE (D) on a busy table, which can trigger blocking sessions or performance issues. Next, you identify locks and deadlocks (C). Then, you investigate performance and potential bottlenecks (B) using V$SESSION and V$SQL. Finally, if the transaction caused undesirable changes or data corruption, use Flashback features (A) to revert.

**Oracle Comparison Note:**  
Equivalent steps exist in other databases, but Oracle’s Flashback is more robust for data restoration.

**Knowledge Connection:**  
Illustrates an advanced real-world SRE scenario combining DML, locks, and Flashback.

**SRE Perspective:**  
Highlights the interplay between concurrency (locks), monitoring (V$ views), and reliability (Flashback for recovery).

**Additional Insight:**  
Always test large DML operations in a lower environment and set up alerts for lock contention and slow queries.

---

End of Day 2 DML Quiz Answer Sheet
