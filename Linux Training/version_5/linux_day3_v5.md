# 🚀 **Linux SRE Training Module - Day 3: Permissions & Ownership**

## 📌 **Introduction**

Welcome to **Day 3** of our Linux SRE Training! Today, we'll tackle **file permissions and ownership**—essential building blocks for any Linux environment.

### **Why Permissions & Ownership Matter**

Permissions control **who** can **read**, **write**, or **execute** files and directories. Ownership determines **which user** (and group) is responsible for those files. From an SRE perspective, properly managed permissions help ensure:

- **Security**: Preventing unauthorized access or changes
- **Reliability**: Guaranteeing that services can read configurations and write logs
- **Traceability**: Identifying which user or group last modified a critical file

### **Objectives**

#### **Beginner-Level (Tier 1)**

1. Explain the fundamentals of `rwx` permissions
2. Use `chmod` to modify permissions in a simple manner
3. Understand `sudo` as a tool for administrative actions

#### **Intermediate-Level (Tier 2)**

1. Apply numeric and symbolic permission setting methods
2. Change ownership and group ownership with `chown` and `chgrp`
3. Combine permissions knowledge in real-world scenarios (e.g., controlling access to shared directories)

#### **SRE-Level (Tier 3)**

1. Demonstrate advanced permission strategies (sticky bit, setuid, setgid)
2. Troubleshoot permission-denied errors in production environments
3. Incorporate permissions best practices and security policies into automated workflows

### **Connection to Previous and Future Topics**

- **From Day 2**: You learned file manipulation (creating, moving, removing). Now you'll control who can do these actions.
- **Coming Up**: Day 4 will focus on advanced text processing with `grep`, `find`, and piping, vital for log analysis and system investigations.

---

## 📚 **Core Concepts**

### **1. The `rwx` Permission Trio**

- **Read (r)**: View or list contents
- **Write (w)**: Modify or create/delete
- **Execute (x)**: Run as a program or traverse directories

Each file or directory has three sets of permissions: one for the **owner**, one for the **group**, and one for **others**.

### **2. Ownership Structure**

- **User (Owner)**: Typically the file creator
- **Group**: A collection of users
- **Others**: Everyone else with no special association

### **3. SRE Application**

- Protect configuration files from unauthorized changes
- Ensure only the correct service user can write logs
- Implement the principle of least privilege in production

### **4. System Impact**

- **Filesystem**: Permission bits stored as part of file metadata
- **Security**: Misconfigured permissions can lead to security breaches
- **Performance**: Overly broad permissions can lead to resource misuse
- **Monitoring**: Tools like `ls -l`, `stat`, or security scanners highlight permission anomalies

---

## 💻 **Command Breakdown**

Below are the four key commands: **chmod**, **chown**, **chgrp**, and **sudo**. Each follows this structure:

---

### **Command: chmod (Change File Mode Bits)**

**Command Overview:**
`chmod` allows you to modify the permissions (read, write, execute) for a file or directory. SREs often use `chmod` to ensure that processes have the right level of access—nothing more, nothing less.

**Syntax & Flags:**

| Flag/Option | Syntax Example              | Description                                                       | SRE Usage Context                                              |
|-------------|-----------------------------|-------------------------------------------------------------------|----------------------------------------------------------------|
| `-R`        | `chmod -R 755 /var/www`    | Apply permissions recursively to a directory and its contents     | Deploying web apps, adjusting permissions en masse             |
| (none)      | `chmod 644 config.yaml`    | Change permissions using numeric or symbolic modes                | Basic single-file permission changes                           |
| (none)      | `chmod u+x script.sh`      | Symbolic mode to add execute permission for the owner             | Granting a script run capability without affecting other perms |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# Grant read, write to the owner, read-only to group and others
$ chmod 644 notes.txt
-rw-r--r-- 1 user user 0 Mar 29 10:00 notes.txt
# Explanation: Numeric notation 644 sets owner=rw, group=r, others=r
```

- 🟡 **Intermediate Example:**

```bash
# Recursively set owner full permissions, group read and execute, others no access
$ chmod -R 750 /home/shared
# Explanation: 7 (rwx) for owner, 5 (r-x) for group, 0 (---) for others
# Operational Significance: Restricts a shared folder for tighter control
```

- 🔴 **SRE-Level Example:**

```bash
# Symbolically add the sticky bit to a directory for shared files
$ chmod +t /var/public_drop
# Explanation: The sticky bit (+t) means only the file owner can delete files
# Production Relevance: Used in multi-user directories to prevent accidental deletions
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Numeric mode (e.g., 755, 644) is concise, but symbolic mode (u+r, g-w, etc.) is more intuitive.
- 🧠 **Beginner Tip:** Always verify results with `ls -l` to confirm the new permissions.

