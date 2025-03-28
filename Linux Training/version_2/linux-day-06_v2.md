# 🚀 **Day 6: Process Management and System Monitoring for SRE**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 5:**

Yesterday, we explored advanced text processing tools including `sed` for stream editing, `awk` for pattern scanning and processing, `sort` for organizing data, and `uniq` for handling duplicates. We also learned how to combine these tools into powerful data processing pipelines to extract meaningful insights from logs and system outputs.

### 📅 **Today's Topics and Importance:**

Today, we focus on **process management and system monitoring** — fundamental skills that allow SREs to observe system behavior, identify resource bottlenecks, and control application processes. These capabilities are critical because:

- Understanding process behavior helps diagnose performance issues
- System resource monitoring prevents outages from resource exhaustion
- Proper process control ensures graceful shutdowns and restarts
- Real-time monitoring enables rapid incident response
- Background process management supports maintenance tasks

As an SRE, your ability to monitor systems and manage processes directly impacts service reliability and performance.

### 🎯 **Learning Objectives:**

By the end of Day 6, you will be able to:

- Monitor running processes using `ps`, `top`, and `htop`
- Control processes with commands like `kill`, `pkill`, and `killall`
- Manage background and foreground jobs using `jobs`, `bg`, and `fg`
- Monitor system resources with `free`, `df`, `du`, and `iostat`
- Gather system information using commands like `uname` and `lsof`
- Apply these skills to diagnose and resolve real-world operational issues

---

## 📚 **Core Concepts Explained**

### **Understanding Processes in Linux**

In Linux, a process is an instance of a running program. Each process has:

- A unique **Process ID (PID)** for identification
- A **Parent Process ID (PPID)** indicating which process created it
- A **priority/nice level** affecting CPU scheduling
- **Resource allocations** for memory, CPU time, etc.
- **Ownership** (user and group) controlling permissions
- A **state** (running, sleeping, stopped, zombie)

Processes form a hierarchy, with the `init` process (PID 1) at the root. Understanding this hierarchy helps in troubleshooting and resource management.

### **System Resource Types**

Effective system monitoring requires understanding the main resource types:

- **CPU**: Processing capacity, measured in percentage utilization
- **Memory**: RAM usage, including buffers and cache
- **Disk**: Storage space and I/O operations
- **Network**: Bandwidth, connections, and interface status

Resource bottlenecks in any of these areas can affect application performance and reliability. SREs must be able to identify which resources are constrained and understand how to address these limitations.

---

## 💻 **Commands to Learn Today**

### **1. Process Monitoring (`ps`, `top`, `htop`)**

#### **`ps` – Process Status**

**Purpose**: Display snapshots of current processes.

**SRE Context**: Identify running processes, track resource usage, and correlate PIDs with applications.

**Syntax:**
```bash
ps [options]
```

**Common options:**
- `aux`: Show all processes with detailed information
- `-ef`: Another format for detailed process listing
- `-u username`: Show processes for a specific user
- `--forest`: Show process hierarchy tree
- `-o format`: Customize output fields

**Examples:**

View detailed information for all processes:
```bash
[sre@prod-server ~]$ ps aux
USER       PID  %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1   0.0  0.1 171712  9152 ?        Ss   Mar07   0:42 /sbin/init
root       814   0.0  0.1  27756  6476 ?        Ss   Mar07   0:00 /usr/sbin/sshd
webapp    1234   2.5  6.2 4120416 506892 ?      Sl   Mar10  14:23 /usr/bin/java -Xmx2g -jar app.jar
```

Show process hierarchy:
```bash
[sre@prod-server ~]$ ps --forest
  PID TTY          TIME CMD
 8392 pts/0    00:00:00 bash
13186 pts/0    00:00:00  \_ ps
```

Find processes by name:
```bash
[sre@prod-server ~]$ ps aux | grep nginx
root      1234  0.0  0.1  10256  8512 ?        Ss   Mar05   0:01 nginx: master process
nginx     1235  0.0  0.1  10256  8384 ?        S    Mar05   0:02 nginx: worker process
```

