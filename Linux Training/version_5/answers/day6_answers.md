# Day 6 Answers

## **Beginner Level Answers**

### **1) MCQ: Which command shows a snapshot of current processes in BSD-style format?**  

- **Question**:  
  A) `ps aux`  
  B) `jobs`  
  C) `free -h`  
  D) `df -h`

- **Correct Answer**: **A) `ps aux`**  
- **Explanation**:
  - **`ps aux`** is the canonical BSD-style way of displaying process information, listing all processes (including those without a controlling terminal) along with user, CPU/memory usage, and command details.
  - **`jobs`** only shows background jobs in the *current shell*, which is not a snapshot of all running processes system-wide.
  - **`free -h`** displays memory usage, not process listings.
  - **`df -h`** reports filesystem disk usage, not processes.

---

### **2) Fill in the Blank: To see the currently running jobs in your shell, you would type `__________`.**  

- **Correct Answer**: `jobs`
- **Explanation**:  
  - `jobs` is the built-in shell command that lists any jobs started (or moved) in the background in the same terminal session. It does not display all system processes, only those initiated by and tied to the current shell session.

---

### **3) Short Answer: Explain the difference between `kill -9` and `kill` (without flags).**  

- **Correct Explanation**:
  - **`kill`** with no explicit signal (or `kill -TERM`) sends **SIGTERM**, which requests a *graceful* termination. The process is given a chance to clean up, close files, and shut down properly.
  - **`kill -9`** sends **SIGKILL**, which **forcefully** stops a process without giving it a chance to handle cleanup. This is used only when the process does not respond to `SIGTERM` or other signals. It can lead to data corruption if the process was writing data at the time.

---

## **Intermediate Level Answers**

### **1) MCQ: Which command below is best for real-time, interactive process monitoring with color-coded output?**  

- **Question**:  
  A) `top -b`  
  B) `htop`  
  C) `ps -ef`  
  D) `jobs`

- **Correct Answer**: **B) `htop`**  
- **Explanation**:
  - **`htop`** provides an interactive, color-coded interface and allows scrolling, searching, and mouse support. It is known for its more user-friendly real-time view than `top`.
  - **`top -b`** is batch mode (non-interactive), typically used for scripting/logging.
  - **`ps -ef`** shows a static snapshot of processes in SysV style, not real-time, not interactive.
  - **`jobs`** only shows background jobs for the current shell session.

---

### **2) Scenario: You notice your `/data` partition is 90% full. Which two commands could help you pinpoint large directories/files?**  

- **Correct Answer**:  
  - **`df -h`** (or `df`) and **`du`** (often with `-h`, `--max-depth`, etc.)  
  - **Explanation**:
    - **`df -h`** shows how full each filesystem is overall.  
    - **`du`** (Disk Usage) lets you see which directories or files are occupying the most space. Often you’ll combine `du -h --max-depth=1 /data` with sorting (`| sort -h`) to find the largest directories.

- **Why other commands alone are less suitable**:
  - `ls -l` can show file sizes, but it won’t efficiently summarize large directory usage.  
  - `ps` or `jobs` are irrelevant to disk space diagnosis.

---

### **3) Fill in the Blank: To resume job number 2 in the background, you would type `__________ %2`.**  

- **Correct Answer**: `bg %2`
- **Explanation**:  
  - **`bg`** is used to resume a suspended job (stopped by `Ctrl+Z` or otherwise) in the background. Specifying `%2` targets the job labeled as “2” in the output of `jobs`.

---

### **4) True/False: `free -h` includes swap usage in its output.**  

- **Correct Answer**: **True**
- **Explanation**:
  - **`free`** shows both main memory (RAM) and **swap** usage, typically summarized below the memory line in the command output. For instance:

    ```bash
    Mem:    15Gi ...
    Swap:   4.0Gi ...
    ```

---

## **SRE Level Answers**

### **1) Scenario: During an outage call, you suspect the Java service is using too much memory. Name two commands that would help you confirm this and how.**  

- **Correct Answer** (various valid approaches exist, but two core ones are):
  1. **`ps aux --sort=-%mem`** (or `ps` with a memory sort)  
     - Explanation: This shows processes sorted by memory usage, so you can confirm whether the Java process is top memory consumer.
  2. **`top`** or **`htop`**  
     - Explanation: Real-time interactive monitoring to watch memory usage climb or see if the Java process’s usage is spiking.

- **Possible Additional Commands**: `free -h` (check overall memory usage and swap), `jmap` (Java-specific memory analysis), or `pmap` (detailed memory mapping).

---

### **2) Short Answer: Why might you run `iostat` or `vmstat` in addition to `top` when investigating a performance bottleneck?**  

- **Correct Explanation**:
  - **`top`** focuses primarily on CPU and memory usage by individual processes in real time.  
  - **`iostat`** focuses on I/O performance and disk usage, revealing if high I/O wait is the root cause.  
  - **`vmstat`** shows detailed virtual memory statistics and context switches, helping you see if there’s excessive paging, swapping, or CPU wait.  
  - Together, they give a broader picture of system health than `top` alone.

---

### **3) MCQ: Which command combination continuously records process snapshots for historical analysis?**  

- **Question**:  
  A) `kill -9 $(pgrep -u root)`  
  B) `top -b -n 1`  
  C) `watch -n 2 ps aux`  
  D) `jobs -l && bg %1`

- **Correct Answer**: **C) `watch -n 2 ps aux`**  
- **Explanation**:
  - `watch -n 2 ps aux` reruns `ps aux` every 2 seconds and displays the output, effectively letting you observe changes over time (or log it if you redirect output).  
  - **A)** forcibly kills all processes owned by root (which is quite dangerous and definitely not about historical analysis).  
  - **B)** runs `top` once in batch mode, but `-n 1` only captures a single snapshot, not continuous data.  
  - **D)** merely lists jobs and backgrounds one; it’s not about repeated snapshots.

---

### **4) True/False: If `df -h` reports enough free space, the system cannot run out of inodes.**  

- **Correct Answer**: **False**  
- **Explanation**:
  - A filesystem can run out of inodes even when `df -h` shows plenty of available space in terms of GB/MB. This situation occurs if there are too many small files. “No space left on device” errors can happen because of *inode exhaustion*, not just block usage.

---

## **Additional Notes**

- Always interpret each command in the context of your system’s state. Some issues (like stuck processes in `D` state) require specialized commands (e.g., `iostat`, `dstat`, or advanced tracing).
- For multi-user or production servers, ensure you have the right privileges and confirm you’re targeting the correct process before issuing potentially disruptive commands like `kill`.

---
