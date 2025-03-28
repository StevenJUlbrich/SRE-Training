# 🚀 **Day 2: File Operations for SRE - Creating, Viewing, and Managing Files**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 1:**

Yesterday, you learned the foundations of Linux navigation (`pwd`, `ls`, `cd`), accessing documentation (`man`, `--help`, `info`), and understanding the Linux filesystem hierarchy. These skills help you efficiently move around and locate important resources on a Linux system.

### 📅 **Today's Topics and Importance:**

Today, we focus on **file operations** - creating, viewing, copying, moving, and removing files and directories. As an SRE, you'll regularly need to:

- Create and modify configuration files
- View and analyze logs
- Save and organize troubleshooting output
- Back up critical files before making changes
- Clean up temporary files to manage disk space

These skills are essential for everyday SRE tasks and critical during incident response.

### 🎯 **Learning Objectives:**

By the end of Day 2, you will be able to:

- Create files and directories (`touch`, `mkdir`)
- View file contents (`cat`, `less`, `head`, `tail`)
- Copy and move files (`cp`, `mv`)
- Delete files and directories (`rm`, `rmdir`)
- Apply these operations in common SRE scenarios

---

## 📚 **Core Concepts Explained**

### **The "Everything is a File" Philosophy**

In Linux, virtually everything is represented as a file - regular files, directories, devices, network sockets, and even processes. This unified approach makes interacting with system resources consistent:

- **Regular files**: Configuration files, logs, scripts
- **Directories**: Special files that can contain other files
- **Device files**: Hardware interfaces (in `/dev`)
- **Socket files**: Inter-process communication endpoints
- **Named pipes**: Another form of inter-process communication

As an SRE, understanding this philosophy helps you interact with systems consistently, whether you're editing a config file or analyzing a device's behavior.

### **File Manipulation in SRE Work**

Think of file operations as the building blocks of system maintenance:

- **Creating files/directories**: Setting up new configurations, organizing logs
- **Viewing files**: Analyzing logs during an incident, checking configurations
- **Copying/Moving**: Backing up before changes, reorganizing resources
- **Deleting**: Cleaning up temp files, removing old logs to free space

During incidents, efficient file operations can significantly reduce time to resolution. For example, quickly viewing the right log file can help identify the root cause of an outage in minutes rather than hours.

---

## 💻 **Commands to Learn Today**

### **1. Creating Files and Directories (`touch`, `mkdir`)**

#### **`touch` - Create Empty Files or Update Timestamps**

**Purpose**: Create new empty files or update timestamps of existing files.

**SRE Context**: Used to create placeholder files, log files, or update file timestamps for testing.

**Syntax:**
```bash
touch [options] filename(s)
```

**Common options:**
- `-a`: Change only the access time
- `-m`: Change only the modification time

**Examples:**

Create a new empty file:
```bash
[sre@prod-server ~]$ touch debug.log
```

Create multiple files at once:
```bash
[sre@prod-server ~]$ touch error.log warning.log info.log
```

Update timestamp of an existing file:
```bash
[sre@prod-server ~]$ touch -m config.yml
```

#### **`mkdir` - Create Directories**

**Purpose**: Create new directories (folders).

**SRE Context**: Organize log files, create backup directories, set up new application directories.

**Syntax:**
```bash
mkdir [options] directory_name(s)
```

**Common options:**
- `-p`: Create parent directories as needed
- `-m`: Set file permissions on creation

**Examples:**

Create a simple directory:
```bash
[sre@prod-server ~]$ mkdir backups
```

Create nested directories:
```bash
[sre@prod-server ~]$ mkdir -p projects/webapp/logs
```

Create a directory with specific permissions (read/write/execute for owner only):
```bash
[sre@prod-server ~]$ mkdir -m 700 secure_configs
```

### **2. Viewing File Contents (`cat`, `less`, `head`, `tail`)**

#### **`cat` - Concatenate and Display Files**

**Purpose**: Show the entire contents of a file.

**SRE Context**: View configuration files, small log files, or error messages.

**Syntax:**
```bash
cat [options] filename(s)
```

**Common options:**
- `-n`: Number all output lines
- `-A`: Show all non-printing characters (helpful for troubleshooting)

**Examples:**

View a configuration file:
```bash
[sre@prod-server ~]$ cat /etc/nginx/nginx.conf
```

Display multiple files:
```bash
[sre@prod-server ~]$ cat server1.log server2.log
```

View file with line numbers:
```bash
[sre@prod-server ~]$ cat -n script.sh
```

#### **`less` - View Files with Pagination**

**Purpose**: Interactively view large files one screen at a time.

**SRE Context**: The preferred tool for examining large log files during troubleshooting.

**Syntax:**
```bash
less [options] filename
```

