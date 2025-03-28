
# ✅ **Day 6 Quiz - Answer Key with Explanations**

## **Answers to Today's Quiz**

### **1. You need to gracefully terminate a process with PID 1234. Which command should you use?**

**Correct Answer:** b) `kill 1234`

**Explanation:**  
The standard `kill` command without any signal specified sends SIGTERM (signal 15), which requests the process to terminate gracefully. This allows the process to:

- Close open files and connections
- Release allocated resources
- Save state if needed
- Execute cleanup routines

Options a) and c) both send SIGKILL (signal 9), which forcibly terminates the process without allowing it to clean up. This should only be used when a process doesn't respond to SIGTERM. Option d) is not a valid Linux command.

**SRE Application:** When terminating services in production, always attempt graceful termination first to prevent data corruption, incomplete transactions, or resource leaks. Only escalate to SIGKILL if the process is unresponsive to SIGTERM after a reasonable timeout.

### **2. During an incident, you need to identify which processes are consuming the most CPU. Which command is most appropriate?**

**Correct Answer:** `ps aux --sort=-%cpu | head -10`

**Explanation:**  
This command sorts all processes by CPU usage in descending order (the `-` before `%cpu` indicates reverse sorting) and displays the top 10 CPU consumers.

The `ps aux` portion shows all processes with detailed information:

- `a`: Shows processes from all users
- `u`: Shows additional details including CPU and memory usage
- `x`: Includes processes not attached to a terminal

The `--sort=-%cpu` parameter sorts by CPU usage in descending order, and `head -10` limits output to the first 10 lines.

**SRE Application:** During performance incidents, quickly identifying resource-hungry processes is crucial. This command gives you immediate visibility into what might be causing CPU contention, allowing you to take targeted action such as killing runaway processes or investigating application issues.

### **3. A service is failing to start because its port is already in use. Which command would help identify which process is using the port?**

**Correct Answer:** d) `lsof -i:PORT`

**Explanation:**  
The `lsof -i:PORT` command lists all processes that have open file connections to the specified port. For example, `lsof -i:8080` shows which process is using port 8080.

Options compared:

- Option a) `netstat -tulpn | grep PORT` works too but provides less detailed information about the process
- Option b) `ps aux | grep PORT` is ineffective because processes don't usually have port numbers in their command names or arguments
- Option c) `kill -9 PORT` is incorrect as `kill` operates on PIDs, not port numbers

**SRE Application:** Port conflicts are a common issue in microservice environments. This command helps quickly resolve startup failures by identifying which process needs to be reconfigured or terminated to free up the required port.

### **4. You notice the system is running slowly, and you suspect disk I/O might be the bottleneck. Which command would help diagnose this?**

**Correct Answer:** c) `iostat -x 2 5`

**Explanation:**  
The `iostat -x 2 5` command provides detailed I/O statistics for all disks:

- `-x`: Shows extended statistics including %util (percentage of CPU time during which I/O requests were issued)
- `2`: Updates every 2 seconds
- `5`: Shows 5 reports before exiting

This command helps identify:

- Which disks are experiencing high utilization
- Read vs. write ratios
- Average queue lengths
- Service times

The other options don't provide specific I/O information:

- Option a) `free -h` only shows memory usage
- Option b) `ps aux` shows process information but not disk I/O details
- Option d) `top -u user` shows general process information for a specific user

**SRE Application:** I/O bottlenecks often manifest as high system load with relatively low CPU usage. Using `iostat` helps SREs distinguish between CPU bottlenecks and I/O bottlenecks, leading to different mitigation strategies (optimizing queries vs. upgrading CPU).

### **5. During a maintenance window, you need to run a long database backup script that will continue even if your SSH session disconnects. Which is the best approach?**

**Correct Answer:** b) `nohup ./backup_script.sh > backup.log 2>&1 &`

**Explanation:**  
This command has several key components:

- `nohup`: Makes the process immune to hangup signals, allowing it to continue running after the terminal closes
- `./backup_script.sh`: The script to execute
- `> backup.log`: Redirects standard output to a log file
- `2>&1`: Redirects standard error to the same place as standard output
- `&`: Runs the process in the background

Alternatives:

- Option a) `./backup_script.sh &` runs the script in the background but it will terminate if the SSH session ends
- Option c) `fg ./backup_script.sh` is incorrect syntax and would attempt to bring a background job to the foreground
- Option d) `screen ./backup_script.sh` is a valid alternative approach using the `screen` utility, but it wasn't listed in today's commands and requires the screen package to be installed

**SRE Application:** Maintaining operation continuity during disconnections is crucial for SREs managing remote systems. Using `nohup` ensures critical maintenance tasks complete even if network issues cause session termination, reducing the risk of incomplete maintenance procedures.

## **SRE Application: Process Management in Production Environments**

These process management and monitoring skills form the foundation of effective SRE practices:

1. **Incident Response:** Commands like `ps`, `top`, and `iostat` provide immediate visibility into system state during incidents, enabling rapid diagnosis and resolution.

2. **Resource Management:** Understanding how to monitor memory, CPU, and I/O usage helps prevent resource exhaustion and maintain service availability.

3. **Graceful Service Control:** Proper use of process control commands ensures minimal disruption when restarting or updating services.

4. **Background Operations:** Skills like using `nohup` allow for safe execution of maintenance tasks even during network instability.

5. **Bottleneck Identification:** The ability to pinpoint which system resources are constrained directly translates to faster problem resolution and better capacity planning.

Mastering these commands gives SREs the tools to maintain system reliability proactively rather than reactively, ultimately improving service quality and reducing outage frequency and duration.
