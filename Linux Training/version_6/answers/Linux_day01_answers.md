# Day 1 Answer Sheet

Below is an **answer sheet** for each quiz question, along with a brief explanation for why that choice is correct (or why the others are not).

---

## 🟢 Beginner (Tier 1)

### 1. Which command shows your current directory?

- **Correct Answer**: **b) `pwd`**  
- **Explanation**:  
  - `pwd` (Print Working Directory) displays the path of your current directory.  
  - `ls` lists the contents of a directory, `cd` changes directories, and `man` shows manual pages.

### 2. How do you list all files, including hidden ones?

- **Correct Answer**: **c) `ls -a`**  
- **Explanation**:  
  - The `-a` (all) flag includes files that start with a dot (`.`), which are hidden by default.  
  - `ls -h` shows human-readable sizes, `ls -l` shows long listing format, `ls -t` sorts by modification time.

### 3. In Linux, which directory is the root of the entire filesystem?

- **Correct Answer**: **c) `/`**  
- **Explanation**:  
  - `/` is the “root” directory at the top of the hierarchy. Everything on a Linux system branches out from `/`.  
  - `/home` is a subdirectory for user home directories, and `/root` is the home directory for the “root” (administrator) user, not the “root” of the filesystem. `/etc` stores configuration files, also not the root.

---

## 🟡 Intermediate (Tier 2)

### 4. To sort files by **modification time** (newest first), which command is correct?

- **Correct Answer**: **b) `ls -lt`**  
- **Explanation**:  
  - Using `-t` with `ls` sorts files by the time they were last modified (most recent first).  
  - `ls -lm`, `ls -lh`, and `ls -la` do not specifically sort by modification time in descending order.

### 5. Which command quickly shows the manual pages for `ls`?

- **Correct Answer**: **c) `man ls`**  
- **Explanation**:  
  - `man` opens the manual page for a given command.  
  - `help ls` might show built-in shell help if `ls` were a built-in (it isn’t in most shells). `ls --man` isn’t a standard syntax. `ls man` would just list any file or directory named `man` in the current folder, so that’s not correct.

### 6. Which directory typically holds system configuration files?

- **Correct Answer**: **b) `/etc`**  
- **Explanation**:  
  - By convention, `/etc` stores system-wide configuration files (e.g., `/etc/ssh/sshd_config`).  
  - `/usr` holds user and system program files, `/var/log` stores logs, and `/bin` contains essential command binaries.

---

## 🔴 SRE-Level (Tier 3)

### 7. During an incident, which location do you **most** likely check first to view recent error logs?

- **Correct Answer**: **b) `/var/log`**  
- **Explanation**:  
  - By default, `/var/log` is the primary location for system logs and many application logs.  
  - `/home/user` is for user data, `/etc` is for config files, and `/tmp` is for temporary files.

### 8. What’s a recommended step before performing a **production** deploy?

- **Correct Answer**: **b) Confirm your current directory with `pwd -P`**  
- **Explanation**:  
  - Ensuring you’re in the correct (usually production) directory prevents accidental deployments in staging or dev environments.  
  - Just listing files or arbitrarily going to `/` doesn’t guarantee you won’t deploy in the wrong place.

### 9. Which hidden files might contain environment-specific data?

- **Correct Answer**: **a) Files with `.env` or `.bashrc` in the name**  
- **Explanation**:  
  - Many environment variables and configurations are stored in “dotfiles” (files starting with `.`), such as `.env` or `.bashrc`.  
  - `.conf` files aren’t necessarily hidden (they can be in `/etc/` or normal directories). There’s no file named `.home` by default that always stores environment data.

---

**Note**: These explanations align with standard Linux usage and SRE best practices, helping you understand not only *which* answer is correct, but *why* it’s the recommended approach in real-world environments.
