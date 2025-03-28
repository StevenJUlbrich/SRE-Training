# 🚀 **Day 1: Linux Fundamentals for SRE - From Beginner to Practitioner**

---

## 📌 **Introduction**

Welcome to Day 1 of your journey to becoming a Site Reliability Engineer (SRE)! This course is designed to accommodate learners of various skill levels, from complete beginners to those with some Linux experience who want to apply their skills to SRE work.

Linux command-line skills form the foundation of successful SRE work, enabling you to monitor systems, troubleshoot issues, automate tasks, and maintain reliable infrastructure.

### **Today's Topics**

- What is Linux and why is it critical for SRE work?
- Understanding the Shell and its role in system management
- Basic navigation commands (`pwd`, `ls`, `cd`) for daily operations
- How to access help and documentation (`man`, `--help`, `info`)
- Filesystem Hierarchy Standard (FHS) - the map of your system

### **Learning Objectives**

By the end of today, you'll be able to:

- Explain why Linux is the backbone of modern infrastructure
- Navigate a Linux server confidently using terminal commands
- Find detailed help for any command when needed
- Understand the organization of Linux filesystem
- Relate these basic skills to real SRE responsibilities

### **How to Use This Resource**

This material is structured in layers:

- **Beginner Sections**: Essential for those new to Linux
- **Intermediate Sections**: Providing more details and options
- **SRE Application Sections**: Connecting concepts to real SRE work
- **Practical Exercises**: For hands-on experience at various skill levels
- **Real-World Scenarios**: Applying knowledge to actual SRE situations

---

## 📚 **Core Concepts Explained**

### **What is Linux and Why SREs Need It**

Linux is an open-source operating system that powers most of the world's servers, cloud infrastructure, and containerized applications. As an SRE, you'll encounter Linux in virtually every environment:

- **Production servers**: Web servers, application servers, database servers
- **Cloud environments**: AWS, GCP, Azure all use Linux-based virtual machines
- **Container platforms**: Docker, Kubernetes all run on Linux
- **Monitoring systems**: Most observability tools run on Linux

Linux's reliability, security, and flexibility make it the ideal platform for mission-critical systems that SREs are responsible for maintaining.

**SRE Perspective**: During incidents, knowing Linux well means you can quickly navigate unfamiliar systems, understand logs, and troubleshoot issues without needing to reference basic commands.

### **What is a Shell?**

The shell is your command center for interacting with Linux systems. Think of it as:

- **Control panel**: Provides direct access to the operating system's capabilities
- **Translator**: Interprets your commands and communicates them to the OS kernel
- **Automation tool**: Can be scripted to perform repetitive tasks

**Common Shell Types:**

- **bash** (Bourne Again Shell) – Most common default
- **zsh** (Z Shell) – Enhanced features, popular with developers
- **sh** (Bourne Shell) – Simpler, more universal

As an SRE, the shell is where you'll spend much of your time - investigating issues, managing systems, and implementing automated solutions.

**Beginner's Note**: You can think of the shell as a text-based receptionist that takes your requests (commands) and delivers them to the right departments (Linux kernel/services).

### **Filesystem Hierarchy Standard (FHS)**

Linux organizes files and directories in a structured hierarchy. Understanding this structure helps you quickly locate configuration files, logs, and other important system components during incidents:

- **`/`** (root): The top-level directory
- **`/etc`**: System-wide configuration files - critical for service configuration
- **`/var`**: Variable files like logs and databases - crucial for troubleshooting
- **`/bin` & `/usr/bin`**: Essential command binaries
- **`/home`**: User home directories
- **`/tmp`**: Temporary files
- **`/proc`**: Virtual filesystem for system information - used for real-time monitoring

**SRE Perspective**: Think of the FHS as a city map for first responders - knowing it well helps you quickly reach the scene of an incident and find the resources you need.

**Beginner's Note**: The Linux filesystem structure is like a well-organized library—each section contains specific types of information, making files easier to find and manage.

---

## 💻 **Commands to Learn Today**

### **1. pwd – Print Working Directory**

**Purpose**: Shows your current location in the filesystem.

**Syntax:**

```bash
pwd
```

**Example:**

```bash
[user@server ~]$ pwd
/home/user
```

**SRE Context**: When troubleshooting an issue or following a procedure, confirming your location is a critical first step to avoid mistakes, especially during incidents.

**Beginner's Tip**: Always run this command when you're not sure where you are in the system. It's like checking your "You Are Here" marker on a map.

### **2. ls – List Directory Contents**

**Purpose**: View files and directories in the current or specified location.

**Syntax:**

```bash
ls [options] [directory]
```

**Common options:**

