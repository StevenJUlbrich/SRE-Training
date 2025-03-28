# 🚀 **Day 5: Advanced Text Processing for SRE - sed, awk, sort, uniq, and Data Transformation**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 4:**

Yesterday, you learned essential text processing and searching tools including `grep` for pattern matching, `find` for locating files, pipes (`|`) for command chaining, and redirection operators (`>`, `>>`, `<`) for controlling input and output. These skills enable you to search through logs, find specific files, and create basic data processing pipelines.

### 📅 **Today's Topics and Importance:**

Today, we're advancing to more powerful text processing tools: **`sed`**, **`awk`**, **`sort`**, and **`uniq`**. For SREs, these tools are invaluable because they allow you to:

- Transform configuration files and logs programmatically
- Extract specific fields from structured data
- Perform complex data analysis on the command line
- Identify patterns and anomalies in system behavior
- Create sophisticated data processing pipelines

These capabilities are crucial for incident response, capacity planning, performance analysis, and automation—all core aspects of the SRE role.

### 🎯 **Learning Objectives:**

By the end of Day 5, you will be able to:

- Perform text substitutions and manipulations with `sed`
- Extract and process structured data with `awk`
- Sort data efficiently with `sort`
- Remove or count duplicates with `uniq`
- Combine these tools into powerful data processing pipelines
- Apply these skills to common SRE scenarios

---

## 📚 **Core Concepts Explained**

### **Text as Data: The Unix Philosophy**

The Unix tools we're learning today embody a powerful philosophy: text is a universal interface. This makes them extraordinarily flexible for SRE work where you deal with:

- Log files from diverse systems
- Configuration files in different formats
- Monitoring and metrics data
- Infrastructure as code definitions
- API responses and reports

By treating everything as text and providing modular tools that process text streams, Unix/Linux creates a consistent interface for working with all these different types of data.

### **Stream Processing vs. Batch Processing**

The tools you'll learn today operate as **stream processors**—they process data line by line as it flows through a pipeline. This approach:

- Scales efficiently to very large files
- Uses minimal memory
- Works well in pipelines with other commands
- Enables real-time processing

This contrasts with graphical tools or full-featured programming languages, which often load entire files into memory. For an SRE managing systems with gigabytes of logs or thousands of configuration files, stream processing is essential.

---

## 💻 **Commands to Learn Today**

### **1. sed – Stream Editor**

**Purpose**: Perform text transformations on a stream of text (substitutions, deletions, insertions).

**SRE Context**: Used for modifying configuration files, transforming log formats, and preparing data for analysis.

**Syntax:**
```bash
sed [options] 'command' file
```

**Common commands:**
- `s/pattern/replacement/`: Substitute text
- `d`: Delete lines
- `p`: Print lines (used with `-n`)
- `/pattern/command`: Apply command to lines matching pattern

**Common options:**
- `-i`: Edit files in place
- `-n`: Suppress automatic printing
- `-e`: Add multiple commands
- `-r` or `-E`: Use extended regular expressions

**Examples:**

Replace "error" with "ERROR" in a log file:
```bash
[sre@prod-server ~]$ sed 's/error/ERROR/g' application.log
```

Remove all comment lines from a configuration file:
```bash
[sre@prod-server ~]$ sed '/^#/d' nginx.conf
```

Modify a configuration value:
```bash
[sre@prod-server ~]$ sed -i 's/max_connections = 100/max_connections = 200/g' postgres.conf
```

Extract specific sections from a structured log:
```bash
[sre@prod-server ~]$ sed -n '/BEGIN transaction/,/END transaction/p' transaction.log
```

### **2. awk – Pattern Scanning and Processing**

**Purpose**: Process text files by fields, allowing for complex data extraction and manipulation.

**SRE Context**: Ideal for analyzing structured logs, extracting specific metrics, and creating reports from command outputs.

**Syntax:**
```bash
awk [options] 'pattern {action}' file
```

