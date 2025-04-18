# **Day 6: Processes & System Monitoring – Enhanced Linux SRE Training Module**

## 📌 **Introduction**

### **Recap of Day 5**

Previously, you honed your Linux skills with advanced text processing tools—such as `sed`, `awk`, `sort`, and `uniq`—and learned how piping and redirection can streamline data manipulation. Those skills enable you to sift through logs, filter data, and automate repetitive tasks effectively.

### **Why Process Management & System Monitoring Matter for SRE**

As a Site Reliability Engineer (SRE), you’re responsible for maintaining service uptime, performance, and security. Process management and system monitoring are critical because:

- **Reliability & Stability**: Keeping key processes healthy ensures system uptime.
- **Performance Optimization**: Identifying resource bottlenecks helps prevent slowdowns and outages.
- **Security**: Monitoring processes and resource usage can help detect unauthorized or malicious activities.
- **Proactive Incident Response**: Real-time metrics allow you to catch anomalies early, preventing minor issues from becoming major incidents.

### **Learning Objectives**

**Beginner Level (3 objectives)**

1. Understand what a process is and how to list running processes.
2. Learn how to start, stop, suspend, and resume processes.
3. Gather basic system info about CPU, memory, and disk usage.

**Intermediate Level (3 objectives)**

1. Master interactive process tools (`top`, `htop`) and advanced flags for deeper insights.
2. Identify and troubleshoot resource constraints by correlating CPU, memory, and disk usage.
3. Use background/foreground job management (`jobs`, `bg`, `fg`) in practical scenarios.

**SRE Level (3 objectives)**

1. Automate real-time monitoring of critical processes and resource metrics.
2. Conduct in-depth incident investigations involving process trees, logs, and system metrics.
3. Integrate process and resource monitoring into a broader observability framework.

### **Connecting to Previous and Future Learning**

- **Previously (Day 5):** You refined text manipulation skills for analyzing logs and output.
- **Today (Day 6):** You’ll apply those skills to observe and manage live processes, interpret system resource usage, and ensure stability.
- **Next (Day 7):** You’ll move into networking fundamentals, diagnosing latency and connectivity issues using commands like `ping`, `netstat`, and `ssh`.

---

## 📚 **Core Concepts**

Below are key concepts essential to mastering process management and system monitoring at any level.

1. **Process Basics**
   - **Beginner Analogy**: A process is like an open app on your phone—each one needs memory and CPU time.
   - **Technical Explanation**: Each running program is assigned a PID (Process ID). It may spawn child processes, has an owner, and consumes system resources (CPU, memory, I/O).
   - **SRE Application**: Overloaded or misbehaving processes can degrade service reliability. Monitoring them is essential to keep systems stable.
   - **System Impact**: A single runaway process can saturate CPU or memory, leading to outages or slow performance.

2. **Foreground vs. Background Jobs**
   - **Beginner Analogy**: Foreground jobs are like the app screen in focus; background jobs are like music streaming while you text.
   - **Technical Explanation**: Processes can run attached to a terminal (foreground) or detached (background). Commands like `bg` and `fg` manage these states.
   - **SRE Application**: SREs commonly run maintenance tasks in the background to keep terminals free. They also bring tasks to the foreground for direct interaction (e.g., debugging).
   - **System Impact**: Proper job control avoids terminal lock-ups and allows multi-tasking.

3. **Process Hierarchy**
   - **Beginner Analogy**: Just as a parent can have children, a parent process spawns child processes in a “family tree.”
   - **Technical Explanation**: Most processes originate from an init process (like `systemd`). Stopping a parent might cascade kills to children.
   - **SRE Application**: Knowing parent-child relationships is crucial for advanced debugging (e.g., zombie or orphan processes).
   - **System Impact**: Poorly managed child processes can accumulate (zombies), clutter the process table, and eventually degrade performance.

4. **System Resource Monitoring**
   - **Beginner Analogy**: Monitoring resources is like checking your car’s fuel gauge, oil level, and tire pressure.
   - **Technical Explanation**: Linux tracks CPU, RAM, disk, and network usage in real time. Tools like `ps`, `top`, `df`, and `free` measure these.
   - **SRE Application**: Quick detection of high CPU, memory exhaustion, or disk saturation is vital to prevent downtime.
   - **System Impact**: Undetected resource starvation can lead to service crashes or major performance hits.

---

## 💻 **Command Breakdown**

Below are 11 critical commands for process management and system monitoring, each presented with structured syntax tables, tiered examples, and instructional notes.

---

### **Command: ps (Process Status)**

**Command Overview:**  
`ps` provides a snapshot of running processes at a single point in time. It’s especially useful for scripting, quick verifications, and piping output to tools like `grep`.

**Syntax & Flags:**

