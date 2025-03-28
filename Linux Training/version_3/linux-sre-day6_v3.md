# 🚀 **Day 6: Process Management and System Monitoring**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 5:**

Yesterday, you enhanced your Linux toolkit with intermediate text and data manipulation commands such as `sed`, `awk`, `sort`, `uniq`, and `wc`, along with advanced pipe usage. These powerful text processing tools allow you to transform, extract, and analyze data from files and command outputs.

### 📅 **Today's Topics and Importance:**

Today, we'll explore **process management and system monitoring** - fundamental skills for any Linux user, and especially critical for SRE work. Understanding how to view, control, and manage processes ensures your Linux system runs smoothly and efficiently. These skills enable you to:

- Monitor system health and resource usage
- Identify performance bottlenecks
- Troubleshoot application issues
- Manage system resources effectively
- Respond quickly to incidents

### 🎯 **Learning Objectives:**

By the end of Day 6, you will be able to:

- View running processes with `ps`, `top`, and `htop`
- Control processes with commands such as `kill`, `jobs`, `bg`, and `fg`
- Gather system information using commands like `uname`, `df`, `du`, and `free`
- Apply these skills to diagnose and resolve common system issues

---

## 📚 **Core Concepts Explained**

### **Understanding Processes in Linux**

In Linux, a process is an instance of a running program. Each process:

- Has a unique **Process ID (PID)** for identification
- Is owned by a specific user
- Uses system resources (CPU, memory, etc.)
- Has a parent process (forming a hierarchical structure)
- Runs either in the foreground (interactive) or background (non-interactive)

> **Beginner's Note:** Think of processes like tasks your computer is handling. Just as you might be juggling multiple tasks (writing an email, listening to music, downloading a file), your computer manages multiple processes simultaneously.

### **Process States**

Processes can be in different states:

- **Running**: Currently executing on CPU
- **Sleeping**: Waiting for a resource or event
- **Stopped**: Suspended (paused)
- **Zombie**: Process has completed but still has an entry in the process table

> **Intermediate Insight:** Zombie processes (shown as "Z" in process listings) indicate parent processes not properly handling child termination. While not consuming significant resources, numerous zombies can indicate application bugs.

### **System Resources**

Monitoring system resources is essential for maintaining performance:

- **CPU usage**: Processing power utilization
- **Memory usage**: RAM and swap space
- **Disk space**: Storage capacity and I/O operations
- **Network**: Connectivity and bandwidth

> **SRE Perspective:** Resource monitoring forms the foundation of reliability engineering. Proactive monitoring helps identify trends before they become incidents, while reactive monitoring helps quickly diagnose issues during outages.

---

## 💻 **Commands to Learn (Detailed)**

### **1. Viewing Processes (`ps`, `top`, `htop`)**

#### **`ps` – Process Status**

**Purpose**: Display a snapshot of current processes.

**Basic Syntax:**

```bash
ps [options]
```

**Beginner Examples:**

View your own processes:

```bash
$ ps
  PID TTY          TIME CMD
 1234 pts/0    00:00:00 bash
 5678 pts/0    00:00:00 ps
```

View all processes (most common usage):

```bash
$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.2 168940 11892 ?        Ss   Apr07   0:27 /sbin/init
alice     1234  0.1  0.5 157952 22668 pts/0    Ss   10:21   0:02 bash
```

> **Beginner's Note:** `ps aux` is one of the most useful commands you'll run. The columns show the user who owns the process, the PID, CPU and memory usage, and the command that was run.

**Intermediate Options:**

```bash
ps -ef         # Another format showing PPID (parent PID)
ps -u username # Show processes for a specific user
ps --forest    # Show process hierarchy as a tree
ps -o pid,ppid,cmd # Customize output fields
```

**Advanced Examples for SREs:**

Find all processes related to a specific application:

```bash
$ ps aux | grep nginx
root      1234  0.0  0.1  10256  8512 ?        Ss   Mar05   0:01 nginx: master process
nginx     1235  0.0  0.1  10256  8384 ?        S    Mar05   0:02 nginx: worker process
```

Sort processes by memory usage:

```bash
ps aux --sort=-%mem | head -10
```

