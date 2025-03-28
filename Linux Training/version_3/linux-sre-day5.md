# 🚀 **Day 5: Advanced Text Processing for SRE - sed, awk, sort, uniq, and Data Transformation**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 4:**

Yesterday, you learned essential text processing and searching tools including `grep` for pattern matching, `find` for locating files, pipes (`|`) for command chaining, and redirection operators (`>`, `>>`, `<`) for controlling input and output. These skills enable you to search through logs, find specific files, and create basic data processing pipelines.

### 📅 **Today's Topics and Importance:**

Today, we're advancing to more powerful text processing tools: **`sed`**, **`awk`**, **`sort`**, **`uniq`**, and **`wc`**. For SREs, these tools are invaluable because they allow you to:

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
- Count lines, words, and characters with `wc`
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

**Beginner's Note**: Think of text processing as having a toolbox where each tool does one job extremely well. Rather than having a single complicated Swiss Army knife, Unix/Linux gives you specialized tools that you can combine in creative ways.

**SRE Perspective**: By treating everything as text and providing modular tools that process text streams, Unix/Linux creates a consistent interface for working with all these different types of data. This is why SREs can apply the same skills to analyze logs, modify configurations, and extract metrics across different systems.

### **Stream Processing vs. Batch Processing**

The tools you'll learn today operate as **stream processors**—they process data line by line as it flows through a pipeline. This approach:

- Scales efficiently to very large files
- Uses minimal memory
- Works well in pipelines with other commands
- Enables real-time processing

**Beginner's Note**: Think of stream processing like an assembly line in a factory. Each piece (line of text) moves down the line, getting processed by different stations (commands) as it goes.

**SRE Perspective**: This contrasts with graphical tools or full-featured programming languages, which often load entire files into memory. For an SRE managing systems with gigabytes of logs or thousands of configuration files, stream processing is essential.

---

## 💻 **Commands to Learn Today**

### **1. sed – Stream Editor**

**Purpose**: Perform text transformations on a stream of text (substitutions, deletions, insertions).

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

**Basic Examples:**

Replace text in a file:

```bash
sed 's/error/ERROR/' logfile.txt
```

Replace all occurrences on each line:

```bash
sed 's/error/ERROR/g' logfile.txt
```

**Intermediate Examples:**

Delete lines containing "DEBUG":

```bash
sed '/DEBUG/d' application.log
```

Edit a file in place (make changes to the file):

```bash
sed -i 's/http:/https:/g' urls.txt
```

Print lines matching a pattern:

```bash
sed -n '/ERROR/p' application.log
```

**SRE Examples:**

Remove all comment lines from a configuration file:

```bash
sed '/^#/d' /etc/nginx/nginx.conf
```

Extract a specific section from a config file:

```bash
sed -n '/^server {/,/^}/p' /etc/nginx/nginx.conf
```

Modify a configuration value:

```bash
sed -i 's/max_connections = 100/max_connections = 200/g' postgres.conf
```

**SRE Context**: Used for modifying configuration files, transforming log formats, and preparing data for analysis. During deployments or configuration changes, `sed` allows you to make precise, automated edits to files.

**Beginner's Tip**: Think of `sed` as a find-and-replace tool that works on text streams. The "s" command (substitute) is the most commonly used.

### **2. awk – Pattern Scanning and Processing**

**Purpose**: Process text files by fields, allowing for complex data extraction and manipulation.

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

**Basic Examples:**

Print the first field (column) of each line:

```bash
awk '{print $1}' names.txt
```

Print specific fields:

```bash
awk '{print $2, $4}' data.txt
```

**Intermediate Examples:**

Print lines containing a pattern:

```bash
awk '/error/{print}' logfile.txt
```

Use a custom field separator:

```bash
awk -F, '{print $1, $3}' data.csv
```

**SRE Examples:**

Extract specific columns from command output:

```bash
ps aux | awk '{print $2, $4, $11}'  # PID, %MEM, COMMAND
```

Calculate average response time from logs:

```bash
awk '{ sum += $7; count++ } END { print "Average:", sum/count "ms" }' access.log
```

Filter logs by field conditions:

```bash
awk '$4 > 300 {print}' response_times.log  # Responses over 300ms
```

Generate a report of HTTP status code distribution:

```bash
awk '{ codes[$9]++ } END { for (code in codes) print code, codes[code] }' access.log
```

**SRE Context**: Ideal for analyzing structured logs, extracting specific metrics, and creating reports from command outputs. `awk` is particularly valuable for extracting meaningful information from complex data sources.

**Beginner's Tip**: `awk` is powerful because it automatically splits lines into fields, making it easy to extract columns of data.

### **3. sort – Sort Lines of Text**

**Purpose**: Sort text input by various criteria.

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

**Basic Examples:**

Sort a file alphabetically:

```bash
sort names.txt
```

Sort numerically:

```bash
sort -n numbers.txt
```

**Intermediate Examples:**

Sort in reverse order:

```bash
sort -r names.txt
```

Sort by a specific column:

```bash
sort -k 2 data.txt
```

**SRE Examples:**

Sort processes by memory usage (highest first):