**Common options:**
- `-N`: Show line numbers
- `-S`: Chop long lines (don't wrap)
- `+F`: Follow mode (like `tail -f`)

**Navigation in `less`:**
- `Space` or `Page Down`: Next page
- `b` or `Page Up`: Previous page
- `/pattern`: Search forward for pattern
- `n`: Next search match
- `N`: Previous search match
- `g`: Go to first line
- `G`: Go to last line
- `q`: Quit

**Examples:**

View a large log file:
```bash
[sre@prod-server ~]$ less /var/log/syslog
```

View with line numbers:
```bash
[sre@prod-server ~]$ less -N /var/log/apache2/error.log
```

Follow a log file in real-time (like `tail -f`):
```bash
[sre@prod-server ~]$ less +F /var/log/application.log
```

#### **`head` - View the Beginning of Files**

**Purpose**: Display the first part of files (default: 10 lines).

**SRE Context**: Quick peek at log files, check file headers or formats.

**Syntax:**
```bash
head [options] filename(s)
```

**Common options:**
- `-n N`: Show first N lines
- `-c N`: Show first N bytes

**Examples:**

View first 10 lines of a file:
```bash
[sre@prod-server ~]$ head /var/log/syslog
```

View first 20 lines:
```bash
[sre@prod-server ~]$ head -n 20 /var/log/auth.log
```

#### **`tail` - View the End of Files**

**Purpose**: Display the last part of files (default: 10 lines).

**SRE Context**: Check most recent log entries, monitor logs in real-time during incidents.

**Syntax:**
```bash
tail [options] filename(s)
```

**Common options:**
- `-n N`: Show last N lines
- `-f`: Follow mode - continuously show new lines as they're added
- `-F`: Follow mode that handles log rotation

**Examples:**

View last 10 lines of a log:
```bash
[sre@prod-server ~]$ tail /var/log/nginx/error.log
```

View last 50 lines:
```bash
[sre@prod-server ~]$ tail -n 50 /var/log/application.log
```

Monitor a log file in real-time (critical for troubleshooting):
```bash
[sre@prod-server ~]$ tail -f /var/log/application.log
```

### **3. Copying and Moving Files (`cp`, `mv`)**

#### **`cp` - Copy Files and Directories**

**Purpose**: Create duplicates of files or directories.

**SRE Context**: Create backups before changes, duplicate configurations for new services.

**Syntax:**
```bash
cp [options] source destination
```

**Common options:**
- `-r`: Recursively copy directories
- `-p`: Preserve mode, ownership, and timestamps
- `-a`: Archive mode (same as `-dpr`)
- `-i`: Interactive (prompt before overwrite)
- `-v`: Verbose output

**Examples:**

Copy a file:
```bash
[sre@prod-server ~]$ cp app.config app.config.bak
```

Copy a file to another directory:
```bash
[sre@prod-server ~]$ cp error.log /tmp/
```

Copy a directory and all its contents:
```bash
[sre@prod-server ~]$ cp -r /etc/nginx /etc/nginx.bak
```

Copy preserving permissions and timestamps (best for backups):
```bash
[sre@prod-server ~]$ cp -a /etc/postgresql/12/main/ /etc/postgresql/12/main.bak
```

#### **`mv` - Move or Rename Files and Directories**

**Purpose**: Relocate or rename files and directories.

**SRE Context**: Reorganize log files, implement new configurations, replace old files.

**Syntax:**
```bash
mv [options] source destination
```

**Common options:**
- `-i`: Interactive (prompt before overwrite)
- `-b`: Create a backup of each existing destination file
- `-v`: Verbose output

**Examples:**

Rename a file:
```bash
[sre@prod-server ~]$ mv old_name.conf new_name.conf
```

Move a file to another directory:
```bash
[sre@prod-server ~]$ mv app.log /var/log/app/
```

Move multiple files to a directory:
```bash
[sre@prod-server ~]$ mv *.log /var/log/archive/
```

Move with backup of destination:
```bash
[sre@prod-server ~]$ mv -b server.conf /etc/nginx/conf.d/
```

### **4. Deleting Files and Directories (`rm`, `rmdir`)**

#### **`rm` - Remove Files and Directories**

**Purpose**: Delete files and directories.

**SRE Context**: Clean up temp files, remove old logs, delete failed deployments.

**Syntax:**
```bash
rm [options] file(s)
```

**Common options:**
- `-r`: Recursively remove directories and their contents
- `-f`: Force removal without prompt
- `-i`: Interactive (prompt before removal)
- `-v`: Verbose output

**Examples:**

Remove a single file:
```bash
[sre@prod-server ~]$ rm temporary.txt
```

Remove multiple files:
```bash
[sre@prod-server ~]$ rm *.tmp
```

Remove a directory and all its contents (use with caution):
```bash
[sre@prod-server ~]$ rm -r old_project/
```

Force remove without prompting (very dangerous, use carefully):
```bash
[sre@prod-server ~]$ rm -rf temp_dir/
```

#### **`rmdir` - Remove Empty Directories**

**Purpose**: Delete empty directories only.

**SRE Context**: Clean up directory structure safely (fails if directory isn't empty).

**Syntax:**
```bash
rmdir [options] directory(s)
```

**Common options:**
- `-p`: Remove directory and its ancestors

**Examples:**

Remove an empty directory:
```bash
[sre@prod-server ~]$ rmdir empty_folder
```

Remove nested empty directories:
```bash
[sre@prod-server ~]$ rmdir -p parent/child/grandchild
```

---

## 🔍 **SRE Perspective: Critical File Operations**

In SRE practice, certain file operations are particularly important:

1. **Log Rotation and Management**: SREs must understand how to handle logs to prevent disk space issues:
   ```bash
   # View the last 100 lines of a log
   tail -n 100 /var/log/application.log
   
   # Monitor logs in real-time during an incident
   tail -f /var/log/application.log
   
   # Archive old logs
   mv /var/log/application.log.1 /var/log/archive/
   ```

2. **Configuration Backups**: Always back up configs before changes:
   ```bash
   # Create a timestamped backup
   cp -a /etc/nginx/nginx.conf /etc/nginx/nginx.conf.$(date +%Y%m%d-%H%M%S).bak
   ```

3. **File Comparison**: Check for differences between files:
   ```bash
   # Compare files (we'll cover more on this in future sessions)
   diff original.conf modified.conf
   ```

4. **Safe Deletion Practices**: Use interactive mode or create backup directories:
   ```bash
   # Interactive deletion
   rm -i important_file.conf
   
   # Alternative: move to a backup location instead of deleting
   mkdir -p ~/trash
   mv important_file.conf ~/trash/
   ```

---

## 🎯 **Practical Exercise: SRE File Operations Drill**

Practice these tasks in your Linux environment:

1. **Setup Test Environment**:
   ```bash
   mkdir -p ~/sre_practice/configs ~/sre_practice/logs
   ```

2. **Create Test Files**:
   ```bash
   touch ~/sre_practice/configs/app.conf
   echo "# Configuration file for test app" > ~/sre_practice/configs/app.conf
   
   # Create sample logs
   for i in {1..100}; do
     echo "$(date) - INFO - Test log entry $i" >> ~/sre_practice/logs/app.log
   done
   ```

3. **View and Analyze**:
   - View the entire configuration file using `cat`
   - View the last 10 log entries using `tail`
   - Examine the log interactively with `less`

4. **Backup Practice**:
   - Create a backup of the config file
   - Create a complete archive of the logs directory with `cp -r`

5. **Clean-up Operations**:
   - Create a new directory for old logs
   - Move log files there instead of deleting them
   - Try using `rmdir` on a non-empty directory and observe the error
   - Use `rm -r` to remove an entire directory structure

---

## 📝 **Quiz: File Operations for SREs**

Test your understanding of today's material:

1. During an incident, you need to monitor an actively written log file in real-time. Which command is most appropriate?
   - a) `cat /var/log/application.log`
   - b) `less /var/log/application.log`
   - c) `tail -f /var/log/application.log`
   - d) `head -n 50 /var/log/application.log`

