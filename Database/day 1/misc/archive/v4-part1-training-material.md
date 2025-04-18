# 🚀 Day 1: Core Relational Database Fundamentals & Basic SQL Queries

Welcome! This is a **comprehensive Day 1 training module** on relational database fundamentals using **PostgreSQL** as our primary reference system. We will also provide minimal references to Oracle and SQL Server where there are important differences to note. This document follows the **v4.0 SRE Database framework** and integrates **SRE principles** (reliability, observability, performance, scalability) from the very first step. Let’s begin our journey!

---

## 📌 Introduction

Databases are the beating heart of most reliable systems today. Understanding how data is structured, stored, and retrieved is crucial for **Product Support** roles and SREs alike. On Day 1, we’ll build your knowledge “brick by brick,” starting from the **absolute basics** of relational databases:

1. **Relational Database Structure** (tables, columns, rows, schemas)
2. **Key Concepts** (primary keys, foreign keys, relationships, constraints)
3. **Basic SQL** (SELECT, FROM, WHERE)
4. **Hands-On** (connecting to PostgreSQL sample databases)

### Why This Matters

Even simple misunderstandings of database concepts can cause:

- **Lost data** due to poorly understood relationships
- **Performance bottlenecks** from inefficient queries
- **Costly incidents and downtime**

Real-world incidents show that improper SELECT queries, missing WHERE clauses, or misunderstanding table relationships can quickly escalate into production outages. Let’s head off those mistakes from Day 1.

Below is a **concept map** that visually outlines Day 1 topics and how they tie together:

```text
            ┌─────────────────────┐
            │  Database (Schema)  │
            └─────────────────────┘
                │
                ▼
      ┌─────────────────────────────────┐
      │       Tables (Rows & Columns)   │
      └─────────────────────────────────┘
            │                │              
            ▼                ▼               
        Primary Key        Foreign Key  
            │                │               
            ▼                ▼               
      ┌─────────────────────────────────┐
      │ SELECT ── FROM ── WHERE         │
      └─────────────────────────────────┘
          (Basic SQL building blocks used to retrieve data)
```

We’ll primarily explore **PostgreSQL** examples, noting if Oracle/SQL Server differ significantly.

---

## 🎯 Learning Objectives by Tier

Below are the **4 objectives** at each skill tier, each tied to **SRE principles** and **practical support tasks**.

### 🔍 Beginner Objectives

1. **Identify** basic relational database components (tables, columns, rows).
2. **Explain** the purpose of primary keys and foreign keys in simple terms.
3. **Execute** simple SELECT queries with FROM and WHERE clauses in PostgreSQL.
4. **Connect** to a PostgreSQL database and **verify** basic connectivity.

### 🧩 Intermediate Objectives

1. **Analyze** database schemas to understand relationships (primary/foreign keys) in support tasks.
2. **Optimize** basic SELECT queries by refining columns and using WHERE clauses effectively.
3. **Troubleshoot** common connection issues in a structured, methodical manner.
4. **Apply** initial SRE concepts (like reliability and observability) when writing queries.

### 💡 SRE-Level Objectives

1. **Evaluate** how SELECT queries impact database performance and resource utilization.
2. **Monitor** queries for reliability and latency metrics using basic observability tools.
3. **Diagnose** slow query performance issues and propose targeted optimizations.
4. **Implement** fundamental capacity and concurrency considerations in daily operations.

---

## 🌉 Knowledge Bridge

Many of you have encountered applications where data is stored or retrieved, but you might not have a deep understanding of *how* the database is organized. Below is how we’ll connect your existing familiarity with “where the data lives” to formal database concepts:

- If you’ve ever used **spreadsheets**, each sheet is like a table, columns define data attributes, and rows hold individual records.
- Day 1 is your foundation: everything from simple queries to advanced SRE reliability starts here.
- **Prerequisite Check:**
  - Comfort with basic command-line operations or GUIs for database connections
  - General sense of how data is read and written by applications

Here’s your **learning timeline** for this course:

```plaintext
[Day 1: Core Relational Concepts] → [Day 2: Advanced Queries & Joins] → [Day 3: SRE-Driven Monitoring & Tuning] → ...
```

Eventually, we’ll connect these relational basics to **NoSQL** and **streaming systems**, demonstrating how different data solutions solve different problems.

---

## 📊 Visual Concept Map

Below is a more detailed visual concept map, **color-coded by complexity level** (🔍 = beginner, 🧩 = intermediate, 💡 = advanced/SRE), showing **how each concept interrelates** and **where SRE principles come into play**:

```text
 ┌─────────────────────────────────────────────────────────────────────────┐
 │                               Database                                  │
 │       (Schemas, Tables, Columns, Rows, Basic Storage Structures)        │
 └─────────────────────────────────────────────────────────────────────────┘
  │                  │                       │              │
  │                  │                       │              ▼ (💡 SRE Principle)
  │                  │                       │      Observability & Monitoring
  ▼ (🔍)             ▼ (🧩)                  ▼ (💡)
  Primary Key       Foreign Key            Performance Tuning
  (Uniqueness)        (Relationships)       (Query Plans, Indexing)
  │                  │                              │
  ▼                  ▼                              ▼
Basic SELECT → FROM → WHERE ───── (🔍 Basic usage → 🧩 Extended usage → 💡 High performance)
  (Reading data)     (Context)         (Filtering)
```

- SRE considerations ( 💡 ) span all tiers, gradually increasing in depth and technicality.

---

## 📚 Core Concepts

### 1. Tables, Columns, Rows, and Schemas

- **Beginner Analogy**: Think of a **table** as a grid in a spreadsheet. Each **column** is a labeled header (like “First Name”), and each **row** is a single record (like one customer).
- **Visual Representation**:

  ```text
  Table: customers
  ┌───────────────┬───────────────┬────────────────┐
  │ customer_id   │ first_name    │  last_name     │
  ├───────────────┼───────────────┼────────────────┤
  │ 1             │ Alice         │ Anderson       │
  │ 2             │ Bob           │ Brown          │
  └───────────────┴───────────────┴────────────────┘
  ```

- **Technical Explanation**: In a **relational** database, data is broken down into logical groupings called **tables**. A **schema** organizes these tables, often by business domain or function (e.g., `public` schema in PostgreSQL).
- **Support/SRE Application**: Knowing your table structure is crucial to troubleshooting missing data or app performance issues.
- **System Impact**: Properly designed tables scale better and reduce query complexity.
- **Common Misconceptions**:
  - *“All data in one table is simpler.”* Actually, large single tables become unmanageable and degrade performance.
- **Quick Reference**: A **table** is a structured collection of data with defined **columns**; each **row** is one record.

### 2. Primary Keys and Foreign Keys

- **Beginner Analogy**: A **primary key** is like a **unique ID number** on an official document; no two documents have the same ID. A **foreign key** is like a **reference** to someone’s ID in another record—tying related data together.
- **Visual Representation**:

  ```text
  Table: orders
  ┌───────────┬─────────────┬───────────┐
  │ order_id  │ customer_id │ amount    │
  ├───────────┼─────────────┼───────────┤
  │ 1001      │ 1           │ 500.00    │
  │ 1002      │ 2           │ 250.00    │
  └───────────┴─────────────┴───────────┘
                     ↑
            foreign key referencing 
            primary key in customers
  ```

- **Technical Explanation**:
  - **Primary Key (PK)**: Uniquely identifies rows in the table (e.g., `customer_id`). Typically indexed to speed lookups.
  - **Foreign Key (FK)**: Enforces referential integrity by linking to a PK in another table. The database ensures valid references.
