# 🚀 Day 4: Text Processing & Searching (Enhanced SRE Training)

---

## 📌 Introduction

### 🔄 Recap of Day 3

On Day 3, we explored **file permissions** and **ownership**. You learned how to read and modify file permissions (`chmod`), how to change ownership (`chown`, `chgrp`), and the importance of using `sudo` effectively. These concepts help you secure resources and manage system privileges safely.

### 📅 Today’s Topics

Today, we focus on four core Linux capabilities:

- **grep** (pattern searching)
- **find** (locating files)
- **pipes** (`|`, chaining commands)
- **redirection** (`>`, `>>`, `<`)

These are fundamental for every SRE, enabling the **efficient processing of textual data**, quick **log analysis**, and powerful **automation** through command chaining.

### 🎯 Learning Objectives

- **Beginner (🔍)**
  1. Perform basic searches with `grep`
  2. Locate files using `find` with simple criteria
  3. Use simple pipes and redirection for data manipulation

- **Intermediate (🧩)**
  4. Apply advanced `grep` and `find` options in large or complex directories
  5. Build multi-command pipelines for routine operational tasks
  6. Safely redirect outputs and inputs in real-world scenarios

- **SRE-Level (💡)**
  7. Perform distributed log correlation with complex `grep` patterns
  8. Automate large-scale file searches and modifications with scripting
  9. Optimize performance by chaining commands and managing resource usage

### Connection to Previous & Future Learning

- **Previously**: You learned about permissions and secure resource management.
- **Today**: You’ll expand your toolbox with text-processing commands integral to SRE workflows.
- **Next**: We’ll build on these fundamentals in Day 5 with advanced text manipulation tools (`sed`, `awk`) and deeper automation strategies.

### Why Text Processing is Fundamental to SRE

1. **Rapid Diagnosis**: Logs contain critical data for understanding system behavior under load or during failures.
2. **Efficient File Management**: Large, complex directory structures require robust search capabilities.
3. **Automation & Scalability**: Chaining commands with pipes and redirection simplifies routine tasks and scales up easily.
4. **Reliability & Observability**: Quickly extracting data from logs and config files improves mean time to repair (MTTR) and overall system reliability.

---

## 📚 Core Concepts

### 1. Text Processing & Searching: The Big Picture

- **Beginner Analogy**: Picture your file system as a huge library. **`grep`** helps you find specific words in a pile of books, while **`find`** locates the correct book on the shelves. Pipes let you pass these books from one librarian to the next, each performing a different task.
- **Technical Explanation**: In Linux, most configurations, logs, and system info are stored as text files. Commands like `grep` and `find` allow you to quickly sift through these text-based resources using pattern matching and metadata-based searches.
- **SRE Application**: Frequent tasks involve diagnosing logs, searching for specific config directives, or automating cleanup. Mastering these commands is key to swiftly resolving incidents.
- **System Impact**: Large recursive searches can consume CPU and I/O. Thoughtful usage and scope limitation keep systems responsive.

### 2. Command Chaining & Redirection

- **Beginner Analogy**: Think of a pipeline where the output of one stage is the input to the next. Redirection is like deciding whether the end product goes into a bottle, a barrel, or the trash.
- **Technical Explanation**: The pipe symbol `|` sends stdout of one command directly into stdin of another. Redirection operators (`>`, `>>`, `<`) manage file I/O, letting you store results or read inputs from files.
- **SRE Application**: Combining commands (e.g., `grep | sort | uniq`) is essential in analyzing massive logs. Redirection captures logs or error messages into separate files for deeper investigation.
- **System Impact**: Each pipe spawns a new process. Overusing them in a single command can be difficult to debug, but typically remains lightweight. Large-scale redirection can impact disk I/O.

---

## 💻 Command Breakdown

### 3.1 Command: **grep** (Global Regular Expression Print)

**Command Overview:**
`grep` searches text files for patterns (by default, basic regular expressions). SREs use it daily for finding errors, warnings, or request IDs within logs.

**Syntax & Flags:**

