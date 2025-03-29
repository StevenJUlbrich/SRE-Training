# Day 2 Training

## 📌 Introduction (Explicitly Merged and Enhanced)

### 🔄 **Explicit Recap of Day 1:**

Yesterday, you explicitly mastered foundational Linux navigation commands (`pwd`, `ls`, `cd`), documentation access methods (`man`, `--help`, `info`), and gained insight into the Linux Filesystem Hierarchy Standard (FHS). These skills explicitly enable efficient navigation, resource identification, and confident interaction with Linux systems.

### 📅 **Today's Explicit Topics and Importance:**

Today, your explicit focus shifts to essential **file manipulation operations**—creating, viewing, copying, moving, and deleting files and directories. As an SRE, proficiency in these operations is explicitly crucial for tasks such as:

- Creating and modifying configuration files explicitly for system setup.
- Efficiently viewing and analyzing log files during incidents.
- Explicitly backing up files prior to system or configuration changes.
- Effectively managing disk space by explicit cleanup of temporary or unnecessary files.

Explicitly mastering these skills ensures quick resolution during incidents, efficient system management, and organized infrastructure.

### 🎯 **Explicit Learning Objectives:**

By the explicit end of today's module, you'll be able to:

- 🟢 **Beginner:**  
  - Explicitly create and organize files and directories (`touch`, `mkdir`).  
  - Explicitly view file contents clearly (`cat`, `less`, `head`, `tail`, `more`).

- 🟡 **Intermediate:**  
  - Explicitly copy, move, and rename files and directories (`cp`, `mv`).  
  - Explicitly delete files and directories with safety considerations (`rm`, `rmdir`).

- 🔴 **SRE-Level:**  
  - Explicitly apply file operation skills effectively in realistic SRE scenarios, including incident response, log management, and system configuration.

---

## 📚 Core Concepts Explained

### **Explicit Concept 1: "Everything is a File" Philosophy**

- 🟢 **Beginner Analogy:**  
  Imagine Linux explicitly as a virtual filing cabinet. Each file and directory is like a document or folder explicitly stored neatly, accessible for you to organize, move, copy, or delete.

- 🟡 **Intermediate Technical Explanation:**  
  Linux explicitly treats virtually every system resource (files, directories, devices, network sockets, processes) as a file. This unified file-based model explicitly simplifies resource management and interaction within the operating system.

- 🔴 **Advanced SRE Operational Insights:**  
  For an SRE, this explicit philosophy facilitates consistent interactions with diverse system resources. Explicitly managing configurations, devices, logs, and processes through common file-based operations simplifies automation, scripting, and troubleshooting across different infrastructure components.

### **Explicit Concept 2: File Manipulation in SRE Work**

- 🟢 **Beginner Analogy:**  
  File manipulation is explicitly similar to organizing papers in your workspace—creating, copying, renaming, moving, or discarding documents to maintain clarity and efficiency.

- 🟡 **Intermediate Technical Explanation:**  
  File operations (`touch`, `mkdir`, `cp`, `mv`, `rm`) explicitly form the foundational tools for daily system management tasks like configuration changes, log analysis, backups, and housekeeping tasks that ensure system reliability and organization.

- 🔴 **Advanced SRE Operational Insights:**  
  Explicit mastery of file operations significantly reduces Mean Time To Repair (MTTR) during incidents. For instance, explicitly viewing the correct logs promptly during an outage directly impacts your ability to diagnose and resolve issues efficiently.

---
Great! Next, I'll explicitly proceed by generating the **💻 Detailed Command Breakdown** and **🛠️ Filesystem & System Effects** sections in this batch. Upon your explicit confirmation, we'll continue with subsequent sections.

---

# 💻 Detailed Command Breakdown (Day 2)

---

## ✅ **Creating Files and Directories**

### **Command: `touch` (Create Empty Files or Update Timestamps)**

#### **Command Overview:**

Explicitly creates new empty files or updates existing file timestamps, useful for log files and placeholders.

#### **Syntax & Flags:**

| Flag/Option | Syntax Example   | Explicit Description                  |
|-------------|------------------|---------------------------------------|
| *(no flag)* | `touch file.txt` | Explicitly creates a new empty file.  |
| `-a`        | `touch -a file`  | Explicitly updates only access time.  |
| `-m`        | `touch -m file`  | Explicitly updates only modification time.|

#### **Explicit Examples:**

