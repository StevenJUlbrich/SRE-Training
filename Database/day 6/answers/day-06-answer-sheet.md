Below is the **Day 6 Answer Sheet** for the quiz questions on Basic Database Administration—covering user accounts, permissions, and the SRE perspective on availability and performance. Each entry restates the question, identifies the **correct answer**, provides a detailed **explanation**, and includes comparisons for Oracle/PostgreSQL/SQL Server, SRE insights, and additional practical tips. Enjoy!

(*Document reference for questions:  and*)

---

## Answer 1: Basic User Creation

🔍 Beginner | Multiple Choice

**Question:**  
Which of the following commands correctly creates a new database user named 'analyst_user' in an Oracle environment, with the password 'StrongPass2025'?

A. `CREATE ROLE analyst_user IDENTIFIED BY 'StrongPass2025';`  
B. `CREATE USER analyst_user IDENTIFIED BY StrongPass2025;`  
C. `CREATE USER analyst_user IDENTIFIED BY 'StrongPass2025';`  
D. `NEW USER analyst_user WITH PASSWORD='StrongPass2025';`

**Correct Answer:** C

**Explanation:**  

- In Oracle, you must enclose the password in quotes to ensure proper handling, especially if it contains special characters. The syntax `CREATE USER analyst_user IDENTIFIED BY 'StrongPass2025';` follows Oracle's convention precisely.  
- Option B omits quotes around the password; while some Oracle versions may parse it, best practice is to quote the password.  
- Option A attempts to create a ROLE rather than a USER.  
- Option D is not valid Oracle syntax.

**Why other options are incorrect:**  

- **A**: `CREATE ROLE ...` is for roles, not users.  
- **B**: Missing quotes around the password. Some Oracle environments require the quotes to parse passwords correctly (especially if containing special chars).  
- **D**: `NEW USER ... WITH PASSWORD` is not valid syntax in Oracle.

**Database Comparison Note:**  

- **PostgreSQL** uses `CREATE ROLE name WITH LOGIN PASSWORD '...'`.  
- **SQL Server** typically uses `CREATE LOGIN name WITH PASSWORD='...'; CREATE USER name FOR LOGIN name;`.

**Knowledge Connection:**  

- Ties into the **Database User Management Fundamentals** from Day 6, showing how to create new users securely.

**SRE Perspective:**  

- Properly defined users with strong passwords bolster security and reduce unauthorized access incidents.

**Additional Insight:**  

- Always apply password complexity rules to reduce vulnerability to brute-force attacks.

---

## Answer 2: System vs. Object Privileges

🔍 Beginner | Multiple Choice

**Question:**  
Which statement best describes the difference between system privileges and object privileges?

A. System privileges apply only to a single schema, while object privileges apply to all database objects.  
B. System privileges allow actions affecting the entire database, while object privileges control access to specific objects like tables or views.  
C. System privileges give read-only access, and object privileges give read-write access.  
D. System privileges are used only for backup tasks, while object privileges are used only for performance tuning.

**Correct Answer:** B

**Explanation:**  

- **System privileges** (e.g., CREATE USER, CREATE TABLESPACE) allow a user to perform operations that affect the overall environment, not just a single table.  
- **Object privileges** (e.g., SELECT, INSERT, UPDATE on a specific table) focus on a particular schema object.

**Why other options are incorrect:**  

- **A**: Reverses the correct scope; system privileges are broader, not limited to one schema.  
- **C**: Not all system privileges are read-only, and object privileges can be read-only or read/write depending on the commands granted.  
- **D**: Backup tasks and performance tuning can each involve both system and object privileges.

**Database Comparison Note:**  

- Oracle: System privileges include `CREATE USER` or `CREATE SESSION`; object privileges include `SELECT ON employees`.  
- PostgreSQL and SQL Server have similar distinctions but may phrase them differently (e.g., “server-level” vs. “database-level” in SQL Server).

**Knowledge Connection:**  

- Reinforces the difference between broad administrative actions and granular access to tables/views from Day 6’s “Privileges and Permissions” segment.

**SRE Perspective:**  

- Over-assigning system privileges can lead to critical outages or security breaches, impacting availability and performance.

**Additional Insight:**  

