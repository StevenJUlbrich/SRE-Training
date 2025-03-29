# 🚀 Linux SRE Training Module – Day 1 (v15.1)

## 📌 Introduction 
Welcome to **Day 1** of your Linux SRE Training! Today, we focus on **The Absolute Basics**—laying the foundation for everything from daily system administration to high-stakes site reliability engineering. This module will guide you through essential commands (`pwd`, `ls`, `cd`, `man`) and core filesystem concepts, ensuring you can confidently navigate any Linux environment.

### Objectives

#### Beginner (Tier 1)
1. **Identify** what Linux is and why it’s widely used.  
2. **Recognize** the purpose of a shell and basic commands.  
3. **Demonstrate** simple navigation using `pwd`, `ls`, and `cd`.

#### Intermediate (Tier 2)
1. **Apply** key command options (flags) to obtain detailed information.  
2. **Locate and utilize** manual pages efficiently (`man` and `--help`).  
3. **Relate** filesystem structures to operational tasks (logs, configs).

#### SRE-Level (Tier 3)
1. **Diagnose** common issues quickly by leveraging command-line skills.  
2. **Automate** navigation and information gathering in complex scenarios.  
3. **Analyze** filesystem implications for performance, security, and reliability.

**Connection to Future Topics**: Mastering these fundamentals will prepare you for advanced file manipulation, process management, system monitoring, and automation that we’ll explore in upcoming modules.

---

## 📚 Core Concepts

Below, each concept is broken down with a **beginner analogy**, a **technical explanation**, an **SRE application**, and a note on **system impact**.

### 1. What is Linux?
- **Beginner Analogy**: Linux is like the engine of a car—it powers everything under the hood so the rest of the “car” can function.
- **Technical Explanation**: Linux is an open-source operating system kernel that manages hardware resources and provides essential services. Distributions (like Ubuntu, CentOS, Debian) layer software on top of the Linux kernel.
- **SRE Application**: As an SRE, you’ll work on servers that almost always run Linux. Understanding how it’s structured enables reliable operations, troubleshooting, and performance tuning.
- **System Impact**: Linux’s modular design influences how processes run, how resources are allocated, and how you monitor or debug system behavior.

### 2. What’s a Terminal/Shell?
- **Beginner Analogy**: A shell is like a “personal assistant” that takes your commands and executes them.
- **Technical Explanation**: The shell (e.g., `bash`, `zsh`) is a command-line interpreter that processes your text commands and returns output from the operating system.
- **SRE Application**: Most SRE tasks (monitoring, deploying, debugging) happen in the shell—especially over SSH to remote servers.
- **System Impact**: Shell usage has minimal overhead but is powerful enough to alter system configurations, so proper usage and caution are crucial.

### 3. Basic Navigation
- **Beginner Analogy**: Navigating the Linux filesystem is like finding rooms in a large building; commands (`pwd`, `ls`, `cd`) are your map and directions.
- **Technical Explanation**: You use `pwd` (present working directory) to see where you are, `ls` (list) to see contents, and `cd` (change directory) to move around.
- **SRE Application**: Efficient navigation is key when responding to incidents—logs in `/var/log`, configs in `/etc`, etc.
- **System Impact**: Navigation itself has minimal system impact, but the directories you access and modify may have security or operational implications.

### 4. Getting Help
- **Beginner Analogy**: `man` pages and `--help` messages are like instruction manuals that come with appliances.
- **Technical Explanation**: `man <command>` retrieves full manual entries; `--help` gives a concise usage overview; `info` can provide more in-depth documentation.
- **SRE Application**: Under time pressure, quickly checking the correct flags or syntax can prevent errors and speed up incident resolution.
- **System Impact**: Documentation commands themselves don’t alter the system, but using them ensures you run the correct commands in production.

### 5. File System Structure
- **Beginner Analogy**: Think of the Linux filesystem like a well-organized library. Sections (`/home`, `/var`, `/etc`) group specific types of “books” (files).
- **Technical Explanation**: Linux follows the Filesystem Hierarchy Standard, with root (`/`) at the top. Directories have specific roles:  
  - `/etc` for configuration  
  - `/var` for variable data (logs, spool files)  
  - `/home` for user directories, etc.