- **Support/SRE Application**: Quick identification of related data across tables. Vital for diagnosing missing or inconsistent data issues.
- **System Impact**: Ensures data consistency, but foreign keys also add overhead on insert/update. Must be balanced with performance.
- **Common Misconception**:
  - *“We can ignore FKs for faster performance.”* This can lead to **orphan data** or data integrity problems.
- **Quick Reference**: **PK** = unique row identifier. **FK** = references PK in another table to link data sets.

---

## 💻 Day 1 Concept & Command Breakdown

Below are the **six key Day 1 concepts/commands**, each broken down in the required format:

---

### **Command/Concept: Relational Database Structure (Basics of Tables, Columns, Rows)**

**Overview:**  
Relational Database Structure forms the core of how data is organized. A database contains **schemas**, which in turn contain **tables** made of **columns** (definitions) and **rows** (actual records).

**Real-World Analogy:**  
A **file cabinet** with multiple **folders** (schemas), each containing **documents** (tables). Within each document, you have labeled sections (columns) and text entries (rows).

**Visual Representation:**

```text
+----------------------- Database -----------------------+
|  Schema: public                                        |
|     +------------------ Table: employees -------------+|
|     |  columns: (id, first_name, last_name, ... )     ||
|     |  rows:    each row is one employee record       ||
|     +-------------------------------------------------+|
+--------------------------------------------------------+
```

**Syntax & Variations:**

| Syntax Form                            | Example                             | Description                                                           | Support/SRE Usage Context                              |
|--------------------------------------- |------------------------------------ |-----------------------------------------------------------------------|--------------------------------------------------------|
| Create Table                           | `CREATE TABLE table_name (...);`    | Defines a new table with specified columns and data types             | Adding new data structures in support of an application|
| Show Tables (PostgreSQL)              | `\dt` (in psql)                     | Lists existing tables in the current schema                           | Quick reference in troubleshooting                     |
| Describe Table (PostgreSQL)           | `\d table_name`                     | Shows columns, types, and constraints of a table                      | Identifies structure before writing queries            |
| Oracle/SQL Server Equivalent           | `DESC table_name;` or `sp_help`     | Minimal differences in CLI commands, but same conceptual structure    | Similar approach but different commands                |

**Tiered Examples:**

- 🔍 **Beginner Example**:

  ```sql
  -- Example: Creating a simple table for storing basic customer info
  CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name  VARCHAR(50),
    last_name   VARCHAR(50)
  );
  /*
    Expected output:
    CREATE TABLE
  */
  -- Step-by-step:
  -- 1) customer_id is the primary key with auto-increment (SERIAL).
  -- 2) first_name, last_name are variable character columns of length 50.
  ```

- 🧩 **Intermediate Example**:

  ```sql
  -- Example: Using a custom schema
  CREATE SCHEMA support_team;

  CREATE TABLE support_team.ticket_logs (
    ticket_id SERIAL PRIMARY KEY,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW()
  );
  /*
    Expected output:
    CREATE SCHEMA
    CREATE TABLE
  */
  -- Relevance:
  -- 1) Separate schema for support_team to isolate resources.
  -- 2) TIMESTAMP column with default ensures we capture creation times.
  ```

- 💡 **SRE-Level Example**:

  ```sql
  -- Example: Creating a table for monitoring logs (with partitioning in PostgreSQL)
  CREATE TABLE monitoring_logs (
    log_id       BIGSERIAL PRIMARY KEY,
    log_message  TEXT,
    log_time     TIMESTAMP NOT NULL
  ) PARTITION BY RANGE (log_time);

  /*
    Expected output:
    CREATE TABLE
  */
  -- Context:
  -- For large-scale production logging, partitioning by time improves query performance and maintenance.
  ```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Use `\d table_name` in psql to examine table structure.
- 🧠 **Beginner Tip:** Start with small, clear tables rather than combining everything into one.
- 🔧 **SRE Insight:** Partitioning and indexing strategies are crucial for reliability and performance over time.
- 🔧 **SRE Insight:** Proper schema organization aids in incident triage, especially during on-call rotations.
- ⚠️ **Common Pitfall:** Creating tables without a primary key can lead to data ambiguity.
- ⚠️ **Common Pitfall:** Accidentally naming tables with special characters or reserved words can cause confusion.
- 🚨 **Security Note:** Limit permissions to create/alter tables in production. A single mistake can disrupt an entire system.
- 💡 **Performance Impact:** Large unindexed tables can cause high I/O and CPU usage.
- ☠️ **Career Risk:** Dropping or truncating the wrong table can be catastrophic—always double-check table names.
- 🧰 **Recovery Strategy:** Immediately restore from backups or point-in-time recovery if a critical table is dropped inadvertently.

---

### **Command/Concept: Primary Keys and Foreign Keys (Types, Constraints, Relationships)**

**Overview:**  
**Primary Keys (PK)** guarantee each row can be uniquely identified. **Foreign Keys (FK)** link rows between tables, ensuring referential integrity.

**Real-World Analogy:**  
A library system where **books** have unique ISBNs (primary key), and a **borrowing record** references the ISBN to track who borrowed which book (foreign key).

**Visual Representation:**

```text
Table: employees         Table: departments
┌────────────┬─────────┐   ┌────────────┬───────────────┐
│ emp_id(PK) │ name    │   │ dept_id(PK)│ dept_name     │
├────────────┼─────────┤   ├────────────┼───────────────┤
│ 1          │ Alice   │   │ 10         │ Accounting    │
│ 2          │ Bob     │   │ 20         │ HR            │
└────────────┴─────────┘   └────────────┴───────────────┘

employees.dept_id (FK) → departments.dept_id (PK)
```

**Syntax & Variations:**

| Syntax Form                               | Example                                                         | Description                                              | Support/SRE Usage Context                             |
|------------------------------------------ |---------------------------------------------------------------- |----------------------------------------------------------|--------------------------------------------------------|
| Defining PK in CREATE TABLE              | `PRIMARY KEY (column_name)`                                     | Marks a column as the unique identifier                 | Ensures consistent identification of rows             |
| Defining FK in CREATE TABLE              | `FOREIGN KEY (col) REFERENCES other_table(other_col)`           | Establishes link to PK in another table                 | Maintains data consistency across tables              |
| Adding FK constraint (PostgreSQL)        | `ALTER TABLE table_name ADD CONSTRAINT fk_name FOREIGN KEY (...)` | Used after table creation if you forgot an FK           | Fixing data consistency after initial design          |
| Oracle/SQL Server Differences            | Syntax mostly the same, but naming conventions vary             | Similar concept                                          | Minimally different for cross-platform support        |

**Tiered Examples:**

- 🔍 **Beginner Example**:

  ```sql
  -- Creating tables with a primary key and foreign key relationship
  CREATE TABLE departments (
    dept_id   SERIAL PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL
  );

  CREATE TABLE employees (
    emp_id    SERIAL PRIMARY KEY,
    emp_name  VARCHAR(100) NOT NULL,
    dept_id   INT REFERENCES departments(dept_id)
  );
  /*
    Expected output:
    CREATE TABLE
    CREATE TABLE
  */
  -- Step-by-step:
  -- 1) departments.dept_id is PK
  -- 2) employees.dept_id references the dept_id in departments
  ```

- 🧩 **Intermediate Example**:

  ```sql
  -- Adding a foreign key constraint after table creation
  ALTER TABLE employees
  ADD CONSTRAINT fk_employees_departments
  FOREIGN KEY (dept_id)
  REFERENCES departments (dept_id)
  ON DELETE CASCADE;
  /*
    Expected output:
    ALTER TABLE
  */
  -- Context:
  -- "ON DELETE CASCADE" ensures that if a department is deleted,
  -- all employees in that department are also deleted. Use carefully.
  ```

