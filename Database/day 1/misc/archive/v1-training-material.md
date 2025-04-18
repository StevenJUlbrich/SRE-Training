## 🏁 Introduction 
Welcome to **Day 1** of our SRE Database Training Module! We’re kicking off our journey into the world of **Relational Databases** and **Basic SQL Queries**. As Product Support personnel transitioning into SRE roles, you’ll learn how fundamental database structures and simple SQL statements are pivotal for reliability, troubleshooting, and everyday support tasks.

In a typical support scenario, you might need to look up customer order details or verify configuration records. These tasks become much simpler when you understand relational database concepts such as **tables**, **columns**, **rows**, **primary keys**, **foreign keys**, and how to use SQL’s **SELECT** statement to retrieve the exact data you need.

Below is a simple visual concept map of what we’ll cover today:

```
   ┌───────────────────────────┐
   │ Relational Databases      │
   │   (Tables, Keys, SQL)     │
   └───────────────────────────┘
               ↓
     ┌───────────────────┐
     │ Basic SQL Queries │
     │ (SELECT, FROM,    │
     │  WHERE)           │
     └───────────────────┘
               ↓
   ┌───────────────────────────┐
   │ Support & SRE Relevance   │
   │   (Reliability,           │
   │    Troubleshooting)       │
   └───────────────────────────┘
```

**Why this matters:**  
- **Real-World Context**: Databases underpin most applications you’ll support. 
- **SRE Alignment**: Understanding relational structures is the bedrock of reliability and performance. 
- **Problem-Solving**: Quick data lookups and root-cause analysis often start with basic SQL.

---

## 🎯 Learning Objectives by Tier

### 🔍 Beginner Objectives
1. **Explain** the concept of a relational database in simple terms.  
2. **Identify** tables, columns, rows, and understand the roles of primary and foreign keys.  
3. **Execute** basic SQL SELECT statements to retrieve data.  
4. **Navigate** a sample database confidently using simple queries.

### 🧩 Intermediate Objectives
1. **Interpret** relational database schemas and understand relationships (one-to-many, many-to-many).  
2. **Formulate** more targeted SELECT queries using WHERE clauses to filter data.  
3. **Assess** common performance implications of simple SELECT queries.  
4. **Troubleshoot** basic query errors and data inconsistencies.

### 💡 SRE-Level Objectives
1. **Analyze** how query design can impact database reliability and resource usage.  
2. **Optimize** SELECT queries to handle larger datasets or concurrent workloads.  
3. **Apply** SRE principles (monitoring, incident management) to database query performance.  
4. **Develop** a preventive mindset to avoid query-related incidents in production.

---

## 🌉 Knowledge Bridge
### Prerequisite Knowledge
- Familiarity with basic computing terminology (files, processes, etc.).
- Awareness of how applications store and retrieve data.

### Connections to Prior Knowledge
- If you’ve ever worked in a spreadsheet, you already understand rows and columns. A relational database applies similar logic but at a much larger scale.

### Future Foundation
- **Day 1** sets the stage for advanced topics like **DML (INSERT, UPDATE, DELETE)** on Day 2.
- Mastering the relational structure now will make it easier to handle joins, transactions, and performance tuning later.

### Learning Journey Timeline
```
(Basic DB Concepts) → [Day 1] → (DML Operations) → (Advanced Queries & Joins) → (Performance Tuning) → (High Availability)
```

---

## 📚 Core Concepts

### 1. Relational Database
- 🔍 **Beginner Analogy**: Think of a **library** where each book has a specific ID (primary key), and the library’s index (catalog) helps you find related topics (foreign keys).  
- 🔬 **Technical Explanation**: A relational database organizes data into **tables** (relations). Each table has columns (attributes) and rows (records). The **relational** part comes from linking data in one table to data in another via **keys**.  
- 💼 **Support/SRE Application**: You’ll query user/account data, log error details, or check system metrics stored in these tables.  
- 🔄 **System Impact**: Good relational design streamlines queries and ensures consistent performance. Poorly designed schemas cause slow queries and reliability issues.  
- ⚠️ **Common Misconceptions**:
  - Believing all databases are relational (some are NoSQL).  
  - Thinking you can’t scale relational databases effectively—modern technology can handle very large relational datasets.

### 2. Tables, Columns, Rows
- 🔍 **Beginner Analogy**: A **spreadsheet** with labeled columns (headers) and multiple rows of data.  
- 🔬 **Technical Explanation**:
  - **Table**: A set of columns defining data structure, and rows containing actual data.  
  - **Column**: A field representing a particular attribute (e.g., `customer_name`).  
  - **Row**: A single record/entry in the table (e.g., one customer).  
