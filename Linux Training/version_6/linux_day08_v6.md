# 🚀 **Enhanced Linux SRE Training Module – Day 8: User & Group Management**

Welcome to your comprehensive Day 8 module, combining the best of two existing documents to give you the depth, structure, and clarity needed to master **User & Group Management**. This guide follows a tiered approach, from **Beginner** to **SRE-level**, weaving together security and performance considerations to equip you with robust operational skills.

---

# 📌 Introduction

## Recap of Day 7

Previously, you gained networking skills that included:

- Connectivity testing with `ping`
- Interface and IP management with `ifconfig` and `ip addr`
- Monitoring active connections with `netstat` or `ss`
- Secure remote operations using `ssh` and `scp`

These are crucial for diagnosing network issues and safely transferring data. Now, we progress to **User & Group Management**, a foundational element for system security and multi-user collaboration.

## Why It Matters for SRE

- **Security & Reliability**: Proper user permissions reduce unauthorized access or system outages.
- **Scalability**: Automated user creation and consistent group structures aid large-scale environments.
- **Compliance**: Auditing and correct privilege levels help meet security standards.

## Objectives by Tier

### Beginner

1. Understand the purpose of Linux users and groups
2. Create, remove, and manage basic user and group accounts
3. Learn simple password management

### Intermediate

1. Configure custom home directories, shells, and group memberships
2. Employ automation for onboarding/offboarding
3. Integrate group-based permission strategies for collaboration

### SRE-Level

1. Enforce least privilege with specialized service accounts
2. Implement advanced security policies (e.g., password aging, account locking)
3. Troubleshoot complex permission conflicts and design robust user management workflows

## Connection to Previous & Future Topics

- **Day 7**: Networking knowledge helps secure remote user access.
- **Day 9**: We’ll handle archiving, compression, and package management—processes that often require specific user and group privileges.

---

# 📚 Core Concepts

## Beginner Analogy
>
> Think of Linux users as employees, each with a unique badge (UID) and personal office (home directory). Groups are like departments or project teams. Access to certain "rooms" (directories) depends on which department you belong to.

## Technical Explanation

- **Users**: Each has a unique UID. They own files and run processes.
- **Groups**: Logical collections of users sharing permissions.
- **Root (UID 0)**: The all-powerful administrator.
- **System vs. Regular Users**: System users often run services with minimal or no interactive shell.
- **Security Model**: Access to files and commands depends on user and group ownership, plus configured permissions.

## SRE Application

- **Least Privilege**: SREs create specialized accounts for services, ensuring minimal access to secure production.
- **Automation**: Onboarding/offboarding at scale requires scripts or configuration management tools.
- **Auditing**: Keeping track of who can do what is critical to compliance and reliability.

## System Impact

- **Filesystem & Metadata**: User IDs tie directly to file ownership. Changing or deleting users affects file accessibility.
- **Security**: Improper user management can leave backdoors or over-privileged accounts.
- **Performance**: Large numbers of users can create overhead, but typically minimal unless you run many processes.
- **Monitoring**: Tools like `who`, `last`, or `w` rely on accurate user data.

---

# 💻 Command Breakdown

Below is a detailed breakdown for each primary command:

---

**Command: useradd (User Add)**

**Command Overview:**
Creates new user accounts. This is critical for adding both standard users (humans) and specialized service users (daemons, system services). In SRE contexts, we often script `useradd` to automate user onboarding across fleets.

**Syntax & Flags:**

