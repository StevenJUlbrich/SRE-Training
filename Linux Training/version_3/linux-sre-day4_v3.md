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

**Beginner's Note**: Think of text processing as the ability to find needles in haystacks. Instead of manually reading through thousands of lines in log files, you can use commands to instantly locate exactly what you need.

**SRE Perspective**: For SREs, these capabilities mean you can quickly analyze gigabytes of logs, extract meaningful data, find configuration issues, and automate remediation steps—all critical for maintaining system reliability.

### **Command Chaining with Pipes and Redirection**

Linux's two powerful mechanisms for combining commands are:

1. **Pipes (`|`)**: Send the output of one command as input to another command, creating processing pipelines
   
2. **Redirection (`>`, `>>`, `<`)**: Direct output to files or take input from files instead of the terminal

**Beginner's Note**: Pipes work like assembly lines in a factory. Each command is a station that performs a specific task on the data before passing it to the next station.

**SRE Perspective**: These mechanisms allow you to build sophisticated data processing workflows without writing complex programs, essential for quick incident response and automated monitoring.

---

## 💻 **Commands to Learn Today**

### **1. grep – Pattern Searching in Files**

**Purpose**: Search for text patterns in files using regular expressions.

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

**Basic Examples:**

Search for a specific word in a file:
```bash
grep "error" logfile.txt
```

Case-insensitive search:
```bash
grep -i "warning" logfile.txt
```

**Intermediate Examples:**

Show context around matches:
```bash
grep -C 3 "connection refused" /var/log/nginx/error.log
```

Recursive search in directories:
```bash
grep -r "TODO" /home/user/project/
```

Show line numbers with matches:
```bash
grep -n "ERROR" application.log
```

**SRE Examples:**

Find all error messages except debugging information:
```bash
grep "ERROR" /var/log/application.log | grep -v "DEBUG"
```

Search with regular expressions to find API endpoints:
```bash
grep -E "GET /api/v[0-9]+/" /var/log/nginx/access.log
```

**SRE Context**: Essential for log analysis, finding errors in configuration files, and extracting specific information from large datasets. During incidents, `grep` is often the first tool SREs reach for to identify patterns in logs.

**Beginner's Tip**: The name `grep` comes from "global regular expression print" - think of it as a search function for files.

### **2. find – Locate Files and Directories**

**Purpose**: Search for files and directories based on various criteria.

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

**Basic Examples:**

Find all text files in current directory:
```bash
find . -name "*.txt"
```

Find directories only:
```bash
find . -type d
```

**Intermediate Examples:**

Find files modified in the last 24 hours:
```bash
find /home/user -type f -mtime -1
```

Find files larger than 100MB:
```bash
find /var -type f -size +100M
```

**SRE Examples:**

Locate configuration files modified in the last 24 hours:
```bash
find /etc -name "*.conf" -type f -mtime -1
```

Find and remove old temporary files:
```bash
find /tmp -type f -mtime +30 -exec rm {} \;
```

Find files with incorrect permissions:
```bash
find /var/www -type f -perm -o=w
```

**SRE Context**: Helps locate configuration files, logs, large files consuming disk space, recently modified files that might relate to an incident, or files with incorrect permissions.

**Beginner's Tip**: Unlike `grep` which searches file content, `find` searches for the files themselves based on their properties.

### **3. Pipes (`|`) – Command Chaining**

**Purpose**: Connect commands by sending the output of one command as input to another.

**Syntax:**
```bash
command1 | command2 | command3
```

**Basic Examples:**

List only directories in long format:
```bash
ls -l | grep "^d"
```

Count lines in a file:
```bash
cat file.txt | wc -l
```

**Intermediate Examples:**

Find processes for a specific application:
```bash
ps aux | grep nginx
```

Show the top 5 largest files:
```bash
du -h /var/log | sort -rh | head -5
```

**SRE Examples:**

Count occurrences of HTTP status codes in a web server log:
```bash
grep -o 'HTTP/1\.[01]" [0-9]\{3\}' /var/log/nginx/access.log | sort | uniq -c | sort -rn
```

