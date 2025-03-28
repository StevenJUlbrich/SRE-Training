# 🚀 **Day 3: Permissions and Ownership for SRE - Securing Access and Resources**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 2:**

Yesterday, you learned essential file operations including creating files and directories (`touch`, `mkdir`), viewing file contents (`cat`, `less`, `head`, `tail`), copying and moving files (`cp`, `mv`), and removing files and directories (`rm`, `rmdir`). These skills enable you to work efficiently with files and directories in Linux environments.

### 📅 **Today's Topics and Importance:**

Today, we focus on **permissions and ownership** - the core of Linux security and access control. Understanding and managing permissions is critical for:

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

**Beginner's Note**: Think of permissions as keys to doors: some people have full access, some limited, and some none at all. Like giving different keys to family members (owners), neighbors (group), and strangers (others).

**SRE Perspective**: In production environments, proper permissions are crucial for both security and functionality. Web servers need to read configuration files but shouldn't be able to modify them, while log directories must be writable by the application but not by unauthorized users.

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

**Beginner's Note**: The permission string always shows all positions, with a `-` indicating the absence of a specific permission.

### **Special Permissions and Security Implications**

Beyond the basic rwx permissions, Linux has special permissions that have significant security implications:

- **Setuid (s)**: When set on an executable, it runs with the permissions of the file owner, not the user who executes it
- **Setgid (s)**: Similarly, allows programs to run with the group permissions of the file
- **Sticky bit (t)**: When set on a directory, files within can only be deleted by their owners

**SRE Perspective**: The setuid bit is particularly important to understand from a security perspective. Many system utilities (like `passwd`) use this to allow regular users to perform specific privileged operations. However, setuid programs can create security vulnerabilities if they contain bugs.

---

## 💻 **Commands to Learn Today**

### **1. Viewing Permissions (`ls -l`)**

**Purpose**: Display detailed file information including permissions.

**Syntax:**

```bash
ls -l [file or directory]
```

**Basic Examples:**

View permissions for files in the current directory:

```bash
ls -l
-rw-r--r-- 1 user group 143 Mar 20 15:30 config.yaml
-rwxr-xr-x 1 user group 2540 Mar 19 09:45 script.sh
drwxr-xr-x 3 user group 4096 Mar 15 11:20 docs
```

**Intermediate Examples:**

View permissions including hidden files:

```bash
ls -la
```

**SRE Context**: Investigating permission issues requires quickly understanding current permission states. During incidents, you'll regularly need to check permissions to determine why a service can't access files it needs.

**Beginner's Tip**: The first character in the permission string tells you the file type: `-` for regular files, `d` for directories.

### **2. Changing Permissions (`chmod`)**

**Purpose**: Modify file or directory permissions.

**Syntax:**

```bash
chmod [options] mode file(s)
```

#### **Symbolic Method**

Uses symbols to specify permissions:

- **Who**: `u` (user/owner), `g` (group), `o` (others), `a` (all)
- **Operation**: `+` (add permission), `-` (remove permission), `=` (set exact permission)
- **Permission**: `r` (read), `w` (write), `x` (execute)

**Basic Examples:**

Add execute permission for the owner:

```bash
chmod u+x script.sh
```

Remove write permission for group and others:

```bash
chmod go-w sensitive.conf
```

**Intermediate Examples:**

Set specific permissions for all (user, group, others):

```bash
chmod u=rwx,g=rx,o=r public_script.sh
```

Set permissions for all users:

```bash
chmod a=r public_file.txt
```

**SRE Context**: When deploying applications or fixing permission-related issues, you'll need to ensure services can read configurations, write logs, and execute scripts.

**Beginner's Tip**: The symbolic method is more intuitive for beginners because you explicitly state what permissions you're adding or removing for which user categories.

#### **Numeric Method**

Uses octal numbers to specify permissions:

- **4**: Read permission
- **2**: Write permission
- **1**: Execute permission

Add these values to create the desired permission for each level (user, group, others).

**Basic Examples:**

Set rwxr-xr-- (user: rwx, group: r-x, others: r--):

```bash
chmod 754 script.sh
```

Set rw-r--r-- (common for regular files):

```bash
chmod 644 config.yaml
```

**Intermediate Examples:**

Set rwx------ (private executable):

```bash
chmod 700 private_script.sh
```

**SRE Context**: The numeric method is commonly used in scripts and documentation because it's more concise and precise.