| Flag/Option   | Syntax Example         | Description                                                   | SRE Usage Context                                     |
|---------------|------------------------|---------------------------------------------------------------|-------------------------------------------------------|
| `-a`, `-u`, `-x` | `ps aux`                 | Shows processes for all users, including those without a TTY   | Broad view of all processes across the system         |
| `-e`, `-f`    | `ps -ef`                | Similar to `aux` but in SysV format                            | Common in scripts for consistent output format        |
| `--forest`    | `ps --forest`           | Displays processes in a tree-like hierarchy                    | Quick visualization of parent-child relationships     |
| `-o`          | `ps -o pid,user,cmd`    | Custom output columns                                          | Tailored investigation, script-friendly output        |
| `--sort=-%cpu`| `ps aux --sort=-%cpu`  | Sort processes by CPU usage (descending)                       | Finding CPU hogs quickly                              |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# List all running processes in BSD style
$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1 169332  9244 ?        Ss   Mar27   0:02 /sbin/init
student    9876  2.5  1.5 241872 12345 pts/2   Sl+ 14:20   0:10 python3 script.py
# Shows process owners, IDs, CPU/memory usage, and commands
```

- 🧩 **Intermediate Example:**

```bash
# Display all processes in SysV style and filter by "nginx"
$ ps -ef | grep nginx
root     11012     1  0 Mar26 ?        00:00:05 nginx: master process /usr/sbin/nginx
www-data 11013 11012  0 Mar26 ?        00:00:10 nginx: worker process
# Demonstrates the master-worker model commonly used by Nginx
```

- 💡 **SRE-Level Example:**

```bash
# Show processes in a hierarchy and display key resource columns
$ ps --forest -o pid,user,%cpu,%mem,cmd
  PID  USER  %CPU %MEM CMD
  1001 root   0.0  0.1 /sbin/init
   1203 root   0.2  0.3  \_ /usr/lib/systemd/systemd-journald
   1500 user1 12.3 12.5 \_ java -Xmx2g -jar myapp.jar
    1501 user1  9.2 10.5     \_ GC Thread
# Quickly identifies which child threads consume the most resources
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** `ps aux` is often used for a quick process overview. Pair it with `grep` to locate specific processes.
- 🧠 **Beginner Tip:** `ps -ef` is equally common, especially in scripted environments (SysV style).

- 🔧 **SRE Insight:** Use `ps -o` with custom columns for advanced debugging or automated scripts (e.g., to parse JSON or CSV).
- 🔧 **SRE Insight:** Sorting the output (`--sort=-%cpu`, `--sort=-%mem`) helps identify potential resource hogs.

- ⚠️ **Common Pitfall:** `ps` is a snapshot in time—it can miss short-lived processes. Use real-time tools (like `top`) for ongoing monitoring.
- ⚠️ **Common Pitfall:** `ps aux | grep something` might show the `grep` process itself; use a trick like `| grep [s]omething` or `pgrep`.

- 🚨 **Security Note:** Process listings might reveal sensitive arguments (e.g., passwords in scripts).
- 💡 **Performance Impact:** `ps` usage is minimal. It’s safe for frequent checks, but for large servers with many processes, it might still generate overhead if overused in tight loops.

---

### **Command: top (Table of Processes)**

**Command Overview:**  
`top` is an interactive tool showing a real-time view of processes. It updates by default every few seconds, allowing you to spot CPU spikes, memory hogs, and quickly gauge load averages.

**Syntax & Flags:**

| Flag/Option | Syntax Example     | Description                                                     | SRE Usage Context                               |
|-------------|--------------------|-----------------------------------------------------------------|-------------------------------------------------|
| `-b`        | `top -b`          | Batch mode (non-interactive), output for scripts                | Logging or collecting snapshots                 |
| `-n`        | `top -b -n 3`     | Number of iterations in batch mode                              | Repeat snapshots for short-term data gathering  |
| `-u [user]` | `top -u nginx`     | Show processes for a specific user                              | Focus on a single service or user               |
| Interactive | Press keys like `1`, `m`, `c` | Toggle CPU cores, memory format, and command-line display in real time | On-the-fly reconfiguration of displayed data    |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Launch top in interactive mode
$ top
top - 14:25:33 up 2 days,  4:12,  2 users,  load average: 0.25, 0.15, 0.10
Tasks: 228 total,   1 running, 227 sleeping,   0 stopped,   0 zombie
%Cpu(s):  1.3 us,  0.7 sy,  0.0 ni, 97.5 id,  0.1 wa,  0.2 hi,  0.2 si,  0.0 st
MiB Mem :  16384.0 total,  12000.0 free,   2000.0 used,   1384.0 buff/cache
```

- 🧩 **Intermediate Example:**

```bash
# Focus on processes owned by "webuser"
$ top -u webuser
# Quickly isolate resource usage for a specific service user
```

- 💡 **SRE-Level Example:**

```bash
# Capture multiple snapshots in batch mode for analysis
$ top -b -n 5 -d 2 > top_log.txt
# Gathers 5 iterations, each 2 seconds apart, for offline performance review
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Press `q` to quit, `c` to show full command paths, and `1` to break down CPU usage by core.
- 🧠 **Beginner Tip:** The load average indicates how many processes are ready to run over time; compare it to your CPU core count.

- 🔧 **SRE Insight:** `top` is often the first stop during incidents for ephemeral spikes. Keep an eye on `%wa` (I/O wait) under CPU usage to diagnose disk issues quickly.
- 🔧 **SRE Insight:** Combine `top -b` with cron or scripts to gather historical usage data for trending.

- ⚠️ **Common Pitfall:** `top` sorts by CPU usage by default. High memory usage processes might not appear at the top if they aren’t using much CPU.
- ⚠️ **Common Pitfall:** Over slow SSH connections, frequent screen redraws can be disruptive.

- 🚨 **Security Note:** Like `ps`, `top` may expose sensitive process arguments.
- 💡 **Performance Impact:** `top` does consume some CPU to refresh. On high-latency links, consider `-d` to reduce refresh frequency.

---

### **Command: htop (Interactive Process Viewer)**

