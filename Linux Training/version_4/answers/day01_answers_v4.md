# 📝 **Quiz Questions with Explicit Answers and Explanations**

---

## 🟢 **Beginner Tier:**

### 1. **Which command explicitly shows your current directory?**

**Answer:** c) `pwd`

**Explanation:**  

- **`pwd` (print working directory)** explicitly shows your current directory path, assisting you in verifying your location.
- **Incorrect Choices:**  
  - `ls` lists directory contents, not your current directory path.
  - `cd` changes directories but does not explicitly display your current path.
  - `dir` is not standard Linux; more commonly used in Windows.

---

### 2. **To list all files, including hidden ones, explicitly type:**

**Answer:** `ls -a`

**Explanation:**  

- The explicit `-a` (all) flag with `ls` displays hidden files (files beginning with a dot `.`), explicitly helping you locate hidden configuration files or directories.

---

### 3. **You need explicit quick documentation about the `cd` command. Which command would you type?**

**Answer:** a) `cd --help`

**Explanation:**  

- Explicitly typing `--help` after any Linux command quickly shows usage and options. This provides concise documentation without needing detailed manual pages.

**Incorrect Choices:**  

- `ls cd`, `pwd cd`, `cd info` explicitly don't provide help documentation for commands.

---

## 🟡 **Intermediate Tier:**

### 1. **You explicitly want to sort files by modification time (newest first). Which command correctly accomplishes this?**

**Answer:** c) `ls -lt`

**Explanation:**  

- Explicitly, the `-t` flag sorts files by modification time, newest first. The `-l` explicitly shows detailed file information.

**Incorrect Choices:**  

- `ls -lh`: sorted by name, human-readable sizes.
- `ls -la`: detailed info and hidden files, no sorting by time.
- `ls -lr`: sorts in reverse alphabetical order, not by time.

---

### 2. **To explicitly navigate back to the previous directory you visited, type:**

**Answer:** `cd -`

**Explanation:**  

- The explicit command `cd -` toggles between the current and previously visited directories, allowing quick back-and-forth navigation, essential during rapid troubleshooting.

---

### 3. **You explicitly suspect hidden configuration files might be causing issues. Which explicit command lists all hidden files with detailed information?**

**Answer:** b) `ls -la`

**Explanation:**  

- Explicitly, the combined flags `-l` (long detailed format) and `-a` (show all including hidden files) provide complete visibility into potentially problematic hidden configuration files.

**Incorrect Choices:**  

- `ls -h`: human-readable sizes without listing hidden files.
- `ls -all`: incorrect syntax.
- `ls -hidden`: invalid flag.

---

## 🔴 **SRE-Level Tier:**

### 1. **During an incident, you explicitly need to find the five largest log files quickly. Which command combination explicitly achieves this?**

**Answer:** c) `ls -lhS | head -5`

**Explanation:**  

- `-l`: Explicit detailed listing.
- `-h`: Human-readable sizes (MB, GB explicitly).
- `-S`: Explicitly sorts by size, largest first.
- `| head -5`: Explicitly outputs the first 5 results, perfect for rapid troubleshooting.

**Incorrect Choices:**  

- `ls -lah`: sorted by name, not size.
- `ls -lt`: sorts by modification time, not size.
- `ls -lr`: reverse alphabetical sorting.

---

### 2. **Explicitly provide a single-line command that navigates into `/var/log`, explicitly lists files sorted by size, and immediately returns to your previous location:**

**Answer:**

```bash
cd /var/log && ls -lhS && cd -
```

**Explanation:**  

- `cd /var/log`: Explicit navigation.
- `ls -lhS`: Explicitly sorts files by size, human-readable.
- `cd -`: Explicitly returns you immediately to the previous directory, efficient for quick checks during incidents.

---

### 3. **You explicitly need to automate checking recently modified `.conf` files in `/etc`. Which command explicitly lists these files sorted by newest modification?**

**Answer:** c) `ls -lta /etc/*.conf`

**Explanation:**  

- `-l`: Detailed explicit listing.
- `-t`: Explicit sorting by modification time (newest first).
- `-a`: Includes all explicitly matched files (though explicitly redundant here as `.conf` files are typically not hidden).

**Incorrect Choices:**  

- `ls -lSh`: sorts by size, not modification time.
- `ls -lah`: no sorting by time explicitly.
- `ls -ltrh`: sorts explicitly by time but reversed (oldest first).
