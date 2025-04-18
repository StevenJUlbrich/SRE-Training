# 🚀 **Linux SRE Training: Enhanced Module on Permissions & Ownership**

## 📌 **Introduction**

### **Tiered Objectives & Importance**

Welcome to the enhanced Day 3 module on **Permissions & Ownership**! In this lesson, you’ll explore how Linux access control mechanisms function, why they’re essential for reliability engineering, and how to apply them effectively. We follow a clear **Beginner → Intermediate → SRE-level** progression.

1. **Beginner (Tier 1)** – Understand the Linux permissions model, use basic `chmod` settings, see how `sudo` is used for admin tasks.
2. **Intermediate (Tier 2)** – Master symbolic and numeric permission modes, adjust ownership with `chown` and `chgrp`, handle real-world shared directory scenarios.
3. **SRE-Level (Tier 3)** – Tackle advanced permission features (setuid, setgid, sticky bit), troubleshoot complex permission issues, and integrate best practices into your operational workflows.

**Why Does This Matter?**

- Proper permissions protect systems from unauthorized access.
- Ownership alignment ensures the right processes can read and write critical files.
- Overly permissive setups create security holes and reliability issues.

**Recap**: Yesterday, you learned to manipulate files and directories. Now we delve deeper into *who* can do *what* with them.

**Preview**: After this module, we’ll move into advanced command-line text processing, building on your ability to secure your environment.

---

## 📚 **Core Concepts**

### 1. **Linux Permissions Model**

Linux classifies three permissions — **Read (r)**, **Write (w)**, **Execute (x)** — across three entities:

- **User (Owner)**
- **Group**
- **Others**

So each file/directory has distinct `rwx` bits for each of the above. For example:

```bash
- rwx r-x r--
│ │   │   │
│ │   │   └── Others permissions: read-only
│ │   └────── Group permissions: read and execute
│ └────────── Owner permissions: read, write, execute
└──────────── File type (- for regular file, d for directory)
```

### 2. **Ownership**

- **User (Owner)**: Typically the creator of the file.
- **Group**: A set of users who can share permissions.
- **Others**: Everyone else on the system.

**SRE Note**: Proper ownership ensures the correct service accounts access files in production. For instance, a web server might run as `nginx` user, so its configs/logs must be owned or accessible by `nginx`.

### 3. **Special Permissions (Advanced)**

- **Setuid (s)**: When set on an executable file, it runs with the file owner’s privileges.
- **Setgid (s)**: Similar to Setuid, but for group privileges, and can be used on directories so new files inherit the directory’s group.
- **Sticky bit (t)**: Commonly used on directories so that only a file’s owner (or root) may remove or rename it, even if it’s world-writable (e.g., `/tmp`).

### 4. **Combining Security & Reliability**

From an SRE perspective, wrongly configured permissions can:

- **Break production apps** (e.g., blocking read/write to logs)
- **Expose sensitive data** (e.g., world-readable credentials)
- **Cause outages** if critical files are overwritten or locked

---

## 💻 **Command Breakdown**

We’ll look at five core commands frequently used by SREs to manage permissions and ownership.

---

### **1. Command: ls -l (List with Details)**

**Command Overview**: Lists files/directories in long format, showing permissions, ownership, size, and more.

**Syntax & Flags**:

| Flag/Option | Syntax Example      | Description                                     | SRE Usage Context                                     |
|-------------|---------------------|-------------------------------------------------|-------------------------------------------------------|
| `-l`        | `ls -l /var/log`   | Long listing format with permissions, ownership | Quickly verifying the permission/ownership on logs   |
| `-a`        | `ls -la`           | Includes hidden files in the listing            | Investigating possible hidden config or dotfiles      |
| `-h`        | `ls -lh`           | Human-readable sizes                             | Checking large log or config file sizes at-a-glance   |

**Tiered Examples**:

- 🔍 **Beginner Example**:

   ```bash
   # List all files in the current directory with details
   $ ls -l
   -rw-r--r-- 1 user group  1234 Mar 29 10:00 data.txt
   drwxr-xr-x 2 user group  4096 Mar 29 09:58 scripts
   ```

   *Explanation*: You see file types, permissions, owner, group, file size, and timestamps.

