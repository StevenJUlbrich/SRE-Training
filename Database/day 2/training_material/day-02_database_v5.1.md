# 🚀 Day 2: Data Manipulation Language (DML) Module

## 📌 Introduction

Welcome to **Day 2** of our SRE Database Training! Yesterday, you explored relational database fundamentals, ensuring you have a solid foundation to understand how databases store and manage information. Today, we’ll build on that knowledge by focusing on **Data Manipulation Language (DML)**—the subset of SQL that adds, modifies, and removes data from database tables.

### Why DML Matters for Support and SRE

DML statements like **INSERT**, **UPDATE**, and **DELETE** are crucial for day-to-day support tasks. They allow you to correct, adjust, and remove data as part of troubleshooting. For SRE engineers, understanding DML at a deeper level helps ensure data consistency, reliability, and minimal downtime in production environments.

### What We’ll Cover

1. **Core DML Operations (INSERT, UPDATE, DELETE)**  
2. **Transaction Control (COMMIT, ROLLBACK, SAVEPOINT)**  
3. **Oracle-Specific DML Features (MERGE, error handling, returning values)**  
4. **Oracle Transaction Management**  
5. **DML Performance Monitoring and Troubleshooting**  
6. **Hands-On Exercises and Scenarios**  

Below is a simple visual concept map to illustrate how DML fits into the overall database lifecycle:

```asciitext
   +---------------+
   | Data Storage  |
   |  (Tables)     |
   +-------+-------+
           |
           |  DML
           v
   +---------------+
   | INSERT/UPDATE |
   |   /DELETE     |
   +-------+-------+
           |
           |Transaction
           | Control
           v
   +---------------+
   | Data Integrity|
   |   & Recovery  |
   +---------------+
```

Understanding these operations in Oracle environments is critical because most large-scale enterprise systems run on Oracle databases. Mastering Oracle-specific techniques and pitfalls can make the difference between a smooth support task and a major data outage.

---

## 🎯 Learning Objectives by Tier

Below are four **measurable** objectives at each tier—beginner (🟢), intermediate (🟡), and SRE-level (🔴)—with a focus on Oracle-specific DML skills.

### 🟢 Beginner Objectives

1. Identify the purpose and basic syntax of **INSERT**, **UPDATE**, and **DELETE** statements in Oracle.  
2. Execute simple **INSERT** statements on a single Oracle table with correct column mappings.  
3. Describe how **COMMIT** and **ROLLBACK** work to finalize or undo transactions.  
4. Recognize common DML-related error messages in Oracle and know where to look for solutions.

### 🟡 Intermediate Objectives

1. Perform **conditional UPDATE** and **DELETE** statements using **WHERE** clauses to target specific rows.  
2. Compare Oracle DML syntax to PostgreSQL and SQL Server using a side-by-side reference table.  
3. Implement **SAVEPOINT** for partial transaction rollbacks and understand how isolation levels affect concurrency.  
4. Use **MERGE** statements for multi-table synchronization with simple error handling.

### 🔴 SRE-Level Objectives

1. Diagnose transaction conflicts and lock contention using Oracle’s **V$** performance views.  
2. Recover from failed DML operations using **Flashback** features (Flashback Query, Transaction, or Table).  
3. Monitor and optimize bulk DML loads using **SQL*Loader** and external tables.  
4. Integrate advanced Oracle-specific DML logging and error capture strategies to ensure reliability at scale.

---

## 📚 Core Concepts

Each core concept below includes a beginner-friendly analogy, a visual representation, a technical explanation, real-world support relevance, system impact, common misconceptions, and a cross-dialect comparison.

### 1. Beginner Analogy

Think of **INSERT** as adding new items to your inventory, **UPDATE** as changing the details (price, quantity) of existing items, and **DELETE** as removing outdated items from your stock.

### 2. Visual Representation

```asciitext
   Table: INVENTORY
   +----------+---------+-----------+
   | ItemID   | Name    | Quantity  |
   +----------+---------+-----------+
   |    1     | Pencil  |    100    |
   |    2     | Pen     |    50     |
   +----------+---------+-----------+

    +--------------+--------------+
    |   INSERT     |   UPDATE     |
    +-------+------+-------+------+
            |              |
            v              v
    +--------------+--------------+
    |   New Row    |  Row Changed |
    +--------------+--------------+

   DELETE removes existing rows entirely.
```