| Flag/Option | Syntax Example                       | Description                                                           | SRE Usage Context                                             |
|-------------|--------------------------------------|-----------------------------------------------------------------------|----------------------------------------------------------------|
| `-m`        | `useradd -m username`               | Creates a home directory                                              | Ensures each user has an isolated workspace                   |
| `-d`        | `useradd -d /opt/newhome username`   | Specifies a custom home directory                                    | Useful for storing app data in non-standard locations         |
| `-s`        | `useradd -s /bin/zsh username`       | Sets the login shell                                                  | Forces a specific shell environment                           |
| `-G`        | `useradd -G wheel,audit username`    | Adds user to supplementary groups                                    | Grants additional privileges in multiple groups               |
| `-r`        | `useradd -r appservice`             | Creates a system (service) account                                   | Occupies reserved UID ranges, used for daemons/services       |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Create a user with default settings
$ sudo useradd alice
$ tail -n 1 /etc/passwd
alice:x:1001:1001::/home/alice:/bin/bash
```

- 🧩 **Intermediate Example:**

```bash
# Create a user with a custom home directory and Zsh shell
$ sudo useradd -m -d /srv/engineer -s /bin/zsh engineer
$ ls -l /srv/
drwxr-xr-x 2 engineer engineer 4096 Mar 28 10:22 engineer
```

- 💡 **SRE-Level Example:**

```bash
# Create a system user (no login shell) for an application
$ sudo useradd -r -s /usr/sbin/nologin -d /opt/appdata -c "App Service" appuser
$ grep appuser /etc/passwd
appuser:x:499:499:App Service:/opt/appdata:/usr/sbin/nologin

# Typically followed by directory ownership changes:
$ sudo chown -R appuser:appuser /opt/appdata
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Verify creation by checking `/etc/passwd` or `id username`.
- 🧠 **Beginner Tip:** Use `-m` if you want an automatically created home directory.

- 🔧 **SRE Insight:** Creating service accounts with `-r` ensures they’re in the system’s reserved UID range.
- 🔧 **SRE Insight:** Combine `-s /usr/sbin/nologin` or `-s /bin/false` with `-r` to prevent interactive login.

- ⚠️ **Common Pitfall:** Omitting `-m` means no home directory is created, which can break scripts expecting `~/`.
- ⚠️ **Common Pitfall:** Forgetting to set a shell for service accounts can accidentally give them interactive access.

- 🚨 **Security Note:** Lock down service accounts if they don’t need interactive access.
- 💡 **Performance Impact:** Minimal overhead, but in large-scale scenarios, consider automation to handle user sprawl.

---

**Command: userdel (User Delete)**

**Command Overview:**
Removes user accounts from the system. Typically used for offboarding or removing obsolete service accounts. In SRE contexts, ensure you have backups or archives before removing critical user data.

**Syntax & Flags:**

| Flag/Option | Syntax Example         | Description                                             | SRE Usage Context                                       |
|-------------|------------------------|---------------------------------------------------------|---------------------------------------------------------|
| `-r`        | `userdel -r alice`    | Removes the user plus their home directory and mail     | Full cleanup when user fully departs                    |
| `-f`        | `userdel -f bob`      | Forces removal even if the user is logged in            | Urgent scenario but can disrupt active sessions         |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Remove user but keep home directory
$ sudo userdel alice
$ grep alice /etc/passwd  # No results
```

- 🧩 **Intermediate Example:**

```bash
# Remove user and home directory
$ sudo userdel -r dev_user
$ ls /home/
# dev_user directory should be gone
```

- 💡 **SRE-Level Example:**

```bash
# Force removal in an urgent scenario
$ sudo userdel -f riskyuser
# Check leftover files/processes
$ find / -user riskyuser
$ ps -u riskyuser
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Always review the user’s home directory or data prior to deletion.
- 🧠 **Beginner Tip:** Use `-r` with caution if you need to preserve data.

- 🔧 **SRE Insight:** Automate offboarding with backups or archiving before removal.
- 🔧 **SRE Insight:** Maintain clear policies on data retention post-user deletion.

- ⚠️ **Common Pitfall:** Leaving behind home directories can create confusion or security holes.
- ⚠️ **Common Pitfall:** Forceful deletion can kill running processes unexpectedly.

- 🚨 **Security Note:** Quick removal prevents unauthorized reentry by parted users.
- 💡 **Performance Impact:** Deleting large home directories can cause an I/O spike.

---

**Command: usermod (User Modify)**

**Command Overview:**
Modifies properties of existing user accounts, including group memberships, shells, and home directories. SRE teams leverage `usermod` to adjust privileges without re-creating users.

**Syntax & Flags:**