- 💡 **SRE-Level Example**:

  ```sql
  -- Example: Enforcing complex relationships with multiple columns
  CREATE TABLE order_items (
    order_id      INT,
    product_id    INT,
    quantity      INT,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE RESTRICT,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE RESTRICT
  );
  /*
    Expected output:
    CREATE TABLE
  */
  -- Context:
  -- Compound PK (order_id + product_id). FKs disallow deleting an order or product 
  -- if items exist, protecting data integrity in production systems.
  ```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Always define primary keys to keep track of unique records.
- 🧠 **Beginner Tip:** Start with simple one-column PKs before moving to composites.
- 🔧 **SRE Insight:** Foreign keys help maintain data integrity, crucial during high-stress incidents.
- 🔧 **SRE Insight:** Proper constraints reduce the chance of data drift, supporting consistent system states.
- ⚠️ **Common Pitfall:** Misusing `ON DELETE CASCADE` can unintentionally delete large amounts of data.
- ⚠️ **Common Pitfall:** Creating foreign keys without proper indexing can slow join queries significantly.
- 🚨 **Security Note:** Restrict user privileges to alter or drop key constraints in production.
- 💡 **Performance Impact:** FKs add overhead on insert/update. Evaluate indexing to offset potential slowdown.
- ☠️ **Career Risk:** Dropping or disabling a foreign key constraint can cause **massive data inconsistency**.
- 🧰 **Recovery Strategy:** Restore from backup or use carefully written scripts to fix orphaned data if constraints are removed by mistake.

---

### **Command/Concept: SELECT Statement (Basic Query Structure)**

**Overview:**  
`SELECT` is used to retrieve data from one or more tables. At its simplest, you specify **which columns** you want.

**Real-World Analogy:**  
Like **filtering** a spreadsheet to display only certain columns you’re interested in.

**Visual Representation:**

```text
┌────────────────────────────────────┐
│       SELECT columns FROM table    │
└────────────────────────────────────┘
                 │
                 ▼
         Results with only 
     the chosen columns displayed
```

**Syntax & Variations:**

| Syntax Form                 | Example                                     | Description                                         | Support/SRE Usage Context              |
|---------------------------- |-------------------------------------------- |-----------------------------------------------------|----------------------------------------|
| Basic SELECT (all columns)  | `SELECT * FROM customers;`                  | Returns all columns from a table                    | Quick data inspection                  |
| SELECT specific columns     | `SELECT first_name, last_name FROM customers;` | Retrieves only needed columns                      | Minimizes data transfer                |
| SELECT DISTINCT             | `SELECT DISTINCT dept_id FROM employees;`    | Removes duplicates                                  | Useful for quick category checks       |
| Oracle/SQL Server           | Same syntax for SELECT statements           | Minimal difference in basic usage                   | Cross-platform query consistency       |

**Tiered Examples:**

- 🔍 **Beginner Example**:

  ```sql
  -- Retrieve all data from the customers table
  SELECT * FROM customers;
  /*
    Expected output (sample):
    customer_id | first_name | last_name
    ------------+------------+----------
    1           | Alice      | Anderson
    2           | Bob        | Brown
    ...
  */
  -- Step-by-step:
  -- 1) '*' means all columns.
  -- 2) FROM indicates which table to read from.
  ```

- 🧩 **Intermediate Example**:

  ```sql
  -- Selecting specific columns to reduce clutter
  SELECT emp_name, dept_id
  FROM employees
  WHERE dept_id = 10;
  /*
    Expected output:
    emp_name  | dept_id
    ----------+---------
    Alice     | 10
    ...
  */
  -- Relevance:
  -- 1) We only fetch the columns we need.
  -- 2) We add a WHERE clause to focus on employees in department 10.
  ```

- 💡 **SRE-Level Example**:

  ```sql
  -- Using an aggregate function and grouping
  SELECT dept_id, COUNT(*) AS employee_count
  FROM employees
  GROUP BY dept_id
  HAVING COUNT(*) > 5;
  /*
    Expected output (sample):
    dept_id | employee_count
    --------+---------------
    10      | 6
    30      | 7
  */
  -- Context:
  -- For an SRE, grouping helps measure departmental load or usage metrics in real time.
  -- HAVING is used for filtering groups.
  ```

**Instructional Notes:**

- 🧠 **Beginner Tip:** `SELECT *` is convenient but can cause performance overhead for large tables.
- 🧠 **Beginner Tip:** Return only the columns you need to reduce noise and confusion.
- 🔧 **SRE Insight:** Aggregations and grouping are crucial for monitoring metrics across many rows.
- 🔧 **SRE Insight:** Query only necessary fields to reduce memory/CPU usage and network bandwidth.
- ⚠️ **Common Pitfall:** Omitting WHERE can lead to huge result sets, harming performance.
- ⚠️ **Common Pitfall:** Using SELECT * in production can degrade query speed.
- 🚨 **Security Note:** Restrict who can run queries returning sensitive columns (e.g., personal data).
- 💡 **Performance Impact:** Full table scans for large datasets can spike CPU and I/O usage.
- ☠️ **Career Risk:** Running an unbounded SELECT in production might saturate resources and cause an outage.
- 🧰 **Recovery Strategy:** Cancel the query (e.g., `pg_cancel_backend` in PostgreSQL) if it’s hogging resources; follow up with indexing or narrower column selection.

---

### **Command/Concept: FROM Clause (Table Specification)**

**Overview:**  
`FROM` specifies **which table** (or tables) the SELECT will read data from. In multi-table queries, `FROM` can combine tables with **JOIN** keywords.

**Real-World Analogy:**  
When you filter a spreadsheet, you pick **which sheet** you’re looking at.

**Visual Representation:**

```sql
SELECT column_list
FROM table_name(s)
      JOIN ...
WHERE conditions
```

**Syntax & Variations:**

| Syntax Form            | Example                                  | Description                                 | Support/SRE Usage Context            |
|----------------------- |----------------------------------------- |---------------------------------------------|--------------------------------------|
| Single Table FROM      | `SELECT * FROM employees;`               | Reads all rows from one table               | Common for basic troubleshooting     |
| Multiple Tables (JOIN) | `SELECT * FROM employees e JOIN departments d ON e.dept_id = d.dept_id;` | Reads data combining two tables | Investigating data across relationships |
| Subquery in FROM       | `SELECT * FROM (SELECT * FROM employees WHERE dept_id=10) AS sub;`        | A query inside a query                      | Advanced scenario analysis           |

**Tiered Examples:**

- 🔍 **Beginner Example**:

  ```sql
  -- Single table
  SELECT * FROM employees;
  /*
    Expected output: all rows from the employees table
  */
  -- Step-by-step: The FROM clause here simply says "read from employees".
  ```

- 🧩 **Intermediate Example**:

  ```sql
  -- Joining employees and departments
  SELECT e.emp_name, d.dept_name
  FROM employees e
  JOIN departments d ON e.dept_id = d.dept_id;
  /*
    Expected output (sample):
    emp_name  | dept_name
    ----------+----------
    Alice     | Accounting
    Bob       | HR
    ...
  */
  -- Relevance:
  -- 1) Shows how to link data across tables using the dept_id foreign key.
  -- 2) Common for troubleshooting cross-functional data issues.
  ```