**Key concepts:**
- **Fields**: awk divides each line into fields (default delimiter is whitespace)
- **$1, $2, ...**: Reference to field 1, field 2, etc.
- **$0**: Reference to the entire line
- **NR**: Built-in variable for the current line number
- **NF**: Built-in variable for the number of fields in the current line
- **BEGIN/END blocks**: Code that runs before/after processing

**Common options:**
- `-F`: Specify field separator
- `-v`: Set a variable

**Examples:**

Print specific columns from a command output:
```bash
[sre@prod-server ~]$ ps aux | awk '{print $2, $4, $11}'  # PID, %MEM, COMMAND
```

Calculate average response time from logs:
```bash
[sre@prod-server ~]$ awk '{ sum += $7; count++ } END { print "Average:", sum/count "ms" }' access.log
```

Extract specific fields from custom-delimited logs:
```bash
[sre@prod-server ~]$ awk -F'|' '{print $2, $5}' application.log
```

Filter logs by field conditions:
```bash
[sre@prod-server ~]$ awk '$4 > 300 {print}' response_times.log  # Responses over 300ms
```

Generate a report of HTTP status code distribution:
```bash
[sre@prod-server ~]$ awk '{ codes[$9]++ } END { for (code in codes) print code, codes[code] }' access.log
```

### **3. sort – Sort Lines of Text**

**Purpose**: Sort text input by various criteria.

**SRE Context**: Used for organizing data for analysis, preparing data for deduplication, and creating readable reports.

**Syntax:**
```bash
sort [options] file
```

**Common options:**
- `-n`: Numeric sort
- `-r`: Reverse sort
- `-k`: Sort by specific column
- `-t`: Specify field separator
- `-u`: Unique (remove duplicates)
- `-h`: Human-readable numbers (e.g., "2K", "3M")

**Examples:**

Sort a file alphabetically:
```bash
[sre@prod-server ~]$ sort users.txt
```

Sort processes by memory usage (highest first):
```bash
[sre@prod-server ~]$ ps aux | sort -k 4 -r
```

Sort by specific delimited field:
```bash
[sre@prod-server ~]$ sort -t',' -k 3 -n csv_data.txt  # Sort by 3rd column, numeric
```

Sort IP addresses correctly:
```bash
[sre@prod-server ~]$ sort -t . -k 1,1n -k 2,2n -k 3,3n -k 4,4n ip_addresses.txt
```

Sort by human-readable sizes:
```bash
[sre@prod-server ~]$ du -h | sort -hr
```

### **4. uniq – Report or Omit Repeated Lines**

**Purpose**: Filter or report repeated lines in a sorted file.

**SRE Context**: Used for identifying unique events, counting occurrences, and detecting patterns in logs.

**Syntax:**
```bash
uniq [options] [input [output]]
```

**Important note**: `uniq` only detects adjacent duplicate lines, so input typically needs to be sorted first.

**Common options:**
- `-c`: Prefix lines with count of occurrences
- `-d`: Only print duplicate lines
- `-u`: Only print unique lines (not duplicated)

**Examples:**

Remove duplicate lines:
```bash
[sre@prod-server ~]$ sort log_entries.txt | uniq
```

Count occurrences of each line:
```bash
[sre@prod-server ~]$ sort log_entries.txt | uniq -c
```

Find lines that appear multiple times:
```bash
[sre@prod-server ~]$ sort error_codes.txt | uniq -d
```

Find lines that appear only once:
```bash
[sre@prod-server ~]$ sort error_codes.txt | uniq -u
```

### **5. Combining Commands: Advanced Pipelines**

The true power of these tools emerges when you combine them into data processing pipelines:

**Analyze HTTP status code distribution in logs:**
```bash
[sre@prod-server ~]$ awk '{print $9}' access.log | sort | uniq -c | sort -nr
```

**Find the top 5 IP addresses making the most requests:**
```bash
[sre@prod-server ~]$ awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -5
```

**Calculate the percentage of error responses:**
```bash
[sre@prod-server ~]$ awk 'BEGIN{total=0; errors=0} {total++; if($9 >= 500) errors++} END{print "Error rate:", (errors/total)*100 "%"}' access.log
```