**Command Overview:**  
`htop` is a more feature-rich, visually appealing alternative to `top`. It offers color-coded usage bars, mouse interaction, scrolling, and filtering.

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description                                        | SRE Usage Context                               |
|-------------|----------------|----------------------------------------------------|-------------------------------------------------|
| `-d`        | `htop -d 10`   | Adjust the delay (tenths of seconds) between updates | Reduce overhead or flicker on slow connections  |
| `-u`        | `htop -u user` | Show only processes owned by `user`               | Focus on a single service or environment        |
| Interactive | Arrow keys     | Navigate process list; F3 to search; F5 for tree view | Real-time, user-friendly process exploration    |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Simply run htop if installed
$ htop
# You get an interactive, color-coded display of CPU, RAM, and processes
```

- 🧩 **Intermediate Example:**

```bash
# Filter processes to a specific user "deploy"
$ htop -u deploy
# Great for analyzing resource usage of a particular deployment
```

- 💡 **SRE-Level Example:**

```bash
# Searching for a resource hog process
# 1) Press F3 to open search
# 2) Type "java"
# 3) Press F4 to filter
# Real-time narrowing down of suspicious processes
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Press F6 to sort by different metrics (CPU, MEM, TIME, etc.).
- 🧠 **Beginner Tip:** You can kill or renice a process interactively by selecting it and pressing F9 or using F7/F8.

- 🔧 **SRE Insight:** `htop` offers a quick memory/CPU usage graph that’s often easier for new team members to interpret.
- 🔧 **SRE Insight:** Advanced filtering (F4) saves time on systems with thousands of processes.

- ⚠️ **Common Pitfall:** May not come pre-installed; install with your distro’s package manager.
- ⚠️ **Common Pitfall:** Overreliance on the mouse can be tricky over laggy SSH.

- 🚨 **Security Note:** Exposes command lines, potentially revealing credentials.
- 💡 **Performance Impact:** Similar overhead to `top`, slightly higher in some cases due to the UI.

---

### **Command: kill (Terminate a Process)**

**Command Overview:**  
`kill` sends signals to processes, typically to stop or control them. SREs use it to gracefully shut down or forcibly terminate unresponsive processes.

**Syntax & Flags:**

| Flag/Option     | Syntax Example   | Description                                               | SRE Usage Context                                    |
|-----------------|------------------|-----------------------------------------------------------|-------------------------------------------------------|
| `-l`            | `kill -l`       | List all available signals                                | Checking signal numbers/names                        |
| `-9` (SIGKILL)  | `kill -9 1234`  | Force a process to stop immediately (cannot be caught)    | Last resort for stuck or runaway processes           |
| `-HUP` (SIGHUP) | `kill -HUP 5678`| Often used to reload daemon configs without full restart  | Minimizes downtime on config changes                 |
| `-TERM` (15)    | `kill -TERM 9999`| Default signal for graceful termination                  | Standard approach for normal shutdown                |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Gracefully end a process with PID 1234
$ kill 1234
# Equivalent to kill -TERM 1234, letting the process clean up
```

- 🧩 **Intermediate Example:**

```bash
# Force-kill a stubborn process with PID 5678
$ kill -9 5678
# Use only if normal termination fails
```

- 💡 **SRE-Level Example:**

```bash
# Reload Nginx config without a full restart
$ kill -HUP $(pgrep nginx)
# Minimizes downtime while applying new configurations
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Always try `kill` (SIGTERM) before `kill -9` (SIGKILL).
- 🧠 **Beginner Tip:** Use `ps` or `top` to confirm the correct PID before killing.

- 🔧 **SRE Insight:** Overusing `kill -9` can skip important cleanup tasks, leading to file locks or orphaned resources.
- 🔧 **SRE Insight:** Some services interpret signals in special ways (e.g., SIGHUP = reload).

- ⚠️ **Common Pitfall:** Killing the wrong PID can disrupt critical services—double-check your target!
- ⚠️ **Common Pitfall:** Processes in `D` (uninterruptible sleep) can’t be killed until I/O completes.

- 🚨 **Security Note:** Accidentally killing security or monitoring agents may leave the system exposed.
- 💡 **Performance Impact:** Terminating heavy processes frees system resources but do it carefully to avoid data corruption.

---

### **Command: jobs (List Current Shell Jobs)**

**Command Overview:**  
`jobs` displays background and suspended jobs in the current shell session. It’s especially useful when you manage multiple tasks in a single terminal.

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description                                 | SRE Usage Context                      |
|-------------|----------------|---------------------------------------------|----------------------------------------|
| (none)      | `jobs`         | Lists current shell’s background/suspended jobs | Quick check of tasks in the same session |
| `-l`        | `jobs -l`      | Shows job numbers with corresponding PIDs  | More precise process control           |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Suppose you run `sleep 300 &`
$ jobs
[1]+  Running                 sleep 300 &
# Indicates job #1 is running in the background
```

- 🧩 **Intermediate Example:**

```bash
$ jobs -l
[1]+  12345 Running                 sleep 300 &
[2]-  12890 Stopped                 top
# Shows PIDs alongside job numbers
```

- 💡 **SRE-Level Example:**

```bash
# During maintenance:
$ jobs -l
[1]   29512 Running  ./backup.sh &
[2]-  29576 Running  ./logrotate.sh &
# Confirms concurrency for multiple background tasks
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Only jobs started in **this** terminal appear. Each shell keeps its own list.
- 🧠 **Beginner Tip:** Use `fg %1` to bring job #1 to the foreground.

- 🔧 **SRE Insight:** Vital for multi-tasking in a single SSH session—common during on-call emergencies.
- 🔧 **SRE Insight:** Combine with `screen`, `tmux`, or `nohup` to persist jobs beyond your logout.

- ⚠️ **Common Pitfall:** Closing the terminal or losing SSH can kill these jobs unless protected by `nohup` or a session manager.
- ⚠️ **Common Pitfall:** Easy to mix up multiple jobs if you don’t label or check them carefully.

- 🚨 **Security Note:** Attackers might hide malicious processes in the background—pay attention to suspicious jobs.
- 💡 **Performance Impact:** Background tasks still consume resources. Keep track of them to avoid overload.

---

### **Command: bg (Resume Suspended Job in Background)**

