# Day 4 – SQL JOIN Types Quiz Questions

citeturn1file0

Below is a comprehensive set of **20 quiz questions** designed to assess knowledge of Day 4’s SQL JOIN concepts (Oracle focus). The questions progress from **Beginner** (🔍) to **Intermediate** (🧩) to **Advanced/SRE** (💡), covering multiple question formats: multiple choice, true/false, fill-in-the-blank, matching, and ordering.

---

## 🔍 Beginner-Level Questions (7 Total)

### 1. Multiple Choice: Basic JOIN Purpose

```
## Question 1: JOIN Fundamentals
🔍 Beginner

Which statement best describes the main purpose of a SQL JOIN?

A. To delete data from multiple tables.
B. To combine rows from multiple tables based on related columns.
C. To replicate data in different tables.
D. To check constraints on foreign keys.
```

### 2. Multiple Choice: ANSI vs. Traditional Syntax

```
## Question 2: Oracle JOIN Syntax
🔍 Beginner

What is the recommended syntax for writing an OUTER JOIN in modern Oracle environments?

A. Using the WHERE clause with the (+) operator
B. Using CROSS JOIN syntax only
C. Using the ANSI syntax (e.g., LEFT OUTER JOIN)
D. Using only a NATURAL JOIN
```

### 3. Multiple Choice: INNER JOIN

```
## Question 3: INNER JOIN Basics
🔍 Beginner

Which of the following best describes an INNER JOIN?

A. Returns all rows from both tables, with NULLs for unmatched rows
B. Returns only matched rows from both tables
C. Returns every possible combination of rows from both tables
D. Returns all rows from the left table, plus matched rows from the right
```

### 4. True/False: LEFT OUTER JOIN

```
## Question 4: LEFT OUTER JOIN Behavior
🔍 Beginner

A LEFT OUTER JOIN returns all rows from the left table, plus matched rows from the right table.

A. True
B. False
```

### 5. Fill-in-the-Blank: CROSS JOIN

```
## Question 5: CROSS JOIN Concept
🔍 Beginner

Complete the following statement:

A CROSS JOIN between two tables produces a ________ of rows from the two tables.

A. partial intersection
B. sequence
C. balanced subset
D. Cartesian product
```

### 6. Matching: JOIN Keywords

```
## Question 6: Matching JOIN Keywords
🔍 Beginner

Match each JOIN keyword with its primary purpose:

Column A:
1. INNER
2. LEFT
3. RIGHT
4. FULL

Column B:
A. Retrieves all rows from both tables, matching where possible
B. Retrieves only rows that have matches in both tables
C. Retrieves all rows from the left table, plus matched rows from the right
D. Retrieves all rows from the right table, plus matched rows from the left
```

### 7. Ordering: Basic Steps in Writing a JOIN

```
## Question 7: Steps in Constructing a JOIN
🔍 Beginner

Arrange the following steps in the correct order when constructing a basic SQL JOIN:

A. Specify the tables in the FROM clause
B. Identify which columns link the tables (JOIN condition)
C. Use the JOIN keyword (INNER, LEFT, etc.)
D. Select the columns to display
```

---

## 🧩 Intermediate-Level Questions (7 Total)

### 8. Multiple Choice: Multiple-Table JOIN

```
## Question 8: Joining 3 Tables
🧩 Intermediate

When writing a query to join three tables (Customers, Orders, Products) in Oracle using ANSI syntax, which clause structure is correct?

A. FROM Customers, Orders, Products WHERE ...
B. FROM Customers c JOIN Orders o, Products p
C. FROM Customers c JOIN Orders o ON c.id = o.id JOIN Products p ON o.pid = p.pid
D. FROM Customers c LEFT Customers d RIGHT Products p
```

### 9. Multiple Choice: JOIN Order Considerations

```
## Question 9: JOIN Order in Oracle
🧩 Intermediate

Which of the following statements about join order in Oracle is TRUE?

A. The order of tables in the FROM clause has no effect on performance.
B. Oracle’s optimizer can reorder JOINs based on cost, but sometimes using hints can affect the chosen order.
C. Only the first two tables in the query can be reordered, subsequent tables remain fixed.
D. The order of tables is completely ignored by the optimizer.
```

### 10. Multiple Choice: RIGHT OUTER JOIN Scenario