#### **`top` – Interactive Process Viewer**

**Purpose**: Display real-time dynamic view of system processes.

**SRE Context**: Monitor system in real-time, identify resource-heavy processes, and observe trends over time.

**Syntax:**
```bash
top [options]
```

**Common options:**
- `-p PID`: Monitor specific process(es)
- `-u username`: Monitor specific user's processes
- `-b`: Run in batch mode (useful for scripts)

**Key interactive commands within top:**
- `k`: Kill a process (prompts for PID)
- `r`: Renice a process (change priority)
- `f`: Select fields to display
- `o`: Change sort order
- `1`: Toggle individual CPU core stats
- `m`: Toggle memory display format
- `c`: Show full command path
- `q`: Quit

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

#### **`htop` – Enhanced Interactive Process Viewer**

**Purpose**: Provides a more user-friendly and feature-rich alternative to `top`.

**SRE Context**: Improved visualization for process monitoring, easier navigation, and better interface for system troubleshooting.

**Note**: May need to be installed (`sudo apt install htop` or `sudo yum install htop`).

**Key features:**
- Color-coded output
- Mouse support
- Horizontal and vertical scrolling
- Tree view of process relationships
- Intuitive process filtering
- Process searching
- Integrated kill and nice commands

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

### **2. Process Control (`kill`, `pkill`, `killall`)**

#### **`kill` – Send Signals to Processes**

**Purpose**: Terminate processes or send other control signals.

**SRE Context**: Gracefully stop applications, restart services, or force-quit hung processes.

**Syntax:**
```bash
kill [options] PID
```

**Common options:**
- `-l`: List all available signals
- `-signal_name` or `-signal_number`: Specify the signal to send

**Common signals:**
- `SIGTERM` (15): Default signal, graceful termination
- `SIGKILL` (9): Immediate termination (cannot be caught or ignored)
- `SIGHUP` (1): Hang up signal, often used to reload configurations
- `SIGINT` (2): Interrupt (like pressing Ctrl+C)
- `SIGSTOP` (19): Pause the process (cannot be caught)
- `SIGCONT` (18): Resume a paused process

**Examples:**

Gracefully terminate a process:
```bash
[sre@prod-server ~]$ kill 1234
```

Force terminate a stubborn process:
```bash
[sre@prod-server ~]$ kill -9 1234
```

Reload a service configuration:
```bash
[sre@prod-server ~]$ kill -HUP 1234
```

#### **`pkill` and `killall` – Kill Processes by Name**

**Purpose**: Kill processes based on name rather than PID.

**SRE Context**: Easily manage multiple instances of the same application, clean up resource-consuming processes by name.

**Syntax:**
```bash
pkill [options] pattern
killall [options] name
```

**Key difference**: `pkill` matches patterns, `killall` requires exact names.

**Common options:**
- `-u username`: Only kill processes owned by user
- `-signal`: Specify signal to send

**Examples:**

Kill all nginx processes:
```bash
[sre@prod-server ~]$ pkill nginx
```

Send SIGHUP to reload all apache processes:
```bash
[sre@prod-server ~]$ killall -HUP apache2
```

Kill all processes owned by a specific user:
```bash
[sre@prod-server ~]$ pkill -u webuser
```

### **3. Job Control (`jobs`, `bg`, `fg`, `nohup`)**

#### **`jobs`, `bg`, `fg` – Manage Shell Jobs**

**Purpose**: Control processes started from the current shell.

**SRE Context**: Run maintenance tasks in the background, manage multiple operations concurrently, keep processes running when terminal connection ends.

**Commands:**
- `jobs`: List all jobs running in the current shell
- `bg [job_id]`: Resume a suspended job in the background
- `fg [job_id]`: Bring a background job to the foreground
- `Ctrl+Z`: Suspend the current foreground job
- `Ctrl+C`: Terminate the current foreground job
- `nohup command &`: Run command immune to hangups

**Examples:**

Start a process in the background:
```bash
[sre@prod-server ~]$ ./long_running_script.sh &
[1] 12345
```