```bash
ps aux | sort -k 4 -r
```

Sort by specific delimited field:

```bash
sort -t',' -k 3 -n csv_data.txt  # Sort by 3rd column, numeric
```

Sort IP addresses correctly:

```bash
sort -t . -k 1,1n -k 2,2n -k 3,3n -k 4,4n ip_addresses.txt
```

Sort by human-readable sizes:

```bash
du -h | sort -hr
```

**SRE Context**: Used for organizing data for analysis, preparing data for deduplication, and creating readable reports. When investigating incidents, sorting helps identify patterns and outliers.

**Beginner's Tip**: By default, `sort` uses alphabetical ordering, which can give unexpected results with numbers (e.g., "10" comes before "2"). Use the `-n` option for numerical sorting.

### **4. uniq – Report or Omit Repeated Lines**

**Purpose**: Filter or report repeated lines in a sorted file.

**Syntax:**

```bash
uniq [options] [input [output]]
```

**Important note**: `uniq` only detects adjacent duplicate lines, so input typically needs to be sorted first.

**Common options:**

- `-c`: Prefix lines with count of occurrences
- `-d`: Only print duplicate lines
- `-u`: Only print unique lines (not duplicated)

**Basic Examples:**

Remove duplicate lines (must be sorted first):

```bash
sort names.txt | uniq
```

Count occurrences of each line:

```bash
sort names.txt | uniq -c
```

**Intermediate Examples:**

Show only duplicate lines:

```bash
sort names.txt | uniq -d
```

Show only unique lines (not duplicated):

```bash
sort names.txt | uniq -u
```

**SRE Examples:**

Count occurrences of HTTP status codes:

```bash
awk '{print $9}' access.log | sort | uniq -c | sort -nr
```

Find the most frequent error messages:

```bash
grep "ERROR" application.log | sort | uniq -c | sort -nr | head -10
```

Identify unique IP addresses accessing a service:

```bash
awk '{print $1}' access.log | sort | uniq
```

**SRE Context**: Used for identifying unique events, counting occurrences, and detecting patterns in logs. Crucial for understanding system behavior and identifying anomalies.

**Beginner's Tip**: Remember that `uniq` requires sorted input to work correctly, as it only identifies adjacent duplicate lines.

### **5. wc – Word Count**

**Purpose**: Count lines, words, and characters in a file.

**Syntax:**

```bash
wc [options] [file...]
```

**Common options:**

- `-l`: Count lines only
- `-w`: Count words only
- `-c`: Count bytes only
- `-m`: Count characters only

**Basic Examples:**

Count lines, words, and characters:

```bash
wc filename.txt
```

Count only lines:

```bash
wc -l filename.txt
```

**Intermediate Examples:**

Count words in multiple files:

```bash
wc -w file1.txt file2.txt
```

Count lines in all text files:

```bash
wc -l *.txt
```

**SRE Examples:**

Count the number of error messages:

```bash
grep "ERROR" application.log | wc -l
```

Monitor the growth of a log file:

```bash
watch "wc -l /var/log/application.log"
```

Count total requests received:

```bash
wc -l /var/log/nginx/access.log
```

**SRE Context**: Useful for quick metrics and status checks. Often combined with other commands to count specific types of events.

**Beginner's Tip**: The default output of `wc` shows lines, words, and characters (in that order). Use specific options like `-l` when you only need one value.

### **6. Combining Commands: Advanced Pipelines**

The true power of these tools emerges when you combine them into data processing pipelines:

**Basic Examples:**

Count unique usernames:

```bash
cut -d, -f1 users.csv | sort | uniq | wc -l
```

Find and replace text, then count occurrences:

```bash
sed 's/error/ERROR/g' log.txt | grep "ERROR" | wc -l
```

**Intermediate Examples:**

Extract unique IP addresses from a log:

```bash
grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' access.log | sort | uniq
```

Find top 5 visitors to a website:

```bash
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -5
```

**SRE Examples:**

Analyze HTTP status code distribution in logs:

```bash
awk '{print $9}' access.log | sort | uniq -c | sort -nr
```

Find the top 5 IP addresses making the most requests:

```bash
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -5
```

Calculate the percentage of error responses:

```bash
awk 'BEGIN{total=0; errors=0} {total++; if($9 >= 500) errors++} END{print "Error rate:", (errors/total)*100 "%"}' access.log
```

Identify slow database queries and format a report:

```bash
grep "SLOW QUERY" mysql.log | sed 's/SLOW QUERY: //' | awk -F' time=' '{print $2, $1}' | sort -nr | head -10
```

**SRE Context**: Advanced pipelines allow for sophisticated data analysis without writing complex programs. This is essential for rapid incident response and ad-hoc investigations.

**Beginner's Tip**: Start with simple pipelines and gradually add more components as you become comfortable. Each command in the pipeline performs a specific transformation on the data.

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

## 🎯 **Practical Exercises: From Beginner to SRE**

### **Beginner Exercises**

1. Create a file called `names.txt` with several duplicate names (one per line).
2. Use `sort` and `uniq` to create a file with only unique names:

   ```bash
   sort names.txt | uniq > unique_names.txt
   ```