**Beginner's Tip**: To calculate the numeric permission, add the values for each permission type: r(4) + w(2) + x(1) = 7 for full permissions. So 755 means rwx for owner, rx for group, rx for others.

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
chmod -R 755 /var/www/html
```

**SRE Caution**: Recursive permission changes can have unintended consequences. Be careful when using `-R`, especially on system directories.

### **3. Changing Ownership (`chown`, `chgrp`)**

#### **`chown` - Change Owner**

**Purpose**: Change the user and/or group that owns a file or directory.

**Syntax:**

```bash
chown [options] user[:group] file(s)
```

**Basic Examples:**

Change the owner of a file:

```bash
sudo chown alice file.txt
```

**Intermediate Examples:**

Change both owner and group:

```bash
sudo chown nginx:webteam /var/www/site
```

Recursively change ownership of a directory and its contents:

```bash
sudo chown -R appuser:appgroup /var/www/application
```

**SRE Context**: Ensure services can access their files when run as specific users (nginx, apache, etc.). After deploying an application, you often need to set correct ownership so the service account can access the files.

**Beginner's Tip**: You usually need `sudo` to change ownership unless you're the current owner of the file.

#### **`chgrp` - Change Group**

**Purpose**: Change the group of a file or directory.

**Syntax:**

```bash
chgrp [options] group file(s)
```

**Basic Examples:**

Change the group of a file:

```bash
sudo chgrp developers project_file.js
```

**Intermediate Examples:**

Recursively change the group of a directory:

```bash
sudo chgrp -R webteam /var/www/html
```

**SRE Context**: Used to allow specific groups access to files while maintaining ownership.

**Beginner's Tip**: `chgrp` is essentially equivalent to `chown :groupname file`, but can be more intuitive for beginners.

### **4. Administrative Access (`sudo`)**

**Purpose**: Execute commands with elevated privileges.

**Syntax:**

```bash
sudo [command]
```

**Basic Examples:**

Edit a system configuration file:

```bash
sudo vim /etc/nginx/nginx.conf
```

**Intermediate Examples:**

Switch to the root user:

```bash
sudo -i
```

View the sudoers file:

```bash
sudo cat /etc/sudoers
```

Restart a service:

```bash
sudo systemctl restart nginx
```

**SRE Context**: Most SRE tasks require administrative access, from configuring services to modifying system files. Using `sudo` appropriately is crucial for security.

**Beginner's Tip**: `sudo` stands for "superuser do" and temporarily gives you administrative powers. Always double-check commands before using sudo!

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

### **3. Securing Sensitive Files**

For files containing credentials or private keys:

```bash
# Restrict access to SSH private keys
chmod 600 ~/.ssh/id_rsa

