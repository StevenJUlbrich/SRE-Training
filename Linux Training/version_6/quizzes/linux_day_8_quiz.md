
# 📝 Quiz Questions

Test your understanding across tiers. No inline answers are provided; keep an answer key separately.

### 🔍 Beginner Quiz (3–4 Questions)

1. **MCQ**: Which file contains encrypted passwords?
   - a) `/etc/passwd`
   - b) `/etc/shadow`
   - c) `/etc/group`
   - d) `/etc/nsswitch.conf`
2. **MCQ**: What does the `-m` flag do in `useradd`?
   - a) Create user without home directory
   - b) Create user with a home directory
   - c) Lock the user account
   - d) Assign a shell
3. **Fill in the Blank**: `__________ -r bob` removes user bob and their home directory.
4. **Scenario**: How do you quickly see if user `alice` exists on the system?

### 🧩 Intermediate Quiz (3–4 Questions)

1. **Scenario**: You added user `dev2` with `sudo useradd dev2` but forgot `-m`. How do you fix it so `dev2` has a home directory under `/home/dev2`?
2. **MCQ**: If you want to add a user to a new group without removing them from existing groups, which flag must you use with `usermod -G`?
   - a) `-r`
   - b) `-a`
   - c) `-g`
   - d) `-f`
3. **Short Answer**: Which command can retrieve user info from an LDAP server if configured properly?
4. **Scenario**: You need to lock an account `opslead` for two days without deleting it. Which command(s) accomplish this?

### 💡 SRE-Level Quiz (3–4 Questions)

1. **Scenario**: You suspect a compromised service account. Which two immediate steps do you take with user management commands?
2. **MCQ**: Which directive in `/etc/nsswitch.conf` ensures `getent` queries both local files and LDAP for user data?
   - a) `passwd: files ldap`
   - b) `ldap: passwd files`
   - c) `hosts: dns`
   - d) `shadow: sss`
3. **Scenario**: A user `opslead` left the company. Outline the recommended approach (commands/policy) to remove or lock their account while preserving logs.
4. **Short Answer**: Name one advantage of creating a system user with `/usr/sbin/nologin` for running services.