**Command Overview:**  
`bg` resumes a previously suspended job (e.g., via `Ctrl+Z`) in the background, freeing the terminal.

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description                                | SRE Usage Context                 |
|-------------|----------------|--------------------------------------------|-----------------------------------|
| `[job_spec]`| `bg %1`        | Specify which suspended job to move to bg  | Precisely manage multiple tasks   |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Suspend "top" with Ctrl+Z
$ jobs
[1]+  Stopped                 top
$ bg %1
[1]+ top &
# "top" continues in the background
```

- 🧩 **Intermediate Example:**

```bash
$ jobs
[1]   Stopped                 python3 script.py
[2]-  Stopped                 vim config.txt
$ bg %2
# Moves job #2 (vim) to background (though it's interactive)
```

- 💡 **SRE-Level Example:**

```bash
# Large data transfer suspended mid-progress
$ rsync -av /bigdata /backup
^Z  # suspended
$ bg %+
# Resumes the most recent job in background
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** `%+` refers to the most recently stopped job; `%1`, `%2` refer to specific job numbers.
- 🧠 **Beginner Tip:** Don’t background interactive editors unless you truly want them running unmonitored.

- 🔧 **SRE Insight:** Allows partial terminal usage for quick tasks while a long process runs.
- 🔧 **SRE Insight:** Pair with logs or watchers in another window to monitor progress.

- ⚠️ **Common Pitfall:** Some commands may not function well in the background if they expect continuous input.
- ⚠️ **Common Pitfall:** You might forget a background job is running, leading to unexpected load or conflicts.

- 🚨 **Security Note:** A job running in the background might display sensitive info if brought to foreground in an insecure environment.
- 💡 **Performance Impact:** No direct overhead beyond the job’s normal resource consumption.

---

### **Command: fg (Resume Job in Foreground)**

**Command Overview:**  
`fg` brings a background or stopped job to the foreground, allowing interactive control again.

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description                                    | SRE Usage Context                 |
|-------------|----------------|------------------------------------------------|-----------------------------------|
| `[job_spec]`| `fg %2`        | Specify which job to foreground               | Interact with previously backgrounded processes |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
$ jobs
[1]+  Running   tail -f /var/log/syslog &
$ fg %1
tail -f /var/log/syslog
# Now it's in the foreground
```

- 🧩 **Intermediate Example:**

```bash
# If you have multiple background tasks
$ fg %2
# Brings job #2 to the foreground for interaction or to terminate
```

- 💡 **SRE-Level Example:**

```bash
# A maintenance script is running in background
$ jobs -l
[1]- 24820 Running backup.sh &
[2]+ 24830 Stopped metrics_collector.sh
# Move metrics_collector.sh to foreground for an interactive check
$ fg %2
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** If you omit `%job_id`, `fg` typically defaults to the most recent job.
- 🧠 **Beginner Tip:** Use `jobs -l` to see both job ID and PID.

- 🔧 **SRE Insight:** Useful for graceful termination or quick debug logs in the middle of large background tasks.
- 🔧 **SRE Insight:** Minimizes guesswork if you’re juggling multiple jobs in a single shell session.

- ⚠️ **Common Pitfall:** Foregrounding a daemon-like process is unusual—daemons typically run under system managers instead.
- ⚠️ **Common Pitfall:** If the job was started in another shell, `fg` won’t work. Each shell manages its own jobs.

- 🚨 **Security Note:** Foregrounding an application might reveal logs or sensitive output on-screen.
- 💡 **Performance Impact:** No specific overhead, just changes your interaction mode.

---

### **Command: uname (Unix Name)**

**Command Overview:**  
`uname` reports basic system information, including kernel name and version. It’s often used to verify kernel updates, architecture, or distribution details (when combined with other commands).

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description                                                      | SRE Usage Context                                   |
|-------------|----------------|------------------------------------------------------------------|-----------------------------------------------------|
| `-a`        | `uname -a`     | Print all system info (kernel, machine, etc.)                    | Quick baseline of system identity                   |
| `-r`        | `uname -r`     | Kernel release version                                           | Verify kernel patch levels, check known issues      |
| `-m`        | `uname -m`     | Machine hardware architecture (e.g., x86_64, aarch64)            | Confirm correct binaries or containers for arch     |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
$ uname -a
Linux server1 5.4.0-81-generic #91-Ubuntu SMP x86_64 x86_64 x86_64 GNU/Linux
# Displays kernel, version, architecture, and OS details
```

- 🧩 **Intermediate Example:**

```bash
# Retrieve only the kernel version
$ uname -r
5.4.0-81-generic
# Handy for checking relevant kernel patches
```

- 💡 **SRE-Level Example:**

```bash
# Automate architecture checks in a script
arch=$(uname -m)
echo "Architecture detected: $arch"
# E.g., used for pulling correct container images or binaries
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** To get distribution info (e.g., Ubuntu vs. CentOS), use `lsb_release -a` or check `/etc/os-release`.
- 🧠 **Beginner Tip:** `uname -a` is a quick one-stop for kernel-level data but lacks distro specifics.

- 🔧 **SRE Insight:** Knowing the exact kernel version is vital when diagnosing performance or security vulnerabilities.
- 🔧 **SRE Insight:** In CI/CD pipelines, `uname -m` can ensure you deploy the correct architecture-specific builds.

- ⚠️ **Common Pitfall:** On containerized environments, `uname` might reflect the host kernel, which can be misleading.
- ⚠️ **Common Pitfall:** Relying solely on `uname` for OS info is incomplete—combine it with other checks.

- 🚨 **Security Note:** Ensure you’re running patched kernels for known CVEs; kernel version is critical for scanning vulnerabilities.
- 💡 **Performance Impact:** `uname` is negligible in resource usage.