- 💡 **SRE-Level Example**:

  ```sql
  -- Subquery-based approach to isolate a complex condition
  SELECT e.emp_name, e.dept_id
  FROM (
    SELECT emp_name, dept_id
    FROM employees
    WHERE dept_id IN (10, 20, 30)
  ) AS filtered_employees e
  WHERE e.dept_id = 20;
  /*
    Expected output:
    emp_name  | dept_id
    ----------+---------
    [Employees in dept 20]
  */
  -- Context:
  -- Subqueries can help performance or clarity for advanced filtering logic.
  ```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Start with single-table FROM before venturing into joins.
- 🧠 **Beginner Tip:** Use aliases (`e`, `d`) for readability.
- 🔧 **SRE Insight:** Multi-table joins can reveal hidden relationships or data anomalies.
- 🔧 **SRE Insight:** Subqueries might be easier to read but can sometimes affect performance—benchmark carefully.
- ⚠️ **Common Pitfall:** Joins without a proper condition can create a massive Cartesian product.
- ⚠️ **Common Pitfall:** Missing or incorrect ON clauses produce unintended or incorrect results.
- 🚨 **Security Note:** For highly sensitive joins (e.g., PII data), consider row-level permissions.
- 💡 **Performance Impact:** Joins can be CPU/IO heavy if not indexed properly.
- ☠️ **Career Risk:** A bad join on production could lock tables or bring down performance.
- 🧰 **Recovery Strategy:** Cancel long-running queries, then add indexes or refine your join conditions.

---

### **Command/Concept: WHERE Clause (Basic Filtering)**

**Overview:**  
`WHERE` filters rows based on specified conditions. It’s a cornerstone for focusing on relevant data and preventing massive scans.

**Real-World Analogy:**  
When searching in a spreadsheet for only rows where **“Status = Open”** to find open tickets.

**Visual Representation:**

```sql
SELECT columns
FROM table
WHERE condition(s)
```
  
**Syntax & Variations:**

| Syntax Form      | Example                                           | Description                               | Support/SRE Usage Context           |
|----------------- |-------------------------------------------------- |-------------------------------------------|-------------------------------------|
| Basic Comparison | `WHERE amount > 1000`                             | Filters rows based on a numeric condition | Common filtering scenario           |
| String Matching  | `WHERE first_name = 'Alice'`                      | Filters by exact match                    | Searching for a known record        |
| Partial Match    | `WHERE last_name LIKE 'Br%'`                      | Finds strings starting with 'Br'          | Quick lookups for partial matches   |
| Logical Operators| `WHERE dept_id = 10 OR dept_id = 20`              | Combines conditions with AND/OR           | Handling multiple conditions        |

**Tiered Examples:**

- 🔍 **Beginner Example**:

  ```sql
  -- Filtering employees by a single dept_id
  SELECT emp_id, emp_name
  FROM employees
  WHERE dept_id = 10;
  /*
    Expected output (sample):
    emp_id | emp_name
    -------+---------
       1   | Alice
  */
  -- Step-by-step: 
  -- 1) Only rows where dept_id = 10 are returned.
  -- 2) Great for verifying specific records.
  ```

- 🧩 **Intermediate Example**:

  ```sql
  -- Filtering on a range using numeric comparison
  SELECT customer_id, amount
  FROM orders
  WHERE amount >= 300 AND amount <= 1000;
  /*
    Expected output (sample):
    customer_id | amount
    ------------+-------
      101       | 500
      102       | 300
  */
  -- Relevance:
  -- 1) Helps narrow down records in typical support ticket queries.
  -- 2) Efficient for diagnosing transactions in a certain range.
  ```

- 💡 **SRE-Level Example**:

  ```sql
  -- Performance-based filtering
  EXPLAIN ANALYZE
  SELECT order_id, amount
  FROM orders
  WHERE amount > 1000
  AND order_date > CURRENT_DATE - INTERVAL '30 days';
  /*
    Expected output:
    Actual query plan showing index usage, cost, row count, etc.
  */
  -- Context:
  -- Checking cost and performance. For SRE, "EXPLAIN ANALYZE" is key to query tuning.
  ```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Always use WHERE to limit result sets—avoid retrieving everything unless you truly need it.
- 🧠 **Beginner Tip:** Use logical operators (AND, OR) to refine filters further.
- 🔧 **SRE Insight:** Combining WHERE with indexing drastically reduces resource usage.
- 🔧 **SRE Insight:** Query plan analysis is your friend; it reveals whether you’re scanning entire tables or using indexes.
- ⚠️ **Common Pitfall:** Using `=` for partial matches or forgetting quotes around strings leads to errors or no results.
- ⚠️ **Common Pitfall:** Overly complex WHERE clauses hamper performance if not indexed properly.
- 🚨 **Security Note:** Parameterize user inputs to avoid SQL injection vulnerabilities (`WHERE` is a common injection point).
- 💡 **Performance Impact:** Proper indexing on filtered columns is critical to reduce full-table scans.
- ☠️ **Career Risk:** A single missing `WHERE` in an UPDATE or DELETE can destroy entire data sets.
- 🧰 **Recovery Strategy:** Stop or rollback the transaction as soon as possible if a mistaken filter is used; rely on backups or point-in-time recovery if data is incorrectly updated or deleted.

---

### **Command/Concept: Database Connection (Connecting to PostgreSQL)**

**Overview:**  
Connecting to a PostgreSQL database is the first step before running any SQL commands. It often involves specifying a hostname, port, database name, username, and password.

**Real-World Analogy:**  
Like **logging into** your email before you can read or send messages.

**Visual Representation:**

```text
[Local/Remote]       [Database Service]
   psql   ----->   (PostgreSQL instance)
     \              
      \-> Auth check (user, password)
       \-> Access database (schema, tables)
```

**Syntax & Variations:**

| Syntax Form                           | Example                                              | Description                                                | Support/SRE Usage Context          |
|-------------------------------------- |----------------------------------------------------- |------------------------------------------------------------|------------------------------------|
| psql CLI Connection                  | `psql -h localhost -p 5432 -U myuser -d mydatabase`  | Connects to Postgres on default port 5432                  | Common approach for quick tasks    |
| Connection String (PG URI)           | `postgresql://myuser:mypass@localhost:5432/mydatabase` | URI format used in many applications                      | Useful for scripts & config files  |
| Oracle/SQL Server Connection         | Oracle uses `sqlplus user/pass@host:port/dbname` etc. | Similar concept, different tools/syntax                    | Minimal differences in structure   |

**Tiered Examples:**

- 🔍 **Beginner Example**:

  ```bash
  # Command line: 
  psql -h localhost -U postgres -d training_db
  # Expected Output:
  # psql (PostgreSQL version info)
  # Type "help" for help.
  # training_db=>
  # Explanation:
  # 1) Host is localhost.
  # 2) Username: postgres (the default superuser).
  # 3) Database: training_db.
  ```

- 🧩 **Intermediate Example**:

  ```bash
  # Using a URI-style connection for automation
  psql "postgresql://support_user:Support#123@dbserver.example.com:5432/support_db"
  # Explanation:
  # This approach is often used in CI/CD pipelines or application configs.
  ```

- 💡 **SRE-Level Example**:

  ```bash
  # Using environment variables for secure connections and advanced parameters
  export PGHOST=dbserver.prod.example.com
  export PGPORT=6432
  export PGUSER=sre_admin
  export PGPASSWORD='SecretProdPass!'
  psql -d production_db --set sslmode=require
  # Explanation:
  # 1) Environment variables keep credentials out of command history.
  # 2) Non-default port (6432) might be behind a load balancer or pgbouncer.
  # 3) SSL is required for secure production traffic.
  ```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Don’t store your database password in plain text. Use environment variables or secure password files.
