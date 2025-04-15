Below is a set of 20 quiz questions following the instructions in day-9_10_quiz_questions.md . They cover Day 9’s SQL vs NoSQL Database Comparison topics, with the specified distribution of difficulty levels and question types. Each question is clearly labeled with a topic, difficulty, and format.

---

# Day 9 - 10 Quiz: SQL vs NoSQL Database Comparison

## Beginner-Level (🔍) Questions

### 1. [Paradigm Differences]
🔍 Beginner | Multiple Choice

Which of the following best describes a **fundamental difference** between SQL (relational) databases and NoSQL databases?

A. SQL databases never use primary keys, whereas NoSQL databases always do  
B. SQL databases are generally optimized for horizontal scaling, whereas NoSQL databases only scale vertically  
C. SQL databases typically rely on schema-on-write, while many NoSQL databases use schema-on-read  
D. SQL databases store JSON documents, while NoSQL systems cannot handle document-oriented data  

---

### 2. [Relational vs Key-Value Stores]
🔍 Beginner | Multiple Choice

A small caching layer is needed to store user session data with minimal query complexity. Which database type is **most appropriate** for this scenario?

A. Relational database with strict foreign key constraints  
B. Document database with nested objects  
C. Key-value store like Redis or DynamoDB  
D. Graph database focusing on relationships  

---

### 3. [ACID vs BASE Basics]
🔍 Beginner | Multiple Choice

Which statement **best** reflects the difference between ACID transactions in SQL databases and BASE properties in NoSQL databases?

A. ACID transactions require eventual consistency, while BASE is always strongly consistent  
B. ACID transactions ensure strict consistency, while BASE embraces eventual consistency  
C. ACID transactions only apply to read operations, while BASE applies to all write operations  
D. ACID transactions allow partial updates, while BASE enforces atomic updates  

---

### 4. [Schema Approaches]
🔍 Beginner | Multiple Choice

Which of the following is **true** about schema management in typical NoSQL systems compared to SQL databases?

A. NoSQL databases enforce rigid schemas at write time  
B. SQL databases allow any document structure at read time  
C. NoSQL databases often use a flexible schema, allowing new fields without altering a central schema  
D. SQL databases can only store denormalized JSON objects  

---

### 5. [Consistency Models]
🔍 Beginner | True/False

In an eventually consistent system (common in some NoSQL databases), writes are guaranteed to appear in all replicas instantly.

A. True  
B. False  

---

### 6. [Key NoSQL Concepts]
🔍 Beginner | Fill-in-the-Blank

Complete the following statement:

“_____________ consistency means that once an update is made, some replicas may not immediately see the change, but eventually, all nodes will reflect the same data.”

A. Immediate  
B. Strong  
C. Eventual  
D. Transactional  

---

### 7. [Data Models]
🔍 Beginner | Matching

Match each **data model** in Column A with its characteristic or typical use case in Column B.

Column A:
1. Document Store  
2. Key-Value Store  
3. Column-Family Store  
4. Graph Database  

Column B:

A. Focuses on storing data in row-like structures grouped by columns for high write throughput  
B. Ideal for relationships and network-like queries using nodes and edges  
C. Uses flexible, self-describing data (often JSON), good for semi-structured data  
D. Organizes data as simple key-value pairs, excellent for caching and rapid lookups  

---

## Intermediate-Level (🧩) Questions

### 8. [Use Case Analysis]
🧩 Intermediate | Multiple Choice

Your team needs a database to store **user profile information** where each user has a distinct structure (some have extra fields, some have fewer). Which NoSQL database type typically handles this **best**?

A. Graph database like Neo4j  
B. Column-family store like Cassandra  
C. Key-value store like Amazon DynamoDB  
D. Document database like MongoDB  

---

### 9. [Data Modeling Techniques]
🧩 Intermediate | Multiple Choice

In a **document database** such as MongoDB, which design approach is commonly recommended to optimize read performance?

A. Highly normalizing data into multiple collections and joining them at query time  
B. Storing related data within the same document to avoid complex multi-collection queries  
C. Eliminating all embedded arrays in favor of single-value fields  
D. Using a star schema with dimension tables and a fact table  

---

### 10. [ACID vs BASE in Practice]
🧩 Intermediate | Multiple Choice

A financial application requires **guaranteed atomic updates** to user balances. Which statement about selecting a database is **most accurate**?

