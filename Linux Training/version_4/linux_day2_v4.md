# 🚀 **Day 2: File Operations for SRE – Creating, Viewing, and Managing Files**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 1:**
Yesterday, you explored Linux navigation basics (`pwd`, `ls`, `cd`), help utilities (`man`, `--help`, `info`), and the Filesystem Hierarchy Standard. These foundational skills help SREs locate logs, configuration files, and other essential system elements quickly.

### 📅 **Today's Topics and Importance:**
Today, you'll master **file operations** — including creating, viewing, copying, moving, and deleting files and directories. These operations are central to daily SRE activities such as:

- Backing up and modifying configuration files
- Navigating and analyzing logs during incidents
- Cleaning up disk space by removing obsolete files
- Saving outputs during troubleshooting or audits

**🛠️ Real-World SRE Example:**
During a production incident at 3 a.m., an application starts returning HTTP 500 errors. The SRE on-call SSHs into the affected node, uses `tail -f` and `grep` to track recent errors in `/var/log/nginx/error.log`, creates a timestamped backup of `/etc/nginx/nginx.conf`, rolls back a faulty deploy using `mv`, and restores service within minutes.

This level of fluency in file operations is what separates reactive responders from reliable engineers.

### 🎯 **Learning Objectives:**
By the end of Day 2, you will be able to:
- Create files and directories (`touch`, `mkdir`)
- View file contents (`cat`, `less`, `more`, `head`, `tail`)
- Copy and move files (`cp`, `mv`)
- Delete files and directories (`rm`, `rmdir`)
- Safely handle files in production environments
- Practice real-world SRE tasks with file operations

### 🔄 **Recap of Day 1:**
Yesterday, you explored Linux navigation basics (`pwd`, `ls`, `cd`), help utilities (`man`, `--help`, `info`), and the Filesystem Hierarchy Standard. These foundational skills help SREs locate logs, configuration files, and other essential system elements quickly.

### 📅 **Today's Topics and Importance:**
Today, you'll master **file operations** — including creating, viewing, copying, moving, and deleting files and directories. These operations are central to daily SRE activities such as:

- Backing up and modifying configuration files
- Navigating and analyzing logs during incidents
- Cleaning up disk space by removing obsolete files
- Saving outputs during troubleshooting or audits

### 🎯 **Learning Objectives:**
By the end of Day 2, you will be able to:
- Create files and directories (`touch`, `mkdir`)
- View file contents (`cat`, `less`, `more`, `head`, `tail`)
- Copy and move files (`cp`, `mv`)
- Delete files and directories (`rm`, `rmdir`)
- Safely handle files in production environments
- Practice real-world SRE tasks with file operations

---

## 📚 **Core Concepts Explained**

### **Everything is a File**
Linux treats everything — including text files, devices, network sockets, and system metadata — as files. This abstraction enables uniform command-line tools for interacting with system resources.

**File Types:**
- **Regular files**: Text files, config files, logs
- **Directories**: Folders containing other files
- **Device files**: Hardware I/O interfaces (e.g., `/dev/sda`)
- **Sockets/Pipes**: Inter-process communication endpoints

**Beginner's Note:** Think of this like a single universal interface — if you can read or write a file, you can interact with nearly anything on Linux.

**SRE Perspective:** This consistency allows for powerful automation: logs, configs, metrics, sockets, and backups can all be handled with the same core tools.

---

## 💻 **Command Reference and Usage**

Each command below includes purpose, syntax, real-world examples, and SRE-relevant actions. Additional troubleshooting examples are provided where useful to prepare you for production situations.

### 🛠️ **1. Creating Files and Directories**

These operations are often used in SRE automation tasks such as provisioning log directories, pre-populating config folders, and setting up recovery structures. Understanding how permissions, ownership, and system constraints interact with these commands is key.

#### `touch`
- **Purpose:** Create an empty file or update timestamps.
- **Syntax:** `touch [options] filename(s)`
- **Examples:**
  ```bash
  touch debug.log error.log
  touch -m /etc/nginx/nginx.conf
  ```

**SRE Use:** Use to create log placeholders, probe test files, or reset timestamps during automated deployment testing.

#### `mkdir`
- **Purpose:** Create directories, including nested ones.
- **Syntax:** `mkdir [-p] [-m mode] dirname`
- **Examples:**
  ```bash
  mkdir logs
  mkdir -p project/webapp/config
  mkdir -m 700 secure_data
  ```