| Flag/Option | Syntax Example                  | Description                                          | SRE Usage Context                                   |
|-------------|---------------------------------|------------------------------------------------------|-----------------------------------------------------|
| `-i`        | `grep -i "error" file.log`     | Case-insensitive search                              | Capture variations like `Error`, `ERROR`, `error`   |
| `-r`        | `grep -r "pattern" /var/log`  | Recursive search through directories                 | Quickly scan entire log folders                     |
| `-n`        | `grep -n "timeout" app.log`   | Show line numbers                                    | Pinpoint exact lines to investigate                 |
| `-v`        | `grep -v "INFO" app.log`       | Invert match (exclude lines containing `INFO`)       | Filter out noise when logs are too verbose          |
| `-E`        | `grep -E "(ERROR|WARN)" file`  | Use extended regular expressions                     | Match multiple patterns at once                     |
| `-A/-B/-C`  | `grep -C 2 "CRITICAL" sys.log` | Show lines before/after match for context            | Provide immediate context around crucial log entries|

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
  # Recursive, case-insensitive search for 'login failed' in /var/log
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

- 🧠 **Beginner Tip:** Always quote your pattern (e.g., `grep "pattern" file.txt`) to avoid shell interpretation.
- 🧠 **Beginner Tip:** Start small by searching specific files to reduce massive output.

- 🔧 **SRE Insight:** Combine multiple `grep` commands to refine results (e.g., `grep ERROR | grep -v DEBUG`).
- 🔧 **SRE Insight:** Keep a library of common regex patterns for frequent tasks.

- ⚠️ **Common Pitfall:** Using `grep -r /` can scan the entire filesystem and overload the system.
- ⚠️ **Common Pitfall:** Not escaping special characters (`.`, `?`, `*`) can cause unexpected matches.

- 🚨 **Security Note:** Sensitive data can appear in logs. Be mindful who can see your search outputs.

- 💡 **Performance Impact:** `grep` can be CPU-intensive on huge logs. Narrow search paths or use additional filters to mitigate.

---

### 3.2 Command: **find** (Locate Files and Directories)

**Command Overview:**
`find` navigates directory trees to locate files by criteria (e.g., name, size, modification date). This helps SREs quickly discover large logs, configuration files, or erroneous permission settings.

**Syntax & Flags:**