- 💼 **Support/SRE Application**: Understanding the structure helps you quickly find relevant data (e.g., searching for user_email in the `users` table).  
- 🔄 **System Impact**: Proper table design avoids duplication and speeds up queries.  
- ⚠️ **Common Misconception**:
  - Mixing up rows and columns can lead to confusion in queries.

### 3. Primary Keys & Foreign Keys
- 🔍 **Beginner Analogy**: The **“Social Security Number”** of a table (primary key) that another table references to connect (foreign key).  
- 🔬 **Technical Explanation**: 
  - **Primary Key (PK)**: A unique identifier for each row in a table (no duplicates, can’t be NULL).  
  - **Foreign Key (FK)**: A column in one table that references the primary key in another table, establishing a relationship.  
- 💼 **Support/SRE Application**: Resolving user issues often involves tracing data across multiple related tables via primary/foreign key relationships.  
- 🔄 **System Impact**: Proper key usage ensures referential integrity; mistakes can cause orphaned records or data inconsistency.  
- ⚠️ **Common Misconception**:
  - Assuming an FK is always a single column—sometimes composite keys exist.

### 4. Introduction to SQL
- 🔍 **Beginner Analogy**: **“Asking questions”** to your database using a structured language.  
- 🔬 **Technical Explanation**: SQL (Structured Query Language) is the standard language for interacting with relational databases. Basic operations include **SELECT**, **INSERT**, **UPDATE**, **DELETE**.  
- 💼 **Support/SRE Application**: You use SQL to query logs, configuration tables, or user data for troubleshooting.  
- 🔄 **System Impact**: Efficient SQL queries improve performance; inefficient queries can overload the system.  
- ⚠️ **Common Misconception**:
  - Thinking SQL is only for “DB Admins.” Support and SRE roles rely heavily on SQL for problem resolution.

---

## 💻 SQL Keyword & Concept Breakdown

### **SQL Keyword: SELECT (Retrieve data from one or more tables)**

**Keyword Overview:**  
- The **SELECT** keyword is used to fetch data from the database. It’s typically the first statement learned in SQL because it allows you to see what’s in your tables. Support and SRE teams use SELECT frequently to retrieve logs, user records, or system configurations.

**Syntax & Variations:**

| Syntax Form            | Example                        | Description                                    | Support/SRE Usage Context                          |
|------------------------|--------------------------------|------------------------------------------------|----------------------------------------------------|
| Basic SELECT           | `SELECT * FROM users;`         | Retrieves all columns from the users table.    | Quickly check all user data for a simple scenario. |
| SELECT specific columns| `SELECT id, name FROM users;`  | Retrieves only specified columns.              | Faster, more targeted lookups (performance gain).  |
| DISTINCT               | `SELECT DISTINCT region FROM users;` | Returns unique values for one column.     | Identify unique regions or categories.             |
| Cross-DB note          | `SELECT "Name" FROM "Users";`  | Some databases (Oracle, Postgres) might require quotes or have case sensitivity rules. | Varies by system; be mindful of reserved keywords. |

**Database Compatibility:**
- **Oracle**: May need double quotes for case-sensitive identifiers.  
- **PostgreSQL**: Similar to Oracle but allows flexible syntax for table/column naming.  
- **SQL Server**: Uses square brackets (`[ ]`) for quoted identifiers.  
- **MongoDB**: Not a SQL database, but the equivalent operation is `db.collection.find({})`.

**Tiered Examples:**

* 🔍 **Beginner Example:**
```sql
-- Example: Quickly view all columns in the 'customers' table
SELECT * 
FROM customers;
/* Expected output:
| customer_id | customer_name | email              | region   |
|-------------|---------------|--------------------|----------|
| 1           | Alice Jones   | alice@example.com  | North    |
| 2           | Bob Smith     | bob@example.com    | East     |
| ...         | ...           | ...                | ...      |
*/
-- This helps you confirm data is present and readable.
```

* 🧩 **Intermediate Example:**
```sql
-- Example: Filter specific columns for a support scenario
SELECT customer_id, customer_name
FROM customers
WHERE region = 'North';
/* Expected output:
| customer_id | customer_name |
|-------------|---------------|
| 1           | Alice Jones   |
| 5           | Mark Twain    |
*/
-- Context: Quick lookup of customers in the North region for a targeted support ticket.
```

