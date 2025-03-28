# 🚀 **Day 2: File Operations for SRE - Creating, Viewing, and Managing Files**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 1:**

Yesterday, you learned the foundations of Linux navigation (`pwd`, `ls`, `cd`), accessing documentation (`man`, `--help`, `info`), and understanding the Linux filesystem hierarchy. These skills help you efficiently move around and locate important resources on a Linux system.

### 📅 **Today's Topics and Importance:**

Today, we focus on **file operations** - creating, viewing, copying, moving, and removing files and directories. These skills are fundamental to Linux and especially critical for SRE work where you'll regularly need to:

- Create and modify configuration files
- View and analyze logs during incidents
- Save and organize troubleshooting output
- Back up critical files before making changes
- Clean up temporary files to manage disk space

As an SRE, efficient file operations can significantly reduce your time to resolution during incidents.

### 🎯 **Learning Objectives:**

By the end of Day 2, you will be able to:

- Create files and directories (`touch`, `mkdir`)
- View file contents (`cat`, `less`, `more`, `head`, `tail`)
- Copy and move files (`cp`, `mv`)
- Delete files and directories (`rm`, `rmdir`)
- Apply these operations in common SRE scenarios
- Practice safe file operations in production environments

---

## 📚 **Core Concepts Explained**

### **The "Everything is a File" Philosophy**

Linux treats everything as a file - this is a core philosophy that makes the system consistent and powerful. Types of files include:

- **Regular files**: Documents, configurations, logs, scripts
- **Directories**: Special files that can contain other files
- **Device files**: Hardware interfaces (in `/dev`)
- **Socket files**: Inter-process communication endpoints
- **Named pipes**: Another form of inter-process communication

**Beginner's Note**: Think of your Linux filesystem as a virtual filing cabinet, where you can create folders (directories), store documents (files), move items around, copy important papers, and throw away (delete) unnecessary ones.

**SRE Perspective**: Understanding this philosophy helps you interact with systems consistently, whether you're editing a config file, analyzing a log, or even interacting with a network interface.

### **File Manipulation in SRE Work**

File operations are the building blocks of system maintenance and incident response:

- **Creating files/directories**: Setting up new configurations, organizing logs
- **Viewing files**: Analyzing logs during an incident, checking configurations
- **Copying/Moving**: Backing up before changes, reorganizing resources
- **Deleting**: Cleaning up temp files, removing old logs to free space

**SRE Perspective**: During incidents, your ability to quickly navigate to the right directory, view the correct log file, and potentially make a backup before implementing changes can make the difference between a minor hiccup and an extended outage.

---

## 💻 **Commands to Learn Today**

### **1. Creating Files and Directories (`touch`, `mkdir`)**

#### **`touch` - Create Empty Files or Update Timestamps**

**Purpose**: Create new empty files or update timestamps of existing files.

**Syntax:**

```bash
touch [options] filename(s)
```

**Common options:**

- `-a`: Change only the access time
- `-m`: Change only the modification time

**Basic Examples:**

Create a new empty file:

```bash
touch notes.txt
```

Create multiple files at once:

```bash
touch file1.txt file2.txt file3.txt
```

**Intermediate Examples:**

Update timestamp of an existing file:

```bash
touch -m config.yml
```

**SRE Context**: SREs use `touch` to create placeholder files, log files, or update file timestamps for testing. For example, creating an empty log file before starting a new service.

**Beginner's Tip**: Think of `touch` as simply "touching" a file to create it or update its timestamp.

#### **`mkdir` - Create Directories**

**Purpose**: Create new directories (folders).

**Syntax:**

```bash
mkdir [options] directory_name(s)
```

**Common options:**

- `-p`: Create parent directories as needed
- `-m`: Set file permissions on creation

**Basic Examples:**

Create a simple directory:

```bash
mkdir projects
```

Create multiple directories:

```bash
mkdir logs backups configs
```

**Intermediate Examples:**

Create nested directories:

```bash
mkdir -p projects/webapp/logs
```

Create a directory with specific permissions:

```bash
mkdir -m 700 secure_configs
```

**SRE Context**: SREs frequently create directory structures for applications, logs, and backups. The `-p` option is particularly useful during deployment scripts to ensure the required directory structure exists.

**Beginner's Tip**: The `-p` flag is like telling `mkdir` to create the entire path at once, even if the parent directories don't exist yet.

### **2. Viewing File Contents (`cat`, `less`, `more`, `head`, `tail`)**

#### **`cat` - Concatenate and Display Files**

**Purpose**: Show the entire contents of a file.

**Syntax:**

```bash
cat [options] filename(s)
```

**Common options:**

- `-n`: Number all output lines
- `-A`: Show all non-printing characters (helpful for troubleshooting)

**Basic Examples:**

View a file:

```bash
cat notes.txt
```

Display multiple files:

```bash
cat file1.txt file2.txt
```

**Intermediate Examples:**

View file with line numbers:

```bash
cat -n script.sh
```

Show non-printing characters:

```bash
cat -A config.file
```

**SRE Context**: `cat` is best for viewing small configuration files or error messages. For large files like logs, other tools are more appropriate.

**Beginner's Tip**: `cat` simply dumps the entire file contents to your screen - great for small files, but overwhelming for large ones.

#### **`less` - View Files with Pagination**

**Purpose**: Interactively view large files one screen at a time.

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

**Basic Examples:**

View a large file:

```bash
less /var/log/syslog
```

**Intermediate Examples:**

View with line numbers:

```bash
less -N /var/log/apache2/error.log
```

Follow a log file in real-time:

```bash
less +F /var/log/application.log
```

**SRE Context**: `less` is the preferred tool for examining large log files during troubleshooting. Its search functionality is invaluable for finding specific error messages in logs.

**Beginner's Tip**: Think of `less` as a more powerful way to read files - you can scroll up and down, search for text, and exit whenever you want.

#### **`more` - View Files with Basic Pagination**

**Purpose**: Display file contents one screen at a time (simpler than `less`).

**Navigation in `more`:**

- `Space`: Next page
- `q`: Quit

**Basic Example:**

```bash
more /etc/passwd
```

**Beginner's Tip**: `more` is simpler than `less` but has fewer features. Most SREs prefer `less` for its additional capabilities.

#### **`head` - View the Beginning of Files**

**Purpose**: Display the first part of files (default: 10 lines).

**Syntax:**

```bash
head [options] filename(s)
```

**Common options:**

- `-n N`: Show first N lines
- `-c N`: Show first N bytes

**Basic Examples:**

View first 10 lines:

```bash
head /var/log/syslog
```

**Intermediate Examples:**

View first 20 lines:

```bash
head -n 20 /var/log/auth.log
```

**SRE Context**: `head` is useful for checking the format of log files or viewing headers and initial configuration entries.

**Beginner's Tip**: `head` shows you the "top" of a file - useful when you only need to see how a file starts.

#### **`tail` - View the End of Files**

**Purpose**: Display the last part of files (default: 10 lines).

**Syntax:**

```bash
tail [options] filename(s)
```

**Common options:**

- `-n N`: Show last N lines
- `-f`: Follow mode - continuously show new lines as they're added
- `-F`: Follow mode that handles log rotation

**Basic Examples:**

View last 10 lines:

```bash
tail /var/log/nginx/error.log
```

**Intermediate Examples:**

View last 50 lines:

```bash
tail -n 50 /var/log/application.log
```

Monitor a log file in real-time:

```bash
tail -f /var/log/application.log
```

**SRE Context**: `tail -f` is one of the most important commands for SREs during incident response, allowing real-time monitoring of log files to identify errors as they occur.

**Beginner's Tip**: `tail` shows the "bottom" of a file - particularly useful for logs where the newest entries are typically at the end.

### **3. Copying and Moving Files (`cp`, `mv`)**