| Flag/Option | Syntax Example                     | Description                                                  | SRE Usage Context                                        |
|-------------|------------------------------------|--------------------------------------------------------------|----------------------------------------------------------|
| `-aG`       | `usermod -aG wheel alice`          | Append user to new supplementary groups                     | Avoid overwriting existing memberships                   |
| `-g`        | `usermod -g engineering alice`     | Change a user’s primary group                               | Realign user to new team or function                    |
| `-L`        | `usermod -L alice`                 | Lock the account (disables password)                         | Temporarily disable access (security measure)           |
| `-U`        | `usermod -U alice`                 | Unlock the account                                           | Re-enable user login                                    |
| `-l`        | `usermod -l newname oldname`       | Rename the user account                                     | Useful for user identity changes                        |
| `-d`        | `usermod -d /new/home alice`       | Change home directory                                       | Move user data to a new location                        |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Add user to one group, preserving other memberships
$ sudo usermod -aG audio alice
$ groups alice
alice : alice audio
```

- 🧩 **Intermediate Example:**

```bash
# Lock a user going on leave
$ sudo usermod -L bob
$ sudo passwd -S bob
bob L 04/01/2025 0 99999 7 -1 (Password locked.)
```

- 💡 **SRE-Level Example:**

```bash
# Rename a user and move their home
$ sudo usermod -l newops oldops
$ sudo usermod -d /home/newops newops
$ sudo chown -R newops:newops /home/newops
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Always include `-a` when adding supplementary groups or you’ll overwrite existing ones.
- 🧠 **Beginner Tip:** Double-check changes using `id username`.

- 🔧 **SRE Insight:** Use account locking (`-L`) for compromised credentials or extended leaves.
- 🔧 **SRE Insight:** Renaming and relocating home directories can be automated with a script to avoid human error.

- ⚠️ **Common Pitfall:** Forgetting `-a` with `-G` can remove all prior groups.
- ⚠️ **Common Pitfall:** Failure to update file ownership after changing username or home directory.

- 🚨 **Security Note:** Lock accounts during investigations rather than deleting them immediately.
- 💡 **Performance Impact:** Typically minimal. Large-scale changes (e.g., mass rename) can cause higher I/O.

---

**Command: groupadd (Group Add)**

**Command Overview:**
Creates new groups to streamline permission management. Group-based strategies significantly reduce overhead when many users share the same resources.

**Syntax & Flags:**

| Flag/Option | Syntax Example         | Description                                | SRE Usage Context                                   |
|-------------|------------------------|--------------------------------------------|-----------------------------------------------------|
| `-g`        | `groupadd -g 1050 dev`| Assign a custom GID                         | Align group IDs across multiple servers or systems  |
| `-r`        | `groupadd -r appgrp`  | Creates a system group (reserved GID range)| For application or service-based group management   |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Create a simple group
$ sudo groupadd marketing
$ grep marketing /etc/group
marketing:x:1002:
```

- 🧩 **Intermediate Example:**

```bash
# Create a group with a specific GID
$ sudo groupadd -g 1500 designers
$ grep designers /etc/group
designers:x:1500:
```

- 💡 **SRE-Level Example:**

```bash
# Create a system group for a specialized microservice
$ sudo groupadd -r secretsvc
$ grep secretsvc /etc/group
secretsvc:x:498:
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Group names should be meaningful and descriptive.
- 🧠 **Beginner Tip:** Verify creation via `/etc/group` or `getent group`.

- 🔧 **SRE Insight:** System groups keep infrastructure accounts separate from normal users.
- 🔧 **SRE Insight:** Consistency across servers is essential. Centralize group definitions if possible.

- ⚠️ **Common Pitfall:** Reusing GIDs can cause permission confusion, especially with shared file servers.
- ⚠️ **Common Pitfall:** Attempting to add users to a group that doesn’t exist can result in errors.

- 🚨 **Security Note:** Restrict membership in privileged groups like `wheel`.
- 💡 **Performance Impact:** Groups themselves don’t consume many resources. The complexity is in membership management.

---

**Command: groupdel (Group Delete)**

**Command Overview:**
Removes groups that are no longer needed. Helps maintain a clean and minimal permission structure. Common for SREs who want to retire old projects or roles.