List current jobs:
```bash
[sre@prod-server ~]$ jobs
[1]+  Running                 ./long_running_script.sh &
[2]-  Stopped                 top
```

Bring a background job to the foreground:
```bash
[sre@prod-server ~]$ fg %1
```

Move a suspended job to the background:
```bash
[sre@prod-server ~]$ bg %2
```

Run a process that persists after logout:
```bash
[sre@prod-server ~]$ nohup ./backup_script.sh > backup.log 2>&1 &
```

### **4. System Resource Monitoring**

#### **`free` – Memory Usage**

**Purpose**: Display system memory usage.

**SRE Context**: Monitor RAM and swap usage to identify memory leaks or resource constraints.

**Syntax:**
```bash
free [options]
```

**Common options:**
- `-h`: Human-readable output (MB, GB)
- `-s seconds`: Continuously display with update interval
- `-c count`: Stop after count iterations

**Example:**
```bash
[sre@prod-server ~]$ free -h
              total        used        free      shared  buff/cache   available
Mem:           15Gi       4.6Gi       8.0Gi       264Mi       3.0Gi        10Gi
Swap:         4.0Gi          0B       4.0Gi
```

#### **`df` – Disk Space Usage**

**Purpose**: Report filesystem disk space usage.

**SRE Context**: Monitor available disk space to prevent outages from full disks.

**Syntax:**
```bash
df [options] [filesystem]
```

**Common options:**
- `-h`: Human-readable sizes
- `-T`: Show filesystem type
- `-i`: Show inode information instead of block usage

**Example:**
```bash
[sre@prod-server ~]$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   32G   18G  64% /
/dev/sda2       100G   45G   55G  45% /var
/dev/sdb1       500G  128G  372G  26% /data
```

#### **`du` – Disk Usage for Files and Directories**

**Purpose**: Estimate file space usage.

**SRE Context**: Identify large files and directories consuming disk space.

**Syntax:**
```bash
du [options] [path]
```

**Common options:**
- `-h`: Human-readable sizes
- `-s`: Display only total for each argument
- `--max-depth=N`: Limit directory recursion
- `-c`: Produce a grand total
- `--exclude=pattern`: Skip files matching pattern

**Examples:**

Find total size of the current directory:
```bash
[sre@prod-server ~]$ du -sh .
258M    .
```

Check sizes of subdirectories:
```bash
[sre@prod-server ~]$ du -h --max-depth=1 /var
124M    /var/log
890M    /var/lib
12K     /var/tmp
1.2G    /var
```

#### **`iostat` – Input/Output Statistics**

**Purpose**: Monitor system I/O device loading.

**SRE Context**: Identify disk I/O bottlenecks affecting application performance.

**Syntax:**
```bash
iostat [options] [interval [count]]
```

**Common options:**
- `-x`: Show extended statistics
- `-d`: Display only device utilization report
- `-c`: Display only CPU utilization report
- `-k/-m`: Display statistics in kilobytes/megabytes per second

**Example:**
```bash
[sre@prod-server ~]$ iostat -xd 5
Linux 5.4.0 (prod-server)         03/15/2023      _x86_64_        (4 CPU)

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
sda              8.24   25.28    172.51   1640.69     0.39     7.48   4.55  22.83    0.36    2.55   0.07    20.93    64.90   0.23   0.78
sdb              1.34    3.62     48.31    116.78     0.02     0.16   1.30   4.23    0.28    0.34   0.00    35.96    32.23   0.17   0.09
```

### **5. System Information and Additional Tools**

#### **`uname` – System Information**

**Purpose**: Print system information.

**SRE Context**: Identify OS version and system architecture for troubleshooting.

**Syntax:**
```bash
uname [options]
```

**Common options:**
- `-a`: Print all information
- `-r`: Print kernel release
- `-m`: Print machine hardware architecture

**Example:**
```bash
[sre@prod-server ~]$ uname -a
Linux prod-server 5.4.0-81-generic #91-Ubuntu SMP Thu Jul 15 19:09:17 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```

#### **`lsof` – List Open Files**

**Purpose**: List files opened by processes.

**SRE Context**: Identify which processes are using specific files or ports.

