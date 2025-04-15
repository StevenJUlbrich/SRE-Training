# **Day 6: Processes & System Monitoring – A Comprehensive Linux SRE Training Module**

---

## 📌 **Introduction**

Processes and system monitoring are central to Linux operations. For Site Reliability Engineers (SREs), effectively viewing, managing, and controlling processes is essential to ensure uptime, optimize performance, and troubleshoot incidents before they escalate.

### **Why This Matters for SRE**

- **Reliability & Stability**: Proper process management ensures services don’t crash unexpectedly or consume all system resources.
- **Performance Monitoring**: Observing CPU, memory, and disk usage highlights bottlenecks early and prevents outages.
- **Security**: Understanding active processes and resource usage can reveal intrusions or malicious activity.

### **Learning Objectives**

**Beginner Level:**

1. Understand basic process concepts in Linux.
2. Use fundamental commands (`ps`, `kill`, etc.) to view and terminate processes.
3. Gather essential system info with commands like `uname`, `df`, `du`, `free`.

**Intermediate Level:**

1. Interactively manage processes (`top`, `htop`), prioritize or renice them, and handle background/foreground transitions.
2. Diagnose resource constraints by correlating process usage with disk, memory, and CPU metrics.
3. Implement more advanced usage of system info commands to monitor usage trends.

**SRE Level:**

1. Automate monitoring of critical processes and dynamically respond to anomalies.
2. Conduct complex incident investigations, combining process control with logs and in-depth resource utilization data.
3. Integrate system monitoring insights into broader observability and reliability frameworks.

### **Connecting to Previous and Future Learning**

- **Previously** (Day 5), you learned advanced text processing techniques to filter logs and data.
- **Today**, you apply those techniques to interpret live process information and resource usage.
- **Next** (Day 7), you’ll move into networking basics—diagnosing network latency and using tools like `ping`, `ssh`, and `netstat`.

---

## 📚 **Core Concepts**

Below are foundational ideas for process management and system monitoring, framed for all levels of expertise:

1. **Process Basics**
   - **Beginner Analogy**: Think of a process as a “task” your computer is doing—like an open app on your phone.
   - **Technical Explanation**: Each running program has a PID (Process ID) and various attributes (owner, priority, memory usage).
   - **SRE Application**: Overloading critical processes can degrade reliability; you must track them diligently.
   - **System Impact**: Misbehaving processes can lock CPU, exhaust memory, or block I/O.

2. **Process Hierarchy**
   - **Beginner Analogy**: A parent process can spawn child processes, like a “family tree.”
   - **Technical Explanation**: `init` or `systemd` often serve as ancestors to all processes. Child processes inherit certain resources from their parents.
   - **SRE Application**: Killing a parent sometimes terminates children; be cautious in multi-service architectures.
   - **System Impact**: Orphan or zombie processes can clutter process tables, causing stability issues.

3. **System Resource Monitoring**
   - **Beginner Analogy**: Monitoring resources is like checking your car’s fuel, temperature, and tire pressure.
   - **Technical Explanation**: Linux tracks CPU, RAM, disk, and I/O usage in real time. Tools like `top` and `htop` display these metrics interactively.
   - **SRE Application**: You must quickly spot resource saturations (e.g., CPU spikes) to avert downtime.
   - **System Impact**: Overworked CPU or insufficient memory leads to slow responses, crashes, or OOM (out-of-memory) kills.

4. **Foreground vs. Background Jobs**
   - **Beginner Analogy**: Foreground tasks are what you see on screen; background tasks work silently behind the scenes.
   - **Technical Explanation**: When you launch a command, it typically occupies the terminal (foreground). You can suspend (`Ctrl+Z`) and resume it in the background (`bg`) or bring it forward again (`fg`).
   - **SRE Application**: Running maintenance or backups in the background allows you to keep the terminal free for critical tasks.
   - **System Impact**: Proper job control prevents terminal lock-ups and allows multi-tasking on a single session.

---

## 💻 **Command Breakdown**

Below are 10 essential commands, each with a structured presentation including syntax tables, tiered examples, and instructional notes.

---

### **Command: ps (Process Status)**

**Command Overview:**  
`ps` provides a snapshot of the currently running processes. SREs use it to identify PID, CPU usage, memory usage, and command details in a single moment in time. It’s especially useful in scripts or to quickly verify if a process is running.

**Syntax & Flags:**

| Flag/Option | Syntax Example       | Description                                                 | SRE Usage Context                                           |
|-------------|----------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| `-a`, `-u`, `-x` | `ps aux`            | Show all processes (including other users, no TTY, etc.)    | Quick full view of everything running                      |
| `-e`, `-f`       | `ps -ef`            | Similar to `aux` format, but a different style (BSD vs SysV) | Common for pipe usage (e.g., grep) and advanced scripting  |
| `--forest`       | `ps --forest`       | Show process hierarchy in a tree-like format               | Identifying parent-child relationships                     |
| `-o`             | `ps -o pid,user,cmd`| Custom output columns                                      | Detailed investigations or specialized reports             |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Display all running processes in BSD style (user-oriented)
$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.2 171712  9352 ?        Ss   Mar27   0:02 /sbin/init
student    9876  2.5  4.5 241872 89120 pts/2   Sl+ 14:20   0:15 python3 script.py
# This gives you a basic list of processes with CPU & memory usage
```

- 🧩 **Intermediate Example:**

```bash
# Show all processes in SysV style and filter for "nginx"
$ ps -ef | grep nginx
root     11012     1  0 Mar26 ?        00:00:05 nginx: master process /usr/sbin/nginx
www-data 11013 11012  0 Mar26 ?        00:00:10 nginx: worker process
# You see the master worker model typical of Nginx
```

- 💡 **SRE-Level Example:**

```bash
# Display hierarchy and custom columns to spot resource-intensive children
$ ps --forest -o pid,user,%cpu,%mem,cmd
  PID  USER  %CPU %MEM CMD
  1001 root   0.0  0.1  /sbin/init
   1203 root   0.1  0.3   \_ /usr/lib/systemd/systemd-journald
   1500 user1 10.3 15.5   \_ java -Xmx2g -jar myapp.jar
   1501 user1  9.7 13.2        \_ GC Thread