- `-l` – Long format with permissions, ownership, size, and timestamps
- `-a` – Shows all files including hidden ones (starting with `.`)
- `-h` – Human-readable file sizes (KB, MB, GB)
- `-t` – Sort by modification time (newest first)
- `-r` – Reverse sort order

**Basic Examples:**

Simple listing:

```bash
[user@server ~]$ ls
documents  downloads  pictures  videos
```

Detailed listing:

```bash
[user@server ~]$ ls -l
total 16
drwxr-xr-x 2 user user 4096 Mar 25 09:30 documents
drwxr-xr-x 2 user user 4096 Mar 24 14:15 downloads
drwxr-xr-x 2 user user 4096 Mar 25 11:22 pictures
drwxr-xr-x 2 user user 4096 Mar 23 16:45 videos
```

Show hidden files:

```bash
[user@server ~]$ ls -a
.  ..  .bashrc  .config  documents  downloads  pictures  videos
```

**Intermediate Examples:**

Combining options:

```bash
[user@server ~]$ ls -lah
total 28K
drwxr-xr-x 5 user user 4.0K Mar 25 11:30 .
drwxr-xr-x 8 root root 4.0K Feb 15 09:10 ..
-rw------- 1 user user  220 Feb 15 09:10 .bash_history
-rw-r--r-- 1 user user  345 Feb 15 09:10 .bashrc
drwxr-xr-x 3 user user 4.0K Mar 25 10:22 .config
drwxr-xr-x 2 user user 4.0K Mar 25 09:30 documents
drwxr-xr-x 2 user user 4.0K Mar 24 14:15 downloads
drwxr-xr-x 2 user user 4.0K Mar 25 11:22 pictures
drwxr-xr-x 2 user user 4.0K Mar 23 16:45 videos
```

Sort by modification time (newest first):

```bash
[user@server ~]$ ls -lt
total 16
drwxr-xr-x 2 user user 4096 Mar 25 11:22 pictures
drwxr-xr-x 2 user user 4096 Mar 25 09:30 documents
drwxr-xr-x 2 user user 4096 Mar 24 14:15 downloads
drwxr-xr-x 2 user user 4096 Mar 23 16:45 videos
```

**SRE Context**: You'll regularly need to locate configuration files, logs, or executables when diagnosing issues. During incidents, the `-lt` option is particularly valuable as it shows recently modified files that might be related to the issue.

**Beginner's Tip**: Start with simple `ls`, then add options one by one to see how each changes the output.

### **3. cd – Change Directory**

**Purpose**: Navigate between directories.

**Syntax:**

```bash
cd [directory_path]
```

**Basic Examples:**

Change to a specific directory:

```bash
[user@server ~]$ cd documents
[user@server documents]$ 
```

Change to an absolute path:

```bash
[user@server ~]$ cd /var/log
[user@server log]$ 
```

Go back to the previous directory:

```bash
[user@server documents]$ cd ..
[user@server ~]$ 
```

Return to your home directory from anywhere:

```bash
[user@server /var/log]$ cd
[user@server ~]$ 
```

**Intermediate Examples:**

Navigate through multiple directories:

```bash
[user@server ~]$ cd documents/projects/website
[user@server website]$ 
```

Move up one level and then into a different directory:

```bash
[user@server projects]$ cd ../presentations
[user@server presentations]$ 
```

Toggle between your current and previous directory:

```bash
[user@server /var/log]$ cd -
[user@server ~]$ cd -
[user@server /var/log]$ 
```

**SRE Context**: Moving efficiently between key locations (config directories, log directories) lets you respond faster to incidents. During production issues, you'll frequently need to check logs in `/var/log`, application files, and configuration in `/etc`.

**Beginner's Tip**: Think of `cd` as your way to move around the filesystem "building." Using `cd ..` is like taking one flight of stairs up.

### **4. Getting Help (`man`, `--help`, `info`)**

**Purpose**: Access documentation for commands and tools.

**SRE Context**: In high-pressure situations, you often need to quickly verify command options or syntax. Knowing how to access help efficiently saves crucial time during incidents.

#### **`man` - Manual Pages**

**Syntax:**

```bash
man [command]
```

**Example:**

```bash
[user@server ~]$ man ls
```

This displays the full manual page for the `ls` command with all available options and examples.

**Navigation in man pages:**

- Use arrow keys to scroll
- Press `q` to quit
- Press `/` followed by a term to search
- Press `n` to go to the next search result

#### **`--help` - Quick Help**

**Syntax:**

```bash
[command] --help
```

**Example:**

```bash
[user@server ~]$ ls --help
```

Provides a concise summary of command options.

#### **`info` - Detailed Documentation**

**Syntax:**

```bash
info [command]
```

**Example:**

```bash
[user@server ~]$ info bash
```

Offers more detailed and structured documentation than man pages.