- 🔧 **SRE Insight:** Automate permission changes in deployment scripts to avoid manual drift.
- 🔧 **SRE Insight:** Use consistent `umask` settings for newly created files, preventing over-permissive defaults.

- ⚠️ **Common Pitfall:** Setting `777` on directories can create security holes.
- ⚠️ **Common Pitfall:** Forgetting `-R` on directories when you intend to change all nested files.

- 🚨 **Security Note:** Overly liberal permissions can allow malicious users to alter or delete critical files.
- 💡 **Performance Impact:** Minimal direct performance impact, but setting correct permissions can prevent resource exhaustion from unauthorized scripts.

---

### **Command: chown (Change File Owner)**

**Command Overview:**
`chown` changes the ownership of a file or directory, typically requiring elevated privileges. SREs use `chown` to ensure that services run under the correct user, aligning ownership with system roles.

**Syntax & Flags:**

| Flag/Option | Syntax Example               | Description                                                          | SRE Usage Context                                           |
|-------------|------------------------------|----------------------------------------------------------------------|-------------------------------------------------------------|
| `-R`        | `chown -R alice /var/data`  | Recursively change ownership of a directory and contents            | Migrating ownership for entire app directories              |
| (none)      | `chown bob config.yml`       | Change the owner of a single file                                   | Adjusting ownership after manual file creation              |
| `:<group>`  | `chown bob:devteam file.txt` | Change both owner and group in one command                          | Setting up multi-user collaborative environment             |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# Change the file owner to 'student'
$ sudo chown student class_notes.txt
# Explanation: Owner is now 'student'. Group remains unchanged.
```

- 🟡 **Intermediate Example:**

```bash
# Recursively change the owner of a directory to 'webuser'
$ sudo chown -R webuser /var/www/app
# Operational Context: In a dev environment, ensuring webuser can manage these files
```

- 🔴 **SRE-Level Example:**

```bash
# Transfer ownership of logs to a specialized logs group
$ sudo chown root:loggrp /var/log/myapp.log
# Explanation: The 'loggrp' group can read/write logs under root supervision
# Production Relevance: Helps implement compliance measures for log management
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** You must be the file owner or have sudo privileges to change ownership.
- 🧠 **Beginner Tip:** Verify the user or group exists before using `chown`.

- 🔧 **SRE Insight:** For large-scale systems, standardize ownership across environments to avoid confusion.
- 🔧 **SRE Insight:** Use `chown user:group` to set both user and group at once.

- ⚠️ **Common Pitfall:** Accidentally breaking services by changing ownership to the wrong user.
- ⚠️ **Common Pitfall:** Recursively altering `/` or critical system directories, causing system-wide issues.

- 🚨 **Security Note:** Restrict `sudo chown` usage to authorized admins. Misuse can lead to privilege escalation.
- 💡 **Performance Impact:** Typically none, unless it triggers large-scale changes on huge directory trees.

---

### **Command: chgrp (Change Group Ownership)**

**Command Overview:**
`chgrp` adjusts the group ownership of a file or directory. SREs commonly use it to grant a group of users shared access to logs or config files without altering the file's individual owner.

**Syntax & Flags:**