# This lets you quickly identify a high-memory Java process and its helper threads
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** If you’re unsure which style to use, `ps aux` is popular for interactive use; `ps -ef` is often used in scripts.
- 🧠 **Beginner Tip:** Pair `ps` with `grep` to find specific processes by name (e.g., `ps aux | grep mysql`).

- 🔧 **SRE Insight:** Sorting the output (`ps aux --sort=-%cpu`) lets you see the top CPU consumers quickly.
- 🔧 **SRE Insight:** Use `ps -o` to reduce noise and collect only essential columns in scripts, e.g., for automated kill or resource monitoring.

- ⚠️ **Common Pitfall:** `ps` is only a snapshot; processes can change quickly. For real-time data, switch to `top` or `htop`.
- ⚠️ **Common Pitfall:** On some distros, `ps aux | grep something` can show the grep command itself. Use `[s]omething` trick or use `pgrep`.

- 🚨 **Security Note:** Listing processes can expose sensitive command-line arguments (e.g., passwords in scripts). Protect or mask them.
- 💡 **Performance Impact:** `ps` has minimal performance overhead, but repeated calls in quick succession can slightly increase load.

---

### **Command: top (Table Of Processes)**

**Command Overview:**  
`top` offers an interactive, real-time view of processes, CPU usage, memory usage, and load averages. It’s an essential command for SREs to quickly gauge system health and spot resource hogs.

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description                                             | SRE Usage Context                                 |
|-------------|----------------|---------------------------------------------------------|---------------------------------------------------|
| `-b`        | `top -b`       | Batch mode (non-interactive)                           | Logging or scripts for repeated snapshots         |
| `-n`        | `top -b -n 5`  | Run the specified number of iterations and exit        | Automating data collection over intervals         |
| `-p`        | `top -p 1234`  | Only monitor specific PID(s)                           | Focus on critical processes to reduce clutter     |
| Interactive | Press `1`, `m` | Toggle CPU cores, memory display, etc. in real time    | Quick on-the-fly reconfiguration of displayed data|

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Run top in default interactive mode
$ top
top - 14:25:33 up 2 days,  4:12,  2 users,  load average: 0.25, 0.15, 0.10
Tasks: 228 total,   1 running, 227 sleeping,   0 stopped,   0 zombie
%Cpu(s):  1.3 us,  0.7 sy,  0.0 ni, 97.5 id,  0.1 wa,  0.2 hi,  0.2 si,  0.0 st
MiB Mem :  16384.0 total,  12000.0 free,   2000.0 used,   1384.0 buff/cache
```

- 🧩 **Intermediate Example:**

```bash
# Monitor only processes owned by 'webuser'
$ top -u webuser
# Great for focusing on a single service or user workload
```

- 💡 **SRE-Level Example:**

```bash
# Collect 5 snapshots in batch mode for an incident timeline
$ top -b -n 5 -d 2 > top_log.txt
# Each snapshot is 2 seconds apart, capturing a short-time performance issue.
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Press `q` to quit. Press `c` to toggle between showing command name vs. full command path.
- 🧠 **Beginner Tip:** Press `1` in `top` to view each CPU core usage separately.

- 🔧 **SRE Insight:** `top` is invaluable for ephemeral spikes; keep it open during major deployments or migrations.
- 🔧 **SRE Insight:** Combine `-b` with cron or a scheduled job to gather historical performance data.

- ⚠️ **Common Pitfall:** `top` only shows the top CPU-consuming processes by default. Some memory hogs might not appear at the top of the list if their CPU usage is low.
- ⚠️ **Common Pitfall:** Running `top` in a slow terminal or over high-latency SSH can cause flicker or delayed refresh.

- 🚨 **Security Note:** As with `ps`, command lines in `top` might expose secrets or credentials.
- 💡 **Performance Impact:** `top` itself consumes some CPU as it refreshes. Over remote connections, frequent screen redraws can add overhead.

---

### **Command: htop (Interactive Process Viewer)**

**Command Overview:**  
`htop` is a user-friendly alternative to `top`. It offers a color-coded interface, mouse support, and easier navigation of processes. It also provides a clear view of CPU cores, memory, and processes in tree form.

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description                                 | SRE Usage Context                                |
|-------------|----------------|---------------------------------------------|--------------------------------------------------|
| `-d`        | `htop -d 10`   | Set the refresh delay in tenths of seconds  | Slower updates to reduce overhead or flickering  |
| `-u`        | `htop -u user` | Show processes for a single user           | Focus on a specific service account             |
| Interactive | Use arrow keys | Navigate the list, press `F3` to search, etc. | Real-time interactive control                    |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Simply start htop if installed
$ htop
# You see a colorful interface with CPU bars and memory usage
```

- 🧩 **Intermediate Example:**

```bash
# Start htop focusing on processes of user "deploy"
$ htop -u deploy
# Helps you isolate a deployment user's processes quickly
```

- 💡 **SRE-Level Example:**

```bash
# Searching for a memory hog process within htop
# 1) Press F3
# 2) Type "java"
# 3) Press F4 to filter
# Allows immediate narrowing of suspicious processes in large environments
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Use arrow keys or PgUp/PgDn to scroll through the full process list.
- 🧠 **Beginner Tip:** Press `F6` to sort by different columns (e.g., CPU, memory).

