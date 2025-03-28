# 🚀 **Day 4: Text Processing and Searching for SRE - Finding and Manipulating Data**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 3:**

Yesterday, you learned about Linux permissions and ownership, including how to interpret and modify file permissions (`chmod`), change ownership (`chown`, `chgrp`), and perform administrative tasks using `sudo`. These skills enable you to secure your systems and ensure services have appropriate access to resources.

### 📅 **Today's Topics and Importance:**

Today, we focus on **text processing and searching** capabilities in Linux. These skills are absolutely critical for SREs because:

- Log analysis is central to troubleshooting production issues
- Configuration file management requires precise text searching and manipulation
- Finding specific files across complex systems is a daily task
- Data needs to be extracted, filtered, and transformed for monitoring and alerting
- Pipes and redirections allow for powerful command combinations that automate complex workflows

These skills dramatically increase your efficiency in identifying and resolving issues in production environments.

### 🎯 **Learning Objectives:**

By the end of Day 4, you will be able to:

- Search for patterns within files using `grep`
- Locate files across the filesystem using `find`
- Chain commands effectively using pipes (`|`)
- Redirect command output and input using operators (`>`, `>>`, `<`)
- Apply these tools in common SRE scenarios to solve real-world problems

---

## 📚 **Core Concepts Explained**

### **The Power of Text Processing in SRE**

Linux excels at text processing for several reasons:

1. **Text-Based Configuration**: Most Linux configurations are stored in plain text files, making text processing tools essential for system management

2. **Structured Logging**: Applications typically generate text-based logs that can be analyzed with standard text processing tools

3. **Command Composition**: Linux's design philosophy encourages small, focused tools that can be combined to solve complex problems

4. **Automation Capabilities**: Text processing enables scripting and automation of routine tasks

For SREs, these capabilities mean you can quickly analyze gigabytes of logs, extract meaningful data, find configuration issues, and automate remediation steps—all critical for maintaining system reliability.

### **Command Chaining with Pipes and Redirection**

Linux's two powerful mechanisms for combining commands are:

1. **Pipes (`|`)**: Send the output of one command as input to another command, creating processing pipelines
   
2. **Redirection (`>`, `>>`, `<`)**: Direct output to files or take input from files instead of the terminal

These mechanisms allow you to build sophisticated data processing workflows without writing complex programs.

---

## 💻 **Commands to Learn Today**

### **1. grep – Pattern Searching in Files**

**Purpose**: Search for text patterns in files using regular expressions.

**SRE Context**: Essential for log analysis, finding errors in configuration files, and extracting specific information from large datasets.

**Syntax:**
```bash
grep [options] pattern [file...]
```

**Common options:**
- `-i`: Case-insensitive search
- `-r` or `-R`: Recursive search through directories
- `-n`: Show line numbers of matches
- `-v`: Invert match (show non-matching lines)
- `-A n`: Show n lines after the match
- `-B n`: Show n lines before the match
- `-C n`: Show n lines before and after the match
- `-E`: Use extended regular expressions
- `--color`: Highlight the matching text

**Examples:**

Search for error messages in a log file:
```bash
[sre@prod-server ~]$ grep "ERROR" /var/log/application.log
```

Find configuration entries for a specific service, ignoring case:
```bash
[sre@prod-server ~]$ grep -i "mysql" /etc/config/services.conf
```

Recursively search for API endpoints in a code repository:
```bash
[sre@prod-server ~]$ grep -r "api/v[0-9]" /opt/application/src/
```

Show errors with 3 lines of context to understand what happened before and after:
```bash
[sre@prod-server ~]$ grep -C 3 "connection refused" /var/log/nginx/error.log
```

Find all lines NOT containing "DEBUG" to filter out noise:
```bash
[sre@prod-server ~]$ grep -v "DEBUG" /var/log/application.log
```

### **2. find – Locate Files and Directories**