- Always verify if a user truly needs a system privilege or if object-level permissions suffice.

---

## Answer 3: Principle of Least Privilege

🔍 Beginner | True/False

**Question:**  
The principle of least privilege states that users should only be granted the minimum permissions they need to perform their tasks effectively.

A. True  
B. False

**Correct Answer:** A (True)

**Explanation:**  

- The principle of least privilege is a fundamental security best practice. It ensures each user has only the privileges necessary for their role, reducing the risk of accidental or malicious misuse.

**Database Comparison Note:**  

- Oracle, PostgreSQL, and SQL Server all encourage roles and granular privileges to enforce least privilege. Implementation details differ, but the concept is the same.

**Knowledge Connection:**  

- Directly related to Day 6’s emphasis on **security best practices** and preventing excessive permissions.

**SRE Perspective:**  

- Least privilege helps contain the impact (blast radius) if an account is compromised, thus protecting system availability and data integrity.

**Additional Insight:**  

- Regularly audit accounts and privileges to maintain a robust least-privilege model.

---

## Answer 4: Read-Only vs. Read-Write

🔍 Beginner | True/False

**Question:**  
Granting read/write access to a database user always has lower security risk than granting read-only access.

A. True  
B. False

**Correct Answer:** B (False)

**Explanation:**  

- Read/write access carries **higher** security risk because it allows modifications to data. Read-only access typically limits a user to viewing data, reducing the potential for data corruption or manipulation.

**Database Comparison Note:**  

- In Oracle or SQL Server, granting `SELECT` is lower risk than granting `INSERT` or `UPDATE`. Similarly, in PostgreSQL, `SELECT` privileges alone are less dangerous than `UPDATE` or `DELETE`.

**Knowledge Connection:**  

- Ties back to the discussion in Day 6 on implementing read-only vs. read/write privileges as a security measure.

**SRE Perspective:**  

- Minimizing write access helps protect data integrity. Fewer write-capable accounts reduce the chance of accidental or malicious data destruction.

**Additional Insight:**  

- If a process only needs to read data, do not grant it extra privileges—this directly enforces the principle of least privilege.

---

## Answer 5: SRE Perspective on Availability

🔍 Beginner | Multiple Choice

**Question:**  
Why is high database availability crucial from an SRE perspective?

A. It guarantees zero user errors.  
B. It ensures compliance with data privacy regulations.  
C. It directly impacts user experience and potential revenue losses due to downtime.  
D. It prevents password sharing among DBAs.

**Correct Answer:** C

**Explanation:**  

- High availability ensures end users can always access the service or data. If the database is down, both user experience and revenue may suffer significantly.

**Why other options are incorrect:**  

- **A**: You cannot guarantee zero errors even with high availability.  
- **B**: Availability helps meet service-level goals, but not all compliance regulations focus on availability alone.  
- **D**: This is more about operational policies, not a direct reason for high availability.

**Database Comparison Note:**  

- All major databases (Oracle, PostgreSQL, SQL Server) offer mechanisms for high availability like clustering or replication, but their specific tooling (Data Guard, streaming replication, Always On) differs.

**Knowledge Connection:**  

- Relates to Day 6 topics: **SRE Perspective**—availability metrics, monitoring solutions, and redundancy strategies.

**SRE Perspective:**  

- Availability is a key SRE concern, directly tied to Service Level Objectives (SLOs) and business continuity.

**Additional Insight:**  

- Measure availability with metrics like uptime percentage and track downtime to help refine SRE alert thresholds.

---

## Answer 6: Permissions Basics

🔍 Beginner | Fill-in-the-Blank

**Question:**  
Complete the following statement:  
A user with ________ permission can insert new records but cannot create or drop tables.

A. CONNECT  
B. SELECT  
C. INSERT  
D. ALTER  

**Correct Answer:** C – INSERT

**Explanation:**  

- `INSERT` allows adding new records to tables, but it does not give the power to create or drop them. Additional privileges like `CREATE TABLE` or `DROP` would be required to manage table structures.

**Why other options are incorrect:**  

- **A**: `CONNECT` generally allows a user to log in or establish a session, not insert rows.  
- **B**: `SELECT` is read-only.  
- **D**: `ALTER` typically modifies table structures.

