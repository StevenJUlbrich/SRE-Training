# Day 6 Answer Sheet

## **Beginner Level**

### **1. MCQ**  

**Question**: Which command lists all processes in a BSD-style format?  
A) ps aux  
B) jobs  
C) free -h  
D) df -h  

**Answer**: **A) ps aux**  

**Explanation**:  

- `ps aux` is a popular way to view all running processes in a BSD-like output format, showing user, PID, CPU/memory usage, and the associated command.  
- `jobs` only shows background/suspended processes in the current shell session.  
- `free -h` and `df -h` report memory and disk usage respectively, not process information.

---

### **2. Fill in the Blank**  

**Question**: To see the currently running jobs in your shell, you would type `__________`.

**Answer**: `jobs`

**Explanation**:  

- The `jobs` command displays all background and suspended jobs within the **current shell** only.  
- It does not show processes system-wide, just the tasks your shell is tracking.

---

### **3. Short Answer**  

**Question**: Explain the difference between `kill` (SIGTERM) and `kill -9` (SIGKILL).

**Answer**:  

- **SIGTERM (kill without flags)** attempts to terminate the process gracefully. The process can catch this signal, perform cleanup, save data, and then exit.  
- **SIGKILL (kill -9)** forcibly terminates the process immediately and **cannot** be caught or ignored by the target process. It is used as a last resort if the process ignores or fails to respond to SIGTERM.

**Explanation**:  

- Graceful termination (SIGTERM) allows services to close open connections and release resources properly, reducing the risk of data loss or corruption.  
- SIGKILL is useful for truly unresponsive or “frozen” processes, but it bypasses any cleanup the application might do.

---

### **4. True/False**  

**Question**: `fg` is used to send a running process to the background.  

**Answer**: **False**  

**Explanation**:  

- `fg` (foreground) **brings** a background or stopped process to the foreground.  
- To move a stopped process to the background, you use `bg`.  
- If you want to background a running foreground process, you typically suspend it first with `Ctrl+Z` and then use `bg` to resume it in the background.

---

## **Intermediate Level**

### **1. MCQ**  

**Question**: Which command provides a real-time, interactive view of processes and allows color-coded output with easier navigation?  
A) top -b  
B) htop  
C) ps -ef  
D) jobs  

**Answer**: **B) htop**  

**Explanation**:  

- `htop` is an interactive, color-coded alternative to `top` that supports mouse interactions and offers convenient filtering and scrolling.  
- `top -b` runs `top` in batch mode (non-interactive).  
- `ps -ef` displays running processes in SysV format but isn’t interactive.  
- `jobs` displays only current shell jobs, not a full real-time system overview.

---

### **2. Fill in the Blank**  

**Question**: To resume job number 3 in the background, you would type `__________ %3`.

**Answer**: `bg %3`

**Explanation**:  

- The `bg` command resumes a stopped job **in the background**.  
- `%3` specifies job ID 3. For example, if you pressed `Ctrl+Z` to suspend job #3, `bg %3` continues it without occupying the terminal.

---

### **3. Scenario**  

**Question**: You notice your `/var` partition is 90% full. Which two commands could help you identify the largest directories or files?

**Answer**:  

- **`df -h`** and **`du -h`**  
  - `df -h` shows partition usage (confirming which partition is near capacity).  
  - `du -h` helps pinpoint where in `/var` disk usage is heaviest by listing sizes of directories or files.  

**Explanation**:  

- `df -h` reveals which filesystem is almost full.  
- `du -h --max-depth=1 /var` (and sorting by size) helps you zero in on the top space consumers within `/var`.  
- You might also use more advanced combos (like `du -h | sort -h` or even `find`) for deeper analysis.

---

### **4. True/False**  

**Question**: `ps aux --sort=-%cpu | head -10` will show you the processes that consume the most CPU at the top.

**Answer**: **True**  

**Explanation**:  

- The `--sort=-%cpu` flag sorts processes by CPU usage in descending order (highest CPU usage first).  
- `head -10` then displays the top 10 processes from that sorted list, meaning those are the highest CPU-consuming processes at that moment.

---

## **SRE Level**

### **1. Scenario**  

**Question**: You suspect a single Java process is leaking memory. Name two commands that would help confirm this suspicion and what you’d look for in their outputs.

**Answer**:  

1. **`ps aux --sort=-%mem`** (or `ps aux | grep java`):  
   - Look for a Java process with unusually large or growing `%MEM` or RSS (Resident Set Size).  
2. **`top` or `htop`**:  
   - Monitor the memory usage of the Java process in real time; watch if `%MEM` (or resident memory) keeps rising, indicating a possible leak.  

**Explanation**:  

- `ps` sorted by memory shows a snapshot ranking processes by memory use.  
- `top`/`htop` gives an ongoing view, helping you see if memory utilization keeps climbing over time.  
- You can also combine these with logs or specialized memory-profiling tools for further investigation.

---

### **2. Short Answer**  

**Question**: Why might you run `iostat` or `vmstat` in addition to `top` when investigating a high load issue?

**Answer**:  

- **`iostat`** reveals disk I/O performance, including read/write throughput, disk utilization (`%util`), and wait times. If your system has high load but low CPU usage, it might be stuck waiting on slow disk operations or a network filesystem.  
- **`vmstat`** offers a view of processes, memory, swapping, block I/O, and CPU activity over time. It helps correlate memory paging/swapping or CPU wait states with load surges.  

**Explanation**:  

- Tools like `top` focus on CPU and memory usage from a process-centric standpoint.  
- `iostat` and `vmstat` address deeper aspects of system health—especially I/O wait and paging—that can drive load average up without visible CPU saturation.

---

### **3. MCQ**  

**Question**: Which command combination continuously records process snapshots for historical analysis?  
A) kill -9 $(pgrep -u root)  
B) top -b -n 1  
C) watch -n 2 ps aux  
D) jobs -l && bg %1  

**Answer**: **C) watch -n 2 ps aux**

**Explanation**:  

- `watch -n 2 ps aux` runs `ps aux` every 2 seconds, effectively logging repeated snapshots you can observe or redirect to a file.  
- `kill -9 $(pgrep -u root)` forcibly kills all processes by root—definitely not for logging.  
- `top -b -n 1` takes only one snapshot in batch mode.  
- `jobs -l && bg %1` is about job control in a single shell session, not repeated system-wide snapshots.

---

### **4. True/False**  

**Question**: If `df -h` reports enough free space, the system cannot run out of inodes.

**Answer**: **False**  

**Explanation**:  

- Inodes track file entries. You can have plenty of disk blocks free but still exhaust inodes if you create a huge number of small files.  
- When you run out of inodes, you get “No space left on device,” even though `df -h` might show available capacity.

---

### **Summary of Answers**

- **Beginner**  
  1. A) ps aux  
  2. jobs  
  3. SIGTERM vs. SIGKILL explanation  
  4. False (fg brings a job to foreground, not background)

- **Intermediate**  
  1. B) htop  
  2. bg %3  
  3. Use `df -h` + `du -h` (or similar) to locate large directories/files  
  4. True (Sorting by `-%cpu` displays highest CPU usage first)

- **SRE Level**  
  1. Use `ps aux --sort=-%mem`, `top`/`htop` to see if Java memory usage grows abnormally  
  2. `iostat`/`vmstat` show I/O wait, swapping, block operations, etc., which top alone might not clarify  
  3. C) watch -n 2 ps aux  
  4. False (inodes can be exhausted even if space remains)

Use these explanations to solidify your understanding of Linux process monitoring and management fundamentals, bridging the gap between basic command usage and advanced SRE-level operational awareness.