- 🧩 **Intermediate Example**:

   ```bash
   # Include hidden files
   $ ls -la /etc/app
   total 24
   drwxr-xr-x  3 root root 4096 Mar 28 12:00 .
   drwxr-xr-x 96 root root 4096 Mar 28 11:00 ..
   -rw-------  1 root root  512 Mar 28 09:00 .secret
   -rw-r--r--  1 root root  300 Mar 27 15:00 config.yml
   ```

   *Operational Significance*: Sometimes hidden dotfiles hold critical config or secrets.

- 💡 **SRE-Level Example**:

   ```bash
   # Combine with grep or other tools to filter for suspicious perms
   $ ls -lR /var/www | grep "777"
   ```

   *Explanation*: Searching recursively for overly permissive `777` directories can proactively catch vulnerabilities.

**Instructional Notes**:

- 🧠 **Beginner Tip**: The first character in the permission string indicates file type: `d` for directory, `-` for normal file, etc.
- 🔧 **SRE Insight**: Pairing `ls -l` with scripting or pipeline filters is a quick way to detect misconfigurations.
- ⚠️ **Common Pitfall**: Don’t rely only on `ls -l`; SELinux or ACLs might further restrict/allow access.
- 🚨 **Security Note**: Checking permissions on system directories (`/etc`, `/var/log`) should be a standard part of any post-deployment checklist.

---

### **2. Command: chmod (Change File Mode Bits)**

**Command Overview**: Modifies file or directory permissions in either symbolic (`u+rwx`, etc.) or numeric (`755`, `644`) form.

**Syntax & Flags**:

| Flag/Option | Syntax Example         | Description                                                       | SRE Usage Context                                 |
|-------------|------------------------|-------------------------------------------------------------------|---------------------------------------------------|
| `-R`        | `chmod -R 755 /var/www` | Recursively apply permissions to all files under a directory     | Deployment scripts for web content                |
| (none)      | `chmod 644 file.conf`  | Change permission using numeric or symbolic modes                 | Single-file permission adjustments                |
| (none)      | `chmod u+x script.sh`  | Symbolic mode to grant execute permission to the file’s owner    | Allowing a script to be run directly              |

**Tiered Examples**:

- 🔍 **Beginner Example**:

  ```bash
  # Give yourself read/write, group read, others read
  $ chmod 644 notes.txt
  -rw-r--r-- 1 user user 0 Mar 29 10:10 notes.txt
  ```

- 🧩 **Intermediate Example**:

  ```bash
  # Recursively set a directory to owner=rwx, group=rx, others=none
  $ chmod -R 750 /home/shared
  # Means: 7=owner rwx, 5=group r-x, 0=others ---
  ```

  *Operational Context*: Great for restricting group-shared directories while locking out others.

- 💡 **SRE-Level Example**:

  ```bash
  # Add the sticky bit to a shared directory
  $ chmod +t /var/public_upload
  # Ensures only the file's owner can delete their own files in /var/public_upload
  ```

**Instructional Notes**:

- 🧠 **Beginner Tip**: Use `ls -l` before and after changes to confirm you set the correct bits.
- 🔧 **SRE Insight**: Numeric notation (e.g., 755, 644) is compact and commonly used in scripts.
- ⚠️ **Common Pitfall**: Setting `777` (full permissions for everyone) can create massive security holes.
- 🚨 **Security Note**: Overly broad permissions on config files might expose passwords or tokens.
- 💡 **Performance Impact**: Typically negligible, but vital to keep services from failing due to permission issues.

---

### **3. Command: chown (Change Ownership)**

**Command Overview**: Assigns or modifies which user (and optionally which group) owns a file/directory. Frequently used so specific system users (like `nginx`, `mysql`) can manage their files.

**Syntax & Flags**:

