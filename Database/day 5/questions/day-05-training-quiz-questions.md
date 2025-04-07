# Day 5 Quiz Questions

## Quiz on Aggregating Data with SQL Aggregate Functions

**Instructions**:  

1. Answer each question based on the Day 5 training content about SQL aggregates (COUNT, SUM, AVG, MIN, MAX), GROUP BY, HAVING, and related performance/optimization considerations.  
2. Do not look for answers here; they are provided in a separate answer key.  
3. Apply the “Observe, Test, Evaluate, and Evolve” mindset.

---

### 🔍 Beginner-Level Questions (7)

#### 1. Multiple Choice

```
## Question 1: Aggregation Fundamentals
🔍 Beginner

Which of the following best describes the primary reason to use SQL aggregate functions such as SUM or AVG?

A. They replace the need for all JOIN operations
B. They combine multiple tables without specifying relationships
C. They summarize data by calculating totals or averages across sets of rows
D. They are only used for filtering out NULL values
```

---

#### 2. Multiple Choice

```
## Question 2: COUNT Function
🔍 Beginner

Which statement is TRUE regarding the difference between COUNT(*) and COUNT(column_name)?

A. COUNT(*) counts all rows including those with NULL in column_name, whereas COUNT(column_name) excludes rows where column_name is NULL.
B. COUNT(*) excludes NULL values, whereas COUNT(column_name) includes them.
C. They produce the same result in all circumstances.
D. COUNT(column_name) is always faster than COUNT(*).
```

---

#### 3. Multiple Choice

```
## Question 3: WHERE vs. HAVING
🔍 Beginner

Which of the following statements about WHERE and HAVING is correct?

A. Both WHERE and HAVING can be used interchangeably before grouping occurs.
B. WHERE filters rows before grouping, while HAVING filters groups after aggregation.
C. HAVING is used only for outer joins, while WHERE is used for inner joins.
D. WHERE is the same as HAVING except for the syntax of parentheses.
```

---

#### 4. True/False

```
## Question 4: Grouping
🔍 Beginner

A GROUP BY clause requires every non-aggregate column in the SELECT list to be included in GROUP BY.

A. True
B. False
```

---

#### 5. Fill-in-the-Blank

```
## Question 5: NULL Handling in Aggregates
🔍 Beginner

Complete the following statement:

________ ignores NULL values when computing the sum of a numeric column.

A. The SUM function
B. The HAVING clause
C. The GROUP BY keyword
D. The ORDER BY clause
```

---

#### 6. Multiple Choice

```
## Question 6: MIN and MAX Functions
🔍 Beginner

Which statement is CORRECT regarding MIN and MAX in SQL?

A. MIN can only be used on numeric columns, and MAX can only be used on date columns
B. MIN and MAX both ignore NULL values by default
C. MIN and MAX can be applied to numeric, date/time, or string columns
D. MIN returns the minimum column length, while MAX returns the maximum column length
```

---

#### 7. True/False

```
## Question 7: AVG Function
🔍 Beginner

When using AVG(column_name), rows with NULL in column_name are counted as zero in the average.

A. True
B. False
```

---

### 🧩 Intermediate-Level Questions (7)

#### 8. Multiple Choice

```
## Question 8: JOIN with Aggregation
🧩 Intermediate

You have two tables: 'orders' and 'customers'. Which SQL statement will correctly return each customer's total order amount?

A. 
SELECT customer_name, SUM(order_total)
FROM orders 
JOIN customers ON orders.customer_id = customers.customer_id;

B.
SELECT c.customer_name, SUM(o.order_total)
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name;

C.
SELECT customer_name, order_total
FROM orders
WHERE order_total IS NOT NULL;

D.
SELECT c.customer_name, o.order_total
FROM customers c, orders o 
WHERE c.customer_id = o.customer_id;
```

---

#### 9. Multiple Choice

```
## Question 9: GROUP BY Multiple Columns
🧩 Intermediate

Which query correctly groups sales by region and product, displaying total sales for each combination?

A.
SELECT region, product, SUM(amount)
FROM sales
WHERE region, product
GROUP BY region, product;

B.
SELECT region, product, SUM(amount)
FROM sales
GROUP BY region AND product;

C.
SELECT region, product, SUM(amount)
FROM sales
GROUP BY region, product;

D.
SELECT region, product, amount
FROM sales
GROUP BY region, product;
```

---

#### 10. Multiple Choice

```
## Question 10: Aggregation Performance
🧩 Intermediate

Which of the following strategies can help improve performance for a GROUP BY query on a large table?

A. Removing the GROUP BY clause entirely
B. Using a MERGE statement instead of SELECT
C. Creating an index on the column(s) used in GROUP BY
D. Converting the table to a CSV file
```