#### **`top` – Interactive Process Viewer**

**Purpose**: Display real-time, dynamic view of system processes.

**Basic Syntax:**

```bash
top [options]
```

**Key sections in the `top` display:**

1. Summary area: System uptime, load average, task counts
2. CPU statistics: User, system, idle percentages
3. Memory usage: Total, used, free memory and swap
4. Process list: Running processes sorted by resource usage

**Basic Interactive Commands:**

- `q`: Quit
- `h`: Show help
- Space: Refresh display immediately

> **Beginner's Note:** `top` refreshes automatically (usually every 3 seconds) and shows you what's happening right now, unlike `ps` which shows a single snapshot.

**Intermediate Interactive Commands:**

- `k`: Kill a process (prompts for PID)
- `r`: Renice a process (change priority)
- `f`: Select fields to display
- `o`: Change sort order
- `1`: Toggle individual CPU core stats
- `m`: Toggle memory display format
- `c`: Show full command path

**Example output:**

```
top - 14:35:42 up 7 days, 23:32, 1 user, load average: 0.12, 0.14, 0.10
Tasks: 213 total,   1 running, 212 sleeping,   0 stopped,   0 zombie
%Cpu(s):  1.7 us,  0.3 sy,  0.0 ni, 97.8 id,  0.1 wa,  0.0 hi,  0.1 si,  0.0 st
MiB Mem :  15993.0 total,   8234.7 free,   4726.5 used,   3031.8 buff/cache
MiB Swap:   4096.0 total,   4096.0 free,      0.0 used.  10828.5 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
 1234 webapp    20   0 4120416 506892  12056 S   2.7   3.1   14:23.45 java
 4567 mysql     20   0 1250024 362548  13016 S   0.7   2.2    5:42.31 mysqld
 8901 nginx     20   0   10256   8384   3224 S   0.3   0.1    0:02.17 nginx
```

> **SRE Perspective:** During incidents, `top` is often your first tool to identify resource contention. Pay close attention to:
>
> - Load average: Values consistently over your CPU count suggest overload
> - High wa% (wait) in CPU stats: Indicates I/O bottlenecks
> - High memory usage with low available memory: Potential memory pressure
> - Specific processes consuming abnormal resources: Application issues

#### **`htop` – Enhanced Interactive Process Viewer**

**Purpose**: Provides a more user-friendly and feature-rich alternative to `top`.

**Basic Usage:**

```bash
htop
```

**Key advantages over `top`:**

- Color-coded output for better readability
- Mouse support for easier navigation
- Horizontal and vertical scrolling
- Visual CPU, memory, and swap usage meters
- Built-in command filtering and tree view

> **Beginner's Note:** If `htop` is not installed on your system, you can usually install it with `sudo apt install htop` (Debian/Ubuntu) or `sudo yum install htop` (RHEL/CentOS).

**Example output:**

```
  CPU[|||||                                                            5.0%]
  Mem[||||||||||||||||||                                         2.42G/15.6G]
  Swp[                                                           0K/4.00G]

  PID USER      PRI  NI  VIRT   RES   SHR S CPU% MEM%   TIME+  Command
 1234 webapp     20   0 4.02G 494M  12M S  2.7  3.1 14:23.45 java -Xmx2g -jar app.jar
 4567 mysql      20   0 1.19G 354M  12M S  0.7  2.2  5:42.31 /usr/sbin/mysqld
 8901 nginx      20   0  10M  8.2M 3.1M S  0.3  0.1  0:02.17 nginx: worker process
```

> **Intermediate Insight:** `htop` offers sophisticated filtering with the `/` key to quickly find specific processes in complex environments with thousands of processes.

### **2. Controlling Processes (`kill`, `jobs`, `bg`, `fg`)**

#### **`kill` – Send Signals to Processes**

**Purpose**: Terminate processes or send other control signals.

**Basic Syntax:**

```bash
kill [options] PID
```

**Beginner Examples:**

Terminate a process gracefully:

```bash
kill 1234
```

Force-terminate an unresponsive process:

```bash
kill -9 1234
```