| Flag/Option | Syntax Example              | Description                                                          | SRE Usage Context                                    |
|-------------|-----------------------------|----------------------------------------------------------------------|------------------------------------------------------|
| `-R`        | `chown -R appuser /opt/app` | Recursively change owner of a directory and all contents            | Setting consistent ownership after deployments       |
| (none)      | `chown alice file.txt`      | Changes file owner to `alice`                                       | Quick fix for single files                           |
| `:<group>`  | `chown alice:devteam file.txt` | Changes file owner to `alice` and group to `devteam`               | Granting multi-user access to dev files             |

**Tiered Examples**:

- 🔍 **Beginner Example**:

  ```bash
  # Change owner to 'student'
  $ sudo chown student assignment.txt
  # Group remains unchanged.
  ```

- 🧩 **Intermediate Example**:

  ```bash
  # Recursively set ownership to 'webuser' for a web directory
  $ sudo chown -R webuser:webgroup /var/www/myapp
  # Operational Context: Ensures the web service can manage its own files.
  ```

- 💡 **SRE-Level Example**:

  ```bash
  # Transfer ownership of logs to a logs group for compliance
  $ sudo chown root:logadmins /var/log/myapp/*.log
  # Production Relevance: Restricts direct write to logs, ensuring accountability.
  ```

**Instructional Notes**:

- 🧠 **Beginner Tip**: Typically requires `sudo` if you’re not the file’s current owner.
- 🔧 **SRE Insight**: Standardize ownership in your dev, staging, and production environments to avoid "it works on my machine" issues.
- ⚠️ **Common Pitfall**: Accidentally using `-R /` or changing ownership on system files can break your OS.
- 🚨 **Security Note**: Always confirm user accounts are legitimate before assigning them ownership.

---

### **4. Command: chgrp (Change Group Ownership)**

**Command Overview**: Changes only the group ownership of a file or directory, handy for collaborative environments.

**Syntax & Flags**:

| Flag/Option | Syntax Example           | Description                                                      | SRE Usage Context                                 |
|-------------|--------------------------|------------------------------------------------------------------|---------------------------------------------------|
| `-R`        | `chgrp -R devteam /app` | Recursively change group ownership for a directory and contents | Ensuring multiple developers share a code folder  |
| (none)      | `chgrp audit file.log`  | Change the group of a single file                               | Grant an audit team read/write privileges         |

**Tiered Examples**:

- 🔍 **Beginner Example**:

  ```bash
  # Set group ownership to 'students'
  $ sudo chgrp students group_project/
  ```

- 🧩 **Intermediate Example**:

  ```bash
  # Recursively assign logs to 'devops' group
  $ sudo chgrp -R devops /var/log/myapp
  # Operational Context: A DevOps team might collectively review logs.
  ```

- 💡 **SRE-Level Example**:

  ```bash
  # Rotating maintenance teams
  $ sudo chgrp -R maintainers /usr/local/maintenance_scripts
  # Production Relevance: Only the assigned maintenance group can modify scripts.
  ```

**Instructional Notes**:

- 🧠 **Beginner Tip**: Check group membership with `groups username`.
- 🔧 **SRE Insight**: Combine with setgid on directories to keep files in the correct group automatically.
- ⚠️ **Common Pitfall**: Mistyping group names or forgetting the `-R` can lead to partial updates.
- 🚨 **Security Note**: Group misconfigurations can inadvertently grant or block access to critical data.

---

### **5. Command: sudo (Superuser Do)**

**Command Overview**: Temporarily run commands with elevated privileges. SREs use `sudo` to perform admin tasks, from editing config files to restarting services.

**Syntax & Flags**:

| Flag/Option | Syntax Example            | Description                                             | SRE Usage Context                                      |
|-------------|---------------------------|---------------------------------------------------------|--------------------------------------------------------|
| `-i`        | `sudo -i`                | Launch an interactive root shell                        | Handling multiple privileged tasks in one session      |
| `-l`        | `sudo -l`                | List the commands that the current user can run via sudo | Auditing user privileges                                |
| (none)      | `sudo systemctl restart` | Execute a system command as root                        | Restarting services, applying system changes           |