---

#### 11. True/False

```
## Question 11: HAVING Clause
🧩 Intermediate

The HAVING clause can be used to filter aggregated results based on conditions involving aggregate functions.

A. True
B. False
```

---

#### 12. Fill-in-the-Blank

```
## Question 12: DISTINCT Keyword
🧩 Intermediate

Complete the following statement:

To count the number of unique regions in a table named 'locations', you would use:

SELECT ________(DISTINCT region)
FROM locations;

A. SUM
B. COUNT
C. AVG
D. GROUP BY
```

---

#### 13. Matching

```
## Question 13: Common Aggregation Concepts
🧩 Intermediate

Match each item in Column A with the correct description in Column B.

Column A:
1. COUNT(*)
2. SUM(column)
3. GROUP BY
4. HAVING

Column B:
A. Filters grouped results based on an aggregate condition
B. Returns the total of numeric values in a column, ignoring NULLs
C. Counts all rows, including those with NULLs
D. Partitions rows into sets by shared column values
```

---

#### 14. Ordering

```
## Question 14: Aggregation Query Execution Order
🧩 Intermediate

Arrange the following phases of a SELECT query with GROUP BY and HAVING in the correct order:

A. GROUP rows based on the GROUP BY clause
B. Apply the HAVING clause to filter grouped rows
C. Perform aggregate calculations (SUM, COUNT, etc.)
D. Select rows from the table
```

---

### 💡 Advanced/SRE-Level Questions (6)

#### 15. Multiple Choice

```
## Question 15: Window Functions
💡 Advanced/SRE

Which statement best describes why you might use a window function (e.g., SUM OVER PARTITION BY) instead of a GROUP BY?

A. Window functions permanently store aggregated results in a new table
B. Window functions allow you to retain detail rows while still performing aggregate calculations
C. Window functions run faster than GROUP BY in all scenarios
D. Window functions can only be used for counting distinct values
```

---

#### 16. Multiple Choice

```
## Question 16: Pre-Aggregation Strategies
💡 Advanced/SRE

You're dealing with a high-throughput system that repeatedly queries the same daily sales aggregates. Which approach best reduces overhead?

A. Always run a fresh GROUP BY query each time
B. Use a CURSOR to manually sum each row in the application layer
C. Create a materialized view or summary table that stores pre-aggregated results
D. Rely on the DISTINCT keyword to optimize queries
```

---

#### 17. Multiple Choice

```
## Question 17: Execution Plan Analysis
💡 Advanced/SRE

In Oracle, you notice your aggregation query is using a “SORT GROUP BY” step with a high cost. Which of the following changes is MOST likely to improve performance?

A. Switch from SUM to AVG
B. Create or use an index aligned with the GROUP BY column(s)
C. Increase the batch size in your application’s code
D. Use nested subqueries without GROUP BY
```

---

#### 18. Fill-in-the-Blank

```
## Question 18: Partitioning for Aggregation
💡 Advanced/SRE

Complete the following statement:

When using table partitioning, large-scale aggregations can be sped up because each partition can be ________.

A. Filled with NULL values
B. Maintained entirely in a foreign key
C. Processed independently in parallel
D. Sorted only once
```

---

#### 19. Matching

```
## Question 19: SRE Aggregation Considerations
💡 Advanced/SRE

Match each SRE-related aggregation concept in Column A with its appropriate description in Column B.

Column A:
1. Materialized View Refresh
2. Execution Plan Monitoring
3. High Availability Setup
4. Partition Pruning

Column B:
A. Automatically discards irrelevant partitions to reduce query time
B. Periodically updates pre-aggregated tables to reflect fresh data
C. Ensures minimal downtime and data redundancy for critical aggregations
D. Involves checking for expensive operations, such as full scans or sorts, in aggregated queries
```

---

#### 20. Ordering

```
## Question 20: Diagnosing Aggregation Performance
💡 Advanced/SRE

Arrange the following troubleshooting steps in the correct order when investigating a slow aggregation query in production:

A. Check the execution plan for GROUP BY or HASH GROUP BY operations
B. Identify the table(s) and index structures used by the query
C. Collect metrics (CPU, I/O, memory usage) and confirm the query is indeed the bottleneck
D. Optimize or add indexes, and rerun the query to evaluate performance improvements
```

---

**End of Quiz**  

This set of 20 questions covers topics ranging from aggregation fundamentals and syntax (COUNT, SUM, AVG, MIN, MAX) to GROUP BY, HAVING, performance optimization, JOIN usage, window functions, and CRUD schema design considek!  

citeturn1file0
