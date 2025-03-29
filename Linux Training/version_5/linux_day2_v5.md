# **Day 2: File Manipulation for SREs**  

Welcome to **Day 2** of our Linux SRE Training Series. Today, we focus on **file manipulation**—creating, viewing, copying, moving, and deleting files and directories. We’ll build from **beginner** concepts to **SRE-level** mastery, ensuring you have both the hands-on command knowledge and the real-world application skills necessary for reliability engineering.

---

## **1. Introduction**

### **Why File Manipulation Matters for SREs**  

- **Beginner**: Learn foundational commands to create and manage files/directories.  
- **Intermediate**: Gain efficiency in viewing, organizing, and moving files for operational tasks.  
- **SRE-Level**: Implement robust file management strategies for automation, backups, and incident response.

### **Objectives per Tier**

- **Beginner Objectives**  
  1. Understand how to create and remove files/directories.  
  2. Practice viewing file contents (all or partial).  
  3. Become comfortable with basic copying and moving.

- **Intermediate Objectives**  
  1. Perform multi-step operations (e.g., archiving logs, reorganizing directories).  
  2. Apply safer or more advanced flags (e.g., interactive mode, recursive copying).  
  3. Understand performance implications of viewing/streaming large files.

- **SRE-Level Objectives**  
  1. Automate file operations and backups in production-like settings.  
  2. Integrate file manipulations with troubleshooting (log analysis under time pressure).  
  3. Implement best practices (versioning, security, and auditing changes).

### **Connection to Previous/Upcoming Topics**  

- On **Day 1**, we covered Linux navigation and help systems, giving you the foundation to move through the filesystem.  
- Today’s **Day 2** builds on that by manipulating files in place.  
- On **Day 3**, we’ll dive into permissions and ownership—critical for securing file operations and enabling collaborative tasks.

---

## **2. Core Concepts**

Below are the core operations you’ll perform daily. Each concept includes an analogy, technical explanation, SRE use, and system impact.

1. **File Creation**  
   - **Beginner Analogy**: Placing a blank sheet of paper into a new folder.  
   - **Technical Explanation**: Commands like `touch` make empty files or update timestamps; `mkdir` creates directories.  
   - **SRE Application**: Stub files for logs, config placeholders, or quick tests.  
   - **System Impact**: Minimal overhead unless you create many files in quick succession.

2. **Viewing Files**  
   - **Beginner Analogy**: Reading printed pages, flipping front to back.  
   - **Technical Explanation**: Commands like `cat`, `less`, `more`, `head`, and `tail` display file content in different ways.  
   - **SRE Application**: Quickly check logs, config files, and system outputs for issues.  
   - **System Impact**: Large file reads can tax I/O; repeated `tail -f` can raise CPU usage if logs are very active.

3. **Copying Files**  
   - **Beginner Analogy**: Photocopying a document and placing it in a second folder.  
   - **Technical Explanation**: `cp` duplicates file data from source to destination.  
   - **SRE Application**: Backups, version control, relocating logs or configs without losing original data.  
   - **System Impact**: Copying large files can consume disk bandwidth, potentially affecting performance.

4. **Moving/Renaming Files**  
   - **Beginner Analogy**: Moving a document from one folder to another or writing a new label on its tab.  
   - **Technical Explanation**: `mv` changes a file’s location or name within the filesystem.  
   - **SRE Application**: Organizing logs post-incident, archiving old files, renaming config files for rollbacks.  
   - **System Impact**: Typically fast on the same filesystem (just updates metadata). Cross-filesystem moves actually copy data and can be slower.

5. **Deleting Files**  
   - **Beginner Analogy**: Throwing out unneeded papers into the trash.  
   - **Technical Explanation**: `rm` and `rmdir` remove files/directories, either singly or recursively.  
   - **SRE Application**: Clearing stale logs or old configs, housekeeping for disk space.  
   - **System Impact**: Freed space and metadata changes. Careless deletion can cause incidents if critical data is removed.

---

## **3. Detailed Command Breakdowns**

Below are **11** commands essential to file manipulation, each with a consistent structure: overview, syntax table, examples at three skill tiers, and instructional notes.

---

### **Command: touch (create/update file timestamps)**

**Command Overview:**  
`touch` primarily creates empty files if they don't exist or updates a file's last access/modify timestamps. SREs commonly use it to generate placeholder files or to test application behaviors dependent on timestamp changes.

**Syntax & Flags:**