Monitor CPU-intensive processes:
```bash
ps aux | sort -rk 3 | head -10
```

**SRE Context**: Essential for filtering and transforming data between commands, allowing complex analyses without intermediate files. Pipes are the foundation of the SRE toolbox for incident response.

**Beginner's Tip**: Think of pipes as connecting multiple tools together in a chain, with data flowing from left to right.

### **4. Redirection (`>`, `>>`, `<`) – Input/Output Control**

**Purpose**: Direct command output to files or take input from files instead of the terminal.

**Types of redirection:**
- `command > file`: Redirect stdout to a file (overwrite)
- `command >> file`: Redirect stdout to a file (append)
- `command 2> file`: Redirect stderr to a file
- `command &> file`: Redirect both stdout and stderr to a file
- `command < file`: Take input from a file

**Basic Examples:**

Save command output to a file:
```bash
ls > filelist.txt
```

Append text to a file:
```bash
echo "new entry" >> log.txt
```

**Intermediate Examples:**

Redirect errors to a separate file:
```bash
find /etc -name "*.conf" 2> find_errors.log
```

Use a file as input:
```bash
sort < unsorted_data.txt
```

**SRE Examples:**

Capture both normal output and errors when running a script:
```bash
./backup_script.sh &> backup_log.txt
```

Create a quick report from multiple commands:
```bash
{
  echo "System Report - $(date)"
  echo "Disk Usage:"
  df -h
  echo "Memory Usage:"
  free -h
} > system_report.txt
```

**SRE Context**: Used for capturing command output for documentation, creating configuration files, or feeding data into commands. Also critical for automated scripts and cron jobs that run without a terminal.

**Beginner's Tip**: Think of `>` as pointing where output should go, with `>>` meaning "add to the end" rather than replacing.

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

## 🎯 **Practical Exercises: From Beginner to SRE**

### **Beginner Exercises**

1. Create a text file called `sample.txt` with a few lines of text.
2. Use `grep` to search for a specific word in that file.
3. Use `find` to locate all `.txt` files in your home directory.
4. Use a pipe to list all hidden files in your home directory:
   ```bash
   ls -a ~ | grep "^\."
   ```
5. Redirect the output of `ls -l` to a file called `directory_contents.txt`.

### **Intermediate Exercises**

1. Create a directory structure with nested folders and various file types:
   ```bash
   mkdir -p practice/{docs,scripts,logs}
   touch practice/docs/{file1.txt,file2.txt,notes.md}
   touch practice/scripts/{script1.sh,script2.sh}
   touch practice/logs/{app.log,system.log}
   ```

2. Use `find` to locate all `.sh` files and make them executable:
   ```bash
   find practice -name "*.sh" -exec chmod +x {} \;
   ```

3. Generate sample log entries:
   ```bash
   for i in {1..50}; do
     echo "$(date) INFO: Normal operation $i" >> practice/logs/app.log
     if (($i % 10 == 0)); then
       echo "$(date) ERROR: Something went wrong at step $i" >> practice/logs/app.log
     fi
   done
   ```

4. Use `grep` to extract and count error messages:
   ```bash
   grep "ERROR" practice/logs/app.log | wc -l
   ```

5. Use pipes to show only the filenames with their sizes in human-readable format:
   ```bash
   ls -l practice | grep -v "^d" | awk '{print $9, $5}'
   ```

