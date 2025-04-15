# **Day 5: Comprehensive Linux SRE Training – Advanced Text Manipulation**

## 📌 Introduction

Welcome to Day 5 of our Linux SRE training series! Building on the foundational skills (Day 1–4) in command-line navigation, file manipulation, searching, and scripting, we now explore five crucial tools that give you powerful capabilities for text/data manipulation: **sed**, **awk**, **sort**, **uniq**, and **wc**. We will also delve deeper into complex pipes and pipelines, connecting everything to real-world SRE scenarios.

### Objectives Per Tier

**Beginner Tier** (3 Objectives)

1. Understand the basic purpose of sed, awk, sort, uniq, and wc.
2. Perform simple text substitutions and line/word counts.
3. Gain confidence building basic command pipelines.

**Intermediate Tier** (3 Objectives)

1. Use sed and awk to transform and extract structured data.
2. Apply sort and uniq to handle and manage large datasets.
3. Develop multi-step pipelines integrating multiple commands.

**SRE-Level Tier** (3 Objectives)

1. Automate complex text processing tasks at scale (e.g., large log files).
2. Troubleshoot performance and reliability issues using advanced piping.
3. Integrate security and performance considerations into text-based workflows.

### Connection to Previous and Future Learning

- **Previously**: You learned how to navigate directories, manage files, use redirection/pipes, and search text with grep/find.
- **Today**: We advance those skills to handle more intricate data processing tasks using powerful text manipulation commands.
- **Next**: We will move into process management, system monitoring, and strategies for maintaining reliability in real-time—essential for SRE.

---

## 📚 Core Concepts

Below are the concepts we’ll cover, each growing from a beginner-friendly analogy to an SRE-level perspective, including system impact.

1. **sed** (Stream Editor)
   - **Beginner Analogy**: A "find and replace" function for text.
   - **Technical Explanation**: Parses text line-by-line, applying editing rules.
   - **SRE Application**: Quickly modify config files or logs in place.
   - **System Impact**: Light CPU overhead, minimal memory usage, potential risk if used carelessly on critical configs.

2. **awk** (Aho, Weinberger, Kernighan)
   - **Beginner Analogy**: A "spreadsheet" tool for columns of data in plain text.
   - **Technical Explanation**: Pattern scanning and data extraction by fields.
   - **SRE Application**: Summarize logs, generate reports, parse large data sets.
   - **System Impact**: CPU usage proportional to file size; handles large streams well.

3. **sort**
   - **Beginner Analogy**: Alphabetizing or ordering lines, like sorting a list.
   - **Technical Explanation**: Orders lines based on alphanumeric, numeric, or custom rules.
   - **SRE Application**: Organize logs, arrange data for deduplication or merging.
   - **System Impact**: Requires disk/CPU for large sorts; sorting very large files can be resource-intensive.

4. **uniq**
   - **Beginner Analogy**: Erases duplicate rows in a sorted list.
   - **Technical Explanation**: Filters out adjacent duplicate lines.
   - **SRE Application**: Consolidate repeated events/log entries, produce unique sets.
   - **System Impact**: Typically lightweight; depends on sorted input.

5. **wc** (Word Count)
   - **Beginner Analogy**: A quick word/line/character counter.
   - **Technical Explanation**: Tallies lines, words, bytes in a file/stream.
   - **SRE Application**: Check log size trends, line counts for quick data checks.
   - **System Impact**: Minimal CPU usage.

6. **Complex Pipes and Pipelines**
   - **Beginner Analogy**: Linking tools like puzzle pieces to do more advanced tasks in a single flow.
   - **Technical Explanation**: Data from one command seamlessly feeds into the next.
   - **SRE Application**: Automate multi-step transformations, real-time log processing.
   - **System Impact**: Involves CPU overhead; carefully chain commands to avoid unnecessary complexity.

---

## 💻 Command Breakdown

### **Command: sed (Stream Editor)**

**Command Overview:**
A non-interactive text editor that reads input line-by-line, applying editing commands (substitution, deletion, insertion). In SRE contexts, sed is handy for bulk or automated config changes, quickly normalizing logs, or hot-patching text data.

**Syntax & Flags:**