**Identify slow database queries and format a report:**
```bash
[sre@prod-server ~]$ grep "SLOW QUERY" mysql.log | sed 's/SLOW QUERY: //' | awk -F' time=' '{print $2, $1}' | sort -nr | head -10
```

---

## 🔍 **SRE Perspective: Common Text Processing Patterns**

### **1. Log Analysis and Metrics Generation**

SREs often need to extract metrics from unstructured or semi-structured logs:

```bash
# Calculate 95th percentile response time
sort -n response_times.log | awk 'BEGIN {count=0} {times[count]=$1; count++} END {print times[int(count*0.95)]}'

# Generate a histogram of response times
awk '{print int($1/100)*100}' response_times.log | sort -n | uniq -c | awk '{printf("%6d ms: %s\n", $2, "+" x $1)}'

# Count events per minute to detect spikes
grep "ERROR" application.log | awk '{print $1, $2}' | cut -d: -f1 | uniq -c

# Extract and aggregate error messages
grep "ERROR" application.log | sed 's/.*ERROR: \(.*\) in.*/\1/' | sort | uniq -c | sort -nr
```

### **2. Configuration Management**

SREs regularly need to audit and modify configuration files:

```bash
# Find all non-commented memory settings across configs
grep -r "^[^#].*memory" /etc/ | sed 's/:.*//' | sort | uniq

# Comment out all occurrences of a deprecated setting
sed -i 's/^old_setting/# old_setting/' /etc/application/*.conf

# Increase all timeout values by 50%
awk '/timeout/ {split($3, a, "s"); $3 = a[1] * 1.5 "s"; print; next} {print}' service.conf > service.conf.new

# Extract all security-related settings for audit
grep -r -E 'password|auth|ssl|secure' /etc/ | sort
```

### **3. System Monitoring and Reporting**

Creating reports and monitoring dashboards from command-line tools:

```bash
# Create a disk usage report sorted by size
df -h | grep -v tmpfs | awk 'NR>1 {print $5, $6}' | sort -nr

# Generate CPU usage report per service
ps aux | grep -v USER | awk '{print $2, $3, $11}' | sort -k2 -nr | head -10

# Summarize network connections by state
netstat -tan | awk 'NR>2 {print $6}' | sort | uniq -c | sort -nr

# Extract and sort the most recently modified files
find /var/log -type f -mtime -1 -exec ls -la {} \; | sort -k 6,8
```

---

## 🎯 **Practical Exercise: SRE Log Analysis and Reporting**

In this exercise, you'll apply today's tools to analyze web server logs and database performance data. You'll extract meaningful metrics, identify performance issues, and generate reports.

1. **Create the sample data files**:

```bash
# Create working directory
mkdir -p ~/sre-advanced/logs

# Create sample web server access log
cat > ~/sre-advanced/logs/access.log << 'EOF'
192.168.1.10 - - [15/Oct/2023:10:15:30 +0000] "GET /api/users HTTP/1.1" 200 1234 "https://example.com" "Mozilla/5.0" 35
192.168.1.15 - - [15/Oct/2023:10:15:35 +0000] "GET /api/users HTTP/1.1" 200 1234 "https://example.com" "Mozilla/5.0" 42
192.168.1.10 - - [15/Oct/2023:10:15:40 +0000] "GET /api/products HTTP/1.1" 200 5678 "https://example.com" "Mozilla/5.0" 30
192.168.1.20 - - [15/Oct/2023:10:15:45 +0000] "GET /api/orders HTTP/1.1" 500 890 "https://example.com" "Mozilla/5.0" 120
192.168.1.25 - - [15/Oct/2023:10:15:50 +0000] "GET /api/users HTTP/1.1" 200 1234 "https://example.com" "Mozilla/5.0" 28
192.168.1.10 - - [15/Oct/2023:10:15:55 +0000] "GET /api/products HTTP/1.1" 200 5678 "https://example.com" "Mozilla/5.0" 33
192.168.1.15 - - [15/Oct/2023:10:16:00 +0000] "GET /api/users HTTP/1.1" 200 1234 "https://example.com" "Mozilla/5.0" 45
192.168.1.30 - - [15/Oct/2023:10:16:05 +0000] "GET /api/settings HTTP/1.1" 403 567 "https://example.com" "Mozilla/5.0" 25
192.168.1.10 - - [15/Oct/2023:10:16:10 +0000] "GET /api/users HTTP/1.1" 200 1234 "https://example.com" "Mozilla/5.0" 38
192.168.1.15 - - [15/Oct/2023:10:16:15 +0000] "GET /api/products HTTP/1.1" 500 890 "https://example.com" "Mozilla/5.0" 150
EOF

# Create sample database query log
cat > ~/sre-advanced/logs/database.log << 'EOF'
[2023-10-15 10:15:29] [INFO] Connected: user=app1 database=userdb
[2023-10-15 10:15:30] [DEBUG] Query: SELECT * FROM users WHERE id = 123 time=15ms rows=1
[2023-10-15 10:15:32] [DEBUG] Query: SELECT * FROM users WHERE email LIKE '%example.com' time=120ms rows=250
[2023-10-15 10:15:35] [DEBUG] Query: UPDATE users SET last_login = NOW() WHERE id = 123 time=5ms rows=1
[2023-10-15 10:15:40] [WARNING] Slow query: SELECT * FROM products JOIN inventory ON products.id = inventory.product_id time=550ms rows=1500
[2023-10-15 10:15:45] [ERROR] Query failed: INSERT INTO orders (user_id, product_id, quantity) VALUES (123, 456, 1) - Foreign key constraint failed
[2023-10-15 10:15:50] [DEBUG] Query: SELECT * FROM users WHERE last_login > '2023-10-14' time=30ms rows=42
[2023-10-15 10:15:55] [DEBUG] Query: SELECT * FROM products WHERE category = 'electronics' time=25ms rows=38
[2023-10-15 10:16:00] [WARNING] Slow query: SELECT * FROM users JOIN orders ON users.id = orders.user_id time=320ms rows=5230
[2023-10-15 10:16:05] [DEBUG] Query: SELECT COUNT(*) FROM settings time=8ms rows=1
[2023-10-15 10:16:10] [DEBUG] Query: SELECT * FROM users WHERE id IN (123, 456, 789) time=12ms rows=3
[2023-10-15 10:16:15] [ERROR] Query failed: INSERT INTO products (name, price) VALUES ('Test Product', -10.99) - Check constraint failed
EOF
```

2. **Task 1: Analyze the Web Server Log**

```bash
# Extract all HTTP 500 errors
grep " 500 " ~/sre-advanced/logs/access.log

# Count requests by IP address
awk '{print $1}' ~/sre-advanced/logs/access.log | sort | uniq -c | sort -nr

# Calculate average response time per endpoint
awk '{gsub("/api/", "", $7); print $7}' ~/sre-advanced/logs/access.log | sort | uniq -c | sort -nr
awk '{gsub("/api/", "", $7); endpoint[$7] += $NF; count[$7]++} END {for (e in endpoint) print e, "avg:", endpoint[e]/count[e] "ms"}' ~/sre-advanced/logs/access.log | sort -k 3 -nr

# Find slowest requests (response time > 100ms)
awk '$NF > 100 {print $0}' ~/sre-advanced/logs/access.log
```

3. **Task 2: Analyze the Database Log**

```bash
# Extract all warnings and errors
grep -E "WARNING|ERROR" ~/sre-advanced/logs/database.log

# Find slow queries (> 100ms)
grep -o "time=[0-9]*ms" ~/sre-advanced/logs/database.log | awk -F'[=ms]' '$2 > 100 {print $0}'
sed -n '/Slow query\|time=[0-9]\{3,\}ms/p' ~/sre-advanced/logs/database.log

# Calculate average query time
grep "time=" ~/sre-advanced/logs/database.log | sed 's/.*time=\([0-9]*\)ms.*/\1/' | awk '{sum += $1; count++} END {print "Average query time:", sum/count "ms"}'

# Extract table names being accessed most frequently
grep -o "FROM [a-z_]*" ~/sre-advanced/logs/database.log | sort | uniq -c | sort -nr
```

