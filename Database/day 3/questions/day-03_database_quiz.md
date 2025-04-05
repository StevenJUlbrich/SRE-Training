# Day 3: Database Design & Normalization Quiz

## Question 1: [Entity Integrity]

🔍 Beginner (Multiple Choice)

Which concept best describes the practice of ensuring each row in an Oracle table is uniquely identifiable, typically enforced by a primary key?

A. Referential Integrity  
B. Entity Integrity  
C. Partial Dependency  
D. Composite Index  

---

## Question 2: [First Normal Form]

🔍 Beginner (Multiple Choice)

Which of the following scenarios most clearly violates First Normal Form (1NF) in an Oracle table design?

A. Storing an integer value in a VARCHAR2 column  
B. Having multiple rows with the same primary key  
C. Including a repeating group of attributes within a single column  
D. Using surrogate keys instead of natural keys  

---

## Question 3: [Constraints]

🔍 Beginner (True/False)

A foreign key constraint in Oracle ensures that the values in a child table column must match existing values in the parent table’s referenced column.

A. True  
B. False  

---

## Question 4: [Entity-Relationship Modeling]

🔍 Beginner (Multiple Choice)

When designing an ER diagram for an Oracle database, which relationship type typically requires the use of an intersection (associative) table to handle data correctly?

A. One-to-One  
B. One-to-Many  
C. Many-to-Many  
D. Self-Referential  

---

## Question 5: [Referential Integrity]

🔍 Beginner (True/False)

In Oracle, if a record in the parent table is deleted, all matching records in the child table must automatically be deleted.

A. True  
B. False  

---

## Question 6: [Normalization Terminology]

🔍 Beginner (Fill-in-the-Blank)

Complete the following statement:

“In Oracle design, ___________ helps ensure that each data attribute depends on the key, the whole key, and nothing but the key.”

A. One-to-Many Relationship  
B. Third Normal Form (3NF)  
C. Denormalization  
D. Domain Integrity  

---

## Question 7: [Key Definitions]

🔍 Beginner (Matching)

Match each type of key in Column A with its appropriate definition in Column B.

**Column A**:  

1. Primary Key  
2. Foreign Key  
3. Unique Key  
4. Surrogate Key  

**Column B**:  
A. A system-generated key (often a numeric sequence in Oracle)  
B. Ensures no duplicate values in a column, but allows one NULL  
C. The field(s) used to identify a row uniquely in its own table  
D. Used to establish referential integrity by referencing another table’s column  

---

## Question 8: [Partial Dependencies]

🧩 Intermediate (Multiple Choice)

Which scenario best describes a partial dependency that violates Second Normal Form (2NF) in an Oracle table?

A. A single-column primary key referencing columns that do not depend on it  
B. A non-key column depending on part of a composite primary key  
C. A foreign key referencing a primary key in another table  
D. A column that has no direct relationship to any key in the table  

---

## Question 9: [Oracle Constraints]

🧩 Intermediate (Multiple Choice)

Which of the following Oracle features allows you to automatically enforce a business rule such as “salary must be greater than 0” at the database level?

A. CHECK constraint  
B. UNIQUE index  
C. ON DELETE CASCADE  
D. CLOB data type  

---

## Question 10: [ER Diagrams]

🧩 Intermediate (True/False)

In an ER diagram for an Oracle system, a one-to-many relationship is represented by a single line connecting the two entities, with crow’s foot notation on the “many” side.

A. True  
B. False  

---

## Question 11: [Performance Considerations]

🧩 Intermediate (Multiple Choice)

Which approach might improve query performance if your Oracle database often needs to join two frequently accessed tables?

A. Eliminating all composite indexes  
B. Normalizing to Fourth Normal Form  
C. Denormalizing part of the schema by combining attributes into one table  
D. Removing foreign key constraints  

---

## Question 12: [Transitive Dependencies]

🧩 Intermediate (Fill-in-the-Blank)

Complete the following statement:

“In 3NF, every non-key attribute must depend on the key, and not on another ________.”

A. Database Session  
B. Non-key Attribute  
C. Table Constraint  
D. Primary Key  

---

## Question 13: [Data Redundancy]

🧩 Intermediate (Multiple Choice)

Which of the following most commonly indicates unnecessary data redundancy in an Oracle design?

A. Use of foreign keys for referential integrity  
B. Multiple tables storing the same customer contact data  
C. Tables without surrogate keys  
D. A single column used in multiple different constraints  

---

## Question 14: [Normalization Steps]

🧩 Intermediate (Ordering)

Arrange the following steps in the correct order to achieve Third Normal Form (3NF):

A. Remove repeating groups (achieve 1NF).  
B. Eliminate partial dependencies (achieve 2NF).  
C. Remove transitive dependencies.  
D. Identify functional dependencies.  

---

## Question 15: [Denormalization Rationale]

💡 Advanced/SRE (Multiple Choice)

In an Oracle environment, which of the following scenarios best justifies a denormalized design for a specific set of tables?

A. When you want to simplify the data dictionary by removing constraints  
B. When you have a read-heavy application needing faster retrieval of aggregated data  
C. Whenever you need to ensure data integrity by having more copies of the same information  
D. When you aim to strictly follow 3NF for all functional dependencies  

---

## Question 16: [Indexing Implications]

💡 Advanced/SRE (Fill-in-the-Blank)

Complete the following statement:

“Adding multiple indexes to an Oracle table can improve read performance but can negatively impact ___________.”

A. Primary Key Selection  
B. Write Performance  
C. Foreign Key Constraints  
D. Stored Procedure Compilation  

---

## Question 17: [Complex Relationship Modeling]

💡 Advanced/SRE (Multiple Choice)

In an Oracle database, which is the best design approach to properly handle a complex many-to-many relationship among three entities that also require additional attributes for the relationships themselves?

A. Use a single intersection table with foreign keys to all three entities  
B. Merge all three entities into a single table with repeated columns  
C. Create multiple materialized views for each relationship  
D. Employ three separate pivot tables, each containing repeated groups  

---

## Question 18: [SRE Workflow]

💡 Advanced/SRE (Ordering)

When troubleshooting database performance issues in Oracle related to schema design, arrange the following steps in the correct order:

A. Check for missing indexes or poorly designed indexes  
B. Analyze query execution plans  
C. Identify slow-running queries and frequent table joins  
D. Assess normalization or potential denormalization needs  

---

## Question 19: [Oracle-Specific Features]

💡 Advanced/SRE (Multiple Choice)

Which Oracle feature can be leveraged to materialize precomputed joins or aggregations, potentially reducing the need for extensive denormalization?

A. B-Tree Indexes  
B. Oracle Virtual Private Database  
C. Materialized Views  
D. Synonyms  

---

## Question 20: [Advanced Matching]

💡 Advanced/SRE (Matching)

Match each advanced Oracle or design concept in Column A with its description in Column B.

**Column A**:  

1. Bitmap Index  
2. Partitioned Table  
3. Reverse Key Index  
4. Oracle Cluster  

**Column B**:  
A. Storing rows from different tables together based on a common key  
B. Useful for columns with low cardinality, improving performance in certain workloads  
C. Dividing a table into smaller, more manageable segments  
D. Reverses the key bytes to reduce index block contention  

---

Remember to consult the Day 3 training material for detailed explanations of these design and normalization concepts.