| Flag/Option | Syntax Example             | Description                                                 | SRE Usage Context                                                      |
|-------------|----------------------------|-------------------------------------------------------------|------------------------------------------------------------------------|
| *(none)*    | `touch myfile.txt`        | Creates a new file if it doesn't exist.                     | Quick placeholder creation for logs or config.                        |
| `-a`        | `touch -a myfile.txt`     | Updates the file’s access time only.                        | Testing read-check logic in apps.                                     |
| `-m`        | `touch -m myfile.txt`     | Updates the file’s modification time only.                  | Manual time updates for triggers or auditing.                         |
| `-t`        | `touch -t 202503290930 file` | Sets custom timestamp (YYYYMMDDhhmm).                        | Simulating old/new files for backup or compliance tests.              |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  # Create an empty file named 'demo.log'
  $ touch demo.log
  
  # Verify it was created:
  $ ls -l demo.log
  -rw-r--r-- 1 user user 0 Mar 29 09:00 demo.log
  ```
  
- 🟡 **Intermediate Example:**

  ```bash
  # Update only the access time of 'demo.log'
  $ touch -a demo.log
  
  # Confirm changes:
  $ stat demo.log
  # Output will show a new 'Access' timestamp but unchanged 'Modify' timestamp.
  ```
  
- 🔴 **SRE-Level Example:**

  ```bash
  # Simulate an older timestamp for a log rotation test
  $ touch -t 202303010800 service.log
  
  # Now the log rotation script sees 'service.log' as older and triggers a rotation process
  ```
  
**Instructional Notes:**

- 🧠 **Beginner Tip:** If you run `touch file1 file2 file3`, it creates multiple files at once.  
- 🧠 **Beginner Tip:** Use `ls -l` after `touch` to confirm zero-size creation if new.

- 🔧 **SRE Insight:** Changing timestamps can help debug cron jobs that rely on file modification times.  
- 🔧 **SRE Insight:** Combine `touch` with automation scripts to dynamically create or refresh placeholders under load testing.

- ⚠️ **Common Pitfall:** Touching a file that already exists won’t alter its contents, but it may confuse novices if they expect changes.  
- ⚠️ **Common Pitfall:** Using custom timestamps incorrectly can break chronological log analysis.

- 🚨 **Security Note:** Malicious users might alter timestamps to obscure activity or bypass detection. Always verify logs with secure checksums.  
- 💡 **Performance Impact:** Generally negligible, but in extremely large directories, frequent metadata updates can slow filesystem performance.

---

### **Command: mkdir (make directory)**

**Command Overview:**  
`mkdir` creates new directories. SREs routinely create folder structures for logs, backups, and environment separation.

**Syntax & Flags:**

| Flag/Option | Syntax Example                 | Description                                                                  | SRE Usage Context                                                |
|-------------|--------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------|
| *(none)*    | `mkdir newfolder`             | Creates a single directory named `newfolder`.                                | Simple folder creation for config or logs.                       |
| `-p`        | `mkdir -p /path/sub1/sub2`    | Creates parent directories if they don’t exist.                              | Building nested structures for backups or app releases.          |
| `-m`        | `mkdir -m 700 secure_dir`     | Sets specific permissions on creation.                                       | Storing sensitive data or configuration.                         |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  # Create a single directory named 'projects'
  $ mkdir projects
  
  # Check if it's created:
  $ ls -l
  drwxr-xr-x 2 user user 4096 Mar 29 09:10 projects
  ```

- 🟡 **Intermediate Example:**

  ```bash
  # Create nested directories for a web application structure
  $ mkdir -p /var/www/myapp/logs
  
  # This ensures '/var/www/myapp' exists and then creates 'logs'
  $ tree /var/www/myapp
  /var/www/myapp/
  └── logs
  ```
  
- 🔴 **SRE-Level Example:**

  ```bash
  # Create a locked-down directory for secret keys
  $ mkdir -m 700 /etc/secure_keys
  
  # Ensures only the owner (typically root) can read/write/execute
  ```
  
**Instructional Notes:**

- 🧠 **Beginner Tip:** If you get “File exists” errors, confirm the directory doesn’t already exist.  
- 🧠 **Beginner Tip:** Use `pwd` before creating directories to know exactly where you are.

- 🔧 **SRE Insight:** SREs often structure log directories in date-based hierarchies, e.g. `mkdir -p /var/log/app/$(date +%Y/%m/%d)` for daily partitioning.  
- 🔧 **SRE Insight:** Combine `mkdir -p` with automation tools (Chef, Ansible) for consistent directory setups across servers.

- ⚠️ **Common Pitfall:** Omitting `-p` can cause failures if the parent directory doesn’t exist.  
- ⚠️ **Common Pitfall:** Using `-m` incorrectly can create insecure or overly restrictive permissions.

- 🚨 **Security Note:** Carefully set permissions (`-m`) when storing credentials or private keys.  
- 💡 **Performance Impact:** Minimal overhead, but large-scale directory creations (thousands) can affect I/O performance briefly.

---

### **Command: cat (concatenate)**

**Command Overview:**  
`cat` displays file contents in one go. It’s quick and straightforward for smaller files. SREs use it to view logs/configs without paging.

**Syntax & Flags:**

| Flag/Option | Syntax Example        | Description                                            | SRE Usage Context                                          |
|-------------|-----------------------|--------------------------------------------------------|------------------------------------------------------------|
| *(none)*    | `cat file.txt`       | Outputs entire file contents to stdout.               | Quick reading of short logs/configs.                      |
| `-n`        | `cat -n file.txt`    | Number each line in the output.                       | Checking line references for error logs or code files.     |
| `-A`        | `cat -A file.txt`    | Shows non-printing characters and line endings.       | Debugging formatting or whitespace issues.                |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  # Display a short text file
  $ cat sample.txt
  Hello, this is a short file.
  End of file.
  ```
  
- 🟡 **Intermediate Example:**

  ```bash
  # View file with line numbers
  $ cat -n server.log
       1  Server starting...
       2  Listening on port 8080...
       3  [ERROR] Database connection failed
  ```
  
- 🔴 **SRE-Level Example:**

  ```bash
  # Combine multiple small logs into one
  $ cat /var/log/app1.log /var/log/app2.log | grep "CRITICAL" > combined_critical.log
  
  # Creates a combined file of only CRITICAL events from both logs
  ```
  
**Instructional Notes:**

- 🧠 **Beginner Tip:** If the file is large, `cat` floods your screen. Use `less` instead.  
- 🧠 **Beginner Tip:** Redirection (`>`) overwrites files, e.g., `cat file1 > file2` replaces file2’s content.

- 🔧 **SRE Insight:** Pipe `cat` with other tools like `grep`, `awk`, or `sed` for fast text processing.  
- 🔧 **SRE Insight:** Use `cat` carefully in scripts—large files can cause memory or performance concerns.

- ⚠️ **Common Pitfall:** `cat bigfile | less` is often replaced by simply `less bigfile`. The extra `cat` is unnecessary overhead.  
- ⚠️ **Common Pitfall:** Accidentally overwriting critical files with redirection can cause data loss.

- 🚨 **Security Note:** Revealing sensitive data (e.g., keys, tokens) in your terminal buffer can pose a security risk.  
- 💡 **Performance Impact:** For very large files, `cat` can lead to high I/O and CPU usage if piped through multiple processes.

---

### **Command: less (file pager)**

**Command Overview:**  
`less` is an interactive pager that lets you scroll forward and backward through large files. SREs commonly use it for log analysis during incidents.

**Syntax & Flags:**

| Flag/Option | Syntax Example           | Description                                     | SRE Usage Context                         |
|-------------|--------------------------|-------------------------------------------------|-------------------------------------------|
| *(none)*    | `less largefile.log`    | Opens file in scrollable pager.                | Quickly navigate big logs                |
| `-N`        | `less -N config.yml`    | Shows line numbers.                            | Easier debugging, referencing lines       |
| `+F`        | `less +F /var/log/syslog` | Follow mode, like `tail -f`.                    | Real-time log viewing with easy exit      |
| `-S`        | `less -S app.log`       | Disable line wrapping (chop long lines).        | For logs with wide lines or JSON entries. |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  # Read a system log with 'less'
  $ less /var/log/syslog
  # Use Up/Down arrows or PageUp/PageDown to scroll, 'q' to quit
  ```
  
