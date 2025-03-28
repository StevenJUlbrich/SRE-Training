# ✅ **Day 6 Quiz – Answer Key with Detailed Explanations**

## Below are the answers and explanations for Day 6’s quiz questions

---

### **Question 1:**  

**What command lists all running processes in detail?**

✅ **Correct Answer:**  
**a)** `ps aux`

**Explanation:**  

- `ps aux` provides detailed information on all running processes, including processes from all users.
- `ps` alone shows limited processes (just current user's processes without details).
- `ps -l` shows limited process information and doesn't include all processes by default.

---

### **Question 2:**  

**How do you forcibly terminate a process with PID `1234`?**

✅ **Correct Answer (fill-in-the-blank):**

```bash
kill -9 1234
```

**Explanation:**  

- The option `-9` sends a SIGKILL signal, forcibly and immediately terminating the process.
- Without `-9`, the `kill` command sends a SIGTERM, allowing processes to terminate gracefully (but possibly ignored).

---

### **Question 3:**  

**What command resumes a suspended job in the background?**

✅ **Correct Answer:**  
**b)** `bg`

**Explanation:**  

- `bg` resumes a suspended job, continuing its execution in the background.
- `fg` resumes a suspended job by bringing it to the foreground.
- `jobs` only lists jobs, doesn't resume them.

---

### **Question 4:**  

**Which command displays available disk space in a readable format?**

✅ **Correct Answer:**  
**c)** `df -h`

**Explanation:**  

- `df -h` provides human-readable (easily understandable) disk usage information.
- `df -a` lists all file systems including pseudo file systems, but isn't inherently readable.
- `du -h` shows sizes of directories/files, not total disk usage across all partitions.

---

### **Question 5:**  

**How can you quickly view total and available RAM?**

✅ **Correct Answer (fill-in-the-blank):**

```bash
free -h
```

**Explanation:**  

- `free -h` shows memory (RAM) and swap usage in a human-readable format.

---

🎯 **Excellent work!**  
Tomorrow, we'll move into networking basics, where you'll explore critical commands like `ping`, `ssh`, and network troubleshooting.

Keep practicing!