- 🧠 **Beginner Tip:** Confirm the correct database name—many new users mix up the database and schema name.
- 🔧 **SRE Insight:** Tools like `pgbouncer` or `pgpool` can help manage connections in high-traffic environments.
- 🔧 **SRE Insight:** Monitor connection counts to avoid maxing out concurrent connections.
- ⚠️ **Common Pitfall:** Using the superuser account for routine tasks is risky—create separate roles.
- ⚠️ **Common Pitfall:** Hard-coding credentials in scripts can lead to security breaches.
- 🚨 **Security Note:** Always encrypt connections, especially outside local networks (`sslmode=require`).
- 💡 **Performance Impact:** Each connection consumes resources; for large-scale systems, pooling is essential.
- ☠️ **Career Risk:** Exposing database credentials in logs or code commits can cause severe security incidents.
- 🧰 **Recovery Strategy:** Rotate credentials immediately if exposed; audit logs for suspicious activity.

---

## 🛠️ System Effects Section

All the commands you’ve learned can affect your database in various ways:

1. **Resource Utilization**:
   - Full table scans spike CPU and disk I/O usage.
   - Large result sets can saturate network bandwidth.

2. **Concurrency and Locks**:
   - Simple `SELECT` queries typically use shared locks.
   - Creating or altering tables can escalate lock levels, blocking other transactions.

3. **Performance Metrics**:
   - Watch for `buffer_hits`, `disk_reads`, `rows_returned`, and query execution times.
   - Use `EXPLAIN (ANALYZE, BUFFERS)` in PostgreSQL for deeper insights.

4. **Monitoring**:
   - Track slow queries in PostgreSQL logs or use extension views like `pg_stat_activity`.
   - Set up alerts for locked transactions or connection saturation.

5. **Warnings**:
   - Large or complex queries might degrade overall system performance if concurrency is high.
   - Unused indexes or poor table design can cause high memory usage and slow writes.

**SRE Perspective**: Always consider how each query scales under load. Evaluate concurrency, watch for locking patterns, and proactively monitor resource usage to maintain reliability.

---

## 🖼️ Day 1 Visual Learning Aids

Below are **four** specific visual aids to reinforce Day 1 concepts:

### 1. **Relational Database Structure**  

A conceptual diagram showing **schemas, tables, columns, and rows**:

```text
┌──────── Database: training_db ────────┐
│   Schema: public                      │
│   ┌────────── Table: customers ─────┐ │
│   │ customer_id (PK)                │ │
│   │ first_name                      │ │
│   │ last_name                       │ │
│   └─────────────────────────────────┘ │
│   ┌────────── Table: orders ────────┐ │
│   │ order_id (PK)                   │ │
│   │ customer_id (FK)                │ │
│   │ amount                          │ │
│   └─────────────────────────────────┘ │
└───────────────────────────────────────┘
```

### 2. **Primary/Foreign Key Relationship**  
```text
  customers                     orders
┌─────────────────┐        ┌─────────────────┐
│ customer_id(PK) │ 1 ---> │ customer_id(FK) │
│ first_name      │        │ order_id(PK)    │
│ last_name       │        │ amount          │
└─────────────────┘        └─────────────────┘
```

### 3. **SQL Query Flow**  

Step-by-step representation of how a **SELECT** query is processed:

```text
SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY
   |        |       |         |         |           |
   |        |       ---- Filter rows    |           |
   |        ---- Identify table(s)      ---- Filter groups
   ---- Choose columns                         ---- Sort final result
```

### 4. **Database Schema Example**  

A small schema with multiple linked tables:

```text
public schema
├── customers
│   ├── customer_id (PK)
│   ├── first_name
│   ├── last_name
│   └── created_at
├── orders
│   ├── order_id (PK)
│   ├── customer_id (FK) -> customers.customer_id
│   ├── amount
│   └── order_date
└── products
    ├── product_id (PK)
    ├── product_name
    └── price
```

---

## 🔨 Day 1 Hands-On Exercises

We have **3 exercises** for each tier.

### 🔍 Beginner Exercises

1. **Database Connection Exercise**  
   - **Goal**: Connect to a local PostgreSQL database named `training_db`.
   - **Instructions**:
     1. Open terminal and run:  

        ```bash
        psql -h localhost -U postgres -d training_db
        ```

     2. Verify successful connection by listing tables with `\dt`.

2. **Basic SELECT Exercise**  
   - **Goal**: Practice retrieving data from a single table.
   - **Instructions**:
     1. In `psql`, run:  

        ```sql
        SELECT * FROM customers;
        ```

     2. Note the columns returned.  
     3. Optionally, try selecting specific columns:

        ```sql
        SELECT customer_id, first_name FROM customers;
        ```

3. **Simple WHERE Filter Exercise**  
   - **Goal**: Retrieve records based on a condition.
   - **Instructions**:
     1. Run:

        ```sql
        SELECT customer_id, first_name 
        FROM customers 
        WHERE customer_id <= 3;
        ```

     2. Observe how only rows matching `customer_id <= 3` appear.

### 🧩 Intermediate Exercises

1. **Multi-Table Exploration**  
   - **Goal**: Identify relationships between tables using primary/foreign keys.
   - **Instructions**:
     1. Examine the `orders` table structure with `\d orders`.
     2. Notice the `customer_id` column referencing `customers(customer_id)`.
     3. Write a query to join both tables:

        ```sql
        SELECT c.first_name, c.last_name, o.amount
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id;
        ```

2. **Column Selection and Filtering**  
   - **Goal**: Write optimized queries selecting only needed columns.
   - **Instructions**:
     1. Query the `orders` table for orders greater than `$200`:

        ```sql
        SELECT order_id, amount
        FROM orders
        WHERE amount > 200;
        ```

     2. Compare this approach to `SELECT * FROM orders;` to see the difference in returned data volume.

3. **Support Scenario Query**  
   - **Goal**: Simulate a request from a support ticket for a specific customer’s data.
   - **Instructions**:
     1. Imagine a ticket says “Customer with ID 2 can’t see their latest order.”
     2. Write:

        ```sql
        SELECT c.first_name, c.last_name, o.order_id, o.amount 
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        WHERE c.customer_id = 2;
        ```

     3. Check if any rows are returned. If none, investigate foreign key relationships or data entry issues.

### 💡 SRE-Level Exercises

1. **Query Performance Analysis**  
   - **Goal**: Examine execution plans for a SELECT statement.
   - **Instructions**:
     1. Identify a table with enough data to matter (e.g., `orders`).
     2. Run:

        ```sql
        EXPLAIN ANALYZE
        SELECT order_id, amount
        FROM orders
        WHERE amount > 300;
        ```

     3. Analyze the cost, rows, and time. Consider adding an index on `amount`.

2. **Data Relationship Verification**  
   - **Goal**: Check referential integrity between `customers` and `orders`.
   - **Instructions**:
     1. Run:

        ```sql
        SELECT o.order_id
        FROM orders o
        LEFT JOIN customers c ON o.customer_id = c.customer_id
        WHERE c.customer_id IS NULL;
        ```

     2. Investigate any results indicating **orphaned** orders referencing a non-existent customer.

3. **Monitoring Setup**  
   - **Goal**: Configure basic query performance monitoring.
   - **Instructions**:
     1. Enable the `pg_stat_statements` extension if available:

        ```sql
        CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
        ```

     2. View the top queries by total time:

        ```sql
        SELECT query, calls, total_time
        FROM pg_stat_statements
        ORDER BY total_time DESC
        LIMIT 5;
        ```

     3. Identify any slow queries and explore indexing or rewriting them.