- **SRE Application**: Knowing where key logs/configs reside is crucial for diagnosing production issues quickly.
- **System Impact**: The filesystem’s structure influences file permissions, data storage strategies, and how you plan for disk capacity in production environments.

---

## 💻 Command Breakdown

Below are **five** detailed breakdowns: four commands (`pwd`, `ls`, `cd`, `man`) plus the **filesystem concept** presented in a similar structured format.

---

### **Command: pwd (Print Working Directory)**

**Command Overview:**  
`pwd` shows the absolute path of your current directory. This is critical for verifying your location—especially before making changes to important files or directories in production.

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description                                | SRE Usage Context                                         |
|-------------|----------------|--------------------------------------------|-----------------------------------------------------------|
| *(none)*    | `pwd`          | Prints the current working directory path | Quick check to ensure you’re in the correct directory     |
| `-L`        | `pwd -L`       | Displays logical path (based on symlinks) | Used when working with symlinked paths in certain builds  |
| `-P`        | `pwd -P`       | Displays the physical path (no symlinks)  | Useful if you need the real directory path for scripting  |

**Tiered Examples:**

* 🟢 **Beginner Example:**
```bash
# Example: Confirm your current directory
$ pwd
/home/student
```
*Explanation*: The shell displays your absolute path, showing you're in `/home/student` directory.

* 🟡 **Intermediate Example:**
```bash
# Example: Checking actual directory behind a symlink
$ pwd -P
/home/student/my_symlinked_folder
```
*Explicit context*: This helps you see the *real* path if `/home/student/my_symlinked_folder` is just a symbolic link to another location.

* 🔴 **SRE-Level Example:**
```bash
# Example: Ensuring correct directory before critical operations
$ if [[ "$(pwd -P)" == "/var/www/production" ]]; then
>   echo "Deploying new version..."
>   # (Deployment script here)
> else
>   echo "Not in production directory, aborting!"
> fi
```
*Explicit context*: Prevents accidental deployment to the wrong environment by verifying the physical path.

**Instructional Notes:**

* 🧠 **Beginner Tip:** `pwd` is especially useful when you open multiple terminals or SSH sessions.  
* 🧠 **Beginner Tip:** If you’re ever unsure “where” you are, `pwd` is a safe, no-impact command to run.

* 🔧 **SRE Insight:** In complex scripts, verifying the actual path (`-P`) can prevent “symlink confusion.”  
* 🔧 **SRE Insight:** Combine `pwd` with environment checks to guard against destructive operations in the wrong directory.

* ⚠️ **Common Pitfall:** Forgetting to confirm your location before moving or deleting files.  
* ⚠️ **Common Pitfall:** Relying on a symlink path in production can cause confusion when code expects the real path.

* 🚨 **Security Note:** Printing the working directory itself poses minimal risk, but always be aware of exposing internal paths in logs.  
* 💡 **Performance Impact:** `pwd` is lightweight and has negligible impact on system resources.

---

### **Command: ls (List Directory Contents)**

**Command Overview:**  
`ls` displays the contents of a directory. It’s used constantly to identify files, directories, hidden items, and file details like permissions or timestamps.

**Syntax & Flags:**

| Flag/Option | Syntax Example   | Description                                                       | SRE Usage Context                                               |
|-------------|------------------|-------------------------------------------------------------------|-----------------------------------------------------------------|
| `-l`        | `ls -l`         | Long listing format (permissions, owner, size, date)              | Quickly check file ownership and timestamps of logs/configs     |
| `-a`        | `ls -a`         | Show hidden files (those starting with `.`)                       | Find hidden config files or environment settings                |
| `-h`        | `ls -lh`        | Display file sizes in human-readable format (KB, MB, etc.)        | Rapidly spot large files during incident triage                 |
| `-t`        | `ls -lt`        | Sort by modification time, descending (newest first)              | Identify recently updated logs or configs for troubleshooting    |
| `-r`        | `ls -lr`        | Reverse the sorting order                                         | Useful to invert default listing logic, e.g. oldest first        |