#### **`cp` - Copy Files and Directories**

**Purpose**: Create duplicates of files or directories.

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

**Basic Examples:**

Copy a file:

```bash
cp notes.txt backup.txt
```

Copy a file to another directory:

```bash
cp report.log /tmp/
```

**Intermediate Examples:**

Copy a directory and all its contents:

```bash
cp -r projects projects_backup
```

Copy preserving permissions and timestamps (best for backups):

```bash
cp -a /etc/nginx /etc/nginx.bak
```

**SRE Context**: SREs frequently make backups before modifying critical configuration files. The `-a` option is crucial for maintaining all file attributes in backups.

**Beginner's Tip**: Always use `-r` when copying directories, or you'll only copy the directory itself without its contents.

#### **`mv` - Move or Rename Files and Directories**

**Purpose**: Relocate or rename files and directories.

**Syntax:**

```bash
mv [options] source destination
```

**Common options:**

- `-i`: Interactive (prompt before overwrite)
- `-b`: Create a backup of each existing destination file
- `-v`: Verbose output

**Basic Examples:**

Rename a file:

```bash
mv oldname.txt newname.txt
```

Move a file to another directory:

```bash
mv report.log /var/log/
```

**Intermediate Examples:**

Move multiple files:

```bash
mv *.log /var/log/archive/
```

Move with backup of destination:

```bash
mv -b important.conf /etc/app/
```

**SRE Context**: `mv` is used to implement new configurations, archive logs, and organize files during maintenance tasks.

**Beginner's Tip**: `mv` can both move AND rename files - if the destination is a directory, the file is moved; if it's a filename, the file is renamed.

### **4. Deleting Files and Directories (`rm`, `rmdir`)**

#### **`rm` - Remove Files and Directories**

**Purpose**: Delete files and directories.

**Syntax:**

```bash
rm [options] file(s)
```

**Common options:**

- `-r`: Recursively remove directories and their contents
- `-f`: Force removal without prompt
- `-i`: Interactive (prompt before removal)
- `-v`: Verbose output

**Basic Examples:**

Remove a file:

```bash
rm temporary.txt
```

Remove multiple files:

```bash
rm file1.txt file2.txt
```

**Intermediate Examples:**

Remove a directory and all its contents:

```bash
rm -r old_project/
```

Prompt before each removal (safer):

```bash
rm -i *.conf
```

**SRE Context**: SREs use `rm` to clean up temporary files, old logs, and obsolete configurations. ALWAYS use caution with `rm -rf` in production environments!

**Beginner's Tip**: Remember that Linux has no "recycle bin" - when you delete files with `rm`, they're typically gone for good.

#### **`rmdir` - Remove Empty Directories**

**Purpose**: Delete empty directories only.

**Syntax:**

```bash
rmdir [options] directory(s)
```

**Common options:**

- `-p`: Remove directory and its ancestors

**Basic Examples:**

Remove an empty directory:

```bash
rmdir empty_folder
```

**Intermediate Examples:**

Remove nested empty directories:

```bash
rmdir -p parent/child/grandchild
```

**SRE Context**: `rmdir` is safer than `rm -r` for cleaning up directory structures as it fails if the directory contains files, preventing accidental data loss.

**Beginner's Tip**: If `rmdir` gives an error, it means the directory isn't empty - you'll need to remove its contents first or use `rm -r` (carefully!).

---

## 🔍 **SRE Perspective: Critical File Operations**

In SRE practice, certain file operations are particularly important:

### **1. Log Rotation and Management**

SREs must understand how to handle logs to prevent disk space issues:

```bash
# View the last 100 lines of a log
tail -n 100 /var/log/application.log
   
# Monitor logs in real-time during an incident
tail -f /var/log/application.log
   
# Archive old logs
mv /var/log/application.log.1 /var/log/archive/
```

### **2. Configuration Backups**

Always back up configs before changes:

```bash
# Create a timestamped backup
cp -a /etc/nginx/nginx.conf /etc/nginx/nginx.conf.$(date +%Y%m%d-%H%M%S).bak
```

### **3. Safe Deletion Practices**

Use interactive mode or create backup directories:

```bash
# Interactive deletion
rm -i important_file.conf
   
# Alternative: move to a backup location instead of deleting
mkdir -p ~/trash
mv important_file.conf ~/trash/
```

### **4. Disk Space Management**

Clean up temporary files and old logs:

```bash
# Find large files
find /var -type f -size +100M

# Safely remove old log files
find /var/log -name "*.log.??" -mtime +30 -exec rm {} \;
```

---

## 🎯 **Practical Exercises: From Beginner to SRE**

### **Beginner Exercises**

1. Create a directory named `practice` in your home folder
2. Inside `practice`, create three empty files: `file1.txt`, `file2.txt`, and `file3.txt`
3. Create a subdirectory called `backup`
4. Copy `file1.txt` to the `backup` directory
5. Rename `file2.txt` to `notes.txt`
6. View the contents of all your files using `cat`
7. Delete `file3.txt`

### **Intermediate Exercises**

1. Create a nested directory structure: `~/projects/webapp/config/`
2. Create a simple configuration file in this structure:

   ```bash
   echo "# Sample configuration" > ~/projects/webapp/config/app.conf
   ```

3. Make a backup of this file with a timestamp in the filename
4. Use `head`, `tail`, and `less` to view the configuration file
5. Create multiple log entries and practice viewing them:

   ```bash
   for i in {1..50}; do echo "Log entry $i" >> ~/projects/webapp/logs.txt; done
   ```

6. View the first and last 10 lines of this log file
7. Practice copying the entire directory structure to a backup location

### **SRE Application Exercises**

1. **Setup Test Environment**:

   ```bash
   mkdir -p ~/sre_practice/configs ~/sre_practice/logs
   ```

2. **Create Test Files**:

   ```bash
   # Create a config file
   echo "# Configuration file for test app" > ~/sre_practice/configs/app.conf
   echo "port=8080" >> ~/sre_practice/configs/app.conf
   echo "debug=true" >> ~/sre_practice/configs/app.conf
   
   # Create sample logs with timestamps
   for i in {1..100}; do
     echo "$(date) - INFO - Test log entry $i" >> ~/sre_practice/logs/app.log
   done
   
   # Create some error entries
   echo "$(date) - ERROR - Connection timeout" >> ~/sre_practice/logs/app.log
   echo "$(date) - ERROR - Database unavailable" >> ~/sre_practice/logs/app.log
   ```

3. **Incident Response Simulation**:
   - Use `grep` to find ERROR entries in the log file
   - Create a backup of the configuration before making changes
   - Modify the configuration file to change settings
   - Monitor the log file in real-time with `tail -f`
   - Practice safe cleanup operations

---

## 📝 **Quiz: Test Your Knowledge**

### **Beginner Level**

1. Which command creates an empty file or updates a file's timestamp?
   - a) `mkdir`
   - b) `touch`
   - c) `cat`
   - d) `cp`

2. To create a directory called "photos", you would type:
   - a) `dir photos`
   - b) `mkdir photos`
   - c) `touch photos`
   - d) `cd photos`

3. Which command would you use to rename a file from "old.txt" to "new.txt"?
   - a) `cp old.txt new.txt`
   - b) `mv old.txt new.txt`
   - c) `rn old.txt new.txt`
   - d) `name old.txt new.txt`

### **Intermediate Level**

4. Which option of `mkdir` allows you to create nested directories like "a/b/c" all at once?
   - a) `-r`
   - b) `-p`
   - c) `-n`
   - d) `-m`

5. How do you list all lines of a file with line numbers?
   - a) `cat -n file.txt`
   - b) `less -N file.txt`
   - c) Both a and b
   - d) Neither a nor b