**SRE Tip**: `--help` is often the fastest way to check syntax during incidents, while `man` pages are better for in-depth learning during non-critical times.

**Beginner's Tip**: If you're unsure how to use a command, start with `command --help` for a quick overview.

---

## 🔍 **SRE Perspective: Why These Skills Matter**

SRE work often involves responding to incidents where systems are under stress:

1. **Rapid Navigation**: During outages, you need to move quickly between directories to check logs, configs, and running services.

2. **Pattern Recognition**: Using `ls` options helps you spot recently modified files or size abnormalities that could indicate problems.

3. **Command Precision**: When working with critical production systems, understanding commands fully through documentation prevents costly mistakes.

4. **Shared Language**: Linux commands are universal across environments - skills transfer between different systems and cloud platforms.

5. **Time Efficiency**: Knowing these commands by heart reduces your mean time to resolution (MTTR) during incidents.

---

## 🎯 **Practical Exercises: From Beginner to SRE**

### **Beginner Exercises**

1. Open your terminal and determine your current location using `pwd`.

2. Use `ls` to list files in your current directory.

3. Use `ls -l` to see detailed information about those files.

4. Navigate to your home directory with `cd ~` or just `cd`.

5. List all files, including hidden ones, with `ls -a`.

6. Try to access the manual page for `ls` with `man ls`.

### **Intermediate Exercises**

1. Navigate to the `/etc` directory and list its contents.

2. Use `ls -lah` to see all files with human-readable sizes.

3. Find recently modified files in your home directory with `ls -lt`.

4. Practice navigating between multiple directories using relative and absolute paths.

5. Use `cd -` to toggle between two directories.

6. Compare the output of `man ls`, `ls --help`, and `info ls`.

### **SRE Application Exercises**

1. Navigate to the `/var/log` directory and identify the most recently updated log files using `ls -lt`.

2. Look for large log files that might be consuming disk space (`ls -lh | sort -hr`).

3. Practice quickly moving between key system directories: `/etc`, `/var/log`, and your home directory.

4. Find configuration files for a specific service (e.g., `ls -la /etc | grep ssh`).

5. Simulate an incident response scenario: How quickly can you navigate to check logs, configurations, and system status?

---

## 📝 **Quiz: Test Your Knowledge**

### **Beginner Level**

1. Which command displays your current location in the filesystem?
   - a) `dir`
   - b) `pwd`
   - c) `loc`
   - d) `cd`

2. How do you list all files including hidden ones?
   - a) `ls -a`
   - b) `ls -l`
   - c) `ls -h`
   - d) `ls -r`

3. To move up one directory level, you type:
   - a) `cd ..`
   - b) `cd /`
   - c) `cd up`
   - d) `cd -`

### **Intermediate Level**

4. You need to check the timestamps of files. Which command shows the most recently modified files first?
   - a) `ls -r`
   - b) `ls -a`
   - c) `ls -lt`
   - d) `ls -h`

5. How do you list all files, including hidden ones, with detailed information in human-readable format?
   - a) `ls -all`
   - b) `ls -lah`
   - c) `ls -hidden`
   - d) `ls -full`

6. Which command provides a quick help summary for a specific command?
   - a) `man grep`
   - b) `grep --help`
   - c) `info grep`
   - d) `help grep`

### **SRE Application Level**

7. During an incident, which directory would you check first for application logs?
   - a) `/log`
   - b) `/usr/log`
   - c) `/var/log`
   - d) `/etc/log`

8. You need to quickly switch between two directories during troubleshooting. Which command helps you toggle between them?
   - a) `cd toggle`
   - b) `cd --switch`
   - c) `cd -`
   - d) `cd --last`

9. Which option combination for `ls` would be most useful to identify recently modified configuration files?
   - a) `ls -a`
   - b) `ls -lt`
   - c) `ls -h`
   - d) `ls -r`

---

## ❓ **FAQ: From Beginners to SREs**

### **Beginner FAQs**

**Q1: What's the difference between `ls -a` and `ls -A`?**

**A:**

- `ls -a`: Lists all files including hidden files and the special directories `.` (current) and `..` (parent)
- `ls -A`: Lists hidden files but excludes the `.` and `..` directory entries

**Q2: How do I quickly return to my home directory?**

**A:** Use `cd` without arguments or `cd ~`. Both will immediately take you to your home directory from anywhere in the filesystem.

**Q3: Is Linux case-sensitive?**

**A:** Yes, Linux is case-sensitive for both commands and filenames. `File.txt` and `file.txt` are considered different files.

### **Intermediate FAQs**

**Q4: How can I combine multiple flags with commands?**

**A:** You can either string them together or use them separately:

- `ls -lah` (combined)
- `ls -l -a -h` (separate)
Both achieve the same result.

