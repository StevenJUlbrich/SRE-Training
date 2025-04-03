# Day 2 of the SRE Database Training Module

## Question 1: INSERT Basics

🟢 Beginner

Which statement best describes the primary use of the INSERT command in Oracle?

A. To delete unwanted rows from a table

B. To modify data in existing rows of a table

C. To add new rows of data into a table

D. To apply transaction control after a commit

---

## Question 2: Data Dictionary Views

🟢 Beginner

True/False: The Oracle data dictionary views (e.g., V$SESSION, V$LOCK) can be used to monitor DML operations and identify which sessions hold specific locks.

A. True

B. False

---

## Question 3: Truncate vs. Delete

🟢 Beginner

Fill in the blank:

"A TRUNCATE operation in Oracle is considered a ________ statement, whereas a DELETE operation is a DML statement."

A. Constraint

B. DDL

C. COMMIT

D. Index

---

## Question 4: Transaction Control

🟢 Beginner

Which of the following commands in Oracle makes all changes since the last COMMIT statement permanent?

A. SAVEPOINT

B. ROLLBACK

C. MERGE

D. COMMIT

---

## Question 5: Impact of a Missing WHERE Clause

🟢 Beginner

Multiple Choice:

What happens if you issue an UPDATE statement in Oracle without a WHERE clause?

A. Only rows inserted in the last transaction are updated

B. Only rows in the current session are updated

C. All rows in the table are updated

D. The statement fails with an error

---

## Question 6: Oracle Locking

🟢 Beginner

True/False:

When you run an UPDATE statement in Oracle, the database acquires row-level locks on the rows being updated.

A. True

B. False

---

## Question 7: Basic DELETE Statement

🟢 Beginner

Arrange the following steps in the correct order to perform a basic DELETE in Oracle:

A. Confirm the correct rows are targeted by SELECT

B. Issue the DELETE statement

C. COMMIT the transaction

D. Check the number of rows affected

---

## Question 8: INSERT ALL

🟡 Intermediate

Multiple Choice:

Which Oracle-specific feature allows inserting multiple rows into a table using a single SQL statement?

A. INSERT ALL

B. MERGE

C. Multi-table UPDATE

D. TRUNCATE

---

## Question 9: Conditional Update

🟡 Intermediate

True/False:

Including a WHERE clause in an UPDATE statement will allow you to conditionally modify only specific rows in Oracle.

A. True

B. False

---

## Question 10: SAVEPOINT Usage

🟡 Intermediate

Fill in the blank:

"A ________ allows you to rollback a portion of a transaction in Oracle without affecting all previously executed statements."

A. COMMIT

B. SAVEPOINT

C. FOREIGN KEY

D. FLASHBACK

---

## Question 11: MERGE Statement

🟡 Intermediate

Multiple Choice:

Which of the following best describes the function of the Oracle MERGE statement?

A. It creates a new table based on an existing query

B. It terminates multiple blocking sessions at once

C. It synchronizes data between two tables, combining INSERT and UPDATE operations

D. It performs a transaction rollback if more than one table is updated

---

## Question 12: Monitoring Blocking Sessions

🟡 Intermediate

Which Oracle view would you query to find sessions that are currently blocking others during a DML operation?

A. DBA_OBJECTS

B. V$SQL

C. V$LOCK

D. USER_INDEXES

---

## Question 13: DML Error Logging

🟡 Intermediate

Match each item in Column A with the appropriate description in Column B.

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

---

## Question 14: Isolation Levels

🟡 Intermediate

Arrange the following Oracle isolation levels in increasing order of strictness:

A. SERIALIZABLE
B. READ COMMITTED
C. READ ONLY
D. READ UNCOMMITTED (Not fully supported by Oracle, but included for comparison)

---

## Question 15: Bulk Data Loading

🔴 SRE-Level

Multiple Choice:

Which tool is best suited for high-volume data insertion into Oracle databases?

A. Data Pump Export
B. Data Pump Import
C. SQL*Loader
D. RMAN

---

## Question 16: Undo Space Management

🔴 SRE-Level

Which of the following statements about Oracle undo space is correct?

A. Undo segments are used only for read consistency and never for rollback

B. Large DML operations can exhaust undo space, leading to "snapshot too old" errors

C. Oracle databases do not require undo segments if using COMMIT frequently

D. Undo space is only consumed by DDL operations, not DML operations

---

## Question 17: Deadlock Detection

🔴 SRE-Level

True/False:

Oracle automatically detects and resolves deadlocks by rolling back one of the conflicting transactions.

A. True

B. False

---

## Question 18: Flashback Query

🔴 SRE-Level

Match each flashback technology to its primary purpose:

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

---

## Question 19: Lock Contention Troubleshooting

🔴 SRE-Level

Fill in the blank:

"To identify the sessions that are blocking others in Oracle, you would typically query __________."

A. V$LOCK

B. DICTIONARY

C. DBA_SEGMENTS

D. USER_TRIGGERS

---

## Question 20: Advanced Transaction Flow

🔴 SRE-Level

Order the following steps to process and recover from an erroneous DML transaction in an SRE scenario:

A. Use Flashback Query/Transaction to view or revert changes
B. Investigate DML performance impact with V$SESSION and V$SQL
C. Identify blocking locks and potential deadlocks
D. Run large batch UPDATE on a high-traffic table
