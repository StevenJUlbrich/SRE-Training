# Quiz questions from the Day 8 module

Each correct answer includes an explanation of why it is correct and why the other choices or approaches are incorrect or less suitable.

---

## 🔍 Beginner Quiz Answers

### 1. **Which file primarily contains encrypted passwords?**  

- **Correct Answer:** (b) `/etc/shadow`

   **Explanation:**

- **(b) `/etc/shadow`** is where modern Linux systems store hashed (encrypted) user passwords. The `/etc/passwd` file no longer contains the actual password—only an `x` placeholder that points to `/etc/shadow`.
- **(a) `/etc/passwd`** holds user account information (UID, GID, home directory, shell) but not the hashed password in modern setups.
- **(c) `/etc/group`** contains group information (group name, GID, members), not individual user passwords.
- **(d) `/etc/nsswitch.conf`** determines how system databases (e.g., passwd, group) are queried (files, LDAP, etc.) but does not store passwords.

---

### 2. **What is the `-m` flag in `useradd` used for?**  

- **Correct Answer:** (b) Create user with a home directory

   **Explanation:**

- **(b)** When you run `useradd -m username`, it automatically creates a home directory (usually `/home/username`).  
- **(a)** Creating a user *without* a home directory is the default if you omit `-m`.  
- **(c)** Locking the user account is not done with `-m`; instead, you’d use `usermod -L` or `passwd -l`.  
- **(d)** Assigning a shell can be done with `-s /path/to/shell`, not `-m`.

---

### 3. **Fill in the Blank:** `__________ -r bob` removes the user bob and their home directory  

- **Correct Answer:** `userdel`

   **Explanation:**

- The command is `userdel -r bob`. The `-r` flag removes both the user account and the user’s home directory (and mail spool, if present).
- Other commands (e.g., `useradd`, `usermod`) do not delete accounts.
- `passwd -r bob` is invalid syntax for removing accounts.

---

### 4. **Scenario:** You need to quickly see if user `alice` exists. Which command do you run?  

- **One Good Answer:** `id alice`

   **Explanation:**  

- `id alice` shows you whether `alice` is recognized by the system, returning UID/GID info if the user exists or an error if not.
- `getent passwd alice` is also acceptable: if `alice` is listed in local files or LDAP, it will show the corresponding entry.
- `grep alice /etc/passwd` can work locally, but it won’t account for LDAP or other directory services.
- `useradd alice` would attempt to *create* a user named `alice`, which isn’t what you want if you’re just verifying existence.

---

## 🧩 Intermediate Quiz Answers

### 1. **Scenario:** You created a user `dev2` with `sudo useradd dev2` but forgot `-m`. How do you fix it so `dev2` gets a home directory under `/home/dev2`?

- **One Good Approach:**  
     1. Create the directory manually:  

        ```bash
        sudo mkdir /home/dev2
        ```  

     2. Use usermod to point the user to that directory (and move any existing files if needed):  

        ```bash
        sudo usermod -d /home/dev2 -m dev2
        ```  

     3. Ensure ownership matches:  

        ```bash
        sudo chown dev2:dev2 /home/dev2
        ```  

   **Explanation:**  

- The `-d` option with `usermod` changes the home directory path.  
- The `-m` option with `usermod` attempts to move existing user files from an old home directory to the new one; even if no old directory exists, it ensures a proper transfer/migration.  
- Simply deleting and re-creating the user might cause confusion or data loss if the user had begun storing files somewhere else.  

---

### 2. **If you want to add a user to a new group without removing them from other groups, which flag must be used?**  

- **Correct Answer:** (b) `-a`

   **Explanation:**

- **(b) `-a`** stands for “append” and prevents overwriting the user’s existing supplementary groups. The full syntax is typically `usermod -aG group user`.  
- **(a) `-r`** is used for creating a system user/group, not appending user group memberships.  
- **(c) `-g`** changes the *primary* group of the user, possibly removing them from existing supplementary groups if you do not use `-aG`.  
- **(d) `-f`** is a “force” option in some commands (`userdel`, `fsck`), not relevant here.

---