---

### **Command: df (Disk Filesystem)**

**Command Overview:**  
`df` shows disk space usage by filesystem. Keeping an eye on free space is crucial to avoid abrupt service failures when logs or data partitions fill up.

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description                                       | SRE Usage Context                                  |
|-------------|----------------|---------------------------------------------------|----------------------------------------------------|
| `-h`        | `df -h`        | Human-readable output (K, M, G)                   | Quick overview of disk usage                       |
| `-T`        | `df -T`        | Displays filesystem type (ext4, xfs, etc.)        | Debugging performance differences across FS types  |
| `-i`        | `df -i`        | Shows inode usage instead of block usage          | Diagnosing “No space left” errors caused by inode exhaustion |

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
# Check filesystem types and usage
$ df -hT
Filesystem     Type   Size  Used Avail Use% Mounted on
/dev/sda1      ext4    20G   13G  6.5G  67% /
/dev/sdb1      xfs    100G   45G   55G  45% /data
tmpfs          tmpfs  2.0G  128M  1.9G   7% /run
```

- 💡 **SRE-Level Example:**

```bash
# Monitor disk usage every 5 seconds to detect rapid log growth
$ watch -n 5 df -h
# Helps catch disk-consuming processes in real-time
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Check “Use%” to see how close a partition is to full. Don’t let it get above ~80% without a plan.
- 🧠 **Beginner Tip:** `df` only gives filesystem-level info. Use `du` to dig deeper into which folders/files are large.

- 🔧 **SRE Insight:** Deleting large files might not free space if a process is still holding the file handle—use `lsof | grep deleted`.
- 🔧 **SRE Insight:** For cloud deployments, consider auto-scaling or provisioning more volumes if usage grows.

- ⚠️ **Common Pitfall:** Network shares (NFS, SMB) can show stale or incorrect data if the server is unreachable.
- ⚠️ **Common Pitfall:** Running out of inodes can show 0% usage but still yield “disk full” errors.

- 🚨 **Security Note:** A full partition for logging can break auditing or intrusion detection if logs can’t be written.
- 💡 **Performance Impact:** `df` is lightweight but can hang if network filesystems are down.

---

### **Command: du (Disk Usage)**

**Command Overview:**  
`du` estimates file or directory space usage, pinpointing which directories or files consume the most space.

**Syntax & Flags:**

| Flag/Option       | Syntax Example            | Description                                             | SRE Usage Context                                      |
|-------------------|---------------------------|---------------------------------------------------------|--------------------------------------------------------|
| `-h`              | `du -h /var/log`         | Human-readable output                                   | Quickly identify large logs/folders                    |
| `-s`              | `du -sh /home/user`      | Show only the total size                                | Overview of a directory’s total usage                  |
| `--max-depth=N`   | `du -h --max-depth=1 .`  | Limit how deep to recurse into subdirectories           | Quickly find which subdirectories are largest          |
| `--exclude=pattern` | `du -h --exclude='*.tmp' /data` | Skip certain files/folders               | Avoid irrelevant large files (temp, backups, etc.)     |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Check size of current directory
$ du -sh .
258M    .
```

- 🧩 **Intermediate Example:**

```bash
# Compare subdirectory sizes in /var/log
$ du -h --max-depth=1 /var/log | sort -h
4.0K  /var/log/apt
12M   /var/log/syslog
1.2M  /var/log/journal
...
```

- 💡 **SRE-Level Example:**

```bash
# Identify the largest subdirectories in /data excluding backups
$ du -h --max-depth=2 --exclude='backup*' /data | sort -h | tail -5
2.3G  /data/logs
1.2G  /data/application/cache
4.5G  /data
# Useful for investigating growth patterns in production
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Pair with `sort -h` to easily see largest directories at the bottom or top.
- 🧠 **Beginner Tip:** `-s` provides just a summary, reducing output clutter.

- 🔧 **SRE Insight:** Rapidly filling partitions often point to logs or temp directories—run `du` on them first in an incident.
- 🔧 **SRE Insight:** Combine with `find` or a “time-based” approach (e.g., large, old files) for deeper forensics.

- ⚠️ **Common Pitfall:** Large directories with many files can make `du` slow. Use `--max-depth` for a quick top-level overview.
- ⚠️ **Common Pitfall:** If symbolic links are involved, ensure you understand how `du` handles them (`-L` vs `-P`).

- 🚨 **Security Note:** Large, unexpected files might indicate a data exfiltration attempt or unauthorized usage.
- 💡 **Performance Impact:** On enormous directories, `du` can generate high I/O. Schedule it in off-peak hours if possible.

---

### **Command: free (Memory Usage)**

**Command Overview:**  
`free` displays total and used physical RAM and swap. It helps confirm memory availability and detect potential out-of-memory (OOM) risks.

**Syntax & Flags:**

| Flag/Option | Syntax Example    | Description                                            | SRE Usage Context                                     |
|-------------|-------------------|--------------------------------------------------------|-------------------------------------------------------|
| `-h`        | `free -h`         | Human-readable memory usage                            | Quick, clear snapshot of RAM usage                    |
| `-s N`      | `free -s 5 -h`    | Repeatedly display memory usage every N seconds        | Tracking memory usage trends in short bursts          |
| `-t`        | `free -t`         | Include total line at the end                          | Summarize overall memory usage                        |

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
# Observe memory usage every 5 seconds
$ free -h -s 5
              total   used   free  shared  buff/cache  available
Mem:           15Gi   6.2Gi  5.3Gi 300Mi    3.5Gi       7.5Gi
Swap:         4.0Gi   0B     4.0Gi
...
```

- 💡 **SRE-Level Example:**

```bash
# Incorporate memory checks in a diagnostic loop
while true; do
  date
  free -m | grep Mem
  sleep 10
