# 🏆 **Day 5 Linux SRE Training – Advanced Text Processing Tools**

## 📌 Introduction

Welcome to **Day 5** of our Linux SRE training series! In this combined training resource, we synthesize the best elements from two previous training documents (V3 and V5) focusing on powerful text processing tools essential for SRE work. We will explore **sed**, **awk**, **sort**, **uniq**, and **wc** in detail, with tiered learning objectives (Beginner, Intermediate, and SRE-Level) and real-world examples.

### Connection to Previous and Future Learning

- **Previously**: We covered searching and filtering text with `grep` and `find`, plus working with pipes and redirection.
- **Today**: We delve deeper into advanced text processing, data transformation, and real-world SRE scenarios.
- **Next**: We will move on to process management, system monitoring, and reliability strategies.

---

## 🎯 Learning Objectives per Tier

### Beginner Tier (3 Objectives)

1. Understand the fundamental purposes of `sed`, `awk`, `sort`, `uniq`, and `wc`.
2. Perform basic text substitutions, counting (lines, words, characters), and simple field extractions.
3. Learn how to build and interpret basic command pipelines.

### Intermediate Tier (3 Objectives)

1. Use `sed` and `awk` for structured data transformations and selective extraction.
2. Apply `sort` and `uniq` to large data sets for organization and deduplication.
3. Develop multi-step pipelines that integrate multiple commands seamlessly.

### SRE-Level Tier (3 Objectives)

1. Automate large-scale text manipulation to handle extensive logs or configuration files.
2. Troubleshoot reliability and performance issues using advanced piping.
3. Integrate security, performance, and operational considerations into text processing workflows.

---

## 📚 Core Concepts

### Unix Philosophy and Text Streams

- **Text as a Universal Interface**: In Unix, text is the cornerstone of data manipulation. SREs regularly handle logs, config files, monitoring outputs, and more—most of which can be represented as text.
- **Stream Processing**: Tools like `sed` and `awk` process data line by line. This approach scales to large files and requires minimal system resources compared to loading entire files in memory.

**Beginner Insight**: Think of each tool as a specialized station on an assembly line—one tool searches and replaces, another filters columns, another sorts, etc.

**SRE Perspective**: By chaining these tools, you can build complex data transformation pipelines without heavy scripting. This is crucial for large-scale log analysis, on-the-fly transformations, and automated system checks.

---

## 💻 Command Breakdown

This training document follows a structured format that highlights each command's overview, common flags, tiered examples, and real-world SRE insights.

### 1. **sed (Stream Editor)**

**Command Overview**:

- `sed` reads text line by line and applies editing commands such as substitution, deletion, or insertion.
- Useful for quick transformations on logs, configuration files, or any stream of text.

**Syntax**: `sed [options] 'command' file`

| Flag/Option | Syntax Example                         | Description                                     | SRE Usage Context                                        |
|-------------|----------------------------------------|-------------------------------------------------|----------------------------------------------------------|
| `-i`        | `sed -i 's/foo/bar/g' file.txt`        | Edit files in place                                | Automating config changes, ensure backup or version ctrl |
| `-n`        | `sed -n '/error/p' file.log`           | Suppress default print, only print matches        | Selective line extraction                                |
| `-e`        | `sed -e 's/foo/bar/' -e 's/baz/qux/'`  | Combine multiple commands                          | Batch transformations in one pass                        |
| `-E` or `-r`| `sed -E 's/(foo[0-9]+)/[\1]/' file.txt` | Extended regex syntax for more complex patterns   | More sophisticated log rewrites                          |

#### Tiered Examples

- **🟢 Beginner**

  ```bash
  # Replace 'hello' with 'Hello' in greetings.txt
  sed 's/hello/Hello/g' greetings.txt
  ```
  
- **🟡 Intermediate**

  ```bash
  # Delete lines starting with a comment in config files
  sed '/^#/d' /etc/myapp/config.ini
  ```

- **🔴 SRE-Level**

  ```bash
  # Replace multiple environment variables in place
  sed -i -e 's/APP_MODE=dev/APP_MODE=prod/' -e 's/DEBUG=true/DEBUG=false/' /etc/myapp.env
  ```

**Instructional Notes**

- **🧠 Beginner Tip**: Use `-n` alongside `p` to precisely control output. Test on a backup file before using `-i`.
- **🔧 SRE Insight**: Combine `sed` with version control or backups to avoid irreversible changes.
- **⚠️ Common Pitfall**: By default, `sed` is line-based; multi-line patterns require advanced techniques.
- **💡 Performance Impact**: Typically fast, but repeated global substitutions on large files can be CPU-intensive.