4. **Task 3: Generate a Consolidated Report**

Create a summary report of the system status:

```bash
echo "System Performance Report - $(date)" > ~/sre-advanced/report.txt
echo "=======================================" >> ~/sre-advanced/report.txt

echo -e "\n1. API Request Distribution:" >> ~/sre-advanced/report.txt
awk '{gsub("/api/", "", $7); print $7}' ~/sre-advanced/logs/access.log | sort | uniq -c | sort -nr >> ~/sre-advanced/report.txt

echo -e "\n2. HTTP Error Codes:" >> ~/sre-advanced/report.txt
awk '{print $9}' ~/sre-advanced/logs/access.log | sort | uniq -c | sort -nr >> ~/sre-advanced/report.txt

echo -e "\n3. Top Clients by Request Count:" >> ~/sre-advanced/report.txt
awk '{print $1}' ~/sre-advanced/logs/access.log | sort | uniq -c | sort -nr >> ~/sre-advanced/report.txt

echo -e "\n4. Response Time Analysis:" >> ~/sre-advanced/report.txt
awk '{sum += $NF; count++} END {print "Average Response Time:", sum/count "ms"}' ~/sre-advanced/logs/access.log >> ~/sre-advanced/report.txt
awk '$NF > 100 {print $0}' ~/sre-advanced/logs/access.log | wc -l | awk '{print "Slow Responses (>100ms):", $1}' >> ~/sre-advanced/report.txt

echo -e "\n5. Database Errors:" >> ~/sre-advanced/report.txt
grep "ERROR" ~/sre-advanced/logs/database.log >> ~/sre-advanced/report.txt

echo -e "\n6. Database Performance:" >> ~/sre-advanced/report.txt
grep "time=" ~/sre-advanced/logs/database.log | sed 's/.*time=\([0-9]*\)ms.*/\1/' | awk '{sum += $1; count++} END {print "Average Query Time:", sum/count "ms"}' >> ~/sre-advanced/report.txt
grep -o "time=[0-9]*ms" ~/sre-advanced/logs/database.log | awk -F'[=ms]' '$2 > 100 {print $0}' | wc -l | awk '{print "Slow Queries (>100ms):", $1}' >> ~/sre-advanced/report.txt

# View the final report
cat ~/sre-advanced/report.txt
```

This exercise simulates a real SRE workflow where you analyze logs from multiple systems, extract meaningful metrics, and create a consolidated report to understand system health.

---

## 📝 **Quiz: Advanced Text Processing**

Test your understanding of today's material:

1. During a performance investigation, you need to replace all occurrences of "debug" with "DEBUG" in a log file but preserve the original file. Which command should you use?
   - a) `sed 's/debug/DEBUG/g' logfile.txt`
   - b) `sed -i 's/debug/DEBUG/g' logfile.txt`
   - c) `sed 's/debug/DEBUG/g' logfile.txt > logfile.txt`
   - d) `sed 's/debug/DEBUG/g' logfile.txt > logfile_modified.txt`

2. You're analyzing a CSV file with fields separated by commas and need to extract the third column. Which command is most appropriate?
   ```bash
   # Fill in the blank
   awk _______ '{print $3}' data.csv
   ```

3. To identify the top 5 most frequent error types in a log file where errors are formatted as "ERROR: [error_type]", which command pipeline would you use?
   - a) `grep "ERROR" application.log | cut -d' ' -f2 | sort | uniq -c`
   - b) `grep "ERROR" application.log | awk '{print $2}' | sort | uniq -c | sort -nr | head -5`
   - c) `grep "ERROR" application.log | sed 's/ERROR: \[\(.*\)\]/\1/' | sort | uniq -c | sort -nr | head -5`
   - d) `grep "ERROR" application.log | sort | head -5`

4. During capacity planning, you need to find directories consuming the most disk space and sort them by size. Which command pipeline is correct?
   - a) `du -h /var | sort -hr | head -10`
   - b) `find /var -type d | sort -hr | head -10`
   - c) `ls -la /var | sort -k 5 -nr | head -10`
   - d) `du -h /var | grep "^[0-9]G" | sort -hr`

