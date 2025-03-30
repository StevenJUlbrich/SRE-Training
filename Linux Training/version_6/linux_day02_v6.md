# **Day 2: File Manipulation for SREs — Comprehensive Merged Module**

Welcome to **Day 2** of our Linux SRE Training Series. This module merges the systematic tiered structure of one training resource with the rich contextual explanations from another, ensuring you not only learn **what** commands do, but also **how** and **why** to use them effectively in real-world SRE scenarios.

---

## **1. Introduction**

File manipulation in Linux is a cornerstone skill for **Site Reliability Engineers (SREs**). The ability to create, view, move, copy, and remove files and directories under time pressure is essential for tasks like:

- Backing up or restoring configurations  
- Quickly analyzing logs during incidents  
- Automating housekeeping to ensure system reliability  

**What You’ll Learn Today**  

- **Beginner**: Basics of creating and viewing files  
- **Intermediate**: Practical multi-step operations with efficiency and safety  
- **SRE-Level**: Advanced usage and automation for real-world production scenarios

### **Objectives Per Skill Tier**

**Beginner Objectives (3)**  

1. Create and remove files and directories safely (`touch`, `mkdir`, `rm`, `rmdir`).  
2. View file contents (all or partial) using essential commands (`cat`, `less`, `more`, `head`, `tail`).  
3. Understand fundamental concepts of file operations and where to locate files in the filesystem.

**Intermediate Objectives (3)**  

1. Copy and move files/directories with best practices (using flags like `-r`, `-p`, `-a`, `-i` in `cp` and `mv`).  
2. Start to incorporate performance considerations for large file operations (logfiles, big directories).  
3. Safely handle multi-step tasks, like archiving logs and reorganizing directory structures.

**SRE-Level Objectives (3)**  

1. Automate file management operations (scripts, backups, log rotation).  
2. Integrate file operations with real-time troubleshooting (e.g., streaming logs with `tail -f`).  
3. Apply advanced security and auditing practices (preserving timestamps, permissions, ownership, and understanding risk).

### **Connection to Previous and Future Topics**

- **Day 1** introduced navigating the Linux filesystem and using built-in help (man pages, `--help`) to understand commands.  
- **Today** (Day 2) focuses on how to manipulate files within that filesystem.  
- **Day 3** will cover file permissions, ownership, and security — crucial for ensuring that only the right users modify or view certain files.

---

## **2. Core Concepts**

Below are fundamental ideas behind file manipulation, each explained with an analogy, technical depth, SRE application, and potential system impacts.

1. **File Creation**  
   - **Beginner Analogy**: Placing a blank sheet of paper into a new folder.  
   - **Technical Explanation**: Use `touch` to create an empty file or update timestamps. Use `mkdir` to create directories.  
   - **SRE Application**: Placeholders for logs, scratch config files for quick tests.  
   - **System Impact**: Minimal overhead except when creating massive numbers of files in a loop.

2. **Viewing Files**  
   - **Beginner Analogy**: Reading a stack of papers page by page or line by line.  
   - **Technical Explanation**: Commands like `cat` (entire file), `less`/`more` (paged), `head`/`tail` (top/bottom).  
   - **SRE Application**: Check logs and configs under time pressure, e.g., during outages.  
   - **System Impact**: Large files can consume I/O; streaming commands can raise CPU usage if logs are very active.

3. **Copying and Moving**  
   - **Beginner Analogy**: Photocopying a paper vs. physically relocating it.  
   - **Technical Explanation**: `cp` duplicates file contents; `mv` renames or relocates them.  
   - **SRE Application**: Backups, archiving logs, reorganizing or versioning config files.  
   - **System Impact**: Copying large files saturates disk I/O; moving on the same disk is quick (just metadata changes).

4. **Deleting Files**  
   - **Beginner Analogy**: Throwing away unnecessary papers or folders.  
   - **Technical Explanation**: `rm` removes files, `rm -r` removes directories, `rmdir` only removes empty directories.  
   - **SRE Application**: Clearing stale logs, housekeeping older backups, or removing temporary files.  
   - **System Impact**: Freed space, but also risk of accidental data loss. Deletion overhead on large directories can be significant.

5. **Reliability Engineering Considerations**  
   - **Backups**: Before changing production configs, create a copy so you can revert if something breaks.  
   - **Performance**: Large file operations can slow critical services if done carelessly in production hours.  
   - **Security**: Ensure sensitive data isn’t copied to unsecured locations; ensure logs are archived before removal.  
   - **Automation**: Scripts must handle error cases (low disk space, permission errors) gracefully.

---

## **3. Detailed Command Breakdowns**

Below are **11** key commands for Day 2. Each is broken down with an overview, syntax table, tiered examples, and instructional notes.

---

### **Command: touch (create/update file timestamps)**

**Command Overview:**  
Use `touch` to create new empty files if they don’t exist, or update a file’s last access/modify timestamps. SREs often create placeholder files or manipulate timestamps for scripts that rely on file age.

**Syntax & Flags:**

| Flag/Option | Syntax Example        | Description                                          | SRE Usage Context                                    |
|-------------|-----------------------|------------------------------------------------------|------------------------------------------------------|
| *(none)*    | `touch myfile.txt`    | Creates file if not present, else updates timestamps.| Quick creation of placeholder or test files.        |
| `-a`        | `touch -a myfile.txt` | Updates only the file’s access time.                 | Testing read-based triggers or behaviors.           |
| `-m`        | `touch -m myfile.txt` | Updates only the file’s modification time.           | Script-based checks that rely on modify times.      |
| `-t`        | `touch -t 202503251200 file` | Sets a custom timestamp (YYYYMMDDhhmm).        | Simulate old/new files for log rotation tests.      |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# Create a new empty file named 'demo.log'
$ touch demo.log