**SRE Use:** During provisioning scripts or CI/CD steps, pre-creating directories with proper permissions is essential.

#### 🚧 **Failure Case Examples**

**Example 1: Permission Denied**
```bash
mkdir /root/newdir
# Output: mkdir: cannot create directory '/root/newdir': Permission denied
```
**Cause:** The user lacks sufficient privileges to write to `/root`.
**Fix:**
```bash
sudo mkdir /root/newdir
```

**Example 2: Missing Parent Directory**
```bash
mkdir config/logs
# Output: mkdir: cannot create directory 'config/logs': No such file or directory
```
**Fix:** Use `-p` to create parent directories:
```bash
mkdir -p config/logs
```

**Example 3: Directory Already Exists**
```bash
mkdir logs
# Output: mkdir: cannot create directory 'logs': File exists
```
**Fix:**
- Use `mkdir -p logs` to avoid errors if the directory already exists

**SRE Tip:** Always wrap directory creation logic in scripts using `mkdir -p` to ensure idempotency and avoid deployment errors.

#### `touch`
- **Purpose:** Create an empty file or update timestamps.
- **Syntax:** `touch [options] filename(s)`
- **Examples:**
  ```bash
  touch debug.log error.log
  touch -m /etc/nginx/nginx.conf
  ```

**SRE Use:** Use to create log placeholders, probe test files, or reset timestamps during automated deployment testing.

#### `mkdir`
- **Purpose:** Create directories, including nested ones.
- **Syntax:** `mkdir [-p] [-m mode] dirname`
- **Examples:**
  ```bash
  mkdir logs
  mkdir -p project/webapp/config
  mkdir -m 700 secure_data
  ```

**SRE Use:** During provisioning scripts or CI/CD steps, pre-creating directories with proper permissions is essential.

---

### 🔍 **2. Viewing File Contents**

#### `cat`
- Displays entire file content.
- Use only for small files.
  ```bash
  cat /etc/hosts
  cat -n script.sh
  ```

#### `less`
- Interactive viewer for large files.
  ```bash
  less /var/log/syslog
  less -N -S app.log
  less +F app.log  # Real-time monitoring mode
  ```

**Example:** Track and search for errors as they occur in logs:
```bash
less +F /var/log/app.log
# Then type: /ERROR to find the next error line
```

#### `grep` with `tail` or `less`
- Filter lines in real time or during interactive log reviews:
  ```bash
  tail -f /var/log/app.log | grep -i error
  grep -i timeout /var/log/nginx/error.log | less
  ```

**SRE Use:** During active incidents, use `tail -f` piped to `grep` to zero in on problematic log entries such as `500`, `timeout`, or `connection refused` in real time. Pair this with `less` for scrollable history and pattern searches.

#### `cat`
- Displays entire file content.
- Use only for small files.
  ```bash
  cat /etc/hosts
  cat -n script.sh
  ```

#### `less`
- Interactive viewer for large files.
  ```bash
  less /var/log/syslog
  less -N -S app.log
  less +F app.log  # Real-time
  ```

#### `more`
- Simpler than `less`, for paginated viewing.

#### `head` / `tail`
- View beginning (`head`) or end (`tail`) of files.
  ```bash
  head -n 20 nginx.conf
  tail -n 50 app.log
  tail -f app.log  # Real-time logs
  ```

**SRE Use:** Use `tail -f` and `grep` to live-monitor logs during deployments or outages.

---

### 📁 **3. Copying and Moving Files**

These commands are fundamental for creating backups, applying updates safely, rotating logs, and maintaining reproducible environments.

**Common SRE Scenarios:**
- Before editing any file, copy it with a timestamp: `cp -a config.yaml config.yaml.$(date +%F-%H%M)`
- After rotating logs: `mv app.log app.log.1 && touch app.log`
- Move files into backup structures or rollback zones.

#### `cp`
- **Syntax:** `cp [-r] [-a] source dest`
- **Examples:**
  ```bash
  cp -a /etc/nginx /etc/nginx.bak
  cp config.yaml config.yaml.$(date +%F-%H%M)
  ```

#### `mv`
- **Syntax:** `mv source dest`
- **Examples:**
  ```bash
  mv file.txt archive/
  mv -b nginx.conf nginx.conf.old
  ```