### 3. Technical Explanation

- **INSERT** adds new rows to a table.  
- **UPDATE** modifies existing rows based on a condition.  
- **DELETE** removes rows based on a condition.  

### 4. Support/SRE Application

- Support engineers frequently insert or update configuration data.  
- During production incidents, you might need to delete incorrect test data introduced by a deployment.  
- SREs often script these DML operations in maintenance tasks to ensure the system’s health and performance.

### 5. System Impact

- **INSERT** can increase storage usage and potentially cause table fragmentation.  
- **UPDATE** can cause locking on the affected rows, potentially leading to concurrency issues.  
- **DELETE** can leave empty space in data blocks, affecting performance if not managed.  
- Proper **transaction control** (COMMIT/ROLLBACK) is essential for maintaining data integrity.

### 6. Common Misconceptions

- Believing **UPDATE** without a **WHERE** clause will only affect one row—actually, it can affect all rows.  
- Thinking **DELETE** immediately frees space—actual space reclamation depends on further maintenance (e.g., **VACUUM** in PostgreSQL or segment management in Oracle).  
- Forgetting to **COMMIT** in Oracle, leaving data changes visible only to the current session and eventually causing locks or rollback on exit.

### 7. SQL Dialect Comparison (Oracle, PostgreSQL, SQL Server)

| Operation | Oracle Example                 | PostgreSQL Example            | SQL Server Example            | Key Differences                                                           |
|-----------|-------------------------------|------------------------------|-------------------------------|---------------------------------------------------------------------------|
| INSERT    | `INSERT INTO table_name      | `INSERT INTO table_name      | `INSERT INTO table_name      | Oracle uses `INSERT ALL` for multi-row;                                   |
|           |  (col1, col2) VALUES         |  (col1, col2) VALUES         |  (col1, col2) VALUES         | PostgreSQL can use `RETURNING`;                                           |
|           |  (val1, val2);`              |  (val1, val2);`              |  (val1, val2);`              | SQL Server can use `OUTPUT` clause.                                       |
| UPDATE    | `UPDATE table_name           | `UPDATE table_name           | `UPDATE table_name           | Oracle often uses `MERGE` for multi-table updates;                        |
|           |  SET col1 = 'new'            |  SET col1 = 'new'            |  SET col1 = 'new'            | PostgreSQL & SQL Server syntax is similar.                                |
|           |  WHERE col2 = 'old';`        |  WHERE col2 = 'old';`        |  WHERE col2 = 'old';`        |                                                                           |
| DELETE    | `DELETE FROM table_name      | `DELETE FROM table_name      | `DELETE FROM table_name      | All support `WHERE` clauses;                                              |
|           |  WHERE col1 = 'val';`        |  WHERE col1 = 'val';`        |  WHERE col1 = 'val';`        | Oracle can also use `TRUNCATE TABLE` for faster deletion of all rows.     |

---

## 💻 Day 2 Concept Breakdown

### 1. INSERT Statement

**Beginner Explanation (🟢)**  

- **Analogy**: Adding new items to a shopping list.  
- **Syntax** (Oracle):

  ```sql
  INSERT INTO table_name (column1, column2)
  VALUES (value1, value2);
  ```

- **Example**:

  ```sql
  INSERT INTO employees (employee_id, first_name, last_name)
  VALUES (101, 'John', 'Doe');
  ```

**Intermediate Details (🟡)**  

- **Batch Inserts**: Multiple rows can be inserted using `INSERT ALL` or `INSERT FIRST` in Oracle.  
- **Dialect Differences**: PostgreSQL supports `RETURNING *`, SQL Server supports `OUTPUT`.  
- **System Impact**: Large batch inserts can lock entire segments or cause row-level locks, impacting concurrency.

**SRE-Level (🔴)**  

- **Bulk Loads**: Use **SQL*Loader** or external tables in Oracle for high-volume data insertion.  
- **Error Handling**: Combine `FORALL` with `SAVE EXCEPTIONS` in PL/SQL to capture row-level errors while continuing with the batch.  
- **Performance Monitoring**: Track I/O usage in Oracle’s **V$SYSSTAT** and **V$SESSION** views.

