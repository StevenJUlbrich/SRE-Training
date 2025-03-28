# 🚀 **Day 3: Permissions and Ownership for SRE - Securing Access and Resources**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 2:**

Yesterday, you learned essential file operations including creating files and directories (`touch`, `mkdir`), viewing file contents (`cat`, `less`, `head`, `tail`), copying and moving files (`cp`, `mv`), and removing files and directories (`rm`, `rmdir`). These skills enable you to work efficiently with files and directories in Linux environments.

### 📅 **Today's Topics and Importance:**

Today, we focus on **permissions and ownership** - the core of Linux security and access control. For SREs, understanding and managing permissions is critical for:

- Securing production systems against unauthorized access
- Troubleshooting permission-related issues (common in web servers and application deployments)
- Implementing principle of least privilege for services
- Managing shared resources in multi-user environments
- Preventing accidental or malicious modifications to critical files

Without proper permissions, services can fail to start, applications may be unable to read configurations or write logs, and security vulnerabilities can emerge.

### 🎯 **Learning Objectives:**

By the end of Day 3, you will be able to:

- Understand the Linux permissions model (read, write, execute for user, group, others)
- Interpret and modify file permissions using both symbolic and numeric notation (`chmod`)
- Change file and directory ownership (`chown`, `chgrp`)
- Use `sudo` to perform administrative tasks
- Apply permissions in common SRE scenarios

---

## 📚 **Core Concepts Explained**

### **The Linux Permissions Model**

Linux uses a three-level access control system, assigning distinct permissions to:

1. **User (Owner)**: The account that owns the file
2. **Group**: A defined collection of users
3. **Others**: Everyone else on the system

For each of these levels, three types of permissions can be granted:

- **Read (r)**: View file contents or list directory contents
- **Write (w)**: Modify files or create/delete files within a directory
- **Execute (x)**: Run files as programs or access files within a directory

This creates a flexible but straightforward security model that allows precise control over who can do what with each file or directory.

### **Understanding Permission Notation**

When you run `ls -l`, you'll see permissions displayed like:
```
-rwxr-xr--
```

This notation breaks down as:

```
- rwx r-x r--
│ │   │   │
│ │   │   └── Others permissions: read-only
│ │   └────── Group permissions: read and execute
│ └────────── Owner permissions: read, write, execute
└──────────── File type (- for regular file, d for directory)
```

In this example:
- The **owner** can read, write, and execute
- The **group** can read and execute, but not write
- **Others** can only read

### **Special Permissions and Security Implications**

Beyond the basic rwx permissions, Linux has special permissions that have significant security implications:

- **Setuid (s)**: When set on an executable, it runs with the permissions of the file owner, not the user who executes it
- **Setgid (s)**: Similarly, allows programs to run with the group permissions of the file
- **Sticky bit (t)**: When set on a directory, files within can only be deleted by their owners

As an SRE, you need to be particularly cautious with setuid and setgid permissions, as they can create security vulnerabilities if misused.

---

## 💻 **Commands to Learn Today**

### **1. Viewing Permissions (`ls -l`)**

**Purpose**: Display detailed file information including permissions.

**SRE Context**: Investigating permission issues requires quickly understanding current permission states.

**Syntax:**
```bash
ls -l [file or directory]
```

**Examples:**

View permissions for files in the current directory:
```bash
[sre@prod-server ~]$ ls -l
-rw-r--r-- 1 sre  sre    143 Mar 20 15:30 config.yaml
-rwxr-xr-x 1 sre  sre   2540 Mar 19 09:45 deploy.sh
drwxr-xr-x 3 root root  4096 Mar 15 11:20 logs
```

View permissions including hidden files:
```bash
[sre@prod-server ~]$ ls -la
```

### **2. Changing Permissions (`chmod`)**

**Purpose**: Modify file or directory permissions.

**SRE Context**: Adjust access rights to ensure services can read configurations, write logs, and execute scripts.

**Syntax:**
```bash
chmod [options] mode file(s)
```

#### **Symbolic Method**

Uses symbols to specify permissions:
- **Who**: `u` (user/owner), `g` (group), `o` (others), `a` (all)
- **Operation**: `+` (add permission), `-` (remove permission), `=` (set exact permission)
- **Permission**: `r` (read), `w` (write), `x` (execute)

**Examples:**

Add execute permission for the owner:
```bash
[sre@prod-server ~]$ chmod u+x script.sh
```

Remove write permission for group and others:
```bash
[sre@prod-server ~]$ chmod go-w sensitive.conf
```

Set permissions for all (user, group, others):
```bash
[sre@prod-server ~]$ chmod a=r public_file.txt
```

#### **Numeric Method**

Uses octal numbers to specify permissions:
- **4**: Read permission
- **2**: Write permission
- **1**: Execute permission

