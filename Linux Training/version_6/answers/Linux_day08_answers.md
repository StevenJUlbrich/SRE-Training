# Day 8 Answers

Below is a suggested **Answer Key** and set of **Explanations** for each quiz question in the Day 8 module.

---

## 🔍 Beginner Quiz – Answers & Explanations

1. **MCQ**: Which file contains encrypted passwords?

   **Answer**: **(b) `/etc/shadow`**  
   **Explanation**: Modern Linux systems store hashed (encrypted) passwords in `/etc/shadow`, which is readable only by root for security reasons. `/etc/passwd` may show an `x` in the password field, indicating the real password data is in `/etc/shadow`.

2. **MCQ**: What does the `-m` flag do in `useradd`?

   **Answer**: **(b) Create user with a home directory**  
   **Explanation**: Using `-m` (short for “make home directory”) instructs `useradd` to automatically create the user’s home directory under `/home/username`, unless otherwise specified. Without `-m`, no home directory is created.

3. **Fill in the Blank**: `__________ -r bob` removes user bob and their home directory.

   **Answer**: **`userdel -r bob`**  
   **Explanation**: `userdel` removes a user account. The `-r` flag ensures the user’s home directory and mail spool are removed as well.

4. **Scenario**: How do you quickly see if user `alice` exists on the system?

   **Answer (One Possible Command)**: `getent passwd alice`  
   **Explanation**: `getent passwd alice` checks all configured name service databases (local `/etc/passwd`, LDAP, etc.) for the user `alice`. Alternatively, running `grep alice /etc/passwd` or `id alice` would also confirm user existence, but `getent` is more complete when remote directories (LDAP) are involved.

---

## 🧩 Intermediate Quiz – Answers & Explanations

1. **Scenario**: You added user `dev2` with `sudo useradd dev2` but forgot `-m`. How do you fix it so `dev2` has a home directory under `/home/dev2`?

   **Answer**:  
   1. Manually create a home directory and set ownership:

      ```bash
      sudo mkdir /home/dev2
      sudo chown dev2:dev2 /home/dev2
      ```

   2. Or use `usermod` to move and create the home automatically:

      ```bash
      sudo usermod -d /home/dev2 -m dev2
      ```

   **Explanation**: The `-m` option with `usermod` moves the existing home directory contents (if any) to the new location. If no home directory existed previously, it creates one. Ensure proper ownership is set.

2. **MCQ**: If you want to add a user to a new group without removing them from existing groups, which flag must you use with `usermod -G`?

   **Answer**: **(b) `-a`**  
   **Explanation**: The `-a` (append) flag with `-G` ensures that the new group is added to the user’s supplementary group list without overwriting the existing memberships. If you omit `-a`, you replace all existing supplementary groups with the new list.

3. **Short Answer**: Which command can retrieve user info from an LDAP server if configured properly?

   **Answer**: **`getent`**  
   **Explanation**: `getent passwd username` (or `getent group groupname`) queries the NSS (Name Service Switch) databases, including local files and any configured LDAP or other directory services.

4. **Scenario**: You need to lock an account `opslead` for two days without deleting it. Which command(s) accomplish this?

   **Answer**:
   - **`sudo usermod -L opslead`** or **`sudo passwd -l opslead`** locks the account by disabling its password.
   - When ready to unlock, you can run **`sudo usermod -U opslead`** or **`sudo passwd -u opslead`**.

   **Explanation**: Locking an account disables password-based logins but preserves the user’s data. You can unlock it later as needed. There’s no built-in “lock for X days” option, so you would manually unlock after two days.

---

## 💡 SRE-Level Quiz – Answers & Explanations

1. **Scenario**: You suspect a compromised service account. Which two immediate steps do you take with user management commands?

   **Answer (Typical Steps)**:
   1. **Lock the account** to prevent further use:

      ```bash
      sudo passwd -l <service_account>
      ```

      or

      ```bash
      sudo usermod -L <service_account>
      ```

   2. **Investigate and kill active sessions** (if needed) and check file ownership:

      ```bash
      pkill -u <service_account>
      find / -user <service_account>
      ```

   After forensics, you can reset the account’s credentials or revoke privileges if confirmed compromised.

   **Explanation**: Locking prevents additional logins. Killing active sessions halts any malicious processes that might be running. Always investigate logs to see what might have been compromised.

2. **MCQ**: Which directive in `/etc/nsswitch.conf` ensures `getent` queries both local files and LDAP for user data?

   **Answer**: **(a) `passwd: files ldap`**  
   **Explanation**: This line instructs the system to first look in local files (i.e. `/etc/passwd`) and then query LDAP if no match is found locally.

3. **Scenario**: A user `opslead` left the company. Outline the recommended approach (commands/policy) to remove or lock their account while preserving logs.

   **Answer (Typical Steps)**:
   1. **Lock the account** (to prevent login):

      ```bash
      sudo usermod -L opslead
      ```

      or

      ```bash
      sudo passwd -l opslead
      ```

   2. **Audit** any running processes or services under `opslead`.
   3. **Archive important data** from the home directory (e.g., `tar` to a secure location).
   4. **Decide on final action**:
      - If needed later for auditing: **keep the locked account** for a specified retention period.
      - If no further need: **`userdel -r opslead`** (but only after confirming data backups).
   5. **Remove or adjust any cron jobs or SSH keys** that `opslead` controlled.

   **Explanation**: This ensures no active processes remain, all data is preserved, and the user cannot log back in. Many companies prefer locking over immediate deletion until an audit is done.

4. **Short Answer**: Name one advantage of creating a system user with `/usr/sbin/nologin` for running services.

   **Answer**:  
   It **prevents interactive logins**, reducing the attack surface if someone tries to compromise the service account.

   **Explanation**: A system user with `/usr/sbin/nologin` (or `/bin/false`) cannot start a shell session, which aligns with the principle of least privilege: the account exists purely to run daemons or services, not for human use.