---

## 📝 Knowledge Check Quiz

We have **4 questions per tier**, totaling **12** questions. Each includes **multiple-choice options** (4 each) and **explanations**.

### 🔍 Beginner Questions (4)

1. **Which statement best describes a table in a relational database?**  
   A) A single row containing all data  
   B) A structured collection of columns and rows  
   C) A type of index that speeds up queries  
   D) A database backup file  
   - **Correct Answer**: B  
     - **Explanation**: A table organizes data into rows (records) and columns (attributes).  
   - **Incorrect Answers**:  
     - A) A single row is just one record, not a full table  
     - C) Indexes are separate structures for performance  
     - D) Backups are outside the live schema  
   - **Work Relevance**: Understanding table structure is step one in writing correct queries.

2. **What is the role of a primary key?**  
   A) Identifies a row uniquely in a table  
   B) Helps define column data types  
   C) Connects two different tables  
   D) Automatically encrypts sensitive data  
   - **Correct Answer**: A  
     - **Explanation**: Primary keys ensure each row has a unique identifier.  
   - **Incorrect Answers**:  
     - B) Data types are defined at column creation  
     - C) That’s a foreign key’s purpose  
     - D) Not related to encryption  
   - **Work Relevance**: Proper PK usage ensures you can find specific rows for troubleshooting.

3. **Which clause specifies the source table in a query?**  
   A) WHERE  
   B) SELECT  
   C) FROM  
   D) SCHEMA  
   - **Correct Answer**: C  
     - **Explanation**: `FROM` indicates the table(s) from which data is being retrieved.  
   - **Incorrect Answers**:  
     - A) WHERE filters data  
     - B) SELECT chooses columns  
     - D) SCHEMA organizes tables but isn’t a query clause  
   - **Work Relevance**: Always verify the correct table is in the FROM clause before running queries.

4. **Which command is used to connect to a PostgreSQL database from the command line?**  
   A) `mysql`  
   B) `psql`  
   C) `sqlplus`  
   D) `sqlserver`  
   - **Correct Answer**: B (`psql`)  
   - **Incorrect Answers**:  
     - A) `mysql` is for MySQL  
     - C) `sqlplus` is for Oracle  
     - D) Not a standard SQL Server CLI  
   - **Work Relevance**: Connection knowledge is essential before any query writing.

---

### 🧩 Intermediate Questions (4)

1. **What does the `JOIN` keyword accomplish in a SQL query?**  
   A) It updates rows in multiple tables  
   B) It retrieves data from multiple tables based on a related column  
   C) It deletes data from a table  
   D) It creates a new table based on existing data  
   - **Correct Answer**: B  
     - **Explanation**: Joins combine rows from different tables based on matching columns (often PK-FK).  
   - **Incorrect Answers**:  
     - A) `UPDATE` modifies existing rows  
     - C) `DELETE` removes rows  
     - D) `CREATE TABLE` or `SELECT INTO` can create new tables  
   - **Work Relevance**: Frequently used when investigating cross-table data issues in support.

2. **Why might you add an `ON DELETE CASCADE` clause to a foreign key constraint?**  
   A) To ensure that deleting a parent record also deletes all related child records  
   B) To prevent the child records from ever being deleted  
   C) To automatically encrypt the child table  
   D) To drastically speed up SELECT queries  
   - **Correct Answer**: A  
     - **Explanation**: `ON DELETE CASCADE` ensures child records are removed when the parent is removed.  
   - **Incorrect Answers**:  
     - B) This does the opposite  
     - C) Not related to encryption  
     - D) It doesn’t necessarily speed up SELECT queries  
   - **Work Relevance**: Carefully consider if such cascading deletes are desired in your environment.

3. **Which of the following is a benefit of selecting only specific columns rather than using `SELECT *`?**  
   A) It guarantees faster queries for all databases in every scenario  
   B) It prevents SQL injection attacks automatically  
   C) It reduces data transfer and can improve performance  
   D) It automatically indexes the table  
   - **Correct Answer**: C  
     - **Explanation**: Selecting fewer columns generally means less data transfer, often improving performance.  
   - **Incorrect Answers**:  
     - A) Usually faster, but not guaranteed in every scenario  
     - B) Doesn’t prevent injection on its own  
     - D) Indexing is a separate action  
   - **Work Relevance**: Vital for optimizing queries in a support environment with large tables.

4. **Which statement about subqueries is accurate?**  
   A) They must always be correlated with the outer query  
   B) They are primarily used to create new tables  
   C) They can appear in the FROM or WHERE clause to filter or reshape data  
   D) They only work on Oracle, not PostgreSQL  
   - **Correct Answer**: C  
     - **Explanation**: Subqueries can appear in various clauses for data filtering or shaping.  
   - **Incorrect Answers**:  
     - A) Some subqueries are correlated, some are not  
     - B) `CREATE TABLE` is for new tables  
     - D) PostgreSQL fully supports subqueries  
   - **Work Relevance**: Subqueries can simplify complex queries or break them into understandable chunks.

---

### 💡 SRE-Level Questions (4)

1. **How can you identify if a SELECT query is doing a full table scan in PostgreSQL?**  
   A) By checking the `pg_tables` catalog for row counts  
   B) By using `EXPLAIN ANALYZE` and looking for `Seq Scan`  
   C) By checking environment variables for psql  
   D) By running `DROP TABLE` and seeing if it completes quickly  
   - **Correct Answer**: B  
     - **Explanation**: `EXPLAIN ANALYZE` reveals query plan details, including sequential scans.  
   - **Incorrect Answers**:  
     - A) That only shows table metadata, not query execution details  
     - C) Environment variables do not show query plan info  
     - D) Extremely risky and unrelated  
   - **Work Relevance**: SREs must diagnose performance issues by analyzing query plans.

2. **Which metric would best indicate your database is saturated with SELECT queries?**  
   A) A high number of user sessions reading from logs  
   B) Low CPU usage and stable disk I/O  
   C) Long running queries with high CPU and I/O usage seen in `pg_stat_activity`  
   D) Low memory usage on the database server  
   - **Correct Answer**: C  
     - **Explanation**: Long running queries consuming CPU/I/O point to saturation.  
   - **Incorrect Answers**:  
     - A) Merely reading logs isn’t an indication of saturation  
     - B) Low CPU/disk I/O is the opposite sign  
     - D) Low memory usage could indicate minimal load  
   - **Work Relevance**: Tying queries to system resource usage helps detect performance bottlenecks.

3. **What is the purpose of partitioning a table by a time-based column?**  
   A) It encrypts old data automatically  
   B) It moves old data to a different database engine  
   C) It organizes data into smaller chunks, improving query and maintenance efficiency  
   D) It creates an index on every column automatically  
   - **Correct Answer**: C  
     - **Explanation**: Partitioning can speed queries on time ranges and eases maintenance.  
   - **Incorrect Answers**:  
     - A/B/D) Partitioning does not provide encryption, cross-engine data movement, or auto-indexing  
   - **Work Relevance**: Critical for large data sets and SRE monitoring logs.

4. **How can you quickly stop a runaway SELECT query in PostgreSQL that’s harming performance?**  
   A) Restart the database server  
   B) Cancel the backend process using `pg_cancel_backend(pid)`  
   C) Kill all user sessions with `pg_terminate_backend()`  
   D) Delete the table being queried  
   - **Correct Answer**: B  
     - **Explanation**: `pg_cancel_backend(pid)` stops the query gracefully without a full server restart.  
   - **Incorrect Answers**:  
     - A) Risky and affects all users  
     - C) Overly drastic, kills all sessions (may be needed in extreme emergencies only)  
     - D) Destroys data permanently, obviously not a valid approach  
   - **Work Relevance**: SREs must handle performance emergencies swiftly without causing further damage.