* 💡 **SRE-Level Example:**
```sql
-- Example: Monitoring query for identifying top customers by order volume
SELECT c.customer_name, SUM(o.order_total) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY c.customer_name
ORDER BY total_spent DESC;
/* Expected output:
| customer_name | total_spent |
|---------------|-------------|
| Jane Doe      | 2540.00     |
| ...           | ...         |
*/
-- Context: Helps with capacity planning or analyzing transaction spikes.
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Always specify the columns you need instead of using `SELECT *` in production—improves performance and clarity.  
- 🧠 **Beginner Tip:** If unsure which columns exist, run a quick `SELECT *` to explore the table, then refine.

- 🔧 **SRE Insight:** Monitoring queries often group or aggregate data to find trends or anomalies.  
- 🔧 **SRE Insight:** Index usage is critical when selecting specific columns or filtering on them.

- ⚠️ **Common Pitfall:** Selecting all columns can cause excessive network traffic and slow queries.  
- ⚠️ **Common Pitfall:** Not filtering (missing WHERE conditions) can result in huge result sets that degrade performance.

- 🚨 **Security Note:** Always check if you’re exposing sensitive columns (e.g., passwords, personal data).  
- 💡 **Performance Impact:** Well-indexed columns in the WHERE clause or GROUP BY can dramatically speed up queries.

---

### **SQL Keyword: FROM (Specify which table(s) to query)**

**Keyword Overview:**  
- **FROM** is used to indicate the table(s) containing the data you want. You can also join multiple tables here. Support and SRE teams often join logs, configuration data, and user tables to diagnose issues.

**Syntax & Variations:**

| Syntax Form          | Example                          | Description                                      | Support/SRE Usage Context                          |
|----------------------|----------------------------------|--------------------------------------------------|----------------------------------------------------|
| Single Table         | `SELECT * FROM customers;`       | Retrieves data from one table.                   | Most common scenario for quick lookups.            |
| Multiple Tables (JOIN) | `SELECT ... FROM tableA JOIN tableB ON ...;` | Combines related data from two or more tables. | Investigate cross-table relationships (e.g., user & order). |
| Cross-DB note        | `SELECT * FROM schema.table;`    | Some systems require specifying schema or database name. | Large organizations with multiple schemas or cross-database queries. |

**Database Compatibility:**
- **Oracle** / **PostgreSQL** / **SQL Server**: Support multi-schema references (e.g., `schema_name.table_name`).  
- **MongoDB**: Uses collections instead of tables (`db.collection.find()`).

**Tiered Examples:**

* 🔍 **Beginner Example:**
```sql
SELECT customer_name 
FROM customers;
/* Retrieves customer_name from the customers table. */
```

* 🧩 **Intermediate Example:**
```sql
SELECT c.customer_name, o.order_date, o.order_total
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date = '2025-03-01';
/* Retrieves customers who placed orders on a specific date. */
```

* 💡 **SRE-Level Example:**
```sql
SELECT l.log_id, l.log_message, s.server_name
FROM logs l
JOIN servers s ON l.server_id = s.server_id
WHERE l.log_timestamp >= CURRENT_TIMESTAMP - INTERVAL '1 day'
ORDER BY l.log_timestamp DESC;
/* Useful for scanning log messages across multiple servers for a recent incident. */
```

**Instructional Notes:**
- 🧠 **Beginner Tip:** Learn the exact table names and schemas in your environment.  
- 🧠 **Beginner Tip:** Aliases (e.g., `customers c`) make queries easier to read.

- 🔧 **SRE Insight:** Joining data from multiple tables can reveal deeper patterns in error logs or usage metrics.  
- 🔧 **SRE Insight:** Indexing foreign keys is crucial for improving JOIN performance.

- ⚠️ **Common Pitfall:** Using the wrong JOIN type (e.g., `INNER JOIN` vs. `LEFT JOIN`) can omit needed data or cause confusion.  
- ⚠️ **Common Pitfall:** Not specifying a proper ON condition can lead to a Cartesian product (excessive row explosion).

- 🚨 **Security Note:** When referencing multiple schemas, be mindful of access controls.  
- 💡 **Performance Impact:** Large JOINs can be expensive; watch out for unindexed or large text columns.

---

### **SQL Keyword: WHERE (Filter rows based on a condition)**

**Keyword Overview:**  
- The **WHERE** clause narrows down the rows returned by your SELECT query. It’s essential for focusing on relevant data. Support engineers often use WHERE to find specific user records or identify logs matching certain criteria.

**Syntax & Variations:**

| Syntax Form              | Example                           | Description                                     | Support/SRE Usage Context                      |
|--------------------------|-----------------------------------|-------------------------------------------------|------------------------------------------------|
| Basic Condition          | `WHERE region = 'North'`          | Filters rows with region = 'North'.            | Target specific records (e.g., for a region).  |
| Multiple Conditions (AND)| `WHERE region = 'North' AND status = 'Active'` | Combine multiple filters.              | Narrow results for more precise troubleshooting. |
| Pattern Matching (LIKE)  | `WHERE email LIKE '%@example.com'`| Looks for email addresses ending with @example.com | Checking user domains or partial matches.  |
| Cross-DB note            | `WHERE "Region" ILIKE '%north%'`  | Some DBs like PostgreSQL support ILIKE for case-insensitive matching. | Varies by system; Oracle uses different functions. |

**Database Compatibility:**
- **Oracle**: Uses `LIKE` with `_` (single char) and `%` (multi-char), case sensitivity can differ.  
- **PostgreSQL**: Has `ILIKE` for case-insensitive matching.  
- **SQL Server**: Similar LIKE usage, no built-in ILIKE.  
- **MongoDB**: Uses query operators like `{"region": "North"}` in `find()` statements.

**Tiered Examples:**

* 🔍 **Beginner Example:**
```sql
SELECT customer_name 
FROM customers
WHERE region = 'North';
/* Retrieves only customers who live in the North region. */
```

* 🧩 **Intermediate Example:**
```sql
SELECT order_id, order_total
FROM orders
WHERE order_total > 100 AND status = 'Completed';
/* Helps identify larger completed orders for potential follow-up or auditing. */
```

* 💡 **SRE-Level Example:**
```sql
SELECT server_name, error_code, log_timestamp
FROM logs
WHERE log_timestamp >= CURRENT_DATE - INTERVAL '1 hour'
  AND error_severity >= 3