- 🟢 Beginner:

```bash
# Explicitly create a new file
touch newlog.txt
```

- 🟡 Intermediate:

```bash
# Explicitly update modification timestamp explicitly for log rotation
touch -m app.log
```

- 🔴 SRE-Level:

```bash
# Explicitly create multiple placeholder files for automation scripts
touch deploy_{frontend,backend,db}.log
```

#### **Instructional Notes:**

- 🧠 **Beginner Tip:** Explicitly use `touch` to quickly create empty placeholder files.
- 🔧 **SRE Insight:** Explicitly updating file timestamps helps manage log rotation and archival automation.
- ⚠️ **Common Pitfall:** Explicitly forgetting that `touch` overwrites timestamps may lead to unintended consequences.

---

### **Command: `mkdir` (Create Directories)**

#### **Command Overview:**

Explicitly creates directories to organize files effectively.

#### **Syntax & Flags:**

| Flag/Option | Syntax Example           | Explicit Description                 |
|-------------|--------------------------|--------------------------------------|
| `-p`        | `mkdir -p dir/subdir`    | Explicitly creates nested directories.|
| `-m`        | `mkdir -m 700 dirname`   | Explicitly sets specific permissions.|

#### **Explicit Examples:**

- 🟢 Beginner:

```bash
# Explicitly create a single directory
mkdir logs
```

- 🟡 Intermediate:

```bash
# Explicitly create nested directories explicitly for application logs
mkdir -p /var/log/myapp/{info,error,debug}
```

- 🔴 SRE-Level:

```bash
# Explicitly create secure directories with restricted permissions explicitly for sensitive data
mkdir -m 700 -p /secure_data/backups
```

#### **Instructional Notes:**

- 🧠 **Beginner Tip:** Explicitly use `-p` to avoid errors when creating nested directories.
- 🔧 **SRE Insight:** Explicitly setting permissions at creation enhances security explicitly for critical directories.
- ⚠️ **Common Pitfall:** Explicitly creating directories without permission consideration might expose sensitive data.

---

## ✅ **Viewing File Contents**

### **Commands: `cat`, `less`, `head`, `tail`, `more`**

#### **Command Overview:**

Explicitly view file contents efficiently for analysis and troubleshooting.

#### **Syntax & Flags:**

| Command | Flag | Syntax Example          | Explicit Description                                 |
|---------|------|-------------------------|------------------------------------------------------|
| `cat`   | `-n` | `cat -n file`           | Explicitly displays contents with line numbers.      |
| `less`  | `-N` | `less -N file`          | Explicitly views files interactively with line numbers.|
| `head`  | `-n` | `head -n 10 file`       | Explicitly views the first N lines of a file.        |
| `tail`  | `-f` | `tail -f file`          | Explicitly follows file output in real-time.         |
| `more`  | N/A  | `more file`             | Explicitly paginated viewing of file contents.       |

#### **Explicit Examples:**

- 🟢 Beginner:

```bash
# Explicitly view entire file
cat config.txt
```

- 🟡 Intermediate:

```bash
# Explicitly view log file interactively during troubleshooting
less -N /var/log/messages
```

- 🔴 SRE-Level:

```bash
# Explicitly monitor logs in real-time explicitly during live incident
tail -f /var/log/nginx/error.log
```

#### **Instructional Notes:**

- 🧠 **Beginner Tip:** Explicitly prefer `less` over `more` explicitly for better navigation.
- 🔧 **SRE Insight:** Explicitly use `tail -f` for real-time log monitoring explicitly during incidents.
- ⚠️ **Common Pitfall:** Explicitly using `cat` for large files can flood your terminal.

---

## ✅ **Copying, Moving, and Deleting Files and Directories**

### **Commands: `cp`, `mv`, `rm`, `rmdir`**

#### **Command Overview:**

Explicitly duplicate, relocate, rename, or delete files and directories.

#### **Syntax & Flags:**

| Command | Flag | Syntax Example            | Explicit Description                                |
|---------|------|---------------------------|-----------------------------------------------------|
| `cp`    | `-a` | `cp -a src dest`          | Explicitly archives files/directories (preserving permissions, timestamps). |
| `mv`    | `-i` | `mv -i old new`           | Explicitly interactive move/rename prompting.      |
| `rm`    | `-r` | `rm -r dir`               | Explicitly recursively deletes directories.        |
| `rmdir` | `-p` | `rmdir -p dir/subdir`     | Explicitly removes empty nested directories.       |