**SRE Use:** Always back up config files with timestamped filenames before changes.

---

### 🗑️ **4. Deleting Files and Directories**

These are some of the most dangerous commands on Linux systems and must be handled with caution. When used correctly, they are vital for reclaiming space, cleaning up post-deploy artifacts, and eliminating sensitive data during decommissioning.

**Production-Safe Practices:**
- Always validate paths: `ls /path/to/files/*`
- Use interactive or dry-run modes before mass-deletion
- Consider using `mv` to a safe trash location and auditing later
- Avoid `rm -rf` unless absolutely certain of target contents

#### `rm`
- Deletes files and folders.
- `-i`: prompt, `-f`: force, `-r`: recursive
  ```bash
  rm -i important.conf
  rm -rf old_logs/
  ```

#### `rmdir`
- Removes empty directories only.
  ```bash
  rmdir emptydir
  ```

**SRE Use:** Use `rm -rf` only after confirming target path. Consider using `mv` to a trash folder as a safer strategy.

---

## 🧪 **Practical Exercises**

### **Beginner**
1. Create a directory `Day2_Practice`
2. Create files `a.log`, `b.txt`, and `notes.md`
3. Copy `a.log` to `logs/` and rename `b.txt` to `backup.txt`
4. View `notes.md` with `cat`, `less`, `head`, and `tail`
5. Delete all three files safely

### **Intermediate**
1. Create nested folder `web/{logs,conf}`
2. Create sample config: `echo 'debug=true' > web/conf/app.conf`
3. Use `cp -a` to back up the entire web directory
4. View `app.conf` with `cat`, then modify and `diff` changes
5. Use `tail -f` with live updates from another terminal

### **SRE Application Drill**
```bash
# Create logs, monitor, backup
mkdir -p /tmp/sre/logs
for i in {1..50}; do echo "[INFO] Test log $i" >> /tmp/sre/logs/app.log; done
tail -f /tmp/sre/logs/app.log &
sleep 2 && echo "[ERROR] OutOfMemory" >> /tmp/sre/logs/app.log
cp -a /tmp/sre/logs /tmp/sre/logs_$(date +%F-%H%M)
```
---

## 📝 **Quiz**

### **Beginner**
1. What does `touch file.txt` do?
    - a) Deletes it
    - b) Views its content
    - c) Creates it
    - **Answer:** c

2. Which option makes `mkdir` create parent dirs?
    - a) `-p`
    - b) `-r`
    - c) `-m`
    - **Answer:** a

3. How do you view the top 5 lines of a config file?
    - a) `less -n config`  
    - b) `tail -n 5 config`  
    - c) `head -n 5 config`  
    - **Answer:** c

---

### **Intermediate**
4. Which command shows the most recent 25 lines of a log?
   ```bash
   tail -n 25 filename
   ```

5. Which `cp` option preserves file metadata and directory structure?
    - a) `-f`
    - b) `-a`
    - **Answer:** b

6. What does this command do?
   ```bash
   cp config.conf config.conf.bak.$(date +%F-%H%M)
   ```
   - a) Copies config.conf with a timestamped name
   - b) Compresses the config file
   - c) Deletes the original file
   - **Answer:** a

---

### **SRE Application**
7. Which command sequence is most appropriate during a "disk full" incident?
   ```bash
   a) rm -rf /var/log/*
   b) du -sh /var/* | sort -rh | head -10
   c) mkdir /backup && mv /var/log/* /backup/
   d) Both b and c
   ```
   - **Answer:** d

8. Before modifying a production configuration, what should you do?
   - a) Edit it directly
   - b) Run `rm` on the old file
   - c) Use `cp -a` to back it up
   - **Answer:** c

9. You want to track live error messages in a growing log. Which command fits?
   ```bash
   tail -f /var/log/app.log | grep ERROR
   ```
   - a) Tracks ERROR messages in real-time
   - b) Deletes all errors
   - c) Compresses log on the fly
   - **Answer:** a

### **Beginner**
1. What does `touch file.txt` do?
    - a) Deletes it
    - b) Views its content
    - c) Creates it
    - **Answer:** c

2. Which option makes `mkdir` create parent dirs?
    - a) `-p`
    - b) `-r`
    - c) `-m`
    - **Answer:** a

