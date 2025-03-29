# 🚀 Day 6: Processes & System Monitoring – Enhanced SRE-Level Training Module

## 📌 Introduction

### 🔄 Recap of Day 5

Yesterday, you mastered intermediate text processing commands (`sed`, `awk`, `sort`, `uniq`) and powerful pipeline operations essential for effective log and system data analysis.

### 📅 Today's Topics and Importance

Today, we dive into **process management and system monitoring**. These skills are crucial for SREs as they enable proactive system observation, effective resource management, and swift troubleshooting—directly contributing to service reliability.

### 🎯 Learning Objectives

By the end of Day 6, you will:

- 🟢 View and manage basic processes with commands (`ps`, `top`, `htop`)
- 🟡 Control processes using commands like `kill`, `pkill`, `killall`, and manage jobs (`jobs`, `bg`, `fg`, `nohup`)
- 🔴 Diagnose and resolve operational incidents using resource monitoring tools (`free`, `df`, `du`, `iostat`, `lsof`, `uname`)

---

## 📚 Core Concepts Explained

- **Beginner Analogy:** Think of processes like employees in a company, each having specific tasks (running programs) identified by their employee IDs (PIDs).

- **Intermediate Technical Explanation:** Processes are running instances of programs, managed via their PIDs, states, and resources (CPU, memory).

- **Advanced SRE Operational Insights:** Understanding process hierarchies and resource constraints allows SREs to maintain service reliability and rapidly diagnose performance issues.

---

## 💻 Commands to Learn Today (Detailed Command Breakdown)

### 🔍 1. Process Monitoring (`ps`, `top`, `htop`)

#### **Command Overview:**

- `ps`: Displays snapshot of current processes.
- `top`: Provides real-time dynamic view of processes.
- `htop`: User-friendly, enhanced interactive viewer.

#### **Syntax & Flags:**

| Flag/Option | Syntax Example | Explicit Description                             |
| ----------- | -------------- | ------------------------------------------------ |
| `aux`       | `ps aux`       | Lists all processes in detailed format.          |
| `-ef`       | `ps -ef`       | Displays detailed process list with parent PIDs. |
| `-u`        | `top -u user`  | Displays processes for a specific user.          |
| `--forest`  | `ps --forest`  | Shows processes in hierarchical tree format.     |

#### **Explicit Examples:**

- 🟢 **Beginner Examples:**

```bash
# Viewing all current processes in detail
$ ps aux
```

```bash
# Real-time process viewer
$ top
```

- 🟡 **Intermediate Examples:**

```bash
# Viewing process hierarchy
$ ps aux --forest
```

```bash
# Monitoring processes of a specific user
$ top -u username
```

- 🔴 **SRE-Level Examples:**

```bash
# Scenario: Investigating high CPU usage
$ ps aux --sort=-%cpu | head -10
```

```bash
# Scenario: Real-time monitoring with enhanced viewer
$ htop
```

#### **Instructional Notes:**

- 🧠 **Beginner Tip:** Use `top` to quickly identify resource-heavy processes.
- 🔧 **SRE Insight:** Regularly monitoring with `htop` can significantly reduce incident response times.
- ⚠️ **Common Pitfall:** Confusing memory statistics in `top`; always verify with `free`.

### 🛠️ Filesystem & System Effects

- Commands are informational; no filesystem changes.
- Metadata impacts: None.
- Automation impact: Often used within monitoring scripts.
- Misuse case: Overloading system resources by running too many monitoring instances simultaneously; preventive measure: limit instances.

---

### 🛠️ 2. Process Control (`kill`, `pkill`, `killall`)

#### **Command Overview:**

- `kill`: Sends signals to terminate or control processes by PID.
- `pkill`: Terminates processes based on name or pattern matching.
- `killall`: Terminates all processes matching an exact name.

#### **Syntax & Flags:**

| Flag/Option | Syntax Example  | Explicit Description                                |
| ----------- | --------------- | --------------------------------------------------- |
| `-9`        | `kill -9 PID`   | Forces immediate termination (SIGKILL).             |
| `-HUP`      | `kill -HUP PID` | Reloads configuration without stopping the process. |
| `-u`        | `pkill -u user` | Terminates processes belonging to a specific user.  |

#### **Explicit Examples:**

- 🟢 **Beginner Examples:**

```bash
# Gracefully terminate a process with PID 1234
$ kill 1234
```

```bash
# Force terminate a process immediately
$ kill -9 1234
```

- 🟡 **Intermediate Examples:**

```bash
# Reload configuration for a running nginx service
$ kill -HUP $(pidof nginx)
```