#### **Explicit Examples:**

- 🟢 Beginner:

```bash
# Explicitly copy file safely
cp config.txt config_backup.txt
```

- 🟡 Intermediate:

```bash
# Explicitly rename a configuration file explicitly prompting before overwriting
mv -i old.conf new.conf
```

- 🔴 SRE-Level:

```bash
# Explicitly remove a failed deployment explicitly with caution
rm -ri /var/www/bad_deploy
```

#### **Instructional Notes:**

- 🧠 **Beginner Tip:** Explicitly always back up files explicitly before deletion.
- 🔧 **SRE Insight:** Explicitly automate critical file backups using `cp -a`.
- ⚠️ **Common Pitfall:** Explicitly using `rm -rf` without caution can lead to catastrophic data loss.

---

# 🛠️ Filesystem & System Effects

Explicitly detailed practical impacts of today's commands on your filesystem and operations.

### Explicit Effects Summary

- `touch` and `mkdir`: Explicitly alter metadata (timestamps, permissions).
- Viewing commands (`cat`, `less`, `head`, `tail`, `more`): Explicitly update file access metadata (`atime`).
- Copying (`cp`) and moving (`mv`): Explicitly duplicate or alter files/directories and metadata explicitly.
- Deletion (`rm`, `rmdir`): Explicitly permanently remove files/directories; metadata is lost explicitly.

### ⚠️ Explicit Misuse Cases and Preventive Measures

- Explicit misuse of deletion commands (`rm -rf`) can explicitly cause data loss; always confirm explicitly before execution.
- Explicitly using `cat` on large files can disrupt terminal operations; explicitly use paginated viewers (`less`).

---
Great! I'll explicitly proceed to the next batch of sections:

- 🎯 **Hands-On Exercises**
- 📝 **Quiz Questions**
- 🚧 **Common Issues and Troubleshooting**

Upon your explicit confirmation, we will then proceed with the remaining sections.

---

# 🎯 Hands-On Exercises (Day 2)

Explicitly structured exercises explicitly reinforcing today’s learning objectives.

## 🟢 Beginner Exercises

**Exercise 1: Creating Files and Directories**

- Explicitly create a directory named `practice`.
- Inside, explicitly create files `test1.txt` and `test2.log`.
- Explicitly confirm creation with `ls`.

**Reflection:** Explicitly reflect on how organized directory structures support efficient workflow.

---

**Exercise 2: Viewing File Contents**

- Explicitly write text to `test1.txt` using:

```bash
echo "Hello Linux!" > test1.txt
```

- Explicitly view the content with `cat`.
- Use `head` and `tail` to explicitly examine the file.

**Reflection:** Explicitly consider how different viewing commands offer flexibility for examining file contents.

---

## 🟡 Intermediate Exercises

**Exercise 1: Copying and Moving Files**

- Explicitly create a backup of `test1.txt` named `test1.bak`.
- Explicitly move `test2.log` into a new subdirectory named `logs`.
- Explicitly confirm operations with `ls -l`.

**Reflection:** Explicitly reflect on the importance of backups in routine operations.

---

**Exercise 2: Safe Deletion**

- Explicitly attempt to delete `test1.bak` interactively using `rm -i`.
- Explicitly confirm deletion choice when prompted.

**Reflection:** Explicitly consider the impact of cautious deletion practices in maintaining data integrity.

---

## 🔴 SRE-Level Exercises

**Exercise 1: Incident Simulation – Log Management**

- Explicitly create directories `/tmp/logs/{old,new}`.
- Explicitly simulate log rotation by moving older logs to `/tmp/logs/old` explicitly.
- Explicitly confirm file movements with `ls`.

**Reflection:** Explicitly discuss how structured log management supports incident response efficiency.

---

**Exercise 2: Archiving Configuration Files**

- Explicitly archive existing files in `/tmp/logs/old` using `cp -a` explicitly to a backup location (`/tmp/backup_logs`).
- Explicitly verify the permissions and timestamps preservation explicitly.

**Reflection:** Explicitly reflect on why preserving file metadata explicitly matters in backups.

---

# 📝 Quiz Questions (Day 2)

Explicitly structured to reinforce today's key Linux commands and operational concepts.

---

## 🟢 Beginner Tier (3 Questions)

