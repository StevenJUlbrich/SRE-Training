# Day 6 Answers

## 📖 Quiz Answers with Full Explanations

### 🟢 Beginner Tier

1. **Real-time monitoring command:**
   - **Answer:** `B) top`
   - **Explanation:** `top` dynamically shows running processes and their real-time resource usage, making it essential for immediate monitoring.

2. **Disk usage command:**
   - **Answer:** `-sh`
   - **Explanation:** `du -sh ~` gives a summarized and human-readable format showing the total size of your home directory.

3. **Pausing a foreground job:**
   - **Answer:** Press `Ctrl+Z`
   - **Explanation:** This key combination temporarily suspends the current foreground job, allowing it to be resumed later.

### 🟡 Intermediate Tier

1. **Reload configuration without stopping:**
   - **Answer:** `A) kill -HUP`
   - **Explanation:** The `SIGHUP` signal tells a running process to reload its configuration files without stopping, useful for uninterrupted service updates.

2. **Detailed disk I/O statistics:**
   - **Answer:** `-x`
   - **Explanation:** `iostat -x 2 5` provides extended disk I/O statistics every 2 seconds for a total of 5 intervals, useful for analyzing performance bottlenecks.

3. **Persistent execution after logout:**
   - **Answer:** Use `nohup`
   - **Explanation:** `nohup` allows a process to continue running after the initiating terminal session has ended, ensuring uninterrupted task completion.

### 🔴 SRE-Level Tier

1. **Open files by port:**
   - **Answer:** `C) lsof -i`
   - **Explanation:** `lsof -i` specifically lists files and processes associated with network connections, making it essential for diagnosing port conflicts or usage.

2. **Sort processes by memory usage:**
   - **Answer:** `-%mem`
   - **Explanation:** Using `ps aux --sort=-%mem | head -10` sorts the processes by memory usage in descending order, quickly identifying the highest memory-consuming processes.

3. **High CPU incident command sequence:**
   - **Answer:** Identify using `top` or `htop`, then terminate with `kill` or force terminate with `kill -9 PID`.
   - **Explanation:** Real-time monitoring tools (`top`/`htop`) rapidly identify resource-intensive processes. Initial graceful termination (`kill PID`) is preferred; forceful termination (`kill -9 PID`) is used if the process does not respond.