---

### 2. UPDATE Statement

**Beginner Explanation (🟢)**  

- **Analogy**: Changing the price tag on a product in a store.  
- **Syntax** (Oracle):

  ```sql
  UPDATE table_name
  SET column1 = value1
  WHERE condition;
  ```

- **Tip**: Always use a **WHERE** clause to avoid updating all rows unintentionally.

**Intermediate Details (🟡)**  

- **Conditional Updates**: Rely on subqueries or `CASE` expressions to update specific rows differently.  
- **Multi-table Updates**: Oracle typically uses `MERGE` to achieve this.  
- **System Impact**: Updating large numbers of rows can lead to row-level locks. Plan updates to avoid peak usage times.

**SRE-Level (🔴)**  

- **Lock Contention**: Investigate `V$LOCK`, `V$SESSION`, and `V$ACCESS` to identify blocking sessions.  
- **Performance Tuning**: Index usage is critical; poorly indexed columns in the **WHERE** clause can cause massive table scans.  
- **Rollback Segments**: Large updates can consume rollback space; SREs must monitor and manage rollback/undo segments.

---

### 3. DELETE Statement

**Beginner Explanation (🟢)**  

- **Analogy**: Removing expired items from a shelf.  
- **Syntax** (Oracle):

  ```sql
  DELETE FROM table_name
  WHERE condition;
  ```

- **Tip**: A missing **WHERE** clause removes all rows, which can be catastrophic.

**Intermediate Details (🟡)**  

- **TRUNCATE**: A DDL operation that quickly removes all rows from a table without generating undo logs (not the same as DELETE).  
- **Partitioned Deletes**: In large Oracle tables, partitioning data can speed up deletes.  
- **System Impact**: Deleting huge volumes of data can cause row-level locks and large undo usage.

**SRE-Level (🔴)**  

- **Bulk Deletions**: Scripting with small commits (batch deletes) can reduce rollback segment pressure.  
- **Logging**: Oracle’s DML error logging can track problematic rows in large delete operations.  
- **Recovery**: **Flashback Table** or **Flashback Query** can restore deleted rows if configured properly.

---

### 4. Transaction Control

**Beginner Explanation (🟢)**  

- **Analogy**: Making a purchase with a shopping cart. You only finalize (COMMIT) once you’re sure. If you change your mind, you ROLLBACK and put everything back.  
- **Syntax** (Oracle):

  ```sql
  COMMIT;
  ROLLBACK;
  SAVEPOINT savepoint_name;
  ROLLBACK TO savepoint_name;
  ```

- **Key Points**:
  - **COMMIT** makes changes permanent.  
  - **ROLLBACK** undoes all changes since the last COMMIT.  
  - **SAVEPOINT** sets a checkpoint you can roll back to without losing all changes.

**Intermediate Details (🟡)**  

- **Partial Rollbacks**: `SAVEPOINT` allows you to undo certain parts of a transaction.  
- **Isolation Levels**: **READ COMMITTED** is default in Oracle; others include **SERIALIZABLE**, **READ ONLY**.  
- **Support Scenario**: Use partial rollbacks when you need to confirm some statements were correct but revert others.

**SRE-Level (🔴)**  

- **Long-Running Transactions**: Can lead to significant lock contention and high undo space usage.  
- **Deadlock Handling**: Oracle usually detects deadlocks automatically; see **ORA-00060** error logs.  
- **Performance Metrics**: Monitor transaction states using **V$TRANSACTION**, **V$SESSION**, and **DBA_BLOCKERS**.

---

### 5. Oracle-Specific DML Features

**MERGE Statement**  

- **Purpose**: Combines **INSERT** and **UPDATE** in a single statement to synchronize data between tables.  
- **Syntax** (simplified):

  ```sql
  MERGE INTO target_table t
  USING source_table s
  ON (t.key = s.key)
  WHEN MATCHED THEN
    UPDATE SET ...
  WHEN NOT MATCHED THEN
    INSERT (...);
  ```

**Error Handling**  

- **DML Error Logging**: Use `LOG ERRORS` clause to capture problematic rows without halting the entire operation.

**Returning Values**  

- **RETURNING Clause**: Oracle lets you retrieve values directly from an insert/update/delete statement without a separate SELECT.

---