**Syntax & Flags:**

| Flag/Option | Syntax Example         | Description                                       | SRE Usage Context             |
|-------------|------------------------|---------------------------------------------------|-------------------------------|
| (none)      | `groupdel marketing`  | Removes the group entry from `/etc/group`         | Cleanup of outdated groups    |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Remove a simple group
$ sudo groupdel marketing
$ grep marketing /etc/group  # No output
```

- 🧩 **Intermediate Example:**

```bash
# Delete group and verify users remain unaffected
$ sudo groupdel designers
$ id alice
uid=1001(alice) gid=1001(alice)
```

- 💡 **SRE-Level Example:**

```bash
# In a large environment, confirm no references remain
$ getent group oldgrp
# If no members or references, safely remove
$ sudo groupdel oldgrp
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Ensure no users rely on the group as their primary group.
- 🧠 **Beginner Tip:** Group removal won’t delete user accounts.

- 🔧 **SRE Insight:** Automate stale group removal as part of regular audits.
- 🔧 **SRE Insight:** Maintain consistent group usage documentation to avoid confusion.

- ⚠️ **Common Pitfall:** Deleting a group still in use by active processes or user ownership can cause breakage.
- ⚠️ **Common Pitfall:** Lack of communication can disrupt teams if group-based permissions vanish unexpectedly.

- 🚨 **Security Note:** Removing privileged groups is safer than leaving them dormant.
- 💡 **Performance Impact:** Minimal, but searching for references can spike I/O on large file systems.

---

**Command: passwd (Password Management)**

**Command Overview:**
Sets, changes, or locks/unlocks user passwords. Vital for maintaining secure authentication. SREs enforce password policies or integrate advanced methods (e.g., MFA, LDAP, Kerberos).

**Syntax & Flags:**

| Flag/Option | Syntax Example       | Description                                        | SRE Usage Context                                    |
|-------------|----------------------|----------------------------------------------------|------------------------------------------------------|
| `-l`        | `passwd -l alice`   | Locks the user’s password                          | Prevent login during investigations or leaves        |
| `-u`        | `passwd -u alice`   | Unlocks the user’s password                        | Restores login access after lock                    |
| `-e`        | `passwd -e bob`     | Forces user to change password at next login       | Immediate password rotation                          |
| `-x`        | `passwd -x 90 bob`  | Sets max password age to 90 days                   | Comply with security policies                        |
| `-d`        | `passwd -d bob`     | Removes password, leaving account passwordless     | Rare, for ephemeral container users or special cases |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Change your own password
$ passwd
Changing password for user alice.
Current UNIX password:
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
```

- 🧩 **Intermediate Example:**

```bash
# Lock a user account
$ sudo passwd -l dev_user
passwd: password expiry information changed.
$ sudo passwd -S dev_user
dev_user L 03/28/2025 0 99999 7 -1 (Password locked)
```

- 💡 **SRE-Level Example:**

```bash
# Enforce password expiration policy
$ sudo passwd -x 30 -n 1 -w 7 -i 5 secadmin
# Explanation:
# -x 30 => Max age of 30 days
# -n 1  => Min age of 1 day
# -w 7  => Warn 7 days before expiration
# -i 5  => Disable account 5 days after expiration
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Use strong passwords and change them regularly.
- 🧠 **Beginner Tip:** If you forget your password, root or rescue mode can reset it.

- 🔧 **SRE Insight:** Enforcing password aging policies across many servers can be automated.
- 🔧 **SRE Insight:** Lock compromised accounts immediately while investigating.

- ⚠️ **Common Pitfall:** Accidentally locking essential service accounts.
- ⚠️ **Common Pitfall:** Setting passwordless accounts (`-d`) is a major security risk if not carefully controlled.

- 🚨 **Security Note:** Combine with `/etc/shadow` checks and PAM configurations.
- 💡 **Performance Impact:** Minimal. Large-scale password changes can lead to a surge in support tickets.

---

**Command: /etc/passwd (User Database File)**

