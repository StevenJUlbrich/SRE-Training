# 🏗️ Day 3: Database Design Principles & Normalization (Oracle-Focused)

## 📌 Introduction

Welcome to Day 3 of your SRE Database Training! Today, we’ll build on the fundamentals you learned on Day 1 and the DML operations from Day 2, diving deeper into how to **design** your database effectively. Well-designed schemas aren’t just about aesthetics; they have a huge impact on **performance**, **data integrity**, and **maintenance**. A real-world example might be a support case where an application experiences sluggish queries due to excessive data redundancy. We’ll see how applying good design practices and normalization can drastically reduce these issues.

Below is a simple visual concept map for how design decisions link directly to overall system reliability:

```asciitet
[User Queries] --> [Schema Design] --> [Query Performance] --> [System Reliability]
                   ^              
                   | (Normalization)
```

Remember: database design is both **art** and **science**, balancing theoretical best practices with practical, real-world needs.

---

### 🎯 Learning Objectives by Tier

**🔍 Beginner**

1. Define key database design principles (clarity, consistency, non-redundancy, integrity)
2. Recognize the basics of Entity-Relationship (ER) modeling
3. Identify the requirements of First Normal Form (1NF)
4. Explain why normalization is essential for database support tasks

**🧩 Intermediate**

1. Differentiate between natural and surrogate keys in an Oracle environment
2. Apply 2NF and 3NF to remove partial and transitive dependencies
3. Understand common design mistakes and how to fix them in Oracle
4. Develop basic denormalization strategies when performance is a concern

**💡 Advanced/SRE**

1. Evaluate trade-offs between normalization and performance using Oracle AWR reports
2. Design index strategies for highly normalized schemas
3. Implement advanced denormalization techniques for enterprise-scale Oracle databases
4. Monitor and troubleshoot design-related performance issues using Oracle-specific tools

---

### 📚 Core Concepts

For each concept, we’ll use the following framework:

* **🔍 Beginner Analogy**
* **🖼️ Visual Representation**
* **🔬 Technical Explanation**
* **💼 Support/SRE Application**
* **🔄 System Impact**
* **⚠️ Common Misconceptions**
* **📊 Oracle Implementation**

---

### 💻 Day 3 Concept Breakdown

#### 1. Database Design Principles

1. **Clarity** – The schema should be easily understood. A good analogy (🔍) is like organizing your files into properly labeled folders at home.
2. **Consistency** – Consistent naming and data types ensure reliable operations.
3. **Non-Redundancy** – Avoid storing the same piece of data in multiple places.
4. **Integrity** – The data should accurately reflect real-world entities.

**🖼️ Visual Representation**:

```ascitext
+---------+    +-----------+   +--------------+ +-----------+
| Clarity |    |Consistency|   |Non-Redundancy| | Integrity |
+---------+    +-----------+   +--------------+ +-----------+
     |               |                 |              |
     | <------ Good Database Design Principles ----->|
```

**🔬 Technical Explanation**: These principles guide structure and relationships in the schema. Violations can lead to data anomalies and performance bottlenecks.

**💼 Support/SRE Application**: Properly designed schemas minimize the risk of data inconsistencies and reduce troubleshooting complexity.

**🔄 System Impact**: Good design yields more efficient queries and updates, improving reliability and speed.

**⚠️ Common Misconceptions**: Believing that design has minimal performance impact or that "database design is just for architects." In fact, support engineers need to understand design to diagnose issues.

**📊 Oracle Implementation**: Oracle’s Data Dictionary (e.g., `USER_TABLES`, `ALL_CONSTRAINTS`) provides ways to validate your schema’s structure. Tools like **Oracle SQL Developer** can also enforce naming conventions.

---

#### 2. Entity-Relationship Modeling

**🔍 Beginner Analogy**: Imagine you’re mapping relationships between people in a family tree.

**🖼️ Visual Representation (ASCII ER Diagram)**:

```asciitext
[ENTITY: Customer] --(places)--> [ENTITY: Order]
       |                          |
  (has attributes)            (has attributes)
```

**🔬 Technical Explanation**: ER modeling involves identifying **entities** (tables), their **attributes** (columns), and **relationships** (one-to-one, one-to-many, many-to-many).

**💼 Support/SRE Application**: Understanding ER diagrams helps quickly identify where performance issues might arise (e.g., in a many-to-many join table that’s poorly indexed).

**🔄 System Impact**: A well-structured ER model reduces join complexity and ensures the database can handle concurrency gracefully.

**⚠️ Common Misconceptions**: Over-simplifying relationships or not accounting for certain constraints, leading to orphan or duplicate records.