- 🟡 **Intermediate Example:**

  ```bash
  # View with line numbers and no wrap
  $ less -N -S /var/log/nginx/error.log
  # Helps to keep lines intact and see exact line references
  ```
  
- 🔴 **SRE-Level Example:**

  ```bash
  # Combine multi-log follow:
  $ tail -f /var/log/app/*.log | less
  # Allows advanced searching inside streaming logs:
  #  /ERROR
  #  n -> next match
  # Press Ctrl+C, then 'q' to exit
  ```
  
**Instructional Notes:**

- 🧠 **Beginner Tip:** Press `q` to quit and `/something` to search text forward. Use `n` to jump to next result.  
- 🧠 **Beginner Tip:** `F` inside `less` toggles follow mode (like `tail -f`).

- 🔧 **SRE Insight:** Combine `less` with search patterns to quickly locate error lines in large logs.  
- 🔧 **SRE Insight:** `less +F` is safer than `tail -f` for real-time logs because you can scroll back up with Ctrl+C.

- ⚠️ **Common Pitfall:** Searching huge logs can be slow; be mindful of production server load.  
- ⚠️ **Common Pitfall:** If you forget to exit follow mode properly, you might remain stuck streaming.

- 🚨 **Security Note:** If logs contain sensitive data, ensure appropriate permissions on the logs themselves.  
- 💡 **Performance Impact:** Reading large logs on a busy system can spike I/O usage. In production, consider rotating logs or partial reads.

---

### **Command: more (basic pager)**

**Command Overview:**  
`more` is a simpler pager than `less`. It only supports forward navigation. SREs generally prefer `less`, but `more` is still useful on minimal systems.

**Syntax & Flags:**

| Flag/Option | Syntax Example       | Description                               | SRE Usage Context           |
|-------------|----------------------|-------------------------------------------|-----------------------------|
| *(none)*    | `more file.log`     | Scroll forward in pages.                  | Quick viewing on older distros |
| `-d`        | `more -d file.log`  | Display help prompts (press space, etc.). | Aids new users              |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  # Display contents page by page
  $ more server.log
  --More-- (Press space to continue, q to quit)
  ```
  
- 🟡 **Intermediate Example:**

  ```bash
  # Use -d for easier navigation instructions
  $ more -d server.log
  --More-- (Press space to continue, 'q' to quit)
  ```
  
- 🔴 **SRE-Level Example:**

  ```bash
  # Typically, you'd use 'less' for advanced navigation, 
  # but if only 'more' is available (in minimal rescue mode):
  $ more /mnt/chroot/var/log/boot.log
  # Check partial logs in a stripped-down environment
  ```
  
**Instructional Notes:**

- 🧠 **Beginner Tip:** If stuck, press `q` to quit. Use space to go to the next page.  
- 🧠 **Beginner Tip:** `more` can’t scroll backward; if you overshoot, you must restart.

- 🔧 **SRE Insight:** On some embedded systems or minimal containers, `less` might not be installed, so knowing `more` is essential.  
- 🔧 **SRE Insight:** Pipe data into `more` for quick paged output on legacy or minimal setups.

- ⚠️ **Common Pitfall:** Doesn’t handle backward scrolling, which frustrates deeper log analysis.  
- ⚠️ **Common Pitfall:** Large files can still overwhelm you page-by-page.

- 🚨 **Security Note:** As with any pager, take care when viewing files with sensitive data in shared sessions.  
- 💡 **Performance Impact:** Minimal, but scanning very large files still consumes I/O.

---

### **Command: head (view file start)**

**Command Overview:**  
`head` shows the first lines of a file. SREs use it to quickly peek at log headers, data formats, or the beginning of config files.

**Syntax & Flags:**

| Flag/Option | Syntax Example         | Description                                              | SRE Usage Context                              |
|-------------|------------------------|----------------------------------------------------------|------------------------------------------------|
| *(none)*    | `head file.txt`       | Shows the first 10 lines by default.                     | Quick look at top of logs/configs.             |
| `-n`        | `head -n 20 file.txt` | Specify number of lines to display.                      | Checking more lines from large logs.           |
| `-c`        | `head -c 100 file.txt`| Show the first 100 bytes of the file.                    | Viewing small chunk of binary or text data.    |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  # View the first 10 lines of /etc/passwd
  $ head /etc/passwd
  root:x:0:0:root:/root:/bin/bash
  ...
  ```
  
- 🟡 **Intermediate Example:**

  ```bash
  # Check the first 25 lines of a large log
  $ head -n 25 /var/log/messages
  ```
  
- 🔴 **SRE-Level Example:**

  ```bash
  # Quick check of the first part of a compressed log (with pipe):
  $ zcat /var/log/app-2025-03-29.gz | head -n 15
  # Useful for verifying correct compression or log rotation
  ```
  
