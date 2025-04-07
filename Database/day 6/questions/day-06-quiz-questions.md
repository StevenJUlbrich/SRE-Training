# **20 quiz questions** for Day 6 of the database training module

Covering user accounts, permissions, and the SRE perspective on availability and performance. Each question is labeled with a difficulty level (🔍 Beginner, 🧩 Intermediate, 💡 Advanced/SRE) and follows the required formats and distribution. No answers are provided here; please supply them in a separate answer key document.

---

## 🔍 BEGINNER-LEVEL QUESTIONS (7)

### 1) Multiple Choice

```
## Question 1: Basic User Creation
🔍 Beginner

Which of the following commands correctly creates a new database user named 'analyst_user' in an Oracle environment, with the password 'StrongPass2025'?

A. CREATE ROLE analyst_user IDENTIFIED BY 'StrongPass2025';
B. CREATE USER analyst_user IDENTIFIED BY StrongPass2025;
C. CREATE USER analyst_user IDENTIFIED BY 'StrongPass2025';
D. NEW USER analyst_user WITH PASSWORD='StrongPass2025';
```

---

### 2) Multiple Choice

```
## Question 2: System vs. Object Privileges
🔍 Beginner

Which statement best describes the difference between system privileges and object privileges?

A. System privileges apply only to a single schema, while object privileges apply to all database objects.
B. System privileges allow actions affecting the entire database, while object privileges control access to specific objects like tables or views.
C. System privileges give read-only access, and object privileges give read-write access.
D. System privileges are used only for backup tasks, while object privileges are used only for performance tuning.
```

---

### 3) True/False

```
## Question 3: Principle of Least Privilege
🔍 Beginner

The principle of least privilege states that users should only be granted the minimum permissions they need to perform their tasks effectively.

A. True
B. False
```

---

### 4) True/False

```
## Question 4: Read-Only vs. Read-Write
🔍 Beginner

Granting read/write access to a database user always has lower security risk than granting read-only access.

A. True
B. False
```

---

### 5) Multiple Choice

```
## Question 5: SRE Perspective on Availability
🔍 Beginner

Why is high database availability crucial from an SRE perspective?

A. It guarantees zero user errors.
B. It ensures compliance with data privacy regulations.
C. It directly impacts user experience and potential revenue losses due to downtime.
D. It prevents password sharing among DBAs.
```

---

### 6) Fill-in-the-Blank

```
## Question 6: Permissions Basics
🔍 Beginner

Complete the following statement:

A user with ________ permission can insert new records but cannot create or drop tables.

A. CONNECT
B. SELECT
C. INSERT
D. ALTER
```

---

### 7) Multiple Choice

```
## Question 7: Users vs. Roles
🔍 Beginner

Which of the following is TRUE regarding the difference between users and roles in many relational databases?

A. Users can log in to the database; roles cannot log in.
B. Roles can log in to the database; users cannot log in.
C. Users always have all privileges, but roles have none.
D. There is no difference; 'user' and 'role' are interchangeable terms.
```

---

## 🧩 INTERMEDIATE-LEVEL QUESTIONS (7)

### 8) Multiple Choice

```
## Question 8: Role-Based Permissions
🧩 Intermediate

A database administrator wants to give a "reporting_role" the ability to run SELECT queries on the "sales" schema without letting them modify any data. Which command best achieves this in PostgreSQL?

A. GRANT INSERT ON ALL TABLES IN SCHEMA sales TO reporting_role;
B. GRANT SELECT ON ALL TABLES IN SCHEMA sales TO reporting_role;
C. GRANT ALL PRIVILEGES ON SCHEMA sales TO reporting_role;
D. GRANT USAGE ON SCHEMA sales TO reporting_role;
```

---

### 9) Multiple Choice

```
## Question 9: GRANT vs. REVOKE
🧩 Intermediate

Which of the following statements about the GRANT and REVOKE commands is CORRECT?

A. REVOKE automatically removes all system privileges from every user in the database.
B. GRANT never allows specifying which columns a user can SELECT.
C. REVOKE can remove a privilege from a user, which may also remove privileges from roles that user manages.
D. GRANT only works for object privileges, not system privileges.
```