> **Beginner's Note:** Always try regular `kill` first before resorting to `kill -9`. Think of `kill` as asking a program to close properly, while `kill -9` is like forcibly shutting it down.

**Common signals:**

- `SIGTERM` (15): Default signal, graceful termination
- `SIGKILL` (9): Immediate termination (cannot be caught or ignored)
- `SIGHUP` (1): Hang up signal, often used to reload configurations
- `SIGINT` (2): Interrupt (like pressing Ctrl+C)

List all available signals:

```bash
kill -l
```

**Advanced Usage for SREs:**

Reload a service configuration without restarting:

```bash
kill -HUP $(pgrep nginx | head -1)
```

Use `pkill` or `killall` to kill processes by name:

```bash
pkill firefox    # Kill all firefox processes
killall java     # Same purpose, different command
```

> **SRE Perspective:** Signals are powerful for controlling services. During incidents, using the right signal matters:
>
> - `SIGTERM` (default) allows processes to close connections and flush data
> - `SIGKILL` is a last resort that may cause data corruption or connection issues
> - `SIGHUP` is often used to reload configurations without downtime

#### **`jobs`, `bg`, `fg` – Manage Shell Jobs**

**Purpose**: Control processes started from your current terminal session.

**Basic Commands:**

- `jobs`: List background and suspended jobs
- `bg [%job_id]`: Resume a suspended job in the background
- `fg [%job_id]`: Bring a background job to the foreground

**Common keyboard shortcuts:**

- `Ctrl+Z`: Suspend the current foreground process
- `Ctrl+C`: Terminate the current foreground process

**Beginner Example:**

Run a command, suspend it, and move it to background:

```bash
$ sleep 100     # Start a process that sleeps for 100 seconds
^Z              # Press Ctrl+Z to suspend it
[1]+  Stopped   sleep 100

$ bg            # Resume in background
[1]+ sleep 100 &

$ jobs          # List jobs
[1]+  Running   sleep 100 &

$ fg            # Bring back to foreground
sleep 100
^C              # Press Ctrl+C to terminate
```

> **Beginner's Note:** These commands only work for processes started in your current terminal session. They won't affect processes started elsewhere.

**Advanced Usage with `nohup`:**

Run a process that continues even if you log out:

```bash
$ nohup ./long_running_script.sh > output.log 2>&1 &
[1] 1234
```

> **Intermediate Insight:** The `&` at the end of a command runs it in the background immediately. This is useful for starting processes that don't need interactive input.

> **SRE Perspective:** For production systems, prefer service managers like `systemd` over `nohup` and `&` for long-running processes. They provide better logging, restart policies, and dependency management.

### **3. System Information and Resource Monitoring**

#### **`uname` – System Information**

**Purpose**: Display system information including kernel version, architecture, and hostname.

**Basic Syntax:**

```bash
uname [options]
```

**Common Options:**

- `-a`: All information
- `-r`: Kernel release
- `-m`: Machine hardware architecture
- `-n`: System hostname

**Examples:**

```bash
$ uname -a
Linux server1 5.4.0-81-generic #91-Ubuntu SMP Thu Jul 15 19:09:17 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux

$ uname -r
5.4.0-81-generic
```

> **Beginner's Note:** This command is useful when you need to know what version of Linux you're running, especially when following instructions that might be version-specific.

#### **`df` – Disk Space Usage**

**Purpose**: Report filesystem disk space usage.

**Basic Syntax:**

```bash
df [options]
```

**Common Options:**

- `-h`: Human-readable sizes (GB, MB)
- `-T`: Show filesystem type
- `-i`: Show inode information instead of block usage

**Examples:**

```bash
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   32G   18G  64% /
/dev/sda2       100G   45G   55G  45% /var
/dev/sdb1       500G  128G  372G  26% /data
```

> **Beginner's Note:** Running out of disk space can cause many problems. Use `df -h` regularly to monitor your available space.

> **SRE Perspective:** In production environments, set up alerts for disk usage thresholds (typically 80-85%) to prevent outages. Remember that some applications crash when temporary space is exhausted, even if other filesystems have space.

#### **`du` – Disk Usage for Files and Directories**

**Purpose**: Estimate file and directory space usage.

**Basic Syntax:**

