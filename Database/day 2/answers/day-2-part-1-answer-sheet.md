# Answer Key for the Day 2.1 Knowledge Check Quiz

Including correct answers and detailed explanations for each question. Use these to verify your understanding of fundamental through SRE-level DML concepts and to reinforce best practices.

---

## 🟢 Beginner-Level Answers (Questions 1–4)

1. **Which SQL command adds a new row to a table?**  
   **Question:**  
   A. SELECT  
   B. INSERT  
   C. UPDATE  
   D. DELETE  

   **Answer:** **B. INSERT**  

   **Explanation:**  
   - **INSERT** is specifically designed to add new rows to a table.  
   - **SELECT** only reads (retrieves) data without changing it.  
   - **UPDATE** modifies existing rows.  
   - **DELETE** removes rows.  

2. **What clause ensures you only update certain rows instead of all rows?**  
   **Question:**  
   A. GROUP BY  
   B. HAVING  
   C. WHERE  
   D. RETURNING  

   **Answer:** **C. WHERE**  

   **Explanation:**  
   - **WHERE** is used in both **UPDATE** and **DELETE** statements to filter which rows to modify or remove.  
   - **GROUP BY** is used for aggregation in SELECT queries.  
   - **HAVING** is used with GROUP BY to filter aggregated results.  
   - **RETURNING** (Postgres) or **OUTPUT** (SQL Server) returns the changed rows after a DML operation, but it does not filter which rows to change.  

3. **After inserting data, which approach can immediately confirm success in PostgreSQL?**  
   **Question:**  
   A. A second session’s verification  
   B. The RETURNING clause  
   C. TRUNCATE  
   D. None, you must trust the DB  

   **Answer:** **B. The RETURNING clause**  

   **Explanation:**  
   - **RETURNING** in PostgreSQL allows you to see which data was inserted (such as the newly generated primary key or other columns), giving immediate feedback on the success and details of the inserted row(s).  
   - While a second session’s verification (A) or trusting logs can work, RETURNING is the direct, built-in mechanism to confirm the operation in the same statement.  
   - **TRUNCATE** is unrelated here, as it deletes all rows from a table.  

4. **If you run `DELETE FROM table_name;` without a WHERE clause, what happens?**  
   **Question:**  
   A. No rows are deleted  
   B. Only the first row is deleted  
   C. All rows are deleted  
   D. The statement errors out  

   **Answer:** **C. All rows are deleted**  

   **Explanation:**  
   - **DELETE** without a **WHERE** condition applies to every row in the table.  
   - This can be a severe mistake if you only intended to remove a subset of rows.  

---

## 🟡 Intermediate-Level Answers (Questions 5–8)

5. **When inserting multiple rows in PostgreSQL, which syntax is correct?**  
   **Question:**  
   A. `INSERT INTO table_name VALUES ('A','B','C');`  
   B. `INSERT INTO table_name (col1, col2) VALUES ('A','B') MULTI;`  
   C. `INSERT INTO table_name (col1, col2) VALUES ('A','B'), ('C','D');`  
   D. `INSERT INTO table_name MULTI VALUES('A','B','C','D');`  

   **Answer:** **C. `INSERT INTO table_name (col1, col2) VALUES ('A','B'), ('C','D');`**  

   **Explanation:**  
   - PostgreSQL supports inserting multiple rows by listing separate sets of values in one statement, separated by commas.  
   - Options A, B, and D use incorrect or non-existent syntax for multi-row inserts.  

6. **Which practice helps confirm the correctness of an UPDATE on multiple rows?**  
   **Question:**  
   A. Using TRUNCATE before updating  
   B. Using a SELECT with the same WHERE clause first  
   C. Using MERGE in Postgres  
   D. Updating without a WHERE clause  

   **Answer:** **B. Using a SELECT with the same WHERE clause first**  

   **Explanation:**  
   - Running `SELECT ... WHERE ...` beforehand shows which rows will be updated, preventing unintended changes.  
   - TRUNCATE (A) and updating without a WHERE clause (D) can be dangerous in many situations.  
   - MERGE (C) is more relevant for multi-table operations or Oracle/SQL Server usage but does not alone confirm correctness.  

7. **What’s a common reason for using INSERT with SELECT?**  
   **Question:**  
   A. To delete rows in another table  
   B. To combine the TRUNCATE and DELETE statements  
   C. To copy or transform data from one table to another  
   D. To rename a table  

   **Answer:** **C. To copy or transform data from one table to another**  

   **Explanation:**  
   - **INSERT ... SELECT** is typically used to copy existing rows from one table into another, optionally transforming or filtering them along the way.  
   - Options A, B, and D are unrelated to typical INSERT/SELECT usage.  