**Tiered Examples**:

- 🔍 **Beginner Example**:

  ```bash
  # Install packages (apt requires root privileges)
  $ sudo apt update && sudo apt upgrade
  ```

- 🧩 **Intermediate Example**:

  ```bash
  # Edit a root-owned file
  $ sudo vim /etc/nginx/nginx.conf
  # Operational Context: Normal user can’t edit system config files.
  ```

- 💡 **SRE-Level Example**:

  ```bash
  # Audit privileges for a user named 'deployer'
  $ sudo -l -U deployer
  # Production Relevance: Validate that 'deployer' can only run certain commands.
  ```

**Instructional Notes**:

- 🧠 **Beginner Tip**: Always verify the command before pressing Enter under sudo.
- 🔧 **SRE Insight**: Use role-based privileges in `/etc/sudoers` or polkit for better security.
- ⚠️ **Common Pitfall**: Overusing `sudo -i` can lead to untracked root sessions.
- 🚨 **Security Note**: All `sudo` actions typically log to `/var/log/auth.log` or `/var/log/secure`, aiding audits.

---

## 🛠️ **System Effects**

1. **Filesystem**: Permission bits and ownership are stored in the file’s inode.
2. **Resources & Security**: Minimal direct performance overhead from changing permissions, but misconfiguration can create service failures or open security holes.
3. **Monitoring & Audits**: Tools like `ls -l`, `stat`, and logs from `sudo` or SELinux highlight permission changes.
4. **SRE Implementation**: Reliable permission management means consistent, automated enforcement across dev, staging, and production.

---

## 🎯 **Hands-On Exercises**

Below are curated exercises for each level to reinforce your skills.

### **Beginner (3 Exercises)**

1. **Simple Permission Adjustments**
   - Create a file `myfile.txt`. Set its permissions so only you (owner) can read and write, and no one else has permissions.
   - Use `ls -l myfile.txt` to confirm.

2. **Symbolic vs Numeric**
   - Copy `myfile.txt` to `myfile_copy.txt`.
   - Use symbolic notation to add execute permission for the owner: `chmod u+x myfile_copy.txt`.
   - Then switch it back to `644` using numeric notation.

3. **Basic Ownership Change**
   - Create a directory `beginner_test`.
   - If you have another local user, try `sudo chown otheruser beginner_test`.
   - Check ownership with `ls -ld beginner_test`.

### **Intermediate (3 Exercises)**

1. **Recursive Permissions**
   - Create a directory structure: `project/{scripts,configs,data}`.
   - Place a few sample files in each.
   - Recursively set everything under `project` to `750`.
   - Verify each file and directory’s permissions.

2. **Group Collaboration**
   - Create a group named `devteam`.
   - Create a directory `shared_docs` owned by you, but set group to `devteam`.
   - Grant read/write to owner and group, no permissions to others.

3. **Checking Sudo**
   - Run `sudo -l` to list your allowed commands.
   - Attempt editing a root-owned file (e.g., `/etc/hosts`). Observe the difference with and without `sudo`.

### **SRE-Level (3 Exercises)**

1. **Sticky Bit for a Shared Folder**
   - Create `/srv/public_drop` and assign it to a shared group.
   - Add the sticky bit so only file owners can delete their own files.
   - Test by creating files as different users.

2. **Hunting setuid Binaries**
   - Find setuid files: `sudo find / -perm -4000 -type f 2>/dev/null`.
   - Identify at least one unusual or unnecessary setuid binary. Document potential risks.

3. **Automation of Permissions**
   - Write a short script to enforce `/var/log/myapp` ownership as `myappuser:logs` with `750` permissions.
   - Schedule it with cron or a systemd timer to auto-correct if changed.

---

## 📝 **Quiz Questions**

### **Beginner Tier (3–4 Questions)**

1. Which numeric permission grants the owner read and write, group read, and others read?
   - A) 644  
   - B) 755  
   - C) 600
2. In `-rwxr-xr--`, which permissions does the group have?
   - A) Read and write  
   - B) Read and execute  
   - C) Read only