**Purpose**: Search for files and directories based on various criteria.

**SRE Context**: Helps locate configuration files, logs, large files consuming disk space, recently modified files that might relate to an incident, or files with incorrect permissions.

**Syntax:**
```bash
find [path] [criteria] [action]
```

**Common criteria:**
- `-name pattern`: Search by filename (case-sensitive)
- `-iname pattern`: Search by filename (case-insensitive)
- `-type [f|d|l]`: Filter by file type (f=file, d=directory, l=symlink)
- `-size n[cwbkMG]`: Find files by size (c=bytes, k=KB, M=MB, G=GB)
- `-mtime n`: Files modified n days ago
- `-mmin n`: Files modified n minutes ago
- `-user username`: Files owned by username
- `-perm mode`: Files with specific permissions
- `-exec command {} \;`: Execute command on each found file

**Examples:**

Find configuration files modified in the last 24 hours:
```bash
[sre@prod-server ~]$ find /etc -name "*.conf" -type f -mtime -1
```

Locate large log files (>100MB) that might be filling disk space:
```bash
[sre@prod-server ~]$ find /var/log -type f -size +100M -exec ls -lh {} \;
```

Find files owned by a specific service account:
```bash
[sre@prod-server ~]$ find /opt/application -user appuser
```

Search for potentially insecure files with world-writable permissions:
```bash
[sre@prod-server ~]$ find /etc -type f -perm -o=w
```

Find and delete old temporary files:
```bash
[sre@prod-server ~]$ find /tmp -type f -mtime +30 -exec rm {} \;
```

Find log files and grep them for errors (combining commands):
```bash
[sre@prod-server ~]$ find /var/log -name "*.log" -type f -exec grep -l "ERROR" {} \;
```

### **3. Pipes (`|`) – Command Chaining**

**Purpose**: Connect commands by sending the output of one command as input to another.

**SRE Context**: Essential for filtering and transforming data between commands, allowing complex analyses without intermediate files.

**Syntax:**
```bash
command1 | command2 | command3
```

**Examples:**

Find processes consuming the most CPU:
```bash
[sre@prod-server ~]$ ps aux | sort -rk 3 | head -10
```

Count occurrences of HTTP status codes in a web server log:
```bash
[sre@prod-server ~]$ grep -o 'HTTP/1\.[01]" [0-9]\{3\}' /var/log/nginx/access.log | sort | uniq -c | sort -rn
```

Extract all unique IP addresses from a log file:
```bash
[sre@prod-server ~]$ grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' /var/log/auth.log | sort | uniq
```

Find the largest directories:
```bash
[sre@prod-server ~]$ du -h /var | sort -hr | head -10
```

### **4. Redirection (`>`, `>>`, `<`) – Input/Output Control**

**Purpose**: Direct command output to files or take input from files instead of the terminal.

**SRE Context**: Used for capturing command output for documentation, creating configuration files, or feeding data into commands.

**Types of redirection:**
- `command > file`: Redirect stdout to a file (overwrite)
- `command >> file`: Redirect stdout to a file (append)
- `command 2> file`: Redirect stderr to a file
- `command &> file`: Redirect both stdout and stderr to a file
- `command < file`: Take input from a file

**Examples:**

Save a list of running processes to a file:
```bash
[sre@prod-server ~]$ ps aux > processes.txt
```

Append monitoring output to a log file:
```bash
[sre@prod-server ~]$ date >> /var/log/monitoring.log
[sre@prod-server ~]$ df -h >> /var/log/monitoring.log
```

Redirect errors to a separate log file:
```bash
[sre@prod-server ~]$ find /etc -name "*.conf" 2> find_errors.log
```

Redirect both standard output and errors to a file:
```bash
[sre@prod-server ~]$ ping -c 4 unreachablehost &> ping_output.log
```

Use a file as input to a command:
```bash
[sre@prod-server ~]$ sort < unsorted_data.txt
```