**📊 Oracle Implementation**: Oracle SQL Developer Data Modeler allows you to visually create and manipulate ERDs. You can also define relationships via **foreign keys** (`FOREIGN KEY (...) REFERENCES ...`).

---

#### 3. Keys and Constraints

**🔍 Beginner Analogy**: A key is like a unique government ID number; constraints are the rules that ensure data makes sense.

**🖼️ Visual Representation**:

```asciitext
      +--------+ Primary Key
      |        |  (Unique Row Identifier)
      V        V
    [Table: Employees]
      PK: EMP_ID
      +-------------+
      | EMP_ID (PK) |
      | NAME        |
      | DEPT_ID (FK)|
      +-------------+
```

**🔬 Technical Explanation**:

- **Natural Key**: Derived from real-world data (e.g., SSN)
- **Surrogate Key**: Artificial key (often an auto-generated number)
- **Constraints**: **PRIMARY KEY**, **FOREIGN KEY**, **UNIQUE**, **CHECK**, **NOT NULL**

**💼 Support/SRE Application**: Properly defined keys and constraints prevent data corruption, which is crucial in high-availability systems.

**🔄 System Impact**: Constraints enforce data integrity but add overhead during writes. SREs must balance integrity with performance.

**⚠️ Common Misconceptions**: Using only surrogate keys without proper unique constraints can lead to duplicate records.

**📊 Oracle Implementation**: Oracle’s constraint syntax includes:

```sql
ALTER TABLE employees
ADD CONSTRAINT pk_emp_id PRIMARY KEY (emp_id);
```

---

#### 4. First Normal Form (1NF)

**🔍 Beginner Analogy**: Each cell in a spreadsheet should hold **one** piece of data—like not listing multiple phone numbers in a single cell.

**🖼️ Visual Representation**:

```asciitext
UN-NORMALIZED:
| Person ID | Phone Numbers       |
|-----------|---------------------|
| 1         | 555-1234, 555-9876  |

1NF:
| Person ID | Phone Number |
|-----------|-------------|
| 1         | 555-1234    |
| 1         | 555-9876    |
```

**🔬 Technical Explanation**: Requires atomic (indivisible) columns, no repeating groups.

**💼 Support/SRE Application**: Avoid storing multiple values in a single column to simplify queries.

**🔄 System Impact**: The DB can handle updates and searches more efficiently, especially when indexing.

**⚠️ Common Misconceptions**: Believing “1NF” means “one table.” In reality, 1NF focuses on atomicity.

**📊 Oracle Implementation**: For multi-value attributes, create a separate child table. Ensuring 1NF is often the first step in designing an Oracle schema.

---

#### 5. Second Normal Form (2NF)

**🔍 Beginner Analogy**: If a spreadsheet row depends on only part of a multi-column identifier, it’s incomplete. Like a recipe where an ingredient is tied to a meal ID and recipe step ID, but some data only relates to the meal ID.

**🖼️ Visual Representation**:

```asciitext
Orders Table (Composite Key: (order_id, product_id))
--------------------------------------------------
| order_id | product_id | order_date | product_name |
--------------------------------------------------

2NF fix ->
(Orders)                (Products)
| order_id | order_date |     | product_id | product_name |
```

**🔬 Technical Explanation**: 2NF applies only if there is a **composite key**. It requires that all non-key columns depend on the **entire** key, not just part of it.

**💼 Support/SRE Application**: If partial dependencies are left in the schema, it can cause anomalies when updating or deleting records.

**🔄 System Impact**: Eliminating partial dependencies reduces redundant data and associated overhead.

**⚠️ Common Misconceptions**: Thinking that if you have no composite keys, you automatically skip 2NF. True, but you should confirm no multi-column primary keys exist.

**📊 Oracle Implementation**: In Oracle, ensure any table with a composite PK has no columns that depend on only part of that PK. If you find partial dependencies, split the table.

---

#### 6. Third Normal Form (3NF)

**🔍 Beginner Analogy**: Think of 3NF like ensuring each detail belongs where it’s most relevant. If you store a supplier’s address in a Product table, that’s a transitive dependency.

**🖼️ Visual Representation**:

```asciitext
TRANSITIVE DEPENDENCY EXAMPLE:
| Product_ID | Product_Name | Supplier_Name | Supplier_Address |

3NF FIX:
(Products)           (Suppliers)
| Product_ID |        | Supplier_ID | Supplier_Name | Supplier_Address |
```

**🔬 Technical Explanation**: 3NF requires removing **transitive dependencies**, where non-key attributes depend on other non-key attributes.

**💼 Support/SRE Application**: Ensures changes in supplier details, for example, happen in one place, preventing data anomalies.