**Instructional Notes:**

- 🧠 **Beginner Tip:** By default, `head` shows 10 lines. Use `-n` to adjust.  
- 🧠 **Beginner Tip:** Combine `head` with `>` redirection to save a snippet for further analysis.

- 🔧 **SRE Insight:** Checking the start of logs can reveal if a service wrote logs from startup or after a crash.  
- 🔧 **SRE Insight:** Pair with `tail` to sample both ends of a large log quickly.

- ⚠️ **Common Pitfall:** Using `head file` on a massive log might still read the entire file if it’s compressed or piped incorrectly.  
- ⚠️ **Common Pitfall:** For multi-GB logs, consider tools like `less` or specialized log management solutions.

- 🚨 **Security Note:** Some files might contain credentials in the header (e.g., config files). Use secure shells or local copies.  
- 💡 **Performance Impact:** Generally low overhead. The command stops reading after the specified lines/bytes.

---

### **Command: tail (view file end)**

**Command Overview:**  
`tail` shows the last lines of a file. It’s crucial for real-time log monitoring during an incident or to see fresh system messages.

**Syntax & Flags:**

| Flag/Option | Syntax Example           | Description                                              | SRE Usage Context                                   |
|-------------|--------------------------|----------------------------------------------------------|-----------------------------------------------------|
| *(none)*    | `tail file.log`         | Shows the last 10 lines by default.                     | Quick glance at recent log messages.               |
| `-n`        | `tail -n 20 file.log`   | Specify the number of lines to display from the end.    | Deeper look at the last part of logs.              |
| `-f`        | `tail -f file.log`      | Follow mode: streams new lines as they are written.     | Live monitoring of logs for incident response.      |
| `-F`        | `tail -F file.log`      | Follow and gracefully handle file rotation.             | Production logs that rotate frequently.            |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  # Show last 10 lines of 'app.log'
  $ tail app.log
  INFO: Application started
  INFO: Connection established
  ...
  ```
  
- 🟡 **Intermediate Example:**

  ```bash
  # Show last 50 lines in a log
  $ tail -n 50 /var/log/secure
  # Often used to see recent authentication attempts
  ```
  
- 🔴 **SRE-Level Example:**

  ```bash
  # Live follow a log that rotates daily
  $ tail -F /var/log/app/current.log
  # Useful in high-availability setups with logrotate
  ```
  
**Instructional Notes:**

- 🧠 **Beginner Tip:** Press Ctrl+C to stop `tail -f`.  
- 🧠 **Beginner Tip:** If the file is not actively written, following mode (`-f`) won’t show new lines until they appear.

- 🔧 **SRE Insight:** In an outage, you might run `tail -f` on multiple logs in parallel or pipe them into `grep` to filter errors.  
- 🔧 **SRE Insight:** `-F` is safer than `-f` in production, especially where logs rotate automatically.

- ⚠️ **Common Pitfall:** `tail -f` on a massive log that’s rapidly growing can fill your screen quickly or even freeze your terminal.  
- ⚠️ **Common Pitfall:** Blindly trusting the last lines can miss the root cause if the error was earlier.

- 🚨 **Security Note:** Use caution if tailing logs that might contain private data (tokens, user info).  
- 💡 **Performance Impact:** A constant `tail -f` on a heavily written log can add overhead. Tools like `journald` or `rsyslog` might be more efficient for high-traffic.

---

### **Command: cp (copy)**

**Command Overview:**  
`cp` duplicates files and directories. SREs frequently use it for backups, versioning configs, or distributing data across directories.

**Syntax & Flags:**

| Flag/Option | Syntax Example                   | Description                                                    | SRE Usage Context                                           |
|-------------|----------------------------------|----------------------------------------------------------------|-------------------------------------------------------------|
| *(none)*    | `cp source.txt dest.txt`         | Copies `source.txt` to `dest.txt`.                            | Simple file duplication                                    |
| `-r`        | `cp -r /src/dir /dest/dir`       | Recursively copy directories.                                 | Copy entire directory trees (configs, logs).               |
| `-p`        | `cp -p fileA fileB`             | Preserve file attributes (mode, ownership, timestamps).       | Maintaining metadata for audits or backups.                |
| `-i`        | `cp -i source.txt dest.txt`      | Interactive, prompts before overwrite.                        | Safer approach to avoid accidental overwrites.             |
| `-a`        | `cp -a /src/dir /dest/dir`       | Archive mode (same as `-dpr`): preserve links, attributes.    | Full backups or migrations preserving symbolic links, etc. |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  # Copy 'file1.txt' to 'file2.txt'
  $ cp file1.txt file2.txt
  
  # Confirm with 'ls'
  $ ls
  file1.txt  file2.txt
  ```
  
- 🟡 **Intermediate Example:**

  ```bash
  # Copy a directory recursively while preserving ownership/timestamps
  $ cp -rp /var/www/ /home/user/www_backup/
  
  # This ensures files in /var/www have same ownership in /home/user/www_backup
  ```
  
- 🔴 **SRE-Level Example:**

  ```bash
  # Archive production config while preserving everything including symlinks
  $ cp -a /etc/myapp/ /backup/myapp_config_$(date +%Y%m%d)
  
  # Useful for rollback points in case of a failed deploy
  ```
  
**Instructional Notes:**

- 🧠 **Beginner Tip:** By default, `cp` overwrites files without warning. Use `-i` to prompt.  
- 🧠 **Beginner Tip:** `cp source target_dir` requires that `target_dir` is a directory.

- 🔧 **SRE Insight:** Using `-a` for config backups ensures you won’t lose symbolic links or permissions.  
- 🔧 **SRE Insight:** For large-scale or remote copying, consider `rsync` for efficiency and network resiliency.

- ⚠️ **Common Pitfall:** Copying huge directories can fill disks quickly if you don’t track sizes.  
- ⚠️ **Common Pitfall:** Missing hidden files (like `.env`) if not accounted for can cause incomplete backups.