```bash
du [options] [path]
```

**Common Options:**

- `-h`: Human-readable sizes
- `-s`: Summary (only total for each directory)
- `--max-depth=N`: Limit directory recursion depth
- `-c`: Show grand total

**Beginner Examples:**

Check size of current directory:

```bash
$ du -sh .
258M    .
```

Find largest directories in your home folder:

```bash
$ du -h --max-depth=1 ~ | sort -hr
1.2G    /home/user
850M    /home/user/Downloads
200M    /home/user/Documents
125M    /home/user/Pictures
```

> **Beginner's Note:** When investigating disk space issues, combine `df` to find the full filesystem and `du` to identify which directories are using the most space.

**Advanced Example for SREs:**

Find the largest subdirectories and files in a problem area:

```bash
# Find largest directories
$ du -h /var --max-depth=2 | sort -hr | head -10

# Find largest files
$ find /var -type f -exec du -h {} \; | sort -hr | head -10
```

#### **`free` – Memory Usage**

**Purpose**: Display amount of free and used memory in the system.

**Basic Syntax:**

```bash
free [options]
```

**Common Options:**

- `-h`: Human-readable output (MB, GB)
- `-s N`: Update continuously every N seconds
- `-c N`: Display N times and exit

**Example:**

```bash
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           15Gi       4.6Gi       3.2Gi       264Mi       7.2Gi        10Gi
Swap:         4.0Gi          0B       4.0Gi
```

Understanding the output:

- **total**: Total installed memory
- **used**: Memory used by applications
- **free**: Completely unused memory
- **shared**: Memory shared by multiple processes
- **buff/cache**: Memory used for buffers and cache
- **available**: Memory available for new applications (free + reclaimable buff/cache)

> **Beginner's Note:** Focus on the "available" column rather than "free" to understand how much memory is truly available. Linux uses otherwise free memory for caching to improve performance, but can reclaim it when needed.

> **Intermediate Insight:** High buff/cache usage is normal and beneficial for performance. Only worry if the "available" memory is consistently low and swap usage is high.

> **SRE Perspective:** Memory pressure in production systems can cause serious performance degradation. Monitor trends of available memory and swap usage. Sudden drops might indicate memory leaks.

#### **Advanced System Information Tools**

**`vmstat` - Virtual Memory Statistics:**

```bash
$ vmstat 2 5  # 5 reports, 2 second intervals
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0      0 3283508 224836 7374148    0    0     0     1    0    0  1  0 99  0  0
 0  0      0 3283424 224836 7374148    0    0     0     0  182  244  0  0 100  0  0
```

**`iostat` - Input/Output Statistics:**

```bash
$ iostat -x 2
Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
sda              8.24   25.28    172.51   1640.69     0.39     7.48   4.55  22.83    0.36    2.55   0.07    20.93    64.90   0.23   0.78
```

**`netstat` or `ss` - Network Statistics:**

```bash
netstat -tuln  # TCP/UDP listening ports
ss -s          # Socket statistics summary
```

> **SRE Perspective:** These advanced tools are essential for comprehensive system analysis. They provide detailed insights into:
>
> - `vmstat`: Process states, memory, paging, block I/O, CPU activity
> - `iostat`: Storage device utilization, queue lengths, wait times
> - `netstat`/`ss`: Network connections, listening ports, socket states

---

## 🎯 **Practical Exercises by Skill Level**

### **Beginner Exercise: Basic Process Management**

1. Open a terminal and run `ps aux | grep $USER` to see your processes.
2. Start the `top` command to see a real-time view of system processes. Press 'q' to exit.
3. Run a command like `sleep 100` in your terminal, then press Ctrl+Z to suspend it.
4. Use `jobs` to verify the process is stopped.
5. Use `bg` to continue the process in the background.
6. Use `jobs` again to verify it's running.
7. Use `fg` to bring it back to the foreground, then press Ctrl+C to terminate it.
8. Check your system's memory usage with `free -h` and disk usage with `df -h`.

### **Intermediate Exercise: Resource Investigation**