**🔄 System Impact**: Reduces data duplication, thus improving update performance.

**⚠️ Common Misconceptions**: Believing 3NF is the final form of all design. Sometimes further normalization forms (BCNF, 4NF, etc.) or partial denormalization is needed.

**📊 Oracle Implementation**: Typically, you create separate tables for each entity. Use foreign keys to link these tables properly.

---

#### 7. Denormalization Strategies

**🔍 Beginner Analogy**: Think of denormalization like storing frequently used shortcuts on your computer desktop rather than always opening your file explorer.

**🖼️ Visual Representation**:

```asciitext
(Normalized)           (Denormalized)
 Many Tables ----> Fewer Tables + Some Redundancy
```

**🔬 Technical Explanation**: Denormalization sometimes duplicates data for **read** performance gains.

**💼 Support/SRE Application**: SREs often face read-heavy workloads, so denormalization might reduce the complexity of queries.

**🔄 System Impact**: Improves some read queries at the expense of more complex updates.

**⚠️ Common Misconceptions**: Overusing denormalization can lead to massive data anomalies.

**📊 Oracle Implementation**: Carefully add redundant columns or tables to reduce join overhead. Always evaluate performance trade-offs using tools like **AWR** (Automatic Workload Repository).

---

### 🔄 Normalization Process in Practice

**Step-by-step example**: Suppose we have this unnormalized table:

```asciitext
| OrderID | CustomerName | CustomerPhone      | OrderDate |
|---------|-------------|--------------------|------------|
| 1001    | John Smith  | 555-1212,555-3434 | 2025-03-02  |
```

1. **1NF**: Separate phone numbers into their own rows.
2. **2NF**: If we have a composite key, ensure each non-key depends on the entire key.
3. **3NF**: Move any data (like CustomerName) that belongs to a Customer entity into a Customer table.

**SQL Examples**:

```sql
-- Create the normalized table in Oracle
CREATE TABLE customers (
  customer_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
  customer_name VARCHAR2(100) NOT NULL,
  PRIMARY KEY (customer_id)
);
```

**Common Pitfalls**:

* Forgetting to move repeating groups
* Not checking for partial dependencies
* Missing out on transitive dependencies

**Verification Techniques**:

* Reviewing each column’s dependency
* Checking Oracle constraints

---

### 🛠️ Oracle Database Design Tools and Features

1. **Oracle SQL Developer Data Modeler** – Drag-and-drop modeling, forward/reverse engineering
2. **Constraint Implementation** – Oracle enforces constraints at the database level
3. **Tablespace Considerations** – Logical storage for schemas (e.g., `USERS` tablespace vs. separate data/index tablespaces)
4. **Schema Comparison** – Tools within SQL Developer or third-party solutions for diffing schema versions

---

### 🔍 Impact of Design on Performance

* **Normalization** generally improves data consistency but can involve more joins.
* **Index Design** in Oracle is critical for normalized schemas to handle joins efficiently.
* **Performance Bottlenecks** often appear in read-heavy joins if not indexed well.
* **SRE Approach**: Use Oracle’s AWR and **EXPLAIN PLAN** to measure the impact of schema design.

---

### 🔨 Hands-On Exercises

**🔍 Beginner**

1. Identify repeating groups in a sample table.
2. Convert a table to 1NF by creating a child table.
3. Write an ER diagram for a small library system.

**🧩 Intermediate**

1. Normalize a table from 1NF to 2NF and 3NF in Oracle.
2. Create `PRIMARY KEY` and `FOREIGN KEY` constraints in Oracle.
3. Practice partial denormalization for a read-heavy table.

**💡 Advanced/SRE**

1. Design an index strategy for a fully normalized schema.
2. Measure query performance before and after normalization using AWR.
3. Implement denormalization with caution, then measure read vs. write trade-offs.

---

### 🚧 Troubleshooting Scenarios

1. **Scenario 1**: A table storing multiple attributes in a single column leads to slow queries. Diagnosing the cause by checking data distribution.
2. **Scenario 2**: A partial dependency causes inconsistent data updates, revealed by a foreign key constraint violation.
3. **Scenario 3**: Excessive joins in a highly normalized schema cause performance issues. Adding a denormalized summary table speeds up key reports.

For each scenario, consider Oracle-specific steps: reviewing constraints in `ALL_CONSTRAINTS`, analyzing queries with `EXPLAIN PLAN`, and checking performance metrics via AWR.

---

### ❓ Frequently Asked Questions

**🔍 Beginner**

1. *What is the difference between a primary key and a unique constraint in Oracle?*
2. *How do I know if my table is in 1NF?*
3. *Do I always need to normalize my tables?*