---

### 2. **awk (Pattern Scanning and Processing)**

**Command Overview**:

- `awk` splits each line into fields, letting you apply patterns or calculations.
- Ideal for extracting columns, computing statistics, and generating quick reports.

**Syntax**: `awk [options] 'pattern { action }' file`

| Flag/Option | Example                                      | Description                                                                      | SRE Usage Context                                  |
|-------------|----------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------|
| `-F`        | `awk -F, '{print $1, $3}' file.csv`          | Sets the field separator (comma, tab, etc.)                                       | Processing CSV logs, multi-column data             |
| `-v`        | `awk -v threshold=100 '{ if($4 > threshold) ... }' file`| Passes a shell variable into `awk`                                           | Dynamic thresholds for performance checks          |
| `BEGIN/END` | `awk 'BEGIN{...} { main } END{...}' file`    | Blocks that run before/after main processing                                     | Summaries, initialization, final reporting         |

#### Tiered Examples

- **🟢 Beginner**

  ```bash
  # Print the first column of each line
  awk '{print $1}' names.txt
  ```

- **🟡 Intermediate**

  ```bash
  # Show processes using more than 10% CPU (fields vary by OS)
  ps aux | awk '$3 > 10 {print $2, $3, $11}'
  ```

- **🔴 SRE-Level**

  ```bash
  # Calculate average response time ignoring N/A lines
  awk '$7 != "N/A" { sum+=$7; count++ } END { print "Avg:", sum/count, "ms" }' access.log
  ```

**Instructional Notes**

- **🧠 Beginner Tip**: `$1` is the first field, `$0` is the entire line, and `NF` is the number of fields.
- **🔧 SRE Insight**: Combine with `grep` or `sed` for advanced filtering or pre-processing.
- **⚠️ Common Pitfall**: Numeric vs. string comparisons can produce unexpected results.
- **💡 Performance Impact**: Efficient for on-the-fly analytics, even with large logs.

---

### 3. **sort**

**Command Overview**:

- `sort` arranges lines of text in ascending or descending order, with numeric or lexicographic sorting.
- SREs use `sort` to organize logs, resource usage outputs, or to prepare data for deduplication.

**Syntax**: `sort [options] file`

| Flag/Option | Example                    | Description                                                                 | SRE Usage Context                          |
|-------------|----------------------------|-----------------------------------------------------------------------------|--------------------------------------------|
| `-n`        | `sort -n file.txt`        | Numeric sort instead of ASCII lexicographic                                 | Sorting numeric IDs, memory usage, etc.     |
| `-r`        | `sort -r file.txt`        | Reverse the order (descending)                                              | Quickly see top resource usage entries     |
| `-k`        | `sort -k3 file.txt`       | Sort by a specific field (the 3rd field)                                    | Sorting logs by timestamp or response time |
| `-t`        | `sort -t',' -k2 file.csv` | Specify a custom delimiter (comma, tab, etc.)                               | Sorting CSV data sets                      |
| `-u`        | `sort -u file.txt`        | Remove duplicate lines while sorting                                        | Combine with deduplication tasks           |

#### Tiered Examples

- **🟢 Beginner**

  ```bash
  # Alphabetically sort lines in names.txt
  sort names.txt
  ```

- **🟡 Intermediate**

  ```bash
  # Sort processes by memory usage descending
  ps aux | sort -k4 -nr | head -5
  ```

- **🔴 SRE-Level**

  ```bash
  # Sort log lines by timestamp (field 3), then by response time (field 7 numerically)
  sort -k3,3 -k7,7n server.log
  ```

**Instructional Notes**

- **🧠 Beginner Tip**: Use `-n` for numeric sorts, else "10" might come before "2".
- **🔧 SRE Insight**: For massive files, sorting can be CPU/IO heavy—monitor system resources.
- **⚠️ Common Pitfall**: Using `-u` vs. `uniq`. They differ in how duplicates are determined.
- **💡 Performance Impact**: Potentially high for large data sets (multi-gigabyte logs).

---

### 4. **uniq**

**Command Overview**:

- `uniq` filters out adjacent duplicate lines, typically used after `sort`.
- Great for summarizing repeated log messages or events.

**Syntax**: `uniq [options] [input [output]]`