| Flag/Option | Syntax Example                     | Description                                                 | SRE Usage Context                                           |
|-------------|------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| `-i`        | `sed -i 's/foo/bar/g' file.txt`    | Edits file in place without creating a new file             | Auto-updates config files, caution with backups             |
| `-n`        | `sed -n '/error/p' file.log`       | Suppress default output, print only matching lines          | Extract relevant logs or lines for analysis                 |
| `-e`        | `sed -e 's/foo/bar/' -e 's/baz/qux/' file.txt` | Combine multiple editing expressions              | Chain multiple transformations in one pass                 |
| `-r` or `-E`| `sed -r 's/(err[0-9]+)/[\1]/g' file.txt`| Enables extended regex support                      | Clean up structured logs with complex patterns             |

**Tiered Examples:**

- 🔍 **Beginner Example:**

  ```bash
  # Replace 'hello' with 'Hello' in greetings.txt
  $ sed 's/hello/Hello/g' greetings.txt
  # Output: each occurrence of "hello" is replaced.
  ```

- 🧩 **Intermediate Example:**

  ```bash
  # Remove all lines that start with # (treat as comments) in config.ini
  $ sed '/^#/d' config.ini
  # Explanation: This helps produce a "cleaned" config without comments.
  ```

- 💡 **SRE-Level Example:**

  ```bash
  # Update multiple environment variables in a config file, in place
  $ sed -i -e 's/APP_MODE=dev/APP_MODE=prod/' -e 's/DEBUG=true/DEBUG=false/' /etc/myapp.env
  # SRE context: Rolling out production changes quickly while controlling config drift.
  ```

**Instructional Notes:**

- 🧠 **Beginner Tip:** Always test sed commands on a backup file or with output redirection.
- 🧠 **Beginner Tip:** Use `s/pattern/replacement/g` for global replacements, or omit `g` for the first occurrence in each line.
- 🔧 **SRE Insight:** Combining `-i` with version control or backups is crucial—otherwise, you risk losing the original file.
- 🔧 **SRE Insight:** Use advanced regex to filter logs or sanitize sensitive data (e.g., removing tokens/passwords).
- ⚠️ **Common Pitfall:** Forgetting that sed applies changes line-by-line, sometimes ignoring multi-line context.
- ⚠️ **Common Pitfall:** Mistyping or misusing patterns can result in partial or no replacements.
- 🚨 **Security Note:** Editing config files in place might expose them to partial writes if the system crashes mid-edit.
- 💡 **Performance Impact:** Typically fast, but large-scale replacements on gigabyte-sized logs can be CPU-intensive.

---

### **Command: awk (Text Field Processor)**

**Command Overview:**
awk is a powerful pattern scanning and processing tool. It reads each line, splits it into fields, and allows flexible conditions and actions for each line. SREs use awk to parse logs, generate metrics, and transform data on the fly.

**Syntax & Flags:**

| Flag/Option | Syntax Example                                     | Description                                                                     | SRE Usage Context                                       |
|-------------|----------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------|
| `-F`        | `awk -F":" '{print $1,$3}' /etc/passwd`          | Sets the field separator                                                        | Extract fields from colon-separated data (e.g., passwd) |
| `-v`        | `awk -v thresh=100 '{if($3>thresh) print $1}' file`| Pass external variables into the awk script                                     | Fine-tune thresholds in log analysis                    |
| `BEGIN`     | `awk 'BEGIN {print "Start"} {print} END {print "End"}' file`| Runs code before reading lines                                         | Initialize counters or print headers                    |
| `END`       | See above                                         | Runs code after reading all lines                                              | Summarize or finalize metrics                           |

**Tiered Examples:**

- 🔍 **Beginner Example:**

  ```bash
  # Print the first field of each line in names.txt
  $ awk '{print $1}' names.txt
  # Explanation: Great for quick column extraction.
  ```

- 🧩 **Intermediate Example:**

  ```bash
  # Display processes using more than 10% CPU
  $ ps aux | awk '$3 > 10 {print $2, $3, $11}'
  # Explanation: Filters columns: PID, CPU%, COMMAND.
  ```

- 💡 **SRE-Level Example:**

  ```bash
  # Calculate average response time from a log's 7th field, ignoring lines with 'N/A'
  $ awk '$7 != "N/A" {sum+=$7; count++} END {print "Avg Response:", sum/count, "ms"}' access.log
  # SRE context: Summarizing performance metrics from large volumes of logs.
  ```

**Instructional Notes:**