Add these values to create the desired permission for each level (user, group, others).

**Examples:**

Set rwxr-xr-- (user: rwx, group: r-x, others: r--):
```bash
[sre@prod-server ~]$ chmod 754 script.sh
```

Set rw-r--r-- (common for regular files):
```bash
[sre@prod-server ~]$ chmod 644 config.yaml
```

Set rwx------ (private executable):
```bash
[sre@prod-server ~]$ chmod 700 private_script.sh
```

#### **Common Permission Patterns for SREs**

| Permissions | Numeric | Use Case |
|-------------|---------|----------|
| rwxr-xr-x   | 755     | Scripts, directories needing wide access |
| rw-r--r--   | 644     | Configuration files, public files |
| rwx------   | 700     | Private scripts and directories |
| rwxrwx---   | 770     | Group collaboration directories |
| rw-------   | 600     | Sensitive files (SSL private keys) |

#### **Recursive Permissions with `-R`**

**Purpose**: Apply permissions to directories and all their contents.

**SRE Context**: Used when deploying applications or restructuring access patterns.

**Example:**

Set read and execute permissions recursively (with caution!):
```bash
[sre@prod-server ~]$ chmod -R 755 /var/www/html
```

### **3. Changing Ownership (`chown`, `chgrp`)**

**Purpose**: Change the user and/or group that owns a file or directory.

**SRE Context**: Ensure services can access their files when run as specific users (nginx, apache, etc.).

#### **`chown` - Change Owner**

**Syntax:**
```bash
chown [options] user[:group] file(s)
```

**Examples:**

Change the owner of a file:
```bash
[sre@prod-server ~]$ sudo chown nginx config.conf
```

Change both owner and group:
```bash
[sre@prod-server ~]$ sudo chown nginx:webteam /var/www/site
```

Recursively change ownership of a directory and its contents:
```bash
[sre@prod-server ~]$ sudo chown -R appuser:appgroup /var/www/application
```

#### **`chgrp` - Change Group**

**Syntax:**
```bash
chgrp [options] group file(s)
```

**Examples:**

Change the group of a file:
```bash
[sre@prod-server ~]$ sudo chgrp developers project_file.js
```

Recursively change the group of a directory:
```bash
[sre@prod-server ~]$ sudo chgrp -R webteam /var/www/html
```

### **4. Administrative Access (`sudo`)**

**Purpose**: Execute commands with elevated privileges.

**SRE Context**: Perform system-level operations that require root access.

**Syntax:**
```bash
sudo [command]
```

**Examples:**

Edit a system configuration file:
```bash
[sre@prod-server ~]$ sudo vim /etc/nginx/nginx.conf
```

Restart a service:
```bash
[sre@prod-server ~]$ sudo systemctl restart nginx
```

Switch to the root user:
```bash
[sre@prod-server ~]$ sudo -i
```

View the sudoers file (who has sudo rights):
```bash
[sre@prod-server ~]$ sudo cat /etc/sudoers
```

#### **SRE Security Note**: `sudo` Practices

The principle of least privilege is critical for SREs:
- Use specific sudo commands rather than `sudo -i` (root shell) whenever possible
- Always double-check commands executed with sudo, especially destructive ones
- Consider using `sudo -l` to list available sudo privileges for your account
- Remember that sudo commands are typically logged in `/var/log/auth.log` or `/var/log/secure`

---

## 🔍 **SRE Perspective: Common Permission Scenarios**

### **1. Web Server Permissions**

Web servers like nginx or Apache often run as their own user and need specific permissions:

```bash
# Set the ownership for web files
sudo chown -R nginx:nginx /var/www/html

# Set secure permissions for web content
sudo chmod -R 755 /var/www/html

# Make configuration files readable but not writable by the web server
sudo chmod 644 /etc/nginx/nginx.conf
```

### **2. Application Deployment**

When deploying applications with specific user requirements:

```bash
# Create appropriate user/group
sudo useradd -r appuser
sudo groupadd appgroup
sudo usermod -aG appgroup appuser

# Set ownership and permissions
sudo chown -R appuser:appgroup /opt/application
sudo chmod -R 750 /opt/application
sudo chmod 770 /opt/application/logs  # Allow writing to logs
```

### **3. Troubleshooting Permission Issues**

Common indicators of permission problems:
- "Permission denied" errors in logs
- Services failing to start
- Applications unable to write logs

Troubleshooting approach:
```bash
# Check the running user for a process
ps aux | grep processname

# Check permissions on relevant files
ls -la /path/to/file

# Test access as the service user
sudo -u nginx cat /etc/nginx/nginx.conf

# Check logs for permission errors
grep "permission denied" /var/log/syslog
```

---

## 🎯 **Practical Exercise: Setting Up a Secure Web Directory**

Practice these tasks in your Linux environment:

1. **Setup the environment**:
   ```bash
   # Create directories and users (requires sudo)
   sudo mkdir -p /opt/webapplication/{public_html,logs,config}
   sudo useradd -m webuser
   sudo groupadd webteam
   sudo usermod -aG webteam webuser
   
   # Create test files
   sudo touch /opt/webapplication/public_html/index.html
   sudo touch /opt/webapplication/config/app.conf
   sudo touch /opt/webapplication/logs/app.log
   ```

2. **Apply the correct ownership**:
   ```bash
   sudo chown -R webuser:webteam /opt/webapplication
   ```

3. **Set appropriate permissions**:
   ```bash
   # Base directory - restrictive
   sudo chmod 750 /opt/webapplication
   
   # Public web content - readable by all
   sudo chmod -R 755 /opt/webapplication/public_html
   
   # Configuration - secure
   sudo chmod -R 640 /opt/webapplication/config
   
   # Logs - writable by webuser and group
   sudo chmod -R 770 /opt/webapplication/logs
   ```

4. **Verify the configuration**:
   ```bash
   ls -la /opt/webapplication
   ls -la /opt/webapplication/config
   ls -la /opt/webapplication/logs
   ```

5. **Test access as different users**:
   ```bash
   # Test as webuser
   sudo -u webuser cat /opt/webapplication/config/app.conf
   
   # Test writing to logs
   sudo -u webuser touch /opt/webapplication/logs/test.log
   
   # Try to write to config (should fail)
   sudo -u webuser touch /opt/webapplication/config/new.conf
   ```

---

## 📝 **Quiz: Permissions & Ownership for SREs**

Test your understanding of today's material:

1. An SRE notices that an application is failing with "Permission denied" errors when trying to write to its log file. The application runs as user `appuser`. What command would fix this issue?
   - a) `chmod 777 /var/log/app.log`
   - b) `chmod 644 /var/log/app.log`
   - c) `sudo chown appuser /var/log/app.log`
   - d) `sudo chmod +r /var/log/app.log`

2. You need to set permissions on a critical configuration file so that the owner has read and write access, while the group and others have only read access. Which command would you use?
   ```bash
   # Fill in the blank
   chmod _____ /etc/application/config.conf
   ```

3. Which permission setting allows the owner to read, write, and execute, the group to read and execute, and gives no permissions to others?
   - a) `chmod 640 script.sh`
   - b) `chmod 750 script.sh`
   - c) `chmod 755 script.sh`
   - d) `chmod 770 script.sh`

4. A junior SRE has accidentally changed permissions on the `/etc` directory. What is the correct command to recursively restore default permissions (755 for directories, 644 for files) without compromising security?
   - a) `sudo chmod -R 777 /etc`
   - b) `sudo chmod -R 755 /etc`
   - c) (This requires a more complex approach, not a single command)
   - d) `sudo chmod -R 644 /etc`

5. During a security audit, you need to identify files with the setuid bit set. Which command would you use?
   - a) `find / -type f -perm -4000 -ls`
   - b) `ls -l / | grep s`
   - c) `chmod -R -s /`
   - d) `chown -R root:root /`

---

## ❓ **FAQ for SREs: Permissions and Ownership Edition**

**Q1: What are the biggest permission-related security risks SREs should watch for?**

**A:** Key security risks include:
- Excessive permissions (e.g., world-writable files/directories)
- Improper use of setuid/setgid bits that can lead to privilege escalation
- Incorrect ownership allowing unauthorized access to sensitive files
- Misconfigured sudo permissions giving users more power than needed
- Insecure temporary files created by applications

**Q2: How should permissions differ between development, staging, and production environments?**

**A:** Best practices by environment:
- **Development**: Can be more permissive, but should still roughly mirror production to catch issues early
- **Staging**: Should exactly match production permissions to catch permission-related bugs before deployment
- **Production**: Most restrictive, following principle of least privilege
  - Service accounts should only access what they need
  - Log directories often need more permissive settings for writing
  - Configuration files should typically be read-only for service accounts
  - Sensitive credential files should have strict 600 permissions

**Q3: How do I recursively change permissions but with different settings for files vs. directories?**

**A:** This common SRE task requires a more complex approach:
```bash
# Set 755 for directories and 644 for files
find /path/to/directory -type d -exec chmod 755 {} \;
find /path/to/directory -type f -exec chmod 644 {} \;
```

**Q4: What's the difference between "access denied" and "permission denied" errors?**

**A:** 
- "Permission denied" typically indicates the Unix permission system (rwx) is preventing access
- "Access denied" might indicate other mechanisms like ACLs (Access Control Lists), SELinux, or AppArmor are involved
- Troubleshooting differs:
  - For permission denied: check file permissions and ownership
  - For access denied with correct permissions: investigate SELinux (`getenforce`, `ls -Z`), ACLs (`getfacl`), or other security systems