| Flag/Option | Example                           | Description                          | SRE Usage Context                                        |
|-------------|-----------------------------------|--------------------------------------|----------------------------------------------------------|
| `-c`        | `sort file.txt \| uniq -c`       | Prefix lines with number of repeats  | Frequency analysis of repeated errors or events          |
| `-d`        | `sort file.txt \| uniq -d`       | Print only duplicated lines          | Quickly isolate repeated issues in logs                  |
| `-u`        | `sort file.txt \| uniq -u`       | Print only unique lines             | Exclude any lines that appear more than once             |

#### Tiered Examples

- **🟢 Beginner**

  ```bash
  # Remove duplicates from a sorted list
  sort names.txt | uniq
  ```

- **🟡 Intermediate**

  ```bash
  # Count occurrences of each severity level in logs
  grep "ERROR\|WARN\|INFO" app.log | sort | uniq -c
  ```

- **🔴 SRE-Level**

  ```bash
  # Identify repeating IP addresses across combined logs
  cat /var/log/app1/access.log /var/log/app2/access.log | \
    awk '{print $1}' | sort | uniq -d
  ```

**Instructional Notes**

- **🧠 Beginner Tip**: Always `sort` before `uniq` so duplicates appear adjacently.
- **🔧 SRE Insight**: Combine `uniq -c` with `sort -nr` to get frequency-based ranking.
- **⚠️ Common Pitfall**: Not sorting first leads to missed duplicates.

---

### 5. **wc (Word Count)**

**Command Overview**:

- `wc` shows line, word, and byte counts for files or piped streams.
- Useful in quick data checks, log sizing, or verifying file length.

**Syntax**: `wc [options] [file...]`

| Flag/Option | Example       | Description                                      | SRE Usage Context                 |
|-------------|---------------|--------------------------------------------------|-----------------------------------|
| `-l`        | `wc -l file`  | Count lines                                     | Basic log or config file checks   |
| `-w`        | `wc -w file`  | Count words                                     | Counting tokens in textual data   |
| `-c`        | `wc -c file`  | Count bytes                                     | Checking file sizes in bytes      |

#### Tiered Examples

- **🟢 Beginner**

  ```bash
  # Count lines in greetings.txt
  wc -l greetings.txt
  ```

- **🟡 Intermediate**

  ```bash
  # Check file size in a script, then compress if over 500KB
  size=$(wc -c < application.log)
  if [ "$size" -gt 500000 ]; then
    gzip application.log
  fi
  ```

- **🔴 SRE-Level**

  ```bash
  # Monitor log growth in real time
  watch "wc -l /var/log/service.log"
  ```

**Instructional Notes**

- **🧠 Beginner Tip**: By default, `wc file.txt` outputs lines, words, and bytes.
- **🔧 SRE Insight**: Great for trending log growth; combine with `tail -f` or `watch`.
- **⚠️ Common Pitfall**: `wc -c` includes all bytes, so watch out for Unicode or multi-byte chars.

---

## 🛠️ System Effects

1. **Filesystem & Metadata**: Using `sed -i` modifies files in place, which can alter permissions or timestamps.
2. **System Resources**: `sort` and advanced regex usage can spike CPU and memory on large data sets.
3. **Security Considerations**: Sensitive info might be exposed or need sanitizing—be mindful when streaming logs.
4. **Monitoring Visibility**: Combining these commands can produce real-time dashboards or aggregated metrics.

---

## 🎯 Hands-On Exercises

### **Beginner Tier**

1. **Simple sed Substitution**: Create a file `mytext.txt` containing `hello world`. Use `sed 's/hello/Hello/g' mytext.txt` to display the updated text.
2. **Basic awk Extraction**: Run `echo "apple banana cherry" | awk '{print $2}'` to display only `banana`. Try `$1` and `$3` to see what changes.
3. **Line Counting**: Create or download a small text file. Use `wc -l filename.txt` to see how many lines it contains.

### **Intermediate Tier**