- 🚨 **Security Note:** Copying files with open permissions to a less secure location can expose sensitive data.  
- 💡 **Performance Impact:** Large or recursive copies spike I/O usage, possibly affecting other processes.

---

### **Command: mv (move/rename)**

**Command Overview:**  
`mv` relocates or renames files and directories. Within the same filesystem, it updates metadata; across filesystems, it behaves like a copy-then-delete.

**Syntax & Flags:**

| Flag/Option | Syntax Example             | Description                                                  | SRE Usage Context                                 |
|-------------|----------------------------|--------------------------------------------------------------|---------------------------------------------------|
| *(none)*    | `mv source.txt dest.txt`  | Renames `source.txt` to `dest.txt`.                          | Re-labeling config files or logs.                 |
| `-i`        | `mv -i old.conf new.conf` | Prompt before overwrite if `new.conf` exists.               | Safety net in critical directories.               |
| `-v`        | `mv -v file1 file2`       | Verbose output, shows the rename/move operations.           | Tracking rename operations during automation.     |
| `-b`        | `mv -b file file.bak`     | Makes a backup of the destination file if it exists.         | Minimizing accidental data loss in scripts.       |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  # Rename 'test.txt' to 'report.txt'
  $ mv test.txt report.txt
  
  # Check result:
  $ ls
  report.txt
  ```
  
- 🟡 **Intermediate Example:**

  ```bash
  # Move multiple log files to an archive directory with verbose output
  $ mv -v /var/log/app/*.log /var/log/app/archive/
  /var/log/app/app1.log -> /var/log/app/archive/app1.log
  /var/log/app/app2.log -> /var/log/app/archive/app2.log
  ```
  
- 🔴 **SRE-Level Example:**

  ```bash
  # Rename a config while creating a backup of the destination if it already exists
  $ mv -b /etc/myapp/config.yml /etc/myapp/config.yml.old
  # Ensures you keep the old config in case of immediate rollback
  ```
  
**Instructional Notes:**

- 🧠 **Beginner Tip:** If you move a file to an existing directory, the file name stays the same unless you specify a new name.  
- 🧠 **Beginner Tip:** `mv file /path/` can also move a file into a directory.

- 🔧 **SRE Insight:** For atomic updates, rename a new file into place, e.g., `mv config.new config` after verifying correctness.  
- 🔧 **SRE Insight:** `mv` across different volumes can be slow as it essentially copies and removes data.

- ⚠️ **Common Pitfall:** Overwriting an existing file without `-i` or backups can cause irreversible data loss.  
- ⚠️ **Common Pitfall:** Scripted moves across network filesystems can fail or partially move data on connection issues.

- 🚨 **Security Note:** Ensure you do not accidentally rename sensitive files into publicly accessible directories.  
- 💡 **Performance Impact:** Within the same filesystem, moves are very fast (just metadata changes). Across different disks, it’s a full copy operation.

---

### **Command: rm (remove)**

**Command Overview:**  
`rm` permanently removes files or directories (with `-r`). SREs typically use this for log rotation cleanup, removing old backups, or housekeeping tasks.

**Syntax & Flags:**

| Flag/Option | Syntax Example            | Description                                            | SRE Usage Context                                  |
|-------------|---------------------------|--------------------------------------------------------|----------------------------------------------------|
| *(none)*    | `rm file.txt`            | Removes `file.txt`.                                    | Basic removal of a single file.                   |
| `-r`        | `rm -r folder`           | Recursively remove `folder` and all sub-contents.      | Deleting entire directories.                       |
| `-i`        | `rm -i file.txt`         | Prompts before removing each file.                     | Safer approach on production systems.             |
| `-f`        | `rm -f file.txt`         | Force remove without prompt or error messages.         | Automated scripts that must proceed under errors.  |
| `-v`        | `rm -v file.txt`         | Verbose, lists each deletion.                          | Logs removal actions in a script.                  |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  # Remove a single file
  $ rm old_file.txt
  
  # Confirm it's gone:
  $ ls old_file.txt
  ls: cannot access 'old_file.txt': No such file or directory
  ```
  
- 🟡 **Intermediate Example:**

  ```bash
  # Remove a directory and its contents, with interactive prompts
  $ rm -ri archive/
  rm: descend into directory 'archive'? y
  rm: remove 'archive/log1.bak'? y
  ...
  ```
  
- 🔴 **SRE-Level Example:**

  ```bash
  # Forcefully remove large, old logs in a script with verbose output
  $ rm -rfv /var/log/app/old_logs/
  removed '/var/log/app/old_logs/log1'
  removed directory '/var/log/app/old_logs'
  # Useful in batch cleanup tasks or housekeeping
  ```
  
**Instructional Notes:**

- 🧠 **Beginner Tip:** Always double-check the file or directory name to avoid accidental deletions.  
- 🧠 **Beginner Tip:** `rm` has no built-in recovery. Once gone, it’s typically gone.

- 🔧 **SRE Insight:** Use caution on production systems—automate `rm` with pre-checks or backups.  
- 🔧 **SRE Insight:** Some teams prefer moving files to a “trash” directory first as a buffer.

- ⚠️ **Common Pitfall:** A stray space or wildcard (e.g., `rm -rf / var/log`) can be catastrophic—always carefully type commands.  
- ⚠️ **Common Pitfall:** Using `-f` in scripts can mask errors, leading to incomplete cleanup or hidden problems.

- 🚨 **Security Note:** Deleting logs can hinder investigations or compliance checks. Ensure relevant logs are archived first.  
- 💡 **Performance Impact:** Large-scale recursive deletions can spike I/O usage. Use caution on busy servers.

---

### **Command: rmdir (remove directory)**

**Command Overview:**  
`rmdir` deletes **empty** directories only. For directories with content, use `rm -r`. SREs use `rmdir` to keep directory structures tidy when they’re sure it’s empty.

**Syntax & Flags:**

| Flag/Option | Syntax Example                | Description                                            | SRE Usage Context                 |
|-------------|-------------------------------|--------------------------------------------------------|-----------------------------------|
| *(none)*    | `rmdir empty_dir`            | Removes the directory if it has no files/subdirs.      | Safely remove empty placeholders. |
| `-p`        | `rmdir -p parent/child/grandchild` | Removes child/grandchild directories up the chain if each is empty. | Cleanup nested empty structures   |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  # Remove an empty directory 'temp'
  $ rmdir temp
  ```
  
- 🟡 **Intermediate Example:**

  ```bash
  # Remove nested empty dirs
  $ rmdir -p logs/archive/2025
  # Removes '2025', then 'archive', then 'logs' if each is empty
  ```
  
- 🔴 **SRE-Level Example:**

  ```bash
  # In an automated cleanup script:
  $ find /tmp -type d -empty -exec rmdir {} \;
  # Recursively removes all empty directories under /tmp
  ```
  
**Instructional Notes:**

- 🧠 **Beginner Tip:** If the directory isn’t empty, `rmdir` fails. Use `ls` to verify emptiness.  
- 🧠 **Beginner Tip:** For multi-level removal, `-p` tries removing parents only if they’re empty.

- 🔧 **SRE Insight:** Using `rmdir` ensures you don’t accidentally remove files or subdirectories. Good for final cleanup.  
- 🔧 **SRE Insight:** Combine with `find -empty` to systematically remove leftover empty directories in large code repos.

- ⚠️ **Common Pitfall:** If any subdirectory has hidden files, `rmdir` won’t remove it.  
- ⚠️ **Common Pitfall:** Not a substitute for `rm -r` when actual content is present—this confuses newcomers.

- 🚨 **Security Note:** An empty directory might still have special permissions or SELinux contexts. Verify ownership before removing.  
- 💡 **Performance Impact:** Very minimal. Typically used for small cleanup tasks.

---

## **4. System Effects of File Commands**

1. **Filesystem and Metadata**  
   - Each create, copy, or move updates inodes, file tables, and timestamps.  
   - Large-scale operations can fill disk or cause fragmentation.  

2. **System Resources**  
   - Copying/moving large files uses disk I/O heavily.  
   - Repetitive `tail -f` across large logs can raise CPU usage and I/O load.

3. **Security Implications**  
   - Overwriting or deleting logs can impede audits.  
   - Creating or moving files with incorrect permissions can expose sensitive data.

4. **Monitoring Visibility**  
   - Tools like `lsof`, `iostat`, or process monitors can help track file operation overhead.  
   - Use log management (e.g., `journald`, `syslog`) to track who performs critical changes.

---

## **5. Hands-On Exercises**

### **Beginner (3 Exercises)**

1. **Create a Practice Directory**  
   - Create a directory named `day2_practice`.  
   - Inside it, use `touch` to make three files: `file1.txt`, `file2.txt`, `file3.txt`.  
   - Confirm the files exist using `ls`.

2. **Viewing Files**  
   - Add random text to `file1.txt` (e.g., `echo "Hello World" > file1.txt`).  
   - Use `cat`, `head`, and `tail` to view this file.  
   - Practice `less file1.txt` to navigate line by line.

3. **Deleting Safely**  
   - Run `rm -i file3.txt` and observe the prompt.  
   - Decline the prompt to keep `file3.txt`.  
   - Finally, confirm `file3.txt` is still present with `ls`.

### **Intermediate (3 Exercises)**

1. **Backup and Move**  
   - Inside `day2_practice`, create a subdirectory named `backup`.  
   - Copy `file1.txt` and `file2.txt` into `backup` using `cp -p`.  
   - Move `file2.txt` from `backup` to `day2_practice` and rename it to `notes.txt`.

2. **Explore Log Files**  
   - Simulate logs:  

     ```bash
     for i in {1..100}; do echo "Log line $i" >> sample.log; done
     ```  

   - Use `head -n 10` and `tail -n 10` to confirm logs were generated.  
   - Practice `tail -f sample.log` in one terminal, and in another terminal run `echo "New log entry" >> sample.log` to see the live update.

3. **Nested Directories**  
   - Use `mkdir -p nested/dir/structure` inside `day2_practice`.  
   - Place a file in `nested/dir/structure`.  
   - Verify that `rmdir nested/dir/structure` fails because it’s not empty.  
   - Remove it with `rm -r nested/dir/structure`.

### **SRE-Level (3 Exercises)**

1. **Timestamp Testing**  
   - Create a file `old.log` and use `touch -t 202303010700 old.log` to simulate it being old.  
   - Write a small script that checks file timestamps; if older than X days, moves them to `archive`.  
   - Validate it works as intended using `ls -l`.

2. **Parallel Log Monitoring**  
   - In one pane, run `tail -F /var/log/syslog`.  
   - In another pane, run a command that generates system messages (e.g., `sudo systemctl restart some_service`).  
   - Observe real-time log changes.  
   - After verifying, copy relevant lines from `/var/log/syslog` to an `incident.log` using `cp` with a date-based naming convention.

3. **Automated Cleanup**  
   - Create a directory `/tmp/sre_cleanup_test` and populate it with random files (e.g., `touch /tmp/sre_cleanup_test/file{1..10}`).  
   - Write or outline a script that removes files older than 1 day and empties subdirectories using `rm`, `find`, and `rmdir`.  
   - Check logs or script output to ensure successful cleanup.

---

## **6. Quiz Questions**

### **Beginner Tier (4 Questions)**

1. **Which command creates an empty file named `notes.txt`?**  
   - A) `mkdir notes.txt`  
   - B) `touch notes.txt`  
   - C) `less notes.txt`  
   - D) `rm -i notes.txt`

2. **How do you view the last 5 lines of `app.log`?**  
   - A) `head -5 app.log`  
   - B) `cat app.log 5`  
   - C) `tail -n 5 app.log`  
   - D) `more -d app.log`

3. **What happens if you run `rmdir mydir` when `mydir` has files?**  
   - A) `mydir` is removed along with all files.  
   - B) `rmdir` fails because the directory is not empty.  
   - C) The files are automatically moved to `/tmp`.  
   - D) The command partially deletes some files.

4. **Which command shows file contents in one continuous flow (no interactive scrolling)?**  
   - A) `less file.txt`  
   - B) `cat file.txt`  
   - C) `more file.txt`  
   - D) `head file.txt`

### **Intermediate Tier (4 Questions)**

1. **You need to create multiple directories at once (`/mnt/data/reports/logs`). Which command should you use?**  
   - A) `mkdir /mnt/data /mnt/data/reports /mnt/data/reports/logs`  
   - B) `mkdir -p /mnt/data/reports/logs`  
   - C) `mkdir -r /mnt/data/reports/logs`  
   - D) `rmdir -p /mnt/data/reports/logs`

2. **If you want to copy `/etc/nginx` to `/backup/nginx` while keeping permissions and symlinks, which option is best?**  
   - A) `cp -i /etc/nginx /backup/nginx`  
   - B) `cp -p /etc/nginx /backup/nginx`  
   - C) `cp -r /etc/nginx /backup/nginx`  
   - D) `cp -a /etc/nginx /backup/nginx`

3. **You accidentally wrote sensitive data into `credentials.txt`. You must remove it without a prompt. Which command ensures no prompts?**  
   - A) `rm credentials.txt`  
   - B) `rm -i credentials.txt`  
   - C) `rm -f credentials.txt`  
   - D) `mv credentials.txt /dev/null`

4. **Which command prevents overwriting an existing file without warning?**  
   - A) `cp -f`  
   - B) `cp -i`  
   - C) `cp -r`  
   - D) `cp -n`

### **SRE-Level Tier (4 Questions)**

1. **During an incident, you suspect new log entries in `app.log`. Which command is most appropriate for real-time monitoring if log rotation is frequent?**  
   - A) `tail -f app.log`  
   - B) `tail -F app.log`  
   - C) `head -f app.log`  
   - D) `less +F app.log`

2. **You have a script that renames config files atomically. Which is the best approach?**  
   - A) `mv config.yml config.yml.bak && cp config_new.yml config.yml`  
   - B) `mv config.yml config.yml.bak && mv config_new.yml config.yml`  
   - C) `cp config_new.yml config.yml.bak && rm config.yml`  
   - D) `tail -f config.yml && cp config_new.yml config.yml`

3. **Which command usage is best for removing large, old logs while seeing the details of each deletion?**  
   - A) `rm -rf /logs/old/`  
   - B) `rm -rv /logs/old/`  
   - C) `rm -rfv /logs/old/`  
   - D) `rm -iv /logs/old/`

4. **To avoid losing file attributes (ownership, timestamps, SELinux context) during a directory backup, which copy approach is recommended?**  
   - A) `cp -a`  
   - B) `cp -r`  
   - C) `mv -f`  
   - D) `cp -n`

---

## **7. Troubleshooting Scenarios**

1. **Scenario: Log Flooding**  
   - **Symptoms**: `tail -f /var/log/app.log` is swamped with thousands of lines every minute, CPU spikes.  
   - **Root Causes**: The application is in a loop or generating excessive logs.  
   - **Diagnostics**: Check `top` or `htop` to see CPU usage, possibly `grep` for repeated error lines.  
   - **Resolution**: Pause the tail or filter logs with `grep "ERROR"`. Investigate the app bug causing floods.  
   - **Prevention**: Implement log rotation and set log-level thresholds.

2. **Scenario: Disk Full While Copying**  
   - **Symptoms**: `cp` or `mv` fails with “No space left on device.”  
   - **Root Causes**: Destination filesystem is out of space or inodes.  
   - **Diagnostics**: `df -h` to check space, `df -i` for inode usage.  
   - **Resolution**: Remove or archive old files, expand the volume if possible.  
   - **Prevention**: Monitor disk usage proactively with alerts.

3. **Scenario: Unable to Remove a Directory**  
   - **Symptoms**: `rm -r` says “Permission denied” or `rmdir` complains the directory isn’t empty.  
   - **Root Causes**: Insufficient permissions, hidden files, or subdirectories.  
   - **Diagnostics**: Check `ls -la`, verify ownership with `stat`.  
   - **Resolution**: `sudo rm -r folder` if you have root privileges, or properly remove hidden files.  
   - **Prevention**: Ensure correct ownership/permissions from the start. Keep track of hidden files with `ls -A`.

---

## **8. Frequently Asked Questions (FAQ)**

### **Beginner FAQs (3)**  

1. **How do I recover a file I deleted with `rm`?**  
   - **Answer**: Generally, you can’t recover it easily. There is no “undo” for `rm`. Check backups or use specialized recovery tools (if the data blocks haven’t been overwritten).

2. **What if I typed `rm file*` by accident?**  
   - **Answer**: If it’s mid-deletion, press Ctrl+C quickly. Anything already removed is gone. Always double-check wildcards before pressing Enter.

3. **Why does `less` show “END” but new lines don’t appear automatically?**  
   - **Answer**: You’re not in follow mode. Use `less +F file` or `tail -f file` for continuous updates.

### **Intermediate FAQs (3)**  

1. **When should I use `mv` instead of `cp`?**  
   - **Answer**: If you want to relocate a file without leaving the original behind. Inside the same filesystem, `mv` is nearly instantaneous because it only updates metadata.

2. **Why does copying large directories sometimes freeze my terminal?**  
   - **Answer**: The disk I/O can be very high, or the network is slow if you’re copying across mounts. You can run large copy commands in the background (`cp ... &`) or use a tool like `rsync` for progress info.

3. **Can I force a directory removal even if I’m not the owner?**  
   - **Answer**: With appropriate permissions or `sudo`, yes. Otherwise, you need the correct file ownership or to escalate privileges.

### **SRE-Level FAQs (3)**  

1. **How to automate file rotation without losing critical logs?**  
   - **Answer**: Use `logrotate` or similar frameworks. They copy or move logs to a rotated file, then gracefully signal the application to start fresh logs.

2. **Is it safe to `tail -f` on production logs all day?**  
   - **Answer**: For short tasks, yes. But constant tailing on large logs can degrade performance. Centralized log solutions (ELK stack, Splunk) are recommended for deeper analysis.

3. **How do I handle partial copies on a flaky network share?**  
   - **Answer**: Use robust tools like `rsync` with checksums or partial file resume. Validate checksums after copying to ensure data integrity.

---

## **9. SRE Scenario: Incident Log Analysis**

**Situation**: A critical web service is returning “502 Bad Gateway” errors. You have 15 minutes to find the root cause.

**Steps**:

1. **SSH into Production Server**  
   - `ssh sre@prod-web01`  
   - *Goal*: Access logs and config files.

2. **Live Tail of Web Server Error Log**  
   - `tail -F /var/log/nginx/error.log`  
   - *Reason*: Check real-time errors. If logs rotate, `-F` handles it.

3. **Simultaneous Check of Application Logs**  
   - `less +F /var/log/myapp/app.log` in another terminal  
   - *Reason*: Compare web server errors with application-level messages.

4. **Search for “CRITICAL” Patterns**  
   - `grep "CRITICAL" /var/log/myapp/app.log | tail -n 20`  
   - *Reason*: Filter out severe messages quickly.

5. **Backup and Modify Config**  
   - `cp -a /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak.$(date +%Y%m%d-%H%M%S)`  
   - *Reason*: Safe backup before changing Nginx config to fix incorrect upstream settings.

6. **Reload Service**  
   - `sudo systemctl reload nginx`  
   - *Reason*: Apply the new config quickly.

7. **Validate Logs**  
   - `tail -n 20 /var/log/nginx/access.log`  
   - *Reason*: Confirm 502 errors are resolved or significantly reduced.

Result: **Within minutes**, you isolated the misconfiguration causing 502 responses and restored normal service operation—an SRE best practice.

---

## **10. Key Takeaways**

1. **Command Summary (5)**  
   - **touch**: Create/update file timestamps.  
   - **mkdir**: Create directories (nested with `-p`).  
   - **cp**: Duplicate files/directories; use `-a` to preserve metadata.  
   - **mv**: Move or rename; minimal overhead on the same filesystem.  
   - **rm/rmdir**: Delete files/directories; `rmdir` only empties, `rm -r` for non-empty.

2. **Operational Insights (3)**  
   - Always keep backups of critical configs/logs.  
   - Use interactive or backup options in production to prevent accidental overwrites.  
   - Monitor disk I/O during large copy/move operations, especially under high load.

3. **Best Practices (3)**  
   - Check disk usage (`df -h`) before large copies to avoid running out of space.  
   - Combine commands with search filters (`grep`, `awk`) for targeted log analysis.  
   - Keep consistent naming conventions and date-based backups for quick rollbacks.

4. **Preview of Next Topic**  
   - **Day 3**: File Permissions & Ownership. We’ll explore how to secure files and implement least-privilege principles—crucial for stable, secure SRE operations.

---

## **11. Further Learning Resources**

### **🟢 Beginner**

1. **The Linux Command Line by William Shotts**  
   - [https://linuxcommand.org/tlcl.php](https://linuxcommand.org/tlcl.php)  
   - *Teaches* foundational commands in a clear style. *How it helps* new users learn everyday file operations.

2. **Beginner’s Guide to the Bash Terminal**  
   - [https://ubuntu.com/tutorials/command-line-for-beginners](https://ubuntu.com/tutorials/command-line-for-beginners)  
   - *Teaches* simple navigation, file creation, and editing. *How it helps* build confidence in basic CLI usage.

### **🟡 Intermediate**

1. **Linux Fundamentals: Pluralsight Course**  
   - [https://www.pluralsight.com/courses/linux-fundamentals](https://www.pluralsight.com/courses/linux-fundamentals)  
   - *Teaches* broader CLI operations, including advanced file manipulations. *How it connects* to operational tasks for system administration.

2. **ArchWiki: Core Utilities**  
   - [https://wiki.archlinux.org/title/Core_utilities](https://wiki.archlinux.org/title/Core_utilities)  
   - *Teaches* in-depth usage of essential commands. *How it connects* by providing deeper details on flags and behaviors in real-world usage.

### **🔴 SRE-Level**

1. **Google SRE Workbook (Chapter: Practical Alerting)**  
   - [https://sre.google/workbook/chapters/alerting/](https://sre.google/workbook/chapters/alerting/)  
   - *Teaches* how SREs integrate logs and file management with alerting. *How it elevates* reliability engineering by focusing on operational response flow.

2. **Advanced Bash-Scripting Guide**  
   - [https://www.tldp.org/LDP/abs/html/](https://www.tldp.org/LDP/abs/html/)  
   - *Teaches* powerful scripting techniques for automation. *How it elevates* reliability with robust file-handling scripts.

3. **Logrotate Documentation**  
   - [https://linux.die.net/man/8/logrotate](https://linux.die.net/man/8/logrotate)  
   - *Teaches* advanced log rotation strategies. *How it elevates* reliability by automating routine log management and avoiding disk saturation.

---

**Congratulations!** You’ve completed **Day 2** of our Linux SRE Training. Mastering file manipulation is a cornerstone of systems reliability—today’s knowledge helps you handle logs, configs, and backups reliably. Up next: **permissions and ownership** for secure and organized systems!