6. Which command would you use to copy a directory and all its contents while preserving file attributes?
   - a) `cp dir1 dir2`
   - b) `cp -r dir1 dir2`
   - c) `cp -a dir1 dir2`
   - d) `mv dir1 dir2`

### **SRE Application Level**

7. During an incident, you need to monitor a log file that's being actively written to. Which command is most appropriate?
   - a) `cat /var/log/app.log`
   - b) `more /var/log/app.log`
   - c) `tail -f /var/log/app.log`
   - d) `head /var/log/app.log`

8. You need to make changes to a critical configuration file. What should you do first?
   - a) Edit the file directly with a text editor
   - b) Make a backup with `cp -a config.file config.file.bak`
   - c) Run `touch config.file` to update the timestamp
   - d) Delete the file and create a new one

9. A server is running out of disk space due to log files. Which sequence of commands would help identify and address the issue?
   - a) `rm -rf /var/log/*`
   - b) `ls -l /var/log; cat /var/log/*`
   - c) `du -h /var/log | sort -hr; tail -n 10 /var/log/large.log; mv large.log /tmp/`
   - d) `touch /var/log/newfile.log`

---

## ❓ **FAQ: From Beginners to SREs**

### **Beginner FAQs**

**Q1: What's the difference between `cat`, `less`, and `more`?**

**A:**

- `cat` displays the entire file at once (best for small files)
- `less` provides interactive scrolling, searching, and navigation (best for large files)
- `more` is a simpler version of `less` with basic pagination

**Q2: Does `rm` permanently delete files?**

**A:** Yes, the standard `rm` command permanently deletes files without sending them to a trash/recycle bin. Always double-check before deleting, especially when using wildcards.

**Q3: Can I undo a `mv` or `rm` command?**

**A:** Generally, no. Once you move or remove a file, there's no built-in "undo" function. This is why making backups before operations is so important in Linux.

### **Intermediate FAQs**

**Q4: What's the difference between `cp` and `cp -a`?**

**A:**

- `cp` only copies file content
- `cp -a` (archive) preserves permissions, ownership, timestamps, and copies directories recursively - making it ideal for backups

**Q5: How can I copy or move multiple files at once?**

**A:** Use wildcards or specify multiple source files:

```bash
# Using wildcards
cp *.log /var/log/backup/

# Specifying multiple files
mv file1.txt file2.txt file3.txt /destination/
```

**Q6: What happens if I try to `cp` or `mv` a file to a location where a file with that name already exists?**

**A:** By default, the existing file will be overwritten without warning. Use the `-i` option (interactive) to get a prompt before overwriting:

```bash
cp -i source.txt destination.txt
mv -i file.txt /path/to/existing/file.txt
```

### **SRE FAQs**

**Q7: What's the safest way to delete files on production systems?**

**A:** Production systems require extra caution:

- Always use `-i` for interactive prompting: `rm -i filename`
- Consider moving instead of deleting: `mv filename /path/to/archive/`
- Use full paths to avoid mistakes from your current directory
- Create temporary backup directories for "deleted" files that can be permanently removed later
- For critical systems, implement change management procedures before any deletion

**Q8: How can I find the largest files or directories when troubleshooting disk space issues?**

**A:** Common approaches include:

- `du -h --max-depth=1 /path | sort -hr` to find large directories
- `find /path -type f -size +100M -exec ls -lh {} \;` to find files over 100MB
- Focus on common culprits: log directories, temporary files, core dumps

**Q9: What's the most efficient way to examine very large log files during an incident?**

**A:** For large log files:

- Use `less` with search functionality (`/pattern`) to find relevant sections
- Use `grep "error" logfile | tail -n 100` to find recent errors
- For real-time monitoring: `tail -f logfile | grep "error"`
- Split analysis: `head` for initialization issues, `tail` for recent issues

---

## 🚧 **Common Issues and Troubleshooting**

### **Issue 1: "No such file or directory" errors**

**Possible causes:**