- 🔧 **SRE Insight:** `htop` can kill or renice processes interactively (use `F9` for kill and `F7/F8` for priority).
- 🔧 **SRE Insight:** It’s easier to visualize multi-core usage at a glance compared to `top`.

- ⚠️ **Common Pitfall:** `htop` may not be installed by default. Install via `sudo apt install htop` or `sudo yum install htop`.
- ⚠️ **Common Pitfall:** Using the mouse over a laggy SSH session can be confusing if clicks do not register promptly.

- 🚨 **Security Note:** The same caution about exposing command-line arguments applies here.
- 💡 **Performance Impact:** `htop` refreshes can be somewhat heavier than `top`; reduce refresh rate if system load is extremely high.

---

### **Command: kill (Terminate a Process)**

**Command Overview:**  
`kill` sends a signal to a process, typically to request termination. As an SRE, you’ll often use `kill` to stop or reload services gracefully—or forcefully if necessary.

**Syntax & Flags:**

| Flag/Option     | Syntax Example     | Description                                                     | SRE Usage Context                                                |
|-----------------|--------------------|-----------------------------------------------------------------|------------------------------------------------------------------|
| `-l`            | `kill -l`         | List all available signals                                      | Checking signal names and numbers                               |
| `-9` (SIGKILL)  | `kill -9 1234`    | Force-kill process immediately                                  | Last resort for hung or unresponsive processes                  |
| `-HUP` (SIGHUP) | `kill -HUP 5678`  | Request process to reload configuration                         | Common for daemon reloads (e.g., reload nginx configs)          |
| `-TERM` (15)    | `kill -TERM 9999` | Default signal, gracefully terminate if possible                | Standard approach for normal shutdown                           |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Gracefully stop a process with PID 1234
$ kill 1234
# This attempts to let the process exit cleanly
```

- 🧩 **Intermediate Example:**

```bash
# Force-kill a stubborn/hung process
$ kill -9 5678
# Use with caution, as the process won't clean up resources
```

- 💡 **SRE-Level Example:**

```bash
# Reload the configuration of an Nginx web server
$ kill -HUP $(pgrep nginx)
# Minimizes downtime by telling Nginx master process to reload conf
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Always try a graceful kill first; `kill` is equivalent to `kill -TERM`.
- 🧠 **Beginner Tip:** Use `ps` or `top` to confirm the PID before killing.

- 🔧 **SRE Insight:** Overusing `kill -9` can lead to orphaned child processes or locked files. Only do it when absolutely necessary.
- 🔧 **SRE Insight:** Some services interpret signals in custom ways. For example, `SIGHUP` can mean “reload config” rather than termination.

- ⚠️ **Common Pitfall:** Killing the wrong PID can disrupt essential system services. Double-check your target.
- ⚠️ **Common Pitfall:** Some processes in uninterruptible I/O (D state) can’t be killed even with `-9`.

- 🚨 **Security Note:** If you kill security monitoring agents or authentication processes inadvertently, you can expose the system to risk.
- 💡 **Performance Impact:** Killing resource-heavy processes can free up system resources instantly—useful in major incidents.

---

### **Command: jobs (List Current Shell Jobs)**

**Command Overview:**  
`jobs` displays the background and suspended jobs started in the current shell. As an SRE, you often run maintenance tasks in the background; `jobs` shows their status.

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description                                  | SRE Usage Context                                  |
|-------------|----------------|----------------------------------------------|----------------------------------------------------|
| (none)      | `jobs`         | Lists jobs in the current shell environment | Quickly check how many tasks you have in progress |
| `-l`        | `jobs -l`      | Shows process IDs alongside job numbers     | Useful for precise process management             |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Assume you ran "sleep 100 &"
$ jobs
[1]+  Running                 sleep 100 &
# This shows the job index [1] and that it's running
```

- 🧩 **Intermediate Example:**

```bash
# Show jobs with PIDs
$ jobs -l
[1]+  12345 Running                 sleep 100 &
[2]-  12890 Stopped                 top
# You see which is running vs. stopped and the PIDs
```

- 💡 **SRE-Level Example:**

```bash
# In a maintenance script, track backgrounded tasks:
$ jobs -l
[1]   29512 Running  ./backup.sh &
[2]-  29576 Running  ./logrotate.sh &
# Using job info, you can confirm concurrency for multiple tasks.
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Only jobs launched in the **current** terminal session appear here, not system-wide.
- 🧠 **Beginner Tip:** Use `fg %1` to bring job #1 to the foreground.

- 🔧 **SRE Insight:** `jobs` is essential for multi-tasking in a single SSH session—common during emergencies.
- 🔧 **SRE Insight:** Combine with `nohup` or `screen/tmux` if you need to log out without killing these jobs.

- ⚠️ **Common Pitfall:** Closing the terminal or losing SSH while a job is running in the foreground can terminate it if not protected.
- ⚠️ **Common Pitfall:** Forgetting which job is which can lead to confusion if you have multiple concurrent tasks.

- 🚨 **Security Note:** Hidden or background jobs might be used by attackers for stealthy processes—keep an eye on them.
- 💡 **Performance Impact:** Background jobs still consume CPU/memory. Monitor them to ensure they don’t choke production.

---

### **Command: bg (Resume Suspended Job in Background)**

