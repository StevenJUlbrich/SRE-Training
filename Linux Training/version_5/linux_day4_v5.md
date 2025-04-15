# Day 4: Text Processing & Searching

---

## 1. Introduction

Welcome to **Day 4** of your Linux SRE Training! Today’s focus is on **text processing and searching** tools: **grep**, **find**, **pipes (|)**, and **redirection (>, >>, <)**. These powerful commands enable SREs to quickly extract insights from logs, locate files in complex directory structures, and build efficient data-processing pipelines.

### Why This Matters for SRE

- **Reliability**: Rapid diagnosis of system logs reduces downtime.
- **Scalability**: Automating text searches and file operations ensures systems can grow without becoming unmanageable.
- **Efficiency**: Combining commands through pipes and redirection helps reduce manual overhead.

### Learning Objectives

#### 🔍 Beginner

1. Understand how to perform basic searches with `grep`
2. Locate files and directories using `find` with simple criteria
3. Apply fundamental pipes and redirection for basic data processing

#### 🧩 Intermediate

4. Use advanced `grep` and `find` options to filter massive logs and directories
5. Build multi-command pipelines for routine operational tasks
6. Redirect outputs and inputs safely and systematically in real scenarios

#### 💡 SRE-Level

7. Correlate logs across distributed systems using complex `grep` patterns
8. Automate large-scale file searches and modifications via scripts
9. Optimize performance by chaining commands with minimal resource overhead

### Connection to Previous & Future Learning

- **Previously**: We covered file permissions, ownership, and `sudo` for secure resource management.
- **Next**: We’ll build on text processing with more advanced tools (`sed`, `awk`) and explore deeper automation patterns to streamline your SRE workflows.

---

## 2. Core Concepts

### 2.1 Text Processing & Searching: A Bird’s-Eye View

1. **Beginner Analogy**: Think of text processing as "finding and sorting notes in a notebook"—tools like `grep` help you find a specific note, while `pipes` let you hand that note off to someone else for further review.

2. **Technical Explanation**: Linux stores most configuration, logs, and system information as text. Tools like `grep` and `find` allow you to query and manipulate these text-based resources with powerful pattern matching and file-search capabilities.

3. **SRE Application**: SREs rely on quick searches of logs to isolate issues, find config references, or identify large files impacting disk usage. Proficient text processing is a critical skill for diagnosing system health.

4. **System Impact**: Commands like `grep` and `find` can be resource-intensive if run on massive directories or logs. However, when used correctly and selectively, they streamline troubleshooting and reduce mean-time-to-recovery.

---

## 3. Command Breakdown

### 3.1 Command: grep (Global Regular Expression Print)

**Command Overview:**  
`grep` searches text for patterns using regular expressions. SREs use it to sift through logs, configuration files, and codebases for specific strings (e.g., errors, warnings, or request IDs) in real time.

**Syntax & Flags:**