**1. Multiple-choice:**  
Which command explicitly creates nested directories such as `app/logs/errors`?

- a) `mkdir -r app/logs/errors`
- b) `mkdir -f app/logs/errors`
- c) `mkdir -p app/logs/errors`
- d) `mkdir -n app/logs/errors`

**2. Fill-in-the-blank:**  
To explicitly view only the first 20 lines of a file, the command is `head ___ 20 file.txt`.

**3. Multiple-choice:**  
Explicitly, which command removes an empty directory named `oldlogs`?

- a) `rm oldlogs`
- b) `rm -r oldlogs`
- c) `rmdir oldlogs`
- d) `remove oldlogs`

---

## 🟡 Intermediate Tier (4 Questions)

**1. Scenario-based:**  
You explicitly want to copy `config.conf` to `backup.conf`, explicitly preserving permissions and timestamps. Which explicit command achieves this?

- a) `cp config.conf backup.conf`
- b) `cp -p config.conf backup.conf`
- c) `cp -a config.conf backup.conf`
- d) `cp -r config.conf backup.conf`

**2. Multiple-choice:**  
Explicitly, which command continuously displays new log entries in real-time?

- a) `tail /var/log/app.log`
- b) `cat -f /var/log/app.log`
- c) `less +F /var/log/app.log`
- d) `tail -f /var/log/app.log`

**3. Fill-in-the-blank:**  
To explicitly rename a file from `error.log` to `error_old.log`, you explicitly use the command: `mv _____ _____`.

**4. Scenario-based:**  
Explicitly, you accidentally deleted a critical file. What explicit preventive measure could have avoided this?

- a) Using `rm -f`
- b) Using `rm -r`
- c) Using `rm -i`
- d) Using `mv` to a backup directory instead of deletion

---

## 🔴 SRE-Level Tier (4 Questions)

**1. Scenario-based:**  
Explicitly during an incident, you need real-time monitoring of an application log file explicitly to detect errors instantly. Which explicit command is best suited?

- a) `cat /var/log/application.log`
- b) `less /var/log/application.log`
- c) `tail -f /var/log/application.log`
- d) `head -n 20 /var/log/application.log`

**2. Fill-in-the-blank:**  
Explicitly removing directories containing files requires the command: `rm ____ directoryname`.

**3. Multiple-choice:**  
Explicitly, to securely delete multiple files interactively, which explicit command would you use?

- a) `rm -f file*`
- b) `rm -r file*`
- c) `rm -i file*`
- d) `rmdir file*`

**4. Scenario-based:**  
Explicitly, you must create multiple empty log files (`app.log`, `db.log`, `web.log`) explicitly in a single command. What explicit command do you run?

- a) `touch app.log && touch db.log && touch web.log`
- b) `touch {app,db,web}.log`
- c) `mkdir app.log db.log web.log`
- d) `cp /dev/null app.log db.log web.log`

---

### ✅ **Explicit Confirmation**

Please explicitly verify if the updated and expanded **Quiz Questions** explicitly meet the gold-standard benchmark and the explicit requirement of 3–4 questions per tier.  

Upon explicit confirmation, we will proceed to the next sections
---

# 🚧 Common Issues and Troubleshooting

Explicitly detail frequent issues encountered with today's commands, their explicit diagnosis, resolution, and prevention.

## 🔎 Issue 1: Directory Deletion Error (`rmdir`)

**Error:**

```bash
rmdir: failed to remove 'logs': Directory not empty
```

**Diagnosis:**

- Explicitly check directory contents:

```bash
ls logs/
```

**Resolution:**

- Explicitly delete contents or use:

```bash
rm -r logs
```

**Prevention:**

- Explicitly confirm directory emptiness with `ls` before using `rmdir`.

---

## 🔎 Issue 2: Permission Denied (`rm`, `cp`, `mv`)

**Error:**

```bash
rm: cannot remove 'file.txt': Permission denied
```

**Diagnosis:**

- Explicitly check file permissions:

```bash
ls -l file.txt
```

- Explicitly verify your current user permissions:

```bash
id
```

**Resolution:**

- Explicitly use elevated privileges carefully:

```bash
sudo rm file.txt
```

**Prevention:**

- Explicitly ensure proper permissions and ownership explicitly before operations.

---

## 🔎 Issue 3: File Overwrite by Accident (`mv`, `cp`)

**Issue:**