- 🧠 **Beginner Tip:** By default, awk splits fields on whitespace; use `-F` to handle CSV or other delimiters.
- 🧠 **Beginner Tip:** `$0` references the entire line, `$1` is the first field, `$NF` is the last field.
- 🔧 **SRE Insight:** Combine with grep or sed for advanced searching or pre-filtering.
- 🔧 **SRE Insight:** Use `BEGIN`/`END` blocks for initialization and summary, especially in performance metrics.
- ⚠️ **Common Pitfall:** Overlooking that numeric comparisons require fields to be numeric (strings can produce unexpected results).
- ⚠️ **Common Pitfall:** Not quoting field separators properly, especially with complex delimiters.
- 🚨 **Security Note:** Be mindful if your data contains sensitive info—filter or mask it.
- 💡 **Performance Impact:** Usually efficient; heavily used in command pipelines for large log files.

---

### **Command: sort**

**Command Overview:**
sort rearranges lines in a file or stream based on alphabetical, numerical, or custom-defined order. SREs use sort to organize logs, data sets, or produce sorted input for uniq.

**Syntax & Flags:**

| Flag/Option | Syntax Example                   | Description                                                                             | SRE Usage Context                              |
|-------------|----------------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------|
| `-n`        | `sort -n file.txt`               | Sort lines numerically (1,2,10) instead of lexicographically (1,10,2)                   | Sorting numeric logs, user IDs, memory usage    |
| `-r`        | `sort -r file.txt`               | Reverse the sort order                                                                  | Quick descending order for largest to smallest  |
| `-k`        | `sort -k2 file.txt`              | Sort based on a specific field (2nd field in this case)                                 | Sorting by CPU usage or specific log columns    |
| `-t`        | `sort -t',' -k3 file.csv`        | Use a custom delimiter (comma)                                                          | CSV-based sorting for metrics or config data    |
| `-u`        | `sort -u file.txt`               | Remove duplicates while sorting                                                         | Combine with uniq tasks, though not identical   |

**Tiered Examples:**

- 🔍 **Beginner Example:**

  ```bash
  # Sort lines in names.txt alphabetically
  $ sort names.txt
  # Output: Lines sorted A to Z.
  ```

- 🧩 **Intermediate Example:**

  ```bash
  # Sort processes by memory usage (4th column from ps aux) descending
  $ ps aux | sort -k4 -nr | head -5
  # Explanation: Identifies top memory-consuming processes.
  ```

- 💡 **SRE-Level Example:**

  ```bash
  # Sort log lines by timestamp (3rd field), then by response time (7th field)
  $ sort -k3,3 -k7,7n server.log
  # SRE context: Triage logs chronologically, then sort by performance metrics.
  ```

**Instructional Notes:**

- 🧠 **Beginner Tip:** By default, sort uses ASCII order, leading to unexpected ordering of numbers. Use `-n` for numeric.
- 🧠 **Beginner Tip:** Combine with `head` or `tail` to quickly see highest/lowest sorted entries.
- 🔧 **SRE Insight:** Sorting large files can be expensive in memory/disk I/O, consider streaming or partial-sorts.
- 🔧 **SRE Insight:** The `-k` option is especially powerful for multi-column logs.
- ⚠️ **Common Pitfall:** Not specifying the correct field range in `-k` can lead to incomplete sorts.
- ⚠️ **Common Pitfall:** Using `-u` incorrectly, expecting it to behave like uniq. They differ in how duplicates are handled.
- 🚨 **Security Note:** Sorting sensitive data can lead to inadvertently exposing patterns; handle carefully.
- 💡 **Performance Impact:** Large sorts can thrash disk/CPU—monitor usage when sorting big logs.

---

### **Command: uniq**

**Command Overview:**
uniq filters or reports duplicate lines, typically used after sort. SREs often rely on uniq to condense repeated log messages or event lines for quick overviews.

**Syntax & Flags:**

| Flag/Option | Syntax Example               | Description                                            | SRE Usage Context                                          |
|-------------|------------------------------|--------------------------------------------------------|------------------------------------------------------------|
| `-c`        | `sort file.txt | uniq -c`   | Prefix lines by the number of occurrences              | Quick frequency analysis on sorted data                    |
| `-d`        | `sort file.txt | uniq -d`   | Print only duplicate lines                             | Identify repeated lines (e.g., repeated errors)            |
| `-u`        | `sort file.txt | uniq -u`   | Print only unique lines                                | Filter out duplicates entirely                             |