### **SRE Application Exercises**

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
   ```

4. **Create an incident report**:
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

## 📝 **Quiz: Test Your Knowledge**

### **Beginner Level**

1. Which symbol is used to pipe the output of one command to another?
   - a) `>`
   - b) `>>`
   - c) `|`
   - d) `<`

2. Which command would you use to search for the word "error" in a file?
   - a) `find "error" file.txt`
   - b) `grep "error" file.txt`
   - c) `locate "error" file.txt`
   - d) `search "error" file.txt`

3. To save the output of a command to a file (overwriting any existing content), which operator would you use?
   - a) `>`
   - b) `>>`
   - c) `|`
   - d) `<`

### **Intermediate Level**

4. To perform a case-insensitive search with grep, which option do you use?
   - a) `-c`
   - b) `-n`
   - c) `-i`
   - d) `-v`

5. If you want to find all files modified in the last 24 hours, which find option would you use?
   - a) `-time 24`
   - b) `-modified 1`
   - c) `-mtime -1`
   - d) `-newer 1day`

6. What will the command `ls | grep "^d"` show?
   - a) All files that start with the letter "d"
   - b) All directories
   - c) All hidden files
   - d) All files larger than "d" bytes

### **SRE Application Level**

7. During an incident, you need to find all occurrences of "connection timeout" in logs, including the lines before and after each occurrence. Which command would you use?
   - a) `grep "connection timeout" /var/log/application.log`
   - b) `grep -A 2 -B 2 "connection timeout" /var/log/application.log`
   - c) `find /var/log -name "connection timeout"`
   - d) `grep -v "connection timeout" /var/log/application.log`

8. To extract the number of 5xx errors from a web server log and save the count to a file, which pipeline would you use?
   - a) `grep "HTTP/1.1\" 5[0-9][0-9]" access.log | wc -l > 5xx_count.txt`
   - b) `grep -c "5[0-9][0-9]" access.log > 5xx_count.txt`
   - c) `find access.log -name "5[0-9][0-9]" | wc -l > 5xx_count.txt`
   - d) `tail access.log | grep "5[0-9][0-9]" > 5xx_count.txt`

9. You suspect a security issue and need to find all files with world-writable permissions anywhere on the system. Which command is most appropriate?
   - a) `ls -la / | grep "w"`
   - b) `find / -type f -perm -o=w`
   - c) `grep -r "777" /etc/passwd`
   - d) `chmod -R o-w / --list`

---

## ❓ **FAQ: From Beginners to SREs**

### **Beginner FAQs**

**Q1: What's the difference between `grep` and `find`?**

**A:** 
- `grep` searches for text patterns **inside** files
- `find` searches for the files themselves based on name, type, size, etc.

Think of `grep` as a content searcher and `find` as a file searcher.

**Q2: What's the difference between `>` and `>>`?**

**A:** Both redirect output to a file, but:
- `>` overwrites any existing content in the file
- `>>` appends new content to the end of the file, preserving what was already there

Use `>` when you want a fresh start, and `>>` when you want to add more data.

**Q3: Can I combine multiple commands without pipes?**

**A:** Yes, there are several ways:
- Use semicolons to run commands sequentially: `cmd1 ; cmd2`
- Use `&&` to run the second command only if the first succeeds: `cmd1 && cmd2`
- Use `||` to run the second command only if the first fails: `cmd1 || cmd2`

### **Intermediate FAQs**

**Q4: How can I use `find` with multiple criteria?**

**A:** You can combine criteria using operators:
- `-a` or just a space for AND
- `-o` for OR
- `!` or `-not` for NOT

Example:
```bash
# Find .txt files that are larger than 1MB
find /home -name "*.txt" -a -size +1M
```

**Q5: Can I search for multiple patterns with grep?**

**A:** Yes, in several ways:
- Use the `-E` option (extended regex): `grep -E "pattern1|pattern2" file.txt`
- Use multiple grep commands with pipes: `grep "pattern1" file.txt | grep "pattern2"`
- Use the `-e` option multiple times: `grep -e "pattern1" -e "pattern2" file.txt`

**Q6: How can I make my searches faster with large files or directories?**

**A:** Try these techniques:
- Be more specific with search paths in `find`
- Use `-type` to limit searches to files or directories
- Add the `-name` option first in `find` commands
- For large files, use `grep` with `head` or `tail` to limit the search area
- Consider tools like `ripgrep` (rg) for faster performance on large codebases

### **SRE FAQs**

**Q7: How can I efficiently search through large log files without loading the entire file into memory?**

**A:** Several approaches work well for large logs:

- Use `less +F /var/log/large.log` to follow a log while saving memory
- Split processing with `head`/`tail` to work on portions: `tail -n 10000 large.log | grep "pattern"`
- For extremely large files, consider tools like `zgrep` for compressed logs or `awk` for streaming processing
- When possible, filter logs at the source using syslog facilities or log-rotation policies

**Q8: What's the best way to monitor logs in real-time during an incident?**

**A:** Combine real-time monitoring with filtering:

```bash
# Follow logs with highlighting
tail -f /var/log/application.log | grep --color=always "ERROR|WARN"