2. You need to make a backup of a critical configuration file before modifying it. Which command preserves all file attributes correctly?
   - a) `cp /etc/service/config.xml /etc/service/config.xml.bak`
   - b) `cp -a /etc/service/config.xml /etc/service/config.xml.bak`
   - c) `mv /etc/service/config.xml /etc/service/config.xml.bak`
   - d) `touch /etc/service/config.xml.bak`

3. Which command would you use to create a nested directory structure for a new application deployment?
   ```bash
   # Fill in the blank
   ______ -p /opt/application/logs/debug
   ```

4. You need to clean up old temporary files in the `/tmp` directory but want to be prompted before each deletion. Which command should you use?
   - a) `rm /tmp/*.old`
   - b) `rm -f /tmp/*.old`
   - c) `rm -i /tmp/*.old`
   - d) `rmdir /tmp/*.old`

5. During a post-incident analysis, you need to check the first 50 lines of a log file to understand the initial error conditions. Which command would you use?
   - a) `cat -n 50 /var/log/service.log`
   - b) `head -n 50 /var/log/service.log`
   - c) `tail -n 50 /var/log/service.log`
   - d) `less -n 50 /var/log/service.log`

---

## ❓ **FAQ for SREs: File Operations Edition**

**Q1: What's the safest way to delete files on production systems?**