**Database Comparison Note:**  

- In Oracle, `INSERT` is an object privilege. In PostgreSQL, you `GRANT INSERT ON table_name`. In SQL Server, you `GRANT INSERT ON dbo.TableName TO username`.

**Knowledge Connection:**  

- Reflects the principle of **least privilege**—give exactly what is needed.

**SRE Perspective:**  

- Over-granting privileges can cause data integrity issues if unauthorized updates or schema changes occur.

**Additional Insight:**  

- Always distinguish between DDL (create/drop) and DML (insert/select/update/delete) privileges.

---

## Answer 7: Users vs. Roles

🔍 Beginner | Multiple Choice

**Question:**  
Which of the following is TRUE regarding the difference between users and roles in many relational databases?

A. Users can log in to the database; roles cannot log in.  
B. Roles can log in to the database; users cannot log in.  
C. Users always have all privileges, but roles have none.  
D. There is no difference; 'user' and 'role' are interchangeable terms.

**Correct Answer:** A

**Explanation:**  

- Typically, a **user** is an account that can authenticate (log in). A **role** (in some systems) is a container of privileges that can be assigned to users. Some DBs (like PostgreSQL) unify the concept of “role” with or without `LOGIN` capability, but conceptually, a user can log in while a non-login role cannot.

**Why other options are incorrect:**  

- **B**: The opposite is true.  
- **C**: Users do not automatically have all privileges; roles can have privileges assigned.  
- **D**: There is usually a conceptual difference, though the syntax can vary across systems.

**Database Comparison Note:**  

- PostgreSQL conflates users and roles into a single concept with the `LOGIN` attribute. Oracle and SQL Server treat users and roles distinctly.

**Knowledge Connection:**  

- Demonstrates **role-based access control** from Day 6.

**SRE Perspective:**  

- Separating login accounts from permission groupings can simplify user management and reduce mistakes that lead to downtime.

**Additional Insight:**  

- Creating a non-login role for each functional group and then assigning users to that role is a best practice for large environments.

---

## Answer 8: Role-Based Permissions

🧩 Intermediate | Multiple Choice

**Question:**  
A database administrator wants to give a "reporting_role" the ability to run SELECT queries on the "sales" schema without letting them modify any data. Which command best achieves this in PostgreSQL?

A. `GRANT INSERT ON ALL TABLES IN SCHEMA sales TO reporting_role;`  
B. `GRANT SELECT ON ALL TABLES IN SCHEMA sales TO reporting_role;`  
C. `GRANT ALL PRIVILEGES ON SCHEMA sales TO reporting_role;`  
D. `GRANT USAGE ON SCHEMA sales TO reporting_role;`

**Correct Answer:** B

**Explanation:**  

- Granting `SELECT ON ALL TABLES IN SCHEMA sales` restricts the role to reading data only. This is precisely what reporting tasks typically need.

**Why other options are incorrect:**  

- **A**: `INSERT` would allow data modifications, which is not desired here.  
- **C**: `ALL PRIVILEGES` is excessive, allowing modifications.  
- **D**: `USAGE` on the schema only gives the ability to access objects in the schema namespace; it doesn’t permit table reads by itself.

**Database Comparison Note:**  

- In Oracle, you might use `GRANT SELECT ON sales.tablename TO reporting_role;` for each table, or a `GRANT SELECT ANY TABLE` system privilege (not recommended for principle of least privilege).  
- SQL Server uses `GRANT SELECT ON OBJECT::sales.myTable TO reporting_role;` for each object or `SCHEMA` if appropriate.

**Knowledge Connection:**  

- This question highlights proper **role-based access control** and the principle of least privilege from Day 6.

**SRE Perspective:**  

- Ensuring roles have limited privileges avoids accidental data corruption, thus supporting overall reliability.

**Additional Insight:**  

- Periodically review which roles have `ALL PRIVILEGES`; often, it’s overkill for typical usage scenarios.

---

## Answer 9: GRANT vs. REVOKE

🧩 Intermediate | Multiple Choice

**Question:**  
Which of the following statements about the GRANT and REVOKE commands is CORRECT?