1. Find the top 5 processes consuming the most CPU: `ps aux --sort=-%cpu | head -6`
2. Find the top 5 processes consuming the most memory: `ps aux --sort=-%mem | head -6`
3. Install `htop` if not already available and explore its interface.
4. Use `du` to identify the largest directories in your home folder:

   ```bash
   du -h --max-depth=1 ~ | sort -hr | head -5
   ```

5. Practice killing a process:
   - Start a process: `sleep 200 &`
   - Find its PID: `ps aux | grep sleep`
   - Terminate it: `kill [PID]`
6. Use `kill -l` to see all available signals and read about their purposes.

### **SRE Application Exercise: System Monitoring Dashboard**

Create a basic system monitoring script that you could use during an incident:

1. Create a bash script called `system_dashboard.sh`:

```bash
#!/bin/bash

echo "===== SYSTEM DASHBOARD ====="
echo "Date: $(date)"
echo

echo "===== SYSTEM LOAD ====="
uptime
echo

echo "===== CPU USAGE ====="
top -bn1 | head -8
echo

echo "===== MEMORY USAGE ====="
free -h
echo

echo "===== DISK USAGE ====="
df -h | grep -v tmpfs
echo

echo "===== TOP 5 CPU CONSUMING PROCESSES ====="
ps aux --sort=-%cpu | head -6
echo

echo "===== TOP 5 MEMORY CONSUMING PROCESSES ====="
ps aux --sort=-%mem | head -6
echo

echo "===== RECENT SYSTEM ERRORS ====="
sudo dmesg | grep -i "error\|warn\|fail" | tail -5 2>/dev/null || echo "No recent errors found (or insufficient permissions)"
echo

echo "===== LISTENING NETWORK PORTS ====="
netstat -tuln 2>/dev/null || ss -tuln
```

2. Make the script executable: `chmod +x system_dashboard.sh`
3. Run the script: `./system_dashboard.sh`
4. Try running it with `watch` for continuous monitoring: `watch -n 5 ./system_dashboard.sh`
5. Discuss how you would enhance this for production monitoring and what thresholds would trigger alerts in your environment.

---

## 📝 **Multi-Level Quiz: Test Your Knowledge**

### **Beginner Level**

1. What command shows a snapshot of all running processes with detailed information?
   - a) `ps aux`
   - b) `ps`
   - c) `ps -l`

2. How do you forcibly terminate a process with PID 1234?

   ```bash
   # Fill in the blank
   kill ____ 1234
   ```

3. Which command displays available disk space in a human-readable format?
   - a) `df -a`
   - b) `du -h`
   - c) `df -h`

### **Intermediate Level**

4. You started a process that's running in the background. How do you bring it to the foreground if it's job number 2?
   - a) `fg 2`
   - b) `fg %2`
   - c) `background 2`

5. Which command would show you the total memory available for new applications on your system?
   - a) `top`
   - b) `free -h`
   - c) `ps aux`

6. You need to find which process is using the most memory on your system. What command would be most efficient?

   ```bash
   # Fill in the blank
   ps aux --sort=_____ | head -5
   ```

### **SRE Application Level**

7. During an incident, you notice high system load but normal CPU usage. What's the most likely cause of this discrepancy?
   - a) Network congestion
   - b) I/O wait or blocking operations
   - c) Too many background processes
   - d) Memory leaks

8. A production service is failing to start because another process is using its port. Which command would help identify the process holding the port?
   - a) `ps aux | grep port`
   - b) `netstat -tuln | grep port`
   - c) `lsof -i :port_number`
   - d) `kill -9 port_number`

9. You need to reload a service's configuration without restarting it. Which signal would you typically use?
   - a) SIGTERM (15)
   - b) SIGKILL (9)
   - c) SIGHUP (1)
   - d) SIGINT (2)

10. A system is showing high memory usage but the sum of all process RSS values doesn't account for it. What's the most likely explanation?
    - a) Hidden processes not visible to your user
    - b) Kernel memory usage and buffers/cache
    - c) Memory leaks in terminated processes
    - d) Virtual memory mistakenly reported as used

---

## ❓ **FAQ for Process Management and Monitoring**

### **Basic Questions**

**Q1: What's the difference between `kill` and `kill -9`?**