**Tiered Examples:**

- 🔍 **Beginner Example:**

  ```bash
  # Remove duplicate lines from colors.txt (after sorting it)
  $ sort colors.txt | uniq
  # Output: Single instance of each color.
  ```

- 🧩 **Intermediate Example:**

  ```bash
  # Show how many times each error string appears in the logs
  $ grep "ERROR" system.log | sort | uniq -c
  # Explanation: Combines search, sort, and count for quick error frequency.
  ```

- 💡 **SRE-Level Example:**

  ```bash
  # Identify recurring IP addresses across multiple logs, focusing on duplicates
  $ cat /var/log/app1/access.log /var/log/app2/access.log | awk '{print $1}' | sort | uniq -d
  # SRE context: Cross-service correlation to find suspicious or repeated client IPs.
  ```

**Instructional Notes:**

- 🧠 **Beginner Tip:** uniq checks only adjacent lines, so always sort first.
- 🧠 **Beginner Tip:** Use `uniq > newfile` or pipe the output to avoid overwriting unsorted data.
- 🔧 **SRE Insight:** Combine with grep or awk to isolate relevant fields before deduplication.
- 🔧 **SRE Insight:** `uniq -c` is handy for quick histogramming of repeated lines.
- ⚠️ **Common Pitfall:** Forgetting to sort input leads to missed duplicates.
- ⚠️ **Common Pitfall:** Using `uniq -u` can remove lines that appear more than once—double-check your logic.
- 🚨 **Security Note:** When deduplicating logs, you might lose context of how often a sensitive event occurred.
- 💡 **Performance Impact:** Typically minimal overhead, reliant on sort for large data sets.

---

### **Command: wc (Word Count)**

**Command Overview:**
wc counts lines, words, and bytes in text. SREs can use wc to track log growth, measure data sets, or quickly confirm file sizes.

**Syntax & Flags:**

| Flag/Option | Syntax Example     | Description                        | SRE Usage Context                                   |
|-------------|--------------------|------------------------------------|-----------------------------------------------------|
| `-l`        | `wc -l file.txt`  | Prints the number of lines         | Checking line counts in logs or config files        |
| `-w`        | `wc -w file.txt`  | Prints the number of words         | Textual data analysis                               |
| `-c`        | `wc -c file.txt`  | Prints the number of bytes         | Quick file size check in bytes                      |

**Tiered Examples:**

- 🔍 **Beginner Example:**

  ```bash
  # Count lines in greetings.txt
  $ wc -l greetings.txt
  # Output: e.g., 25 greetings.txt
  ```

- 🧩 **Intermediate Example:**

  ```bash
  # Check total bytes of a log, then compress if too large
  $ size=$(wc -c < application.log)
  $ if [ "$size" -gt 500000 ]; then gzip application.log; fi
  # Explanation: Automated housekeeping.
  ```

- 💡 **SRE-Level Example:**

  ```bash
  # Monitor real-time log growth: lines processed per minute
  $ while true; do wc -l /var/log/service.log; sleep 60; done
  # SRE context: Watch load patterns or detect unusual surge in logs.
  ```

**Instructional Notes:**

- 🧠 **Beginner Tip:** `wc file.txt` alone shows lines, words, and bytes in that order.
- 🧠 **Beginner Tip:** Pipe data into wc to measure streams (e.g., `ls | wc -l`).
- 🔧 **SRE Insight:** Great for trending log growth and validating data ingestion.
- 🔧 **SRE Insight:** Use in scripts to set thresholds for log rotation or archiving.
- ⚠️ **Common Pitfall:** Confusing bytes vs. characters, especially with multi-byte encodings.
- ⚠️ **Common Pitfall:** If you’re using `< file`, you only see the numeric output without the filename.
- 🚨 **Security Note:** Counting lines or bytes might reveal patterns about user activity—avoid overexposure.
- 💡 **Performance Impact:** Very fast for typical usage.

---

## 🛠️ System Effects

When using these commands, keep in mind:

1. **Filesystem & Metadata**: `sed -i` modifies files in place, which can change file timestamps and risk partial updates.
2. **System Resources**: Large data sets can tax CPU/disk. `sort` especially can use considerable RAM for big files.
3. **Security Implications**: Text transformations might inadvertently expose or remove sensitive info; handle logs carefully.
4. **Monitoring Visibility**: Tools that process data streams help you create real-time dashboards or metrics, but can also obscure original data if not logged properly.