Combine redirection with pipes for complex operations:
```bash
[sre@prod-server ~]$ grep "ERROR" /var/log/application.log | sort | uniq -c > error_summary.txt
```

---

## 🔍 **SRE Perspective: Common Text Processing Patterns**

### **1. Log Analysis Workflows**

Quickly identifying issues in production logs:

```bash
# Extract all ERROR and WARNING lines
grep -E "ERROR|WARNING" /var/log/application.log

# Get the most frequent errors
grep "ERROR" /var/log/application.log | cut -d':' -f3 | sort | uniq -c | sort -nr

# Find errors around a specific time
grep -A 10 -B 10 "2023-10-15 14:2[0-9]" /var/log/application.log | grep -i error

# Track a request through distributed logs using its ID
find /var/log -name "*.log" -exec grep -l "REQUEST-1234" {} \; | xargs grep "REQUEST-1234"
```

### **2. System Health Checking**

Command pipelines for system diagnostics:

```bash
# Find processes consuming the most memory
ps aux | sort -rnk 4 | head

# Check disk space with human-readable output
df -h | grep -v "tmpfs" | sort -rk 5

# Find services listening on network ports
sudo netstat -tulpn | grep LISTEN

# Find recently changed configuration files
find /etc -type f -mtime -1 -exec ls -la {} \;
```

### **3. Configuration Management**

Examining and modifying configuration files:

```bash
# Find all configuration files that reference a specific database
grep -r "db.example.com" /etc --include="*.conf"

# Create a backup before editing critical configs
cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.$(date +%Y%m%d)

# Comment out all lines containing a specific setting
grep -n "old_setting" /etc/application/config.conf
# Then use an editor to comment those lines
```

---

## 🎯 **Practical Exercise: SRE Log Analysis**

Let's practice analyzing logs like an SRE would during an incident:

1. **Create sample log files for analysis**:
   ```bash
   # Create a directory for practice
   mkdir -p ~/sre-practice/logs

   # Generate a sample application log
   cat > ~/sre-practice/logs/application.log << 'EOF'
   2023-10-15 14:20:45 INFO [RequestProcessor] Processing request REQUEST-1234
   2023-10-15 14:20:46 DEBUG [DatabaseLayer] Connecting to database
   2023-10-15 14:20:47 ERROR [DatabaseLayer] Connection refused to db.example.com:3306
   2023-10-15 14:20:48 WARNING [RequestProcessor] Database unavailable, using cache
   2023-10-15 14:20:49 INFO [CacheLayer] Retrieved data from cache
   2023-10-15 14:20:50 INFO [RequestProcessor] Request REQUEST-1234 completed with status WARNING
   2023-10-15 14:21:10 INFO [RequestProcessor] Processing request REQUEST-1235
   2023-10-15 14:21:11 DEBUG [DatabaseLayer] Connecting to database
   2023-10-15 14:21:12 ERROR [DatabaseLayer] Connection refused to db.example.com:3306
   2023-10-15 14:21:13 ERROR [CacheLayer] Cache miss for requested data
   2023-10-15 14:21:14 ERROR [RequestProcessor] Request REQUEST-1235 failed with status ERROR
   EOF

   # Create a web server access log
   cat > ~/sre-practice/logs/access.log << 'EOF'
   192.168.1.10 - - [15/Oct/2023:14:20:40] "GET /api/data HTTP/1.1" 200 1234
   192.168.1.10 - - [15/Oct/2023:14:20:45] "GET /api/data HTTP/1.1" 200 1234
   192.168.1.15 - - [15/Oct/2023:14:20:50] "GET /api/users HTTP/1.1" 200 532
   192.168.1.20 - - [15/Oct/2023:14:21:05] "GET /api/settings HTTP/1.1" 404 125
   192.168.1.10 - - [15/Oct/2023:14:21:10] "GET /api/data HTTP/1.1" 500 890
   192.168.1.25 - - [15/Oct/2023:14:21:15] "GET /api/admin HTTP/1.1" 403 120
   192.168.1.30 - - [15/Oct/2023:14:21:20] "GET /api/health HTTP/1.1" 200 98
   EOF
   ```