- Accidentally overwriting files explicitly due to lack of prompt.

**Resolution:**

- Explicitly use interactive mode explicitly:

```bash
mv -i file1 file2
```

**Prevention:**

- Explicitly configure shell aliases explicitly to always prompt explicitly for sensitive operations:

```bash
alias mv='mv -i'
alias cp='cp -i'
alias rm='rm -i'
```

---

Great—explicitly understood. Moving forward, I'll explicitly generate the next batch of sections:

- ❓ **FAQ**
- 🔥 **SRE Scenario Walkthrough**

Upon your explicit confirmation, we’ll proceed to complete the final remaining sections.

---

# ❓ FAQ (Day 2)

Explicitly structured FAQs, clearly addressing common practical operational questions per learner tier.

---

## 🟢 Beginner FAQ

### **Q1: What is the explicit difference between `rm` and `rmdir`?**  

**A:** Explicitly, `rm` removes files and directories (when used with `-r`), while `rmdir` only explicitly removes empty directories.

### **Q2: How do I explicitly view large files without cluttering my terminal?**  

**A:** Explicitly use paginated commands like `less file.txt` to explicitly scroll through large files interactively.

### **Q3: Can I recover explicitly deleted files easily?**  

**A:** Explicitly, no. Once deleted explicitly with `rm`, recovery is difficult. Explicitly always double-check before deletion.

---

## 🟡 Intermediate FAQ

### **Q1: Why use `cp -a` instead of just `cp`?**  

**A:** Explicitly, `cp -a` (archive mode) preserves file attributes explicitly, including permissions, timestamps, and ownership—essential explicitly for backups.

### **Q2: How can I explicitly monitor a log file for real-time updates?**  

**A:** Explicitly use `tail -f logfile` or `less +F logfile` explicitly for live log monitoring.

### **Q3: What is the safest explicit way to delete files interactively?**  

**A:** Explicitly use `rm -i file.txt`, which explicitly prompts for confirmation explicitly before each deletion.

---

## 🔴 SRE-Level FAQ

### **Q1: How do SREs explicitly prevent accidental file deletions in production?**  

**A:** Explicitly:

- Always explicitly use interactive deletion (`rm -i`) or explicitly move files to a backup directory explicitly instead of deletion.
- Explicitly configure shell aliases explicitly for safety:

```bash
alias rm='rm -i'
```

### **Q2: What's the explicit best practice for archiving configuration files before critical changes?**  

**A:** Explicitly use timestamped backups explicitly preserving metadata explicitly:

```bash
cp -a config.conf config.conf.bak.$(date +%Y%m%d-%H%M%S)
```

### **Q3: How do I explicitly locate large files consuming disk space quickly?**  

**A:** Explicitly use:

```bash
du -h --max-depth=1 /path | sort -hr
find /path -type f -size +100M -exec ls -lh {} \;
```

---

# 🔥 SRE Scenario Walkthrough (Day 2)

### **Explicit Scenario Description:**

You explicitly receive an alert indicating "Disk Usage Exceeded 90%" explicitly on a critical production server (`prod-db-02`). Your explicit task is to quickly identify and archive large log files explicitly to mitigate the issue immediately.

---

### 🚨 **Incident Response Steps:**

**Step 1: Explicitly connect to the affected server**  

```bash
ssh sre@prod-db-02
```

- **Explicit Rationale:** Rapid connection explicitly to assess the situation.

---

**Step 2: Explicitly identify disk usage explicitly**  

```bash
df -h /
```

- **Explicit Rationale:** Confirm disk utilization explicitly to verify severity.

---

**Step 3: Explicitly locate large files explicitly**  

```bash
du -h --max-depth=1 /var/log | sort -hr | head -5
```

- **Explicit Rationale:** Quickly pinpoint explicitly the largest log directories.

---

**Step 4: Explicitly archive the largest log files explicitly before cleanup**  

```bash
mkdir -p /var/log/archive/$(date +%Y%m%d)
cp -a /var/log/mysql/mysql.log /var/log/archive/$(date +%Y%m%d)/
```

- **Explicit Rationale:** Explicitly safeguard data explicitly by archiving before deleting.

---

**Step 5: Explicitly truncate the archived log file explicitly to reclaim space immediately**  

```bash
> /var/log/mysql/mysql.log
```

- **Explicit Rationale:** Explicitly clears log contents explicitly to quickly recover disk space explicitly without affecting permissions.