| Flag/Option | Syntax Example               | Description                                                      | SRE Usage Context                                   |
|-------------|------------------------------|------------------------------------------------------------------|-----------------------------------------------------|
| `-R`        | `chgrp -R analytics /data`  | Recursively change group ownership for a directory and contents | Data science or log analysis requiring group access |
| (none)      | `chgrp devteam source.cpp`   | Change the group of a single file                               | When developers collaborate on a shared code file   |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# Change group ownership to 'developers'
$ sudo chgrp developers docs/
# Explanation: All users in 'developers' group can now share doc access
```

- 🟡 **Intermediate Example:**

```bash
# Recursively grant 'auditteam' group ownership of log files
$ sudo chgrp -R auditteam /var/log/secure_app
# Operational Context: Allows a specialized team to read secure logs
```

- 🔴 **SRE-Level Example:**

```bash
# Rotate group ownership for phased maintenance schedules
$ sudo chgrp -R maintwindow /usr/local/maintenance_scripts
# Production Relevance: Different teams maintain systems in assigned windows
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** This command only changes group ownership, not the file’s owner.
- 🧠 **Beginner Tip:** Confirm new group ownership with `ls -l`.

- 🔧 **SRE Insight:** Combine `chown user:group` and `chgrp group` effectively to manage multi-tenant systems.
- 🔧 **SRE Insight:** Align group membership in `/etc/group` or LDAP for streamlined user management.

- ⚠️ **Common Pitfall:** Omitting the `-R` flag when you intend to change all nested files.
- ⚠️ **Common Pitfall:** Using a group name that doesn’t exist or is misspelled.

- 🚨 **Security Note:** Group misconfiguration can inadvertently expose or hide files from the correct team.
- 💡 **Performance Impact:** Large directory trees might experience brief overhead while applying group changes.

---

### **Command: sudo (Superuser Do)**

**Command Overview:**
`sudo` temporarily grants root (or another user’s) privileges to run administrative commands. For an SRE, `sudo` is a gateway to higher privileges, vital for changing system-wide configurations and ownership.

**Syntax & Flags:**

| Flag/Option | Syntax Example          | Description                                                 | SRE Usage Context                                      |
|-------------|-------------------------|-------------------------------------------------------------|----------------------------------------------------------|
| `-i`        | `sudo -i`              | Open a root shell as if the user is root                    | Deep system changes or investigating critical issues     |
| `-l`        | `sudo -l`              | List allowed and forbidden commands for the current user    | Auditing privileges, verifying least-privilege settings  |
| (none)      | `sudo systemctl start` | Run a command (here, systemctl) with elevated privileges    | Restarting critical services without logging in as root  |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# Update package lists
$ sudo apt update
# Explanation: The user is briefly elevated to root to fetch package info
```

- 🟡 **Intermediate Example:**

```bash
# Edit a critical config file
$ sudo vim /etc/nginx/nginx.conf
# Operational Significance: The file belongs to root, so normal users need sudo
```

- 🔴 **SRE-Level Example:**

```bash
# Investigate allowed privileges for a specific user in complex environments
$ sudo -l -U devopsuser
# Production Relevance: Confirms if devopsuser can run certain commands under certain conditions
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Always double-check your commands before pressing Enter under sudo—no undo button.
- 🧠 **Beginner Tip:** `sudo !!` repeats the last command with sudo privileges, but be cautious.

- 🔧 **SRE Insight:** Restrict sudo in `/etc/sudoers` or via polkit for precise role-based privilege.
- 🔧 **SRE Insight:** Logs of sudo usage can provide an audit trail, essential in regulated environments.

- ⚠️ **Common Pitfall:** Using `sudo` too freely leads to potential system compromises.
- ⚠️ **Common Pitfall:** Running interactive scripts (like editors) with `sudo` in the wrong environment can cause file ownership mix-ups.

- 🚨 **Security Note:** Maintaining a minimal set of sudo commands helps preserve the principle of least privilege.
- 💡 **Performance Impact:** Minimal direct performance effect, but unrestrained sudo usage can cause accidental resource mismanagement.

---

## 🛠️ **System Effects**

1. **Filesystem & Metadata**: Permissions are stored in the inode. Adjusting permissions means rewriting inode data.
2. **System Resources**: Minimal overhead in setting permissions unless large-scale directory changes are involved.
3. **Security**: Proper permissions form your first defense line, especially in multi-user or multi-service setups.
4. **Monitoring Visibility**: Tools like `ls -l`, `stat`, and system logs help track permission changes. SREs frequently automate these checks.