# Verify with ls -l
-rw-r--r-- 1 user user 0 Mar 29 09:00 demo.log
```

- 🟡 **Intermediate Example:**

```bash
# Update only the access time of 'report.txt'
$ touch -a report.txt

$ stat report.txt
# Notice the 'Access' timestamp has changed, 'Modify' is unchanged
```

- 🔴 **SRE-Level Example:**

```bash
# Simulate an older timestamp for a script that rotates logs if older than X days
$ touch -t 202303010700 service.log

# Now the rotation script sees 'service.log' as older, triggering action
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** `touch file1 file2 file3` creates multiple empty files at once.  
- 🧠 **Beginner Tip:** If you `touch` an existing file, its size doesn’t change, only its timestamps.

- 🔧 **SRE Insight:** Adjusting timestamps can help debug scripts that rely on `find` or `make` by simulating older/newer files.  
- 🔧 **SRE Insight:** Used in load tests to create placeholder logs or test concurrency issues with rotating files.

- ⚠️ **Common Pitfall:** Expecting `touch` to change file contents — it doesn’t.  
- ⚠️ **Common Pitfall:** Accidentally misusing custom timestamps can break chronological log analysis.

- 🚨 **Security Note:** Attackers might alter timestamps to hide malicious activity. Rely on cryptographic checksums for critical logs.  
- 💡 **Performance Impact:** Very low. Metadata operations are generally cheap unless repeated en masse in massive directories.

---

### **Command: mkdir (make directory)**

**Command Overview:**  
`mkdir` creates directories. SREs need directory structures for configs, logs, and backups. It’s straightforward but essential for organizing large environments.

**Syntax & Flags:**

| Flag/Option | Syntax Example                | Description                                               | SRE Usage Context                             |
|-------------|-------------------------------|-----------------------------------------------------------|-----------------------------------------------|
| *(none)*    | `mkdir logs`                 | Create a single directory named `logs`.                   | Basic directory setup for logs/configs.       |
| `-p`        | `mkdir -p /path/sub1/sub2`   | Create parent directories as needed.                      | Creating nested paths in automation scripts.  |
| `-m`        | `mkdir -m 700 secure_folder` | Create directory with specified permissions immediately.  | Lock down directories containing secrets.     |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# Create a directory named 'projects'
$ mkdir projects

# Verify directory creation:
$ ls -l
drwxr-xr-x 2 user user 4096 Mar 29 09:10 projects
```

- 🟡 **Intermediate Example:**

```bash
# Create nested directories for an application release
$ mkdir -p /var/www/myapp/releases/v1.2.3

# This ensures /var/www/myapp/releases exist before creating 'v1.2.3'
```

- 🔴 **SRE-Level Example:**

```bash
# Create a directory for sensitive config files with restricted permissions
$ mkdir -m 700 /etc/secure_configs

# Only the owner (often root) has read/write/execute permissions
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Use `mkdir -p` to avoid errors if parent directories don’t exist.  
- 🧠 **Beginner Tip:** If you see “File exists” errors, the directory likely already exists — double-check with `ls`.

- 🔧 **SRE Insight:** Often used in CI/CD or provisioning scripts (`ansible`, `terraform`) to ensure consistent folder structures.  
- 🔧 **SRE Insight:** Consider date-based directories for log partitioning: `mkdir -p /var/log/app/$(date +%Y/%m/%d)`.

- ⚠️ **Common Pitfall:** Omitting `-p` can break automation if the parent path isn’t already there.  
- ⚠️ **Common Pitfall:** Setting overly permissive modes (e.g., `chmod 777`) can expose sensitive data.

- 🚨 **Security Note:** Setting `-m 700` is essential when storing credentials or private keys.  
- 💡 **Performance Impact:** Negligible for single directories. Large-scale directory creation (thousands) can spike I/O.

---

### **Command: cat (concatenate)**

**Command Overview:**  
`cat` outputs the content of files to standard output. It’s best for small or moderate-size files. For SREs, `cat` is handy to quickly confirm the contents of config or log files.

**Syntax & Flags:**

| Flag/Option | Syntax Example     | Description                                                  | SRE Usage Context                                     |
|-------------|--------------------|--------------------------------------------------------------|-------------------------------------------------------|
| *(none)*    | `cat file.txt`     | Display the entire file.                                     | Quick checks of small files.                          |
| `-n`        | `cat -n file.txt`  | Number each line in the output.                             | Referencing line numbers in error logs/configs.       |
| `-A`        | `cat -A file.txt`  | Show non-printing characters (whitespace, line endings).     | Debugging hidden formatting issues or special chars.  |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# View a small config file
$ cat config.ini
[server]
port=8080
debug=true
```

- 🟡 **Intermediate Example:**

```bash
# Display file contents with line numbers
$ cat -n error.log
     1  ERROR: Connection refused
     2  ERROR: Database timeout
     3  INFO: Retrying...
```

- 🔴 **SRE-Level Example:**

```bash
# Combine multiple small logs and filter for critical lines
$ cat /var/log/app1.log /var/log/app2.log | grep CRITICAL > combined.log

# All CRITICAL entries from both logs are saved to combined.log
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** For big files, use `less` or `more` instead of `cat` to avoid scrolling floods.  
- 🧠 **Beginner Tip:** Redirection (`>`) overwrites, while `>>` appends.

- 🔧 **SRE Insight:** Pair `cat` with `grep`, `awk`, or `sed` to quickly process logs.  
- 🔧 **SRE Insight:** Sometimes replaced by `less file` to avoid loading entire file into screen output.