**Syntax:**
```bash
lsof [options]
```

**Common options:**
- `-p PID`: Files opened by specific process
- `-u username`: Files opened by specific user
- `-i [protocol][:port]`: Files used on specified port
- `-c process`: Files opened by command name

**Examples:**

Find which process is using port 80:
```bash
[sre@prod-server ~]$ sudo lsof -i:80
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
nginx   1234   root    6u  IPv4  24850      0t0  TCP *:http (LISTEN)
nginx   1235  nginx    6u  IPv4  24850      0t0  TCP *:http (LISTEN)
```

Find all files opened by a specific process:
```bash
[sre@prod-server ~]$ sudo lsof -p 1234
```

Find who's accessing a specific file:
```bash
[sre@prod-server ~]$ sudo lsof /var/log/syslog
```

---

## 🔍 **SRE Perspective: System Analysis Patterns**

### **1. Analyzing System Load and Bottlenecks**

When a system is slow or unresponsive, follow this diagnostic pattern:

```bash
# 1. Check system load and CPU usage
top

# 2. Check memory usage and swap
free -h

# 3. Check disk space
df -h

# 4. Check for I/O issues
iostat -x 2 5

# 5. Check for specific process issues
ps aux --sort=-%cpu | head -10
ps aux --sort=-%mem | head -10
```

### **2. Resolving Hung Processes**

When applications become unresponsive:

```bash
# 1. Identify the process
ps aux | grep application_name

# 2. Check if it's in uninterruptible sleep (often I/O issues)
ps aux | grep " D "

# 3. Check open files and network connections
lsof -p PID

# 4. Attempt graceful termination
kill PID

# 5. If unresponsive, force terminate
kill -9 PID
```

### **3. Troubleshooting Memory Issues**

When memory problems occur:

```bash
# 1. Check total memory usage
free -h

# 2. Identify top memory consumers
ps aux --sort=-%mem | head -10

# 3. Check for memory leaks (increasing RES over time)
watch -n 10 'ps -o pid,vsz,rss,comm -p PID'

# 4. Check for available memory
cat /proc/meminfo | grep Available

# 5. Check OOM killer logs
dmesg | grep -i "out of memory"
```

---

## 🎯 **Practical Exercise: System Monitoring Dashboard**

Create a basic system monitoring dashboard using the commands you've learned:

1. **Create a bash script called `system_dashboard.sh`**:

```bash
#!/bin/bash

echo "===== SYSTEM DASHBOARD ====="
echo "Date: $(date)"
echo

echo "===== SYSTEM LOAD ====="
uptime
echo

echo "===== CPU USAGE ====="
mpstat 1 1 | tail -n 1
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
dmesg | grep -i "error\|warn\|fail" | tail -5
echo

echo "===== LISTENING PORTS ====="
netstat -tulpn | grep LISTEN
```

2. **Make the script executable**:

```bash
chmod +x system_dashboard.sh
```

3. **Run the script to get an immediate overview of your system**:

```bash
./system_dashboard.sh
```

4. **Create a continuous monitoring view by combining the script with `watch`**:

```bash
watch -n 5 ./system_dashboard.sh
```

This provides a dashboard that refreshes every 5 seconds, giving you real-time visibility into system health.

---

## 📝 **Quiz: Process Management and System Monitoring**

Test your understanding of today's material:

1. You need to gracefully terminate a process with PID 1234. Which command should you use?
   - a) `kill -9 1234`
   - b) `kill 1234`
   - c) `kill -SIGKILL 1234`
   - d) `terminate 1234`

2. During an incident, you need to identify which processes are consuming the most CPU. Which command is most appropriate?
   ```bash
   # Fill in the blank
   ps aux --sort=_________ | head -10
   ```

3. A service is failing to start because its port is already in use. Which command would help identify which process is using the port?
   - a) `netstat -tulpn | grep PORT`
   - b) `ps aux | grep PORT`
   - c) `kill -9 PORT`
   - d) `lsof -i:PORT`