```bash
# Terminate all instances of 'apache2'
$ killall apache2
```

- 🔴 **SRE-Level Examples:**

```bash
# Scenario: Quickly stop all user-specific processes during a security incident
$ pkill -u compromised_user
```

```bash
# Scenario: Troubleshooting unresponsive processes with detailed feedback
$ pkill --signal SIGTERM -ef 'java.*app.jar'
```

#### **Instructional Notes:**

- 🧠 **Beginner Tip:** Always try `kill` without `-9` first to allow graceful termination.
- 🔧 **SRE Insight:** Use signals like `SIGHUP` for configuration reloads without downtime.
- ⚠️ **Common Pitfall:** Using `kill -9` prematurely can lead to data corruption or resource leaks.

### 🛠️ Filesystem & System Effects

- Filesystem changes: Potential log file truncation or corruption with forced kills.
- Metadata impacts: Process metadata entries removed.
- Automation impact: Essential in automated maintenance scripts.
- Misuse case: Accidentally terminating critical system processes; preventive measure: confirm PIDs and names before executing termination commands.

---

### ⚙️ 3. Job Control (`jobs`, `bg`, `fg`, `nohup`)

#### **Command Overview:**

- `jobs`: Lists active jobs initiated by the current shell.
- `bg`: Resumes a suspended job in the background.
- `fg`: Moves a background job to the foreground.
- `nohup`: Allows processes to continue running after terminal logout.

#### **Syntax & Flags:**

| Flag/Option | Syntax Example    | Explicit Description                               |
| ----------- | ----------------- | -------------------------------------------------- |
| `&`         | `command &`       | Runs command in the background.                    |
| `%n`        | `fg %1`, `bg %1`  | Selects job number to bring foreground/background. |
| `nohup`     | `nohup command &` | Makes a job immune to hangup signals.              |

#### **Explicit Examples:**

- 🟢 **Beginner Examples:**

```bash
# Run a command in the background
$ sleep 300 &
```

```bash
# View all active jobs
$ jobs
```

- 🟡 **Intermediate Examples:**

```bash
# Resume suspended job number 2 in background
$ bg %2
```

```bash
# Bring background job number 1 to foreground
$ fg %1
```

- 🔴 **SRE-Level Examples:**

```bash
# Scenario: Run critical backup script persistently through SSH session interruptions
$ nohup ./backup_script.sh > backup.log 2>&1 &
```

```bash
# Scenario: Managing a long-running job that requires intermittent foreground control
$ ./maintenance_script.sh &
$ jobs
$ fg %1  # bring to foreground for immediate interaction
```

#### **Instructional Notes:**

- 🧠 **Beginner Tip:** Use `jobs` frequently to track background tasks.
- 🔧 **SRE Insight:** Integrate `nohup` into scripts to ensure reliability across network interruptions.
- ⚠️ **Common Pitfall:** Forgetting `nohup` when starting long jobs remotely can result in unexpected termination.

### 🛠️ Filesystem & System Effects

- Filesystem changes: Output redirected to files when using `nohup`.
- Metadata impacts: Generated output files will update file timestamps.
- Automation impact: Crucial in resilient automation scripts.
- Misuse case: Excessive background jobs without proper management; preventive measure: regularly monitor and clear unnecessary jobs.

---

### 📈 4. System Resource Monitoring (`free`, `df`, `du`, `iostat`, `lsof`, `uname`)

#### **Command Overview:**

- `free`: Displays memory usage.
- `df`: Reports disk space usage.
- `du`: Estimates file and directory space usage.
- `iostat`: Monitors system I/O.
- `lsof`: Lists open files.
- `uname`: Prints system information.

#### **Syntax & Flags:**

| Flag/Option | Syntax Example     | Explicit Description                          |
| ----------- | ------------------ | --------------------------------------------- |
| `-h`        | `free -h`, `df -h` | Human-readable format for sizes.              |
| `-x`        | `iostat -x`        | Extended I/O statistics.                      |
| `-i`        | `lsof -i:80`       | Lists open files for a specific network port. |
| `-a`        | `uname -a`         | All available system information.             |

#### **Explicit Examples:**

- 🟢 **Beginner Examples:**

```bash
# Check total memory and usage
$ free -h
```

```bash
# Show available disk space
$ df -h
```

- 🟡 **Intermediate Examples:**

```bash
# Monitor detailed disk I/O activity
$ iostat -x 2 5
```

```bash
# List files open by processes on port 443
$ sudo lsof -i:443
```

- 🔴 **SRE-Level Examples:**