---

## 🎯 **Hands-On Exercises**

### **Beginner Tier (3 Exercises)**

1. **Basic Permissions:**
   - Create a file named `myfile.txt`. Set permissions so only you (the owner) can read and write, while group and others have no permissions.
   - Confirm using `ls -l myfile.txt`.

2. **Symbolic vs. Numeric:**
   - Copy `myfile.txt` to `myfile_copy.txt`.
   - Use symbolic notation to give yourself execute permission on the new file.
   - Use numeric notation to restore to `644`.

3. **Simple Ownership Check:**
   - Create a directory `beginner_dir`.
   - Run `ls -ld beginner_dir` to check its owner and group.
   - If available, change the directory’s owner to another local user (e.g., `sudo chown anotheruser beginner_dir`).

### **Intermediate Tier (3 Exercises)**

1. **Recursive Changes:**
   - Create a directory structure `projects/java_app/src`.
   - Place sample files in each subdirectory.
   - Recursively set everything under `java_app` to `750`.
   - Verify each file/directory’s permissions.

2. **Group Collaboration:**
   - Create a group named `devteam` (if permissible).
   - Set a shared directory `shared_docs` owned by your user but group-owned by `devteam`.
   - Give the group read and write permissions, but no access to others.

3. **sudo Usage Review:**
   - Run `sudo -l` to list allowed commands.
   - Attempt to edit a root-owned file (e.g., `/etc/hosts`).
   - Observe the difference when editing with and without `sudo`.

### **SRE-Level Tier (3 Exercises)**

1. **Sticky Bit for Shared Folder:**
   - Create a directory `/srv/public_drop` accessible by a shared group.
   - Add the sticky bit so only owners can delete their own files.
   - Test by creating files as different users.

2. **Setuid & Security Checks:**
   - Identify any files with the setuid bit: `sudo find / -perm -4000 -type f 2>/dev/null`.
   - Document at least one binary with setuid. Investigate if it’s required or not.

3. **Advanced Permission Automation:**
   - Write a short shell script that ensures `/var/log/myservice` is always owned by `myserviceuser` and group `logs`, with `750` permissions.
   - Automate its execution via cron or systemd timer.

---

## 📝 **Quiz Questions**

### **Beginner Tier (3–4 Questions)**

1. **Which permission bits are represented by `755`?**
   - A) Owner can read/write, group can read, others no permissions
   - B) Owner can read/write/execute, group can read/execute, others can read/execute
   - C) Owner can read/write, group and others can only read

2. **True/False**: `chmod +x script.sh` sets execute permission for all users.

3. **Fill in the Blank**: To change the owner of `fileA.txt` to user `bob`, you would use `____ bob fileA.txt`.

### **Intermediate Tier (3–4 Questions)**

1. **Match the numeric notation to symbolic notation**:
   - `600` → `__?__`
   - `775` → `__?__`
   - `444` → `__?__`

2. **Scenario**: A file `report.csv` has permissions `rw-r--r--`. Which command restricts it so only the owner can read and write?
   - A) `chmod 644 report.csv`
   - B) `chmod 600 report.csv`
   - C) `chmod u+w,go-r report.csv`

3. **Multiple Choice**: You need to give the group write permission but not others on `shared_notes.txt`. Which symbolic option is correct?
   - A) `chmod g+w,o-r shared_notes.txt`
   - B) `chmod ug+w shared_notes.txt`
   - C) `chmod 770 shared_notes.txt`

4. **True/False**: Using `sudo chown -R user:group /home/user` will also change hidden files inside `/home/user`.

### **SRE-Level Tier (3–4 Questions)**

1. **Short Answer**: Name two reasons setuid bits are considered high risk.
2. **Multiple Choice**: You see `-rwsr-xr-x` on `/usr/bin/passwd`. Which statement is **true**?
   - A) The setuid bit is set, so it runs with the owner’s permissions.
   - B) The sticky bit is set, so it can’t be deleted by others.
   - C) This file is missing the owner execute bit.