2. **Analyze the application log**:
   ```bash
   # Extract all error lines
   grep "ERROR" ~/sre-practice/logs/application.log
   
   # Show context around database errors
   grep -B 1 -A 2 "Connection refused" ~/sre-practice/logs/application.log
   
   # Count occurrences of each log level
   grep -o 'INFO\|DEBUG\|WARNING\|ERROR' ~/sre-practice/logs/application.log | sort | uniq -c
   
   # Find all lines related to a specific request
   grep "REQUEST-1234" ~/sre-practice/logs/application.log
   ```

3. **Analyze the web server log**:
   ```bash
   # Extract HTTP status codes and count them
   grep -o "HTTP/1.1\" [0-9]\{3\}" ~/sre-practice/logs/access.log | sort | uniq -c
   
   # Find all 4xx and 5xx errors
   grep -E "HTTP/1.1\" [45][0-9]{2}" ~/sre-practice/logs/access.log
   
   # Count requests by IP address
   grep -o "^[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}" ~/sre-practice/logs/access.log | sort | uniq -c
   
   # Identify endpoints with error responses
   grep -E "HTTP/1.1\" [45][0-9]{2}" ~/sre-practice/logs/access.log | grep -o "GET [^ ]*" | sort | uniq
   ```

4. **Combine multiple log sources**:
   ```bash
   # Find timestamps where both logs showed errors
   grep "ERROR" ~/sre-practice/logs/application.log | cut -d' ' -f1,2 > ~/sre-practice/error_times.txt
   grep -E "HTTP/1.1\" [45][0-9]{2}" ~/sre-practice/logs/access.log | grep -o "\[[^]]*\]" | cut -d':' -f1 | sed 's/\[//g' > ~/sre-practice/access_error_times.txt
   
   # This is a simplified example; in real scenarios, you'd need more sophisticated time matching
   ```

5. **Save your findings**:
   ```bash
   # Create an incident report template
   echo "# Incident Analysis" > ~/sre-practice/incident_report.txt
   echo "## Error Summary" >> ~/sre-practice/incident_report.txt
   echo "### Application Errors" >> ~/sre-practice/incident_report.txt
   grep "ERROR" ~/sre-practice/logs/application.log >> ~/sre-practice/incident_report.txt
   echo "### Web Server Errors" >> ~/sre-practice/incident_report.txt
   grep -E "HTTP/1.1\" [45][0-9]{2}" ~/sre-practice/logs/access.log >> ~/sre-practice/incident_report.txt
   ```

---

## 📝 **Quiz: Text Processing and Searching**

Test your understanding of today's material:

1. During an incident, you need to find all occurrences of "connection timeout" in logs, including the lines before and after each occurrence to understand the context. Which command would you use?
   - a) `grep "connection timeout" /var/log/application.log`
   - b) `grep -A 2 -B 2 "connection timeout" /var/log/application.log`
   - c) `find /var/log -name "connection timeout"`
   - d) `grep -v "connection timeout" /var/log/application.log`

2. You need to find all configuration files larger than 1MB in the /etc directory. Which command is correct?
   ```bash
   # Fill in the blank
   find /etc _______ -size +1M
   ```

3. To extract the number of 5xx errors from a web server log and save the count to a file, which pipeline would you use?
   - a) `grep "HTTP/1.1\" 5[0-9][0-9]" access.log | wc -l > 5xx_count.txt`
   - b) `grep -c "5[0-9][0-9]" access.log > 5xx_count.txt`
   - c) `find access.log -name "5[0-9][0-9]" | wc -l > 5xx_count.txt`
   - d) `tail access.log | grep "5[0-9][0-9]" > 5xx_count.txt`

