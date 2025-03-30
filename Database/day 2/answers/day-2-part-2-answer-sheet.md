# Answer Key for the Day 2.2 Knowledge Check Quiz

Including correct answers and detailed explanations for each question. Review them to reinforce your understanding of transaction management concepts and best practices.

---

## 🟢 Beginner-Level Answers (Questions 1–4)

1. **Which command starts a transaction in PostgreSQL?**  
   **Question:**  
   A. `START WORK;`  
   B. `BEGIN;`  
   C. `OPEN TRANSACTION;`  
   D. `ACTIVATE TRAN;`  

   **Answer:** **B. `BEGIN;`**  

   **Explanation:**  
   - In PostgreSQL, the standard command to explicitly start a new transaction block is **BEGIN;**.  
   - Some other databases may use `BEGIN TRAN` or `START TRANSACTION;`, but **BEGIN;** is the canonical form in Postgres.  

2. **When does the database apply changes made in a transaction?**  
   **Question:**  
   A. Immediately after each statement  
   B. When you ROLLBACK  
   C. When you COMMIT  
   D. When the database restarts  

   **Answer:** **C. When you COMMIT**  

   **Explanation:**  
   - By design, changes in a transaction remain pending until you issue **COMMIT**, at which point they become permanent (barring any rollback mechanisms).  
   - **ROLLBACK** discards changes, not applies them.  

3. **What is the meaning of Atomicity in ACID?**  
   **Question:**  
   A. Transactions run in parallel  
   B. Data changes happen all-or-nothing  
   C. Data is always consistent  
   D. Database recovers from disk failure  

   **Answer:** **B. Data changes happen all-or-nothing**  

   **Explanation:**  
   - **Atomicity** guarantees that in a transaction, either **all** statements succeed and commit or **none** do. You can’t end up with partial application of the transaction’s operations.  
   - Consistency, isolation, and durability are other ACID properties, but atomicity specifically refers to all-or-none behavior.  

4. **Which statement about ROLLBACK is correct?**  
   **Question:**  
   A. It permanently saves changes  
   B. It discards changes made since the last COMMIT or BEGIN  
   C. It only works on read-only transactions  
   D. It’s used to rename tables  

   **Answer:** **B. It discards changes made since the last COMMIT or BEGIN**  

   **Explanation:**  
   - **ROLLBACK** undoes (or discards) all modifications in the current transaction, resetting the database to the state before the transaction began (or the last savepoint).  
   - It does not save changes (A), it has nothing to do with read-only transactions (C), and it’s not for renaming tables (D).  

---

## 🟡 Intermediate-Level Answers (Questions 5–8)

5. **Why might you use a savepoint?**  
   **Question:**  
   A. To change the isolation level  
   B. To partially roll back only some changes  
   C. To rename a table within a transaction  
   D. Because it’s mandatory in all transactions  

   **Answer:** **B. To partially roll back only some changes**  

   **Explanation:**  
   - **Savepoints** allow you to mark specific points within a transaction. You can roll back to a savepoint without discarding **all** changes in the overall transaction.  
   - Isolation level changes (A) and table renames (C) are different operations. Savepoints are also not mandatory in every transaction (D).  

6. **Which isolation level typically prevents dirty reads but may allow nonrepeatable reads?**  
   **Question:**  
   A. READ UNCOMMITTED  
   B. READ COMMITTED  
   C. REPEATABLE READ  
   D. SERIALIZABLE  

   **Answer:** **B. READ COMMITTED**  

   **Explanation:**  
   - **READ COMMITTED** disallows dirty reads (i.e., seeing uncommitted data) but can still allow **nonrepeatable reads** or **phantom reads** because each statement in the transaction sees only committed changes at that moment.  
   - **REPEATABLE READ** and **SERIALIZABLE** provide stronger guarantees by preventing most or all concurrency anomalies.  

7. **If you encounter a constraint violation mid-transaction, what usually happens?**  
   **Question:**  
   A. The transaction continues unaffected  
   B. The database automatically commits partial changes  
   C. The database will require a rollback or mark the transaction as failed  
   D. All other transactions are also rolled back  

   **Answer:** **C. The database will require a rollback or mark the transaction as failed**  

   **Explanation:**  
   - A constraint violation typically forces that statement to fail, and the database marks the entire **current** transaction as invalid. You either have to explicitly roll back or the database automatically invalidates it, requiring a rollback before continuing.  
   - It does not just commit partial changes (B), nor does it roll back other users’ transactions (D).  