4. You notice the system is running slowly, and you suspect disk I/O might be the bottleneck. Which command would help diagnose this?
   - a) `free -h`
   - b) `ps aux`
   - c) `iostat -x 2 5`
   - d) `top -u user`

5. During a maintenance window, you need to run a long database backup script that will continue even if your SSH session disconnects. Which is the best approach?
   - a) `./backup_script.sh &`
   - b) `nohup ./backup_script.sh > backup.log 2>&1 &`
   - c) `fg ./backup_script.sh`
   - d) `screen ./backup_script.sh`

---

## ❓ **FAQ for SREs: Process Management and Monitoring**

**Q1: How do I determine what's causing high CPU usage on a system?**

**A:** Follow this diagnostic approach:

```bash
# Get an overall view of system load
top

# For multi-core systems, check individual core usage
mpstat -P ALL 1 5

# Identify top CPU consumers
ps aux --sort=-%cpu | head -10

# For a specific process, check its threads
ps -L -o pcpu,pid,tid,cmd -p <PID> | sort -r

# Monitor CPU usage in real-time for a specific process
top -p <PID>
```

**Q2: What's the difference between a zombie process and an orphan process?**

**A:**
- **Zombie Process**: A process that has completed execution but still has an entry in the process table. It appears as "Z" in process status. These can indicate a parent process not properly handling child termination.
- **Orphan Process**: A process whose parent has terminated. The init process (PID 1) adopts orphans, which is normal behavior.

To find zombie processes:
```bash
ps aux | awk '{if ($8=="Z") {print $2}}'
```

**Q3: How do I monitor memory usage effectively to prevent OOM (Out of Memory) events?**

**A:** Monitor these key memory indicators:

```bash
# Overall memory usage including buffers/cache
free -h

# Memory that's truly available for applications
cat /proc/meminfo | grep "MemAvailable"

# Memory usage of a specific application over time
watch -n 10 'ps -o pid,vsz,rss,cmd -p <PID>'

# Track OOM killer events
dmesg | grep -i "out of memory"

# Set up a simple memory monitoring script
while true; do free -m | grep Mem | awk '{print $3 " / " $2 " MB used"}' >> mem_usage.log; sleep 60; done
```

**Q4: When should I use kill -9 versus regular kill?**

**A:**
- Always try `kill` (SIGTERM) first, which allows the process to shut down gracefully by closing files, releasing resources, and saving state
- Use `kill -9` (SIGKILL) only when:
  - The process doesn't respond to regular kill
  - You need immediate termination in an emergency
  - The process is stuck in an uninterruptible state

Remember that kill -9:
- Doesn't allow the process to clean up
- May leave shared resources in an inconsistent state
- Can cause data loss or corruption

---

## 🚧 **Common Issues and Troubleshooting**

### **Issue 1: "Unable to Allocate Memory" Errors**

**Possible causes:**
- Actual out of memory condition
- Memory fragmentation
- Per-process resource limits

**Diagnosis and solutions:**
```bash
# Check overall memory
free -h

# Check specific application memory use
ps -o pid,vsz,rss,comm -p <PID>

# Check for memory limits
ulimit -a

# Check if the OOM killer has been active
dmesg | grep -i "out of memory"

# Possible solutions:
# 1. Increase swap space
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# 2. Check for and fix memory leaks in the application
# 3. Increase actual RAM if necessary
```

### **Issue 2: High Load Average but Low CPU Usage**

**Possible causes:**
- I/O bottlenecks
- Processes in uninterruptible sleep
- Resource contention

**Diagnosis and solutions:**
```bash
# Check I/O wait in top (wa column in CPU stats)
top

# Check disk I/O specifically
iostat -x 2 5

# Check for processes in uninterruptible sleep (D state)
ps aux | grep " D "

# Check which processes are waiting on I/O
iotop (if available) or iostat -xp

# Possible solutions:
# 1. Upgrade to SSD storage
# 2. Optimize disk I/O patterns
# 3. Add more IOPS capacity
# 4. Check for and fix I/O contention in applications
```

---

## 🔄 **Real-World SRE Scenario: Investigating a Slow Web Application**