5. You need to count the distribution of HTTP status codes in a web server log where the status code is the 9th field. Which command would you use?
   - a) `awk '{print $9}' access.log | sort`
   - b) `awk '{print $9}' access.log | sort | uniq`
   - c) `awk '{print $9}' access.log | sort | uniq -c`
   - d) `awk '{print $9}' access.log | sort | uniq -c | sort -nr`

---

## ❓ **FAQ for SREs: Advanced Text Processing**

**Q1: How can I modify files in-place safely with `sed`?**

**A:** When performing in-place edits with `sed -i`, follow these safety practices:

```bash
# Create a backup with extension .bak
sed -i.bak 's/old/new/g' config.file

# Test changes before applying
sed 's/old/new/g' config.file | diff -u config.file -

# Use version control when possible
git commit -am "Before sed changes"
sed -i 's/old/new/g' config.file
git diff  # Review changes

# For critical files, consider writing to a new file first
sed 's/old/new/g' critical_config.file > critical_config.file.new
# Review changes
mv critical_config.file.new critical_config.file
```

**Q2: How do I handle complex multi-line patterns?**

**A:** For multi-line processing:

```bash
# With sed, use N to append next line to pattern space
sed '/START/{N;N;s/START.*END/REPLACED/}' file.txt

# For more complex patterns, consider using awk with multi-line record processing
awk 'BEGIN {RS=""; FS="\n"} /pattern across\nmultiple lines/ {print $0}' file.txt

# Or use Perl for the most complex cases (if available)
perl -0777 -ne 'print "$1\n" while /start(.*?)end/gs' file.txt
```

**Q3: How do I process very large log files without causing memory issues?**

**A:** For large files:

```bash
# Stream processing instead of loading the whole file
grep "pattern" large_file.log | awk '{process only what you need}'

# Split the file for parallel processing
split -l 1000000 huge_file.log segment_
for f in segment_*; do
  grep "pattern" $f | process_further >> results.txt &
done
wait

# Use head/tail to process just portions of the file
head -n 1000000 huge_file.log | grep "pattern"
```

**Q4: What's the best way to process JSON logs on the command line?**

**A:** For JSON data:

```bash
# Install jq if not already available
# sudo apt install jq  # Debian/Ubuntu
# sudo yum install jq  # RHEL/CentOS

# Extract specific fields
cat logs.json | jq '.field1'

# Filter by conditions
cat logs.json | jq 'select(.status_code >= 500)'

# Create new JSON structures
cat logs.json | jq '{service: .service, error: .error_message, time: .timestamp}'

# For basic extraction without jq, you can sometimes use grep and awk:
grep -o '"error_message":"[^"]*"' logs.txt | awk -F':' '{print $2}' | tr -d '"'
```

---

## 🚧 **Common Issues and Troubleshooting**

### **Issue 1: Text Processing Commands Producing Unexpected Output**

**Possible causes:**
- Regular expression syntax errors
- Field numbering confusion
- Delimiter mismatches
- Special characters not escaped

**Solutions:**
```bash
# Test regular expressions incrementally
grep "part1" file.txt
grep "part1.*part2" file.txt

# For complex sed operations, test each part separately
sed 's/pattern/replacement/' file.txt  # Test basic replacement
sed -n '/pattern/p' file.txt  # Test pattern matching

# For awk field issues, print field numbers to debug
awk '{print "Field 1: [" $1 "]", "Field 2: [" $2 "]"}' file.txt

# Visualize delimiters and whitespace
cat -A file.txt  # Show all characters including invisible ones
```

### **Issue 2: Performance Problems with Text Processing Pipelines**

**Possible causes:**
- Inefficient regular expressions
- Multiple passes over large files
- Unnecessary sorting or processing

