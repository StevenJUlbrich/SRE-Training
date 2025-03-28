# 📝 **Process Management and System Monitoring – Answer Key with Explanations**

---

## **Beginner Level**

### **1. What command shows a snapshot of all running processes with detailed information?**

**Correct Answer: a) `ps aux`**

**Explanation:** `ps aux` provides a comprehensive listing of all processes running on the system with detailed information including:

- User who owns the process (`USER`)
- Process ID (`PID`)
- CPU and memory usage percentages (`%CPU`, `%MEM`)
- Virtual and resident memory size (`VSZ`, `RSS`)
- Process state (`STAT`)
- Start time (`START`)
- CPU time consumed (`TIME`)
- Full command (`COMMAND`)

Option b) `ps` shows only processes associated with your current terminal session, with minimal information.
Option c) `ps -l` shows a long format but only for your current terminal session processes, not all system processes.

### **2. How do you forcibly terminate a process with PID 1234?**

**Correct Answer: `-9`**

**Explanation:** The command `kill -9 1234` sends the SIGKILL signal (signal number 9) to process 1234. This is a forceful termination that cannot be caught or ignored by the process, making it useful for killing unresponsive programs.

The `-9` flag specifies the signal number. SIGKILL is special because:

- It bypasses the normal termination procedure
- The process cannot perform cleanup operations
- It cannot be caught, blocked, or ignored by the process

This should be used as a last resort after trying the normal termination with simply `kill 1234` (which sends SIGTERM, signal 15).

### **3. Which command displays available disk space in a human-readable format?**

**Correct Answer: c) `df -h`**

**Explanation:** The `df` (disk free) command shows available and used disk space on mounted filesystems. The `-h` option formats the output in "human-readable" form, using units like KB, MB, GB instead of showing everything in bytes, making it much easier to interpret.

Option a) `df -a` shows all filesystems, including ones with 0 blocks, but doesn't make sizes human-readable.
Option b) `du -h` is a different command that shows disk usage of files and directories, not filesystem space.

---

## **Intermediate Level**

### **4. You started a process that's running in the background. How do you bring it to the foreground if it's job number 2?**

**Correct Answer: b) `fg %2`**

**Explanation:** In shell job control, the `fg` command brings a background job to the foreground. Jobs are identified by their job number, prefixed with a `%` symbol. So `fg %2` brings job number 2 to the foreground.

Option a) `fg 2` is incorrect syntax because the `%` is required to identify job numbers.
Option c) `background 2` is not a valid command in standard Linux shells.

The job number differs from the process ID (PID) and is specific to the current shell session. You can see job numbers by running the `jobs` command.

### **5. Which command would show you the total memory available for new applications on your system?**

**Correct Answer: b) `free -h`**

**Explanation:** The `free -h` command shows memory usage statistics in a human-readable format. The "available" column in the output specifically shows the amount of memory that is available for starting new applications, which is different from the "free" column.

The available memory includes memory that's currently used for caching and buffers but can be reclaimed immediately if needed by applications. This provides a more accurate picture of usable memory than just looking at "free" memory.

Option a) `top` can show memory usage, but doesn't directly highlight available memory as clearly.
Option c) `ps aux` shows processes but doesn't provide a system-wide memory summary.

### **6. You need to find which process is using the most memory on your system. What command would be most efficient?**

**Correct Answer: `-%mem`**

**Explanation:** The complete command `ps aux --sort=-%mem | head -5` sorts all processes by memory usage in descending order (`-%mem` where the minus sign reverses the sort) and then displays only the top 5 results.

This is efficient because:

- `ps aux` lists all processes with detailed information
- `--sort=-%mem` sorts by the memory percentage column in descending order
- `head -5` limits output to just the 5 highest memory consumers

The minus sign before `%mem` is crucial as it reverses the sort order. Without it, you'd get the processes using the least memory instead of the most.

---

## **SRE Application Level**

### **7. During an incident, you notice high system load but normal CPU usage. What's the most likely cause of this discrepancy?**

**Correct Answer: b) I/O wait or blocking operations**

**Explanation:** System load average represents the number of processes that are either running or waiting for resources. When load is high but CPU usage remains normal, it typically indicates that processes are waiting for something other than CPU time.

I/O wait (shown as `wa` in top's CPU stats) occurs when processes are waiting for disk, network, or other I/O operations to complete. Similarly, processes can be blocked waiting for locks, semaphores, or other system resources. Both situations contribute to high load without high CPU usage.

Option a) Network congestion might cause I/O wait but isn't directly reflected in system load.
Option c) Background processes would show up in CPU usage if they're consuming CPU.
Option d) Memory leaks would typically show as high memory usage, not necessarily high load.

This is a classic pattern SREs need to recognize because the troubleshooting approach differs significantly from CPU-bound problems.

### **8. A production service is failing to start because another process is using its port. Which command would help identify the process holding the port?**

**Correct Answer: c) `lsof -i :port_number`**

**Explanation:** The `lsof -i :port_number` command lists open files (including network sockets) associated with the specified port. It shows which process is currently using that port, including its PID, user, and command.

For example, `lsof -i :80` would show processes using port 80.

Option a) `ps aux | grep port` would search process listings for the text "port", not find processes using a specific port number.
Option b) `netstat -tuln | grep port` shows listening ports but doesn't always clearly identify which process owns them.
Option d) `kill -9 port_number` is incorrect; you cannot kill a port, only a process.

Port conflicts are common in production environments, especially during deployments, making this command essential for SREs.

### **9. You need to reload a service's configuration without restarting it. Which signal would you typically use?**

**Correct Answer: c) SIGHUP (1)**

**Explanation:** SIGHUP (Hangup signal, signal number 1) traditionally indicated that a terminal was disconnected, but many services repurposed it as a signal to reload their configuration without a full restart. This has become a standard convention in many Linux services and daemons.

For example, to reload the Nginx web server configuration: `kill -HUP $(pidof nginx)`

Option a) SIGTERM (15) is used for graceful termination, not configuration reload.
Option b) SIGKILL (9) forcibly terminates a process and cannot be caught or handled.
Option d) SIGINT (2) is equivalent to pressing Ctrl+C and typically terminates programs.

Using SIGHUP for configuration reload is especially important in production environments where service restarts can cause downtime or dropped connections.

### **10. A system is showing high memory usage but the sum of all process RSS values doesn't account for it. What's the most likely explanation?**

**Correct Answer: b) Kernel memory usage and buffers/cache**

**Explanation:** The Linux kernel uses memory for various purposes beyond what's visible in process listings:

- **Kernel structures and modules**: Memory used by the kernel itself
- **Buffers**: Memory used for file system metadata
- **Cache**: Memory used to cache file contents for faster access
- **Slab**: Memory used for kernel data structures

These memory allocations improve system performance but aren't directly attributable to specific user processes. The `free` command separates these allocations in its "buff/cache" column.

Option a) Hidden processes is unlikely as processes are visible in the process table.
Option c) Memory from terminated processes is released back to the system.
Option d) Virtual memory is not counted in actual memory usage statistics.

Understanding kernel memory usage is important for SREs to accurately diagnose memory pressure situations and avoid false alarms.
