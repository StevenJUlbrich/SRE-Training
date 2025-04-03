# Day 1 Database Quiz Questions

---

## 🟢 Beginner-Level Questions (7)

### 1. Multiple Choice

## Question 1: Oracle Database Structure

🟢 Beginner

Which of the following best describes a **table** in an Oracle database?

A. A collection of columns from multiple schemas  
B. A logical area used to store data files  
C. A structured set of rows and columns representing a single entity  
D. A user account that stores various database objects  

---

### 2. Multiple Choice

## Question 2: Basic SQL SELECT

🟢 Beginner

Which clause in a `SELECT` statement specifies the table from which data is retrieved?

A. SELECT  
B. FROM  
C. WHERE  
D. ORDER BY  

---

### 3. Multiple Choice

## Question 3: Primary & Foreign Keys

🟢 Beginner

Which statement about primary keys in Oracle is **true**?

A. A table can have multiple primary keys  
B. A primary key column must contain unique and non-null values  
C. Primary keys are optional for table creation  
D. Primary keys automatically create foreign keys in another table  

---

### 4. True/False

## Question 4: Oracle Tools

🟢 Beginner

SQL*Plus is a command-line tool provided by Oracle to interact with the database.

A. True  
B. False  

---

### 5. Fill-in-the-Blank

## Question 5: Database Dialects

🟢 Beginner

Complete the following statement:

Oracle uses `ROWNUM` to limit rows, while PostgreSQL uses ________, and SQL Server typically uses the `TOP` keyword.

A. OFFSET  
B. SKIP  
C. LIMIT  
D. FETCH  

---

### 6. Matching

## Question 6: Core Terminology

🟢 Beginner

Match each item in Column A with the appropriate description in Column B.

Column A:  

1. Table  
2. Column  
3. Row  
4. Schema  

Column B:  
A. A specific attribute or field in a table  
B. The collection of database objects owned by a user  
C. Represents a single record of data in a table  
D. A structured set of rows and columns representing an entity  

---

### 7. Ordering

## Question 7: SQL*Plus Connection Steps

🟢 Beginner

Arrange the following steps in the correct order to connect and run a simple query in SQL*Plus:

A. Type a SELECT statement and press Enter  
B. Exit SQL*Plus by typing `EXIT`  
C. Connect using `sqlplus username/password@hostname:port/SID`  
D. Verify successful connection by checking the SQL*Plus prompt  

---

## 🟡 Intermediate-Level Questions (7)

### 8. Multiple Choice

## Question 8: Oracle Data Dictionary

🟡 Intermediate

Which Oracle view can you query to list all tables **owned by the current user**?

A. DBA_TABLES  
B. ALL_TABLES  
C. USER_TABLES  
D. V$TABLES  

---

### 9. Multiple Choice

## Question 9: SQL Dialect Differences

🟡 Intermediate

In Oracle, the concatenation operator is `||`, whereas in SQL Server, the equivalent is:

A. `+`  
B. `CONCAT`  
C. `&`  
D. `||`  

---

### 10. Multiple Choice

## Question 10: Foreign Keys

🟡 Intermediate

Which of the following constraints in Oracle ensures that a column in the `orders` table references a valid customer ID in the `customers` table?

A. PRIMARY KEY (orders.customer_id)  
B. FOREIGN KEY (orders.customer_id) REFERENCES customers(customer_id)  
C. CHECK (customer_id IS NOT NULL)  
D. UNIQUE (customer_id)  

---

### 11. Multiple Choice

## Question 11: Oracle Tools

🟡 Intermediate

Which statement about Oracle SQL Developer is correct?

A. It is only available on UNIX systems  
B. It is a command-line utility similar to SQL*Plus  
C. It provides a graphical interface to browse schema objects and run SQL statements  
D. It cannot connect to remote Oracle databases  

---

### 12. True/False

## Question 12: Performance in Oracle

🟡 Intermediate

Creating an index on a frequently searched column can help improve the performance of SELECT queries in Oracle.

A. True  
B. False  

---

### 13. Fill-in-the-Blank

## Question 13: Troubleshooting Scenario

🟡 Intermediate

Complete the following statement:

When a user is unable to log in to Oracle due to account lockout, the DBA can unlock the user with the command:  

```sql
ALTER USER username ________;
```

A. ACCOUNT UNLOCK  
B. RESET LOCK  
C. ENABLE USER  
D. RELEASE ACCOUNT  

---

### 14. Matching

## Question 14: Oracle Dictionary Views

🟡 Intermediate

Match each Oracle dictionary view in Column A with its main purpose in Column B.

Column A:  

1. USER_TABLES  
2. DBA_USERS  
3. V$SESSION  
4. ALL_CONSTRAINTS  

Column B:  
A. Displays login names, statuses, and properties of all database accounts  
B. Shows currently active sessions in the database  
C. Lists the constraints defined on tables accessible to the user  
D. Lists tables owned by the current user  

---

## 🔴 SRE-Level Questions (6)

### 15. Multiple Choice

## Question 15: Oracle Execution Plans

🔴 SRE-Level

Which command sequence allows you to generate and view an execution plan for a query in Oracle?

A. `ANALYZE PLAN <query>; SELECT * FROM DBMS_XPLAN.EXPLAIN;`  
B. `EXPLAIN PLAN FOR <query>; SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);`  
C. `SHOW PLAN FOR <query>; SELECT plan_table;`  
D. `SELECT plan_table FROM V$SQL;`  

---

### 16. Multiple Choice

## Question 16: Oracle Performance Views

🔴 SRE-Level

Which performance view would you query to find information on SQL statements currently stored in the shared SQL area?

A. V$SQLAREA  
B. V$SESSION_LONGOPS  
C. USER_TABLES  
D. ALL_CONSTRAINTS  

---

### 17. Multiple Choice

## Question 17: Oracle SRE Operations

🔴 SRE-Level

When investigating a lock contention issue where multiple sessions are waiting on row locks, which view is most useful to identify blocking and waiting sessions?

A. V$LOCK  
B. V$MEMORY_STATISTICS  
C. USER_LOCKS  
D. ALL_SESSIONS  

---

### 18. True/False

## Question 18: Oracle Recovery

🔴 SRE-Level

RMAN (Recovery Manager) is an Oracle utility for performing backup and recovery operations.

A. True  
B. False  

---

### 19. Fill-in-the-Blank

## Question 19: Oracle Flashback

🔴 SRE-Level

Complete the following statement:

To retrieve older data from a table using Oracle Flashback Query, you can specify the ________ clause in your SELECT statement along with a past timestamp or SCN.

A. AS RECOVERED  
B. AS RESTORED  
C. AS OF  
D. AS ARCHIVE  

---

### 20. Ordering

## Question 20: SRE Diagnostic Steps

🔴 SRE-Level

Arrange the following steps in the correct sequence for diagnosing a slow-running query in Oracle:

A. Examine the query’s execution plan using `EXPLAIN PLAN`.  
B. Check real-time performance data in `V$SESSION` or `V$SQLAREA`.  
C. Identify the specific query or session causing the slowdown.  
D. Investigate indexes or rewrite the query for optimization.  

---

**End of Quiz**