- ⚠️ **Common Pitfall:** `cat largefile | less` is redundant; `less largefile` is enough.  
- ⚠️ **Common Pitfall:** Overwrites can happen if you misuse `> file` in a pipeline.

- 🚨 **Security Note:** Dumping credentials or tokens on screen in multi-user environments is risky.  
- 💡 **Performance Impact:** Minimal for smaller files; large files can cause high I/O if piped into other processes.

---

### **Command: less (file pager)**

**Command Overview:**  
`less` lets you scroll forward and backward through file content. Ideal for large files (e.g., logs) because you don’t load the entire file into memory at once. Searching within `less` is efficient for real-time debugging.

**Syntax & Flags:**

| Flag/Option | Syntax Example            | Description                                           | SRE Usage Context                                    |
|-------------|---------------------------|-------------------------------------------------------|------------------------------------------------------|
| *(none)*    | `less largefile.log`     | Opens file in a pager for navigation.                 | Day-to-day log analysis in production.              |
| `-N`        | `less -N config.yml`     | Display line numbers.                                 | Quickly reference lines in configs or scripts.      |
| `-S`        | `less -S longfile.log`   | Disable line wrapping (chop lines).                   | Helpful for wide log lines or large JSON objects.    |
| `+F`        | `less +F /var/log/syslog`| Follow mode, akin to `tail -f`, with ability to scroll| Real-time log watching without losing scrollback.   |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# Read a system log with less
$ less /var/log/syslog