- Typo in the file or directory name
- Trying to access a path that doesn't exist
- Working in the wrong directory

**Solutions:**

```bash
# Check current directory
pwd

# List files to verify names
ls -la

# Check for typos in path
ls -la /path/to/check/
```

### **Issue 2: "Permission denied" errors**

**Possible causes:**

- Insufficient permissions for the file
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
```

### **Issue 3: "No space left on device" when creating files**

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
```

### **Issue 4: "rm: cannot remove 'folder': Is a directory"**

**Possible causes:**

- Trying to use `rm` without `-r` on a directory

**Solutions:**

```bash
# For directories, use -r
rm -r directory_name

# Or to remove only if empty
rmdir directory_name
```

---

## 🚨 **SRE Caution: Dangerous Commands**

Be extremely careful with these commands, especially on production systems:

1. **`rm -rf /`**: NEVER run this! It attempts to recursively delete everything from the root.

2. **`rm -rf *`**: Extremely dangerous. Deletes everything in the current directory recursively.

3. **`> filename`**: Truncates a file to zero length. Particularly dangerous with important files like `/etc/passwd`.

⚠️ **Best Practices:**

- Always double-check commands with destructive potential
- Use `ls` to preview what wildcards will match before using them with `rm`
- Consider using `rm -i` on production systems
- Maintain current backups of critical systems

---

## 🔄 **Real-World SRE Scenario: Log Analysis During an Incident**

**Situation:** You receive alerts that a web service is returning 500 errors. Users are reporting that they cannot access the application. You need to quickly identify the issue.

**SRE Response Using Today's Commands:**

1. SSH to the affected server:

   ```bash
   ssh sre@web-server-prod-03
   ```

2. Navigate to the log directory:

   ```bash
   cd /var/log/nginx
   ```

3. Check the most recent error logs:

   ```bash
   tail -n 50 error.log
   ```

4. Look for patterns in the application logs:

   ```bash
   grep "ERROR" /var/log/application/app.log | tail -n 20
   ```

5. Monitor logs in real-time to correlate with errors:

   ```bash
   tail -f /var/log/application/app.log
   ```

6. After identifying a configuration issue, make a backup before changes:

   ```bash
   cp -a /etc/nginx/sites-available/webapp.conf /etc/nginx/sites-available/webapp.conf.bak.$(date +%Y%m%d-%H%M%S)
   ```

7. Edit the configuration file to fix the issue.

8. After resolving the issue, archive relevant logs for post-incident analysis:

   ```bash
   mkdir -p /var/log/incident_archives/$(date +%Y%m%d)
   cp /var/log/application/app.log /var/log/incident_archives/$(date +%Y%m%d)/
   ```

This sequence demonstrates how file operations are fundamental to incident response and resolution. The ability to quickly navigate to the right directories, examine logs, and make safe changes can dramatically reduce the Mean Time To Resolution (MTTR).

---

## 📚 **Further Learning Resources**

### **For Beginners**

- [Linux Journey - Text Manipulation](https://linuxjourney.com/lesson/text-manipulation-tools) - Interactive tutorials for file operations
- [Linux Command Line by William Shotts (Free Ebook)](http://linuxcommand.org/tlcl.php) - Comprehensive guide with examples

### **For Intermediate Users**

- [Bash Guide for Beginners - File Operations](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_02_03.html) - Detailed explanation of file commands
- [Linux Command Library - File Operations](https://linuxcommandlibrary.com/basic/filecommands.html) - Comprehensive reference

### **For SRE Application**

- [Google SRE Book - Chapter 13: Data Processing](https://sre.google/sre-book/data-processing/) - SRE perspective on data handling
- [Effective Troubleshooting for SREs](https://www.usenix.org/conference/srecon20americas/presentation/lunney) - Case studies of troubleshooting with Linux tools

---

🎓 **Day 2 completed!** Tomorrow, we'll explore file permissions and ownership - critical concepts for securing Linux systems and controlling access to sensitive data in SRE environments.