| Flag/Option | Syntax Example                          | Description                                    | SRE Usage Context                                   |
|-------------|------------------------------------------|------------------------------------------------|------------------------------------------------------|
| `-name`     | `find /etc -name "*.conf"`             | Finds files by exact name match                | Searching for config files by extension             |
| `-iname`    | `find /opt -iname "release*"`          | Case-insensitive name match                    | Handling varied naming conventions                  |
| `-type`     | `find /data -type d`                    | Filter by file type (f=file, d=directory)      | Locating directories or symlinks for audits         |
| `-size`     | `find /var/log -size +100M`             | Search by file size                            | Identifying large logs that eat disk space          |
| `-mtime`    | `find /tmp -mtime +7`                   | Files modified more than 7 days ago            | Housekeeping stale temp files                       |
| `-exec`     | `find . -name "*.log" -exec rm {} \;` | Execute a command on each match                | Automating tasks like deletion, copying, archiving  |

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
  ```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Always specify a starting directory (e.g., `find .`) to avoid scanning the entire system.
- 🧠 **Beginner Tip:** Test commands on a small directory before attempting large-scale deletions with `-exec`.

- 🔧 **SRE Insight:** Using `-exec` can be powerful but risky. Use `-exec echo rm {} \;` first to confirm your targets.
- 🔧 **SRE Insight:** Pair `find` with `-prune` or `-maxdepth` to limit search scope and reduce resource load.

- ⚠️ **Common Pitfall:** Missing the backslash before `;` in `-exec` leads to syntax errors.
- ⚠️ **Common Pitfall:** Searching very large directories without restricting scope can degrade performance.

- 🚨 **Security Note:** Use `-perm` to find world-writable files that pose security risks.

- 💡 **Performance Impact:** On huge filesystems, `find` can be expensive. Narrow your path or apply multiple filters.

---

### 3.3 Command: **pipes** (`|`)

**Command Overview:**
Pipes chain commands together: the output of one is the input of the next. This is fundamental to Linux’s philosophy of building complex solutions from simple tools.

**Syntax & Flags:**

| Symbol    | Syntax Example          | Description                                            | SRE Usage Context                         |
|-----------|-------------------------|--------------------------------------------------------|-------------------------------------------|
| `|` (pipe)| `command1 | command2`  | Send `command1` output to `command2`                   | Quick filtering and transformation flows  |
| (N/A)     | `cmd1 | cmd2 | cmd3`   | Chain multiple commands in sequence                    | Building complex data analyses            |

**Tiered Examples:**

- 🔍 **Beginner Example:**

  ```bash
  # List files, then filter only those containing "report"
  $ ls | grep "report"
  monthly_report.txt
  report_summary.doc
  ```

- 🧩 **Intermediate Example:**

  ```bash
  # Check running processes, sort by memory usage, view top 5
  $ ps aux | sort -rnk 4 | head -5
  root 1234 30.2 1.5 124392 12340 ? Ssl Mar29 10:11 /usr/bin/java
  root 2231 25.9 1.1 99348 10480 ? Sl  Mar29  8:55 /usr/bin/python
  ...
  ```

- 💡 **SRE-Level Example:**

  ```bash
  # Extract IPs from auth.log, find unique, count occurrences
  $ grep -oE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" /var/log/auth.log \
    | sort | uniq -c | sort -rn | head
       45 192.168.1.15
       30 192.168.1.100
       12 10.0.0.3
       ...
  ```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Pipe into `less` (e.g., `ls -l | less`) to scroll through large outputs.
- 🧠 **Beginner Tip:** Common combos: `grep`, `sort`, `uniq`, `wc -l`, etc.

- 🔧 **SRE Insight:** Use pipelines in scripts to quickly parse logs or combine with monitoring commands.
- 🔧 **SRE Insight:** For advanced filtering, consider using `awk` or `jq` in the pipeline.

- ⚠️ **Common Pitfall:** A single misplaced space can break your pipeline logic.
- ⚠️ **Common Pitfall:** Overly long pipelines can be hard to maintain or debug.

- 🚨 **Security Note:** Be careful not to pipe sensitive information into logs or external tools.

- 💡 **Performance Impact:** Typically small overhead, but each `|` spawns a subshell. For enormous data sets, consider specialized tools.

---

### 3.4 Command: **redirection** (`>`, `>>`, `<`)

**Command Overview:**
Redirection controls where command input comes from and where output goes. SREs use it to capture logs, create reports, or separate normal output from errors.

**Syntax & Flags:**

| Operator  | Syntax Example                 | Description                                   | SRE Usage Context                                     |
|-----------|--------------------------------|-----------------------------------------------|--------------------------------------------------------|
| `>`       | `echo "Hello" > file.txt`      | Overwrite output to file                       | Creating or replacing config/log data                  |
| `>>`      | `echo "New line" >> file.txt`  | Append output to file                          | Appending results to logs or reports                  |
| `<`       | `grep "pattern" < input.txt`   | Use file as input instead of stdin             | Feeding prepared data into commands                   |
| `2>`      | `command 2> error.log`         | Redirect stderr to a file                      | Separating errors from normal logs                    |
| `&>`      | `command &> alloutput.log`     | Redirect both stdout and stderr to one file    | Full capture for debugging or auditing                |

**Tiered Examples:**

- 🔍 **Beginner Example:**

  ```bash
  # Save list of files to filelist.txt (overwrites if exists)
  $ ls /etc > filelist.txt
  ```

- 🧩 **Intermediate Example:**

  ```bash
  # Append memory status to system_report.txt
  $ free -h >> system_report.txt
  # system_report.txt grows with each command run
  ```

- 💡 **SRE-Level Example:**

  ```bash
  # Capture both normal output and errors from a backup script
  $ /usr/local/bin/db_backup.sh > /tmp/backup_stdout.log 2> /tmp/backup_stderr.log
  ```

**Instructional Notes:**

- 🧠 **Beginner Tip:** `>` overwrites, `>>` appends. Double-check which you need before running.
- 🧠 **Beginner Tip:** Use redirection to store command output for later review.

- 🔧 **SRE Insight:** Splitting stdout/stderr is crucial for debugging production scripts.
- 🔧 **SRE Insight:** In CI/CD pipelines, capturing logs in files helps with post-build analysis.

- ⚠️ **Common Pitfall:** Confusing `>` with `>>` can wipe out important data.
- ⚠️ **Common Pitfall:** Redirecting to `/dev/null` can hide meaningful errors.

- 🚨 **Security Note:** Redirected files might contain secrets or tokens. Protect their permissions.

- 💡 **Performance Impact:** Writing massive amounts of data to disk can become an I/O bottleneck.

---

## 🛠️ System Effects

1. **Filesystem Changes**: Using `>` can overwrite files. `>>` can grow files quickly.
2. **Resource Usage**: `grep` and `find` on large directories consume CPU and I/O.
3. **Security**: Searching logs can reveal secrets; be mindful where outputs are saved.
4. **Monitoring**: Commands like `grep` and `find` often feed into scripts that update dashboards or alerts.
5. **Performance**: Large-scale text processing requires careful scoping (avoid scanning unnecessary paths).

---

## 🎯 Hands-On Exercises

### 🔍 Beginner Exercises

1. **Basic Grep**: Create a file named `sample.txt` with text lines. Use `grep` to find a specific word.
2. **Find by Name**: In your home directory, use `find` to locate any file ending with `.sh`.
3. **Redirect Output**: Run `ls -l /etc` and redirect it into a file called `etc_list.txt`.

### 🧩 Intermediate Exercises

1. **Recursive Grep**: Search `/var/log` for the word `error` recursively with line numbers.
2. **File Size Hunt**: Use `find` to locate files larger than 50MB in `/var/log`, redirect results to `large_logs.txt`.
3. **Pipeline Sorting**: Run `ps aux`, pipe to `grep root`, then pipe to `sort` by memory usage.

### 💡 SRE-Level Exercises

1. **Multi-Service Log Analysis**: Combine `grep` and pipes to extract error lines from multiple logs (e.g., `app.log`, `db.log`), storing them in `all_errors.log`.
2. **Disk Cleanup Script**: Use `find` with `-exec` or `xargs` to compress or remove logs older than 7 days in `/var/log`.
3. **Redirect for Debugging**: Run a custom script and send stdout/stderr to separate files. Investigate differences in normal output vs. error output.

---

## 📝 Quiz Questions

### 🔍 Beginner

1. **Which flag in `grep` makes the search case-insensitive?**
2. **What is the purpose of `>` in a command?**
3. **What command finds `.conf` files in `/etc`?** (Fill in: `find /etc ____ "*.conf"`)

### 🧩 Intermediate

4. **How do you show line numbers with `grep`?** (Which option?)
5. **Which `find` option locates files over 100MB in size?** (Fill in: `find /var/log ____ +100M`)
6. **What does the `|` operator do in `ls | grep script`?**

### 💡 SRE-Level

7. **Which operator redirects both stdout and stderr to the same file?**
8. **In `cmd1 | cmd2 | cmd3`, which command receives the output of `cmd2`?**
9. **Why might using `grep -r /` be risky on a production system?**

*(Instructor key with explanations is provided separately.)*

---

## 🚧 Troubleshooting

1. **High CPU Usage with `grep`**
   - **Symptom**: System load spikes during `grep -r /var/log`.
   - **Cause**: Large log files or insufficient search filters.
   - **Diagnostic**: Check file sizes, possibly search subdirectories.
   - **Resolution**: Narrow the path or use more specific patterns.
   - **Prevention**: Implement log rotation, store older logs compressed.

2. **Accidental Overwrite of Critical File**
   - **Symptom**: Using `>` destroyed previous file content.
   - **Cause**: Confusion between `>` and `>>`.
   - **Diagnostic**: Check timestamps, compare backups.
   - **Resolution**: Restore from backup.
   - **Prevention**: Always confirm you want to overwrite. Use `>>` if appending.

3. **Command Not Found in `-exec`**
   - **Symptom**: `-exec rm {} ; not found` or similar errors.
   - **Cause**: Missing backslash before `;` or spacing error.
   - **Diagnostic**: Review exact syntax: `-exec command {} \;`.
   - **Resolution**: Correct the syntax.
   - **Prevention**: Test with `-exec echo` before destructive operations.

---

## ❓ FAQ

### 🔍 Beginner

1. **Can I use `grep` on multiple files at once?**
   Yes, list them: `grep "pattern" file1.txt file2.txt`.

2. **How do I stop a long-running `grep` or `find` command?**
   Press `Ctrl + C`.

3. **Is `>` the same as copy-and-paste into a file?**
   It’s similar for text, but `>` overwrites the file automatically.

### 🧩 Intermediate

1. **How can I use a pattern file with `grep`?**
   Use `-f patternfile.txt`, where each line in the file is a pattern.

2. **Does `find` search inside file contents?**
   By default, `find` checks file **names** and metadata, not contents. Combine with `-exec grep` to search within files.

3. **What happens if I use both `>` and `>>` in the same command?**
   The last operator takes precedence, but mixing them is typically confusing and should be avoided.

### 💡 SRE-Level

1. **How do I avoid scanning special or remote filesystems with `find`?**
   Use `-xdev` to skip other mount points, or `-prune` to exclude directories.

2. **How do I handle failures in a pipeline?**
   In Bash, use `set -o pipefail`, which fails the pipeline if any command fails.

3. **Is there a safe way to mass-delete files using `find -exec`?**
   Yes, try `-exec echo rm {} \;` first to ensure correctness, then remove `echo` once confirmed.

---

## 🔥 SRE Scenario: Investigating a Sudden Log Surge

**Situation**: An alert indicates `/var/log` is filling up rapidly on `web-prod`. Disk usage is at 90%.

1. **Identify large logs**:

   ```bash
   find /var/log/nginx -type f -size +100M -exec ls -lh {} \;
   ```

   *Reasoning*: Pinpoint the biggest files to see which logs are ballooning.

2. **Check for Error Patterns**:

   ```bash
   grep -i "error" /var/log/nginx/access.log | tail -n 50
   ```

   *Reasoning*: Determine if repeated errors spike log size.

3. **Correlate with System Load**:

   ```bash
   ps aux | sort -rnk 3 | head -5
   ```

   *Reasoning*: See if any process is hogging CPU or causing abnormal log generation.

4. **Redirect Key Outputs**:

   ```bash
   df -h > /tmp/disk_usage_snapshot.txt
   ```

   *Reasoning*: Capture disk usage info for your incident report.

5. **Narrow Down Suspicious IPs**:

   ```bash
   grep -oE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" /var/log/nginx/access.log \
     | sort | uniq -c | sort -rn | head
   ```

   *Reasoning*: Identify potential attackers or heavy traffic sources.

6. **Mitigate**:

   ```bash
   find /var/log/nginx -type f -mtime +2 -exec gzip {} \;
   ```

   *Reasoning*: Compress older logs to free space while retaining data.

7. **Monitor**:

   ```bash
   tail -f /var/log/nginx/access.log | grep --color=always "error"
   ```

   *Reasoning*: Watch real-time logs for ongoing errors.

*Connection to SRE Principles*: Rapid, data-driven triage, proactive resource management, and a methodical approach to root cause analysis.

---

## 🧠 Key Takeaways

1. **Command Summary**:
   - `grep`: Filters text using patterns.
   - `find`: Locates files by name, size, date, and more.
   - Pipes (`|`): Chains commands for powerful processing.
   - Redirection (`>`, `>>`, `<`): Manages command I/O.

2. **Operational Insights**:
   - Always refine searches to avoid heavy resource use.
   - Logs often contain sensitive info; handle with care.
   - Combining commands speeds up debugging.

3. **Best Practices**:
   - Test destructive commands (like `-exec rm`) with small samples or `echo` first.
   - Avoid scanning the entire filesystem when searching.
   - Separate stderr/stdout to improve troubleshooting.

4. **Preview of Next Topic**:
   - We’ll learn about **`sed`** and **`awk`** for advanced text manipulation and data transformations.

---

## 📚 Further Learning Resources

### 🔍 Beginner

1. **[Grep Tutorial (Linuxize)](https://linuxize.com/post/grep-command/)** - A thorough introduction to grep.
2. **[Find Command Basics (GeeksforGeeks)](https://www.geeksforgeeks.org/find-command-in-linux-with-examples/)** - Simple find usage examples.
3. **[Redirection & Pipes (Ryan’s Tutorials)](https://ryanstutorials.net/linuxtutorial/piping.php)** - Visual guide to I/O redirection.

### 🧩 Intermediate

1. **[GNU grep Manual](https://www.gnu.org/software/grep/manual/grep.html)** - In-depth explanations of regex and performance considerations.
2. **[Advanced Find Tricks (Linode Docs)](https://www.linode.com/docs/guides/find-command/)** - Detailed usage of `find`, including `-exec`.
3. **[Bash Pipelines in Practice (DigitalOcean)](https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection)** - Chaining and advanced redirection.

### 💡 SRE-Level

1. **[Google SRE Workbook - Alerting & Monitoring](https://sre.google/workbook/alerting-on-sli/)** - Integrates text processing with observability.
2. **[Log Searching Strategies (Datadog)](https://www.datadoghq.com/blog/log-analysis-monitoring/)** - Large-scale log correlation.
3. **[Brendan Gregg’s Blog](http://www.brendangregg.com/)** - Performance tuning and pipeline optimization for production.

---

**Congratulations!** You’ve completed Day 4 of Linux SRE Training, covering essential text processing and searching commands. Next time, we’ll tackle **`sed`** and **`awk`** for even more powerful manipulations.