**Command Overview:**  
`bg` resumes a job that’s been stopped (via `Ctrl+Z` or otherwise) in the background. SREs use this to free the terminal while a long task continues.

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description                                       | SRE Usage Context                                 |
|-------------|----------------|---------------------------------------------------|---------------------------------------------------|
| `[job_spec]`| `bg %1`        | Specify the job number or name to resume         | Precisely target the desired suspended job        |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Suppose you press Ctrl+Z on "top" to suspend it
$ jobs
[1]+  Stopped                 top
$ bg %1
[1]+ top & 
# Now "top" continues in the background
```

- 🧩 **Intermediate Example:**

```bash
# If you have multiple jobs
$ jobs
[1]   Stopped                 python3 script.py
[2]-  Stopped                 vim config.txt
$ bg %2
# Brings "vim config.txt" job to background (though vim in background is unusual)
```

- 💡 **SRE-Level Example:**

```bash
# During a large data transfer, you can suspend it to check something, then send it to bg
$ rsync -av /bigdata /backup
^Z  # suspended
$ bg %+
# The most recently suspended job is resumed in the background
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** `%+` refers to the most recently used job, while `%1` or `%2` refer to specific job numbers.
- 🧠 **Beginner Tip:** Backgrounding interactive programs (like `vim`) usually isn’t helpful—only do it for tasks that don’t require real-time input.

- 🔧 **SRE Insight:** If you realize a command will take hours, background it to keep working in the same shell.
- 🔧 **SRE Insight:** Pair with `tail -f` or log watchers in separate windows to monitor job progress in real time.

- ⚠️ **Common Pitfall:** Some programs cannot effectively run in the background if they expect continuous input.
- ⚠️ **Common Pitfall:** If you background a job that needs terminal input, it may hang or fail.

- 🚨 **Security Note:** Interactive jobs left running in background might expose partial data if an unauthorized user gains the same session.
- 💡 **Performance Impact:** Running many background tasks can degrade system performance; keep an eye on system load.

---

### **Command: fg (Resume Job in Foreground)**

**Command Overview:**  
`fg` brings a background or stopped job back to the foreground, allowing direct interaction. This is crucial when a background task needs your immediate attention.

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description                                 | SRE Usage Context                        |
|-------------|----------------|---------------------------------------------|------------------------------------------|
| `[job_spec]`| `fg %2`        | Specify job number or name to bring forward| Switch back to an interactive session    |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# A job is running in background
$ jobs
[1]+  Running   tail -f /var/log/syslog &
$ fg %1
tail -f /var/log/syslog
# Now you're back at the tail -f in the foreground
```

- 🧩 **Intermediate Example:**

```bash
# Switching from a background data copy to monitor progress
$ fg %copy_data
# If you named the job or recognized it by partial command in advanced shells
```

- 💡 **SRE-Level Example:**

```bash
# During maintenance, you might have multiple scripts
$ jobs -l
[1]- 24820 Running backup.sh &
[2]+ 24830 Stopped metrics_collection.sh
# Bring metrics to foreground to confirm output
$ fg %2
metrics_collection.sh
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Use `jobs` to see the job index before calling `fg`.
- 🧠 **Beginner Tip:** `fg` without arguments typically brings up the most recently backgrounded or stopped job.

- 🔧 **SRE Insight:** This is invaluable during large scripts or backups that occasionally need interactive input or checks.
- 🔧 **SRE Insight:** `fg` can help you gracefully terminate a job that was running in the background instead of just killing it blindly.

- ⚠️ **Common Pitfall:** If the job was started on a different shell, `fg` won’t work. Each shell only knows about its own jobs.
- ⚠️ **Common Pitfall:** Bringing certain services to foreground (like daemons) might not make sense. Usually, they run as services, not shell jobs.

- 🚨 **Security Note:** Foregrounding a previously backgrounded sensitive script might reveal logs or credentials on screen—ensure you’re in a secure environment.
- 💡 **Performance Impact:** No direct performance impact; just changes how you interact with the job.

---

### **Command: uname (Unix Name)**

**Command Overview:**  
`uname` provides system information such as kernel name, version, and architecture. SREs use it to quickly check kernel details, especially when diagnosing kernel-specific issues or verifying compatibility.

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description                                                | SRE Usage Context                                  |
|-------------|----------------|------------------------------------------------------------|----------------------------------------------------|
| `-a`        | `uname -a`     | Print all system info: kernel name, version, architecture | Quick baseline info in incident triage            |
| `-r`        | `uname -r`     | Kernel release                                            | Checking if system is up-to-date or matching known bug fixes |
| `-m`        | `uname -m`     | Machine hardware name (architecture)                      | Confirming 64-bit vs. 32-bit compatibility         |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
$ uname -a
Linux server1 5.11.0-40-generic #44-Ubuntu SMP x86_64 x86_64 x86_64 GNU/Linux
# Basic overview of the kernel and OS platform
```

- 🧩 **Intermediate Example:**

```bash
$ uname -r
5.11.0-40-generic
# Handy if you need to check for kernel-level patches or modules
```

- 💡 **SRE-Level Example:**

```bash
# Quickly see if architecture matches deployment artifacts
$ arch=$(uname -m)
$ echo "Running architecture is: $arch"
# E.g., x86_64, aarch64, etc., used in automation to pull correct binaries
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Often used in combination with other commands (like `lsb_release -a`) for full OS details.
- 🧠 **Beginner Tip:** If you only need kernel version, `uname -r` is more concise.

- 🔧 **SRE Insight:** Knowing the kernel version is critical when debugging performance issues or applying kernel patches.
- 🔧 **SRE Insight:** Automate environment checks in CI/CD pipelines to ensure the correct environment is running.