### **Intermediate**
3. Command to see last 25 lines of a log:
   ```bash
   tail -n 25 filename
   ```

4. Which `cp` option preserves metadata?
    - a) `-f`
    - b) `-a`
    - **Answer:** b

### **SRE Level**
5. What’s safest step before modifying `/etc/nginx/nginx.conf`?
    - **Answer:** `cp -a nginx.conf nginx.conf.bak`

---

## ❓ **FAQs and Troubleshooting**

### 🔎 **Real-World Troubleshooting Examples**

#### 🧪 Example: Logs not updating during incident
- **Symptom:** `tail -f /var/log/app.log` shows no updates despite ongoing errors.
- **Diagnosis:** Application may be writing to a different log file or has stopped logging.
- **Solution:**
  ```bash
  ps aux | grep app
  lsof -p <PID> | grep .log
  ```
  Locate active file descriptor, verify correct log path, and update your monitoring command.

#### 🧪 Example: Config changes silently fail
- **Symptom:** Changes to `/etc/app/config.yml` do not take effect.
- **Diagnosis:** App requires a restart or reload to apply changes.
- **Solution:**
  ```bash
  systemctl status app
  sudo systemctl reload app
  ```
  Always reload the relevant service and confirm with `systemctl status`.

#### 🧪 Example: `cp` fails with permission denied
- **Symptom:** You receive `cp: cannot create regular file ... : Permission denied`
- **Diagnosis:** Copying to a directory owned by root or another service.
- **Solution:**
  ```bash
  sudo cp source.conf /etc/app/
  ```
  Use `ls -ld` to inspect directory permissions.

#### 🧪 Example: Unable to delete logs despite `rm` usage
- **Symptom:** `rm app.log` appears successful but disk usage remains unchanged.
- **Diagnosis:** File is still held open by a running process.
- **Solution:**
  ```bash
  lsof | grep deleted
  systemctl restart app
  ```
  Restart the service to release the file descriptor.

---

**Q1:** How do I preview before deleting with wildcards?
```bash
ls pattern*
rm -i pattern*
```

**Q2:** How do I monitor logs in real time?
```bash
tail -f /var/log/app.log
```

**Q3:** How do I find big files hogging space?
```bash
sudo du -ahx / | sort -rh | head -20
```

**Q4:** Why use `cp -a` instead of `cp -r`?
- `-a` preserves timestamps, permissions, symlinks — ideal for config backups

---

## 📚 **SRE Scenario: Responding to 500 Errors**

```bash
ssh sre@web-prod
cd /var/log/nginx
tail -n 100 error.log | grep -i error
cp -a /etc/nginx/nginx.conf /etc/nginx/nginx.conf.$(date +%F-%H%M)
vim /etc/nginx/nginx.conf
systemctl reload nginx
```
- Investigate the issue through logs
- Back up the current configuration
- Fix the faulty line or misconfigured value
- Reload the web server to apply the fix

### ✅ **Post-Incident Cleanup and Recovery**

```bash
# Archive logs for audit and root cause analysis
mkdir -p /var/log/incidents/$(date +%F)
cp /var/log/nginx/error.log /var/log/incidents/$(date +%F)/error.log

# Roll back config if the fix failed
cp /etc/nginx/nginx.conf.$(date +%F-%H%M) /etc/nginx/nginx.conf
systemctl reload nginx
```

- Store logs for incident documentation
- Prepare for a blameless postmortem by preserving system state
- Use timestamped backups to safely roll back if needed
- Validate fix impact by tailing live logs and confirming resolution

**SRE Best Practice:** Create a checklist of validation steps post-fix (status code monitoring, uptime check, user simulation) to ensure full recovery.

```bash
ssh sre@web-prod
cd /var/log/nginx
tail -n 100 error.log | grep -i error
cp -a /etc/nginx/nginx.conf /etc/nginx/nginx.conf.$(date +%F-%H%M)
vim /etc/nginx/nginx.conf
```
- Investigate
- Back up
- Fix
- Restart

---

## 📚 **Further Learning**

- [Linux Command Line - William Shotts](http://linuxcommand.org/tlcl.php)
- [Explainshell](https://explainshell.com/)
- [Google SRE Workbook](https://sre.google/books/)
- Practice with `/var/log`, `/etc`, and simulated services

---

🎯 **End of Day 2** – You’re now equipped to work confidently with files in a real Linux/SRE environment!