**Command Overview:**
A critical text file storing user account information: username, UID, GID, home directory, and shell. Modern systems store actual passwords in `/etc/shadow` for enhanced security.

**Syntax & Flags:**

| Flag/Option      | Syntax Example          | Description                         | SRE Usage Context                |
|------------------|-------------------------|-------------------------------------|----------------------------------|
| N/A (file-based) | `cat /etc/passwd`       | Displays entire file                | Quick check of user accounts     |
| N/A (file-based) | `grep alice /etc/passwd`| Searches for a specific user entry  | Validate user creation           |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# View entire file
$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
...
alice:x:1001:1001::/home/alice:/bin/bash
```

- 🧩 **Intermediate Example:**

```bash
# Search for a particular user
$ grep engineer /etc/passwd
engineer:x:1012:1012:Engineer Account:/home/engineer:/bin/zsh
```

- 💡 **SRE-Level Example:**

```bash
# Programmatically parse /etc/passwd for audits
$ awk -F: '{ printf "User: %s, UID: %s, Home: %s\n", $1, $3, $6 }' /etc/passwd > user_report.txt
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** The `x` in the password field means the real password is in `/etc/shadow`.
- 🧠 **Beginner Tip:** Always keep a backup if you manually edit (or use `vipw`).

- 🔧 **SRE Insight:** Large fleets need programmatic parsing to track accounts.
- 🔧 **SRE Insight:** Compare `/etc/passwd` across servers for consistency.

- ⚠️ **Common Pitfall:** Messing up the format can lock you out of the system.
- ⚠️ **Common Pitfall:** Storing actual passwords here is outdated and insecure.

- 🚨 **Security Note:** `root` ownership and correct file permissions are critical.
- 💡 **Performance Impact:** Reading is trivial. In massive environments, replication or version control matters.

---

**Command: getent (Get Entries)**

**Command Overview:**
Retrieves entries from system databases configured in `/etc/nsswitch.conf`. Vital in environments that use LDAP or other network directories. SREs rely on `getent` to confirm user or group presence across local and remote systems.

**Syntax & Flags:**

| Flag/Option        | Syntax Example           | Description                              | SRE Usage Context                              |
|--------------------|--------------------------|------------------------------------------|------------------------------------------------|
| N/A (database usage)| `getent passwd alice`   | Get user info from the passwd database   | Validate presence in local/remote directories  |
| N/A (database usage)| `getent group devs`     | Get group info                           | Confirm group membership consistency           |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Retrieve local user data
$ getent passwd alice
alice:x:1001:1001::/home/alice:/bin/bash
```

- 🧩 **Intermediate Example:**

```bash
# Check group membership
$ getent group devs
devs:x:1015:bob,carol,dan
```

- 💡 **SRE-Level Example:**

```bash
# Check an LDAP-based user
$ getent passwd ldapuser
ldapuser:*:20010:20010:LDAP Directory User:/home/ldapuser:/bin/bash
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** If no output, the user or group likely doesn’t exist locally or in remote directories.
- 🧠 **Beginner Tip:** Also works for hosts, services, protocols, etc.

- 🔧 **SRE Insight:** Great for verifying LDAP or NIS integration.
- 🔧 **SRE Insight:** Include `getent` checks in provisioning scripts to ensure correct distribution of accounts.

- ⚠️ **Common Pitfall:** Misconfiguration of `/etc/nsswitch.conf` leads to incomplete results.
- ⚠️ **Common Pitfall:** Not all systems have the same NSS backends.

- 🚨 **Security Note:** A compromised LDAP server can lead to wide-scale infiltration.
- 💡 **Performance Impact:** Typically lightweight queries, but repeated calls in large directories can be slow.

---

# 🛠️ System Effects

1. **Filesystem & Metadata**: Changing UIDs or GIDs can orphan files. Removing users also eliminates ownership references.
2. **System Resources**: Each user can run processes, potentially impacting CPU/RAM if usage is unbounded.
3. **Security Implications**: Improperly configured users/groups can allow privilege escalation.
4. **Monitoring Visibility**: Commands like `who` or `last` rely on accurate user login data. Tools like SIEM or centralized logging also track user activity.
5. **Performance Considerations**: Bulk user management (add/delete) can cause I/O spikes. Large-scale queries or directory lookups (LDAP) can slow authentication if not optimized.