---

## 🚧 Day 1 Troubleshooting Scenarios

1. **Scenario: "Missing Data" Misconception**  
   - **Symptom**: A support analyst says “We can’t find the record for customer ID 5!”  
   - **Possible Causes**:  
     - WHERE clause too restrictive  
     - Typo in table or column name  
     - The data actually exists in a related table (FK misunderstanding)  
   - **Diagnostic Approach**:  
     1. Double-check the table name: `\d customers`.  
     2. Run a broad SELECT: `SELECT * FROM customers WHERE customer_id = 5;`  
     3. Check related tables if not found.  
   - **Resolution Steps**:  
     - Correct the query or table reference.  
     - If foreign key relationships exist, ensure you’re querying the correct table.  
   - **Prevention Strategy**:  
     - Maintain a proper data dictionary so the support team knows which tables hold which information.  
   - **Knowledge Connection**:  
     - Ties directly to basic table structure and primary/foreign keys.  
   - **SRE Metrics**:  
     - Watch for `no_data_found` or similar error logs that might indicate query or schema issues.

2. **Scenario: Slow Query Performance**  
   - **Symptom**: A basic SELECT query “takes forever.”  
   - **Possible Causes**:  
     - Missing or no WHERE clause retrieving the entire table  
     - Selecting unnecessary columns with `SELECT *`  
     - Heavy load on the database from other processes  
   - **Diagnostic Approach**:  
     - Check query plan with `EXPLAIN ANALYZE`  
     - Verify indexing on the columns used in WHERE  
     - Check `pg_stat_activity` for concurrency conflicts  
   - **Resolution Steps**:  
     - Add filters or indexes  
     - Avoid `SELECT *`; specify only needed columns  
     - Investigate parallel load or maintenance tasks  
   - **Prevention Strategy**:  
     - Good query hygiene from Day 1; index high-use columns  
   - **Knowledge Connection**:  
     - Ties to SELECT, FROM, WHERE, and indexing fundamentals  
   - **SRE Metrics**:  
     - Query execution time, I/O usage, CPU load

3. **Scenario: Connection Issues**  
   - **Symptom**: Unable to connect to the sample PostgreSQL database.  
   - **Possible Causes**:  
     - Wrong credentials or connection string  
     - Network/firewall settings blocking the port  
     - PostgreSQL service is down  
   - **Diagnostic Approach**:  
     1. Test local connection: `psql -U user -d dbname`  
     2. Check `pg_hba.conf` and firewall rules  
     3. Verify `systemctl status postgresql` (Linux) or service status on Windows  
   - **Resolution Steps**:  
     - Correct credentials/connection string  
     - Open firewall port or fix routing  
     - Start PostgreSQL service if stopped  
   - **Prevention Strategy**:  
     - Document correct connection parameters; keep environment configs up to date  
   - **Knowledge Connection**:  
     - Relates to the “Database Connection” lab  
   - **SRE Metrics**:  
     - Monitoring connection counts, service availability, logs for authentication failures

---

## ❓ Frequently Asked Questions

Below are **3 FAQs per tier**, **total 9**.

### 🔍 Beginner FAQs

1. **Q**: Do I need to memorize all SQL syntax to start working with databases?  
   **A**: Not at all. Focus on basics—SELECT, FROM, WHERE, primary keys. You can learn more advanced syntax as you go.

2. **Q**: What’s the easiest way to see a table’s columns in PostgreSQL?  
   **A**: Use `\d table_name` in the `psql` tool or a GUI like pgAdmin.

3. **Q**: Why can’t I delete a row from a table with a foreign key constraint?  
   **A**: The foreign key is likely protecting related data. You may need `ON DELETE CASCADE` or remove child rows first.

### 🧩 Intermediate FAQs

1. **Q**: Should every table have a primary key?  
   **A**: In almost all cases, **yes**. A primary key prevents duplicate rows and simplifies data referencing and troubleshooting.

2. **Q**: How do I see which user roles can access my table?  
   **A**: Use PostgreSQL’s `\du` to list roles and check GRANTs with `\z table_name` or relevant system catalogs.

3. **Q**: What’s the difference between `JOIN` and `LEFT JOIN`?  
   **A**: A `JOIN` (often `INNER JOIN`) returns rows that match in both tables. A `LEFT JOIN` returns **all rows** from the left table, plus matching rows from the right table.

### 💡 SRE-Level FAQs

1. **Q**: How do I monitor long-running queries automatically?  
   **A**: Use the `pg_stat_activity` view or extensions like `pg_stat_statements` with scheduled checks/alerts (e.g., Prometheus + Grafana or specialized DB monitoring tools).

2. **Q**: When do I choose partitioning vs. indexing for large tables?  
   **A**: If data grows by time or a specific range, partitioning helps manage data in chunks. Indexing is for faster lookups. Often you **combine** both strategies for optimal performance.

3. **Q**: How do I approach capacity planning for my database?  
   **A**: Estimate growth in data size, concurrency, query patterns. Monitor usage metrics (CPU, memory, I/O). Plan index or partition strategies and test with production-like workloads.

---

## 🔥 Support/SRE Scenario

**Detailed Incident**: A customer complains of extremely slow order lookups in a production environment. We suspect a missing index and a large dataset.

### Steps (5-7 explicit actions)

1. **Check Active Queries**  

   ```sql
   SELECT pid, usename, query, state, query_start
   FROM pg_stat_activity
   WHERE state = 'active';
   ```

   - **Reasoning**: Identify if multiple long-running SELECT queries are piling up.  
   - **SRE Principle**: Observability. Checking `pg_stat_activity` reveals real-time usage.

2. **EXPLAIN ANALYZE**  

   ```sql
   EXPLAIN ANALYZE
   SELECT order_id, customer_id, amount
   FROM orders
   WHERE amount > 1000
     AND order_date > CURRENT_DATE - INTERVAL '90 days';
   ```

   - **Reasoning**: Exposes whether a sequential scan or index usage is happening.  
   - **SRE Principle**: Reliability. Efficient queries ensure stable response times.

3. **Add Index**  

   ```sql
   CREATE INDEX idx_orders_amount_date 
     ON orders (amount, order_date);
   ```

   - **Reasoning**: We suspect the database is scanning all orders. This index should speed up the filtered query.  
   - **SRE Principle**: Performance optimization under production load.

4. **Re-run EXPLAIN ANALYZE**  

   ```sql
   EXPLAIN ANALYZE
   SELECT order_id, customer_id, amount
   FROM orders
   WHERE amount > 1000
     AND order_date > CURRENT_DATE - INTERVAL '90 days';
   ```

   - **Reasoning**: Confirm that the plan changed to an index scan.  
   - **SRE Principle**: Observability. Validate improvements with measurable data.

5. **Monitor Logs & Metrics**  
   - Check for improved query times and reduced CPU usage.  
   - **Reasoning**: Ensure the fix actually solves the user complaint.  
   - **SRE Principle**: Post-incident review for reliability confirmation.

6. **Communicate to Stakeholders**  
   - Summarize the root cause (missing index) and resolution to the support team and management.  
   - **Reasoning**: Clear, consistent updates maintain trust and knowledge sharing.  
   - **SRE Principle**: Incident management and accountability.

7. **Document in Runbook**  
   - Add a “Slow Query” section to the internal knowledge base with these steps.  
   - **Reasoning**: Recurring issues demand thorough documentation for future on-call engineers.  
   - **SRE Principle**: Continuous improvement.