**Tiered Examples:**

* 🟢 **Beginner Example:**
```bash
# Example: Basic directory listing
$ ls
Documents  Downloads  notes.txt
```
*Explanation*: Shows the items in your current directory at a glance.

* 🟡 **Intermediate Example:**
```bash
# Example: Checking logs sorted by last modification time
$ ls -lt /var/log
-rw-r--r-- 1 root root   10240 Mar 29 10:15 syslog
-rw-r--r-- 1 root root   24576 Mar 29 09:59 auth.log
...
```
*Explicit context*: Helps you identify which log file was updated most recently (important in diagnosing live issues).

* 🔴 **SRE-Level Example:**
```bash
# Example: Finding large or hidden files quickly
$ cd /var/log
$ ls -lha
drwxr-xr-x  2 root root 4.0K Mar 29 10:20 .
drwxr-xr-x 12 root root 4.0K Mar 29 08:00 ..
-rw-r--r--  1 root root 100M Mar 29 10:15 syslog
-rw-r--r--  1 root root  24K Mar 29 09:59 auth.log
-rw-r--r--  1 root root  512 Mar 29 09:15 .secret_log
```
*Explicit context*: Quickly see file sizes (e.g., `100M` indicates `syslog` might be growing too large).

**Instructional Notes:**

* 🧠 **Beginner Tip:** Combine flags like `-lh` to see both details and human-readable sizes.  
* 🧠 **Beginner Tip:** Use tab completion to avoid typing long directory names.

* 🔧 **SRE Insight:** Sorting by timestamp (`-t`) is extremely helpful when investigating real-time issues—check which files updated just before an incident.  
* 🔧 **SRE Insight:** Filter output with `grep` (e.g., `ls -l | grep error`) to zero in on suspicious filenames.

* ⚠️ **Common Pitfall:** Forgetting `-a` can hide critical “dotfiles” used for configurations.  
* ⚠️ **Common Pitfall:** Using `ls` in massive directories can create very long outputs—consider piping to `less` or `head`.

* 🚨 **Security Note:** Hidden files sometimes contain sensitive info (e.g., credentials). Avoid exposing them inadvertently.  
* 💡 **Performance Impact:** `ls` is usually light, but listing extremely large directories can spike I/O usage.

---

### **Command: cd (Change Directory)**

**Command Overview:**  
`cd` moves you between directories. It’s fundamental for day-to-day tasks and absolutely essential when responding to issues in disparate locations.

**Syntax & Flags:**

| Flag/Option | Syntax Example     | Description                                    | SRE Usage Context                                  |
|-------------|--------------------|------------------------------------------------|----------------------------------------------------|
| *(none)*    | `cd /var/log`     | Changes directory to `/var/log`               | Jump to critical log location quickly              |
| `-`         | `cd -`            | Returns you to the last directory visited      | Toggles between two critical directories (e.g. `/etc` ↔ `/var/log`) |
| `~`         | `cd ~`            | Moves you to your home directory               | Return to your personal workspace for quick tasks  |

**Tiered Examples:**

* 🟢 **Beginner Example:**
```bash
# Example: Moving into Documents folder
$ cd Documents
$ pwd
/home/student/Documents
```
*Explanation*: Confirms you have changed into the `Documents` directory.

* 🟡 **Intermediate Example:**
```bash
# Example: Jumping to /var/log from home, then returning
$ cd /var/log
$ cd -
/home/student
```
*Explicit context*: Quickly toggling between logs and your home directory to reference scripts or notes.

* 🔴 **SRE-Level Example:**
```bash
# Example: Navigating across multiple directories in a script
$ cat deploy.sh
#!/bin/bash
cd /var/www/production || exit 1
git pull origin main
cd static
./build_assets.sh
cd -
systemctl restart myapp
```
*Explicit context*: An SRE deployment script automatically navigates to the correct folders, builds assets, and returns to a previous location.

**Instructional Notes:**

* 🧠 **Beginner Tip:** Use `cd ..` to go one directory “up.”  
* 🧠 **Beginner Tip:** Typing `cd` alone (or `cd ~`) always brings you back to your home directory.