1. **Filtering Config Files**: Create a `config.ini` with commented lines (#). Use `sed '/^#/d' config.ini | wc -l` to see how many lines remain after removing comments.
2. **Sorting Log Severity**: Make a short mock log containing lines with `INFO`, `WARN`, `ERROR`. Sort them (e.g., `sort mock.log`) and pipe into `uniq -c` to see how many of each severity.
3. **Aggregating with awk**: Create a CSV `scores.csv` with `name,score`. Use `awk -F',' '{ sum+=$2; count++ } END { print "Average:", sum/count }' scores.csv` to compute the average.

### **SRE-Level Tier**

1. **Real-Time Log Monitoring**: Tail a live log (`tail -f /var/log/syslog`) and pipe it into `grep 'error' | awk '{print $0}'`. Observe new error lines in real time.
2. **Complex Pipeline on Large Data**: For a large log (`50MB+`), chain `grep`, `awk`, `sort`, `uniq -c`, and `head -10` to see the top repeated patterns.
3. **Automated Bulk Config Edits**: Suppose multiple `*.conf` files define `timeout=30`. Use a for-loop with `sed -i 's/timeout=30/timeout=60/' *.conf` and confirm changes with `grep timeout *.conf`.

---

## 📝 Quiz Questions

### **Beginner Level (4)**

1. How do you replace all instances of `apple` with `Apple` in `fruit.txt` using sed?
2. Which part of a line does `$3` represent in an awk command?
3. By default, does `sort` sort data numerically or lexicographically?
4. What does `wc -l logfile.txt` show?

### **Intermediate Level (4)**

1. How would you remove lines beginning with `#` in a file using sed?
2. Why is sorting usually necessary before using `uniq`?
3. What does `awk '$3 > 50 {print $0}' data.txt` do?
4. Why might running `sort -nr big.log` consume significant system resources?

### **SRE-Level (4)**

1. What is a key risk of using `sed -i` on production configuration files?
2. How can advanced regex in `sed` or `awk` help parse multiline or complex structured data?
3. Give one advantage of chaining `grep`, `awk`, `sort`, `uniq`, and `wc` in a single pipeline.
4. How might you use `wc` to detect abnormal log growth patterns?

---

## 🚧 Troubleshooting Scenarios

1. **sed Substitution Not Working**
   - **Symptom**: Running `sed 's/Error/ERROR/' file.log` shows no change.
   - **Likely Cause**: Case mismatch or an unexpected pattern. The file might contain `ERROR:` or `Error` (capital E) instead.
   - **Resolution**: Use case-insensitive flags or verify exact match (e.g., `sed 's/[Ee]rror/ERROR/' file.log`).
   - **Prevention**: Always confirm the pattern with a `grep` test first.

2. **uniq Fails to Remove Duplicates**
   - **Symptom**: `uniq -d data.txt` returns nothing, despite known duplicates.
   - **Likely Cause**: Data wasn’t sorted, so duplicates aren’t adjacent.
   - **Resolution**: Pipe through `sort` first: `sort data.txt | uniq -d`.
   - **Prevention**: Remember that `uniq` only checks consecutive lines.

3. **High CPU Usage When Sorting**
   - **Symptom**: Sorting large logs causes severe performance slowdown.
   - **Likely Cause**: `sort` can be memory/IO intensive on multi-GB files.
   - **Resolution**: Use partial or external sorts, split large files, or watch system limits (`sort --buffer-size=...`).
   - **Prevention**: Plan for resource usage or adopt parallel/distributed approaches for truly massive data sets.

---

## ❓ FAQ

### **Beginner Tier (3)**

1. **How do I save sed output to a file?**  
   - Use redirection: `sed 's/old/new/g' file.txt > newfile.txt`.
2. **Can awk handle CSV files?**  
   - Yes. Use `-F','` to set the comma as the field separator.
3. **Why does sort put `10` before `2` sometimes?**  
   - By default, it does lexicographic sorting. Use `-n` for numeric.

### **Intermediate Tier (3)**

1. **Can sed remove multiple patterns?**  
   - Yes, specify multiple commands with `-e`: `sed -e 's/foo/bar/' -e 's/baz/qux/' file`.
2. **Why does awk not print the correct field with `$4`?**  
   - Possibly the file uses different whitespace or delimiters. Use `-F` or check spacing.
3. **How do I perform a case-insensitive sort?**  
   - Use `sort -f` to fold uppercase and lowercase together.

### **SRE-Level Tier (3)**

1. **How do I handle multi-line logs with sed/awk?**  
   - Advanced sed uses hold space or multiline flags; awk can use custom record separators (RS). Sometimes external scripting is simpler.
2. **When to choose awk over Python or vice versa?**  
   - For quick, line-based transformations, awk is faster to implement. For larger codebases or multi-file logic, Python might be more maintainable.
3. **How can I mask sensitive data in logs?**  
   - Use `sed` or `awk` to substitute fields (e.g., `s/token=[^ ]+/token=****/`), then ensure logs are securely stored.

---

## 🔥 Detailed SRE Scenario

**Incident**: You notice sporadic HTTP 500 errors and slow response times. You suspect a database performance bottleneck.

**Investigation Steps**

1. **Check 500 Errors**

   ```bash
   grep " 500 " /var/log/nginx/access.log | wc -l
   ```

   > Quick measure of how many 500 errors occurred.

2. **Identify Heaviest-Hit Endpoints**

   ```bash
   awk '{print $7}' /var/log/nginx/access.log | sort | uniq -c | sort -nr | head -5
   ```

   > Summarizes which endpoints are receiving the most requests.

3. **Filter Slow Responses**

   ```bash
   awk '$NF > 100 {print $0}' /var/log/nginx/access.log
   ```

   > Identify requests that took > 100ms (or your threshold).

4. **Correlate with DB Errors**

   ```bash
   grep -i "error" /var/log/mysql/mysql.log
   ```

   > Check if DB is throwing errors that match the 500s timeline.

5. **Average Query Time**

   ```bash
   grep "time=" /var/log/mysql/mysql.log | sed 's/.*time=\([0-9]*\)ms.*/\1/' | \
   awk '{ sum+=$1; c++ } END { print "Avg query time:", sum/c, "ms" }'
   ```

   > See if queries are generally slower than normal.

6. **Check CPU/Memory**

   ```bash
   ps aux | sort -k3 -nr | head -5
   ```

   > Identify resource-heavy processes.

7. **Validate Config**

   ```bash
   sed -n '/rate_limit/,/}/p' /etc/nginx/nginx.conf
   ```

   > Ensure a misconfigured rate limit or throttle isn’t impacting performance.

---

## 🧠 Key Takeaways

1. **Command Summary (5–7 key points)**
   - **sed**: Stream editing for in-line substitutions, deletions, etc.
   - **awk**: Field-based scanning for data extraction, filtering, aggregations.
   - **sort**: Ordering data alphabetically or numerically.
   - **uniq**: Deduplicating sorted data.
   - **wc**: Counting lines, words, or bytes.
   - Harness these tools in pipelines for powerful on-the-fly transformations.

2. **Operational Insights (3–5 points)**
   1. Stream-based tools are efficient for large logs, crucial for real-time analysis.
   2. Sorting and deduplication help spot patterns and outliers in production incidents.
   3. Scripting these commands for routine tasks fosters consistency and reduces manual error.

3. **Best Practices (3–5 recommendations)**
   1. Test transformations (`sed`, `awk`) on non-critical data or backups before applying changes in place.
   2. Combine these commands with `grep`, `head`, `tail`, and watchers (like `watch`) for live system insights.
   3. Monitor resource usage when handling very large data sets or complex regex.

4. **Preview of Next Topic**
   - We’ll expand into process management and system monitoring, learning to control processes, measure performance, and build reliability—a perfect complement to the text-based analytics we’ve covered.

---

## 📚 Further Learning Resources

### 🟢 **Beginner**

1. **GNU sed Manual** – [https://www.gnu.org/software/sed/manual/](https://www.gnu.org/software/sed/manual/)
2. **Awk Introduction (Linuxize)** – [https://linuxize.com/post/awk-command/](https://linuxize.com/post/awk-command/)
3. **TutorialsPoint: Learning Bash Scripting** – [https://www.tutorialspoint.com/unix/bash_scripting.htm](https://www.tutorialspoint.com/unix/bash_scripting.htm)

### 🟡 **Intermediate**

1. **The Linux Command Line** – [http://linuxcommand.org/tlcl.php](http://linuxcommand.org/tlcl.php)
2. **Mastering the awk Command (DigitalOcean)** – [https://www.digitalocean.com/community/tutorials/how-to-use-the-awk-language-to-manipulate-text-in-linux](https://www.digitalocean.com/community/tutorials/how-to-use-the-awk-language-to-manipulate-text-in-linux)
3. **Grep, Sed, and Awk (O’Reilly)** – [https://www.oreilly.com/library/view/grep-sed-awk/9781449396677/](https://www.oreilly.com/library/view/grep-sed-awk/9781449396677/)

### 🔴 **SRE-Level**

1. **Google SRE Book: Monitoring & Alerting** – [https://sre.google/sre-book/](https://sre.google/sre-book/)
2. **Netflix TechBlog – Linux Performance Analysis** – [https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-accc10403c55](https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-accc10403c55)
3. **Advanced Sed and Awk (IBM Developer)** – [https://developer.ibm.com/tutorials/l-sed1/](https://developer.ibm.com/tutorials/l-sed1/)

---

**Congratulations!** You’ve reached the end of the merged, comprehensive Day 5 training resource on advanced text manipulation for SRE. By mastering `sed`, `awk`, `sort`, `uniq`, and `wc`—and learning how to combine them effectively—you’re well on your way to solving complex data challenges in production environments. Next stop: process management and real-time monitoring!