**A:** Production systems require extra caution:
- Always use `-i` for interactive prompting: `rm -i filename`
- Consider moving instead of deleting: `mv filename /path/to/archive/`
- Use full paths to avoid mistakes from your current directory
- Create temporary backup directories for "deleted" files that can be permanently removed later
- For critical systems, implement change management procedures before any deletion

**Q2: How can I find the largest files or directories when troubleshooting disk space issues?**

**A:** Common approaches include:
- `du -h --max-depth=1 /path | sort -hr` to find large directories
- `find /path -type f -size +100M -exec ls -lh {} \;` to find files over 100MB
- Utilities like `ncdu` for interactive exploration
- Focus on common culprits: log directories, temporary files, core dumps

**Q3: What's the most efficient way to examine very large log files during an incident?**

**A:** For large log files:
- Use `less` with search functionality (`/pattern`) to find relevant sections
- Use `grep "error" logfile | tail -n 100` to find recent errors
- For real-time monitoring: `tail -f logfile | grep "error"`
- Split analysis: `head` for initialization issues, `tail` for recent issues
- Consider specialized tools like `logrotate` for managing log sizes

**Q4: How do I handle file operations across multiple servers?**

**A:** For multi-server operations:
- Use `scp` or `rsync` for secure file transfers
- Consider configuration management tools (Ansible, Chef, Puppet)
- Create scripts that leverage SSH to execute commands on multiple hosts
- Remember that automation reduces errors in repetitive tasks

---

## 🚧 **Common Issues and Troubleshooting**

### **Issue 1: "No space left on device" when creating files**

**Possible causes:**
- Filesystem actually full
- Inode limit reached (plenty of space but no free inodes)
- Disk quota exceeded

**Solutions:**
```bash
# Check disk space
df -h

# Check inode usage
df -i

# Find large files
find / -type f -size +100M 2>/dev/null

# Find directories with many files (inode usage)
find / -type d -exec ls -la {} \; | sort -nr -k2 | head -20
```

### **Issue 2: "Permission denied" errors during file operations**

**Possible causes:**
- Insufficient permissions for the user
- File is owned by another user
- Directory permissions prevent access

**Solutions:**
```bash
# Check file permissions
ls -la filename

# Check parent directory permissions
ls -la /path/to/

# Check effective user and groups
id

# For emergencies (be careful!)
sudo cp important_file /backup/
```

---

## 🔄 **Real-World SRE Scenario: Log Analysis During an Incident**

**Situation:** You receive alerts that a web service is returning 500 errors. You need to quickly examine logs to determine the cause.

**SRE Response Using Today's Commands:**

1. SSH to the affected server:
   ```bash
   ssh sre@web-server-prod-03
   ```

2. Check the most recent logs:
   ```bash
   tail -n 50 /var/log/nginx/error.log
   ```

3. Look for patterns in the application logs:
   ```bash
   grep "ERROR" /var/log/application/app.log | tail -n 20
   ```

4. Monitor logs in real-time to correlate with errors:
   ```bash
   tail -f /var/log/application/app.log
   ```

5. After identifying a configuration issue, make a backup before changes:
   ```bash
   cp -a /etc/application/config.json /etc/application/config.json.bak.$(date +%Y%m%d-%H%M%S)
   ```

6. After resolving the issue, archive relevant logs for post-incident analysis:
   ```bash
   mkdir -p /var/log/incident_archives/$(date +%Y%m%d)
   cp /var/log/application/app.log /var/log/incident_archives/$(date +%Y%m%d)/
   ```

This sequence demonstrates how file operations are fundamental to incident response and resolution.

---

## 🚨 **SRE Caution: Dangerous Commands**

Be extremely careful with these commands, especially on production systems:

1. **`rm -rf /`**: NEVER run this! It attempts to recursively delete everything from the root.

2. **`rm -rf *`**: Extremely dangerous. Deletes everything in the current directory recursively.

3. **`rm -rf .`**: Attempts to delete the current directory and all contents.

4. **`> filename`**: Truncates a file to zero length. Particularly dangerous with important files like `/etc/passwd`.

5. Commands with wildcards (`*`) without verification.

⚠️ **Best Practices:**
- Always double-check commands with destructive potential
- Use `ls` to preview what wildcards will match before using them with `rm`
- Consider using `rm -i` on production systems
- Maintain current backups of critical systems

---

## 📚 **Further Learning Resources**

- [Linux Command Library - File Operations](https://linuxcommandlibrary.com/basic/filecommands.html)
- [Taming the Terminal - Files & Directories](https://www.bartbusschots.ie/s/2013/05/25/taming-the-terminal-part-6-more-file-operations/)
- [Google SRE Book - Chapter 13: Data Processing](https://sre.google/sre-book/data-processing/)

---

🎓 **Day 2 completed!** Tomorrow, we'll explore file permissions and ownership - critical concepts for securing Linux systems and controlling access to sensitive data in SRE environments.