* 🔧 **SRE Insight:** If `cd` fails (e.g., “No such file or directory”), add error-handling in scripts to avoid partial deployments.  
* 🔧 **SRE Insight:** Combining `cd` with environment variables (like `$HOME` or `$APP_DIR`) keeps scripts flexible across servers.

* ⚠️ **Common Pitfall:** Typo in the path can waste time or cause script failures.  
* ⚠️ **Common Pitfall:** Using relative paths incorrectly in automation can lead to unintentional file overwrites in the wrong folder.

* 🚨 **Security Note:** Be mindful if you `cd` into directories with restricted permissions—verify who has access.  
* 💡 **Performance Impact:** `cd` itself is trivial on system resources, but the actions you take afterward can have significant effects.

---

### **Command: man (Manual Pages)**

**Command Overview:**  
`man` displays the manual (documentation) for other commands. It’s often your first stop for understanding how a command works and what flags it accepts.

**Syntax & Flags:**

| Flag/Option | Syntax Example    | Description                                         | SRE Usage Context                                  |
|-------------|-------------------|-----------------------------------------------------|----------------------------------------------------|
| *(none)*    | `man ls`         | Opens the man page for `ls`                         | Quick reference for available flags                |
| `-k`        | `man -k "search"` | Searches the man page descriptions for a keyword    | Discover relevant commands or subcommands          |
| `-f`        | `man -f ls`      | Tells you which man page section a command is in    | Clarify commands with multiple man pages (e.g., `printf` in shell vs C library) |

**Tiered Examples:**

* 🟢 **Beginner Example:**
```bash
# Example: Checking manual for pwd
$ man pwd
```
*Explanation*: Opens the full documentation for `pwd`.

* 🟡 **Intermediate Example:**
```bash
# Example: Searching for commands related to "disk"
$ man -k disk
disk_free (1)      - estimate file space usage
diskpart (8)       - partition a hard disk
...
```
*Explicit context*: Helps you discover tools you might not know exist.

* 🔴 **SRE-Level Example:**
```bash
# Example: Investigating advanced usage of systemd
$ man systemd.unit
```
*Explicit context*: SREs often deep-dive into man pages for service management and advanced daemon configurations.

**Instructional Notes:**

* 🧠 **Beginner Tip:** Press **`q`** to quit the manual page. Use arrow keys or **Page Up/Page Down** to scroll.  
* 🧠 **Beginner Tip:** Not all commands have man pages; try `[command] --help` if `man` returns “No manual entry.”

* 🔧 **SRE Insight:** In downtime situations, referencing man pages ensures exact syntax usage under pressure.  
* 🔧 **SRE Insight:** Pair `man -k` with domain-specific keywords to find lesser-known tools that can assist in complex troubleshooting.

* ⚠️ **Common Pitfall:** Reading half the page and missing a crucial flag. Always check the “EXAMPLES” or “NOTES” sections for real-world usage.  
* ⚠️ **Common Pitfall:** Over-reliance on partial knowledge when a thorough read might reveal more efficient solutions.

* 🚨 **Security Note:** Some man pages discuss security-related flags or best practices. Make sure to follow those recommendations in production.  
* 💡 **Performance Impact:** Running `man` has negligible impact on system performance.

---

### **Concept: Filesystem Structure**

**Command/Concept Overview:**  
While not a single executable command, understanding the **filesystem hierarchy** is crucial. Directories like `/etc`, `/var/log`, `/home`, and `/usr` each hold specific categories of data and configuration.

**Syntax & Flags:**  
*(Not a command, but these references matter)*

| Location    | Example Path         | Description                               | SRE Usage Context                                              |
|-------------|----------------------|-------------------------------------------|----------------------------------------------------------------|
| `/`         | N/A                  | Root of the filesystem                    | Starting point for absolute paths                              |
| `/etc`      | `/etc/ssh/sshd_config` | Configuration files for system services   | Adjusting service configs; reloading after changes             |
| `/var/log`  | `/var/log/syslog`    | Log storage directory                     | Monitoring, incident analysis                                  |
| `/home`     | `/home/sre`          | User home directories                     | Personal files, development scripts                            |
| `/usr/bin`  | `/usr/bin/python3`   | Common location for user-level binaries   | Executing system-wide tools and software                       |