8. **Which SQL Server feature returns updated row info similarly to Postgres RETURNING?**  
   **Question:**  
   A. OUTPUT  
   B. PRINT  
   C. DBMS_OUTPUT.PUT_LINE  
   D. MERGE  

   **Answer:** **A. OUTPUT**  

   **Explanation:**  
   - **OUTPUT** in SQL Server can provide old and new values of updated or inserted rows, similar to PostgreSQL’s RETURNING.  
   - **PRINT** simply shows a message.  
   - **DBMS_OUTPUT.PUT_LINE** is an Oracle mechanism, not SQL Server.  
   - **MERGE** is more complex and used for combining insert, update, or delete logic, not specifically for returning changed rows.  

---

## 🔴 SRE-Level Answers (Questions 9–12)

9. **You need to update a large table with minimal downtime. Which approach is most likely recommended?**  
   **Question:**  
   A. Update all rows in one statement during peak hours  
   B. Split the update into smaller batches or use a rolling approach  
   C. Rewrite the entire table from scratch  
   D. Switch to Oracle for better performance  

   **Answer:** **B. Split the update into smaller batches or use a rolling approach**  

   **Explanation:**  
   - Performing a **large update** in batches (or a rolling approach) helps manage locks, resource usage, and can reduce contention.  
   - Updating everything in one go (A) during peak hours often causes blocking or performance issues.  
   - Rewriting the entire table (C) or switching databases (D) is not the practical or immediate best practice.  

10. **What is a key risk when combining multi-table joins with UPDATE?**  
   **Question:**  
   A. The database automatically inserts missing rows  
   B. Potential for cross join that updates more rows than intended  
   C. The operation only updates one row at a time  
   D. You cannot use a WHERE clause in multi-table updates  

   **Answer:** **B. Potential for cross join that updates more rows than intended**  

   **Explanation:**  

   - If the join condition is incorrect or missing, you may get a **cross join**, which can multiply rows and cause large-scale unintended updates.  
   - You can still use **WHERE** (D) with multi-table updates, and the DB won’t automatically insert rows unless you explicitly use MERGE logic.  

11. **In PostgreSQL, TRUNCATE often can’t be rolled back because:**  
   **Question:**  
   A. It has no difference from DELETE  
   B. It’s a fully transactional command  
   C. It bypasses normal transaction logging  
   D. It only works on system catalogs  

   **Answer:** **C. It bypasses normal transaction logging**  

   **Explanation:**  

   - **TRUNCATE** is often minimally logged for performance reasons, which is why it’s closer to a DDL operation. Because of this, you typically can’t roll back a TRUNCATE once executed.  
   - It is distinct from DELETE, which logs each row change, so (A) is not correct.  

12. **A good data verification strategy after large-scale DML includes:**  
   **Question:**  
   A. Rely on user complaints for feedback  
   B. Combining row count checks, returning clauses, and logging  
   C. Only verifying partial data changes every few months  
   D. Setting all columns to 0 or NULL to see if they changed  

   **Answer:** **B. Combining row count checks, returning clauses, and logging**  

   **Explanation:**  

   - A robust verification strategy ensures you confirm changes using:  
     1. **Row count checks** (e.g., `SELECT COUNT(*)`),  
     2. **Returning/OUTPUT** to see which rows changed,  
     3. **Logging/auditing** for deeper validation or rollback potential.  
   - Relying on user complaints (A) is obviously risky. Verifying only partially or sporadically (C) is inadequate. Setting columns to 0 or NULL (D) isn’t a verification strategy—it's a destructive operation.  

---

## Summary

- **Beginner Questions**: Covered the fundamentals of INSERT, WHERE clauses, RETURNING, and the effect of DELETE without WHERE.  
- **Intermediate Questions**: Demonstrated multi-row INSERT syntax, verification techniques for multiple-row updates, and the purpose of INSERT with SELECT.  
- **SRE-Level Questions**: Showed best practices for handling large-scale updates, multi-table joins, the nature of TRUNCATE, and comprehensive verification strategies.

By understanding not just the **correct answer** but also **why** the alternatives are incorrect, you reinforce a deeper grasp of DML best practices—a critical skill set for a support or SRE role.