---

# 🎯 Hands-On Exercises

Practice is essential. Below are 3 exercises for each skill level.

### 🔍 Beginner Level (3 Exercises)

1. **Basic User Creation**:
   - Use `sudo useradd -m testuser` and then set a password with `passwd testuser`.
   - Verify the user with `id testuser`.
2. **Examine /etc/passwd**:
   - Run `cat /etc/passwd` and locate `testuser`.
   - Identify the 7 fields in that user’s entry.
3. **Delete the User**:
   - Remove `testuser` with `userdel -r testuser`.
   - Verify the user and home directory no longer exist.

### 🧩 Intermediate Level (3 Exercises)

1. **Group Assignment**:
   - Create a group `projectteam` with `sudo groupadd projectteam`.
   - Add a user `projuser` with `sudo useradd -m -G projectteam projuser`.
   - Confirm membership with `groups projuser`.
2. **Lock & Unlock**:
   - Lock `projuser` with `sudo usermod -L projuser`. Verify with `sudo passwd -S projuser`.
   - Unlock with `sudo usermod -U projuser`.
3. **Rename & Move**:
   - Rename `projuser` to `newproj` using `sudo usermod -l newproj projuser`.
   - Move the home directory to `/home/newproj` and update ownership.

### 💡 SRE-Level (3 Exercises)

1. **Service Account Creation**:
   - Create a system user `appsvc` with no login shell: `sudo useradd -r -s /usr/sbin/nologin -d /opt/appsvc appsvc`.
   - Set correct ownership of `/opt/appsvc`.
2. **Password Policy**:
   - Set `appsvc` to expire in 30 days, warn 5 days prior.
   - Confirm with `chage -l appsvc`.
3. **Automated Onboarding**:
   - Write a script that creates a user `teamops`, sets a default password, locks it, and logs creation time in `/var/log/user_mgmt.log`.

---

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

---

# 🚧 Troubleshooting (3 Scenarios)

1. **Locked-Out Admin**
   - **Symptom**: An admin can’t log in despite the correct password.
   - **Cause**: Account locked, password expired, or shell set to nologin.
   - **Diagnostic**: `passwd -S adminuser`, `chage -l adminuser`, check shell in `/etc/passwd`.
   - **Resolution**: Unlock with `passwd -u adminuser` or reset password. Possibly restore shell with `usermod -s /bin/bash adminuser`.
   - **Prevention**: Monitor locked accounts and password expiry.

2. **Group Ownership Confusion**
   - **Symptom**: Files have unknown group IDs or ownership.
   - **Cause**: Group was deleted without reassigning ownership.
   - **Diagnostic**: `ls -l` reveals numeric GID. `getent group <gid>` is empty.
   - **Resolution**: Recreate the group with the same GID or change file ownership.
   - **Prevention**: Audit group usage before removal.

3. **Service Outage After User Removal**
   - **Symptom**: A critical service halts after user removal.
   - **Cause**: That user was the service account.
   - **Diagnostic**: Check logs for `user not found` or permission errors.
   - **Resolution**: Restore or recreate the service account with the correct UID.
   - **Prevention**: Document service accounts thoroughly and lock if unsure.

---

# ❓ FAQ

### 🔍 Beginner FAQ (3)

1. **Q**: How do I see which groups I belong to?
   **A**: Use `groups` or `id`.
2. **Q**: Can I change my own username?
   **A**: Typically requires admin privileges. Use `sudo usermod -l newname oldname`.
3. **Q**: Do I need to log out to see group changes?
   **A**: Yes, or use `newgrp <groupname>` to apply group changes in your current session.

### 🧩 Intermediate FAQ (3)

1. **Q**: Is there a quick way to force **all** users to change passwords on next login?
   **A**: Yes. For each user with a valid UID (e.g., above 1000), run `sudo passwd -e username`. Tools like `chage` or scripts can automate this.