---

## 🎯 Hands-On Exercises

Below are three exercises per tier, guiding you through progressive skill-building.

### Beginner Tier (3 Exercises)

1. **Simple sed Substitution**
   - Create a file `mytext.txt` with the line `hello world`. Replace `hello` with `Hello` using sed and display the output.
   - Verify the change in your terminal without editing the file in place.
2. **Basic awk Field Extraction**
   - Use `echo "apple banana cherry" | awk '{print $2}'` to display only `banana`.
   - Experiment with printing `$1` and `$3`.
3. **Line Counting**
   - Download a small text file (e.g., a sample log) and run `wc -l` to see how many lines it contains.

### Intermediate Tier (3 Exercises)

1. **Filtering Config Files**
   - Create a `config.ini` with commented lines (#). Use sed to remove comment lines and pipe the result into `wc -l` to see how many active lines remain.
2. **Sorting Log Entries by Severity**
   - Make a small mock log with lines containing `INFO`, `WARN`, `ERROR` in random order. Sort them alphabetically (`sort`) and count duplicates (`uniq -c`) to see how many of each severity level you have.
3. **Aggregating with awk**
   - Generate a CSV file with columns: `name,score`. Use awk with `-F','` to calculate the average score.

### SRE-Level Tier (3 Exercises)

1. **Real-Time Log Monitoring**
   - Tail a growing log file (e.g., `tail -f /var/log/syslog`), pipe through grep to highlight a keyword (like `error`), and use awk to print the timestamp/field to keep track in real time.
2. **Complex Pipeline for Large Data**
   - If you have a sizable log (e.g., 50MB+), run a pipeline that: filters by a pattern (grep), sorts by a field, finds duplicates (uniq -c), and extracts the top 10 (sort -nr | head -10). Summarize what you discover.
3. **Automated Bulk Config Edits**
   - Suppose you have multiple `.conf` files that specify `timeout=30`. Use a for-loop and sed to replace `timeout=30` with `timeout=60` across all config files. Confirm changes with grep.

---

## 📝 Quiz Questions

### Beginner Tier (4 Questions)

1. **sed Substitution**: Which sed command replaces all instances of `apple` with `Apple` in `fruits.txt`?
2. **awk Fields**: In `awk '{print $3}'`, which part of the line are we extracting?
3. **sort Default Behavior**: By default, does `sort` order data numerically or lexicographically?
4. **wc -l**: If a file has 100 lines, what numeric output does `wc -l filename` provide?

### Intermediate Tier (4 Questions)

1. **Removing Comments**: How can you remove lines starting with `#` in a config file using sed?
2. **Combining sort & uniq**: Why do we typically run `sort` before `uniq`?
3. **Filtering with awk**: What does `awk '$2 > 50 {print $0}' file.txt` do?
4. **Memory Usage**: Why might `sort -nr largefile.log` consume a lot of resources?

### SRE-Level Tier (4 Questions)

1. **In-Place Editing**: What risk does `sed -i` present when used on critical config files?
2. **Regex Complexity**: How could advanced regex in sed or awk help parse multiline data?
3. **Advanced Pipelines**: Provide one advantage of chaining grep → awk → sort → uniq → wc in a single pipeline.
4. **Performance Monitoring**: How would you use `wc` in a script to detect an abnormally large log growth event?

---

## 🚧 Troubleshooting Scenarios

Below are three realistic scenarios you may encounter:

1. **Scenario**: `sed` Substitution Not Working
   - **Symptom**: You run `sed 's/Error/ERROR/' file.log` but see no change in output.
   - **Likely Cause**: The term in file.log might be `ERROR:` or `Error` with different casing.
   - **Resolution Steps**:
     1. Inspect the file with `grep` to confirm the exact text.
     2. Adjust your pattern: `sed 's/[Ee]rror/ERROR/' file.log`.
   - **Prevention**: Always check case variations or use the `i` (case-insensitive) flag if needed.

2. **Scenario**: `uniq` Doesn’t Remove Duplicates
   - **Symptom**: Running `uniq -d data.txt` yields no duplicates, but you know there are repeated lines.
   - **Likely Cause**: The file wasn’t sorted first, so duplicates aren’t adjacent.
   - **Resolution Steps**:
     1. Sort the file with `sort data.txt > sorted_data.txt`.
     2. Rerun `uniq -d sorted_data.txt`.
   - **Prevention**: Always apply `sort` prior to `uniq` for accurate deduplication.

3. **Scenario**: High CPU Usage When Sorting Logs
   - **Symptom**: Sorting a multi-gigabyte log causes high CPU and system sluggishness.
   - **Likely Cause**: `sort` attempts to load large data sets and create massive temporary files.
   - **Resolution Steps**:
     1. Use partial or streaming strategies: `sort --compress-program=gzip` or `sort -S` to limit memory usage.
     2. Split logs into chunks, sort individually, then merge.
   - **Prevention**: Monitor resource usage; consider more efficient or distributed approaches for extremely large data.

---

## ❓ FAQ (3 per Tier)

### Beginner Tier FAQ

1. **How do I store sed output in a new file instead of printing?**
   - **Answer**: Use redirection: `sed 's/old/new/g' input.txt > output.txt`.
2. **Can awk handle CSV files?**
   - **Answer**: Yes, with `-F','` you set the comma as the delimiter.
3. **Why is `sort` mixing numbers like 2 and 10?**
   - **Answer**: Without `-n`, `sort` does alphabetical ordering, so `10` comes before `2` lexicographically.

### Intermediate Tier FAQ

1. **Can sed remove more than one pattern?**
   - **Answer**: Yes, with `-e`: `sed -e 's/foo/bar/' -e 's/baz/qux/' file.txt`.
2. **Why is `awk '{print $4}'` not printing the correct field in my log?**
   - **Answer**: Possibly different whitespace or a different delimiter. Use `-F` or examine the log format carefully.
3. **What if I want to do case-insensitive sorts?**
   - **Answer**: Use `sort -f`, which folds uppercase and lowercase together for sorting.

### SRE-Level Tier FAQ

1. **How can I handle multi-line logs with sed or awk?**
   - **Answer**: You can use `sed -n 'H;…'` techniques for multi-line or advanced `awk` RS (record separator) usage.
2. **When do I choose awk over a scripting language like Python?**
   - **Answer**: For quick, in-stream transformations or filtering tasks, awk is faster to implement. For complex logic or multi-file operations, Python might be more maintainable.
3. **How to protect sensitive data while using text manipulation in pipelines?**
   - **Answer**: Mask fields using sed or awk (e.g., replace secrets with `****`) and ensure pipeline logs aren’t stored in insecure locations.

---

## 🔥 Detailed SRE Scenario

**Incident**: A critical web service is experiencing slow responses and sporadic 500 errors. We suspect an overloaded endpoint or DB latency.

**Steps with Explanation**:

1. **Check the Access Log for 500 Errors**

   ```bash
   grep " 500 " /var/log/nginx/access.log | wc -l
   ```

   - Rationale: See how many 500 errors occurred in the last hour.
2. **Identify the Heaviest-Hit Endpoints**

   ```bash
   awk '{print $7}' /var/log/nginx/access.log | sort | uniq -c | sort -nr | head -5
   ```

   - Rationale: Summarize which endpoints are receiving the most traffic.
3. **Filter for Slow Responses**

   ```bash
   awk '$NF > 1000 {print $0}' /var/log/nginx/access.log
   ```

   - Rationale: Focus on requests that took more than 1000ms.
4. **Correlate Errors with DB Logs**

   ```bash
   grep -i "error" /var/log/mysql/mysql.log
   ```

   - Rationale: Check if database side is throwing errors at the same times.
5. **Average Query Time**

   ```bash
   grep "Query" /var/log/mysql/mysql.log | sed 's/.*time=\([0-9]*\)ms.*/\1/' | awk '{sum+=$1; c++} END {print sum/c "ms"}
   ```

   - Rationale: Confirm if DB queries are generally slower, indicating possible performance bottleneck.
6. **Check High CPU or Memory Processes**

   ```bash
   ps aux | sort -k3 -nr | head -5
   ```

   - Rationale: Identify if any process is hogging CPU.
7. **Validate Config for Rate Limits**

   ```bash
   sed -n '/rate_limit/,/}/p' /etc/nginx/nginx.conf
   ```

   - Rationale: Inspect config blocks that might throttle or break traffic.

**Outcome**: By systematically investigating logs and resource usage with these text manipulation commands, you pinpoint the root cause—like an unoptimized query or misconfigured rate limit—and apply a fix to restore normal operation.

---

## 🧠 Key Takeaways

1. **Command Summary** (5 Items):
   - **sed**: Powerful stream editor for text substitution.
   - **awk**: Flexible field-based data extractor.
   - **sort**: Organizes lines in a chosen order.
   - **uniq**: De-duplicates sorted lines.
   - **wc**: Quick counts (lines, words, bytes).

2. **Operational Insights** (3 Items):
   1. For large-scale log analysis, chaining these commands is often more performant than manual or GUI-based approaches.
   2. Carefully controlling the order of commands (like sorting before uniq) ensures accurate data results.
   3. Always consider memory and CPU overhead for massive data sets—especially with sort or advanced regex operations.

3. **Best Practices** (3 Items):
   1. **Backup or test** before making in-place sed changes on critical files.
   2. Use **awk** for quick metric calculations or pattern-based filtering—particularly for logs.
   3. Combine **sort** and **uniq** to quickly detect repeated patterns or duplicates in logs.

4. **Preview of Next Topic**
   - Next, we’ll move into **process management and monitoring**. You’ll learn how to manage system processes (starting, stopping, diagnosing performance), gather system metrics, and respond to real-time issues—a natural extension of the text-based insights you gain today.

---

## 📚 Further Learning Resources

### 🔍 Beginner (2–3 resources)

1. **"GNU sed Manual" (Official)**
   - Link: [https://www.gnu.org/software/sed/manual/](https://www.gnu.org/software/sed/manual/)
   - Teaches basic sed usage and examples. Ideal for beginners wanting a deeper reference.
   - Applies to simple search-and-replace tasks and line filtering.
2. **"Awk Introduction" by Linuxize**
   - Link: [https://linuxize.com/post/awk-command/](https://linuxize.com/post/awk-command/)
   - Covers the basics of awk fields, syntax, and usage.
   - Helps beginners grasp fundamental pattern scanning and printing.
3. **"Learning Bash Scripting" (Beginner-Focused Tutorial)**
   - Link: [https://www.tutorialspoint.com/unix/bash_scripting.htm](https://www.tutorialspoint.com/unix/bash_scripting.htm)
   - Provides context on combining commands in scripts.
   - Strengthens understanding of how sed/awk integrate into simple pipelines.

### 🧩 Intermediate (2–3 resources)

1. **"The Linux Command Line" Book**
   - Link: [http://linuxcommand.org/tlcl.php](http://linuxcommand.org/tlcl.php)
   - Offers deeper insights into command-line operations, including advanced usage.
   - Connects well to operational skills for real-world tasks.
2. **"Mastering the awk Command" by DigitalOcean**
   - Link: [https://www.digitalocean.com/community/tutorials/how-to-use-the-awk-language-to-manipulate-text-in-linux](https://www.digitalocean.com/community/tutorials/how-to-use-the-awk-language-to-manipulate-text-in-linux)
   - Explores field manipulation, conditionals, and scripting with awk.
   - Ideal for operational automation and log parsing.
3. **"Grep, Sed, and Awk" (O’Reilly)**
   - Link: [https://www.oreilly.com/library/view/grep-sed-awk/9781449396677/](https://www.oreilly.com/library/view/grep-sed-awk/9781449396677/)
   - Discusses advanced usage patterns.
   - Connects multiple Unix text-processing tools.

### 💡 SRE-Level (2–3 resources)

1. **"Google SRE Book" (Chapter on Monitoring & Alerting)**
   - Link: [https://sre.google/sre-book/](https://sre.google/sre-book/)
   - High-level approach to reliability engineering.
   - Relates text processing to core SRE tasks of analyzing logs & data.
2. **"Linux Performance Analysis in 60,000 Milliseconds" by Netflix TechBlog**
   - Link: [https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-accc10403c55](https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-accc10403c55)
   - Examines performance analysis using standard Linux tools.
   - Showcases real-time pipeline usage for troubleshooting.
3. **"Advanced Sed and Awk" (IBM Developer Tutorials)**
   - Link: [https://developer.ibm.com/tutorials/l-sed1/](https://developer.ibm.com/tutorials/l-sed1/)
   - Focuses on complex stream editing and data transformations.
   - Perfect for large-scale, production-grade manipulations.