3. Count how many unique names exist:

   ```bash
   wc -l unique_names.txt
   ```

4. Create a file with some text, including the word "error" multiple times.
5. Use `sed` to replace all instances of "error" with "ERROR":

   ```bash
   sed 's/error/ERROR/g' textfile.txt
   ```

6. Count the number of lines and words in a file using `wc`:

   ```bash
   wc -l textfile.txt  # Count lines
   wc -w textfile.txt  # Count words
   ```

### **Intermediate Exercises**

1. Create a CSV file with name,email,department structure:

   ```bash
   cat > employees.csv << 'EOF'
   John,john@example.com,Engineering
   Sarah,sarah@example.com,Marketing
   Mike,mike@example.com,Engineering
   Lisa,lisa@example.com,HR
   David,david@example.com,Engineering
   Emma,emma@example.com,Marketing
   EOF
   ```

2. Extract all email addresses:

   ```bash
   awk -F, '{print $2}' employees.csv
   ```

3. Count employees by department:

   ```bash
   awk -F, '{print $3}' employees.csv | sort | uniq -c
   ```

4. Create a tab-separated file and process it with different field separators:

   ```bash
   cat > data.tsv << 'EOF'
   Name Score Grade
   John 85 B
   Sarah 92 A
   Mike 78 C
   Lisa 95 A
   EOF
   
   # Extract names and grades
   awk -F'\t' '{print $1, $3}' data.tsv
   ```

5. Use `sed` to extract specific sections from a text file:

   ```bash
   cat > report.txt << 'EOF'
   === System Performance ===
   CPU: 45% utilized
   Memory: 3.2GB/8GB
   Disk: 65% full
   
   === Network Status ===
   Connections: 234 active
   Bandwidth: 45Mbps
   Latency: 15ms
   EOF
   
   # Extract just the Network section
   sed -n '/=== Network Status ===/,/EOF/p' report.txt
   ```

### **SRE Application Exercises**

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

# View the final report
cat ~/sre-advanced/report.txt
```

---

## 📝 **Quiz: Test Your Knowledge**

### **Beginner Level**

1. How would you replace all instances of "linux" with "Linux" in a file called `notes.txt`?
   - a) `sed 's/Linux/linux/g' notes.txt`
   - b) `sed 's/linux/Linux/g' notes.txt`
   - c) `sed -i 's/linux/Linux/' notes.txt`
   - d) `awk '{gsub("linux", "Linux"); print}' notes.txt`

2. Which command counts the number of lines in a file?
   - a) `wc -w file.txt`
   - b) `wc -l file.txt`
   - c) `wc -c file.txt`
   - d) `wc -m file.txt`

3. How do you sort a file called `numbers.txt` in numerical order?
   - a) `sort numbers.txt`
   - b) `sort -n numbers.txt`
   - c) `sort -r numbers.txt`
   - d) `sort -h numbers.txt`

### **Intermediate Level**

4. To print only the second and third fields from a space-delimited file, which command would you use?
   - a) `awk '{print $2, $3}' data.txt`
   - b) `awk '{print 2,3}' data.txt`
   - c) `sed -n '2,3p' data.txt`
   - d) `cut -f 2,3 data.txt`

5. Which command sorts data in reverse numerical order?
   - a) `sort -n file.txt`
   - b) `sort -nr file.txt`
   - c) `sort -r file.txt`
   - d) `sort -rn file.txt`

6. How do you count the number of unique lines in a file?
   - a) `uniq -c file.txt | wc -l`
   - b) `sort file.txt | uniq | wc -l`
   - c) `sort file.txt | uniq -c | wc -l`
   - d) `wc -l file.txt | uniq`

### **SRE Application Level**

7. During a performance investigation, you need to replace all occurrences of "debug" with "DEBUG" in a log file but preserve the original file. Which command should you use?
   - a) `sed 's/debug/DEBUG/g' logfile.txt`
   - b) `sed -i 's/debug/DEBUG/g' logfile.txt`
   - c) `sed 's/debug/DEBUG/g' logfile.txt > logfile.txt`
   - d) `sed 's/debug/DEBUG/g' logfile.txt > logfile_modified.txt`

8. To identify the top 5 most frequent error types in a log file where errors are formatted as "ERROR: [error_type]", which command pipeline would you use?
   - a) `grep "ERROR" application.log | cut -d' ' -f2 | sort | uniq -c`
   - b) `grep "ERROR" application.log | awk '{print $2}' | sort | uniq -c | sort -nr | head -5`
   - c) `grep "ERROR" application.log | sed 's/ERROR: \[\(.*\)\]/\1/' | sort | uniq -c | sort -nr | head -5`
   - d) `grep "ERROR" application.log | sort | head -5`

9. You need to count the distribution of HTTP status codes in a web server log where the status code is the 9th field. Which command would you use?
   - a) `awk '{print $9}' access.log | sort`
   - b) `awk '{print $9}' access.log | sort | uniq`
   - c) `awk '{print $9}' access.log | sort | uniq -c`
   - d) `awk '{print $9}' access.log | sort | uniq -c | sort -nr`

---