**Q5: What's the difference between relative and absolute paths?**

**A:**

- **Absolute paths** start with `/` and specify the full location from root (e.g., `/var/log/syslog`)
- **Relative paths** are relative to your current directory (e.g., `../config/settings.json`)

**Q6: What do the permissions in `ls -l` output mean?**

**A:** In the output like `drwxr-xr-x`:

- First character (`d`) indicates the file type (directory, in this case)
- Next three characters (`rwx`) are owner permissions
- Middle three (`r-x`) are group permissions
- Last three (`r-x`) are permissions for others
Where `r` = read, `w` = write, `x` = execute, `-` = no permission

### **SRE FAQs**

**Q7: Why is the command line preferred over graphical interfaces for SRE work?**

**A:** Command-line interfaces offer:

- **Remote access**: Work on servers without a GUI
- **Efficiency**: Perform complex operations faster
- **Automation**: Easy to script and repeat operations
- **Resource efficiency**: Lower overhead than graphical interfaces
- **SSH access**: Connect securely to remote systems

**Q8: How can I efficiently navigate between frequently used directories?**

**A:** Try these techniques:

- Use `cd -` to toggle between your current and previous directory
- Create aliases for common locations in your `.bashrc` file
- Use the `pushd` and `popd` commands to maintain a directory stack

**Q9: How do SREs typically find files or commands on an unfamiliar system?**

**A:**

- Use `which [command]` to locate a command's executable
- Use `locate [filename]` for quick file searching (if installed)
- Use `find / -name [filename]` for comprehensive searches
- Check common locations: configuration files in `/etc`, logs in `/var/log`

---

## 🚧 **Common Issues and Troubleshooting**

### **Issue 1: "No such file or directory" when using `cd`**

**Possible causes:**

- Typo in the directory name
- Directory doesn't exist
- Permission issues
- Using a space in directory name without quotes

**Solutions:**

```bash
# For directories with spaces
cd "My Directory"
# OR
cd My\ Directory

# Check if directory exists
ls -la | grep "directory-name"

# Check permissions
ls -ld /path/to/directory
```

### **Issue 2: Terminal shows strange path or doesn't recognize commands**

**Possible causes:**

- PATH environment variable issues
- Wrong shell
- Incorrect environment setup

**Solutions:**

```bash
# Check your current shell
echo $SHELL

# Check your PATH variable
echo $PATH

# Reset your terminal or source your profile
source ~/.bashrc
```

### **Issue 3: `ls` command shows strange colors or no colors**

**Possible causes:**

- Color settings not enabled
- Terminal doesn't support colors
- Aliases not set

**Solutions:**

```bash
# Enable colors temporarily
ls --color=auto

# Set alias permanently
echo "alias ls='ls --color=auto'" >> ~/.bashrc
source ~/.bashrc
```

---

## 🔄 **Real-World SRE Scenario**

**Situation:** You receive an alert at 2 AM that a web service is down. Initial reports suggest the application server is running out of disk space.

**SRE Response Using Today's Commands:**

1. SSH to the affected server:

   ```bash
   ssh sre@web-server-prod-03
   ```

2. Check your current location:

   ```bash
   pwd
   ```

3. Navigate to the log directory:

   ```bash
   cd /var/log
   ```

4. List logs by size to identify space consumers:

   ```bash
   ls -lah | sort -rh
   ```

5. Look for recently modified log files that might indicate the problem:

   ```bash
   ls -lt
   ```

6. Check the application-specific logs:

   ```bash
   cd /var/log/application-name
   ls -lah
   ```

7. Navigate to the application directory to check for other issues:

   ```bash
   cd /var/www/application-name
   ls -la
   ```

This sequence of basic navigation commands is often the first step in diagnosing many production issues. Tomorrow, we'll build on these skills to examine file content and manage the files you've located.

---

## 📚 **Further Learning Resources**

### **For Beginners**

- [Linux Journey - Command Line](https://linuxjourney.com/lesson/the-shell) - Interactive tutorials for beginners
- [Linux Command Line by William Shotts (Free Ebook)](http://linuxcommand.org/tlcl.php) - Comprehensive guide starting from basics

### **For Intermediate Users**

- [Linux Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html) - Official documentation on directory structure
- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html) - In-depth bash shell documentation

### **For SRE Application**

- [Google SRE Book - Chapter 5: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) - Industry-standard SRE practices
- [Practical Linux for Incident Response](https://learning.oreilly.com/library/view/practical-linux-incident/9781484266540/) - Linux commands applied to incident scenarios

---

🎓 **Day 1 completed!**

Tomorrow we'll explore file manipulation commands to view, create, modify, and delete files—essential skills for managing configuration files and logs in SRE work.