4. During system maintenance, you need to append the output of a disk space check to a log file without overwriting existing content. Which redirection operator would you use?
   - a) `df -h > maintenance.log`
   - b) `df -h >> maintenance.log`
   - c) `df -h | maintenance.log`
   - d) `df -h 2> maintenance.log`

5. You suspect a security issue and need to find all files modified in the last 24 hours anywhere on the system. Which command is most appropriate?
   - a) `ls -la /* --time=mtime`
   - b) `find / -mtime 1`
   - c) `find / -mtime -1 -type f`
   - d) `grep -r "modified" / --include="*"`

---

## ❓ **FAQ for SREs: Text Processing and Searching**

**Q1: How can I efficiently search through large log files without loading the entire file into memory?**

**A:** Several approaches work well for large logs:

- Use `less +F /var/log/large.log` to follow a log while saving memory
- Split processing with `head`/`tail` to work on portions: `tail -n 10000 large.log | grep "pattern"`
- For extremely large files, consider tools like `zgrep` for compressed logs or `awk` for streaming processing
- When possible, filter logs at the source using syslog facilities or log-rotation policies

**Q2: How do I search across multiple log files spread across different directories?**

**A:** Combine `find` with `grep`:

```bash
# Search all logs in /var/log and subdirectories for a pattern
find /var/log -name "*.log" -type f -exec grep -l "search pattern" {} \;

# For more control, use xargs
find /var/log -name "*.log" -type f | xargs grep "search pattern"

# Use parallel processing for faster results on large log collections
find /var/log -name "*.log" -type f | xargs -P 4 grep "search pattern"
```

**Q3: How can I extract and analyze structured data like JSON logs?**

**A:** For structured logs:

- Basic extraction with `grep` and `cut`:
  ```bash
  grep "error" application.log | grep -o '"message":"[^"]*"' | cut -d':' -f3 | tr -d '"'
  ```

- For JSON specifically, use `jq` (may need installation):
  ```bash
  grep "error" application.log | jq -r '.message'
  ```

- For CSV-like data, `awk` is powerful:
  ```bash
  awk -F, '{print $3}' data.csv | sort | uniq -c
  ```

**Q4: What's the best way to monitor logs in real-time during an incident?**

**A:** Combine real-time monitoring with filtering:

```bash
# Follow logs with highlighting
tail -f /var/log/application.log | grep --color=always "ERROR|WARN"

# Follow multiple logs simultaneously
tail -f /var/log/application.log /var/log/system.log | grep "connection"

# Filter noisy logs in real-time
tail -f /var/log/application.log | grep -v "DEBUG" | grep --color=always "ERROR|WARN"
```

---

## 🚧 **Common Issues and Troubleshooting**

### **Issue 1: grep returns too many matches or too few**

**Possible causes:**
- Regular expression syntax issues
- Case sensitivity differences
- Special characters not properly escaped

**Solutions:**
```bash
# Make search case-insensitive
grep -i "error" log.txt

# Use word boundaries to match whole words only
grep -w "error" log.txt

# Use extended regex for more complex patterns
grep -E "error|warning" log.txt

# Escape special characters
grep "connection\.refused" log.txt
# OR
grep -F "connection.refused" log.txt  # Treat pattern as fixed string
```

### **Issue 2: find command runs too slowly**

**Possible causes:**
- Searching large filesystems
- Too many nested paths
- Excessive file operations in `-exec`

**Solutions:**
```bash
# Restrict search depth
find /var/log -maxdepth 2 -name "*.log"

# Exclude certain directories
find /var -not -path "*/cache/*" -name "*.log"

# Limit to specific filesystems
find /var -xdev -name "*.log"

# Use -exec with + instead of \; for fewer processes
find /var -name "*.log" -exec grep "error" {} \+
```

---

## 🔄 **Real-World SRE Scenario: Troubleshooting a Service Outage**