```bash
# Scenario: Identifying large disk usage by directory
$ du -h --max-depth=1 /var | sort -hr
```

```bash
# Scenario: Troubleshoot memory usage over time
$ watch -n 5 free -h
```

#### **Instructional Notes:**

- 🧠 **Beginner Tip:** Regularly use `df -h` to avoid unexpected disk full issues.
- 🔧 **SRE Insight:** Leverage `lsof` to rapidly troubleshoot port conflicts.
- ⚠️ **Common Pitfall:** Overlooking cached memory when interpreting `free` output; always refer to 'available' memory.

### 🛠️ Filesystem & System Effects

- Filesystem changes: None, purely informational.
- Metadata impacts: Access time (`atime`) updated when checking file sizes (`du`).
- Automation impact: Essential for automated system health checks.
- Misuse case: Misinterpreting output; preventive measure: thoroughly understand command outputs before automating.

---

### 🎯 Hands-On Exercises

#### 🟢 Beginner Exercises

1. **Process Viewing**
   - Use `ps aux` to list all running processes. Identify the PID of a process (e.g., your terminal).

2. **Memory Check**
   - Execute `free -h` and note total and available memory.

3. **Disk Usage**
   - Check disk space usage of your home directory with `du -sh ~`.

#### 🟡 Intermediate Exercises

1. **Process Hierarchy**
   - Use `ps aux --forest` to visualize process hierarchy and identify parent-child relationships.

2. **Background Job Management**
   - Start a background job (`sleep 100 &`), suspend it (`Ctrl+Z`), resume it in the background (`bg %1`), and finally bring it to foreground (`fg %1`).

3. **System I/O Monitoring**
   - Run `iostat -x 2 3` to monitor system disk I/O and analyze the output.

#### 🔴 SRE-Level Exercises

1. **Persistent Task Execution**
   - Create a persistent monitoring script using `nohup` that logs `free -h` output every minute. Verify persistence after terminating your SSH session.

2. **Incident Simulation - High CPU Usage**
   - Start a CPU-intensive process (e.g., infinite loop script). Identify and terminate this process using `htop` and `kill`.

3. **Resource Constraint Diagnosis**
   - Identify the largest directories under `/var` using `du -h --max-depth=1 /var`, and formulate a cleanup strategy.

---

### 📝 Quiz Questions

#### 🟢 Beginner Tier

1. **Multiple-Choice:** Which command provides real-time monitoring of processes?
   - A) `ps`
   - B) `top`
   - C) `uname`
   - D) `df`

2. **Fill-in-the-Blank:** To check disk usage of your home directory, you use `du ____ ~`.

3. **Scenario-Based:** You started a job but forgot to run it in the background. How do you pause it temporarily?

#### 🟡 Intermediate Tier

1. **Multiple-Choice:** What command reloads the configuration of a running process without stopping it?
   - A) `kill -HUP`
   - B) `kill -9`
   - C) `killall`
   - D) `pkill`

2. **Fill-in-the-Blank:** To monitor detailed disk I/O statistics, use `iostat ____ 2 5`.

3. **Scenario-Based:** Your process needs to continue after logging out of an SSH session. What command ensures this?

#### 🔴 SRE-Level Tier

1. **Multiple-Choice:** Which command lists files currently open by processes on a specific port?
   - A) `ps`
   - B) `top`
   - C) `lsof -i`
   - D) `uname`

2. **Fill-in-the-Blank:** Identify processes sorted by memory usage with `ps aux --sort=______ | head -10`.

3. **Scenario-Based:** During a high CPU usage incident, what sequence of commands would you execute to identify and terminate the problematic process?

---

### 🚧 Common Issues and Troubleshooting

#### 🛠️ Issue 1: "Process does not terminate with `kill`"

- **Common Cause:** The process is in an uninterruptible sleep state (D state).
- **Explicit Troubleshooting Steps:**
  1. Identify the problematic process state using `ps aux | grep " D "`.
  2. Investigate open files or resources using `lsof -p PID`.
  3. If unresponsive, consider rebooting or investigating underlying hardware issues.
- **Preventive Recommendation:** Monitor processes regularly to identify hung states early.

#### 📁 Issue 2: "Disk space reported full but large files not found"

- **Common Cause:** Deleted files still held by running processes.
- **Explicit Troubleshooting Steps:**
  1. Use `lsof | grep deleted` to identify files still consuming space.
  2. Restart services holding deleted files to free disk space.
- **Preventive Recommendation:** Regularly audit disk usage with `df` and `du`.

#### 📉 Issue 3: "Memory usage unexpectedly high"