---

## 🧠 Key Takeaways

1. **Command/Concept Summary**:  
   - **Tables** organize data into rows/columns, **PK** uniquely identifies rows, **FK** enforces relationships, **SELECT** reads data, **WHERE** filters records, and **FROM** specifies sources.

2. **Command/Concept Summary**:  
   - **Joins** are essential for retrieving linked data. **EXPLAIN** reveals performance details.

3. **Command/Concept Summary**:  
   - **Connection** knowledge is foundational. Don’t forget security best practices.

4. **Command/Concept Summary**:  
   - **Schemas** help organize data logically. Keep them consistent and well-named.

5. **Command/Concept Summary**:  
   - **Indexes** are vital for performance but can slow writes; use them wisely.

---

### 3 Operational Insights for Reliability

1. **Monitor Query Plans**: Use `EXPLAIN` regularly to spot potential performance pitfalls.  
2. **Enforce Constraints**: Primary and foreign keys preserve data integrity under heavy load.  
3. **Validate Production Queries**: Keep an eye on concurrency levels to avoid lock contention.

---

### 3 Best Practices for Performance

1. **Use SELECT columns** instead of `SELECT *`.  
2. **Index high-usage columns** for common WHERE filters.  
3. **Partition large tables** by date or usage patterns if appropriate.

---

### 3 Critical Warnings or Pitfalls

1. **Missing WHERE** in UPDATE/DELETE is the classic catastrophic mistake.  
2. **ON DELETE CASCADE** can remove large chunks of data—use caution.  
3. **Overusing subqueries** without indexing can degrade performance.

---

### 3 Monitoring Recommendations

1. **pg_stat_activity**: Monitor active queries, concurrency, locks.  
2. **pg_stat_statements**: Track query frequency and total time.  
3. **Alerts on slow queries**: Set thresholds to trigger alerts and logs for queries taking too long.

---

### Clear Connections to Support/SRE Excellence

- By mastering **basic relational concepts**, you reduce **MTTR (Mean Time to Recovery)** during incidents.  
- Good **query hygiene** preserves performance under peak loads.  
- Thorough **monitoring and observability** keep your environment healthy and minimize surprises.

---

## 🚨 Day 1 Career Protection Guide

**Focus**: Preventing critical mistakes while you’re still learning.

### High-Risk SELECT Operations

1. **SELECT * on huge tables**: Can cause massive resource usage.  
2. **No WHERE clause**: Returns all data, can lock or saturate the database.  
3. **SELECT with complex joins**: Risk of unintended cartesian products if join conditions are missing.

**Real-World Incident**:  

- A junior admin inadvertently ran `SELECT * FROM 10-million-row table` in production during peak load. Result? Database node choked, causing application timeouts.

**Warning Signs**:  

- Query runs unusually long, high disk I/O, CPU spikes.

---

### Verification Best Practices

1. **Use LIMIT** to test a query on a small subset.  
2. **Test in Dev/QA** before running in production.  
3. **Check EXPLAIN** or query plan for sanity.

---

### Recovery Strategies

1. **Cancel runaway queries** (`pg_cancel_backend`) if you see your query is harming performance.  
2. **Use backups** or **Point-in-Time Recovery** if data was incorrectly updated or locked.  
3. **Escalate** to senior DB admins if you suspect serious performance or data consistency issues.

---

### First-Day Safeguards

1. **Access Control**: Only read permissions on critical production tables.  
2. **Query Review**: Let a senior colleague verify complex queries.  
3. **Minimal Privileges**: Don’t log in as a superuser unless absolutely necessary.

---

## 🔮 Preview of Next Topic

Tomorrow, we’ll dive deeper into **joins, advanced WHERE clauses, and writing more efficient SQL queries**. You’ll learn about sorting, grouping, subqueries, and how to handle **JOIN** across multiple tables. Make sure to:

- Review Day 1’s fundamentals (primary/foreign keys, basic SELECT usage).
- Experiment with small queries so you can confidently handle larger or more complex queries on Day 2.
- Start thinking about **how multiple tables link together**—that’s our big next step.

---

## 📚 Day 1 Further Learning Resources

### 🔍 Beginner SQL & Relational Database Resources (3)

1. **[Official PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html)**  
   - **Focus**: Basic SQL and table creation.  
   - **Relevance**: Great intro for new support staff.  
   - **Time**: ~2–3 hours total.

2. **[Khan Academy: Intro to SQL](https://www.khanacademy.org/computing/computer-programming/sql)**  
   - **Focus**: Fundamentals of SELECT, WHERE, and data structure.  
   - **Relevance**: Interactive exercises, ideal for beginners.  
   - **Time**: ~2 hours of hands-on practice.

3. **[W3Schools SQL Tutorial](https://www.w3schools.com/sql/)**  
   - **Focus**: Quick reference for basic SQL commands.  
   - **Relevance**: Step-by-step instructions with simple examples.  
   - **Time**: ~1–2 hours for the basics.

---

### 🧩 Intermediate Relational Concepts Resources (3)

1. **[PostgreSQL Documentation on Joins](https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-JOIN)**  
   - **Focus**: Deeper exploration of JOIN types.  
   - **Relevance**: Connects to multi-table support scenarios.  
   - **Takeaway**: Understand left/right/inner/outer joins.

2. **[SQLBolt](https://sqlbolt.com/)**  
   - **Focus**: Interactive lessons with advanced queries.  
   - **Relevance**: Builds on basic queries, adding complexity.  
   - **Takeaway**: Hands-on approach to writing better SQL.

3. **[Database Normalization Guide](https://www.guru99.com/database-normalization.html)**  
   - **Focus**: Proper table design and relationships.  
   - **Relevance**: Prevent data redundancy, essential for stable support.  
   - **Takeaway**: Ties Day 1’s PK/FK concepts to intermediate normalization forms.

---

### 💡 SRE-Level Reliability Resources (3)

1. **[PostgreSQL Performance Tuning Wiki](https://wiki.postgresql.org/wiki/Performance_Optimization)**  
   - **Focus**: From indexing to partitioning and beyond.  
   - **Relevance**: Ties basic SQL knowledge to production reliability.  
   - **Value**: Real-world tips for preventing downtime.

2. **[Google SRE Book: Database Reliability Engineering Section](https://sre.google/sre-book/table-of-contents/)**  
   - **Focus**: High-level reliability concepts.  
   - **Relevance**: Connects database fundamentals to large-scale reliability.  
   - **Value**: Industry best practices.

3. **[PG Observability Tools Blog Series](https://www.percona.com/blog/?s=postgresql+observability)**  
   - **Focus**: Deep dive into monitoring queries, locks, and performance.  
   - **Relevance**: SRE perspective on measuring everything.  
   - **Value**: Detailed coverage of real production scenarios.

---

## 🎉 Closing Message

Congratulations on completing **Day 1** of this SRE Database training module! You’ve laid a solid foundation in **relational database fundamentals**—understanding how tables, primary/foreign keys, and basic SQL (SELECT, FROM, WHERE) work. You’ve also gained crucial insights into **career protection** (avoiding harmful queries) and **SRE principles** (monitoring, reliability, and performance).

Tomorrow, we’ll deepen these skills, tackling more complex **joins**, subqueries, and **advanced filtering** to further bolster your support and SRE capabilities. Keep experimenting with Day 1’s commands, and remember that **reliability** starts with a firm grasp of the **basics**.

Stay curious, keep exploring, and get ready for a richer dive into relational SQL tomorrow!

---

## End of Day 1: Core Relational Database Fundamentals & Basic SQL Queries