### 3. **Which command can retrieve user info from an LDAP server if configured properly?**  

- **Correct Answer:** `getent`

   **Explanation:**  

- **`getent passwd username`** queries the passwd database according to `/etc/nsswitch.conf`, which can include LDAP, NIS, or other directory services.  
- `id username` may not show LDAP users if `nsswitch.conf` is not configured properly.  
- `grep` alone only checks local files, not external directories.  
- `useradd` doesn’t retrieve info— it creates local accounts.

---

## 💡 SRE-Level Quiz Answers

### 1. **Scenario:** You suspect a compromised service account. Which two immediate steps do you take using user management commands?

- **One Good Answer:**  
     1. **Lock/Disable the Account:**  

        ```bash
        sudo usermod -L compromised_svc
        ```

        or  

        ```bash
        sudo passwd -l compromised_svc
        ```

        This prevents new logins under that account.  
     2. **Force Password Reset or Investigate/Remove Credentials:**  

        ```bash
        sudo passwd -e compromised_svc
        ```

        This ensures that the account cannot be reused without a new secure password.  

   **Explanation:**

- Locking the account halts any immediate unauthorized use.  
- Requiring a password reset (or removing credentials entirely) ensures that even if an attacker had the old password, they can’t reuse it.  
- You might also kill active processes belonging to that account and examine logs, but the two essential *user management commands* are lock and force reset.

---

### 2. **Which directive in `/etc/nsswitch.conf` ensures `getent` queries both local files and LDAP?**  

- **Correct Answer:** (a) `passwd: files ldap`

   **Explanation:**

- **(a)** Telling the system to look in local `files` first, then `ldap`, ensures `getent passwd` (and other queries) can retrieve user info from both sources.  
- **(b) `ldap: passwd files`** is incorrect syntax because it would indicate a database named `ldap` at the top level, which is typically not how nsswitch lines are structured.  
- **(c) `hosts: dns`** pertains to hostnames/IP lookups, not user accounts.  
- **(d) `shadow: sss`** is for integrating with SSSD or other backends for the `shadow` database, not `passwd`.  

---

### 3. **Scenario:** A user `opslead` left the company. Outline the recommended approach (commands/policy) to fully remove or lock their account while preserving logs

- **One Good Answer (Step-by-step):**  
     1. **Lock the account** to prevent logins:

        ```bash
        sudo usermod -L opslead
        ```

     2. **Investigate file ownership**:

        ```bash
        sudo find / -user opslead -exec ls -l {} \\; > /tmp/opslead_files.txt
        ```

     3. **Archive home directory**:

        ```bash
        sudo tar -czf /backup/opslead_home_$(date +%Y%m%d).tar.gz /home/opslead
        ```

     4. **Remove or keep locked** depending on policy:
        - If you need a record, keep the account locked indefinitely.  
        - If you want a full removal:

          ```bash
          sudo userdel -r opslead
          ```

     5. **Preserve logs**: Do not delete system or application logs referencing `opslead`; ensure compliance teams have a record.

   **Explanation:**

- Lock first to block unauthorized access.  
- Find & archive files for data retention and forensics.  
- Use `userdel -r` only after archiving if you must remove the account entirely.  
- This approach balances security (no active login) and operational needs (preserving data/logs).

---

### 4. **Name one advantage of specifying a system user with `-r` and shell `/usr/sbin/nologin` for running daemons.**

- **Correct Answer (Sample)**:  
  - “It prevents interactive logins, reducing security risk if attackers obtain the account credentials, while also ensuring the UID is in the reserved system range.”

   **Explanation:**

- A **system user** created with `-r` typically has a UID below 1000, clearly marking it as non-human.  
- `/usr/sbin/nologin` (or `/bin/false`) disallows normal shell access, so attackers cannot log in interactively.  
- This adheres to the **principle of least privilege**, limiting how much damage a compromised daemon account can do.

---

### Final Note

These detailed explanations clarify each correct answer and contrast it with the other choices or approaches. By understanding *why* an answer is correct (and why other options are not), students and practitioners gain deeper insights into Linux user/group management best practices.