- **Common Cause:** Memory leaks or excessive cache usage.
- **Explicit Troubleshooting Steps:**
  1. Check available memory using `free -h`.
  2. Identify high memory processes using `ps aux --sort=-%mem | head -10`.
  3. Investigate potential leaks or inefficient memory usage in identified processes.
- **Preventive Recommendation:** Set up regular monitoring and alerts for memory thresholds.

---
### ❓ FAQ

#### 🟢 Beginner Tier:

1. **How do I check my current disk usage quickly?**
   - Use the command `df -h` to display available and used disk space in a human-readable format.

2. **What is a PID?**
   - PID (Process ID) is a unique number assigned by Linux to identify a running process.

3. **Why might I use the `nohup` command?**
   - To ensure your processes continue running even if you close your terminal session.

#### 🟡 Intermediate Tier:

1. **Can I terminate multiple processes simultaneously?**
   - Yes, using `pkill` or `killall` allows you to terminate multiple processes based on names or patterns.

2. **What's the difference between `kill` and `kill -9`?**
   - `kill` sends a graceful termination signal, allowing processes to close properly. `kill -9` forcibly terminates without cleanup.

3. **How do I find which process uses a specific port?**
   - Execute `sudo lsof -i:<port_number>` to see which processes are using the port.

#### 🔴 SRE-Level Tier:

1. **What's the best way to identify resource bottlenecks quickly?**
   - Use `top`, `htop`, `iostat`, and `free` in conjunction to quickly diagnose CPU, memory, and disk bottlenecks.

2. **How can I ensure my process monitoring is effective during incidents?**
   - Set up automated monitoring scripts that combine tools like `top`, `ps`, and `lsof` to proactively alert on anomalies.

3. **How do I investigate a sudden memory spike?**
   - Run `ps aux --sort=-%mem` and `free -h` to pinpoint memory-consuming processes and available memory, then investigate further with detailed tools like `lsof`.

---
### 🔥 SRE Scenario Walkthrough

#### 🚨 Scenario: Diagnosing a Slow Web Server Incident

##### Incident Description

Users report slow response times on a critical web application. Your goal is to swiftly identify the root cause and restore normal service performance.

#### Explicit Steps & Rationale

1. **Check overall system health:**

   ```bash
   top
   ```

   - **Rationale:** Quickly identifies general CPU, memory usage, and load averages.

2. **Inspect memory usage:**

   ```bash
   free -h
   ```

   - **Rationale:** Ensures adequate memory availability and checks for swap usage indicating potential RAM exhaustion.

3. **Review disk usage and I/O:**

   ```bash
   df -h
   iostat -x 2 5
   ```

   - **Rationale:** Identifies disk space issues or I/O bottlenecks affecting server performance.

4. **Identify resource-intensive processes:**

   ```bash
   ps aux --sort=-%cpu | head -10
   ```

   - **Rationale:** Pinpoints processes consuming excessive CPU resources potentially impacting web service performance.

5. **Check network connections:**

   ```bash
   netstat -anp | grep :80 | wc -l
   ```

   - **Rationale:** Detects abnormal network connection counts possibly indicating an overload or attack.

6. **Examine web server logs for recent errors:**

   ```bash
   tail -n 50 /var/log/nginx/error.log
   ```

   - **Rationale:** Provides immediate insight into application-level issues.

7. **Implement remediation:**

   - Optimize resource-heavy processes identified.
   - Restart the web server if necessary.

#### Explicit Reflection

This structured diagnostic approach rapidly addresses common web service performance degradation scenarios, aligning directly with today's objectives of process management and system monitoring. Regular practice of these steps ensures readiness during real-world incidents.

---
### 🧠 Key Takeaways

- **Critical Commands & Concepts:**
  - Mastered real-time (`top`, `htop`) and snapshot (`ps`) process monitoring.
  - Process control using signals (`kill`, `pkill`, `killall`).
  - Effective job management (`jobs`, `bg`, `fg`, `nohup`).
  - Resource monitoring and management (`free`, `df`, `du`, `iostat`, `lsof`, `uname`).

- **Best Practices & Operational Insights:**
  - Prioritize graceful process termination to maintain system integrity.
  - Regularly monitor resource usage to preemptively address potential bottlenecks.
  - Use persistent command execution (`nohup`) to ensure continuity of critical tasks.
  - Automate monitoring routines to facilitate rapid incident response.

- **Preview of Next Day's Topic:**
  Tomorrow, we'll explore networking basics, including network troubleshooting, DNS configuration, and network monitoring tools. These skills are essential for managing distributed systems and ensuring robust, reliable connectivity across infrastructures.