**Situation:** Users report that the authentication service is failing intermittently. You need to investigate the cause and determine the impact.

**SRE Response Using Today's Commands:**

1. Check the service status:
   ```bash
   sudo systemctl status auth-service
   ```

2. Look for errors in the service log:
   ```bash
   sudo grep -i "error\|failed\|exception" /var/log/auth-service/application.log | tail -n 50
   ```

3. Check when the errors started occurring:
   ```bash
   sudo grep -i "error" /var/log/auth-service/application.log | head -n 10
   ```

4. Look for patterns in the errors:
   ```bash
   sudo grep -i "error" /var/log/auth-service/application.log | cut -d' ' -f4- | sort | uniq -c | sort -nr
   ```

5. Check for related system issues:
   ```bash
   sudo find /var/log -type f -mtime -1 -exec grep -l "database\|connection\|refused" {} \;
   ```

6. Check network connectivity to the database:
   ```bash
   ping -c 3 db-server.example.com > ping_results.txt
   ```

7. Find database configuration files:
   ```bash
   sudo find /etc -name "*.conf" -type f -exec grep -l "database\|connection" {} \;
   ```

8. Assess the impact by counting affected requests:
   ```bash
   grep -c "authentication failed" /var/log/auth-service/application.log
   ```

9. Create a report of your findings:
   ```bash
   {
     echo "## Auth Service Investigation"
     echo "### Error Count:"
     grep -c "error" /var/log/auth-service/application.log
     echo "### Most Common Errors:"
     grep -i "error" /var/log/auth-service/application.log | sort | uniq -c | sort -nr | head -n 5
     echo "### Database Connectivity:"
     cat ping_results.txt
   } > auth_service_report.txt
   ```

This investigation flow demonstrates how text processing commands are chained together in real incident response scenarios.

---

## 🔧 **Advanced Tips for SREs**

### **Filtering Out Noise**

When working with verbose logs:
```bash
# Exclude multiple patterns
grep -v -E "DEBUG|INFO|healthcheck" application.log

# Focus on unusual events
grep -v -f common_patterns.txt application.log
```

### **Time-Based Analysis**

For time-sensitive troubleshooting:
```bash
# Extract log entries during a specific timeframe
sed -n '/2023-10-15 14:2[0-5]/,/2023-10-15 14:3[0-5]/p' application.log

# Find rapid sequences of errors (errors occurring within seconds of each other)
grep "ERROR" application.log | awk '{print $1, $2}' | uniq -c | grep -E "^ *[0-9]{2,}"
```

### **Multi-Service Correlation**

For complex, distributed systems:
```bash
# Extract request IDs from multiple logs
grep -o "REQUEST-[0-9]*" /var/log/service1.log | sort > service1_requests.txt
grep -o "REQUEST-[0-9]*" /var/log/service2.log | sort > service2_requests.txt

# Find requests that appear in both logs
comm -12 service1_requests.txt service2_requests.txt

# Trace a single request across multiple services
find /var/log -name "*.log" -exec grep -l "REQUEST-1234" {} \; | xargs grep "REQUEST-1234"
```

---

## 📚 **Further Learning Resources**

- [GREP Command in Linux/Unix with Examples](https://www.geeksforgeeks.org/grep-command-in-unixlinux/)
- [Find Command in Linux with Examples](https://linuxize.com/post/how-to-find-files-in-linux-using-the-command-line/)
- [Linux Pipes and Redirection](https://ryanstutorials.net/linuxtutorial/piping.php)
- [Google SRE Book - Chapter 15: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Log Analysis for SRE - Datadog Blog](https://www.datadoghq.com/blog/log-analysis-monitoring/)

---

🎓 **Day 4 completed!** Tomorrow, we'll explore more advanced text manipulation tools like `sed`, `awk`, `sort`, and `uniq`, which will further enhance your ability to analyze and transform data in complex systems.