---

## 🚧 **Common Issues and Troubleshooting**

### **Issue 1: Service won't start due to permission problems**

**Possible causes:**
- Service user can't read configuration files
- Service can't write to its log directory
- Executable lacks execute permission

**Diagnosis and solutions:**
```bash
# Check the service status for clues
sudo systemctl status servicename

# Check the journal logs
sudo journalctl -u servicename

# Verify permissions on key files
ls -la /etc/servicename/
ls -la /var/log/servicename/

# Fix configuration file permissions
sudo chmod 644 /etc/servicename/config.conf

# Fix log directory permissions
sudo chown -R serviceuser:servicegroup /var/log/servicename/
sudo chmod 755 /var/log/servicename/
```

### **Issue 2: Permission changes don't apply as expected**

**Possible causes:**
- Symbolic links pointing elsewhere
- Mount points with different filesystems
- SELinux or other security systems

**Diagnosis and solutions:**
```bash
# Check if target is a symbolic link
ls -la /path/to/file

# Check mount points
mount | grep /path/to/directory

# Check SELinux context
ls -Z /path/to/file

# Change SELinux context if needed
sudo chcon -t appropriate_type /path/to/file
```

---

## 🔄 **Real-World SRE Scenario: Fixing a Permission-Related Outage**

**Situation:** Users report a web application is returning 503 errors. Initial investigation shows the service is failing to restart after a routine system update.

**SRE Response Using Today's Commands:**

1. Check the service status to see error details:
   ```bash
   sudo systemctl status webapp.service
   ```
   
   Output shows: "Failed to open the application log file: Permission denied"

2. Check log directory permissions:
   ```bash
   ls -la /var/log/webapp/
   ```
   
   Output shows logs directory owned by root:root with 755 permissions

3. Check the running user for the service:
   ```bash
   grep User /etc/systemd/system/webapp.service
   ```
   
   Output shows: "User=webappuser"

4. Fix the ownership:
   ```bash
   sudo chown -R webappuser:webappuser /var/log/webapp/
   ```

5. Verify the user can write to logs:
   ```bash
   sudo -u webappuser touch /var/log/webapp/test.log
   ```

6. Restart the service:
   ```bash
   sudo systemctl restart webapp.service
   ```

7. Prevent future issues:
   ```bash
   # Make sure the correct permissions are documented
   echo "Log directory should be owned by webappuser:webappuser" >> /etc/webapp/README.md
   
   # Add a check to deployment scripts
   echo "chown -R webappuser:webappuser /var/log/webapp/" >> /usr/local/bin/webapp-deploy.sh
   ```

This real scenario demonstrates how permission issues often cause outages and how SREs use their knowledge of Linux permissions to diagnose and resolve them quickly.

---

## 🛡️ **SRE Security Best Practices for Permissions**

Implement these practices to enhance system security:

1. **Audit sensitive permission bits regularly**:
   ```bash
   # Find setuid files
   sudo find / -perm -4000 -type f -exec ls -la {} \; 2>/dev/null
   
   # Find world-writable files
   sudo find / -perm -2 -type f -not -path "/proc/*" -exec ls -la {} \; 2>/dev/null
   ```

2. **Use restrictive umask**:
   ```bash
   # Set default umask in /etc/profile or /etc/bashrc
   umask 027  # New files: 640, directories: 750
   ```

3. **Implement file integrity monitoring**:
   ```bash
   # Consider tools like AIDE, Tripwire, or auditd
   sudo apt install aide
   sudo aide --init
   ```

4. **Secure temporary directories**:
   ```bash
   # Create separate tmp directories for services
   sudo mkdir /var/tmp/servicespecific
   sudo chown serviceuser /var/tmp/servicespecific
   sudo chmod 700 /var/tmp/servicespecific
   ```

5. **Use ACLs for complex permission scenarios**:
   ```bash
   # Add specific user access to a file
   sudo setfacl -m u:specialuser:rx /path/to/file
   
   # View ACLs
   getfacl /path/to/file
   ```

---

## 📚 **Further Learning Resources**

- [Linux Permissions Beyond the Basics](https://www.redhat.com/sysadmin/linux-permissions-guide)
- [Understanding Linux File Permissions (IBM Developer)](https://developer.ibm.com/tutorials/l-lpic1-104-5/)
- [Google SRE Book - Chapter 14: Managing Incidents](https://sre.google/sre-book/managing-incidents/)
- [Linux Systems Administration: File Permissions](https://linuxacademy.com/course/linux-systems-administration-file-permissions/)

---

🎓 **Day 3 completed!** Tomorrow, we'll explore text processing and searching with powerful tools like `grep`, `find`, and pipes/redirection - essential skills for effectively analyzing logs and configurations in SRE environments.