3. **Scenario**: A service fails to read its config file in `/etc/app`. Which command best helps you confirm if permissions are the cause?
   - A) `sudo ls -lt /etc/app`
   - B) `sudo cat /etc/app/config.yaml`
   - C) `stat /etc/app/config.yaml`

4. **True/False**: Setting the sticky bit on a file ensures only the root user can execute it.

---

## 🚧 **Troubleshooting (3 Scenarios)**

1. **Scenario**: Permission Denied on Application Startup
   - **Symptoms**: Service logs show `Permission denied` accessing `/var/log/app/app.log`.
   - **Diagnostics**: Check ownership: `ls -l /var/log/app/app.log` → Owned by `root:root`.
   - **Solution**: `sudo chown appuser:appgroup /var/log/app/app.log` and `chmod 660`.
   - **Prevention**: Ensure log directories are always correct in deployment scripts.

2. **Scenario**: Group Collaboration Failure
   - **Symptoms**: Team members can’t edit each other’s files in a shared directory.
   - **Diagnostics**: Confirm group membership with `groups username`.
   - **Solution**: `sudo chgrp devteam /shared/dir && chmod 770 /shared/dir`.
   - **Prevention**: Regularly verify group ownership and membership.

3. **Scenario**: Mysterious 503 Errors on Web Server
   - **Symptoms**: The web server can’t read a critical config file after an update.
   - **Diagnostics**: `ls -l /etc/nginx/nginx.conf` shows `rw------- root root`.
   - **Solution**: `sudo chmod 644 /etc/nginx/nginx.conf` so the nginx user can read it.
   - **Prevention**: Automated checks or CI pipeline verifying file permissions.

---

## ❓ **FAQ**

### **Beginner FAQs** (3 total)

1. **Q**: Do I always need `sudo` to change permissions?
   - **A**: You can change permissions on files you own without sudo, but to modify files owned by another user, you need elevated privileges.

2. **Q**: What’s the difference between numeric and symbolic chmod?
   - **A**: Numeric uses three (or four) digits to define exact permissions. Symbolic uses letters and operators (u, g, o, +, -, =) to incrementally adjust permissions.

3. **Q**: How do I see if a file is executable?
   - **A**: Run `ls -l filename` and check for the `x` in the permission bits.

### **Intermediate FAQs** (3 total)

1. **Q**: Can I change both owner and group together?
   - **A**: Yes, with `sudo chown user:group filename`. This is common when transferring files across teams.

2. **Q**: How do I remove execute permission from only the owner?
   - **A**: `chmod u-x file`. Symbolic notation works well for granular changes.

3. **Q**: Are group permissions automatically applied if a user is in the group?
   - **A**: Yes, once the file is group-owned, any user in that group has those group-level permissions. Just confirm the user’s session recognizes the group membership.

### **SRE-Level FAQs** (3 total)

1. **Q**: Can SELinux or AppArmor override traditional `rwx` permissions?
   - **A**: Yes. SELinux and AppArmor implement mandatory access control, which can deny access even if `rwx` says otherwise.

2. **Q**: What’s the difference between `setuid` and `sudo`?
   - **A**: `setuid` permanently imbues an executable with the owner’s privileges, whereas `sudo` dynamically grants privileges based on user authentication.

3. **Q**: Do logs track who changed permissions?
   - **A**: On many distros, yes. `sudo` usage is logged in `/var/log/auth.log` (Debian/Ubuntu) or `/var/log/secure` (RHEL/CentOS). For advanced auditing, configure `auditd`.

---

## 🔥 **SRE Scenario**

**Incident**: Your production monitoring tool can’t write to its logs, causing alert flooding. Fix it!

1. **Check the process owner**:

   ```bash
   ps aux | grep monitoring_tool
   ```

   _Reasoning_: Identify which user runs the tool, e.g., `monuser`.

2. **Inspect log file permissions**:

   ```bash
   ls -l /var/log/monitoring_tool/monitor.log
   ```

   _Reasoning_: Confirm if it’s owned by `root` or if `monuser` lacks write permission.