# Use Up/Down keys to scroll, 'q' to quit
```

- 🟡 **Intermediate Example:**

```bash
# View line numbers and avoid wrapping
$ less -N -S /var/log/nginx/error.log
```

- 🔴 **SRE-Level Example:**

```bash
# Combine multiple logs, then open them with less for search
$ cat /var/log/app/*.log | less

# Inside less, you can:
#   /ERROR      -> search forward for "ERROR"
#   n           -> jump to next match
#   Shift+F     -> toggle follow mode
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Press `/pattern` to search forward, `n` for next match. Press `q` to quit.  
- 🧠 **Beginner Tip:** `F` inside `less` toggles follow mode.

- 🔧 **SRE Insight:** `less +F` can replicate `tail -f` but allows you to scroll up, then resume real-time view.  
- 🔧 **SRE Insight:** Use for quick scanning of large compressed logs via `zless`.

- ⚠️ **Common Pitfall:** Large searches in huge files can consume memory and CPU.  
- ⚠️ **Common Pitfall:** If you exit follow mode incorrectly, you might remain stuck if you don’t press Ctrl+C and then `q`.

- 🚨 **Security Note:** Some logs can contain private data (e.g., tokens). Confirm file permissions first.  
- 💡 **Performance Impact:** Generally good for large files because it reads content lazily.

---

### **Command: more (basic pager)**

**Command Overview:**  
`more` is an older, simpler pager than `less`. It only supports forward movement (no scrolling backward). Useful in minimal environments or rescue shells where `less` isn’t available.

**Syntax & Flags:**

| Flag/Option | Syntax Example     | Description                                  | SRE Usage Context              |
|-------------|--------------------|----------------------------------------------|--------------------------------|
| *(none)*    | `more file.log`    | Display file in pages, press space to scroll.| Quick checking on minimal distros. |
| `-d`        | `more -d file.log` | Show navigation prompts.                     | Helps new users see navigation keys. |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# Display file with paging
$ more /etc/passwd
--More-- (Press space to continue, q to quit)
```

- 🟡 **Intermediate Example:**

```bash
# Show instructions on navigating
$ more -d /var/log/messages
```

- 🔴 **SRE-Level Example:**

```bash
# In a minimal rescue environment with no 'less':
$ more /mnt/chroot/var/log/boot.log
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Press `Space` to go forward one page, `q` to quit. No backward scroll.  
- 🧠 **Beginner Tip:** If you overshoot, you must restart since you can’t go back.

- 🔧 **SRE Insight:** Rarely used if `less` is installed. But invaluable if `less` is unavailable (initrd or minimal rescue mode).  
- 🔧 **SRE Insight:** In tight environments, `more` has a smaller footprint than `less`.

- ⚠️ **Common Pitfall:** Expecting to scroll up can cause confusion.  
- ⚠️ **Common Pitfall:** Large file partial reads can still be slow if you page too quickly.

- 🚨 **Security Note:** Same considerations with sensitive logs.  
- 💡 **Performance Impact:** Similar to `less` for smaller files; lacking backward navigation means fewer advanced features.

---

### **Command: head (view file start)**

**Command Overview:**  
`head` displays the first few lines (default 10) of a file. Great for quickly checking file headers, log intros, or verifying data formats.

**Syntax & Flags:**

| Flag/Option | Syntax Example          | Description                                              | SRE Usage Context                             |
|-------------|-------------------------|----------------------------------------------------------|-----------------------------------------------|
| *(none)*    | `head file.txt`        | Shows the first 10 lines by default.                     | Quick peek at top of file (logs, configs).    |
| `-n`        | `head -n 20 file.txt`  | Specify the number of lines to show.                     | View a custom portion of the beginning.       |
| `-c`        | `head -c 100 file.txt` | Shows the first 100 bytes of a file.                     | Check partial binary data or encoding tests.  |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# View the first 10 lines of syslog
$ head /var/log/syslog
```

- 🟡 **Intermediate Example:**

```bash
# View the first 20 lines to see any initial errors
$ head -n 20 app.log
```

- 🔴 **SRE-Level Example:**

```bash
# Quickly verify the start of a large compressed log
$ zcat /var/log/app-archive.gz | head -n 15

# Confirms correct compression and initial log entries
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** By default, `head` is 10 lines. Use `-n` to adjust.  
- 🧠 **Beginner Tip:** `head` stops reading after showing the specified lines, making it fast on large files.

- 🔧 **SRE Insight:** Useful in pipelines to sample only the top portion. For instance, `grep ERROR huge.log | head -n 50` to see if errors exist.  
- 🔧 **SRE Insight:** Combine with `tail` to see both ends of a log quickly.

- ⚠️ **Common Pitfall:** For compressed files, you must pipe through `zcat` or similar. Direct `head bigfile.gz` will show gibberish.  
- ⚠️ **Common Pitfall:** Relying solely on the header might miss mid-file or end-file issues.

- 🚨 **Security Note:** Header lines might contain credentials in config files. Check carefully.  
- 💡 **Performance Impact:** Minimal read overhead.

---

### **Command: tail (view file end)**

**Command Overview:**  
`tail` displays the last few lines of a file. In `-f` or `-F` mode, it shows lines appended to the file in real time, which is critical for incident monitoring.

**Syntax & Flags:**

| Flag/Option | Syntax Example          | Description                                          | SRE Usage Context                                 |
|-------------|-------------------------|------------------------------------------------------|---------------------------------------------------|
| *(none)*    | `tail file.log`        | Shows last 10 lines by default.                      | Quick peek at recent log entries.                |
| `-n`        | `tail -n 20 file.log`  | Show last 20 lines.                                  | Deeper look at the log tail.                      |
| `-f`        | `tail -f file.log`     | Follow mode: update output as file grows.            | Real-time monitoring (incident, debugging).       |
| `-F`        | `tail -F file.log`     | Follow mode with log rotation detection.             | Production logs that rotate regularly.            |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# Show the last 10 lines of a log
$ tail /var/log/messages
```

- 🟡 **Intermediate Example:**

```bash
# Show the last 50 lines
$ tail -n 50 /var/log/app/debug.log
```

- 🔴 **SRE-Level Example:**

```bash
# Real-time monitoring in a rotating environment
$ tail -F /var/log/myapp/current.log

# Continues to follow new log file if rotation occurs
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Press Ctrl+C to stop `tail -f`.  
- 🧠 **Beginner Tip:** If a file is not actively written, you won’t see new lines until they appear.

- 🔧 **SRE Insight:** In an outage, you might run multiple `tail -f` commands in separate terminals for different logs.  
- 🔧 **SRE Insight:** `-F` is safer than `-f` when logs rotate (common in production).

- ⚠️ **Common Pitfall:** A runaway log might flood your terminal. Use filters (`grep`) or watch usage if the log grows rapidly.  
- ⚠️ **Common Pitfall:** Focusing only on the end could miss earlier root causes.

- 🚨 **Security Note:** Tailing logs with sensitive info (tokens, user data) can leak data if done on shared terminals.  
- 💡 **Performance Impact:** Constantly reading a high-volume log can increase CPU/I/O usage. Tools like `journald` or external log aggregators can offload this.

---

### **Command: cp (copy)**

**Command Overview:**  
`cp` duplicates files and directories. SREs commonly do this for backups, configuration versioning, and moving critical data between directories.

**Syntax & Flags:**

| Flag/Option | Syntax Example                    | Description                                                    | SRE Usage Context                                   |
|-------------|-----------------------------------|----------------------------------------------------------------|-----------------------------------------------------|
| *(none)*    | `cp source.txt dest.txt`          | Copy `source.txt` → `dest.txt`.                                | Basic file duplication.                             |
| `-r`        | `cp -r /src/dir /dest/dir`        | Recursively copy directories.                                  | Copy entire folder structures (logs, config sets).  |
| `-p`        | `cp -p file1 file2`              | Preserve permissions, ownership, timestamps.                   | Maintain metadata for audits, backups.             |
| `-a`        | `cp -a /src/dir /dest/dir`        | Archive mode (same as `-dpr`): preserve everything including links. | Full backups or migrations that keep symbolic links. |
| `-i`        | `cp -i source.txt dest.txt`       | Interactive prompt before overwrite.                           | Avoid accidental overwrites in production.          |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# Copy 'file1.txt' to 'file2.txt'
$ cp file1.txt file2.txt

# Verify both exist
$ ls
file1.txt  file2.txt
```

- 🟡 **Intermediate Example:**

```bash
# Copy a directory recursively preserving permissions
$ cp -rp /var/www/ /home/user/www_backup/

# Ownership and timestamps stay intact
```

- 🔴 **SRE-Level Example:**

```bash
# Archive production configs with everything preserved
$ cp -a /etc/nginx/ /backup/nginx_$(date +%Y%m%d)

# Perfect for rollback if a deployment fails
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** By default, `cp` overwrites existing files silently. Use `-i` for safety.  
- 🧠 **Beginner Tip:** `cp /source /destination_dir/` retains the same filename in `destination_dir`.

- 🔧 **SRE Insight:** `cp -a` is crucial for preserving symbolic links and exact permissions in production backups.  
- 🔧 **SRE Insight:** For remote or large-scale copying, consider `rsync` for better efficiency and checksums.

- ⚠️ **Common Pitfall:** Forgetting hidden files when copying directories if not using `-r` properly.  
- ⚠️ **Common Pitfall:** Large recursive copies can fill disks quickly.

- 🚨 **Security Note:** Make sure not to copy sensitive files into publicly readable locations.  
- 💡 **Performance Impact:** Large copies can monopolize disk I/O, impacting other services.

---

### **Command: mv (move/rename)**

**Command Overview:**  
`mv` changes a file or directory’s location or name. On the same filesystem, it’s nearly instant (metadata update). Across filesystems, it copies then deletes.

**Syntax & Flags:**

| Flag/Option | Syntax Example             | Description                                              | SRE Usage Context                                   |
|-------------|----------------------------|----------------------------------------------------------|-----------------------------------------------------|
| *(none)*    | `mv old.txt new.txt`      | Renames `old.txt` to `new.txt`.                          | Simple renaming or relocating.                      |
| `-i`        | `mv -i source target`     | Prompt before overwrite if target exists.                | Safe approach for critical directories.             |
| `-v`        | `mv -v file1 file2`       | Verbose output, shows rename steps.                      | Tracking rename operations in scripts.              |
| `-b`        | `mv -b file file.bak`     | Create backup of the destination file if it exists.      | Minimizing risk of overwriting important data.      |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# Rename 'test.txt' to 'report.txt'
$ mv test.txt report.txt
```

- 🟡 **Intermediate Example:**

```bash
# Move multiple logs to an archive directory with verbose output
$ mv -v /var/log/app/*.log /var/log/app/archive/
/var/log/app/app1.log -> /var/log/app/archive/app1.log
/var/log/app/app2.log -> /var/log/app/archive/app2.log
```

- 🔴 **SRE-Level Example:**

```bash
# Rename a config file while creating a backup if the new name already exists
$ mv -b /etc/myapp/config.yml /etc/myapp/config.yml.old
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Moving a file to a directory without specifying a new filename keeps the original name.  
- 🧠 **Beginner Tip:** If you move a file to a different filesystem, it behaves like a copy + delete.

- 🔧 **SRE Insight:** Atomic deployment often involves `mv config.new config` to swap configurations in one step.  
- 🔧 **SRE Insight:** For large folders across network shares, use robust copy-check-then-remove approach.

- ⚠️ **Common Pitfall:** Overwriting existing files if you forget `-i` or `-b`.  
- ⚠️ **Common Pitfall:** If the destination is on another partition, an aborted move can lead to partial data in both locations.

- 🚨 **Security Note:** Accidentally moving private files to a public path can cause leaks. Double-check paths.  
- 💡 **Performance Impact:** Same-filesystem moves are instant; cross-filesystem moves can be slow for large files.

---

### **Command: rm (remove)**

**Command Overview:**  
`rm` permanently deletes files. With `-r`, you can remove directories and their contents. This is powerful and potentially dangerous in production if misused.

**Syntax & Flags:**

| Flag/Option | Syntax Example       | Description                                                  | SRE Usage Context                                  |
|-------------|----------------------|--------------------------------------------------------------|----------------------------------------------------|
| *(none)*    | `rm file.txt`        | Removes the specified file.                                  | Routine cleanup of single files.                  |
| `-r`        | `rm -r folder`       | Recursively remove folder and all sub-files.                 | Deleting directory trees (logs, backups).          |
| `-i`        | `rm -i file.txt`     | Interactive mode, prompts before removing each file.         | Safer approach for critical data.                 |
| `-f`        | `rm -f file.txt`     | Force removal, no prompts or warnings.                       | Automated scripts that must proceed on errors.    |
| `-v`        | `rm -v file.txt`     | Verbose output, printing each removed file.                  | Logging deletions in housekeeping scripts.         |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# Remove a single file
$ rm old_file.txt

$ ls old_file.txt
ls: cannot access 'old_file.txt': No such file or directory
```

- 🟡 **Intermediate Example:**

```bash
# Remove a directory and contents interactively
$ rm -ri archive/
rm: descend into directory 'archive'? y
rm: remove 'archive/old.log'? y
...
```

- 🔴 **SRE-Level Example:**

```bash
# Forcefully remove old logs with verbose output
$ rm -rfv /var/log/app/old_logs/
removed '/var/log/app/old_logs/log1'
removed directory '/var/log/app/old_logs'
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Once a file is removed, it can’t be easily recovered. Always be sure.  
- 🧠 **Beginner Tip:** `rm file1 file2 file3` removes multiple files in one command.

- 🔧 **SRE Insight:** Consider moving files to a “trash” directory first, then removing after verification.  
- 🔧 **SRE Insight:** Confirm backups or archives exist for logs that must be retained for compliance.

- ⚠️ **Common Pitfall:** A stray space or wildcard can wipe out more than intended (e.g., `rm -rf / var/log`).  
- ⚠️ **Common Pitfall:** Using `-f` in automation can mask errors (e.g., permission issues or non-existent paths).

- 🚨 **Security Note:** Deleting logs can hamper incident investigations or audits. Archive first.  
- 💡 **Performance Impact:** Large recursive deletions can spike disk I/O; schedule them during low usage.

---

### **Command: rmdir (remove directory)**

**Command Overview:**  
`rmdir` removes **empty** directories only. For directories with contents, use `rm -r`. SREs sometimes use `rmdir` in scripts to clean up empty placeholders.

**Syntax & Flags:**

| Flag/Option | Syntax Example                        | Description                                                      | SRE Usage Context                               |
|-------------|---------------------------------------|------------------------------------------------------------------|-------------------------------------------------|
| *(none)*    | `rmdir empty_dir`                     | Removes `empty_dir` if it has no files/subdirectories.           | Safe removal of placeholders.                   |
| `-p`        | `rmdir -p parent/child/grandchild`    | Removes nested directories if each is empty.                     | Cleaning up nested empty structures easily.     |

**Tiered Examples:**

- 🟢 **Beginner Example:**

```bash
# Remove an empty directory 'temp'
$ rmdir temp
```

- 🟡 **Intermediate Example:**

```bash
# Remove nested empty directories
$ rmdir -p logs/archive/2025
# Removes 2025, then archive, then logs if each is empty
```

- 🔴 **SRE-Level Example:**

```bash
# Automated cleanup of leftover empty dirs
$ find /tmp -type d -empty -exec rmdir {} \;

# Recursively removes all empty directories under /tmp
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** If the directory isn’t empty, `rmdir` fails. Use `rm -r directory` if you truly want to delete everything inside.  
- 🧠 **Beginner Tip:** To remove multiple empty directories, list them: `rmdir dir1 dir2 dir3`.

- 🔧 **SRE Insight:** Helps keep folder structures tidy post-deployment if certain directories remain empty.  
- 🔧 **SRE Insight:** Combine `rmdir` with scripts that verify emptiness before removal.

- ⚠️ **Common Pitfall:** Hidden files (`.gitignore`, `.env`) can cause “Directory not empty” errors.  
- ⚠️ **Common Pitfall:** Not a replacement for `rm -r` when the directory has contents.

- 🚨 **Security Note:** Double-check that the directory is indeed empty (no hidden files).  
- 💡 **Performance Impact:** Minimal, generally a quick metadata check.

---

## **4. System Effects of File Commands**

1. **Filesystem & Metadata Updates**  
   - Every create/move/modify or removal updates inodes, timestamps, and directory entries.  
   - Large-scale operations can fragment the disk or fill the inode table.

2. **System Resource Consumption**  
   - Copying/moving huge files or recursively handling many files consumes disk I/O, CPU, and memory.  
   - Repetitive `tail -f` on active logs can push CPU usage if logs are massive.

3. **Security Implications**  
   - Improper handling of sensitive data can expose secrets (accidental copy to public directory).  
   - Logs containing PII must be removed or archived securely, respecting compliance (GDPR, etc.).

4. **Monitoring & Auditing**  
   - SRE teams often track file operations via auditing tools (`auditd`, logging solutions).  
   - Deletions or overwrites in production may trigger alerts.

---

## **5. Hands-On Exercises**

### **Beginner Tier (3 Exercises)**

1. **Simple File/Directory Practice**  
   - Create a directory named `day2_practice`.  
   - Inside it, run `touch file1.txt file2.txt`.  
   - Verify their existence using `ls`; remove `file2.txt` using `rm` and confirm it’s gone.

2. **View Contents**  
   - In `file1.txt`, add text: `echo "Hello, SRE!" > file1.txt`.  
   - Use `cat`, `head`, and `tail` to view the file.  
   - Practice scrolling it with `less`.

3. **Build and Remove Nested Directories**  
   - Create nested directories with `mkdir -p nested/dir/structure`.  
   - Observe what happens when you try to remove `structure` with `rmdir`.  
   - Remove it fully with `rm -r nested/dir/structure`.

---

### **Intermediate Tier (3 Exercises)**

1. **Copying and Moving**  
   - Create a folder `logs` with `mkdir logs`.  
   - Generate a log file: `for i in {1..50}; do echo "Log line $i" >> logs/app.log; done`.  
   - Copy `logs/app.log` to `logs/app_backup.log` preserving timestamps (`-p`).  
   - Move `logs/app_backup.log` to `archive/` (create `archive` if needed) and rename it `old_app.log`.

2. **Partial Viewing and Large File**  
   - Extend `logs/app.log` by appending 50 more lines.  
   - Use `head -n 10 logs/app.log` and `tail -n 10 logs/app.log` to verify new entries.  
   - Open it with `less -N` to see line numbers.  
   - Filter lines containing “Log line 75” using `cat logs/app.log | grep "Log line 75"`.

3. **Automated Cleanup**  
   - Create multiple empty files in a directory: `touch cleanup{1..5}.tmp`.  
   - Write a small script (or command sequence) that moves all `.tmp` files to a `trash` folder.  
   - If the `trash` folder doesn’t exist, create it automatically with `mkdir -p`.

---

### **SRE-Level Tier (3 Exercises)**

1. **Timestamp Rotation Simulation**  
   - Create a file `old.log` and set its timestamp to a week ago: `touch -t 202303010800 old.log`.  
   - Write a script that checks if any `.log` files are older than 5 days, then moves them to `archive/`.  
   - Validate by listing the archive directory and confirming the move.

2. **Live Log Analysis**  
   - In one terminal, run `tail -F /var/log/syslog`.  
   - Trigger some events: `sudo systemctl restart cron` or other system service.  
   - Observe real-time logs.  
   - Copy relevant lines with errors to `incident.log` using `grep` or `sed` piped from `tail -F` (e.g., `tail -F /var/log/syslog | grep -i error` in a second pane).

3. **Recursive Backup and Cleanup**  
   - Recursively copy `/etc/nginx/` to a backup location (`/backup/nginx_YYYYMMDD`) using `cp -a`.  
   - Remove any leftover `.bak` files older than 7 days in `/backup/nginx_*`.  
   - Ensure the removal step is logged (e.g., `rm -v` or log output into a file).

---

## **6. Quiz Questions**

### **Beginner Level (4 Questions)**

1. Which command creates an empty file named `notes.txt`?  
   A) `mkdir notes.txt`  
   B) `touch notes.txt`  
   C) `less notes.txt`  
   D) `rm -i notes.txt`  

2. How do you view the last 5 lines of `app.log`?  
   A) `head -5 app.log`  
   B) `cat app.log 5`  
   C) `tail -n 5 app.log`  
   D) `more -d app.log`  

3. What happens if you run `rmdir mydir` when `mydir` has files inside?  
   A) `mydir` and all files are deleted  
   B) The `rmdir` command fails because the directory isn’t empty  
   C) The files are automatically moved to `/tmp`  
   D) The command partially deletes some files  

4. Which command shows the entire file contents in one go (no interactive scrolling)?  
   A) `less file.txt`  
   B) `cat file.txt`  
   C) `head file.txt`  
   D) `more file.txt`  

### **Intermediate Level (4 Questions)**

1. Which command and option combination creates the entire path `/data/projects/logs` if none of the folders exist?  
   A) `mkdir /data /data/projects /data/projects/logs`  
   B) `mkdir -p /data/projects/logs`  
   C) `mkdir -r /data/projects/logs`  
   D) `rmdir -p /data/projects/logs`  

2. If you want to copy `/etc/nginx` into `/backup/nginx` and preserve permissions, ownership, and symlinks, which flag should you use?  
   A) `cp -r /etc/nginx /backup/nginx`  
   B) `cp -p /etc/nginx /backup/nginx`  
   C) `cp -a /etc/nginx /backup/nginx`  
   D) `cp -i /etc/nginx /backup/nginx`  

3. You accidentally wrote secrets into `credentials.txt`. You must remove it without any confirmation. Which command ensures no prompt?  
   A) `rm credentials.txt`  
   B) `rm -i credentials.txt`  
   C) `rm -f credentials.txt`  
   D) `mv credentials.txt /dev/null`  

4. Which command helps you avoid overwriting an existing file?  
   A) `cp -f source.txt dest.txt`  
   B) `cp -i source.txt dest.txt`  
   C) `cp -r source.txt dest.txt`  
   D) `cp -n source.txt dest.txt` (assuming a shell that supports `-n`)  

### **SRE-Level Tier (4 Questions)**

1. During an incident, which command is most appropriate for real-time monitoring of a frequently rotated log?  
   A) `tail -f app.log`  
   B) `tail -F app.log`  
   C) `head -f app.log`  
   D) `less -N app.log`  

2. Your script renames config files atomically. Which approach is best?  
   A) `mv config.yml config.yml.bak && cp config_new.yml config.yml`  
   B) `mv config.yml config.yml.bak && mv config_new.yml config.yml`  
   C) `cp config_new.yml config.yml.bak && rm config.yml`  
   D) `tail -f config.yml && cp config_new.yml config.yml`  

3. Which command usage is best for removing large, old logs while displaying each file removed?  
   A) `rm -rf /var/log/old/`  
   B) `rm -rv /var/log/old/`  
   C) `rm -rfv /var/log/old/`  
   D) `rm -iv /var/log/old/`  

4. To avoid losing file ownership and timestamps during a directory backup, which flag should be used with `cp`?  
   A) `-a`  
   B) `-r`  
   C) `-p`  
   D) `-i`  

### Instructor Key provided separately

---

## **7. Troubleshooting Scenarios**

1. **Scenario: Log Flooding**  
   - **Symptoms**: Running `tail -f /var/log/app.log` shows thousands of lines added per minute; CPU usage spikes.  
   - **Causes**: Application in an error loop, excessive debug logging, or misconfigured log level.  
   - **Diagnostics**: Check `top` or `htop` for CPU usage, look for repeating patterns with `grep`.  
   - **Resolution**: Switch to `tail -F | grep "CRITICAL"` or filter logs to reduce spam. Then fix the app’s logging level or bug.  
   - **Prevention**: Implement log rotation, limit debug logs in production.

2. **Scenario: Disk Full When Copying**  
   - **Symptoms**: `cp` fails with “No space left on device.”  
   - **Causes**: The destination partition is out of free space or inodes.  
   - **Diagnostics**: Use `df -h` to check space, `df -i` for inodes, possibly `du -sh` to locate large directories.  
   - **Resolution**: Remove or archive old files, expand the partition, or relocate data to a larger filesystem.  
   - **Prevention**: Monitor disk usage with alerts, automatically remove or compress old logs.

3. **Scenario: Directory Not Empty**  
   - **Symptoms**: `rmdir myfolder` fails because it isn’t empty.  
   - **Causes**: Hidden or leftover files exist.  
   - **Diagnostics**: `ls -la myfolder` to see hidden files.  
   - **Resolution**: Remove contents first with `rm -r myfolder`; or remove hidden files, then `rmdir myfolder`.  
   - **Prevention**: Confirm no unexpected hidden files, carefully design deployment scripts to clean up properly.

---

## **8. FAQ**

### **Beginner FAQs (3)**

1. **Q**: Can I undo an `rm` command?  
   **A**: Not easily. Linux doesn’t have a native undo or recycle bin. Always confirm before deleting, especially in production.

2. **Q**: Why does `cat` sometimes show garbage characters?  
   **A**: You might be viewing a binary or compressed file. Use tools like `zcat` for compressed logs, or a hex editor for binaries.

3. **Q**: What if I get “Permission denied” when creating or removing files?  
   **A**: You likely lack the correct permissions or are in the wrong directory. Use `ls -l`, `whoami`, or `sudo` if appropriate.

### **Intermediate FAQs (3)**

1. **Q**: How can I safely remove many files without risking accidental wildcard expansions?  
   **A**: Use interactive mode (`rm -i`), or first `echo rm file*` to see what matches. Alternatively, move them to a staging “trash” directory.

2. **Q**: Should I use `cp` or `rsync` for backups?  
   **A**: `cp` is straightforward but lacks incremental or network awareness. `rsync` is more robust for large or remote backups, offering checksums and partial transfers.

3. **Q**: What’s the difference between `tail -f` and `tail -F`?  
   **A**: `-F` handles log rotation gracefully. If the log file is renamed or recreated, `-f` might lose track, but `-F` will keep following the new file.

### **SRE-Level FAQs (3)**

1. **Q**: How can I manage extremely large logs in production?  
   **A**: Implement log rotation (e.g., `logrotate`), centralize logs with ELK stack/Splunk, or limit the verbosity level. Continuously tailing multi-GB logs is unscalable.

2. **Q**: When moving large directories across disks, is `mv` enough?  
   **A**: An inter-disk `mv` effectively does a copy + delete. It’s often better to use `rsync` with checksums for data integrity, then remove the source after verification.

3. **Q**: How do I audit who deleted critical files?  
   **A**: Use Linux auditing frameworks like `auditd`, which can log file operations (create, unlink). SREs rely on these logs for forensic analysis after incidents.

---

## **9. SRE Scenario: Quick Incident Log Analysis**

**Situation**: A production web service is returning 502 errors. You have 15 minutes to locate the root cause.

### **Step-by-Step SRE Response**

1. **SSH into the Web Server**  
   - `ssh sre@prod-web01`  
   - **Why**: Access logs and config files quickly.

2. **Check Nginx Error Log**  
   - `tail -F /var/log/nginx/error.log`  
   - **Why**: Look for HTTP 502 messages or upstream connection errors in real time.

3. **Parallel Check of Application Logs**  
   - `less +F /var/log/myapp/app.log`  
   - **Why**: Compare application-level logs with web server errors for correlation (e.g., app crashed or timed out).

4. **Search for ‘CRITICAL’**  
   - `grep "CRITICAL" /var/log/myapp/app.log | tail -n 20`  
   - **Why**: Quickly identify severe error messages near the incident timeframe.

5. **Backup and Edit Config**  
   - `cp -a /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak.$(date +%Y%m%d-%H%M%S)`  
   - `vim /etc/nginx/nginx.conf`  
   - **Why**: Safe to back up before adjusting possibly incorrect upstream settings.

6. **Reload Nginx**  
   - `sudo systemctl reload nginx`  
   - **Why**: Apply the new config so the 502 errors may be resolved.

7. **Verify Recovery**  
   - `tail -n 20 /var/log/nginx/access.log`  
   - **Why**: Check if 502 errors stop and normal HTTP 200 responses resume.

Within minutes, you’ve leveraged file commands for real-time monitoring, quick edits, and ensuring reliability in production.

---

## **10. Key Takeaways**

1. **Command Summary (5)**  
   - **touch/mkdir**: Create files/directories (placeholders, logs, structuring).  
   - **cat/less/more/head/tail**: Inspect file contents in different ways.  
   - **cp**: Duplicate files and directories with optional metadata preservation.  
   - **mv**: Rename or relocate files, crucial for atomic updates.  
   - **rm/rmdir**: Remove files or empty directories — be cautious.

2. **Operational Insights (3)**  
   - Always back up critical files before changes to enable quick rollbacks.  
   - Be mindful of disk I/O usage for large file operations, especially in production.  
   - Logging and log rotation are essential to keep systems stable and maintain visible audit trails.

3. **Best Practices (3)**  
   - **Check** space and inodes (`df -h`, `df -i`) before large copies or moves.  
   - **Automate** housekeeping with safe defaults (interactive prompts or move-to-trash approach).  
   - **Secure** sensitive file operations: preserve permissions, avoid exposing credentials, and consider an audit trail.

4. **Preview of Next Topic**  
   - **Day 3**: File Permissions & Ownership — controlling who can read, write, or execute files. A must-know for secure, reliable systems.

---

## **11. Further Learning Resources**

### **🟢 Beginner**

1. **The Linux Command Line (William Shotts)**  
   - [https://linuxcommand.org/tlcl.php](https://linuxcommand.org/tlcl.php)  
   - **Teaches**: Fundamentals of file operations in a fun, tutorial style.  
   - **Relevance**: Perfect for building confidence with Linux basics.

2. **Ubuntu Tutorial: Command Line for Beginners**  
   - [https://ubuntu.com/tutorials/command-line-for-beginners](https://ubuntu.com/tutorials/command-line-for-beginners)  
   - **Teaches**: Step-by-step CLI usage, including file manipulation.  
   - **Relevance**: Walks novices through daily tasks with clear examples.

### **🟡 Intermediate**

1. **Pluralsight: Linux Fundamentals**  
   - [https://www.pluralsight.com/courses/linux-fundamentals](https://www.pluralsight.com/courses/linux-fundamentals)  
   - **Teaches**: Broader CLI operations, including advanced file handling.  
   - **Relevance**: Bridges the gap between basic usage and operational tasks.

2. **ArchWiki: Core Utilities**  
   - [https://wiki.archlinux.org/title/Core_utilities](https://wiki.archlinux.org/title/Core_utilities)  
   - **Teaches**: Detailed usage of core commands (cp, mv, rm, etc.).  
   - **Relevance**: Offers deeper insight into flags and real-world behaviors.

### **🔴 SRE-Level**

1. **Google SRE Workbook: Practical Alerting & Monitoring**  
   - [https://sre.google/workbook/chapters/alerting/](https://sre.google/workbook/chapters/alerting/)  
   - **Teaches**: How file-based logs integrate with alerting and incident response.  
   - **Relevance**: Helps you tie file operations to an SRE’s broader responsibilities.

2. **Advanced Bash-Scripting Guide**  
   - [https://www.tldp.org/LDP/abs/html/](https://www.tldp.org/LDP/abs/html/)  
   - **Teaches**: Complex scripting, including advanced file manipulation, flow control.  
   - **Relevance**: Enables automation of repetitive file tasks, log rotations, backups.

3. **Logrotate Man Page**  
   - [https://linux.die.net/man/8/logrotate](https://linux.die.net/man/8/logrotate)  
   - **Teaches**: Configuring automatic log rotation.  
   - **Relevance**: Vital for managing logs in production to prevent disk exhaustion.

---

**Congratulations!** You’ve completed **Day 2** of our Linux SRE Training. Understanding file creation, viewing, copying, moving, and deleting is critical for quick, confident action during both routine maintenance and high-pressure incidents. Up next: **Permissions and Ownership** for robust security and collaboration!