2. **Q**: How can I automate user creation across multiple servers?
   **A**: Use config management tools like Ansible, Puppet, or Chef. They can handle consistent account creation, password setting, and group assignments.
3. **Q**: Can I share a single user account among multiple people?
   **A**: It’s possible but strongly discouraged. Individual accounts are more secure and auditable.

### 💡 SRE-Level FAQ (3)

1. **Q**: We use LDAP/Kerberos for user management. Do these commands still apply?
   **A**: Yes. Commands like `useradd` are for local accounts, but `getent`, `groups`, and `id` still function to query remote directories, based on `/etc/nsswitch.conf`.
2. **Q**: How do I enforce multi-factor authentication on Linux?
   **A**: Integrate PAM modules (e.g., Google Authenticator or Duo). Edit `/etc/pam.d/sshd` or similar to require a second factor.
3. **Q**: Can I mitigate UID collisions in a large environment?
   **A**: Centralize ID management (e.g., with FreeIPA or AD) to ensure unique UID ranges. Manual assignment across hundreds of servers is error-prone.

---

# 🔥 SRE Scenario: Deploying a New Microservice

**Situation**: You’re deploying a containerized microservice that processes sensitive data. Your goal is to set up a secure service account with proper directory permissions, minimal privileges, and monitoring integration.

**Implementation Steps**:

1. **Create a System Group & User**:

   ```bash
   sudo groupadd -r microservice_logs
   sudo useradd -r -s /usr/sbin/nologin -c "Microservice Svc" -d /opt/microservice micro_svc
   ```

   *Reasoning*: `-r` ensures a reserved system UID. No login shell prevents interactive sessions.

2. **Set Up Directories**:

   ```bash
   sudo mkdir -p /opt/microservice/{bin,config,data,logs}
   sudo chown root:root /opt/microservice
   sudo chmod 755 /opt/microservice
   ```

   *Reasoning*: A clear structure isolates files for easy auditing and management.

3. **Assign Ownership & Permissions**:

   ```bash
   # Binaries
   sudo chown root:root /opt/microservice/bin
   sudo chmod 755 /opt/microservice/bin

   # Config
   sudo chown micro_svc:micro_svc /opt/microservice/config
   sudo chmod 750 /opt/microservice/config

   # Data
   sudo chown micro_svc:micro_svc /opt/microservice/data
   sudo chmod 700 /opt/microservice/data

   # Logs
   sudo chown micro_svc:microservice_logs /opt/microservice/logs
   sudo chmod 770 /opt/microservice/logs
   sudo chmod g+s /opt/microservice/logs  # Preserve group ownership
   ```

   *Reasoning*: Restrictive permissions enforce least privilege. Only the service can modify configs and data. The `microservice_logs` group can access logs.

4. **Configure a Systemd Service**:

   ```bash
   sudo bash -c 'cat > /etc/systemd/system/micro_svc.service << EOF
   [Unit]
   Description=Microservice
   After=network.target

   [Service]
   Type=simple
   User=micro_svc
   Group=micro_svc
   ExecStart=/opt/microservice/bin/run.sh
   WorkingDirectory=/opt/microservice
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   EOF'

   sudo systemctl daemon-reload
   sudo systemctl enable micro_svc
   ```

   *Reasoning*: Systemd ensures the service runs with minimal privileges.

5. **Log Rotation & Monitoring**:

   ```bash
   # Logrotate config
   sudo bash -c 'cat > /etc/logrotate.d/microservice << EOF
   /opt/microservice/logs/*.log {
       daily
       missingok
       rotate 7
       compress
       delaycompress
       notifempty
       create 0640 micro_svc microservice_logs
   }
   EOF'
   ```

   *Reasoning*: Proper log rotation avoids disk exhaustion. The microservice_logs group can read logs.

6. **Test & Validate**:
   - Start the service: `sudo systemctl start micro_svc`
   - Check logs: `ls -l /opt/microservice/logs`
   - Confirm correct ownership & permissions: `find /opt/microservice -ls`

7. **SRE Principles**:
   - **Least Privilege**: Minimizes attack surface.
   - **Automation**: Systemd and logrotate ensure continuous, consistent operations.
   - **Observability**: Dedicated log directory and group facilitate monitoring.