ORDER BY log_timestamp DESC;
/* Focus on high-severity errors in the last hour for immediate incident response. */
```

**Instructional Notes:**
- 🧠 **Beginner Tip:** Use `AND`/`OR` carefully; parentheses can clarify complex conditions.  
- 🧠 **Beginner Tip:** Watch out for typos in string comparisons (SQL is often case-sensitive depending on config).

- 🔧 **SRE Insight:** Filtering logs by time windows is critical for investigating incidents.  
- 🔧 **SRE Insight:** Creating indexes on frequently filtered columns (e.g., `region`, `order_date`) dramatically improves query performance.

- ⚠️ **Common Pitfall:** Omitting the WHERE clause inadvertently returns all rows—performance or data leakage risk.  
- ⚠️ **Common Pitfall:** Using `OR` across multiple columns can degrade performance if not indexed properly.

- 🚨 **Security Note:** Be mindful of SQL injection if user input is directly appended to WHERE clauses. Always sanitize or use parameterized queries.  
- 💡 **Performance Impact:** Proper filters reduce result sets and resource usage, improving response times.

---

## 🛠️ System Effects Section
When you run **SELECT** queries with **FROM** and **WHERE** clauses, the database engine:
1. **Parses** the query and checks if the syntax is valid.  
2. **Optimizes** the query plan (determines which indexes to use, how to join tables, etc.).  
3. **Executes** the query, reading data from disk or memory (I/O and CPU usage).  
4. **Returns** the result set to the user/application.

Factors affecting performance:
- **Indexes**: Speed up searches but have storage overhead.  
- **Table Size**: Larger tables require more I/O.  
- **Concurrency**: Multiple users running complex queries simultaneously can lead to contention.  
- **Caching**: Data frequently accessed can be cached, improving speed.

A simplified query execution flow might look like this:

```
┌───────────┐     ┌─────────────┐
│ User/Tool │     │ SQL Database │
└────┬──────┘     └─────┬───────┘
     │ 1) SELECT query   │
     └──────────────────>│
     │                   │ 2) Parse & Optimize
     │                   │ 3) Execute Plan
     │                   │ 4) Return Result
     │<──────────────────┘