- ⚠️ **Common Pitfall:** `uname` alone might not provide distribution info (like “Ubuntu” or “CentOS”). Use distro-specific commands or `/etc/os-release`.
- ⚠️ **Common Pitfall:** On containers, `uname` might reflect the host kernel, which can be misleading.

- 🚨 **Security Note:** Some older kernels might have known security exploits—always patch regularly.
- 💡 **Performance Impact:** `uname` is extremely lightweight and has negligible performance impact.

---

### **Command: df (Disk Filesystem)**

**Command Overview:**  
`df` reports disk space usage of file systems. SREs must ensure no file system runs out of space unexpectedly, as that leads to service failures and data corruption.

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description                                      | SRE Usage Context                               |
|-------------|----------------|--------------------------------------------------|-------------------------------------------------|
| `-h`        | `df -h`        | Human-readable sizes (K, M, G)                  | Quick glance at space usage                     |
| `-T`        | `df -T`        | Show filesystem type                            | Diagnosing ext4, xfs, tmpfs, etc. for performance or features |
| `-i`        | `df -i`        | Display inode usage instead of block usage      | Important if “no space left” is actually inode exhaustion |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        20G   13G  6.5G  67% /
/dev/sdb1       100G   45G   55G  45% /data
```

- 🧩 **Intermediate Example:**

```bash
# Check file system types and usage
$ df -hT
Filesystem     Type   Size  Used Avail Use% Mounted on
/dev/sda1      ext4    20G   13G  6.5G  67% /
/dev/sdb1      xfs    100G   45G   55G  45% /data
tmpfs          tmpfs  2.0G  128M  1.9G   7% /run
```

- 💡 **SRE-Level Example:**

```bash
# Monitoring disk usage during an incident every 5 seconds
$ watch -n 5 df -h
# Helps you see if log files are rapidly consuming space
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** If your root (`/`) is nearly full, your system may become unstable—act quickly.
- 🧠 **Beginner Tip:** Look at the “Use%” column for a quick sense of capacity.

- 🔧 **SRE Insight:** Sometimes a disk appears full even after deleting files—processes with open file handles keep space allocated until they exit.
- 🔧 **SRE Insight:** Use `df -i` if your system claims “no space left” but `df -h` shows plenty of space—inode exhaustion might be the culprit.

- ⚠️ **Common Pitfall:** `df` only shows usage at the filesystem level, not per folder or file. Use `du` for deeper analysis.
- ⚠️ **Common Pitfall:** NFS or network mounts can report unusual data if the remote server is down or unreachable.

- 🚨 **Security Note:** Overfull logs can lead to system denial-of-service or inability to write critical security events.
- 💡 **Performance Impact:** `df` is typically fast. However, unresponsive network mounts can make it hang temporarily.

---

### **Command: du (Disk Usage)**

**Command Overview:**  
`du` estimates file or directory usage on disk. SREs use `du` to pinpoint large log files or directories that risk filling up storage.

**Syntax & Flags:**

| Flag/Option       | Syntax Example         | Description                                            | SRE Usage Context                                    |
|-------------------|------------------------|--------------------------------------------------------|------------------------------------------------------|
| `-h`              | `du -h /var/log`       | Human-readable output                                  | Faster readability of large directories             |
| `-s`              | `du -sh /home/user`    | Summarize only the total size                          | Quick snapshot of overall directory size            |
| `--max-depth=N`   | `du -h --max-depth=1 .`| Limit directory depth                                  | Identify which subdirectories are largest           |
| `--exclude=pattern` | `du -h --exclude='*.tmp' /data` | Skip certain files/directories               | Avoid clutter from logs, temporary files, etc.      |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Check the size of the current directory
$ du -sh .
258M    .
```

- 🧩 **Intermediate Example:**

```bash
# Compare subdirectory sizes in /var/log
$ du -h --max-depth=1 /var/log
4.0K    /var/log/apt
12M     /var/log/syslog
1.2M    /var/log/journal
...
# Notice which logs are big
```

- 💡 **SRE-Level Example:**

```bash
# Exclude backups and only go 2 levels deep in /data
$ du -h --max-depth=2 --exclude='backup*' /data
2.3G  /data/logs
1.2G  /data/application/cache
4.5G  /data
# Useful in big data environments to focus on critical folders
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** `-s` is handy if you only want a single total instead of a long file-by-file list.
- 🧠 **Beginner Tip:** Pair `du` with `sort -h` to see largest directories on top.

- 🔧 **SRE Insight:** If a partition is filling rapidly, run `du` on suspected directories (e.g., `/var/log`) to locate the culprit quickly.
- 🔧 **SRE Insight:** Combine `du` with `find` to track files by size and modification time for deeper forensics.

- ⚠️ **Common Pitfall:** Large directories with thousands of files can make `du` slow. Use `--max-depth` for quicker partial insights.
- ⚠️ **Common Pitfall:** Symbolic links can create confusion if you aren’t aware you’re measuring the same data multiple times. Check `-L` or `-P` usage carefully.

- 🚨 **Security Note:** World-readable directories might reveal sensitive file sizes or patterns—be mindful about what you share.
- 💡 **Performance Impact:** On very large directories, `du` can spike disk I/O. Schedule large analyses in off-peak hours.

---

### **Command: free (Memory Usage)**

**Command Overview:**  
`free` displays the system’s memory usage, including physical RAM, swap space, and buffers/cache. SREs monitor this to detect memory leaks, heavy usage, or potential OOM conditions.

**Syntax & Flags:**