A. REVOKE automatically removes all system privileges from every user in the database.  
B. GRANT never allows specifying which columns a user can SELECT.  
C. REVOKE can remove a privilege from a user, which may also remove privileges from roles that user manages.  
D. GRANT only works for object privileges, not system privileges.

**Correct Answer:** C

**Explanation:**  

- **REVOKE** can remove privileges directly from a user. If that user also possessed roles or had privileges that cascade, removing a privilege can indirectly affect other privileges. For instance, in some DBs if a user was the only membership path to a role, that cascade can remove the chain of privileges.

**Why other options are incorrect:**  

- **A**: REVOKE doesn’t automatically remove all privileges from everyone; it only affects privileges explicitly specified.  
- **B**: You can specify individual columns to GRANT `SELECT` on in many DBs (e.g., `GRANT SELECT(column1, column2) ON table` in some systems).  
- **D**: You can also grant system privileges (e.g., `GRANT CREATE SESSION TO user` in Oracle).

**Database Comparison Note:**  

- Oracle, PostgreSQL, and SQL Server each have slightly different syntax for partial revocations and cascading effects. The general principle remains that revoking privileges can have a chain effect.

**Knowledge Connection:**  

- References the **GRANT and REVOKE** commands discussed in Day 6, emphasizing how revoking privileges can cascade.

**SRE Perspective:**  

- Incorrect revocations can cause outages if essential privileges are accidentally removed from critical service accounts.

**Additional Insight:**  

- Always test changes to roles/privileges in a staging environment to avoid unintended service disruptions.

---

## Answer 10: Database Auditing

🧩 Intermediate | Multiple Choice

**Question:**  
Which scenario BEST illustrates proper auditing for compliance in a database environment?

A. Allowing only the DBA to view logs manually once a month.  
B. Automatically logging all DDL changes (e.g., CREATE TABLE) and storing them in a secured audit table.  
C. Disabling audit logs during peak hours to save I/O resources.  
D. Using a single superuser account with no login trace for faster changes.

**Correct Answer:** B

**Explanation:**  

- Proper auditing involves **logging critical actions** (DDL changes) in a secure, tamper-resistant manner and reviewing them regularly for anomalies. Automated logging is standard for compliance.

**Why other options are incorrect:**  

- **A**: Monthly manual reviews are too infrequent and rely solely on a single person.  
- **C**: Disabling logs can allow malicious or accidental changes to go undetected.  
- **D**: A single superuser account without traceability is a significant compliance and security risk.

**Database Comparison Note:**  

- Oracle has `AUDIT` functionality for DDL statements; PostgreSQL can use extensions like `pgaudit`; SQL Server has an Audit feature within the Security node.

**Knowledge Connection:**  

- Related to Day 6’s **security best practices** including auditing user and admin activities.

**SRE Perspective:**  

- Effective auditing helps detect incidents early, improving reliability and reducing mean time to detect (MTTD).

**Additional Insight:**  

- Store audit data in a secure, separate schema or even a separate system to prevent tampering and performance overhead on the main database.

---

## Answer 11: Availability Challenges

🧩 Intermediate | Multiple Choice

**Question:**  
Which of these is a common challenge to maintaining high database availability?

A. Having roles that are too granular.  
B. Not having a read-only user for reporting.  
C. Single points of failure in database architecture.  
D. Creating too many user accounts.

**Correct Answer:** C

**Explanation:**  

- A single point of failure (e.g., one database server with no standby) can bring the entire system down if that component fails. This is a primary issue for high availability.

**Why other options are incorrect:**  

- **A**: Granular roles can be beneficial if managed well.  
- **B**: Lacking a read-only user is not a direct availability threat (though it can cause performance or security issues).  
- **D**: Many user accounts can be cumbersome but isn’t typically the main factor in availability.

**Database Comparison Note:**  

- Oracle: Data Guard addresses single point of failure.  
- PostgreSQL: Streaming replication or Patroni-based clusters help.  
- SQL Server: Always On Availability Groups is a popular solution.

**Knowledge Connection:**  

- Builds on **SRE Perspective: Database Availability** from Day 6.

**SRE Perspective:**  

- Eliminating single points of failure is central to designing resilient systems that meet strict SLAs.