**🧩 Intermediate**

1. *When should I use a surrogate key instead of a natural key in Oracle?*
2. *How can I detect partial dependencies in my schema?*
3. *What Oracle tools are best for visualizing normalization?*

**💡 Advanced/SRE**

1. *Does denormalization hurt Oracle replication or standby databases?*
2. *How do I measure the impact of normalization using Oracle AWR?*
3. *What are common design pitfalls when scaling to very large Oracle databases?*

---

### 🔥 Oracle-Specific SRE Scenario

**Real-World Incident**:
A large e-commerce site reports intermittent 2-second delays on the checkout flow.

1. **Initial Observation**: AWR shows high buffer gets on a join involving five tables.
2. **Investigation**:
   - `EXPLAIN PLAN` reveals a cart table joined to product, user, promotions, and inventory.
   - The promotions data is partially stored in the cart table, leading to transitive dependencies.
   - Surrogate keys are used, but no consistent foreign key constraints enforce data integrity.
3. **Resolution**:
   - Normalize the promotions data out of the cart table.
   - Add missing foreign keys.
   - Rebuild indexes.
   - Test performance with AWR again.
4. **SRE Principles**: Ongoing monitoring, focusing on reliability by ensuring data consistency and minimized anomalies.

---

### 🧠 Key Takeaways

* Good database design is **essential** for performance, integrity, and maintainability.
* Normalization (1NF, 2NF, 3NF) reduces redundancy but can introduce more joins.
* Balancing theory with real-world performance needs may require **denormalization**.
* Oracle-specific features (e.g., constraints, indexing, AWR) must be leveraged properly.
* Continual review and schema evolution keep the database aligned with changing requirements.

---

### 🚨 Career Protection Guide for Database Design

1. **High-Risk Design Decisions**: E.g., overusing denormalization or ignoring constraints.
2. **Design Reviews**: Always get peer and architect review before rolling out major changes.
3. **Staged Implementation**: Use dev/staging environments to test design changes.
4. **Communication**: Clearly explain proposed design changes to stakeholders.
5. **Testing**: Validate design changes with real workload or synthetic load tests.

---

### 🔮 Preview of Next Day’s Content

Tomorrow (Day 4), we’ll focus on **Querying Related Data with SQL JOINs**. The normalization skills you’ve learned today will make those joins more intuitive and efficient.

---

## 🚀 Additional Enhancement Sections

### 1. Design Pattern Examples

**Common Oracle Design Patterns**:

* **Star Schema** for analytics
* **Transactional OLTP** with 3NF for core data
* **Master-Detail** relationships

**Anti-patterns**:

* **One Big Table**: All data in a single table leads to huge queries.
* **Hidden Multi-value Fields**: Storing delimited data in a single column.

**Visual Comparison**:

```
Good Design:                Poor Design:
(3NF)                        (1 Giant Table)
(Constraints)               (Minimal Constraints)
```

### 2. Normalization Decision Tree

```
            [Does the table have repeating groups?]
                   /              \
                  / Yes           \ No
                 /                 \
         [Apply 1NF]         [Check for composite keys?]
                                  /           \
                                 / Yes        \ No
                                /               \
                        [Apply 2NF]      [Go to 3NF check]
```

**Performance Implications**: Each decision step might add more tables but also reduces redundancy.

### 3. Oracle Constraints Visualization

```asciitext
| Employees         |           | Departments          |
|-------------------|           |----------------------|
| emp_id (PK)       | -- FK --> | dept_id (PK)         |
| emp_name          |           | dept_name (UNIQUE)   |
| dept_id (FK)      |           | location (CHECK)     |
| NOT NULL fields   |           | NOT NULL fields      |
```

### 4. Performance Impact Analysis

* Before Normalization: Fewer tables, simpler queries, but lots of redundancy.
* After Normalization: More tables, possibly more joins, but less redundancy.
* **Oracle Execution Plans** may show additional steps for joins but lower row scans.

### 5. Schema Evolution Management

* **Schema Changes**: Use `ALTER TABLE` carefully, watch for locks and potential downtime.
* **Managing Constraints**: Temporarily disable constraints if reloading data, then re-enable.
* **Backward Compatibility**: Keep old columns until upstream apps are updated.
* **Monitoring**: SRE-level logging and metrics before and after changes.

---

Congratulations! You’ve completed Day 3, focusing on the critical art of **Database Design Principles** and **Normalization**. You’re now equipped to craft better schemas in Oracle, troubleshoot design-related performance issues, and build a robust foundation for Day 4’s exploration of **SQL JOINs**.