| Flag/Option | Syntax Example  | Description                                        | SRE Usage Context                                      |
|-------------|-----------------|----------------------------------------------------|--------------------------------------------------------|
| `-h`        | `free -h`       | Human-readable format                              | Quick, easy-to-read memory stats                       |
| `-s N`      | `free -s 5 -h`  | Continuously display memory usage every N seconds | Automated observation of memory usage trends           |
| `-t`        | `free -t`       | Show total line at the end                         | Summarize overall memory usage in detail               |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           15Gi       4.6Gi       8.0Gi       264Mi       3.0Gi        10Gi
Swap:         4.0Gi          0B       4.0Gi
```

- 🧩 **Intermediate Example:**

```bash
# Watch memory usage every 5 seconds
$ free -h -s 5
              total   used   free   shared  buff/cache  available
Mem:           15Gi   6.2Gi  5.3Gi  300Mi    3.5Gi       7.5Gi
Swap:         4.0Gi   0B     4.0Gi
...
# This will continuously update
```

- 💡 **SRE-Level Example:**

```bash
# Incorporate into a quick performance check script
$ while true; do 
  date
  free -m | grep Mem
  sleep 10
done
# Logs memory usage every 10 seconds with timestamps for correlation
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Look at the “available” column, not just “free.” Linux caches aggressively, so “free” alone can be misleading.
- 🧠 **Beginner Tip:** The “buffers/cache” usage is often reclaimed quickly if needed by running processes.

- 🔧 **SRE Insight:** A sudden drop in “available” memory might indicate a memory leak or runaway process.
- 🔧 **SRE Insight:** Check swap usage to see if the system is actively paging out—this often slows performance drastically.

- ⚠️ **Common Pitfall:** `free` doesn’t detail which process uses how much memory—use `ps aux --sort=-%mem` or tools like `smem`.
- ⚠️ **Common Pitfall:** “Used” memory can appear high because of caches; rely on “available” for real usage.

- 🚨 **Security Note:** Low memory can cause critical security daemons (like intrusion detection) to be killed by OOM. Always maintain sufficient memory overhead.
- 💡 **Performance Impact:** `free` is lightweight, but rely on continuous monitoring solutions for large-scale or distributed environments.

---

## 🛠️ **System Effects**

- **Filesystem & Metadata**  
  Commands like `df` and `du` only read metadata and directory info but do not modify files. However, incorrectly interpreting disk usage can lead to accidental deletions.
- **System Resources**  
  Monitoring tools (`top`, `htop`) have minimal overhead but can still impact CPU usage if run excessively or on large terminal sessions.
- **Security Implications**  
  Viewing process details (`ps`, `top`, `htop`) can expose sensitive info. Terminating critical security processes can open vulnerabilities.
- **Monitoring Visibility**  
  Combining these commands with logs and metrics helps create a holistic monitoring strategy. They are cornerstones of on-host observability in SRE practice.

---

## 🎯 **Hands-On Exercises**

### **Beginner Exercises (3)**

1. **Listing Processes**
   - Run `ps aux` and observe the output. Identify at least one system process (e.g., `systemd`) and note its PID.
   - Practice `ps aux | grep <process_name>` to filter for that process.

2. **Terminating a Test Process**
   - Open a second terminal, run `sleep 300`.
   - In the first terminal, find its PID (`ps aux | grep sleep`) and gracefully terminate it (`kill <PID>`).

3. **Checking Disk Space**
   - Run `df -h` on your system.
   - Identify which partition has the highest usage. Discuss how you might reduce usage if it’s close to 100%.

### **Intermediate Exercises (3)**

1. **Monitoring Resource Usage in Real Time**
   - Start a resource-heavy command (e.g., `sha256sum /dev/zero`—careful with CPU usage).
   - Run `top` or `htop` to watch it consume CPU. Take note of the PID and CPU% usage. Terminate it with `kill`.

2. **Investigating Large Folders**
   - Use `du -h --max-depth=1 /var/log` to see which logs are largest.  
   - Sort them by size (`du -h --max-depth=1 /var/log | sort -h`) and identify top consumers.

3. **Experimenting with Background Jobs**
   - Start a command like `sleep 300`.
   - Press `Ctrl+Z` to suspend it, then use `bg` to resume it in the background.  
   - Confirm it’s running with `jobs`, then bring it to the foreground with `fg`.

### **SRE-Level Exercises (3)**

1. **Automated Disk Monitoring**
   - Write a small script using `df -h` and `du -sh` in a loop, logging results to a file every minute for 10 minutes.
   - Analyze the log to see how usage changes over time (simulate or create some disk usage in between).

2. **Memory Stress and Monitoring**
   - Use a memory stress test tool (e.g., `stress --vm 1 --vm-bytes 512M --timeout 60s`) to artificially load memory.
   - In parallel, run `free -h -s 5` to watch real-time memory usage.  
   - Observe how the system recovers after the stress test completes.

3. **Process Tree Investigation**
   - Run a service that spawns multiple child processes (e.g., `nginx` or a `node` cluster).
   - Use `ps --forest` (or `pstree`) combined with `lsof -p <PID>` to map out parent-child relationships and open ports/files.  
   - Document any potential performance or security issues you discover.

---

## 📝 **Quiz Questions**

### **Beginner Level (3-4 Qs)**

1. **MCQ**: Which command shows a snapshot of current processes in BSD-style format?  
   A) `ps aux`  
   B) `jobs`  
   C) `free -h`  
   D) `df -h`

2. **Fill in the Blank**: To see the currently running jobs in your shell, you would type `__________`.

3. **Short Answer**: Explain the difference between `kill -9` and `kill` (without flags).

### **Intermediate Level (3-4 Qs)**