**Tiered Examples:**

* 🟢 **Beginner Example:**
```bash
# Example: Listing top-level directories from root
$ cd /
$ ls
bin   etc   lib   media  root  srv   usr
boot  home  lib64 mnt    run   sys   var
```
*Explanation*: You see the structure from the root directory.

* 🟡 **Intermediate Example:**
```bash
# Example: Checking contents of /etc to review configuration files
$ ls -l /etc
-rw-r--r-- 1 root root  3028 Jan 10 06:12 ssh_config
drwxr-xr-x 2 root root  4096 Mar  1 07:30 cron.d
...
```
*Explicit context*: Quick scan of config files is typical during a configuration review or pre-deployment check.

* 🔴 **SRE-Level Example:**
```bash
# Example: Searching logs recursively in /var for "ERROR"
$ grep -Ri "ERROR" /var/log/
...
/var/log/syslog:Mar 29 10:59:12 servername app[1234]: ERROR: Database connection failed
...
```
*Explicit context*: SREs frequently grep through large log directories to pinpoint root causes of incidents.

**Instructional Notes:**

* 🧠 **Beginner Tip:** Remember: `/root` is the home directory of the **root user**, not to be confused with `/` (the root of the entire filesystem).  
* 🧠 **Beginner Tip:** Each directory serves a distinct purpose—learn the “common ones” first.

* 🔧 **SRE Insight:** Knowing standard locations prevents “Where is that file?” chaos when time is critical.  
* 🔧 **SRE Insight:** Large log directories (e.g. `/var/log`) can fill up disk—monitor them proactively.

* ⚠️ **Common Pitfall:** Editing files in `/etc` incorrectly can break services or lock you out. Always create backups.  
* ⚠️ **Common Pitfall:** Mistaking relative for absolute paths when scripting can cause modifications in the wrong location.

* 🚨 **Security Note:** Some directories (like `/var/log/audit`) might contain sensitive info. Secure them with strict permissions.  
* 💡 **Performance Impact:** File fragmentation and large directory usage can degrade I/O performance; plan your partition scheme wisely.

---

## 🛠️ System Effects

Understanding how these commands and the filesystem impact your system is vital:

1. **Filesystem & Metadata**:  
   - `pwd`, `ls`, and `cd` primarily read metadata (like directory structure). They don’t inherently modify data but can lead you to places where you perform writes or changes.

2. **System Resources**:  
   - These commands are typically low-cost on CPU/memory, but listing huge directories can increase I/O. 
   - Grepping through many files can consume CPU and disk bandwidth.

3. **Security Implications**:  
   - Accessing or listing directories with sensitive files (config, keys) must be done under the correct permissions.  
   - Always verify you’re in a safe directory before performing elevated operations.

4. **Monitoring Visibility**:  
   - Navigation commands themselves typically won’t appear in logs unless auditing is enabled.  
   - Familiarity with `/var/log` is crucial for analyzing system events in real time.

---

## 🎯 Hands-On Exercises

### 🟢 Beginner Exercises (Tier 1)

1. **Basic Navigation**  
   - Task: Open a terminal, run `pwd`, then `ls`. Write down the contents of your current directory.  
   - Goal: Recognize your starting directory and see files/folders at a glance.

2. **Moving to a Subdirectory**  
   - Task: Create a folder named `practice` in your home directory (`mkdir practice`), then `cd` into it.  
   - Goal: Understand creating and accessing subdirectories.

3. **Checking Manual Pages**  
   - Task: Run `man pwd`. Scroll through it, then exit with `q`.  
   - Goal: Familiarize yourself with reading official documentation.

### 🟡 Intermediate Exercises (Tier 2)

1. **Detailed Listing & Sorting**  
   - Task: Navigate to `/var/log`, run `ls -lt` to sort files by last modification. Identify which file was updated most recently.  
   - Goal: Connect file timestamps to system events.

2. **Hidden Files Exploration**  
   - Task: In your home directory, run `ls -a` to see hidden files. Inspect one hidden file’s contents with `cat` or `less`.  
   - Goal: Understand what “dotfiles” can store (configurations, environment variables, etc.).