---

# 🧠 Key Takeaways

1. **Command Summary (5)**:
   - **useradd**: Create users (human or service).
   - **userdel**: Remove users, optionally cleaning home dirs.
   - **usermod**: Modify existing users (shell, groups, lock/unlock).
   - **groupadd/groupdel**: Manage group lifecycles.
   - **passwd**: Configure password settings and policies.

2. **Operational Insights (3)**:
   - **Least Privilege**: Only grant the exact access users need.
   - **Automation**: Scripts or tools (Ansible, Puppet) streamline user management at scale.
   - **Auditing & Logging**: Keep track of account changes to ensure compliance and traceability.

3. **Best Practices (3)**:
   - **Centralize Management**: Use LDAP or similar for large fleets.
   - **Lock vs. Delete**: Lock accounts when unsure; delete only after confirming no needed resources.
   - **Regular Reviews**: Periodically audit user and group lists to remove stale accounts.

4. **Preview of Next Topic**:
   - **Day 9**: Archiving and compression (e.g., `tar`, `gzip`) plus advanced package management. Critical for backups, deployments, and system updates.

---

# 📚 Further Learning Resources

### 🔍 Beginner (2–3)

1. **Linux.com – Basic User Administration**
   - Link: [https://www.linux.com/training-tutorials/linux-commands-user-administration/](https://www.linux.com/training-tutorials/linux-commands-user-administration/)
   - Teaches: Simple user-related commands, conceptual overview.
   - Applies: Perfect for first-time user management learners.
2. **Ubuntu Official Docs: Add Users**
   - Link: [https://help.ubuntu.com/community/AddUsersHowto](https://help.ubuntu.com/community/AddUsersHowto)
   - Teaches: Step-by-step instructions for Ubuntu-based environments.
   - Applies: Ideal for quick hands-on practice.
3. **Raspberry Pi Documentation**
   - Link: [https://www.raspberrypi.org/documentation/computers/configuration.html](https://www.raspberrypi.org/documentation/computers/configuration.html)
   - Teaches: Beginner-friendly approach to user management in a small-scale environment.
   - Applies: Great for hobbyist or lab settings.

### 🧩 Intermediate (2–3)

1. **Red Hat Enterprise Linux Docs**
   - Link: [https://access.redhat.com/documentation](https://access.redhat.com/documentation)
   - Teaches: Advanced user/group management, SELinux integration.
   - Connects: Well-suited for enterprise scenarios requiring robust security.
2. **DigitalOcean Tutorials: User Management**
   - Link: [https://www.digitalocean.com/community/tags/users](https://www.digitalocean.com/community/tags/users)
   - Teaches: Common tasks for production servers, best practices.
   - Connects: Bridges simpler tasks to operational mastery.
3. **CentOS Project Documentation**
   - Link: [https://docs.centos.org/](https://docs.centos.org/)
   - Teaches: Day-to-day admin tasks and distribution-specific nuances.
   - Connects: Good reference for standard enterprise environments.

### 💡 SRE-Level (2–3)

1. **Google SRE Book**
   - Link: [https://sre.google/sre-book](https://sre.google/sre-book)
   - Teaches: Large-scale account and access management from a reliability perspective.
   - Elevates: Real-world strategies for designing minimal-privilege systems.
2. **PAM (Pluggable Authentication Modules) Advanced Config**
   - Link: [https://www.linux-pam.org/](https://www.linux-pam.org/)
   - Teaches: Fine-tuning authentication, including MFA options.
   - Elevates: Crucial for advanced security measures.
3. **LDAP Administration (OpenLDAP)**
   - Link: [https://www.openldap.org/doc/admin24/](https://www.openldap.org/doc/admin24/)
   - Teaches: Directory services for large user bases.
   - Elevates: Mastering identity management at scale.

---

**Congratulations on completing Day 8**! You can now create and modify Linux user and group accounts with precision, enforce password policies, and design robust permission architectures. Next, we’ll tackle **archiving, compression, and package management**—integral to efficient backups, software distribution, and system maintenance.
