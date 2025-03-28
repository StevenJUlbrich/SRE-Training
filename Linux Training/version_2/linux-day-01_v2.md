# 🚀 **Day 1: Linux Fundamentals for SRE - Shell, Navigation, and Filesystem**

---

## 📌 **Introduction**

Welcome to Day 1 of your journey to becoming a Site Reliability Engineer (SRE)! Linux command-line skills form the foundation of successful SRE work, enabling you to monitor systems, troubleshoot issues, automate tasks, and maintain reliable infrastructure.

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

---

## 📚 **Core Concepts Explained**

### **What is Linux and Why SREs Need It**

Linux is an open-source operating system that powers most of the world's servers, cloud infrastructure, and containerized applications. As an SRE, you'll encounter Linux in virtually every environment:

- **Production servers**: Web servers, application servers, database servers
- **Cloud environments**: AWS, GCP, Azure all use Linux-based virtual machines
- **Container platforms**: Docker, Kubernetes all run on Linux
- **Monitoring systems**: Most observability tools run on Linux

Linux's reliability, security, and flexibility make it the ideal platform for mission-critical systems that SREs are responsible for maintaining.

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

### **Filesystem Hierarchy Standard (FHS)**

Linux organizes files and directories in a structured hierarchy. Understanding this structure helps you quickly locate configuration files, logs, and other important system components during incidents:

- **`/`** (root): The top-level directory
- **`/etc`**: System-wide configuration files - critical for service configuration
- **`/var`**: Variable files like logs and databases - crucial for troubleshooting
- **`/bin` & `/usr/bin`**: Essential command binaries
- **`/home`**: User home directories
- **`/tmp`**: Temporary files
- **`/proc`**: Virtual filesystem for system information - used for real-time monitoring

Think of the FHS as a city map for first responders - knowing it well helps you quickly reach the scene of an incident.

---

## 💻 **Commands to Learn Today**

### **1. pwd – Print Working Directory**

**Purpose**: Shows your current location in the filesystem.

**SRE Context**: When troubleshooting an issue or following a procedure, confirming your location is a critical first step to avoid mistakes, especially during incidents.

**Syntax:**
```bash
pwd
```

**Example:**
```bash
[sre@prod-server ~]$ pwd
/home/sre
```

### **2. ls – List Directory Contents**

**Purpose**: View files and directories in the current or specified location.

**SRE Context**: You'll regularly need to locate configuration files, logs, or executables when diagnosing issues or making changes.

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

**Examples:**

Basic listing:
```bash
[sre@prod-server ~]$ ls
applications  backups  logs  scripts
```

Detailed listing with permissions and timestamps:
```bash
[sre@prod-server ~]$ ls -l
total 16
drwxr-xr-x 4 sre sre 4096 Mar 25 08:30 applications
drwxr-xr-x 2 sre sre 4096 Mar 24 14:15 backups
drwxr-xr-x 3 sre sre 4096 Mar 25 10:22 logs
drwxr-xr-x 2 sre sre 4096 Mar 23 16:45 scripts
```

Show hidden configuration files in your home directory:
```bash
[sre@prod-server ~]$ ls -la
total 28
drwxr-xr-x 5 sre  sre  4096 Mar 25 11:30 .
drwxr-xr-x 8 root root 4096 Feb 15 09:10 ..
-rw------- 1 sre  sre   220 Feb 15 09:10 .bash_history
-rw-r--r-- 1 sre  sre   345 Feb 15 09:10 .bashrc
drwxr-xr-x 4 sre  sre  4096 Mar 25 08:30 applications
drwxr-xr-x 2 sre  sre  4096 Mar 24 14:15 backups
drwxr-xr-x 3 sre  sre  4096 Mar 25 10:22 logs
drwxr-xr-x 2 sre  sre  4096 Mar 23 16:45 scripts
```

### **3. cd – Change Directory**

**Purpose**: Navigate between directories.

**SRE Context**: Moving efficiently between key locations (config directories, log directories) lets you respond faster to incidents.

**Syntax:**
```bash
cd [directory_path]
```

**Examples:**

Change to a specific directory:
```bash
[sre@prod-server ~]$ cd /var/log
[sre@prod-server log]$ 
```

Move to a subdirectory:
```bash
[sre@prod-server ~]$ cd scripts
[sre@prod-server scripts]$ 
```

Go back to the previous directory:
```bash
[sre@prod-server scripts]$ cd ..
[sre@prod-server ~]$ 
```

Return to your home directory from anywhere:
```bash
[sre@prod-server /var/log]$ cd
[sre@prod-server ~]$ 
```

Move up one level and then into a different directory:
```bash
[sre@prod-server scripts]$ cd ../logs
[sre@prod-server logs]$ 
```

### **4. Getting Help (`man`, `--help`, `info`)**

**Purpose**: Access documentation for commands and tools.

**SRE Context**: In high-pressure situations, you often need to quickly verify command options or syntax.

#### **`man` - Manual Pages**

**Syntax:**
```bash
man [command]
```