3. True/False: `chmod +x script.sh` sets execute permission for all users.
4. To change the owner of `example.txt` to `alice`, which command is correct?
   - A) `chown alice example.txt`  
   - B) `chmod alice example.txt`  
   - C) `sudo chgrp alice example.txt`

### **Intermediate Tier (3–4 Questions)**

1. Which command recursively sets a directory’s permissions to `770`?
   - A) `chmod 770 directory/`  
   - B) `chmod -R 770 directory/`  
   - C) `chown -R 770 directory/`
2. A file has permissions `-rw-r--r--`. Which command makes it so only the owner can read/write it, with no access for group or others?
   - A) `chmod 640 file`  
   - B) `chmod 600 file`  
   - C) `chmod 700 file`
3. True/False: Using `chown :developers file.txt` changes the owner to `developers`.
4. Match the numeric notation:
   - 700 → `rwx------`
   - 755 → `rwxr-xr-x`
   - 666 → `rw-rw-rw-`

### **SRE-Level Tier (3–4 Questions)**

1. Why is a setuid binary risky?
2. You see `-rwsr-xr-x` on `/usr/bin/passwd`. What does the `s` indicate?
   - A) Sticky bit  
   - B) setuid bit  
   - C) The owner can’t execute
3. True/False: SELinux or AppArmor can override traditional file permissions.
4. Which command best helps confirm a file’s permission bits and extended attributes?
   - A) `ls -lh /path/file`  
   - B) `stat /path/file`  
   - C) `cat /path/file`

---

## 🚧 **Troubleshooting (3 Scenarios)**

1. **Service Fails to Start (Permission Denied)**
   - **Symptoms**: The application logs show “Cannot open config file: Permission denied.”
   - **Diagnostic**: Check ownership (`ls -l config.yaml`). If it’s owned by root, the service user can’t read it.
   - **Solution**: `sudo chown serviceuser:servicegroup config.yaml && chmod 640 config.yaml`.
   - **Prevention**: Automated scripts or config management ensuring correct ownership.

2. **Shared Directory Not Working**
   - **Symptoms**: Team members cannot edit each other’s files in `/shared/projects`.
   - **Diagnostic**: Confirm group ownership (`ls -ld /shared/projects`).
   - **Solution**: `sudo chown -R user:devteam /shared/projects && chmod 770 /shared/projects`.
   - **Prevention**: Use setgid on the directory so newly created files inherit the group.

3. **Web Server 503 Errors**
   - **Symptoms**: Nginx or Apache can’t read `/etc/nginx/nginx.conf` after an update.
   - **Diagnostic**: `ls -l /etc/nginx/nginx.conf` shows `rw------- root root`.
   - **Solution**: `sudo chmod 644 /etc/nginx/nginx.conf` so the nginx user can read it.
   - **Prevention**: CI/CD pipeline checks that production config permissions match a known baseline.

---

## ❓ **FAQ**

### **Beginner (3 FAQs)**

1. **Do I always need sudo to change permissions?**
   - Not if you own the file. Otherwise, yes—Linux prevents non-owners from changing permissions or ownership.
2. **What’s the difference between symbolic (`u+rwx`) and numeric (`755`) permission methods?**
   - Symbolic is more descriptive for small changes, numeric is concise and typical in scripts.
3. **How can I tell if a file is executable?**
   - Run `ls -l` and look for an `x` in the permission bits.

### **Intermediate (3 FAQs)**

1. **How do I change both owner and group in one command?**
   - Use `sudo chown user:group file`. This is often the simplest approach.
2. **What’s the sticky bit used for?**
   - Primarily on directories like `/tmp`; it ensures only file owners can remove their files, preventing others from deleting them.
3. **Can I revoke execute permission from just the group?**
   - Yes, with a symbolic command like `chmod g-x file.sh`.

### **SRE-Level (3 FAQs)**

1. **Does SELinux override normal permissions?**
   - Yes. SELinux or AppArmor can further restrict or allow access beyond basic `rwx` bits.