**A:** The regular `kill` command sends a SIGTERM (signal 15) to a process, asking it to terminate gracefully. This allows the process to clean up, close files, and exit properly. In contrast, `kill -9` sends SIGKILL (signal 9), which forces immediate termination without allowing cleanup. Always try regular `kill` first and only use `kill -9` as a last resort when a process is unresponsive.

**Q2: How can I install `htop` if it's missing?**

**A:** Use your distribution's package manager:

- For Debian/Ubuntu: `sudo apt install htop`
- For RHEL/CentOS/Fedora: `sudo yum install htop` or `sudo dnf install htop`
- For Arch Linux: `sudo pacman -S htop`
- For macOS with Homebrew: `brew install htop`

**Q3: Why does my terminal hang after I run a command?**

**A:** The command is running in the foreground and hasn't completed yet. You have several options:

- Wait for it to complete
- Press Ctrl+C to terminate it
- Press Ctrl+Z to suspend it, then type `bg` to continue it in the background
- Next time, add `&` at the end of the command to run it in the background initially

### **Intermediate Questions**

**Q4: How do I find which process is using a specific port?**

**A:** Use one of these commands:

```bash
# Using lsof (install if needed)
sudo lsof -i :80   # Replace 80 with your port number

# Using netstat
sudo netstat -tulpn | grep :80

# Using ss (newer alternative to netstat)
sudo ss -tulpn | grep :80
```

**Q5: What do the different process states mean in `ps` and `top` output?**

**A:** Common process states include:

- `R`: Running or runnable (on run queue)
- `S`: Interruptible sleep (waiting for an event)
- `D`: Uninterruptible sleep (usually I/O)
- `Z`: Zombie (terminated but not reaped by parent)
- `T`: Stopped (suspended)
- `+`: Foreground process group

Processes in state `D` (uninterruptible sleep) cannot be killed even with SIGKILL until the I/O operation they're waiting for completes.

**Q6: What's the difference between VSZ and RSS in process memory usage?**

**A:**

- **VSZ (Virtual Size)**: All memory the process can access, including memory that may not be resident in RAM
- **RSS (Resident Set Size)**: Actual physical memory used by the process

RSS is generally more important for understanding actual memory consumption, while VSZ includes memory that might be swapped out or not allocated yet.

### **SRE-Focused Questions**

**Q7: How do I determine what's causing high load average on a system?**

**A:** High load average can be caused by different types of contention:

1. Check if it's CPU-bound:

```bash
top          # Look at %CPU and CPU states
mpstat -P ALL # Check individual CPU core utilization
```

2. Check if it's I/O-bound:

```bash
iostat -x    # Look at %util and await columns
top          # Check %wa (wait) in CPU stats
```

3. Check for memory pressure:

```bash
free -h      # Look for low available memory and swap usage
vmstat 1     # Check si/so columns for swap activity
```

4. Check for process/resource contention:

```bash
ps aux | grep D    # Processes in uninterruptible sleep
lsof | wc -l       # Count open files
```

**Q8: How can I prevent critical services from being killed during memory pressure?**

**A:** Use the Out-Of-Memory (OOM) score adjustment mechanism:

```bash
# Protect a running process (lower value = less likely to be killed)
echo -1000 > /proc/PID/oom_score_adj

# For services managed by systemd, add to the service file:
[Service]
OOMScoreAdjust=-1000
```

Values range from -1000 (never kill) to +1000 (kill first). Consider this carefully as preventing OOM killer from working could lead to system-wide freezes.

**Q9: What's the best way to monitor a process and automatically restart it if it fails?**

**A:** For production systems, use a proper service manager:

1. **systemd** (modern Linux distributions):

```bash
# Create a unit file in /etc/systemd/system/myservice.service
[Unit]
Description=My Critical Service
After=network.target

[Service]
ExecStart=/path/to/your/program
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target

# Enable and start
sudo systemctl enable myservice
sudo systemctl start myservice
```

2. For simpler needs, consider tools like `supervisord` or a basic script with a monitoring loop.

---

## 🚧 **Common Issues and Troubleshooting**

### **Issue 1: "kill: Operation not permitted"**

**Cause**: You're trying to terminate a process owned by another user.