## 🔒 Transaction Management in Oracle

1. **ACID Properties**: Oracle adheres to atomicity, consistency, isolation, and durability.  
2. **Isolation Levels**: Default is **READ COMMITTED**, but **SERIALIZABLE** is available for stricter consistency.  
3. **Locking Behavior**: Oracle uses row-level locking, but even row locks can escalate if massive updates or queries are performed.  
4. **Best Practices**: Keep transactions short to minimize lock durations.  
5. **SRE Considerations**: Monitor for locked rows and potential deadlocks using Oracle views (**V$LOCK**, **DBA_BLOCKERS**).

---

## 🛠️ Oracle-Specific DML Tools and Techniques

1. **SQL*Loader for Bulk Data Loading**  
   - Ideal for large, one-time data imports.  
   - Use direct path loads for faster performance.

2. **External Tables**  
   - Treat external files as tables for reading or partial insertion.  
   - Great for periodic data ingestion.

3. **Flashback Technology**  
   - **Flashback Query** to view past data states.  
   - **Flashback Transaction** or **Table** to recover from erroneous DML.

4. **DML Error Logging**  
   - `LOG ERRORS INTO error_table` allows capturing and isolating rows that fail constraints or other validations.

---

## 🔍 Oracle DML Performance Monitoring

1. **Impact on Performance**  
   - Large DML operations can cause CPU, memory, and I/O spikes.  
   - Concurrency bottlenecks occur if multiple sessions update the same rows.

2. **V$ Views**  
   - **V$SESSION**: Check current sessions and locks.  
   - **V$SQL**: Identify top DML statements by CPU or I/O.  
   - **V$TRANSACTION**: Monitor active transactions, rollbacks, and undo usage.

3. **Lock Contention**  
   - Use **DBA_BLOCKERS** and **DBA_WAITERS** to see who is blocking whom.  
   - Implement an SRE approach by setting alerts for blocked sessions exceeding certain thresholds.

---

## 🔨 Hands-On Exercises

### 🟢 Beginner Exercises

1. **Simple INSERT**: Insert rows into a practice `employees` table.  
2. **Basic UPDATE**: Change an employee’s last name.  
3. **DELETE**: Remove a test employee record.

### 🟡 Intermediate Exercises

1. **Condition-Based UPDATE**: Increase salaries for employees in the “Sales” department by 10%.  
2. **MERGE**: Synchronize two small tables, `source_customers` and `target_customers`.  
3. **Partial Rollback**: Use **SAVEPOINT** to demonstrate rolling back only part of a transaction.

### 🔴 SRE-Level Exercises

1. **Bulk INSERT** using **SQL*Loader**. Measure the time taken and system resources consumed.  
2. **Lock Diagnosis**: Run concurrent updates on the same table and identify lock contention via **V$** views.  
3. **Flashback**: Delete rows, then use Flashback Table to recover them.

---

## 🚧 Troubleshooting Scenarios

Below are three realistic scenarios illustrating how to diagnose and resolve DML problems in Oracle.

1. **Stuck COMMIT**  
   - **Symptoms**: Session hangs on COMMIT.  
   - **Cause**: Another transaction holding locks.  
   - **Resolution**: Use **V$LOCK** to identify the blocker. Kill or roll back the blocking session if safe.

2. **Batch Update Failure**  
   - **Symptoms**: Large batch update fails halfway.  
   - **Cause**: Insufficient undo space.  
   - **Resolution**: Increase undo tablespace or commit in smaller batches. Use `DML ERROR LOGGING` to capture partial failures.

3. **Accidental Mass DELETE**  
   - **Symptoms**: All rows in a table are gone.  
   - **Cause**: Missing **WHERE** clause.  
   - **Resolution**: Roll back if still in the same session. Otherwise, use **Flashback Table** (if enabled) or restore from backup.

---

## ❓ Frequently Asked Questions

### 🟢 Beginner FAQs

1. **Why do I need COMMIT or ROLLBACK in Oracle?**  
   - Oracle requires explicit transaction control; changes are not automatically saved.
2. **Can I insert multiple rows in a single statement?**  
   - Yes, using `INSERT ALL` or multiple **VALUES** clauses in some dialects.
3. **Why can’t I see my changes in another session?**  
   - You must **COMMIT** for other sessions to see your changes in Oracle.

