# Day 1 Answer Sheet

Below is the **Answer Key** for the 12 quiz questions, now with **explanations** that clarify why each choice is correct. This answer set is typically kept separate from the main training module, as requested. Use it to **validate** your understanding and deepen your reasoning about each concept.

---

## 🟢 Beginner Questions (1-4)

1. **Which term best describes an individual record in a table?**  
   - **Correct Answer: B) Row**  
   - **Explanation**: In relational databases, data is organized in **rows** and **columns**. Each individual record (e.g., one customer, one order) is a row. A **column** is a specific field/attribute. A **schema** defines the overall structure. A **primary key** is a unique identifier, not the record itself.

2. **What does a primary key guarantee?**  
   - **Correct Answer: B) A unique identifier for each row**  
   - **Explanation**: The primary key constraint ensures that no two rows can share the same primary key value and that the primary key column(s) can never be null. It does not guarantee an index automatically (though most DBs create one), nor does it reference other tables.

3. **To retrieve all columns from a table named `users`, which command is correct?**  
   - **Correct Answer: B) `SELECT * FROM users;`**  
   - **Explanation**: `SELECT *` means “select all columns.” `SHOW * FROM users;` is invalid SQL. `SELECT FROM users;` is incomplete because it lacks what to select. `SELECT ALL FROM users;` is not standard syntax for retrieving all columns.

4. **Which tool is used to connect to a PostgreSQL database via command line?**  
   - **Correct Answer: A) psql**  
   - **Explanation**: PostgreSQL’s default command-line interface is **psql**. **sqlplus** is Oracle’s CLI, **sp_columns** is a SQL Server procedure for table structure, and **SSMS** (SQL Server Management Studio) is a graphical tool for SQL Server.

---

## 🟡 Intermediate Questions (5-8)

5. **What is the main difference between `JOIN` and listing tables separated by commas in the FROM clause?**  
   - **Correct Answer: B) Explicit JOIN is usually clearer and prevents accidental cartesian products**  
   - **Explanation**: Modern SQL best practice is to use **explicit JOIN** syntax (`JOIN ... ON ...`) for clarity and maintainability. Comma-separated tables without a proper WHERE join condition can lead to a **cartesian product** (combination of every row in the first table with every row in the second).

6. **Which command reveals detailed table structure in PostgreSQL (psql)?**  
   - **Correct Answer: B) `\d tablename`**  
   - **Explanation**: In psql, `\d tablename` describes the schema, columns, indexes, and constraints of a table. `\dt` just lists tables. `DESC tablename;` is an Oracle command, and `SHOW columns FROM tablename` is not standard in PostgreSQL.

7. **If a row is missing when you run a query, which might be the likely cause?**  
   - **Correct Answer: B) The WHERE clause may be filtering it out**  
   - **Explanation**: A row can appear “missing” if the filter condition (WHERE) is too restrictive. While uncommitted transactions or locks can sometimes be a cause, the **most common** day-to-day reason is an overly narrow or incorrect WHERE condition.

8. **Which index scenario might speed up a WHERE clause filter on a customer’s name?**  
   - **Correct Answer: C) Index on the `name` column**  
   - **Explanation**: If your query frequently filters by `name`, an index on the `name` column helps the database look up rows more efficiently. Indexing other columns (phone number) doesn’t help name filters, and disabling indexing isn’t beneficial for performance.

---

## 🔴 SRE-Level Questions (9-12)

9. **Which statement best describes the use of execution plans?**  
   - **Correct Answer: B) They show how the DB engine will run the query, revealing performance details**  
   - **Explanation**: Execution plans (e.g., via `EXPLAIN`) detail which indexes or joins the DB engine will use. This is critical for diagnosing slow queries, not just an optional or trivial feature.

10. **When might you want a partitioned table structure in PostgreSQL?**  

   - **Correct Answer: C) For very large tables, to manage performance and maintainability**  
   - **Explanation**: Partitioning is helpful when dealing with large data sets. It can improve query performance and maintenance tasks by splitting a large table into smaller, more manageable segments.

11. **How can too many concurrent SELECT queries harm a production system?**  

   - **Correct Answer: B) They can starve the CPU, increase I/O load, and cause blocking**  
   - **Explanation**: Even read-only queries consume resources. If too many occur at once, CPU, memory, and disk I/O can be saturated. Some databases also apply locks for reads, potentially blocking other operations.

12. **Which best practice helps ensure safe queries in production?**  

   - **Correct Answer: C) Always test queries in a development or staging environment first**  
   - **Explanation**: Testing queries in non-production environments is a best practice to avoid accidental performance hits or data issues. Running everything as superuser (option A) is risky, skipping WHERE clauses (option B) can hamper performance or correctness, and randomly killing queries (option D) is obviously not a best practice.

---

## Final Note
Use these **explanations** to see how each question ties back to the core Day 1 concepts: **relational structures, safe querying, performance awareness, and SRE reliability**. Mastering these fundamentals ensures you’re well-equipped to troubleshoot and prevent many common database pitfalls.