---

**Step 6: Explicitly recheck disk usage explicitly after cleanup**  

```bash
df -h /
```

- **Explicit Rationale:** Explicit verification explicitly confirms issue resolution.

---

**Step 7: Explicitly monitor log file growth explicitly in real-time**  

```bash
tail -f /var/log/mysql/mysql.log
```

- **Explicit Rationale:** Explicitly detect potential recurrence immediately explicitly.

---

### 🚩 **Incident Reflection (Explicitly Linking Scenario to Objectives):**

This explicit scenario explicitly highlights the critical nature of today's commands (`cp`, `mkdir`, `du`, `tail`, and log file handling) explicitly in real-time SRE operational contexts. Explicit mastery of these file operations explicitly ensures efficient disk management and rapid incident recovery explicitly in production environments.

---

# 🧠 Key Takeaways (Day 2)

Explicitly summarized below are the critical file manipulation commands, concepts, operational insights, and best practices explicitly emphasized today.

## 📌 **Critical Commands Learned:**

- **File & Directory Creation:**
  - `touch`: Explicitly create new files or explicitly update timestamps.
  - `mkdir`: Explicitly create directories, explicitly using `-p` for nested structures.

- **File Viewing:**
  - `cat`: Explicitly view file contents.
  - `less`/`more`: Explicitly paginate large file viewing interactively.
  - `head`/`tail`: Explicitly view start or end of files, explicitly with real-time log monitoring using `tail -f`.

- **Copying, Moving, Deletion:**
  - `cp`: Explicitly duplicate files/directories, explicitly preserving attributes with `-a`.
  - `mv`: Explicitly relocate/rename files, explicitly using `-i` for safety prompts.
  - `rm`/`rmdir`: Explicitly delete files/directories explicitly with caution (`-i`, `-r`).

---

## ✅ **Operational Best Practices and Insights:**

- Explicitly create timestamped and attribute-preserving backups explicitly before critical file operations.
- Explicitly use real-time log monitoring explicitly (`tail -f`) during incident response.
- Explicitly implement interactive prompts (`rm -i`) explicitly to reduce accidental data loss.
- Explicitly apply structured log management explicitly for efficient disk usage explicitly and incident handling.

---

## ⚠️ **Explicit Preventive Measures Against Common Pitfalls:**

- Explicitly verify files explicitly before deletion to avoid permanent data loss.
- Explicitly avoid using dangerous deletion commands (`rm -rf`) explicitly without caution or confirmation.
- Explicitly prefer interactive deletion (`rm -i`) explicitly and backup (`cp -a`) explicitly as safe operational defaults.

---

## 🚀 **Preview of Next Day's Topic (Day 3):**

Tomorrow explicitly focuses on **file permissions, ownership, and system security**. These concepts explicitly ensure data protection, access control, and secure operations—explicitly critical skills in SRE roles.

---

# 📚 Further Learning Resources (Day 2)

Explicitly structured additional resources for each learner tier explicitly to reinforce and extend today's knowledge:

---

## 🟢 Beginner Resources

- [Linux Journey – File Operations](https://linuxjourney.com/lesson/file-operations)  
  Explicit beginner-friendly tutorials explicitly introducing file handling concepts and commands.

- [Linux Command Line Tutorial](http://linuxcommand.org/lc3_lts0050.php)  
  Explicit clear explanations explicitly focusing on fundamental Linux file management operations.

---

## 🟡 Intermediate Resources

- [Taming the Terminal - File Operations](https://www.bartbusschots.ie/s/2013/05/25/taming-the-terminal-part-6-more-file-operations/)  
  Explicit intermediate-level guidance explicitly on more complex file operations and command options.

- [Linux File and Directory Management (The Linux Foundation)](https://training.linuxfoundation.org/resources/free/linux-tutorials/managing-files-and-directories/)  
  Explicitly covers practical skills explicitly used in professional Linux environments.

---

## 🔴 SRE-Level Resources

- [Google SRE Book – Chapter 13: Data Processing](https://sre.google/sre-book/data-processing/)  
  Explicitly addresses advanced SRE use cases explicitly involving file manipulation, data analysis, and log management.

- [Advanced Linux File Operations and Troubleshooting (Red Hat)](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_file_systems/)  
  Explicitly deepens understanding explicitly around file operations in enterprise Linux environments, explicitly suitable for experienced SREs.