```
## Question 10: RIGHT OUTER JOIN Usage
🧩 Intermediate

You have two tables: `departments` (right side) and `employees` (left side). A RIGHT OUTER JOIN is used to:

A. Return all rows from employees, plus matched rows from departments
B. Return only matched rows in both employees and departments
C. Return all rows from departments, plus matched rows from employees
D. Return a cartesian product of employees and departments
```

### 11. Multiple Choice: Legacy ( + ) Syntax

```
## Question 11: Oracle (+) Syntax
🧩 Intermediate

Which statement about the legacy `(+)` operator in Oracle is correct?

A. It can only be used for CROSS JOINs.
B. It can be placed on any column, including the SELECT list.
C. It is used in the WHERE clause to denote an outer join.
D. It indicates an INNER JOIN when used in the FROM clause.
```

### 12. True/False: Execution Plans

```
## Question 12: Viewing Execution Plans
🧩 Intermediate

You can use `EXPLAIN PLAN` or `DBMS_XPLAN.DISPLAY` in Oracle to inspect the execution plan for a JOIN query.

A. True
B. False
```

### 13. Fill-in-the-Blank: Index Usage

```
## Question 13: JOIN Performance
🧩 Intermediate

Complete the following statement:

Creating an index on columns used in the JOIN condition often ________ the query performance by allowing faster lookups.

A. degrades
B. improves
C. hides
D. complicates
```

### 14. Matching: JOIN Types vs. Result Sets

```
## Question 14: Matching JOIN Types
🧩 Intermediate

Match each JOIN type in Column A with its typical result set description in Column B:

Column A:
1. FULL OUTER JOIN
2. SELF JOIN
3. INNER JOIN
4. CROSS JOIN

Column B:
A. Joins all rows where a condition matches between two references of the same table
B. Includes all rows from both tables, matching where possible
C. Produces a cartesian product between two tables
D. Returns only the rows that match in both tables
```

---

## 💡 Advanced/SRE-Level Questions (6 Total)

### 15. Multiple Choice: HASH vs. NESTED LOOP

```
## Question 15: JOIN Algorithm
💡 Advanced/SRE

When might Oracle choose a HASH JOIN over a NESTED LOOP JOIN for an INNER JOIN?

A. When both tables are extremely small
B. When one table must be scanned multiple times with tight filtering
C. When large, unsorted data sets are joined, and a hashed approach is more efficient
D. When an equi-join involves partitioned tables
```

### 16. Multiple Choice: Performance Pitfalls

```
## Question 16: Performance Issues
💡 Advanced/SRE

Which scenario is most likely to cause performance issues in an OUTER JOIN query?

A. Using proper indexes on both sides of the JOIN
B. Retrieving a small subset of rows using a selective WHERE clause
C. Full table scans due to missing indexes on the joined columns
D. Maintaining accurate Oracle statistics on all tables
```

### 17. T/F: CROSS JOIN in Production

```
## Question 17: CROSS JOIN Caution
💡 Advanced/SRE

A CROSS JOIN is commonly used in large-scale production systems to retrieve all possible row combinations.

A. True
B. False
```

### 18. Fill-in-the-Blank: Join Hints

```
## Question 18: Oracle Hints
💡 Advanced/SRE

Complete the statement:

In Oracle, using a hint such as `USE_HASH` on a table can influence the ________ used by the optimizer.

A. index creation
B. join method
C. dataset constraints
D. referential integrity
```

### 19. Multiple Choice: Multiple-Table JOIN Optimization

```
## Question 19: Complex JOINs
💡 Advanced/SRE

When joining four large tables in Oracle, which step is most critical for preventing major performance bottlenecks?

A. Avoid specifying any WHERE clauses
B. Use `ORDER BY` on every column to pre-sort data
C. Analyze execution plans and ensure join columns are indexed appropriately
D. Always choose RIGHT OUTER JOIN for better performance
```

### 20. Ordering: Steps to Diagnose JOIN Performance

```
## Question 20: Performance Troubleshooting
💡 Advanced/SRE

Arrange the following steps in the correct order when diagnosing a slow JOIN query in Oracle:

A. Examine the execution plan via `DBMS_XPLAN.DISPLAY`
B. Identify relevant indexes on joined columns
C. Check table and index statistics
D. Compare actual vs. expected row counts in AWR or ASH reports
```
