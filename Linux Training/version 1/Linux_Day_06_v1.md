
# 🚀 Day 6: Processes & System Monitoring – Managing and Monitoring Your Linux System

---

## 📌 Introduction

### 🔄 Recap of Day 5

Yesterday, you enhanced your Linux toolkit with intermediate text and data manipulation commands such as `sed`, `awk`, `sort`, `uniq`, and `wc`, along with advanced pipe usage.

### 📅 Today's Topics and Importance

Today, you'll explore **process management and system monitoring**. Understanding how to view, control, and manage processes ensures your Linux system runs smoothly and efficiently.

### 🎯 Learning Objectives

By the end of Day 6, you will be able to:

- View running processes with `ps`, `top`, and `htop`.
- Control processes with commands such as `kill`, `jobs`, `bg`, and `fg`.
- Gather system information using commands like `uname`, `df`, `du`, and `free`.

---

## 📚 Core Concepts Explained

- **Processes:** Every running program or service is a "process" with a unique ID (PID).
- **Foreground vs Background:** Foreground processes are interactive, background processes run silently.
- **Resource Monitoring:** Understand system resource usage to maintain performance.

---

## 💻 Commands to Learn (Detailed)

### 1. Viewing Processes (`ps`, `top`, `htop`)

- **`ps` – Snapshot of current processes**

  ```bash
  ps aux       # Lists all processes with details
  ps -ef       # Similar detailed output in different format
  ```

- **`top` – Real-time process monitoring**

  ```bash
  top          # Interactive process viewer
  ```

- **`htop` – Enhanced interactive process viewer (install if unavailable)**

  ```bash
  htop         # More user-friendly real-time viewer
  ```

---

### 2. Controlling Processes (`kill`, `jobs`, `bg`, `fg`)

- **`kill` – Stop a process**

  ```bash
  kill PID        # Graceful termination
  kill -9 PID     # Force termination
  ```

- **`jobs` – List background processes**

  ```bash
  jobs
  ```

- **`bg` – Resume suspended jobs in background**

  ```bash
  bg %1           # Resumes job 1 in the background
  ```

- **`fg` – Bring background job to foreground**

  ```bash
  fg %1           # Brings job 1 to foreground
  ```

---

### 3. System Information (`uname`, `df`, `du`, `free`)

- **`uname` – System details**

  ```bash
  uname -a       # Kernel and OS info
  ```

- **`df` – Disk space usage**

  ```bash
  df -h          # Human-readable disk space
  ```

- **`du` – Directory disk usage**

  ```bash
  du -sh ~/Downloads   # Size of Downloads folder
  ```

- **`free` – Memory usage**

  ```bash
  free -h        # Human-readable memory stats
  ```

---

## 🎯 Practical Exercise Suggestion

1. View current processes with `ps` and real-time monitoring using `top` or `htop`.
2. Start a process (e.g., `sleep 100`) and move it to the background (`Ctrl+Z`, then `bg`).
3. List jobs, bring your process back to foreground (`fg`), and terminate it (`kill`).
4. Check your disk usage (`df -h`) and memory usage (`free -h`).

---

## 📝 Quiz Section (End of Day)

1. What command lists all running processes in detail?
   - a) `ps aux`
   - b) `ps`
   - c) `ps -l`

2. How do you forcibly terminate a process with PID `1234`?

   ```bash
   kill ____ 1234
   ```

3. What command resumes a suspended job in the background?
   - a) `fg`
   - b) `bg`
   - c) `jobs`

4. Which command displays available disk space in a readable format?
   - a) `df -a`
   - b) `du -h`
   - c) `df -h`

5. How can you quickly view total and available RAM?

   ```bash
   ____ -h
   ```

---

## ❓ FAQ Section

**Q1:** What's the difference between `kill` and `kill -9`?

- **A:** `kill` attempts graceful termination; `kill -9` forces immediate termination.

**Q2:** How can I install `htop` if it's missing?

- **A:** Use your package manager (e.g., `sudo apt install htop` or `sudo yum install htop`).

**Q3:** Can I monitor a specific user's processes?

- **A:** Yes, `ps -u username` or `top -u username`.

---

## 🚧 Common Issues Section

### Issue: "kill: Operation not permitted"

- **Reason:** You're trying to terminate a process you don't own.
- **Solution:** Use `sudo kill PID`.

### Issue: "`df` shows disk full, but can't find large files"

- **Reason:** Hidden or deleted files still occupying space.
- **Solution:** Check with `du -sh /path/*` or restart services holding deleted files.

---

## 🎯 Great job today

You've mastered essential Linux system monitoring and process management commands.

Tomorrow, we'll explore networking basics—essential tools like `ping`, `ssh`, and network diagnostics.

Keep practicing and building your skills!