**Situation:** Users are reporting that a critical web application is responding slowly. You need to investigate the root cause and restore normal performance.

**SRE Response Using Today's Commands:**

1. First, check overall system resources:
   ```bash
   # Get a quick overview of the system
   top
   ```

   You notice high load average but moderate CPU usage, suggesting I/O issues.

2. Check for memory pressure:
   ```bash
   free -h
   ```

   Memory looks adequate with minimal swap usage.

3. Check disk space and I/O:
   ```bash
   df -h
   iostat -x 2 5
   ```

   You see high I/O wait times on the disk containing the application's database.

4. Identify the specific processes causing the I/O:
   ```bash
   ps aux --sort=-%cpu | head -10
   ```

   You notice the database process near the top of CPU consumers.

5. Check database connections:
   ```bash
   netstat -anp | grep 3306 | wc -l
   ```

   This shows unusually high connection counts to the database.

6. Look at the web server's process resource usage:
   ```bash
   top -p $(pgrep -f apache2 | tr '\n' ',' | sed 's/,$//')
   ```

   The web server processes have normal CPU usage but are in waiting (D) state.

7. Check for specific database queries causing the slowdown:
   ```bash
   # On the database server
   mysqladmin processlist | grep -v Sleep
   ```

   You identify a poorly optimized query causing table scans.

8. Check for log error messages related to the database:
   ```bash
   grep -i "error\|warn\|slow" /var/log/mysql/error.log | tail -20
   ```

   You see multiple slow query warnings for the same query pattern.

9. Based on this analysis, you optimize the problematic query, add an index to the database table, and restart the web application.

10. Monitor the situation after your fix:
    ```bash
    watch -n 5 'iostat -x && echo "" && netstat -anp | grep 3306 | wc -l'
    ```

This systematic approach demonstrates how command-line tools can quickly identify the root cause of performance issues in a production environment.

---

## 🔎 **Advanced System Monitoring Techniques**

### **Process Limits and Resource Constraints**

Check and understand process limits:
```bash
# View limits for current shell
ulimit -a

# Check limits for a specific process
cat /proc/PID/limits

# View system-wide limits
sysctl -a | grep -E 'fs.file-max|fs.nr_open|vm.max_map_count'
```

### **Custom Monitoring Scripts**

Create tailored monitoring for specific applications:
```bash
#!/bin/bash
# Simple web server monitoring
while true; do
    TIME=$(date +%Y-%m-%d_%H:%M:%S)
    # Process count
    PROC_COUNT=$(pgrep -c apache2)
    # Connection count
    CONN_COUNT=$(netstat -anp | grep apache2 | grep ESTABLISHED | wc -l)
    # Memory usage
    MEM_USAGE=$(ps aux | grep apache2 | grep -v grep | awk '{sum+=$6} END {print sum/1024 "MB"}')
    
    echo "$TIME,$PROC_COUNT,$CONN_COUNT,$MEM_USAGE" >> web_server_stats.csv
    sleep 60
done
```

### **System Resource Limits**

Monitor system-wide resource limits:
```bash
# File descriptor usage
lsof | wc -l

# Per-process fd count
ls -la /proc/PID/fd | wc -l

# System-wide open files
cat /proc/sys/fs/file-nr
```

---

## 📚 **Further Learning Resources**

- [Linux Process Management (RedHat)](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/monitoring_and_managing_system_status_and_performance/getting-started-with-managing-system-processes_monitoring-and-managing-system-status-and-performance)
- [System Performance Analysis Tools for Linux (Brendan Gregg)](http://www.brendangregg.com/linux.html)
- [Google SRE Book - Chapter 7: Managing Load](https://sre.google/sre-book/handling-overload/)
- [Linux Systems Performance (Netflix TechBlog)](https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-accc10403c55)
- [Linux Performance Tools (Tutorial)](https://netflixtechblog.com/netflix-at-velocity-2015-linux-performance-tools-51964ddb81cf)

---

🎓 **Day 6 completed!** Tomorrow, we'll explore networking basics including network troubleshooting, DNS configuration, and network monitoring tools—essential skills for managing distribute