3. **Filesystem Review**  
   - Task: Explore `/etc` with `ls /etc`. Locate a familiar config file (e.g., `sshd_config`) and note its permissions using `ls -l`.  
   - Goal: Relate real config files to the system’s operational state.

### 🔴 SRE-Level Exercises (Tier 3)

1. **Deployment Directory Check**  
   - Task: Write a small script that checks if you are in `/var/www/production` before pulling new code from Git. If not, echo a warning.  
   - Goal: Automate a safety check to prevent deployments in the wrong directory.

2. **Log Analysis Quick Scan**  
   - Task: Use `cd` to move to `/var/log`, then combine `ls -lh` with `grep` to locate large log files containing “ERROR”.  
   - Goal: Practice combining fundamental commands for real troubleshooting.

3. **Multi-Directory Scripting**  
   - Task: Create a script that navigates between `/etc` and `/var/log`, checks a config file, restarts a service (`systemctl restart something`), and verifies logs updated.  
   - Goal: Perform an end-to-end mini-incident resolution workflow.

---

## 📝 Quiz Questions

### 🟢 Beginner (Tier 1)
1. Which command shows your current working directory?  
   A. `pwd`  
   B. `ls`  
   C. `cd`  

2. How do you list **all** files, including hidden ones?  
   A. `ls -h`  
   B. `ls -l`  
   C. `ls -a`  

3. Which directory is considered the top-level (root) of the Linux filesystem?  
   A. `/home`  
   B. `/`  
   C. `/root`  

---

### 🟡 Intermediate (Tier 2)
4. To **reverse** the order of a long listing, you would use:  
   A. `ls -lr`  
   B. `ls -ar`  
   C. `ls -ra`  

5. What does `pwd -P` provide that `pwd` alone might not?  
   A. Physical path without following symlinks  
   B. Permission details of the current directory  
   C. Printing all files in the directory  

6. In which directory would you typically expect to find **system configuration** files?  
   A. `/usr/bin`  
   B. `/tmp`  
   C. `/etc`  

---

### 🔴 SRE-Level (Tier 3)
7. During an outage, you need to find logs mentioning “timeout.” What combination of commands might you use?  
   A. `cd /etc && man logs`  
   B. `pwd -P /var/log && ls -l`  
   C. `cd /var/log && ls -lt | grep "timeout"` or `grep -Ri "timeout" /var/log`  

8. Why might an SRE use `ls -lt` in the `/var/log` directory when troubleshooting?  
   A. To see the largest files first  
   B. To identify which logs changed most recently  
   C. To hide any files from non-root users  

9. When writing a script that deploys code, what is an essential check before performing destructive actions?  
   A. Confirm the user has run `pwd` in the past hour  
   B. Verify you’re in the correct directory using `pwd -P`  
   C. Always run `ls -a` to check for hidden files  

*(Answer key provided separately to instructors.)*

---

## 🚧 Troubleshooting Scenarios

Below are **three** realistic scenarios, each with symptoms, potential causes, diagnostics, resolutions, and prevention tips:

1. **Scenario: Permission Denied in `/var/log`**  
   - **Symptom**: `cd /var/log/app` → “Permission denied.”  
   - **Possible Cause**: File permissions do not allow your user or group access.  
   - **Diagnostic**: `ls -ld /var/log/app` to check permissions.  
   - **Resolution**: If appropriate, run `sudo chown -R sre:sre /var/log/app` or adjust permissions with `chmod`.  
   - **Prevention**: Standardize permission settings via configuration management (e.g., Ansible, Puppet).

2. **Scenario: Confusion with Symlinks**  
   - **Symptom**: Scripts referencing `/var/www/live` fail, but referencing `/var/www/production` works.  
   - **Possible Cause**: `/var/www/live` is a symlink that got broken or pointed to the wrong location.  
   - **Diagnostic**: Use `pwd -P` after `cd /var/www/live` to see where it physically leads.  
   - **Resolution**: Correct or re-create the symlink: `ln -s /var/www/production /var/www/live`.  
   - **Prevention**: Keep documentation of symlinks and ensure scripts use consistent paths.