1. **MCQ**: Which command below is best for real-time, interactive process monitoring with color-coded output?  
   A) `top -b`  
   B) `htop`  
   C) `ps -ef`  
   D) `jobs`

2. **Scenario**: You notice your `/data` partition is 90% full. Which two commands could help you pinpoint large directories/files?

3. **Fill in the Blank**: To resume job number 2 in the background, you would type `__________ %2`.

4. **True/False**: `free -h` includes swap usage in its output.

### **SRE Level (3-4 Qs)**

1. **Scenario**: During an outage call, you suspect the Java service is using too much memory. Name two commands that would help you confirm this and how.
2. **Short Answer**: Why might you run `iostat` or `vmstat` in addition to `top` when investigating a performance bottleneck?
3. **MCQ**: Which command combination continuously records process snapshots for historical analysis?  
   A) `kill -9 $(pgrep -u root)`  
   B) `top -b -n 1`  
   C) `watch -n 2 ps aux`  
   D) `jobs -l && bg %1`
4. **True/False**: If `df -h` reports enough free space, the system cannot run out of inodes.

---

## 🚧 **Troubleshooting Scenarios**

Below are three realistic issues an SRE might face:

1. **Scenario: Zombie Processes After a Crash**
   - **Symptoms**: `ps aux` shows multiple processes in `Z` (zombie) status; system performance is normal but the process table is cluttered.
   - **Likely Cause**: Parent processes failed to wait on child processes after they exited.
   - **Diagnostics**:
     - Use `ps --forest` to see parent-child relationships.
     - Check if the parent is still running or stuck.
   - **Resolution**:
     - If the parent is still alive, restart or kill it gracefully so it reaps zombies.
     - If the parent is critical, schedule downtime for a controlled restart.
   - **Prevention**: Ensure well-behaved daemons that properly handle child exit. Use modern init systems (systemd) to manage services.

2. **Scenario: High Load, Low CPU Usage**
   - **Symptoms**: `top` shows high load averages, but CPU usage is low. Many processes in uninterruptible sleep (`D` state).
   - **Likely Cause**: I/O bottleneck on disk or NFS mount.
   - **Diagnostics**:
     - Run `iostat -x 2 5` or `dstat` to check disk throughput.
     - Look for processes waiting on disk I/O.
   - **Resolution**:
     - If it’s an NFS issue, check network connectivity and NFS server logs.
     - If local disk, investigate hardware health or resizing the workload.
   - **Prevention**: Implement storage monitoring, alerts for I/O wait, and adequate resource provisioning.

3. **Scenario: Out of Disk Space Despite File Deletions**
   - **Symptoms**: `df -h` remains high usage, even after removing large files. Services are complaining of “no space left on device.”
   - **Likely Cause**: A process still holds open file descriptors to deleted files.
   - **Diagnostics**:
     - Use `lsof | grep deleted` to locate which processes reference removed files.
   - **Resolution**:
     - Gracefully restart or kill the process to release the file descriptors.
   - **Prevention**: Use log rotation (e.g., `logrotate`) to properly rotate and close logs.

---

## ❓ **FAQ**

### **Beginner Level (3)**

1. **Q:** How do I stop a command that’s running in my terminal right now?  
   **A:** Press `Ctrl+C` for an immediate interrupt. If you want to pause it, use `Ctrl+Z` and then decide if you want to terminate or resume in the background.

2. **Q:** What does `jobs` show?  
   **A:** It lists tasks that were started in or moved to the background in your current shell, along with their status.

3. **Q:** Why do I see “%CPU” and “%MEM” in `ps aux`?  
   **A:** They show the percentage of CPU and memory that each process is currently using, giving a quick sense of resource consumption.

### **Intermediate Level (3)**

1. **Q:** Can I run `top` in a script?  
   **A:** Yes, use `top -b -n <iterations>`. This non-interactive mode captures output to a file or pipeline for analysis.

2. **Q:** Why is my disk still full after deleting a large file?  
   **A:** A process might still hold it open. Check with `lsof` for “deleted” references and stop or restart that process.

3. **Q:** Is it normal for `free -h` to show small “free” but large “available”?  
   **A:** Yes, Linux caches frequently used files in memory for performance. “Available” indicates memory that can be reclaimed quickly.

### **SRE Level (3)**

1. **Q:** How do I handle a critical service stuck in `D` state that refuses `kill -9`?  
   **A:** Processes in uninterruptible I/O can’t be killed until I/O completes. Investigate the underlying I/O device or network storage.

2. **Q:** What’s the difference between using `ps aux | grep` and `pgrep`?  
   **A:** `pgrep` is designed to search for processes by name without matching the grep command itself. It’s more script-friendly.

3. **Q:** If I suspect a memory leak, how do I track it over time?  
   **A:** Use repeated or continuous snapshots (`ps aux --sort=-%mem` or `free -h -s 5`) plus logging. Tools like `pidstat`, `smem`, or `cgroup` tracking can also help in deeper analysis.

---

## 🔥 **SRE Scenario: Investigating Sudden High Memory Usage**

**Incident Context**: Your monitoring system triggers an alert that memory usage on the main web server is at 85% and rising. The system is at risk of OOM kills.

**SRE Command Steps**:

1. **Check Overall Usage**  

   ```bash
   free -h
   ```

   *Reasoning:* Confirm the actual memory usage vs. cache to see if the alert is valid.

2. **Identify Top Consumers**  

   ```bash
   ps aux --sort=-%mem | head -10
   ```

   *Reasoning:* Sort processes by memory usage to see if a single process is ballooning.

3. **Monitor in Real Time**  

   ```bash
   top
   ```

   *Reasoning:* Watch the memory usage live, check if it continues to grow.