| Flag/Option | Syntax Example                          | Description                                             | SRE Usage Context                                      |
|-------------|------------------------------------------|---------------------------------------------------------|--------------------------------------------------------|
| `-i`        | `grep -i "error" file.log`             | Case-insensitive search                                | Useful for catching varied log formats (Error, ERROR) |
| `-r`        | `grep -r "pattern" /var/log`           | Recursive search through directories                   | Scanning entire log directories for a pattern         |
| `-n`        | `grep -n "timeout" app.log`            | Show line numbers of matches                           | Pinpointing exact lines that need investigation       |
| `-v`        | `grep -v "INFO" app.log`                | Invert match: show non-matching lines                  | Filtering out noise (e.g., ignoring INFO lines)       |
| `-E`        | `grep -E "(ERROR|WARN)" app.log`        | Use extended regular expressions                       | Capturing multiple patterns in a single command       |
| `-A/-B/-C`  | `grep -C 2 "CRITICAL" system.log`       | Show context lines (After, Before, Combined)           | Quickly see surrounding log lines for better context  |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Search for the word "error" in app.log (case-sensitive)
$ grep "error" app.log
2025-03-29 10:15:42 ERROR Unable to connect to server
2025-03-29 11:00:05 ERROR Database timeout occurred
```

- 🧩 **Intermediate Example:**

```bash
# Perform a recursive, case-insensitive search for 'login failed' in /var/log
$ grep -ir "login failed" /var/log
/var/log/auth.log:Mar 29 09:45:21 server sshd[1234]: PAM 2 more login failed...
/var/log/auth.log:Mar 29 10:01:12 server sshd[2233]: PAM 1 more login failed...
```

- 💡 **SRE-Level Example:**

```bash
# Search for errors or warnings across multiple logs, showing 2 lines of context
$ grep -E -C 2 "(ERROR|WARN)" /var/log/app/*.log
/var/log/app/app.log-2025-03-29:2025-03-29 14:02:11 INFO Starting service
/var/log/app/app.log-2025-03-29-2025-03-29 14:02:12 WARN High latency detected
/var/log/app/app.log-2025-03-29:2025-03-29 14:02:13 INFO Fallback mechanism triggered
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Quoting your pattern (`"pattern"`) avoids issues with special shell characters.
- 🧠 **Beginner Tip:** Start with smaller files or use partial logs (`tail`, `head`) to practice searching without overwhelming output.

- 🔧 **SRE Insight:** Combine `grep` with other commands (e.g., `grep "ERROR" | grep -v "DEBUG"`) to refine searches.
- 🔧 **SRE Insight:** Store common regex patterns in scripts or config files for faster repetition.

- ⚠️ **Common Pitfall:** Using `grep -r` on the root directory `/` can hang or cause massive I/O. Narrow the search path.
- ⚠️ **Common Pitfall:** Forgetting to escape special regex characters (like `.` or `?`) leads to unexpected matches.

- 🚨 **Security Note:** Searching logs might reveal sensitive data (passwords, tokens). Be mindful of who can see your command history or shared outputs.

- 💡 **Performance Impact:** `grep` uses CPU heavily if run on large files or directories. Filtering logs by date or size first can mitigate performance hits.

---

### 3.2 Command: find (Locate Files and Directories)

**Command Overview:**  
`find` navigates directory trees to locate files or directories based on criteria like name, size, type, or modification time. SREs rely on it to discover large files consuming disk space, identify outdated logs, or locate misnamed config files quickly.

**Syntax & Flags:**

| Flag/Option | Syntax Example                                          | Description                                 | SRE Usage Context                                    |
|-------------|----------------------------------------------------------|---------------------------------------------|-------------------------------------------------------|
| `-name`     | `find /etc -name "*.conf"`                             | Find files by exact name match             | Searching config files by extension                  |
| `-iname`    | `find /opt -iname "release*"`                           | Case-insensitive name match                 | Handling varied naming conventions in large repos    |
| `-type`     | `find /data -type d`                                    | Filter by file type (f=file, d=directory)   | Identifying directories or symlinks for auditing      |
| `-size`     | `find /var/log -size +100M`                              | Search by file size                         | Finding massive logs that may cause disk pressure     |
| `-mtime`    | `find /tmp -mtime +7`                                    | Files modified more than 7 days ago         | Cleaning stale temp files for housekeeping           |
| `-exec`     | `find . -name "*.log" -exec rm {} \;`                 | Execute a command on each match            | Automating tasks like deletion, copying, or archiving |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Find all .txt files in the current directory
$ find . -name "*.txt"
./notes.txt
./backup/config-old.txt
```

- 🧩 **Intermediate Example:**

```bash
# Search for directories named "archive", ignoring case
$ find /var -type d -iname "archive"
/var/Log/ARCHIVE
/var/www/logs/archive
```

- 💡 **SRE-Level Example:**

```bash
# Find logs over 200MB in /var/log and compress them automatically
$ find /var/log -type f -size +200M -exec gzip {} \;
# This helps prevent disk exhaustion in production logs
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Always specify a starting directory (e.g., `find .` or `find /home/user`) to avoid searching entire filesystem.
- 🧠 **Beginner Tip:** Test with simple name filters before adding advanced flags like `-exec`.

- 🔧 **SRE Insight:** Combine `-exec` with caution—mass deletions or modifications can cause disruptions if used improperly.
- 🔧 **SRE Insight:** For large-scale systems, break down searches by partition or mount point to avoid scanning irrelevant data.

- ⚠️ **Common Pitfall:** Omitting a backslash when using `\;` in `-exec` results in syntax errors.
- ⚠️ **Common Pitfall:** Searching large directories without restricting scope can spike I/O and slow the system.

- 🚨 **Security Note:** Use `-perm` flags to find world-writable files or directories, which might be a security risk.

- 💡 **Performance Impact:** On huge filesystems, `find` can become expensive. Pair with `-maxdepth`, `-prune`, or search specific paths.

---

### 3.3 Command: pipes (|) (Command Chaining)

**Command Overview:**  
Pipes (`|`) feed the standard output of one command into the standard input of another. This chain-based approach is core to Unix philosophy and SRE workflows, letting you build mini data pipelines.

**Syntax & Flags:**

| Flag/Option | Syntax Example          | Description                                         | SRE Usage Context                         |
|-------------|-------------------------|-----------------------------------------------------|-------------------------------------------|
| `|` (pipe)  | `command1 | command2`  | Send output of `command1` as input to `command2`   | Quick filtering and transformation flows  |
| `| ... |`    | `cmd1 | cmd2 | cmd3`  | Chain multiple commands in sequence                | Building complex data analyses            |
| (N/A)       | `ps aux | grep nginx`  | Common usage example for process filtering         | Troubleshooting services in real time     |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# List all files, then filter only those containing "report"
$ ls | grep "report"
monthly_report.txt
report_summary.doc
```

- 🧩 **Intermediate Example:**

```bash
# Check running processes, sort by memory usage, and view top 5
$ ps aux | sort -rnk 4 | head -5
root       1234  30.2  1.5 124392 12340 ?       Ssl  Mar29  10:11 /usr/bin/java
root       2231  25.9  1.1  99348 10480 ?       Sl   Mar29   8:55 /usr/bin/python
...
```

- 💡 **SRE-Level Example:**

```bash
# Extract IP addresses from auth.log, find unique ones, and count occurrences
$ grep -oE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" /var/log/auth.log \
  | sort | uniq -c | sort -rn | head
   45 192.168.1.15
   30 192.168.1.100
   12 10.0.0.3
   ...
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Use `head`, `tail`, `sort`, `uniq` with pipes for basic data manipulation.
- 🧠 **Beginner Tip:** If output scrolls too fast, pipe into `less` for interactive viewing.

- 🔧 **SRE Insight:** Combine pipes with performance monitoring commands (e.g., `top -b | grep process_name`) to parse live data.
- 🔧 **SRE Insight:** Shell scripting often leverages multiple pipes in a single line to automate repeated tasks.

- ⚠️ **Common Pitfall:** Misplacing a space or using the wrong command order can yield no results or errors.
- ⚠️ **Common Pitfall:** Very long pipelines can be hard to debug; consider intermediate checks or break them down.

- 🚨 **Security Note:** Be cautious piping commands that contain secret keys or credentials into logs or third-party tools.

- 💡 **Performance Impact:** Each pipe spawns a new process. In extremely large-scale workflows, consider specialized tools (e.g., `awk` or `jq`).

---

### 3.4 Command: redirection (>, >>, <)

**Command Overview:**  
Redirection allows you to direct a command’s output to files or read input from files instead of the terminal. SREs utilize it to collect logs, append data for record-keeping, and script tasks requiring file input.

**Syntax & Flags:**

| Flag/Option  | Syntax Example               | Description                               | SRE Usage Context                                   |
|--------------|------------------------------|-------------------------------------------|-----------------------------------------------------|
| `>`          | `echo "Hello" > file.txt`    | Overwrite output to file                  | Creating or replacing config/log data               |
| `>>`         | `echo "New line" >> file.txt`| Append output to file                     | Appending results to existing logs or reports       |
| `<`          | `grep "pattern" < input.txt` | Use a file as input instead of stdin       | Feeding prepared data files into commands           |
| `2>`         | `command 2> error.log`       | Redirect error output (stderr)            | Separating errors from normal logs for clarity      |
| `&>`         | `command &> alloutput.log`   | Redirect both stdout and stderr to a file | Capturing everything for debugging or auditing      |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
# Save the list of files to filelist.txt (overwrite if exists)
$ ls /etc > filelist.txt
```

- 🧩 **Intermediate Example:**

```bash
# Append the current memory status to system_report.txt
$ free -h >> system_report.txt
# Now system_report.txt grows with new data each time you run the command
```

- 💡 **SRE-Level Example:**

```bash
# Capture both output and errors from a backup script in separate files
$ /usr/local/bin/db_backup.sh > /tmp/backup_stdout.log 2> /tmp/backup_stderr.log
# This helps you see normal progress messages vs. error messages distinctly.
```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Overwriting (`>`) can accidentally delete existing file contents—double-check before using.
- 🧠 **Beginner Tip:** `>` and `>>` can be used with almost any command, from `echo` to complex scripts.

- 🔧 **SRE Insight:** Splitting stdout and stderr allows focusing on failure modes without sifting through normal output.
- 🔧 **SRE Insight:** In CI/CD pipelines, logs can be redirected to artifacts for post-run analysis and archiving.

- ⚠️ **Common Pitfall:** Misuse of `>` instead of `>>` can cause data loss or partial log overwriting.
- ⚠️ **Common Pitfall:** Using the same file for both stdout and stderr can lead to jumbled outputs.

- 🚨 **Security Note:** Redirecting logs containing sensitive data to world-readable files can expose credentials.

- 💡 **Performance Impact:** Redirection is generally light, but writing massive data to disk can be an I/O bottleneck.

---

## 4. System Effects

1. **Filesystem Changes**: Using `>` can overwrite or create new files; `>>` appends data, potentially leading to large files if not managed.
2. **Resource Usage**: `grep` and `find` may consume high CPU or I/O when scanning large directories or logs.
3. **Security Considerations**: Searching logs can expose secrets, and redirecting outputs might create files with sensitive data.
4. **Monitoring Implications**: Tools like `grep` and `find` can be integrated into scripts that feed data into monitoring pipelines or dashboards.

---

## 5. Hands-On Exercises

### 🔍 Beginner Exercises

1. **Basic Grep**: Create a file named `sample.txt` containing some text. Use `grep` to find a specific word in it.
2. **Find by Name**: In your home directory, locate any file ending with `.sh` using `find`.
3. **Redirect Output**: Run `ls -l /etc` and redirect the output into a file called `etc_list.txt`.

### 🧩 Intermediate Exercises

1. **Recursive Grep**: In `/var/log`, search for the word `error` in all files recursively. Use an option to show line numbers.
2. **File Size Hunt**: Use `find` to locate files larger than 50MB in `/var/log` and output the list to `large_logs.txt`.
3. **Pipeline Sorting**: Generate a list of running processes (`ps aux`), then pipe to `grep` for processes containing `root`, and finally sort by memory usage.

### 💡 SRE-Level Exercises

1. **Multi-Service Log Analysis**: Combine `grep` and pipes to extract error lines from multiple log files (e.g., `app.log`, `db.log`), and store them in `all_errors.log`.
2. **Disk Cleanup Script**: Use `find` with `-exec` or piping to `xargs` to automatically compress or remove logs older than 7 days in `/var/log`.
3. **Redirect for Debugging**: Run a custom script and redirect stdout/stderr to separate files. Investigate the differences between normal output and error output.

---

## 6. Quiz Questions

### 🔍 Beginner

1. **Which flag in `grep` makes the search case-insensitive?**
2. **What does `>` do when used after a command?**
3. **Which command searches for `.conf` files in `/etc`?** (Fill in the blank: `find /etc ______ "*.conf"`)

### 🧩 Intermediate

1. **How do you show line numbers with `grep`?** (Which option?)
2. **Which command locates files over 100MB in size?** (Fill in the blank: `find /var/log ______ +100M`)
3. **What does the `|` operator do in `ls | grep script`?**

### 💡 SRE-Level

1. **How can you redirect both stdout and stderr to the same file?** (Provide the redirection operator)
2. **In a pipeline (`cmd1 | cmd2 | cmd3`), which command receives the output of `cmd2`?**
3. **Name one reason why searching logs with `grep -r /` might be risky in production.**

### Instructor key with explanations is provided separately

---

## 7. Troubleshooting

1. **High CPU Usage with `grep`**
   - **Symptom**: System load spikes when running `grep -r /var/log`.
   - **Cause**: The search might be scanning very large or archived log files.
   - **Diagnostic**: Check file sizes in `/var/log` and consider filtering by subdirectory or file extension.
   - **Resolution**: Narrow the search path (e.g., `/var/log/app`) or limit recursion.
   - **Prevention**: Implement log rotation and store older logs in compressed form.

2. **Accidental Overwrite of Critical File**
   - **Symptom**: Running `ls > important_file.txt` erases previous content.
   - **Cause**: `>` overwrote the file.
   - **Diagnostic**: Inspect `ls -l` timestamps or check file content.
   - **Resolution**: Restore from backup if available.
   - **Prevention**: Use `>>` for appending or confirm file existence before overwriting.

3. **Command Not Found in `-exec`**
   - **Symptom**: `find` returns an error: `-exec rm {} ; not found`.
   - **Cause**: Missing backslash or spacing in `-exec rm {} \;`.
   - **Diagnostic**: Verify exact syntax `-exec command {} \;`.
   - **Resolution**: Correct the command syntax.
   - **Prevention**: Always check small test commands before large-scale deletions.

---

## 8. FAQ

### 🔍 Beginner (3)

1. **Can I use `grep` on multiple files at once?**  
   Yes. Simply list files: `grep "pattern" file1.txt file2.txt`.

2. **How do I stop a long-running `find` or `grep` command?**  
   Press `Ctrl + C` to interrupt.

3. **Is `>` the same as copy-and-paste into a file?**  
   Functionally similar for text output, but `>` is more precise and overwrites the file automatically.

### 🧩 Intermediate (3)

1. **How can I use a pattern file with `grep`?**  
   Use `-f patternfile.txt`, where each line in `patternfile.txt` is treated as a pattern.

2. **Can `find` search inside file contents like `grep`?**  
   By default, `find` only looks at filenames and metadata. Combine with `-exec grep` to search file contents.

3. **What happens if I combine `>` and `>>` in the same command?**  
   The last operator in the sequence determines whether you overwrite or append (not recommended to mix them).

### 💡 SRE-Level (3)

1. **How do I avoid scanning NFS or special filesystems when using `find`?**  
   Use flags like `-xdev` or manually prune directories that cross mount points.

2. **How do I handle pipeline failures in a script (e.g., `cmd1 | cmd2 | cmd3`)?**  
   In Bash, use `set -o pipefail`, which causes the pipeline to fail if any command fails.

3. **Is there a safe way to mass-delete files with `find -exec`?**  
   Yes, test your command with `-exec echo rm {}` first, ensuring you see the correct targets before removing `echo`.

---

## 9. SRE Scenario: Investigating a Sudden Log Surge

**Situation**: You receive an alert about rapidly growing log sizes on the `web-prod` server. Disk usage is at 90%.

**Steps**:

1. **Identify large logs**: `find /var/log/nginx -type f -size +100M -exec ls -lh {} \;`  
   *Reasoning*: Quickly see which logs exceed 100MB, since these are top disk consumers.
2. **Check for Error Patterns**: `grep -i "error" /var/log/nginx/access.log | tail -n 50`  
   *Reasoning*: Determine if repeated errors or unusual traffic is causing the logs to grow.
3. **Correlate with System Load**: `ps aux | sort -rnk 3 | head -5`  
   *Reasoning*: Check if high CPU processes relate to the log surge.
4. **Redirect Key Outputs**: `df -h > /tmp/disk_usage_snapshot.txt`  
   *Reasoning*: Capture a snapshot of disk usage for your incident report.
5. **Narrow Down IPs**: `grep -oE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" /var/log/nginx/access.log | sort | uniq -c | sort -rn | head`  
   *Reasoning*: Identify suspicious IPs or traffic patterns.
6. **Mitigate**: Compress older logs: `find /var/log/nginx -type f -mtime +2 -exec gzip {} \;`  
   *Reasoning*: Free up disk space while preserving historical data.
7. **Monitor**: Use `tail -f /var/log/nginx/access.log | grep --color=always "error"` in a separate session to watch for new errors.

*Connection to SRE Principles*: This approach demonstrates data-driven triage, quick feedback loops, and an emphasis on preserving system stability.

---

## 10. Key Takeaways

1. **Command Summary**:
   - `grep`: Filters text using patterns
   - `find`: Locates files by name, size, type, etc.
   - Pipes (`|`): Chains commands for powerful, flexible workflows
   - Redirection (`>`, `>>`, `<`): Manages inputs and outputs in scripts
   - Integrating them is key for efficient text processing.

2. **Operational Insights**:
   - Always refine your search scope to minimize resource usage.
   - For safe production usage, consider logging strategies and proper file handling.
   - Combining commands in pipelines can drastically speed up analysis.

3. **Best Practices**:
   - Test destructive commands (like `rm` with `-exec`) in a small or echo-only mode first.
   - Isolate large searches to specific paths to avoid system-wide performance hits.
   - Separate stdout and stderr to improve troubleshooting clarity.

4. **Preview of Next Topic**:
   - We’ll delve into advanced text manipulation with `sed` and `awk`, enabling more complex transformations and data wrangling for SRE tasks.

---

## 11. Further Learning Resources

### 🔍 Beginner (2–3 Resources)

1. **[Grep Tutorial (Linuxize)](https://linuxize.com/post/grep-command/)**  
   Comprehensive coverage of basic grep usage and flags—perfect to build foundational skills.
2. **[Find Command Basics (GeeksforGeeks)](https://www.geeksforgeeks.org/find-command-in-linux-with-examples/)**  
   Explains fundamental `find` syntax with step-by-step examples for beginners.
3. **[Redirection & Pipes (Ryan’s Tutorials)](https://ryanstutorials.net/linuxtutorial/piping.php)**  
   Introduces piping and redirection with visuals—great for seeing data flow.

### 🧩 Intermediate (2–3 Resources)

1. **[GNU grep Manual](https://www.gnu.org/software/grep/manual/grep.html)**  
   Delivers in-depth explanations of regex syntax, performance considerations, and advanced usage.
2. **[Advanced Find Tricks (Linode Docs)](https://www.linode.com/docs/guides/find-command/)**  
   Shows more sophisticated `find` operations, including combining multiple tests and using `-exec` safely.
3. **[Bash Pipelines in Practice (DigitalOcean Tutorial)](https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection)**  
   Provides advanced examples of chaining commands and redirecting streams effectively.

### 💡 SRE-Level (2–3 Resources)

1. **[SRE Edition: Log Searching Strategies (Datadog Blog)](https://www.datadoghq.com/blog/log-analysis-monitoring/)**  
   Discusses best practices for large-scale log searching and correlation.
2. **[Google SRE Workbook — Monitoring & Alerting](https://sre.google/workbook/alerting-on-sli/)**  
   Explores how advanced filtering (like `grep`) plays into monitoring design and reliability.
3. **[Performance Tuning for Unix Pipelines (Brendan Gregg)](http://www.brendangregg.com/)**  
   Offers insights on pipeline performance under heavy loads, relevant to SRE-scale tasks.
