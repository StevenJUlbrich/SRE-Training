# 📝 **Quiz Questions**

## **Beginner Level (3-4 Questions)**

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