done
# Logs memory usage every 10 seconds for correlation with other metrics
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Focus on the “available” column. Linux uses extra memory for caching, so “free” alone can be misleading.
- 🧠 **Beginner Tip:** High “buff/cache” is normal. It speeds up disk access and is reclaimed when apps need memory.

- 🔧 **SRE Insight:** Monitoring swap usage is key. If the system is actively swapping, performance often degrades.
- 🔧 **SRE Insight:** Use with continuous sampling to detect memory leaks or sudden spikes.

- ⚠️ **Common Pitfall:** `free` doesn’t show which processes use memory—use `ps aux --sort=-%mem` or specialized tools (e.g., `smem`) for per-process details.
- ⚠️ **Common Pitfall:** On container hosts, container cgroups might mask actual memory usage if not accounted for at the host level.

- 🚨 **Security Note:** Critical security processes might be killed by OOM if memory is not properly monitored.
- 💡 **Performance Impact:** `free` is negligible overhead. Continuous sampling is still minimal but should be combined with a real monitoring system.

---

## 🛠️ **System Effects**

1. **Filesystem & Metadata**  
   - Commands like `df` and `du` read filesystem metadata to show space usage. Deletion without closing file handles can lead to misleading readings until the process is terminated or the file is truly released.
2. **System Resources**  
   - Monitoring tools (`top`, `htop`, `ps`) each consume a small amount of CPU. In large environments, repeated invocations can add noticeable overhead.
3. **Security Implications**  
   - Exposing command lines (e.g., via `ps`, `top`, `htop`) may reveal secrets or passwords.  
   - Killing critical security or logging processes can create vulnerabilities.
4. **Monitoring Visibility**  
   - Real-time tools like `top` or `htop` provide immediate insight but must be used continuously (or via automation) to catch transient events.  
   - Logging snapshots with `top -b`, `df`, or `free` helps build historical data for trend analysis.

---

## 🎯 **Hands-On Exercises**

### **Beginner Exercises (3)**

1. **Basic Process Inspection and Termination**
   - Run `ps aux` to view processes on your system. Identify one process owned by your user.
   - Start a dummy process: `sleep 300 &`. Find its PID and gracefully terminate it with `kill <PID>`.

2. **Foreground vs. Background**
   - Execute `top`. Press `Ctrl+Z` to suspend it.
   - Use `jobs` to confirm it’s stopped, then `bg` to resume it in the background.
   - Finally, `fg` to bring it forward and press `Ctrl+C` to quit.

3. **Disk and Memory Snapshot**
   - Run `df -h` to see which partition is most filled.
   - Run `free -h` and note total, used, and free (available) memory.
   - Discuss how you might address a disk near 90% usage (e.g., cleaning logs, archiving data).

### **Intermediate Exercises (3)**

1. **Resource Hog Identification**
   - Start a CPU-intensive process, for example:

     ```bash
     sha256sum /dev/zero
     ```

   - Open a second terminal and use `top` or `htop` to see the CPU usage. Notice the high CPU.
   - Terminate the process with `kill`. Verify with `ps` or `top` that it’s gone.

2. **Investigating Large Logs**
   - Navigate to `/var/log` (or another log directory).
   - Use `du -h --max-depth=1` to see which log subdirectories are largest.
   - Sort them (`sort -h`) and identify potential culprits for disk usage.

3. **Background Job Management**
   - Start a command like `sleep 600` in foreground; press `Ctrl+Z` to suspend.
   - Use `bg %1` to resume it in the background; confirm with `jobs`.
   - Bring it back with `fg %1`, then terminate with `Ctrl+C`.

### **SRE-Level Exercises (3)**

1. **Automated Disk Monitoring Script**
   - Write a small script that runs `df -h` and `du -sh /var/log` every minute for 5 iterations. Log the output to a file.
   - Simulate disk usage growth (e.g., copy some large files).  
   - Review your log file to see changes over time and consider how to automate alerts if usage crosses a threshold.

2. **Memory Stress and Monitoring**
   - Use a memory stress tool (e.g., `stress --vm 1 --vm-bytes 512M --timeout 60s`) to artificially load memory.
   - In parallel, run `free -h -s 5` or `top` to watch how memory usage changes in real time.
   - Observe whether the system dips into swap or triggers any OOM warnings (check `dmesg`).

3. **Process Tree & Child Process Analysis**
   - Run a service that spawns multiple child processes (e.g., `nginx` or a `node` cluster).
   - Use `ps --forest` or `pstree` to observe the hierarchy. Then use `lsof -p <PID>` to see open files/ports.
   - Document which children are worker threads and note any potential security or performance concerns (e.g., too many worker processes).

---

## 📝 **Quiz Questions**

### **Beginner Level (3-4 Questions)**

1. **MCQ**: Which command lists all processes in a BSD-style format?  
   A) `ps aux`  
   B) `jobs`  
   C) `free -h`  
   D) `df -h`  

2. **Fill in the Blank**: To see the currently running jobs in your shell, you would type `__________`.

3. **Short Answer**: Explain the difference between `kill` (SIGTERM) and `kill -9` (SIGKILL).

4. **True/False**: `fg` is used to send a running process to the background.

### **Intermediate Level (3-4 Questions)**

1. **MCQ**: Which command provides a real-time, interactive view of processes and allows color-coded output with easier navigation?  
   A) `top -b`  
   B) `htop`  
   C) `ps -ef`  
   D) `jobs`  

2. **Fill in the Blank**: To resume job number 3 in the background, you would type `__________ %3`.

3. **Scenario**: You see your `/var` partition is 90% full. Which two commands would help you identify the largest directories or files?