8. **Which action is NOT a recommended way to avoid deadlocks?**  
   **Question:**  
   A. Consistently access tables in the same order  
   B. Keep transactions small and short  
   C. Lock rows in alphabetical order of table names  
   D. Let the DB kill one transaction and retry  

   **Answer:** **C. Lock rows in alphabetical order of table names**  

   **Explanation:**  
   - While consistent lock ordering is recommended, doing it **alphabetically** by table name is not a standard or recommended approach—it’s contrived and could cause confusion or unintended side effects. Typically, you coordinate lock ordering by **logical** or **business** rules, not alphabetical sorting.  
   - Options (A), (B), and (D) represent valid strategies: consistent lock order, minimal transaction scope, and retrying after deadlock.  

---

## 🔴 SRE-Level Answers (Questions 9–12)

9. **What typically happens if two transactions concurrently cause a SERIALIZABLE conflict in Postgres?**  
   **Question:**  
   A. Both transactions automatically succeed  
   B. The database picks one to fail with a serialization error  
   C. All locks are released and changes get lost  
   D. The database duplicates the data as a fallback  

   **Answer:** **B. The database picks one to fail with a serialization error**  

   **Explanation:**  
   - Under **SERIALIZABLE** isolation, Postgres will detect conflicts that can’t be resolved without violating serializability. One transaction is forcibly failed, returning an error like “could not serialize access.” The application should then retry that transaction.  

10. **Which scenario could lead to a “lost update” if the isolation level is too low?**  
   **Question:**  
   A. Two transactions reading and updating the same row, overwriting each other’s changes without seeing them  
   B. A single transaction never calling COMMIT  
   C. A large transaction causing a deadlock  
   D. Using savepoints to revert partial steps  

   **Answer:** **A. Two transactions reading and updating the same row, overwriting each other’s changes without seeing them**  

   **Explanation:**  

   - A “lost update” happens when each transaction reads the old value, then writes a new value without knowledge that another transaction has concurrently updated that same row. Lower isolation levels (like READ UNCOMMITTED or poorly implemented READ COMMITTED) can allow this.  

11. **In an SRE context, how should you handle a deadlock error in production?**  
   **Question:**  
   A. Restart the entire database immediately  
   B. Ignore it; the database will fix itself  
   C. Log the error, let one transaction be killed, and implement a retry logic or fix lock ordering  
   D. Switch to a NoSQL database with no transactions  

   **Answer:** **C. Log the error, let one transaction be killed, and implement a retry logic or fix lock ordering**  

   **Explanation:**  

   - In most RDBMSs, a deadlock results in killing one “victim” transaction. The best practice is to handle that error in the application or SRE workflow. You either **retry** the failed transaction or change your lock ordering.  
   - Restarting the DB (A) or ignoring the problem (B) are not sustainable solutions.  

12. **Which is a best practice for transaction performance under high concurrency?**  
   **Question:**  
   A. Use extremely long transactions so you only commit once a day  
   B. Use the highest isolation (SERIALIZABLE) for all transactions by default  
   C. Keep transactions as short as possible and reduce lock duration  
   D. Always manually set READ UNCOMMITTED for maximum speed  

   **Answer:** **C. Keep transactions as short as possible and reduce lock duration**  

   **Explanation:**  

   - **Short, focused transactions** reduce contention, free locks quickly, and help the system handle high concurrency.  
   - Very long transactions (A) cause extensive locking and big transaction logs. Always using the highest isolation (B) can hinder performance unless truly needed. Forcing READ UNCOMMITTED (D) can lead to data anomalies.  

---

## Summary

- **Beginner Questions**: Covered basic transaction commands (BEGIN, COMMIT, ROLLBACK), the concept of atomicity, and how ROLLBACK works.  
- **Intermediate Questions**: Highlighted savepoints, isolation levels (READ COMMITTED vs. others), mid-transaction errors, and avoiding deadlocks with consistent strategies.  
- **SRE-Level Questions**: Focused on SERIALIZABLE conflicts, lost updates, deadlock handling, and practical performance tips for high concurrency.

Having these explanations helps solidify your understanding of transaction management, ensuring you can handle multi-step data changes safely and effectively as an SRE or database support professional.