3. **Change ownership if needed**:

   ```bash
   sudo chown monuser:monuser /var/log/monitoring_tool/monitor.log
   ```

   _Reasoning_: The logging user must own or at least have write privileges.

4. **Adjust permissions**:

   ```bash
   sudo chmod 640 /var/log/monitoring_tool/monitor.log
   ```

   _Reasoning_: Owner read/write, group read, others none.

5. **Validate logging**:

   ```bash
   sudo -u monuser echo "Test log entry" >> /var/log/monitoring_tool/monitor.log
   ```

   _Reasoning_: Confirms that the user can now write logs.

6. **Restart the service**:

   ```bash
   sudo systemctl restart monitoring_tool
   ```

   _Reasoning_: Ensures fresh startup with correct permissions.

7. **Implement a check**:

   ```bash
   # Possibly add a script or systemd unit that verifies permissions at each boot
   ```

   _Reasoning_: Automated guard to prevent future incidents.

---

## 🧠 **Key Takeaways**

1. **Command Summary**:
   - `chmod`: Adjusts file/directory permissions
   - `chown`: Changes file ownership
   - `chgrp`: Changes group ownership
   - `sudo`: Elevates privileges for administrative tasks
   - `ls -l`: Primary way to view permission bits

2. **Operational Insights**:
   1. Permissions directly impact service stability; misconfigured permissions can cause outages.
   2. Automated scripts help enforce consistent permissions across environments.
   3. Using groups strategically streamlines multi-user collaboration.

3. **Best Practices**:
   1. Keep to the principle of least privilege—never grant more permission than necessary.
   2. Always confirm user and group existence before applying `chown` or `chgrp`.
   3. Leverage sticky bits, setuid, and setgid carefully to avoid security vulnerabilities.

4. **Preview of Next Topic**:
   - Tomorrow, we’ll delve into **text processing** with tools like `grep`, `find`, and piping/redirection—vital for log analysis, searching large codebases, and building SRE scripts.

---

## 📚 **Further Learning Resources**

### **Beginner (2–3 Resources)**

1. [Linux File Permissions Basics (Ubuntu Docs)](https://help.ubuntu.com/community/FilePermissions)
   - Explains `rwx` in simple terms
   - Perfect for new Linux users exploring their home directories
2. [chmod Fundamentals (Linuxize)](https://linuxize.com/post/how-to-use-chmod-command/)
   - Covers numeric vs. symbolic modes
   - Great introduction for first-time learners
3. [Official GNU Coreutils Documentation for chmod](https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html)
   - Detailed but easy enough to parse
   - Helps clarify the basics of command usage

### **Intermediate (2–3 Resources)**

1. [Linux Permissions and Ownership (DigitalOcean Tutorial)](https://www.digitalocean.com/community/tutorials/linux-permissions)
   - Focuses on deeper uses of chmod, chown, and chgrp
   - Explores special permissions like sticky bit
2. [Managing Groups in Linux (Red Hat)](https://www.redhat.com/sysadmin/linux-manage-groups)
   - Detailed approach to group management
   - Perfect for multi-user collaboration scenarios

### **SRE-Level (2–3 Resources)**

1. [SELinux Project Documentation](https://selinuxproject.org/page/Main_Page)
   - Advanced access controls beyond traditional `rwx`
   - Essential for SREs dealing with secure environments
2. [Linux Audit and SELinux (Open Security Training)](https://opensecuritytraining.info/IntroToLinuxAudit.html)
   - Focuses on auditing capabilities
   - Great for compliance and advanced SRE security measures
3. [Setuid Demystified (Kernel.org docs)](https://www.kernel.org/doc/html/latest/admin-guide/security.html)
   - Explains the implications of setuid programs
   - Vital for high-level security and compliance settings

---

**End of Day 3 – Congratulations!** You’ve mastered the fundamentals and deeper aspects of Linux permissions and ownership. In tomorrow’s session, we’ll leap into text processing magic using commands like `grep`, `find`, pipes, and redirections—indispensable tools for every SRE.