**Additional Insight:**  

- Always test failover or redundancy features regularly to ensure they work when needed.

---

## Answer 12: Database Security Best Practice

🧩 Intermediate | Fill-in-the-Blank

**Question:**  
Complete the following statement:  
Implementing ________ helps track unauthorized attempts to modify critical database objects and detect potential security breaches early.

A. Connection pooling  
B. Indexing  
C. Auditing  
D. Sharding  

**Correct Answer:** C – Auditing

**Explanation:**  

- **Auditing** logs and monitors changes (especially DDL or privileged commands), helping identify unauthorized or suspicious activities quickly.

**Why other options are incorrect:**  

- **A**: Connection pooling helps manage resource usage, not track unauthorized changes.  
- **B**: Indexing improves query performance but doesn’t detect security breaches.  
- **D**: Sharding distributes data across multiple nodes, not specifically about detecting intrusions.

**Database Comparison Note:**  

- Oracle’s `AUDIT` commands, PostgreSQL’s `pgaudit`, and SQL Server’s Audit feature all serve this purpose.

**Knowledge Connection:**  

- Reinforces **security best practices** from Day 6 regarding user activity monitoring.

**SRE Perspective:**  

- Early detection of unauthorized modifications preserves data integrity and shortens incident response times.

**Additional Insight:**  

- Combine auditing with real-time alerting for best results—just logging is insufficient if no one reviews it promptly.

---

## Answer 13: Syntax Comparison

🧩 Intermediate | Matching

**Question:**  
Match each CREATE USER or equivalent syntax to the correct database system (Column A to Column B):

Column A:  

1. `CREATE USER sarah FOR LOGIN sarah;`  
2. `CREATE ROLE sarah WITH LOGIN PASSWORD 'Pass123';`  
3. `CREATE USER sarah IDENTIFIED BY Pass123;`  
4. `CREATE USER 'sarah'@'localhost' IDENTIFIED BY 'Pass123';`

Column B:  
A. Oracle  
B. SQL Server  
C. PostgreSQL  
D. MySQL  

**Correct Matches:**  
1 – B (SQL Server)  
2 – C (PostgreSQL)  
3 – A (Oracle)  
4 – D (MySQL)

**Explanation:**  

- **SQL Server**: Typically uses `CREATE LOGIN ...; CREATE USER ... FOR LOGIN ...`. The shorthand can be `CREATE USER sarah FOR LOGIN sarah;`.  
- **PostgreSQL**: Has the concept of “roles,” with `WITH LOGIN PASSWORD ...`.  
- **Oracle**: Uses `CREATE USER username IDENTIFIED BY password;`.  
- **MySQL**: Has a host-based syntax, e.g., `CREATE USER 'sarah'@'localhost'`.

**Database Comparison Note:**  

- Highlights how each system’s syntax differs for user creation.

**Knowledge Connection:**  

- Shows how the **user management** concept is universal, though the syntax differs across DBs.

**SRE Perspective:**  

- SREs must be familiar with multiple platforms since large organizations may run different database engines.

**Additional Insight:**  

- Always confirm host-based or domain-based restrictions in MySQL or SQL Server to ensure only valid network paths are allowed.

---

## Answer 14: Permission Assignment Steps

🧩 Intermediate | Ordering

**Question:**  
Arrange the following steps in the correct order when assigning permissions to a new user:

A. Assign appropriate privileges or roles.  
B. Create the user in the database.  
C. Verify privileges by testing with the new user account.  
D. Document the permission changes for audit purposes.

**Correct Order:** B → A → C → D

**Explanation:**  

1. **Create** the user (B).  
2. **Assign** privileges (A).  
3. **Verify** by logging in as that user (C).  
4. **Document** changes for compliance and auditing (D).

**Database Comparison Note:**  

- The general workflow is similar across Oracle, PostgreSQL, and SQL Server, though each has different commands for creation and assignment.

**Knowledge Connection:**  

- Reflects Day 6’s guidance to always test new permissions and keep records.

**SRE Perspective:**  

- Proper logging of user provisioning helps track changes and speeds incident investigation if misconfigurations arise.

**Additional Insight:**  

- In many organizations, an internal ticketing or change management system tracks these steps for accountability.