# Restrict access to configuration with passwords
sudo chmod 600 /etc/app/credentials.conf
sudo chown appuser:appgroup /etc/app/credentials.conf
```

---

## 🎯 **Practical Exercises: From Beginner to SRE**

### **Beginner Exercises**

1. Create a directory called `practice` in your home directory.
2. Inside it, create a simple script file with `touch script.sh`.
3. Make the script executable for yourself, but read-only for others:

   ```bash
   chmod u+x,go=r script.sh
   ```

4. Verify the permissions with `ls -l script.sh`.
5. Create another file called `private.txt` and make it readable and writable only by you:

   ```bash
   chmod 600 private.txt
   ```

### **Intermediate Exercises**

1. Create a directory structure for a simple project:

   ```bash
   mkdir -p project/{scripts,configs,data}
   ```

2. Create some files in each directory:

   ```bash
   touch project/scripts/{setup.sh,backup.sh}
   touch project/configs/settings.conf
   touch project/data/sample.dat
   ```

3. Make all scripts executable by the owner and readable by others:

   ```bash
   chmod 755 project/scripts/*.sh
   ```

4. Set restrictive permissions on the config file:

   ```bash
   chmod 640 project/configs/settings.conf
   ```

5. If you have sudo access, try changing ownership of files:

   ```bash
   sudo chown -R :developers project
   ```

### **SRE Application Exercises**

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

## 📝 **Quiz: Test Your Knowledge**

### **Beginner Level**

1. Which command displays detailed file information including permissions?
   - a) `dir -l`
   - b) `ls -l`
   - c) `cat -l`
   - d) `perms -show`

2. In the permission string `-rw-r--r--`, what permissions does the file owner have?
   - a) Read only
   - b) Read and write
   - c) Read, write, and execute
   - d) No permissions

3. Which command adds execute permission for the owner of a file?
   - a) `chmod +x file.sh`
   - b) `chmod u+x file.sh`
   - c) `chmod a+x file.sh`
   - d) `chmod x+u file.sh`

### **Intermediate Level**

4. What numeric value represents read and write permission but not execute?
   - a) 7
   - b) 5
   - c) 6
   - d) 3

5. Which permission setting allows the owner to read, write, and execute, the group to read and execute, and gives no permissions to others?
   - a) `chmod 640 script.sh`
   - b) `chmod 750 script.sh`
   - c) `chmod 755 script.sh`
   - d) `chmod 770 script.sh`

6. To change both the owner and group of a file to "webuser" and "webteam" respectively, which command would you use?
   - a) `sudo chown webuser + webteam file.html`
   - b) `sudo chown webuser:webteam file.html`
   - c) `sudo chown webuser webteam file.html`
   - d) `sudo chgrp webuser webteam file.html`

### **SRE Application Level**

7. An SRE notices that an application is failing with "Permission denied" errors when trying to write to its log file. The application runs as user `appuser`. What command would fix this issue?
   - a) `chmod 777 /var/log/app.log`
   - b) `chmod 644 /var/log/app.log`
   - c) `sudo chown appuser /var/log/app.log`
   - d) `sudo chmod +r /var/log/app.log`

8. During a security audit, you need to identify files with the setuid bit set. Which command would you use?
   - a) `find / -type f -perm -4000 -ls`
   - b) `ls -l / | grep s`
   - c) `chmod -R -s /`
   - d) `chown -R root:root /`

9. A junior SRE has accidentally changed permissions on the `/etc` directory. What is the correct command to recursively restore default permissions (755 for directories, 644 for files) without compromising security?
   - a) `sudo chmod -R 777 /etc`
   - b) `sudo chmod -R 755 /etc`
   - c) (This requires a more complex approach, not a single command)
   - d) `sudo chmod -R 644 /etc`

---

## ❓ **FAQ: From Beginners to SREs**

### **Beginner FAQs**

**Q1: What's the difference between symbolic (`u+rwx`) and numeric (`755`) permission methods?**

**A:** Symbolic notation is more descriptive - you specify user categories (u/g/o/a) and whether you're adding (+), removing (-), or setting (=) permissions. Numeric notation is more concise, using numbers that represent permission combinations (4=r, 2=w, 1=x). Both achieve the same result, but symbolic is often easier for beginners, while numeric is commonly used in scripts and documentation.

**Q2: Why do I need `sudo` to change file ownership?**

**A:** Changing ownership typically requires root privileges to prevent unauthorized users from taking ownership of files they shouldn't access. This is a security feature of Linux.

**Q3: What happens if I remove execute permission from a directory?**

**A:** Without execute permission on a directory, you can't access or list the files inside, even if you know their names. Execute permission on directories allows you to "enter" the directory and use it as your current working directory.

### **Intermediate FAQs**

**Q4: Can I give multiple permission changes in one command?**

**A:** Yes, you can combine multiple changes in a single command:

- Symbolic: `chmod u+rwx,g+rx,o+r file.sh`
- Numeric: `chmod 754 file.sh` (which sets rwx for owner, r-x for group, r-- for others)

**Q5: What's the difference between `chown` and `chgrp`?**

**A:**

- `chown` can change both the owner and group of a file (e.g., `chown user:group file`)
- `chgrp` only changes the group ownership
- For changing just the group, either `chown :group file` or `chgrp group file` works

**Q6: What's the sticky bit and when should I use it?**

**A:** The sticky bit (mode 1000, displayed as 't' in the permissions) is primarily used on directories. When set, files in that directory can only be deleted by their owner, the directory owner, or root - even if the directory has write permissions for everyone. It's commonly used on shared directories like `/tmp` to prevent users from deleting each other's files.

### **SRE FAQs**

**Q7: What are the biggest permission-related security risks SREs should watch for?**

**A:** Key security risks include:

- Excessive permissions (e.g., world-writable files/directories)
- Improper use of setuid/setgid bits that can lead to privilege escalation
- Incorrect ownership allowing unauthorized access to sensitive files
- Misconfigured sudo permissions giving users more power than needed
- Insecure temporary files created by applications

**Q8: How should permissions differ between development, staging, and production environments?**

**A:** Best practices by environment:

- **Development**: Can be more permissive, but should still roughly mirror production to catch issues early
- **Staging**: Should exactly match production permissions to catch permission-related bugs before deployment
- **Production**: Most restrictive, following principle of least privilege
  - Service accounts should only access what they need
  - Log directories often need more permissive settings for writing
  - Configuration files should typically be read-only for service accounts
  - Sensitive credential files should have strict 600 permissions

**Q9: How do I recursively change permissions but with different settings for files vs. directories?**

**A:** This common SRE task requires a more complex approach:

```bash
# Set 755 for directories and 644 for files
find /path/to/directory -type d -exec chmod 755 {} \;
find /path/to/directory -type f -exec chmod 644 {} \;
```

---

## 🚧 **Common Issues and Troubleshooting**

### **Issue 1: "Permission denied" errors**

**Possible causes:**

- Insufficient permissions for your user
- Wrong ownership of the file
- Execute permission missing on a directory in the path

**Beginner Solutions:**

```bash
# Check current permissions
ls -la file_or_directory

# Check your effective user and groups
id
```

**SRE Solutions:**

```bash
# Check the running user for a process
ps aux | grep processname

# Test access as the service user
sudo -u serviceuser cat /path/to/file

# Check for SELinux or AppArmor restrictions
ls -Z /path/to/file
getenforce
```

### **Issue 2: `"chmod: changing permissions of 'file.txt': Operation not permitted"`**

**Possible causes:**

- You're not the owner of the file
- You don't have sudo/root privileges

**Solutions:**

```bash
# Check ownership
ls -la file.txt

# Use sudo if necessary
sudo chmod 644 file.txt
```

### **Issue 3: Service won't start due to permission problems**

**Possible causes:**

- Service user can't read configuration files
- Service can't write to its log directory
- Executable lacks execute permission

**SRE Diagnosis and solutions:**

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
   grep User /etc/systemd/system/webapp