# Follow multiple logs simultaneously
tail -f /var/log/application.log /var/log/system.log | grep "connection"

# Filter noisy logs in real-time
tail -f /var/log/application.log | grep -v "DEBUG" | grep --color=always "ERROR|WARN"
```

**Q9: How can I extract and analyze structured data like JSON logs?**

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

---

## 🚧 **Common Issues and Troubleshooting**

### **Issue 1: grep returns too many or too few matches**

**Possible causes:**
- Regular expression syntax issues
- Case sensitivity differences
- Special characters not properly escaped

**Beginner Solutions:**
```bash
# Make search case-insensitive
grep -i "error" log.txt

# Use word boundaries for whole words only
grep -w "error" log.txt
```

**SRE Solutions:**
```bash
# Use extended regex for more complex patterns
grep -E "error|warning" log.txt

# Escape special characters
grep "connection\.refused" log.txt
# OR
grep -F "connection.refused" log.txt  # Treat pattern as fixed string
```

### **Issue 2: "No such file or directory" errors**

**Possible causes:**
- Trying to access a file that doesn't exist
- Path typos
- Permissions issues

**Solutions:**
```bash
# Check if file exists
ls -la /path/to/file

# Verify path is correct
find /path -name "filename*"

# Check permissions
ls -la /path/to/directory
```

### **Issue 3: find command runs too slowly**

**Possible causes:**
- Searching large filesystems
- Too many nested paths
- Excessive file operations in `-exec`

**SRE Solutions:**
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

### **1. Filtering Out Noise**

When working with verbose logs:
```bash
# Exclude multiple patterns
grep -v -E "DEBUG|INFO|healthcheck" application.log

# Focus on unusual events
grep -v -f common_patterns.txt application.log
```

### **2. Time-Based Analysis**

For time-sensitive troubleshooting:
```bash
# Extract log entries during a specific timeframe
sed -n '/2023-10-15 14:2[0-5]/,/2023-10-15 14:3[0-5]/p' application.log

# Find rapid sequences of errors (errors occurring within seconds of each other)
grep "ERROR" application.log | awk '{print $1, $2}' | uniq -c | grep -E "^ *[0-9]{2,}"
```

### **3. Multi-Service Correlation**

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

### **For Beginners**
- [GREP Command in Linux/Unix with Examples](https://www.geeksforgeeks.org/grep-command-in-unixlinux/)
- [Find Command in Linux with Examples](https://linuxize.com/post/how-to-find-files-in-linux-using-the-command-line/)
- [Linux Pipes and Redirection](https://ryanstutorials.net/linuxtutorial/piping.php)

### **For Intermediate Users**
- [Advanced Grep Usage with Examples](https://www.digitalocean.com/community/tutorials/using-grep-regular-expressions-to-search-for-text-patterns-in-linux)
- [Master the Linux Find Command](https://linuxhandbook.com/find-command-examples/)
- [Learn Linux, 101: I/O Redirection](https://developer.ibm.com/tutorials/l-lpic1-103-4/)

### **For SRE Application**
- [Google SRE Book - Chapter 15: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Log Analysis for SRE - Datadog Blog](https://www.datadoghq.com/blog/log-analysis-monitoring/)
- [Effective Troubleshooting - Google SRE Book](https://sre.google/sre-book/effective-troubleshooting/)

---

🎓 **Day 4 completed!** Tomorrow, we'll explore more advanced text manipulation tools like `sed`, `awk`, `sort`, and `uniq`, which will further enhance your ability to analyze and transform data in complex systems.