3. **Scenario: Logs Not Updating**  
   - **Symptom**: `ls -lt /var/log` shows no recent log file changes, but the application is still running.  
   - **Possible Cause**: Application logging level changed or logs redirected to a different path.  
   - **Diagnostic**: Check application configs in `/etc` or environment variables. Look for changes in logging drivers.  
   - **Resolution**: Update config to write logs to the correct location, or revert the logging change.  
   - **Prevention**: Maintain version control for config files and log changes systematically.

---

## ❓ FAQ

### 🟢 Beginner (Tier 1)
1. **Q**: Why is Linux often preferred over other operating systems for servers?  
   **A**: Linux offers stability, security, and transparency (open-source), making it reliable for server environments.

2. **Q**: What’s the easiest way to go “up one level” in the filesystem?  
   **A**: Use `cd ..` to move to the parent directory.

3. **Q**: I ran `man` and got “No manual entry found.” Now what?  
   **A**: Some commands don’t have a man page installed. Try `<command> --help` or install extra documentation packages.

---

### 🟡 Intermediate (Tier 2)
1. **Q**: How can I see hidden files and directories by default without always typing `ls -a`?  
   **A**: Many shells let you configure an alias, e.g., `alias ls='ls -a --color=auto'`. Adjust to your preference in `~/.bashrc` or `~/.zshrc`.

2. **Q**: If I’m in `/var/log`, why does `pwd` show `/var/log/` sometimes but `/var/log` other times (with no trailing slash)?  
   **A**: Paths can appear slightly different depending on how they were traversed (e.g., symlinks, trailing slash usage). Functionally, both are the same directory.

3. **Q**: Should I worry if I see many `.something` files in my home directory?  
   **A**: Hidden “dotfiles” are normal for storing app settings. It’s only a concern if they contain sensitive data in plain text or if they clutter your environment.

---

### 🔴 SRE-Level (Tier 3)
1. **Q**: How do I quickly navigate to multiple directories in a single command?  
   **A**: You can chain `cd` commands with `&&`. For example: `cd /etc && ls && cd /var/log && ls`. This only proceeds if each step succeeds.

2. **Q**: What if my script needs to confirm the absolute path on different distributions (e.g., Ubuntu vs. CentOS)?  
   **A**: Use `pwd -P` inside the script or rely on environment variables that store distribution-specific paths. Incorporate conditional logic if necessary.

3. **Q**: Can changes in `/etc/fstab` or `/etc/mtab` affect my ability to `cd` somewhere?  
   **A**: Yes. If a filesystem isn’t mounted or is mounted incorrectly, directories in that path might be inaccessible. Always validate mount points and permissions when investigating “cd” failures.

---

## 🔥 SRE Scenario

**Incident**: A production web server suddenly becomes unresponsive. You suspect high disk usage in `/var/log` is causing partial system lock-up.

**Steps (5–7) with Reasoning**:

1. **Verify Current Directory**  
   ```bash
   pwd
   ```
   *Reasoning*: Confirm you aren’t already in `/var/log` from a previous session. Avoid confusion with multiple SSH windows.

2. **Navigate to Logs**  
   ```bash
   cd /var/log
   ```
   *Reasoning*: This directory typically contains system and application logs crucial to diagnosing disk usage issues.

3. **Check File Sizes**  
   ```bash
   ls -lh
   ```
   *Reasoning*: Identify any unusually large files. Big logs can fill up storage quickly and degrade server performance.

4. **Investigate Most Recently Modified**  
   ```bash
   ls -lt
   ```
   *Reasoning*: See which logs are actively growing. If one is updated excessively, it may be the culprit.

5. **Grep for Error Patterns**  
   ```bash
   grep -Ri "error" .
   ```
   *Reasoning*: Quickly find lines containing “error” across all log files in the current directory.

6. **Clean or Archive Log**  
   ```bash
   # Example approach if disk is 100% full:
   echo "" > large_log_file.log
   # Or move it:
   mv large_log_file.log /tmp/large_log_file_backup_$(date +%F)
   ```
   *Reasoning*: Prevent immediate disk exhaustion. For deeper analysis, move logs or compress them.