4. **True/False**: `ps aux --sort=-%cpu | head -10` will show you the processes that consume the most CPU at the top.

### **SRE Level (3-4 Questions)**

1. **Scenario**: You suspect a single Java process is leaking memory. Name two commands to confirm this suspicion and what you’d look for in their outputs.
2. **Short Answer**: Why might you run `iostat` or `vmstat` alongside `top` when investigating high load?
3. **MCQ**: Which command combination continuously records process snapshots for historical analysis?  
   A) `kill -9 $(pgrep -u root)`  
   B) `top -b -n 1`  
   C) `watch -n 2 ps aux`  
   D) `jobs -l && bg %1`  
4. **True/False**: Even if `df -h` shows plenty of free space, your system can run out of inodes and throw a "No space left on device" error.

---

## 🚧 **Troubleshooting Scenarios**

Below are three realistic issues, each with symptoms, causes, diagnostics, resolutions, and prevention tips.

---

### **1. Zombie Processes After a Crash**

- **Symptoms**: `ps aux` shows multiple processes in `Z` (zombie) state. System performance might be fine, but the process table is cluttered.
- **Likely Cause**: Parent processes failed to reap child processes after they exited.
- **Diagnostics**:
  - Use `ps --forest` or `pstree` to find the parent.  
  - Verify if the parent is alive or stuck.
- **Resolution**:
  - Restart or gracefully kill the parent process so it can reap zombies.  
  - If it’s a critical service, schedule a controlled restart to avoid downtime.
- **Prevention**:
  - Ensure properly written daemons that wait on child processes.  
  - Modern init systems like `systemd` typically handle zombie reaping automatically.

---

### **2. High Load, Low CPU Usage**

- **Symptoms**: System load average is high (e.g., above the number of CPU cores), but `top` shows low CPU utilization. Many processes in `D` state (uninterruptible sleep).
- **Likely Cause**: I/O bottleneck—processes are waiting on disk or network storage operations.
- **Diagnostics**:
  - Check disk I/O with `iostat -x 2 5`.  
  - Look at `%wa` (I/O wait) in `top`.  
  - Confirm if remote volumes (NFS) are slow or offline.
- **Resolution**:
  - Investigate the underlying storage or network.  
  - Optimize queries, upgrade disk performance, or fix NFS issues.  
  - Reduce concurrency if the system is saturating I/O.
- **Prevention**:
  - Monitor disk usage and I/O wait.  
  - Scale storage solutions and employ caching or load balancing to avoid single bottlenecks.

---

### **3. Disk Full Despite File Deletions**

- **Symptoms**: `df -h` still shows high usage even after large files are removed. Services complain about "No space left on device."
- **Likely Cause**: A process is holding open file descriptors on deleted files.
- **Diagnostics**:
  - Use `lsof | grep deleted` to see which processes still reference removed files.
- **Resolution**:
  - Terminate or restart the process to release the handles.
- **Prevention**:
  - Use proper log rotation (e.g., `logrotate`) so processes close old files.  
  - Regularly check for “deleted but open” files if the system sees frequent large file creation/deletion.

---

## ❓ **FAQ**

### **Beginner Level (3)**

1. **Q:** How do I stop a command running in my terminal right now without suspending it?  
   **A:** Press `Ctrl+C` to send an interrupt signal (SIGINT), which typically ends the process immediately.

2. **Q:** What does `jobs` do if I open a new shell?  
   **A:** `jobs` only shows processes in the **current** shell. A new shell starts with no known background or suspended tasks.

3. **Q:** Does `top` show the entire command or just the binary name by default?  
   **A:** By default, `top` may show just the binary name. Press `c` to toggle full command lines in interactive mode.

---

### **Intermediate Level (3)**

1. **Q:** Can I run `top` in a script?  
   **A:** Yes. Use `top -b -n <iterations>` for batch (non-interactive) mode. This is ideal for logging or automated performance snapshots.

2. **Q:** Why does my disk appear full even though I freed space by deleting files?  
   **A:** A running process might still have those files open. Use `lsof | grep deleted` to find which process is hanging onto that data.

3. **Q:** How can I see each CPU core’s usage separately in `top`?  
   **A:** While in `top`, press `1`. It toggles per-core CPU statistics.

---

### **SRE Level (3)**

1. **Q:** How do I protect critical processes from being killed by the OOM killer?  
   **A:** Adjust their OOM score. For example:  

   ```bash
   echo -1000 > /proc/<PID>/oom_score_adj
   ```

   Lower values make them less likely to be killed.

2. **Q:** What’s the difference between `ps aux | grep <process>` and `pgrep <process>`?  
   **A:** `pgrep` returns only PIDs of matching processes, avoiding listing the `grep` command itself. It’s more script-friendly and less error-prone.

3. **Q:** How do I investigate high load that isn’t caused by CPU usage?  
   **A:** Check `wa` (I/O wait) with `top` or `vmstat` and use `iostat` to inspect disk usage. Processes stuck in `D` state often indicate an I/O bottleneck.

---

## 🔥 **SRE Scenario: Investigating Sudden High Memory Usage**

**Incident Context**: An alert triggers: “Memory usage at 85% and climbing” on a critical web server. Users report slower response times, but no errors yet.

**Step-by-Step Analysis**:

1. **Check Overall Memory**  

   ```bash
   free -h
   ```

   *Reasoning:* Confirm if the alert is valid; see how much is actually available vs. cache.

2. **Identify Top Memory Consumers**  

   ```bash
   ps aux --sort=-%mem | head -10
   ```

   *Reasoning:* Sort processes by memory usage; see if one process stands out.

3. **Check Real-Time Activity**  

   ```bash
   top
   ```

   *Reasoning:* Observe if memory usage is still climbing. Watch for swap usage or OOM risk.