2. **Is there a risk with setuid executables in production?**
   - Absolutely. They run with the owner’s privileges, so vulnerabilities can lead to privilege escalation.
3. **Where do I see logs of permission changes?**
   - Typically in `/var/log/auth.log` or `/var/log/secure` for `sudo` actions. For deeper audits, enable `auditd`.

---

## 🔥 **SRE Scenario**

**Situation**: Your custom monitoring tool is failing to write logs, leading to silent monitoring coverage gaps.

1. **Identify the Tool’s User**: `ps aux | grep monitoring_tool` → discovers it runs as `monuser`.
2. **Check Log Directory**: `ls -l /var/log/monitoring_tool` → Owned by `root:root`, `drwxr-xr-x`.
3. **Assign Proper Ownership**:

   ```bash
   sudo chown -R monuser:monuser /var/log/monitoring_tool
   ```

4. **Set Secure Permissions**:

   ```bash
   sudo chmod 750 /var/log/monitoring_tool
   ```

5. **Validate Write Access**:

   ```bash
   sudo -u monuser touch /var/log/monitoring_tool/test.log
   ```

6. **Restart Service**:

   ```bash
   sudo systemctl restart monitoring_tool
   ```

7. **Implement Checks**:
   - Add a script or systemd unit to ensure `/var/log/monitoring_tool` remains correctly owned and permissioned.

---

## 🧠 **Key Takeaways**

1. **Command Summary (5):**
   - `ls -l`: Inspect permissions/ownership
   - `chmod`: Adjust `rwx` bits
   - `chown`: Change file ownership
   - `chgrp`: Change file group ownership
   - `sudo`: Execute commands with elevated privileges

2. **Operational Insights (3):**
   1. **Least Privilege**: Always restrict user and service permissions to the minimal necessary.
   2. **Consistent Automation**: Use scripts/CI pipelines to maintain uniform permissions across environments.
   3. **Collaborative Ownership**: Assign groups appropriately to simplify multi-user workflows.

3. **Best Practices (3):**
   1. **Separate System & App Users**: Keep services running under distinct accounts to isolate access.
   2. **Use Group Inheritance**: For directories where multiple users share files, setgid plus correct group ownership can streamline collaboration.
   3. **Security Audits**: Regularly check for setuid/setgid files and overly permissive directories.

4. **Next Topic Preview**: The next module explores text processing with commands like `grep` and `find`, along with piping, which is crucial for analyzing logs and building advanced SRE scripts.

---

## 📚 **Further Learning Resources**

### **Beginner (2–3)**

1. [Ubuntu Docs: FilePermissions](https://help.ubuntu.com/community/FilePermissions) — Straightforward explanation of `rwx`.
2. [Linuxize: chmod Command](https://linuxize.com/post/how-to-use-chmod-command/) — Good coverage of symbolic vs numeric modes.
3. [GNU Coreutils: chmod](https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html) — Detailed official reference.

### **Intermediate (2–3)**

1. [DigitalOcean: Linux Permissions](https://www.digitalocean.com/community/tutorials/linux-permissions) — Deeper look at special permissions.
2. [Red Hat: Linux Group Management](https://www.redhat.com/sysadmin/linux-manage-groups) — Explains best practices for group-based collaboration.

### **SRE-Level (2–3)**

1. [SELinux Project Docs](https://selinuxproject.org/page/Main_Page) — Understand mandatory access controls beyond classic `rwx`.
2. [Open Security Training: Linux Audit](https://opensecuritytraining.info/IntroToLinuxAudit.html) — Explore advanced auditing features.
3. [Kernel.org on setuid Security](https://www.kernel.org/doc/html/latest/admin-guide/security.html) — Dive deeper into setuid security implications.

---

## End of Enhanced Module

Congratulations on completing this consolidated, SRE-focused training module on Linux Permissions & Ownership. Mastering these commands and concepts is crucial for maintaining secure, reliable systems. Tomorrow, we’ll expand further with advanced text manipulation—skills that complement your newly acquired permission management prowess.