```

---

## 🔨 Hands-On Exercises

### 🔍 Beginner Exercises (3)

1. **Basic SELECT**  
   - **Goal**: Retrieve all columns from the `customers` table.  
   - **Steps**:  
     1. Connect to the sample database.  
     2. Run `SELECT * FROM customers;`.  
     3. Observe the output and identify the columns/rows returned.  
   - **Verification**: Ensure you see data for each customer in the console.

2. **Selective Columns**  
   - **Goal**: Query only the `customer_id` and `customer_name` from `customers`.  
   - **Steps**:  
     1. Run `SELECT customer_id, customer_name FROM customers;`.  
     2. Confirm only two columns display.  
   - **Verification**: Matches the expected columns without extra data.

3. **Simple WHERE Filter**  
   - **Goal**: Return all customers in the “North” region.  
   - **Steps**:  
     1. Run `SELECT * FROM customers WHERE region = 'North';`.  
     2. Observe how many results are returned.  
   - **Verification**: Ensure results only list customers with `region = 'North'`.

---

### 🧩 Intermediate Exercises (3)

1. **Multiple Condition Query**  
   - **Goal**: List orders where `order_total > 50` and `status = 'Completed'`.  
   - **Steps**:  
     1. Connect to or switch to the appropriate `orders` table.  
     2. Run a query with `WHERE order_total > 50 AND status = 'Completed';`.  
     3. Notice how many results appear.  
   - **Verification**: Only completed orders with totals above 50 are shown.

2. **JOIN Two Tables**  
   - **Goal**: Find all customers and their corresponding orders made in the last 7 days.  
   - **Steps**:  
     1. Use `JOIN` on `customers` and `orders` with the matching key (`customer_id`).  
     2. Filter on `order_date >= CURRENT_DATE - INTERVAL '7 days'`.  
     3. Return columns like `customer_name`, `order_id`, and `order_total`.  
   - **Verification**: Ensure each row shows a valid `customer_name` with a recent `order_id` and `order_total`.

3. **Using Aliases and Sorting**  
   - **Goal**: Retrieve `customer_name` and total spent, sorted by total spent descending.  
   - **Steps**:  
     1. Alias `customers` as `c` and `orders` as `o`.  
     2. SUM up `order_total` grouped by `customer_name`.  
     3. Sort by the sum in descending order.  
   - **Verification**: Confirm the results show customers with a calculated `total_spent`, properly sorted.

---

### 💡 SRE-Level Exercises (3)

1. **Identify Slow Queries**  
   - **Goal**: Write a SELECT statement that intentionally scans a large table without an index, then use the database’s execution plan tools to identify the bottleneck.  
   - **Steps**:  
     1. Ensure the `logs` table has no index on `message_text`.  
     2. Run a query using `WHERE message_text LIKE '%error%'`.  
     3. Check the execution plan to see table scans.  
   - **Verification**: Confirm that the database indicates a full table scan, highlighting potential performance issues.

2. **Time-Window Analysis for Incident**  
   - **Goal**: Query logs from the last hour to diagnose a production incident.  
   - **Steps**:  
     1. Use `WHERE log_timestamp >= CURRENT_TIMESTAMP - INTERVAL '1 hour'`.  
     2. Filter by `error_severity >= 3`.  
     3. Sort by `log_timestamp DESC`.  
   - **Verification**: Check how many critical errors occurred in the last hour.

3. **Performance-Oriented JOIN**  
   - **Goal**: Investigate top resource-consuming queries by joining a `query_stats` table and a `users` table.  
   - **Steps**:  
     1. JOIN `query_stats` on `users.user_id = query_stats.user_id`.  
     2. Filter by queries with `execution_time > 500ms`.  
     3. Return relevant columns to highlight potential user-related patterns.  
   - **Verification**: Confirm the results show which user is running slow queries, and how often.

---

## 📝 Knowledge Check Quiz

### 🔍 Beginner Tier (3 Questions)
1. **Which of the following best describes a primary key?**  
   - A) A column that can contain duplicates  
   - B) A unique identifier for each row, can’t be NULL  
   - C) A separate table for referencing data  
   - D) A naming convention for the first column  
   - **Answer Explanation**: B is correct. Primary keys must be unique for each row and cannot be NULL.

2. **What does `SELECT * FROM customers;` do?**  
   - A) Inserts data into the customers table  
   - B) Deletes data from the customers table  
   - C) Retrieves all columns and rows from the customers table  
   - D) Updates the customers table  
   - **Answer Explanation**: C is correct. `SELECT *` returns all columns/rows.

3. **Which statement is false regarding relational databases?**  
   - A) Data is organized into tables with rows and columns  
   - B) Tables are linked through primary and foreign keys  
   - C) They cannot handle large datasets  
   - D) SQL is commonly used to query them  
   - **Answer Explanation**: C is false. Relational databases can indeed handle large datasets with proper design and scaling.

---

### 🧩 Intermediate Tier (3 Questions)
1. **When you use `WHERE region = 'North' AND status = 'Active'`, how many rows will be returned?**  
   - A) Rows where region is 'North' or status is 'Active'  
   - B) Only rows that have both region = 'North' and status = 'Active'  
   - C) All rows from the table  
   - D) No rows at all  
   - **Answer Explanation**: B is correct. Both conditions must be true for a row to appear.

2. **What is a key difference between `SELECT *` and `SELECT column1, column2`?**  
   - A) There is no difference in performance or clarity  
   - B) `SELECT *` returns all columns, potentially causing more data transfer  
   - C) `SELECT *` is faster in every situation  
   - D) `SELECT column1, column2` is invalid SQL syntax  
   - **Answer Explanation**: B is correct. `SELECT *` can impact performance and clarity.

3. **If an `INNER JOIN` is used but the matching rows don’t exist in the second table, what happens?**  
   - A) It returns all rows from the first table regardless  
   - B) It returns only matched rows, excluding those without matches  
   - C) It merges unmatched rows with nulls  
   - D) It errors out  
   - **Answer Explanation**: B is correct. `INNER JOIN` only returns rows with matching keys in both tables.

---

### 💡 SRE-Level Tier (3 Questions)
1. **Which factor most significantly impacts query performance for large tables?**  
   - A) The number of columns only  
   - B) Proper indexing and query design  
   - C) Using `SELECT *` in all queries  
   - D) The naming convention of the table  
   - **Answer Explanation**: B is correct. Indexing and thoughtful query design are crucial for performance.

2. **What is the primary benefit of analyzing an execution plan for a SELECT query?**  
   - A) It automatically fixes performance problems  
   - B) It shows how the database will execute the query, revealing bottlenecks  
   - C) It displays all possible queries run in the last 24 hours  
   - D) It is only for database administrators, not SREs  
   - **Answer Explanation**: B is correct. Execution plans help you understand the query path and optimize accordingly.

3. **Which scenario would likely cause concurrency issues and slow performance?**  
   - A) A single user running SELECT * on a small table  
   - B) Multiple large scans on heavily used tables lacking proper indexes  
   - C) Using a WHERE clause that references an indexed column  
   - D) Running a query during off-peak hours  
   - **Answer Explanation**: B is correct. Multiple large scans without indexes can choke concurrency.

---

## 🚧 Troubleshooting Scenarios

Below are **3** realistic scenarios you might encounter in support roles:

1. **Scenario: Missing Orders in Report**  
   - 📊 **Symptom**: The “daily sales” dashboard is missing some orders.  
   - 🔍 **Possible Causes**:  
     1. Orders were entered after the reporting cutoff time.  
     2. The JOIN condition was incorrect in the SQL statement.  
     3. The `WHERE` clause accidentally filtered out certain orders.  
   - 🔬 **Diagnostic Approach**:  
     1. Check if the report’s SELECT statement has a date range (WHERE clause).  
     2. Validate the JOIN between `orders` and `customers`.  
     3. Compare the raw `orders` table count vs. the count used in the dashboard.  
   - 🔧 **Resolution Steps**:  
     1. Adjust the date range to include late entries.  
     2. Correct any incorrect JOIN logic.  
     3. Remove or refine filters that exclude valid data.  
   - 🛡️ **Prevention Strategy**: Automate time windows or use dynamic date filters to avoid missing data.  
   - 🧩 **Knowledge Connection**: Highlights the importance of accurate WHERE and JOIN clauses.

2. **Scenario: Timeout Errors on Production Queries**  
   - 📊 **Symptom**: Several SELECT queries are timing out, causing slow application responses.  
   - 🔍 **Possible Causes**:  
     1. Large table scans with no index usage.  
     2. High concurrency (many queries at once).  
     3. Poor network bandwidth or resource limits.  
   - 🔬 **Diagnostic Approach**:  
     1. Check the execution plan to see if indexes are used.  
     2. Monitor concurrent connections and CPU usage.  
     3. Test from multiple network segments.  
   - 🔧 **Resolution Steps**:  
     1. Create or update indexes on frequently filtered columns.  
     2. Tune the query or split it into smaller subqueries if needed.  
     3. Increase or optimize resources (memory, CPU).  
   - 🛡️ **Prevention Strategy**: Regular index maintenance and capacity planning.  
   - 🧩 **Knowledge Connection**: Demonstrates how performance issues relate to SRE responsibilities.

3. **Scenario: User Records Not Updating**  
   - 📊 **Symptom**: Support team notices that user profile changes are not reflected in search results.  
   - 🔍 **Possible Causes**:  
     1. Caching or stale read replicas.  
     2. The SELECT query is pointing to an old or incorrect database instance.  
     3. The data was never actually committed or updated.  
   - 🔬 **Diagnostic Approach**:  
     1. Compare the user row in the primary database vs. read replica.  
     2. Check the connection string for the correct database environment.  
     3. Validate the last updated timestamp for the row.  
   - 🔧 **Resolution Steps**:  
     1. Refresh or invalidate the cache if using a caching layer.  
     2. Update the SELECT statement to point to the correct instance.  
     3. Confirm successful execution of UPDATE/COMMIT.  
   - 🛡️ **Prevention Strategy**: Have clear environment naming and verify read/write connections.  
   - 🧩 **Knowledge Connection**: Shows how simple SELECT queries can expose deeper environment or replication issues.

---

## ❓ Frequently Asked Questions

### 🔍 Beginner FAQs
1. **Can I learn SQL without a technical background?**  
   - **Answer**: Absolutely! SQL is designed for readability and is often easier for beginners compared to lower-level programming.  
2. **Is there a difference between a table and a spreadsheet?**  
   - **Answer**: Conceptually similar in structure, but databases enforce stricter rules and can handle more data and concurrency.  
3. **Why do I see quotes or brackets around table names in some queries?**  
   - **Answer**: Different databases have different rules for naming conventions and reserved words. Quotes/brackets help avoid conflicts.

### 🧩 Intermediate FAQs
1. **How can I find which columns are available in a table?**  
   - **Answer**: Use commands like `DESCRIBE table_name;` (MySQL), or check information_schema tables in PostgreSQL/SQL Server.  
2. **Does using WHERE always improve performance?**  
   - **Answer**: Generally, filtering can reduce the data set, but performance also depends on proper indexing of the filtered columns.  
3. **What if I need data from three or more tables?**  
   - **Answer**: You can JOIN multiple tables in a chain. Just ensure your JOIN conditions are correct to avoid cartesian products.

### 💡 SRE-Level FAQs
1. **How do I measure the performance cost of a SELECT query?**  
   - **Answer**: Use `EXPLAIN` or `EXPLAIN ANALYZE` in your database to see the query execution plan and measure run times.  
2. **When should I worry about concurrency in SELECT queries?**  
   - **Answer**: High-traffic environments or large, complex queries can cause contention. Monitoring CPU, locks, and response times is critical.  
3. **Is partitioning relevant for basic SELECT statements?**  
   - **Answer**: It can be, especially if your tables are huge. Partitioning by date or region can improve query performance and manage large data sets.

---

## 🔥 Support/SRE Scenario

**Detailed Incident: Slow Customer Lookup**

This scenario walks you through a **5-step** process using SQL commands to diagnose and fix a slow query used by Support for customer lookups:

1. **Step 1**: Identify the slow query reported by Support:
   ```sql
   SELECT * 
   FROM customers
   WHERE email LIKE '%@example.com';
   ```
   - **Reasoning**: The wildcard `%` at the start can force a full table scan.

2. **Step 2**: Check the execution plan:
   ```sql
   EXPLAIN ANALYZE
   SELECT * 
   FROM customers
   WHERE email LIKE '%@example.com';
   ```
   - **Reasoning**: We want to see if an index is used or if a sequential scan occurs.

3. **Step 3**: Add an index on the `email` column (if appropriate):
   ```sql
   CREATE INDEX idx_customers_email ON customers (email);
   ```
   - **Reasoning**: For improved performance. However, note the leading `%` negates many indexing benefits unless using specialized indexes (e.g., full-text or trigram indexes in PostgreSQL).

4. **Step 4**: Modify the query pattern if possible:
   ```sql
   SELECT *
   FROM customers
   WHERE email LIKE '%@example.com' 
     AND email LIKE '%.com';
   ```
   - **Reasoning**: In some cases, refining conditions can help. Alternatively, capturing the domain in a separate column can drastically improve indexing.

5. **Step 5**: Re-test performance:
   ```sql
   EXPLAIN ANALYZE
   SELECT *
   FROM customers
   WHERE email LIKE '%@example.com';
   ```
   - **Reasoning**: Confirm the query runs faster and the plan indicates better optimization.

**SRE Principles**: 
- **Observability**: Use `EXPLAIN` and logs to see how queries behave.  
- **Performance**: Indexing and query design are crucial for reliability.  
- **Scalability**: Properly optimized queries scale better under load.

---

## 🧠 Key Takeaways

**Command/Keyword Summary Points (5+)**  
1. **SELECT** – The fundamental keyword for retrieving data.  
2. **FROM** – Specifies the table(s) from which to pull data.  
3. **WHERE** – Filters rows to narrow down your query.  
4. **JOIN** – Combines data from multiple tables based on related columns.  
5. **PRIMARY KEY** & **FOREIGN KEY** – Essential for relational structure and data integrity.  
6. **INDEX** – A performance booster that helps queries run faster.

**Operational Insights (3+)**  
1. Efficient indexing dramatically improves query performance and reduces timeouts.  
2. Well-structured SQL statements help isolate issues quickly during incidents.  
3. Monitoring query execution plans is crucial to maintain reliability and optimal performance.

**Best Practices (3+)**  
1. Always specify columns rather than using `SELECT *` in production.  
2. Validate table relationships and keys regularly to avoid data mismatches.  
3. Use aliases and consistent naming conventions to keep queries readable and maintainable.

**Critical Warnings/Pitfalls (3+)**  
1. Overusing `SELECT *` can degrade performance and leak unnecessary data.  
2. Incorrect JOIN conditions can lead to missing or duplicated rows, confusing results.  
3. Failing to sanitize user inputs can lead to SQL injection vulnerabilities.

**Connections to Support/SRE Excellence**  
- Rapid, accurate data retrieval underpins quick incident resolution.  
- Proper query design ensures minimal downtime and resource usage.  
- Preventing performance issues frees time for proactive SRE tasks.

---

## 🔮 Preview of Next Topic
**Day 2** will cover **DML (INSERT, UPDATE, DELETE)** queries. You’ll learn how to add new records, modify existing data, and remove unnecessary rows safely. We’ll also explore **transactions** and how they help ensure data consistency—critical for SRE duties like reliable deployments and maintenance.

**Prep Suggestion**: Familiarize yourself with the table structures in your environment. Knowing the table and column names will help you confidently use INSERT, UPDATE, and DELETE in the next session.

---

## 📚 Further Learning Resources

### 🔍 Beginner Resources (3)

1. **SQLBolt**  
   - **Link**: [https://sqlbolt.com/](https://sqlbolt.com/)  
   - **Description**: Interactive SQL lessons starting from basic SELECT queries.  
   - **Support Role Application**: Great for hands-on practice with fundamental queries.

2. **W3Schools SQL Tutorial**  
   - **Link**: [https://www.w3schools.com/sql/](https://www.w3schools.com/sql/)  
   - **Description**: Step-by-step guide with examples and quizzes.  
   - **Support Role Application**: Quickly review concepts when you need a refresher.

3. **Khan Academy – Intro to SQL**  
   - **Link**: [https://www.khanacademy.org/computing/computer-programming/sql](https://www.khanacademy.org/computing/computer-programming/sql)  
   - **Description**: Beginner-friendly, covers essential SQL basics with practice exercises.  
   - **Support Role Application**: Solid foundation for new support engineers or those wanting to solidify knowledge.

---

### 🧩 Intermediate Resources (3)

1. **PostgreSQL Documentation**  
   - **Link**: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)  
   - **Description**: Official documentation covering deeper SQL functionalities.  
   - **Operational Connection**: Learn about advanced queries, indexing, and performance tuning relevant to support tasks.

2. **Microsoft SQL Server Tutorials**  
   - **Link**: [https://docs.microsoft.com/sql/](https://docs.microsoft.com/sql/)  
   - **Description**: Microsoft’s official how-to guides and reference pages.  
   - **Operational Connection**: Many enterprise systems run on SQL Server, so this helps with real-world problem solving.

3. **Oracle Live SQL**  
   - **Link**: [https://livesql.oracle.com/](https://livesql.oracle.com/)  
   - **Description**: Browser-based Oracle SQL environment for experiments.  
   - **Operational Connection**: Practice multi-table queries and Oracle-specific syntax for enterprise scenarios.

---

### 💡 SRE-Level Resources (3)

1. **Use The Index, Luke!**  
   - **Link**: [https://use-the-index-luke.com/](https://use-the-index-luke.com/)  
   - **Description**: Deep dive into indexing and query optimization across different RDBMS.  
   - **Reliability Engineering Focus**: Optimize queries to maintain high availability.

2. **High Performance MySQL** (Book)  
   - **Link**: [https://www.oreilly.com/library/view/high-performance-mysql/9781449332471/](https://www.oreilly.com/library/view/high-performance-mysql/9781449332471/)  
   - **Description**: Covers performance tuning, replication, and cluster setups.  
   - **Reliability Engineering Focus**: Insightful for SREs managing large-scale MySQL deployments.

3. **Database Reliability Engineering** (Book)  
   - **Link**: [https://www.oreilly.com/library/view/database-reliability-engineering/9781491925935/](https://www.oreilly.com/library/view/database-reliability-engineering/9781491925935/)  
   - **Description**: Explores the intersection of DB administration and SRE principles.  
   - **Reliability Engineering Focus**: Ideal for advanced SRE-level knowledge on scaling and maintaining databases.

---

## 🎉 Closing Message
You’ve completed **Day 1** of the SRE Database Training Module! Today, you learned how relational databases are structured, why primary and foreign keys matter, and how to write basic SQL SELECT queries. These fundamental skills will help you troubleshoot effectively and keep systems reliable. 

Take a moment to celebrate your progress. Next, get ready to dive into **DML operations**—INSERT, UPDATE, and DELETE—where you’ll learn how to manipulate data safely and effectively in real-world support scenarios.

Keep practicing, stay curious, and remember that consistent improvement in SQL skills will make you a standout SRE and support engineer!

---

_**End of Day 1 Materials**_