**Example:**
```bash
[sre@prod-server ~]$ man ls
```
This displays the full manual page for the `ls` command with all available options and examples.

#### **`--help` - Quick Help**

**Syntax:**
```bash
[command] --help
```

**Example:**
```bash
[sre@prod-server ~]$ ls --help
```
Provides a concise summary of command options.

#### **`info` - Detailed Documentation**

**Syntax:**
```bash
info [command]
```

**Example:**
```bash
[sre@prod-server ~]$ info bash
```
Offers more detailed and structured documentation than man pages.

---

## 🔍 **SRE Perspective: Why These Skills Matter**

SRE work often involves responding to incidents where systems are under stress:

1. **Rapid Navigation**: During outages, you need to move quickly between directories to check logs, configs, and running services.

2. **Pattern Recognition**: Using `ls` options helps you spot recently modified files or size abnormalities that could indicate problems.

3. **Command Precision**: When working with critical production systems, understanding commands fully through documentation prevents costly mistakes.

4. **Shared Language**: Linux commands are universal across environments - skills transfer between different systems and cloud platforms.

---

## 🎯 **Practical Exercise: SRE First Steps**

Practice these tasks in your Linux environment:

1. Open your terminal and determine your current location using `pwd`.

2. Use `ls -la` to list all files in your current directory. Note any hidden configuration files (starting with `.`).

3. Navigate to the `/var/log` directory using `cd`. This directory typically contains system logs.

4. List the contents of `/var/log` sorted by modification time (`ls -lt`) to see the most recently updated log files.

5. Look for large files that might be consuming disk space (`ls -lh`).

6. Navigate back to your home directory (`cd` or `cd ~`).

7. Read the man page for the `cd` command to discover any additional options (`man cd`).

8. Find basic information about your Linux system (`uname --help` then `uname -a`).

---

## 📝 **Quiz: Day 1 Foundations**

Test your understanding of today's material:

1. Which command displays your current location in the filesystem?
   - a) `dir`
   - b) `pwd`
   - c) `loc`
   - d) `cd`

2. You need to check the timestamps of log files during an incident. Which command shows the most recently modified files first?
   - a) `ls -r`
   - b) `ls -a`
   - c) `ls -lt`
   - d) `ls -h`

3. How do you list all files, including hidden ones, with detailed information in human-readable format?
   - a) `ls -all`
   - b) `ls -lah`
   - c) `ls -hidden`
   - d) `ls -full`

4. During an incident, you need to quickly look up the options for the `grep` command. Which is the fastest way?
   - a) `man grep`
   - b) `grep --help`
   - c) `info grep`
   - d) `help grep`

5. In the Linux filesystem hierarchy, which directory typically contains log files that SREs need to examine during troubleshooting?
   - a) `/log`
   - b) `/usr/log`
   - c) `/var/log`
   - d) `/etc/log`

---

## ❓ **FAQ for SREs**

**Q1: Why is the command line preferred over graphical interfaces for SRE work?**

**A:** Command-line interfaces offer:
- **Remote access**: Work on servers without a GUI
- **Efficiency**: Perform complex operations faster
- **Automation**: Easy to script and repeat operations
- **Resource efficiency**: Lower overhead than graphical interfaces
- **SSH access**: Connect securely to remote systems

**Q2: How can I efficiently navigate between frequently used directories?**

**A:** Try these techniques:
- Use `cd -` to toggle between your current and previous directory
- Create aliases for common locations in your `.bashrc` file
- Use the `pushd` and `popd` commands to maintain a directory stack

**Q3: How do SREs typically find files or commands on an unfamiliar system?**

**A:** 
- Use `which [command]` to locate a command's executable
- Use `locate [filename]` for quick file searching (if installed)
- Use `find / -name [filename]` for comprehensive searches
- Check common locations: configuration files in `/etc`, logs in `/var/log`

**Q4: What's the difference between relative and absolute paths, and when should I use each?**

**A:**
- **Absolute paths** start with `/` and specify the full location from root (e.g., `/var/log/syslog`)
- **Relative paths** are relative to your current directory (e.g., `../config/settings.json`)
- Use absolute paths in scripts for reliability
- Use relative paths for convenience when navigating interactively

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

---

## 🔄 **Real-World SRE Scenario**

**Situation:** You receive an alert that a web service is down. Initial reports suggest the application server is running out of disk space.

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
   ls -lah
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

This sequence of basic navigation commands is often the first step in diagnosing many production issues. Tomorrow, we'll build on these skills to examine file content and manage the files you've located.

---

## 📚 **Further Learning Resources**

- [Linux Journey - Command Line](https://linuxjourney.com/lesson/the-shell)
- [The Linux Command Line (William Shotts)](http://linuxcommand.org/tlcl.php)
- [Linux Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html)
- [Google SRE Book - Chapter 5: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)

---

🎓 **Day 1 completed!** Tomorrow we'll explore file manipulation commands to view, create, modify, and delete files—essential skills for managing configuration files and logs in SRE work.