**Solution**:

- Use `sudo` if you have administrator privileges: `sudo kill PID`
- Contact the system administrator if you don't have sudo access
- For your own processes running as different users, try logging in as that user first

**Prevention**:

- Run processes using your own user account when possible
- Use proper service management for multi-user systems

### **Issue 2: System shows "disk full" but `df` shows available space**

**Cause**: Several possibilities:

1. Deleted files still held open by running processes
2. Out of inodes (file entries) but not out of blocks
3. Filesystem quota limits reached

**Diagnosis**:

```bash
# Check inode usage
df -i

# Find deleted files still in use
lsof | grep deleted

# Check for quota limits (if enabled)
quota -v
```

**Solution**:

- For deleted files still in use, restart the process holding them open
- For inode exhaustion, clean up small files (especially in /tmp, cache directories)
- For quota issues, remove unneeded files or request quota increase

### **Issue 3: High Memory Usage Despite Few Running Applications**

**Cause**: Linux uses available memory for disk caching to improve performance.

**Diagnosis**:

```bash
# Check memory breakdown
free -h

# Look at detailed memory statistics
cat /proc/meminfo
```

**Understanding**: Look at the "available" memory column in `free` output rather than "free" column. Memory shown as "buff/cache" is used for performance optimization but can be reclaimed when applications need it.

**Solution**: This is normal behavior! Only take action if:

- Available memory is consistently low
- System is actively swapping (check swap used and si/so in vmstat)
- Applications are being killed by the OOM killer (check dmesg)

### **Issue 4: Zombie Processes Won't Die Even with kill -9**

**Cause**: Zombie processes are already dead; they're just waiting for their parent process to acknowledge their exit status.

**Diagnosis**:

```bash
# Find zombies
ps aux | grep defunct

# Find parent of zombie
ps -o ppid= -p ZOMBIE_PID
```

**Solution**:

1. Restart the parent process if possible
2. If the parent is essential and can't be restarted, you'll need to wait for it to be fixed
3. In extreme cases (many zombies affecting performance), consider restarting the system

---

### 🔄 **Real-World SRE Scenario: Troubleshooting a Slow Web Application**

**Incident**: Users are reporting slow response times from your web application. The monitoring system shows increasing response latency over the past hour, but no outage or error alerts have triggered yet. You need to diagnose and resolve the issue quickly.

**Step 1: Initial Assessment**

First, get a quick overview of system health:

```bash
# Check system load and uptime
uptime
```

Output:

```
15:30:22 up 47 days, 3:42, 2 users, load average: 6.72, 5.89, 4.21
```

The load averages are high and increasing (compared to your 4 CPU cores), suggesting resource contention.

**Step 2: Examine Resource Usage**

```bash
# Check overall resource usage
top
```

Key findings in the output:

- CPU usage shows 35% in `wa` (I/O wait)
- Several application processes using high CPU
- Memory usage at 85% with minimal free memory

**Step 3: Check Disk I/O**

The high I/O wait time suggests disk bottlenecks:

```bash
# Check disk I/O statistics
iostat -x 2
```

Output shows high `%util` (nearly 100%) on the database disk, with long `await` times, confirming I/O bottleneck.

**Step 4: Investigate Database Activity**

```bash
# Check database connections
sudo netstat -anp | grep 3306 | grep ESTABLISHED | wc -l
```

Output: `215`

This is much higher than normal (usually ~50 connections).

**Step 5: Application Process Investigation**

```bash
# Find application-specific processes
ps aux | grep java
```

You notice multiple application server processes with high CPU and memory usage.

**Step 6: Check Application Logs**

```bash
# Check for errors or warnings
sudo tail -n 100 /var/log/application/app.log | grep -i "error\|warn\|exception"
```

You find numerous log entries showing:

```
WARN [2023-10-15 15:20:12] Connection pool reaching maximum capacity
ERROR [2023-10-15 15:25:47] Database query timeout after 30 seconds
```

**Step 7: Check Database Logs**

```bash
# Look at recent database logs
sudo tail -n 100 /var/log/mysql/mysql-slow.log
```

The slow query log shows a particular query taking excessive time:

```
# Time: 2023-10-15T15:10:11.123456Z
# User@Host: appuser[appuser] @ webserver1 [192.168.1.10]
# Query_time: 45.234091  Lock_time: 0.000025  Rows_sent: 1  Rows_examined: 3824656
SELECT * FROM order_items JOIN orders ON order_items.order_id = orders.id WHERE orders.created_at > '2023-01-01';
```

**Root Cause Analysis**:

1. A database query missing an index is causing full table scans
2. This is creating high I/O wait times and database contention
3. Connection pool is maxing out as queries take longer to complete
4. Web application response time increases due to waiting for database

**Resolution Steps**:

1. **Immediate Mitigation**:

   ```bash
   # Restart the application to clear connection pool
   sudo systemctl restart webapp
   
   # Add missing index to the orders table
   mysql -u admin -p orders_db -e "CREATE INDEX idx_created_at ON orders (created_at);"
   ```

2. **Verification**:

   ```bash
   # Check system load again
   uptime
   ```

   Load average starts decreasing.

   ```bash
   # Verify database I/O has improved
   iostat -x 2
   ```

   I/O utilization drops to normal levels (<30%).

3. **Long-term Fixes**:
   - Add proper monitoring for database query performance
   - Implement query review process before deployment
   - Set up alerts for connection pool saturation
   - Add load testing to the CI/CD pipeline

**Post-Incident Documentation**:

- Document root cause, resolution steps, and preventive measures
- Schedule a review of other potential missing indexes
- Create runbook for similar incidents
- Plan a knowledge sharing session about database performance tuning

---

## 📚 **Further Learning Resources**

### **Beginner Resources**

- [Linux Journey - Process Utilization](https://linuxjourney.com/lesson/process-utilization)
- [Tutorials Point - Linux Commands for Beginners](https://www.tutorialspoint.com/unix_commands/index.htm)
- [Linux Command Line Basics - Udacity Free Course](https://www.udacity.com/course/linux-command-line-basics--ud595)
- [Digital Ocean's Linux Basics Series](https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-basics)

### **Intermediate Resources**

- [The Linux Command Line (William Shotts)](http://linuxcommand.org/tlcl.php) - Free comprehensive book
- [Linux Performance Tools Tutorial](https://netflixtechblog.com/netflix-at-velocity-2015-linux-performance-tools-51964ddb81cf)
- [Linux System Administrator's Guide](https://tldp.org/LDP/sag/html/index.html)
- [Linux Performance Troubleshooting Course](https://www.linkedin.com/learning/linux-performance-tuning)

### **SRE-Specific Resources**

- [Google SRE Book - Chapter 7: The Evolution of Automation at Google](https://sre.google/sre-book/automation-at-google/)
- [Linux Systems Performance (Brendan Gregg)](http://www.brendangregg.com/linuxperf.html)
- [USE Method for Linux Performance Analysis](http://www.brendangregg.com/usemethod.html)
- [SRE Classroom: How to Monitor System Health](https://linkedin.github.io/school-of-sre/level101/metrics_and_monitoring/introduction/)
- [Practical Linux Performance Tools & Methods](https://www.youtube.com/watch?v=FJW8nGV4jxY) - Video presentation

---

## 🎓 **Quiz Answers**

### **Beginner Level**

1. a) `ps aux`
2. `-9`
3. c) `df -h`

### **Intermediate Level**

4. b) `fg %2`
5. b) `free -h`
6. `-%mem`

### **SRE Application Level**

7. b) I/O wait or blocking operations
8. c) `lsof -i :port_number`
9. c) SIGHUP (1)
10. b) Kernel memory usage and buffers/cache

---

## 🏆 **Key Takeaways**

- Process management is fundamental to Linux system administration and SRE work
- Regular monitoring helps prevent issues before they become incidents
- Understanding resource usage patterns helps with capacity planning
- A methodical, step-by-step approach is essential for troubleshooting
- The right tools make a significant difference in problem diagnosis speed
- Process and resource management are core skills that improve with practice

Great job today! Tomorrow, we'll explore networking basics including `ping`, `ssh`, network diagnostics, and connectivity troubleshooting—essential skills for working with distributed systems in SRE environments.