4. **Focus on Suspect Process**  

   ```bash
   lsof -p <PID> | grep -i 'tmp\|log'
   ```

   *Reasoning:* See if the process is creating/holding large files, logs, or caches.

5. **Attempt Graceful Restart**  

   ```bash
   systemctl restart myservice
   ```

   *Reasoning:* Release memory if it’s a leak or runaway. If memory usage doesn’t drop, proceed further.

6. **Examine Logs**  

   ```bash
   grep -i 'oom\|error' /var/log/syslog
   ```

   *Reasoning:* Check if the OOM killer is looming or if the service logs critical issues.

7. **Plan Longer-Term Fix**  
   - Add memory if usage is legitimate.  
   - Patch or reconfigure the leaking process.  
   - Introduce monitoring that triggers earlier warnings.  
   *Reliability Principle:* Combining immediate mitigation (restart or kill) with root-cause resolution ensures stable, long-term operations.

---

## 🧠 **Key Takeaways**

1. **Command Summary**  
   - **`ps`, `top`, `htop`**: Foundation of process visibility  
   - **`kill`**: Send signals to gracefully or forcefully stop processes  
   - **`jobs`, `bg`, `fg`**: Control foreground/background tasks in your current shell  
   - **`uname`, `df`, `du`, `free`**: Core system and resource usage info  

2. **Operational Insights**  
   - **Proactive Monitoring**: Quick detection of CPU, memory, or disk anomalies is critical for reliability.  
   - **Signal Discipline**: Always attempt graceful kills before resorting to `-9`.  
   - **Disk & Memory**: Overfull disks and memory leaks are leading causes of service disruptions.

3. **Best Practices**  
   - **Use `top -b` or `ps` in scripts** for repeatable snapshots and logging.  
   - **Keep logs from saturating disk**—consider log rotation and routine `df/du` checks.  
   - **Automate memory/disk alerts** in production to catch issues before they become critical.

4. **Preview of Next Topic**  
   - Next, we’ll tackle **networking basics**—diagnosing connectivity, analyzing ports, and using commands like `ping`, `netstat`, and `ss` for deeper reliability in distributed systems.

---

## 📚 **Further Learning Resources**

### 🔍 **Beginner (3)**  

1. **Linux Journey - Process Utilization**  
   **Link**: [https://linuxjourney.com/lesson/process-utilization](https://linuxjourney.com/lesson/process-utilization)  
   **Description**: Interactive tutorials covering basic process concepts.  
   **Beginner Application**: Builds foundational understanding of how processes work in Linux.

2. **Ubuntu Official Documentation - Basic Commands**  
   **Link**: [https://help.ubuntu.com/community/UsingTheTerminal](https://help.ubuntu.com/community/UsingTheTerminal)  
   **Description**: Introduces essential terminal usage.  
   **Beginner Application**: Perfect for first-time users exploring Linux commands.

3. **The Linux Command Line (William Shotts, Free PDF)**  
   **Link**: [http://linuxcommand.org/tlcl.php](http://linuxcommand.org/tlcl.php)  
   **Description**: A complete beginner’s guide to Linux CLI.  
   **Beginner Application**: Excellent resource for in-depth learning with practical examples.

### 🧩 **Intermediate (3)**  

1. **DigitalOcean Tutorials: Process Management**  
   **Link**: [https://www.digitalocean.com/community/tutorials/tag/linux-process](https://www.digitalocean.com/community/tutorials/tag/linux-process)  
   **Description**: Step-by-step guides for advanced process viewing, signals, and job control.  
   **Operational Connection**: Great for honing day-to-day sysadmin and SRE tasks.

2. **Linux Performance Tools by Brendan Gregg**  
   **Link**: [http://www.brendangregg.com/linuxperf.html](http://www.brendangregg.com/linuxperf.html)  
   **Description**: Focuses on performance analysis and troubleshooting techniques.  
   **Operational Connection**: Invaluable for diagnosing complex CPU, memory, or I/O issues in real-world systems.

3. **Red Hat SysAdmin Skills**  
   **Link**: [https://www.redhat.com/sysadmin](https://www.redhat.com/sysadmin)  
   **Description**: Articles and case studies on Linux administration, process management, and monitoring.  
   **Operational Connection**: Provides applied knowledge for intermediate-level SREs.

### 💡 **SRE-Level (3)**  

1. **Google SRE Book - Handling Overload**  
   **Link**: [https://sre.google/sre-book/handling-overload/](https://sre.google/sre-book/handling-overload/)  
   **Description**: Strategies for dealing with system overloads and load shedding.  
   **Reliability Engineering Skill**: Teaches how to manage resource-intensive processes and prevent meltdown under heavy load.

2. **Netflix TechBlog: Linux Performance Tools**  
   **Link**: [https://netflixtechblog.com/](https://netflixtechblog.com/) (search “Linux Performance Tools”)  
   **Description**: Deep dives into real-world performance troubleshooting.  
   **Reliability Engineering Skill**: Learn how at-scale companies debug major performance or resource anomalies.

3. **System Performance: Enterprise and the Cloud (Brendan Gregg)**  
   **Link**: [http://www.brendangregg.com/index.html](http://www.brendangregg.com/index.html)  
   **Description**: Comprehensive coverage of advanced monitoring, profiling, and tuning.  
   **Reliability Engineering Skill**: Ideal for SREs seeking mastery in diagnosing CPU, memory, and file system interactions at scale.

---

Congratulations! You have completed **Day 6** of your Linux SRE training. With solid foundations in process management and system monitoring, you’re well-equipped to ensure stable, high-performance services. Next up: **networking essentials**—where you’ll learn to diagnose connectivity problems and maintain robust distributed systems.