### 🟡 Intermediate FAQs

1. **How do I update a row in one table based on data in another table?**  
   - Use a `MERGE` statement or a subquery in the **WHERE** clause of **UPDATE**.
2. **What happens if my transaction remains uncommitted for too long?**  
   - You may block other sessions, consume undo space, and risk a system or session crash rolling back your work.
3. **How do I handle constraint errors while inserting data?**  
   - Use **DML error logging** (`LOG ERRORS`) to capture failed rows separately for review.

### 🔴 SRE-Level FAQs

1. **How do I detect and resolve deadlocks?**  
   - Oracle raises ORA-00060. Check trace files and the **V$LOCK** view. Usually, Oracle automatically chooses a victim to roll back.
2. **What is the best way to monitor DML performance in real-time?**  
   - Use **V$SESSION**, **V$SQL**, and **V$TRANSACTION** along with Oracle Enterprise Manager (OEM) or AWR reports.
3. **How can I recover from a mass delete where flashback was not enabled?**  
   - In the worst case, restore from RMAN backup if no flashback or valid rollback segments exist.

---

## 🔥 Oracle-Specific SRE Scenario

**Incident**: A critical reporting application experiences extreme slowness. Investigation shows that a weekly script is running a massive **MERGE** statement on the `orders` table.

1. **Diagnosis**  
   - Use **V$SESSION** and **V$LOCK** to see multiple blocked sessions waiting on row locks.  
   - The MERGE process is touching millions of rows, causing row-level locking.  

2. **Commands and Outputs**  

   ```sql
   SELECT sid, blocking_session, wait_class, event
   FROM v$session
   WHERE blocking_session IS NOT NULL;

   SELECT * FROM v$lock WHERE block = 1; -- identifies blocking locks
   ```

3. **Resolution**  
   - Pause the MERGE operation or break it into smaller batches (e.g., 100k rows at a time).  
   - Schedule the heavy MERGE during off-peak hours or implement partitioning to reduce the locking scope.  

4. **Broader SRE Principles**  
   - **Monitoring**: Proactive alerts for long-running sessions.  
   - **Observability**: Regular performance baselines to detect anomalies.  
   - **Reliability**: Batch or chunk large DML tasks to avoid single points of massive locking.

---

## 🧠 Key Takeaways

1. **Core DML Concepts**: Insert, update, and delete are fundamental building blocks of database operations.  
2. **Operational Insights**: Always plan DML changes carefully to avoid impacting performance.  
3. **Best Practices**:  
   - **Use WHERE Clauses** to scope changes.  
   - **Commit/Rollback** transactions promptly.  
   - **Leverage Tools** like SQL*Loader for bulk operations.  
4. **Oracle-Specific Cautions**:  
   - **Flashback** can be a lifesaver if configured properly.  
   - **MERGE** simplifies multi-table operations but can lock large chunks of data if not carefully used.

---

## 🚨 Career Protection Guide for DML Operations

1. **High-Risk DML Operations**  
   - Deleting large volumes of data.  
   - Updating production data without a backup or flashback plan.

2. **Recovery Strategies**  
   - **Flashback Query**: Retrieve historical data for minor corrections.  
   - **Flashback Table**: Revert entire tables to a previous state quickly.  
   - **RMAN Backup**: Last line of defense if all else fails.

3. **Verification Best Practices**  
   - Test queries on a **staging** or **development** environment.  
   - Use a small **SELECT** with the same WHERE clause to confirm target rows.  
   - Double-check row counts before finalizing.

4. **Safeguards**  
   - **SAVEPOINT** and partial rollbacks reduce risk.  
   - Implement triggers or foreign key constraints carefully.  
   - Maintain good documentation of all changes for auditing.

---

## 🔮 Preview of Next Day’s Content

On **Day 3**, we will shift focus to **Database Design Principles and Normalization**, exploring how to structure tables to optimize data quality and performance. Oracle-specific design considerations—such as partitioning strategies—will also be discussed to build on the DML knowledge acquired today.

---

This completes the Day 2 module on Data Manipulation Language (DML) in Oracle. By mastering these concepts, you’ll be equipped to handle most real-world data modification tasks confidently, while minimizing downtime and protecting your cven best practices.