---

### 10) Multiple Choice

```
## Question 10: Database Auditing
🧩 Intermediate

Which scenario BEST illustrates proper auditing for compliance in a database environment?

A. Allowing only the DBA to view logs manually once a month.
B. Automatically logging all DDL changes (e.g., CREATE TABLE) and storing them in a secured audit table.
C. Disabling audit logs during peak hours to save I/O resources.
D. Using a single superuser account with no login trace for faster changes.
```

---

### 11) Multiple Choice

```
## Question 11: Availability Challenges
🧩 Intermediate

Which of these is a common challenge to maintaining high database availability?

A. Having roles that are too granular.
B. Not having a read-only user for reporting.
C. Single points of failure in database architecture.
D. Creating too many user accounts.
```

---

### 12) Fill-in-the-Blank

```
## Question 12: Database Security Best Practice
🧩 Intermediate

Complete the following statement:

Implementing ________ helps track unauthorized attempts to modify critical database objects and detect potential security breaches early.

A. Connection pooling
B. Indexing
C. Auditing
D. Sharding
```

---

### 13) Matching

```
## Question 13: Syntax Comparison
🧩 Intermediate

Match each CREATE USER or equivalent syntax to the correct database system (Column A to Column B):

Column A:
1. CREATE USER sarah FOR LOGIN sarah;
2. CREATE ROLE sarah WITH LOGIN PASSWORD 'Pass123';
3. CREATE USER sarah IDENTIFIED BY Pass123;
4. CREATE USER 'sarah'@'localhost' IDENTIFIED BY 'Pass123';

Column B:
A. Oracle
B. SQL Server
C. PostgreSQL
D. MySQL
```

---

### 14) Ordering

```
## Question 14: Permission Assignment Steps
🧩 Intermediate

Arrange the following steps in the correct order when assigning permissions to a new user:

A. Assign appropriate privileges or roles.
B. Create the user in the database.
C. Verify privileges by testing with the new user account.
D. Document the permission changes for audit purposes.
```

---

## 💡 ADVANCED/SRE-LEVEL QUESTIONS (6)

### 15) Multiple Choice

```
## Question 15: High Availability Architecture
💡 Advanced/SRE

Which of the following BEST describes a typical high availability architecture for a critical production database?

A. A single primary database with no failover nodes to simplify configuration.
B. A read-replica that mirrors the primary database asynchronously, used exclusively for reporting.
C. A cluster of nodes with synchronous replication, automatic failover, and shared storage or data replication across nodes.
D. A single server where backups are taken weekly, ensuring minimal downtime.
```

---

### 16) Multiple Choice

```
## Question 16: SRE Performance Monitoring
💡 Advanced/SRE

Which metric is MOST critical to monitor for early detection of database performance degradation?

A. The color scheme of the admin UI.
B. The total size of archived audit logs over the past year.
C. The average query response time and concurrent active sessions.
D. The number of user accounts in the system.
```

---

### 17) True/False

```
## Question 17: Incident Response
💡 Advanced/SRE

If an SRE team observes a drastic drop in database throughput combined with connection timeouts, the first step is to immediately fail over to the standby without any investigation.

A. True
B. False
```

---

### 18) Fill-in-the-Blank

```
## Question 18: Least Privilege in High-Traffic Systems
💡 Advanced/SRE

Complete the statement:

Applying the principle of least privilege in high-traffic production databases helps minimize the ________ when a compromised account is used for malicious activities.

A. need for logs
B. blast radius
C. replication delay
D. performance overhead
```

---

### 19) Matching

```
## Question 19: Advanced Permissions & Roles
💡 Advanced/SRE

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
```

---

### 20) Ordering

```
## Question 20: SRE Availability Response
💡 Advanced/SRE

Arrange the following steps in the correct order for responding to a severe database availability incident:

A. Assess monitoring metrics (e.g., CPU, memory, I/O).
B. Identify if failover or partial shutdown is necessary.
C. Notify stakeholders and the on-call team.
D. Document the incident in detail for post-mortem analysis.
```

---

**End of Quiz*ference: citeturn1file0*)