A. A strongly consistent NoSQL store can handle atomic updates, but a typical eventual consistency model might not  
B. A typical key-value store using eventual consistency is sufficient for guaranteed atomic updates  
C. Document databases do not support transactions under any circumstances  
D. ACID compliance is irrelevant when dealing with monetary transactions  

---

### 11. [Query Language Differences]
🧩 Intermediate | Multiple Choice

Which query approach is most commonly associated with **key-value** NoSQL databases?

A. Full-blown SQL with joins and subqueries  
B. A CRUD-based API where you get and set values by key  
C. A graph traversal language focusing on edges and relationships  
D. A document query engine that allows nested field matching  

---

### 12. [Scalability and Sharding]
🧩 Intermediate | True/False

Sharding a NoSQL database typically requires less manual schema design work than sharding a relational database, because NoSQL systems are often built with horizontal scaling in mind.

A. True  
B. False  

---

### 13. [Schema Flexibility]
🧩 Intermediate | Fill-in-the-Blank

Complete the following statement:

“In many NoSQL databases, **schema evolution** is simpler because the database follows a _____________ approach, allowing new fields or structures without a central DDL change.”

A. Schema-on-Write  
B. Schema-on-Read  
C. Strictly Enforced Schema  
D. Single-Table  

---

### 14. [ACID vs BASE Ordering]
🧩 Intermediate | Ordering

Arrange the following **ACID transaction properties** in the correct sequence to reflect their usual listing order:

A. Consistency  
B. Durability  
C. Atomicity  
D. Isolation  

---

## Advanced-Level (💡) Questions

### 15. [Reliability Considerations]
💡 Advanced/SRE | Multiple Choice

A high-traffic e-commerce site uses a **document database** (MongoDB) with **replica sets**. It experiences intermittent stale reads when a secondary is behind the primary. Which solution most directly addresses this **stale read** concern?

A. Using a read preference of “secondary” to reduce load on the primary  
B. Configuring “readConcern: majority” so that reads wait for changes to propagate to a majority of replicas  
C. Relying on offline batch processes to eventually fix data discrepancies  
D. Lowering replication factor to reduce overhead  

---

### 16. [CAP Theorem in Distributed NoSQL]
💡 Advanced/SRE | Multiple Choice

According to the CAP theorem, which **two** guarantees are typically prioritized by DynamoDB in a partition-tolerant scenario?

A. Consistency and durability  
B. Consistency and availability  
C. Availability and partition tolerance  
D. Partition tolerance and consistency  

*(Note: CAP typically references Consistency, Availability, Partition tolerance. DynamoDB design commonly trades off strict consistency for availability in many configurations, though it offers optional strong consistency on reads.)*

---

### 17. [Operational Complexity]
💡 Advanced/SRE | True/False

**Statement**: Managing operational tasks (like backups, cluster resizing, or version upgrades) is typically simpler in a self-managed NoSQL environment than in a fully managed cloud NoSQL service.

A. True  
B. False  

---

### 18. [Advanced Consistency Settings]
💡 Advanced/SRE | Fill-in-the-Blank

Complete the following statement:

“Cassandra offers tunable consistency, meaning you can configure _____________ for both read and write operations to balance availability and consistency needs.”

A. Shared Keys  
B. Sharding Thresholds  
C. Consistency Levels  
D. Multi-Master Indexes  

---

### 19. [Data Models Comparison]
💡 Advanced/SRE | Matching

Match each **NoSQL database type** in Column A with a **key architectural characteristic** in Column B.

Column A:  
1. Graph Database  
2. Document Database  
3. Column-Family Store  
4. Key-Value Store  

Column B:  
A. Stores data in a flexible JSON or BSON-like structure, allowing nested fields  
B. Specialized in storing and traversing nodes and edges to handle relationship-heavy data  
C. Organizes data into column families, providing high write throughput and partitioned structures  
D. Uses a simple get/put API for values associated with unique keys  

---

### 20. [Migration Strategy Ordering]
💡 Advanced/SRE | Ordering

When **migrating** a monolithic relational data model into a NoSQL-based microservices architecture, arrange these steps in a logical sequence:

A. Identify read/write patterns and define service boundaries  
B. Choose an appropriate NoSQL data model (document, key-value, column-family, etc.)  
C. Extract entities or tables from the monolith into specialized services or collections  
D. Validate data consistency and handle edge cases in the new design  

---

**End of Quiz**