---

## Answer 15: High Availability Architecture

💡 Advanced/SRE | Multiple Choice

**Question:**  
Which of the following BEST describes a typical high availability architecture for a critical production database?

A. A single primary database with no failover nodes to simplify configuration.  
B. A read-replica that mirrors the primary database asynchronously, used exclusively for reporting.  
C. A cluster of nodes with synchronous replication, automatic failover, and shared storage or data replication across nodes.  
D. A single server where backups are taken weekly, ensuring minimal downtime.

**Correct Answer:** C

**Explanation:**  

- For a **critical production** environment, a cluster-based solution with synchronous replication and automated failover ensures minimal downtime and data loss. This is the gold standard for high availability.

**Why other options are incorrect:**  

- **A**: Single primary = single point of failure.  
- **B**: Asynchronous read replicas are good for performance but can lose data if the primary fails.  
- **D**: Weekly backups alone do not assure high availability; you can still suffer significant downtime.

**Database Comparison Note:**  

- Oracle has **Real Application Clusters (RAC)** or Data Guard.  
- PostgreSQL uses **Patroni**, **pgPool**, or built-in streaming replication.  
- SQL Server offers **Always On Availability Groups** or Failover Cluster Instances.

**Knowledge Connection:**  

- Comes from Day 6’s discussion of **SRE perspective on availability** and redundancy strategies.

**SRE Perspective:**  

- Synchronous replication ensures near-zero data loss. Automatic failover reduces downtime, aligning with strict SLOs.

**Additional Insight:**  

- Test failover procedures regularly. Document them so the on-call engineer can act swiftly during incidents.

---

## Answer 16: SRE Performance Monitoring

💡 Advanced/SRE | Multiple Choice

**Question:**  
Which metric is MOST critical to monitor for early detection of database performance degradation?

A. The color scheme of the admin UI.  
B. The total size of archived audit logs over the past year.  
C. The average query response time and concurrent active sessions.  
D. The number of user accounts in the system.

**Correct Answer:** C

**Explanation:**  

- **Average query response time** and the **number of active sessions** provide direct insight into performance bottlenecks. When response times spike, it’s a key indicator of trouble.

**Why other options are incorrect:**  

- **A**: UI color scheme is aesthetic, not performance-critical.  
- **B**: Past audit log size is not an immediate performance metric.  
- **D**: The number of user accounts doesn’t necessarily reflect real-time load.

**Database Comparison Note:**  

- All major databases provide performance views or tables (Oracle’s AWR, PostgreSQL’s pg_stat_activity, SQL Server’s DMVs) to track query response times and concurrency.

**Knowledge Connection:**  

- Integrates Day 6’s coverage of **database performance metrics** and monitoring solutions.

**SRE Perspective:**  

- Early detection of performance issues prevents escalations that could breach SLAs.

**Additional Insight:**  

- Setting thresholds for average query times can trigger alerts, giving teams time to react before widespread impact.

---

## Answer 17: Incident Response

💡 Advanced/SRE | True/False

**Question:**  
If an SRE team observes a drastic drop in database throughput combined with connection timeouts, the first step is to immediately fail over to the standby without any investigation.

A. True  
B. False

**Correct Answer:** B (False)

**Explanation:**  

- Instantly failing over can cause **unnecessary complexity** or data inconsistency if the root cause is something fixable on the primary. An SRE process typically includes investigating logs, metrics, or potential locks first.

**Database Comparison Note:**  

- The general approach is consistent across all databases: gather diagnostic data, check resource utilization, look for locks or blocked sessions.

**Knowledge Connection:**  

- Relates to the **incident response** and **availability** aspects from Day 6, highlighting the importance of **diagnosis** before major failover actions.

**SRE Perspective:**  

- Minimizing downtime requires systematic triage. Failing over blindly could complicate or prolong recovery.

**Additional Insight:**  

- Some organizations do define an “auto-failover” if specific metrics exceed thresholds, but they typically confirm the cause first to avoid ping-pong failovers.

---

## Answer 18: Least Privilege in High-Traffic Systems

💡 Advanced/SRE | Fill-in-the-Blank