**Solutions:**
```bash
# Use grep to filter data early in the pipeline
grep "relevant" huge_file.log | awk '{complex processing}'  # Better
# vs.
awk '/relevant/ {complex processing}' huge_file.log  # Less efficient for simple patterns

# Combine multiple sed/awk operations
awk '{gsub(/pattern1/, "replacement1"); gsub(/pattern2/, "replacement2"); print}' file.txt  # Better
# vs.
sed 's/pattern1/replacement1/g' file.txt | sed 's/pattern2/replacement2/g'  # Less efficient

# Use monitoring tools to identify bottlenecks
time grep "pattern" large_file.log | awk '{print $1}' | sort | uniq -c
```

---

## 🔄 **Real-World SRE Scenario: Performance Degradation Analysis**

**Situation:** Users are reporting increased response times. You need to analyze logs from multiple services to pinpoint the cause and quantify the impact.

**SRE Response Using Today's Commands:**

1. Check for increased error rates in application logs:
   ```bash
   grep "ERROR\|WARN" /var/log/application/*.log | awk '{print $1, $2}' | cut -d: -f1 | sort | uniq -c
   ```

2. Analyze response time trends:
   ```bash
   # Extract timestamp and response time
   awk '{print $4, $NF}' /var/log/nginx/access.log > /tmp/response_times.txt
   
   # Calculate average response time per minute
   sed 's/\[//g' /tmp/response_times.txt | awk -F'[ :]' '{print $1 ":" $2 ":" int($3/10)*10; rt[$1 ":" $2 ":" int($3/10)*10] += $4; count[$1 ":" $2 ":" int($3/10)*10]++} END {for (t in rt) print t, rt[t]/count[t]}' | sort
   ```

3. Identify slow database queries:
   ```bash
   grep -o "Query: .* time=[0-9]*ms" /var/log/mysql/mysql_slow.log | 
   sed 's/.*Query: \(.*\) time=\([0-9]*\)ms/\2 \1/' | 
   sort -nr | 
   head -10
   ```

4. Check for resource constraints:
   ```bash
   # Extract CPU% and memory usage by service
   ps aux | grep -v "grep\|ps aux" | awk '{print $2, $3, $4, $11}' | sort -k3 -nr > /tmp/resource_usage.txt
   
   # Find processes consuming most CPU
   head -10 /tmp/resource_usage.txt
   ```

5. Analyze network connections:
   ```bash
   # Connection count by state
   netstat -ant | awk '{print $6}' | sort | uniq -c
   
   # Connection count by remote IP
   netstat -ant | grep ESTABLISHED | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr | head -10
   ```

6. Create a summary report:
   ```bash
   {
     echo "Performance Degradation Analysis - $(date)"
     echo "========================================"
     
     echo -e "\n1. Error Rates:"
     grep -c "ERROR\|WARN" /var/log/application/*.log | sort -t: -k2 -nr
     
     echo -e "\n2. Top 5 Slowest Endpoints:"
     awk '{print $7, $NF}' /var/log/nginx/access.log | sort -k2 -nr | head -5
     
     echo -e "\n3. Database Query Analysis:"
     grep -o "Query: .* time=[0-9]*ms" /var/log/mysql/mysql_slow.log | sed 's/.*Query: \(.*\) time=\([0-9]*\)ms/\2 \1/' | sort -nr | head -5
     
     echo -e "\n4. Resource Utilization:"
     head -10 /tmp/resource_usage.txt
     
     echo -e "\n5. Connection States:"
     netstat -ant | awk '{print $6}' | sort | uniq -c
   } > /tmp/performance_report.txt
   
   cat /tmp/performance_report.txt
   ```

This scenario demonstrates how SREs combine text processing tools to quickly identify the root causes of performance problems by analyzing data from multiple sources in a systematic way.

---

## 🔧 **Advanced SRE Text Processing Techniques**

### **1. Correlation Analysis Across Multiple Logs**

When dealing with microservices, correlating events across different logs is essential:

```bash
# Extract request IDs from multiple log files
grep -o "request_id=[a-f0-9-]*" /var/log/service1.log | sort > /tmp/service1_requests.txt
grep -o "request_id=[a-f0-9-]*" /var/log/service2.log | sort > /tmp/service2_requests.txt

# Find common request IDs (requests that touched both services)
comm -12 /tmp/service1_requests.txt /tmp/service2_requests.txt > /tmp/common_requests.txt

# Find requests that appear in service1 but not service2 (potential points of failure)
comm -23 /tmp/service1_requests.txt /tmp/service2_requests.txt > /tmp/incomplete_requests.txt

# Extract full log entries for failed requests
while read request; do
  echo "=== $request ==="
  grep "$request" /var/log/service1.log /var/log/service2.log
  echo ""
done < /tmp/incomplete_requests.txt > /tmp/failure_analysis.txt
```

### **2. Performance Optimization for Large-Scale Log Analysis**

For production systems with gigabytes of logs:

```bash
# Pre-filter with grep before complex processing
grep --binary-files=text "ERROR" /var/log/huge.log | awk '{print $4, $5, $6}'

# Use efficient regex patterns
# Bad: grep ".*error.*" huge.log  # Backtracking can be slow
# Good: grep "error" huge.log     # Much faster

# Process logs in chunks
split -l 1000000 huge.log chunk_
for chunk in chunk_*; do
  awk '{process}' $chunk > $chunk.processed &
done
wait
cat chunk_*.processed > results.txt
rm chunk_*

# Use parallel processing where possible
grep "pattern" huge.log | parallel --pipe -N1000 'awk "{print \$1, \$4}"' > results.txt
```

### **3. Automated Configuration Auditing**

Create scripts to validate configurations across servers:

```bash
# Compare enabled modules across multiple web servers
for server in web1 web2 web3; do
  ssh $server "apache2ctl -M | sort" > /tmp/$server-modules.txt
done

# Find differences
diff -y /tmp/web1-modules.txt /tmp/web2-modules.txt
diff -y /tmp/web1-modules.txt /tmp/web3-modules.txt

# Check for security misconfigurations
for server in app1 app2 app3; do
  echo "=== $server ==="
  ssh $server "grep -E 'password|auth|ssl|security' /etc/app/*.conf" | sort
done > /tmp/security_audit.txt
```

### **4. Continuous Monitoring Scripts**

Create simple scripts for real-time monitoring:

```bash
# Monitor error rates in production logs
while true; do
  now=$(date "+%Y-%m-%d %H:%M:%S")
  errors=$(grep -c "ERROR" /var/log/application.log)
  echo "$now $errors" >> /tmp/error_trend.log
  sleep 60
done

# Generate cumulative metrics report every hour
0 * * * * {
  echo "Hourly System Health Check - $(date)"
  echo "===================================="
  
  echo "Error Count (Last Hour):"
  grep "ERROR" /var/log/application.log | grep -c "$(date '+%Y-%m-%d %H:')"
  
  echo "Average Response Time (Last Hour):"
  grep "$(date '+%Y-%m-%d %H:')" /var/log/nginx/access.log | awk '{sum+=$NF; count++} END {print sum/count "ms"}'
  
  echo "Current DB Connection Count:"
  mysql -u monitor -p'password' -e "SHOW STATUS LIKE 'Threads_connected';" | grep -v Variable_name
  
  echo "Top 5 Resource-Intensive Processes:"
  ps aux --sort=-%cpu | head -6
} > /var/log/hourly_health/$(date '+%Y%m%d%H').txt
```

---

## 📚 **Further Learning Resources**

- [Practical Sed & Awk for SREs](https://developer.ibm.com/tutorials/l-sed-awk/)
- [Advanced Text Processing with Grep, Sed, and Awk](https://www.redhat.com/sysadmin/advanced-text-processing)
- [The AWK Programming Language Book](https://ia803404.us.archive.org/25/items/pdfy-MgN0H1joIoDVoIC7/The_AWK_Programming_Language.pdf)
- [Google SRE Book - Chapter 18: Software Engineering in SRE](https://sre.google/sre-book/software-engineering-in-sre/)
- [Modern Linux CLI Tools for Development and Operations](https://github.com/ibraheemdev/modern-unix)

---

🎓 **Day 5 completed!** Tomorrow, we'll explore process management and system monitoring, giving you the tools to observe and control Linux system behavior in real-time—essential skills for managing and troubleshooting production systems.