4. **Inspect the Process Further**  

   ```bash
   lsof -p <PID_of_suspect> | grep -i 'log\|tmp'
   ```

   *Reasoning:* See if the process is holding large log files open or creating excessive temporary data.

5. **Attempt Graceful Restart**  

   ```bash
   kill -TERM <PID_of_suspect>
   # or systemctl restart myservice
   ```

   *Reasoning:* A graceful stop or service restart can free memory. If not, escalate to `kill -9`.

6. **Check Logs**  

   ```bash
   grep -i "out of memory" /var/log/syslog
   ```

   *Reasoning:* Identify if the system is about to invoke or has invoked the OOM killer.

7. **Plan for Prevention**  
   *Reasoning:* Patch or reconfigure the service if it’s leaking memory. Possibly add swap or more RAM if usage is legitimate.

This approach demonstrates SRE best practices: quickly identify the culprit, attempt graceful recovery, verify logs, and plan long-term fixes.

---

## 🧠 **Key Takeaways**

1. **Command Summary**  
   - **`ps`**: Snapshot of processes.  
   - **`top/htop`**: Real-time, interactive system monitoring.  
   - **`kill`**: Send signals to processes (terminate or reload).  
   - **`jobs`, `bg`, `fg`**: Shell-based job control.  
   - **`uname`, `df`, `du`, `free`**: System info, disk usage, and memory usage.

2. **Operational Insights**  
   - Monitoring is proactive. Quick detection of anomalies helps maintain high availability.  
   - Always verify the exact process you’re targeting before sending signals.  
   - Combining real-time and snapshot tools provides a full picture of system health.

3. **Best Practices**  
   - Use graceful signals first (`SIGTERM`) before `SIGKILL`.  
   - Keep an eye on background tasks—don’t let them consume all resources unnoticed.  
   - Use advanced flags (`--forest`, `-b`, etc.) for deeper investigations and automation.

4. **Preview of Next Topic**  
   - Next, you’ll dive into networking fundamentals: `ping`, `netstat`, DNS basics, and more. Mastering these is crucial for diagnosing slow or failing connections in distributed systems.

---

## 📚 **Further Learning Resources**

### **🔍 Beginner**

1. **“Linux Journey”**  
   **Link**: [https://linuxjourney.com/](https://linuxjourney.com/)  
   **Description**: Interactive lessons on Linux fundamentals, including processes and file systems.  
   **Beginner Application**: Builds core CLI and system knowledge at a gentle pace.

2. **“Ubuntu Official Documentation - Basic Commands”**  
   **Link**: [https://help.ubuntu.com/community/UsingTheTerminal](https://help.ubuntu.com/community/UsingTheTerminal)  
   **Description**: Covers essential terminal usage and basic commands.  
   **Beginner Application**: Quick references for new users to practice daily tasks.

3. **“The Linux Command Line” (Free PDF)**  
   **Link**: [http://linuxcommand.org/tlcl.php](http://linuxcommand.org/tlcl.php)  
   **Description**: A complete beginner’s guide to the command line.  
   **Beginner Application**: Learn how to navigate the shell, manage files, and run commands effectively.

### **🧩 Intermediate**

1. **“Linux System Administration Skills” (Red Hat)**  
   **Link**: [https://www.redhat.com/sysadmin](https://www.redhat.com/sysadmin)  
   **Description**: Articles on administering Linux systems, focusing on monitoring and process management.  
   **Operational Connection**: Helps you apply commands in real server environments.

2. **“DigitalOcean Tutorials: Process Management”**  
   **Link**: [https://www.digitalocean.com/community/tutorials/tag/linux-process](https://www.digitalocean.com/community/tutorials/tag/linux-process)  
   **Description**: Step-by-step guides for process viewing, signals, and job control.  
   **Operational Connection**: Great for honing day-to-day sysadmin tasks.

3. **“Linux Performance Analysis in 60 Seconds”**  
   **Link**: [http://www.brendangregg.com/linuxperf.html](http://www.brendangregg.com/linuxperf.html)  
   **Description**: Quick performance triage tips from an industry expert.  
   **Operational Connection**: Perfect for mid-level engineers needing swift incident triage strategies.

### **💡 SRE-Level**

1. **“Google SRE Book - Chapter: Managing Load”**  
   **Link**: [https://sre.google/sre-book/handling-overload/](https://sre.google/sre-book/handling-overload/)  
   **Description**: Advanced concepts in load management and reliability.  
   **Reliability Engineering Skill**: In-depth approach to capacity planning and systematic performance management.

2. **“Netflix TechBlog: Linux Performance Tools”**  
   **Link**: [https://netflixtechblog.com/](https://netflixtechblog.com/) (search for “Linux Performance Tools”)  
   **Description**: Deep-dive articles on advanced Linux troubleshooting tools beyond the basics.  
   **Reliability Engineering Skill**: Learn how at-scale companies debug major performance issues.

3. **“System Performance: Enterprise and the Cloud” (Brendan Gregg)**  
   **Link**: [http://www.brendangregg.com/index.html](http://www.brendangregg.com/index.html)  
   **Description**: Comprehensive coverage of monitoring, profiling, and tuning.  
   **Reliability Engineering Skill**: Gains advanced techniques for analyzing CPU, memory, file systems, and more at scale.

---

**Congratulations!** You have completed Day 6 of the Linux SRE path, mastering essential commands for process management and system monitoring. Practice them regularly to develop muscle memory and incorporate them into your SRE toolbox for real-world reliability and performance challenges. Next up: **networking basics**—where you’ll learn how to diagnose connectivity issues and handle distributed systems more effectively.