**Question:**  
Complete the statement:  
Applying the principle of least privilege in high-traffic production databases helps minimize the ________ when a compromised account is used for malicious activities.

A. need for logs  
B. blast radius  
C. replication delay  
D. performance overhead  

**Correct Answer:** B – blast radius

**Explanation:**  

- Restricting each user’s privileges ensures that if an attacker compromises one account, their potential to damage or extract data is limited.

**Why other options are incorrect:**  

- **A**: Logging needs remain crucial.  
- **C**: Replication delay is unrelated to user privileges.  
- **D**: While some overhead may exist for permission checks, that’s not the primary concern here.

**Database Comparison Note:**  

- All systems (Oracle, PostgreSQL, SQL Server) benefit from restricted privileges. Implementation specifics (roles vs. individual grants) may differ.

**Knowledge Connection:**  

- Expands on Day 6’s advanced security and SRE synergy concepts around preventing large-scale incidents.

**SRE Perspective:**  

- A smaller blast radius means an incident affects fewer systems and data sets, aligning with reliability goals.

**Additional Insight:**  

- Combine least privilege with strong authentication and auditing to quickly detect compromised credentials.

---

## Answer 19: Advanced Permissions & Roles

💡 Advanced/SRE | Matching

**Question:**  
Match each advanced concept (Column A) with its appropriate description (Column B):

Column A:  

1. Role Inheritance  
2. Row-Level Security  
3. Failover Trigger  
4. Auditing of Superuser Actions  

Column B:  
A. Mechanism that selectively restricts data access at the row level.  
B. Monitoring and logging of all commands run by privileged accounts.  
C. Automatic script or condition to shift database traffic from a failed primary to a standby.  
D. Allowing a role to inherit permissions from another role in a hierarchical manner.

**Correct Matches:**  
1 – D  
2 – A  
3 – C  
4 – B

**Explanation:**  

- (1 → D): Role inheritance means one role can include privileges from another.  
- (2 → A): Row-level security allows restricting data access at a row granularity.  
- (3 → C): A failover trigger is a condition or script that initiates failover.  
- (4 → B): Auditing superuser actions logs privileged commands.

**Database Comparison Note:**  

- **PostgreSQL** has built-in Row-Level Security.  
- **Oracle** uses Virtual Private Database for similar effects.  
- **SQL Server** calls row-level security “RLS.”  
- **Failover** is handled differently across Data Guard, Always On, etc.

**Knowledge Connection:**  

- All are advanced topics covered on Day 6, relevant to **security, availability,** and **reliability**.

**SRE Perspective:**  

- Properly configured advanced permissions and failover triggers are key to maintaining secure, highly available systems.

**Additional Insight:**  

- Enforcing row-level security can reduce data exposure, especially in multi-tenant environments.

---

## Answer 20: SRE Availability Response

💡 Advanced/SRE | Ordering

**Question:**  
Arrange the following steps in the correct order for responding to a severe database availability incident:

A. Assess monitoring metrics (e.g., CPU, memory, I/O).  
B. Identify if failover or partial shutdown is necessary.  
C. Notify stakeholders and the on-call team.  
D. Document the incident in detail for post-mortem analysis.

**Correct Order:** C → A → B → D

**Explanation:**  

1. **Notify stakeholders** (C): Quickly informing the relevant people (on-call team, business owners) ensures timely and coordinated response.  
2. **Assess metrics** (A): Gather data to understand the issue’s scope.  
3. **Identify** a solution (B), e.g., failover or partial shutdown if resource exhaustion is detected.  
4. **Document** the incident (D) thoroughly for future reference and improvements.

**Database Comparison Note:**  

- The response plan is mostly the same for Oracle, PostgreSQL, or SQL Server; differences lie in the commands or tools to evaluate and fail over.

**Knowledge Connection:**  

- Reflects **SRE best practices** from Day 6, focusing on structured incident handling.

**SRE Perspective:**  

- Timely communication (C) is crucial because uncoordinated responses can worsen downtime. Clear steps reduce confusion.

**Additional Insight:**  

- A well-defined runbook ensures each step is followed systematically, preventing panic or oversight during high-pressure incidents.

---

**End of Day 6 Answer Sheet**  
(*Document refers: cnd citeturn2file1*)