7. **Recheck Available Disk Space**  
   ```bash
   df -h
   ```
   *Reasoning*: Confirm that clearing or archiving logs freed up space and restored normal operations.

**Connection to SRE Principles**: Quick identification and mitigation of resource-based outages, while preserving logs for root cause analysis.

---

## 🧠 Key Takeaways

1. **Command Summary (min 5)**  
   - **pwd**: Verify current directory; crucial before performing critical changes.  
   - **ls**: Inspect directory contents; sort by modification time to see updates.  
   - **cd**: Navigate efficiently across the filesystem.  
   - **man**: Access official documentation quickly.  
   - **Filesystem**: Rooted at `/` with directories like `/etc`, `/var/log`, `/home`, each serving a unique purpose.

2. **Operational Insights (min 3)**  
   - Always confirm your directory (`pwd`) in production scripts to avoid destructive mistakes.  
   - Sorting logs by modification time is invaluable for real-time troubleshooting.  
   - A well-understood filesystem hierarchy accelerates incident response and reduces confusion under pressure.

3. **Best Practices (min 3)**  
   - Keep your environment well-organized: use consistent naming, avoid random symlinks.  
   - Check `man` pages (or `--help`) for exact flags to ensure correct syntax in mission-critical tasks.  
   - Monitor `/var/log` usage to prevent disk fill-ups that can bring down services.

4. **Preview of Next Topic**  
   - **Day 2**: We’ll expand into file manipulation (creating, moving, deleting, examining content), and how SREs automate these tasks. Expect more hands-on scenarios and advanced command usage (like `grep`, `tail`, `chmod`, etc.) to build on today’s solid foundation.

---

## 📚 Further Learning Resources

### 🟢 Beginner (2–3)

1. **“Linux Journey: Command Line Basics”**  
   - Link: [https://linuxjourney.com/lesson/the-shell](https://linuxjourney.com/lesson/the-shell)  
   - Teaches fundamentals of the command line with friendly visuals.  
   - Perfect for new users wanting a step-by-step introduction.

2. **“The Linux Command Line” (William Shotts)**  
   - Link: [http://linuxcommand.org/tlcl.php](http://linuxcommand.org/tlcl.php)  
   - Comprehensive free ebook guiding you through basic to intermediate shell usage.  
   - Helps beginners build confidence in daily CLI tasks.

### 🟡 Intermediate (2–3)

1. **“Linux File System Hierarchy”**  
   - Link: [https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html)  
   - Detailed description of standard directories and their purposes.  
   - Aids in better operational awareness and navigational efficiency.

2. **“ExplainShell”**  
   - Link: [https://explainshell.com/](https://explainshell.com/)  
   - Breaks down shell commands and flags from man pages.  
   - Perfect for quickly clarifying complex command usage in your daily workflow.

### 🔴 SRE-Level (2–3)

1. **“Google SRE Book – Chapter: Handling Emergencies”**  
   - Link: [https://sre.google/sre-book/](https://sre.google/sre-book/)  
   - Delivers deep insights into incident response and reliability best practices.  
   - Elevates your perspective on how basic Linux commands integrate with large-scale reliability strategies.

2. **“Advanced Bash-Scripting Guide”**  
   - Link: [http://tldp.org/LDP/abs/html/](http://tldp.org/LDP/abs/html/)  
   - Provides in-depth coverage of bash scripting for automation.  
   - Essential for SREs to streamline operational tasks, from deployments to monitoring checks.

3. **“Linux Performance Optimization”**  
   - Link: [https://www.brendangregg.com/linuxperf.html](https://www.brendangregg.com/linuxperf.html)  
   - Discusses tools & techniques for analyzing and improving Linux performance.  
   - Critical for advanced SREs to maintain high availability under production load.

---

**Congratulations on completing Day 1!** You’ve covered the fundamental commands and filesystem structure essential to every Linux SRE. Tomorrow, we’ll build on these skills with **file manipulation, permissions, and deeper troubleshooting** techniques to strengthen your reliability engineering capabilities.