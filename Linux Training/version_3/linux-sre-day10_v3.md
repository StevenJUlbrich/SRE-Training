# 🚀 **Day 10: Shell Scripting Basics & Automation**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 9:**

Yesterday, you learned about archiving, compression, and package management. You mastered tools like `tar`, `gzip`, and `zip` for bundling and compressing files, as well as package managers (`apt`, `yum`, `dpkg`, `rpm`) for installing and maintaining software. These skills enable you to efficiently manage files and software across Linux systems.

### 📅 **Today's Topics and Importance:**

Today marks the final day of your intensive Linux course, focusing on **shell scripting**. This topic is essential because:

- It allows you to automate repetitive tasks, saving time and reducing human error
- It enables consistent execution of complex operations across systems
- It forms the foundation for system administration, maintenance, and deployment tasks
- It's a fundamental skill for both Linux administrators and SREs (Site Reliability Engineers)

By learning shell scripting, you'll transform your collection of individual Linux commands into powerful automation workflows.

### 🎯 **Learning Objectives:**

By the end of Day 10, you will be able to:

- Create and run basic shell scripts
- Use variables and environment variables
- Implement conditional logic with `if` statements
- Create loops for repetitive tasks
- Process command line arguments
- Use command substitution to capture output
- Apply basic error handling in scripts
- Customize your shell environment

---

## 📚 **Core Concepts Explained**

### **What is Shell Scripting?**

> **Beginner's Note:** Think of shell scripting as writing a list of instructions for your computer to follow automatically, much like a recipe.

Shell scripting is a way to automate command sequences that you would normally type at the command line. A shell script is simply a text file containing a series of commands that the shell can execute.

The primary shell we'll focus on is **Bash** (Bourne Again SHell), which is the default on most Linux distributions. However, the concepts apply to other shells like Zsh or Dash with minor syntax differences.

> **Intermediate Insight:** Shell scripts bridge the gap between simple command line usage and full programming languages. While not as powerful as Python or Ruby, shell scripts excel at system tasks, file operations, and command automation with minimal overhead.

> **SRE Perspective:** For SREs, shell scripting is a cornerstone skill for reducing toil (manual, repetitive work). Scripts can automate routine checks, deployments, and recovery procedures, increasing reliability and freeing up time for more strategic work.

---

## 💻 **Shell Scripting Essentials**

### **1. Creating and Running Basic Scripts (Beginner Level)**

To create your first script:

1. Create a file with a `.sh` extension:

   ```bash
   touch myscript.sh
   ```

2. Edit the file and add the shebang line (which specifies the interpreter):

   ```bash
   #!/bin/bash
   
   # My first shell script
   echo "Hello, World!"
   echo "Current date: $(date)"
   ```

3. Make the script executable:

   ```bash
   chmod +x myscript.sh
   ```

4. Run the script:

   ```bash
   ./myscript.sh
   ```

> **Beginner's Note:** The first line `#!/bin/bash` tells the system to use the Bash shell to interpret the script. This line is called the "shebang" line.

### **2. Variables (Beginner Level)**

Variables store data that you can reference later in your script.

**Assigning and Using Variables:**

```bash
#!/bin/bash

# Assign variables (no spaces around equals sign)
name="John"
age=30
current_date=$(date)

# Use variables by prefixing with $
echo "Hello, $name!"
echo "You are $age years old."
echo "Today is $current_date"
```

> **Beginner's Note:** Always avoid spaces around the equals sign when assigning variables. `name="John"` works, but `name = "John"` will cause an error.

### **3. Conditionals with `if` Statements (Beginner Level)**

Conditionals let your script make decisions based on conditions.

**Basic If-Else Structure:**

```bash
#!/bin/bash

username="admin"

if [ "$username" = "admin" ]; then
    echo "Welcome, administrator!"
else
    echo "Welcome, user!"
fi
```

**Checking File Existence:**

```bash
#!/bin/bash

filename="config.txt"

if [ -f "$filename" ]; then
    echo "$filename exists."
else
    echo "$filename does not exist."
    touch "$filename"
    echo "Created $filename."
fi
```

> **Beginner's Note:** Common file test operators:
> - `-f file`: True if file exists and is a regular file
> - `-d file`: True if file exists and is a directory
> - `-e file`: True if file exists (any type)
> - `-r file`: True if file exists and is readable
> - `-w file`: True if file exists and is writable
> - `-x file`: True if file exists and is executable

### **4. Loops (Beginner Level)**

Loops allow you to repeat actions multiple times.

**For Loop Through Items:**

```bash
#!/bin/bash

# Loop through a list of items
for fruit in apple banana orange; do
    echo "I like $fruit"
done
```

**For Loop Through Files:**

```bash
#!/bin/bash

# Loop through all text files in current directory
for file in *.txt; do
    echo "Processing $file"
    wc -l "$file"
done
```

**Numerical For Loop:**

```bash
#!/bin/bash

# Count from 1 to 5
for i in {1..5}; do
    echo "Number: $i"
done
```

> **Beginner's Note:** The `for` loop is perfect for iterating through files, directories, or any list of items.

---

## **Intermediate Shell Scripting Concepts**

### **1. Command Line Arguments (Intermediate Level)**

Scripts can accept input through command line arguments.

```bash
#!/bin/bash

# $0 is the script name
# $1, $2, etc. are the arguments
# $# is the number of arguments
# $@ is all arguments

echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Number of arguments: $#"
echo "All arguments: $@"

if [ $# -lt 2 ]; then
    echo "Usage: $0 <source_dir> <destination_dir>"
    exit 1
fi
```

Running the script:

```bash
./script.sh /path/to/source /path/to/destination
```

> **Intermediate Insight:** Using command line arguments makes scripts more flexible and reusable. Check the number of arguments with `$#` to ensure the script has all the information it needs.

### **2. Environment Variables (Intermediate Level)**

Environment variables store system-wide information.

```bash
#!/bin/bash

# Reading environment variables
echo "Current user: $USER"
echo "Home directory: $HOME"
echo "Current shell: $SHELL"

# Setting an environment variable
export MY_VARIABLE="custom value"
echo "Custom variable: $MY_VARIABLE"
```

> **Intermediate Insight:** Environment variables like `PATH`, `HOME`, and `USER` are available to all processes. Use `export` to make a variable available to child processes.

### **3. Input and Output (Intermediate Level)**

You can redirect output to files and read input from the user.

```bash
#!/bin/bash

# Write output to a file
echo "Log entry: $(date)" > logfile.txt
echo "Additional information" >> logfile.txt  # Append to file

# Read input from user
echo "Enter your name:"
read username
echo "Hello, $username!"

# Read password (hidden input)
echo "Enter password:"
read -s password
echo "Password received."
```

> **Intermediate Insight:** Use `>` to overwrite a file, `>>` to append to a file. The `read` command captures user input, and the `-s` flag hides the input (useful for passwords).

### **4. Functions (Intermediate Level)**

Functions allow you to group commands for reuse.

```bash
#!/bin/bash

# Define a function
greet() {
    local name=$1  # Local variable, only visible in this function
    echo "Hello, $name!"
}

# Function to check if a file exists
check_file() {
    if [ -f "$1" ]; then
        echo "File $1 exists."
        return 0  # Success return code
    else
        echo "File $1 does not exist."
        return 1  # Error return code
    fi
}

# Call the functions
greet "Alice"
greet "Bob"

check_file "/etc/hosts"
if [ $? -eq 0 ]; then
    echo "File check succeeded."
fi
```

> **Intermediate Insight:** Use `local` for function-scoped variables to avoid conflicts with global variables. Functions can return status codes (0-255) using the `return` statement, where 0 typically indicates success.

### **5. Error Handling (Intermediate Level)**

Proper error handling makes scripts more robust.

```bash
#!/bin/bash

# Exit immediately if any command fails
set -e

# Custom error handler
handle_error() {
    echo "Error occurred at line $1"
    exit 1
}

# Trap errors and call error handler with line number
trap 'handle_error $LINENO' ERR

# Check for required commands
if ! command -v curl &> /dev/null; then
    echo "Error: curl is not installed"
    exit 1
fi

# Function to safely execute commands
execute_cmd() {
    echo "Running: $@"
    if ! "$@"; then
        echo "Command failed: $@"
        exit 1
    fi
}

# Use the function for risky operations
execute_cmd mkdir -p /tmp/safedir
execute_cmd cp -r /etc/hosts /tmp/safedir/

echo "Script completed successfully"
```

> **Intermediate Insight:** The `set -e` option makes the script exit if any command fails. The `trap` command lets you catch errors and execute custom code. Always check for required commands and handle possible failures.

---

## **Advanced Shell Scripting for SREs**

### **1. Monitoring and Health Checks (SRE Application)**

SREs often create scripts to monitor system health.

```bash
#!/bin/bash

# System health check script
# Checks disk space, memory usage, and critical services

LOG_FILE="/var/log/health_check.log"
THRESHOLD_DISK=90  # Alert if disk usage over 90%
THRESHOLD_MEM=80   # Alert if memory usage over 80%
CRITICAL_SERVICES="nginx mysql postgresql"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

check_disk_space() {
    log "Checking disk space..."
    local disk_usage=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')
    
    if [ "$disk_usage" -gt "$THRESHOLD_DISK" ]; then
        log "WARNING: Disk usage is at ${disk_usage}%"
        return 1
    else
        log "Disk usage is at ${disk_usage}%"
        return 0
    fi
}

check_memory() {
    log "Checking memory usage..."
    local mem_usage=$(free | grep Mem | awk '{print int($3 / $2 * 100)}')
    
    if [ "$mem_usage" -gt "$THRESHOLD_MEM" ]; then
        log "WARNING: Memory usage is at ${mem_usage}%"
        return 1
    else
        log "Memory usage is at ${mem_usage}%"
        return 0
    fi
}

check_services() {
    log "Checking critical services..."
    local failed_services=""
    
    for service in $CRITICAL_SERVICES; do
        if ! systemctl is-active --quiet "$service"; then
            failed_services+="$service "
        fi
    done
    
    if [ -n "$failed_services" ]; then
        log "WARNING: The following services are not running: $failed_services"
        return 1
    else
        log "All critical services are running"
        return 0
    fi
}

# Main health check
log "Starting health check"

errors=0
check_disk_space || ((errors++))
check_memory || ((errors++))
check_services || ((errors++))

if [ "$errors" -eq 0 ]; then
    log "All systems nominal"
else
    log "Health check found $errors issues"
    # Could send email or other notification here
fi

log "Health check completed"
```

> **SRE Perspective:** Monitoring scripts should be designed to run regularly via cron jobs, report clear metrics, and provide actionable alerts. This script could be enhanced to send notifications via email, Slack, or integrate with monitoring systems like Prometheus.

### **2. Log Analysis and Reporting (SRE Application)**

Automating log analysis is a common SRE task.

```bash
#!/bin/bash

# Log analysis script
# Analyzes web server logs for errors and generates a report

LOG_FILE="/var/log/nginx/access.log"
REPORT_FILE="/var/log/reports/daily_report_$(date +%Y%m%d).txt"
ERROR_THRESHOLD=50  # Alert if more than 50 errors

mkdir -p "$(dirname "$REPORT_FILE")"

echo "=== Web Server Log Analysis ===" > "$REPORT_FILE"
echo "Date: $(date)" >> "$REPORT_FILE"
echo "Log File: $LOG_FILE" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Count requests by status code
echo "=== Status Code Breakdown ===" >> "$REPORT_FILE"
grep -v "^#" "$LOG_FILE" | awk '{print $9}' | sort | uniq -c | sort -nr >> "$REPORT_FILE"

# Count 5xx errors
error_count=$(grep -v "^#" "$LOG_FILE" | awk '$9 ~ /^5/ {count++} END {print count}')
echo "" >> "$REPORT_FILE"
echo "Total 5xx errors: $error_count" >> "$REPORT_FILE"

# List top 10 IPs making requests
echo "" >> "$REPORT_FILE"
echo "=== Top 10 Client IPs ===" >> "$REPORT_FILE"
grep -v "^#" "$LOG_FILE" | awk '{print $1}' | sort | uniq -c | sort -nr | head -10 >> "$REPORT_FILE"

# List top 10 requested URLs
echo "" >> "$REPORT_FILE"
echo "=== Top 10 Requested URLs ===" >> "$REPORT_FILE"
grep -v "^#" "$LOG_FILE" | awk '{print $7}' | sort | uniq -c | sort -nr | head -10 >> "$REPORT_FILE"

# Check if error threshold exceeded
if [ "$error_count" -gt "$ERROR_THRESHOLD" ]; then
    echo "" >> "$REPORT_FILE"
    echo "WARNING: Error threshold exceeded ($error_count > $ERROR_THRESHOLD)" >> "$REPORT_FILE"
    
    # Send email alert
    mail -s "High Error Rate Alert" admin@example.com < "$REPORT_FILE"
fi

echo "" >> "$REPORT_FILE"
echo "Report generated on $(date)" >> "$REPORT_FILE"

echo "Analysis complete. Report saved to $REPORT_FILE"
```

> **SRE Perspective:** Log analysis scripts help identify trends, troubleshoot issues, and provide valuable insights into system behavior. This script could be scheduled to run daily and build a historical record of system performance.

### **3. Automated Deployment (SRE Application)**

Scripts can automate deployment processes, ensuring consistency.

```bash
#!/bin/bash

# Deployment script for web application
# Usage: ./deploy.sh [version]

set -e  # Exit immediately if a command fails

# Configuration
APP_NAME="mywebapp"
DEPLOY_DIR="/var/www/$APP_NAME"
BACKUP_DIR="/var/backups/$APP_NAME"
VERSION=${1:-"latest"}
REPO_URL="git@github.com:company/$APP_NAME.git"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

create_backup() {
    log "Creating backup of current deployment"
    mkdir -p "$BACKUP_DIR"
    
    if [ -d "$DEPLOY_DIR" ]; then
        tar -czf "$BACKUP_DIR/$APP_NAME-$(date +%Y%m%d-%H%M%S).tar.gz" -C "$DEPLOY_DIR" .
        log "Backup created successfully"
    else
        log "No existing deployment to backup"
    fi
}

deploy_application() {
    log "Deploying $APP_NAME version $VERSION"
    
    # Create or clean deploy directory
    mkdir -p "$DEPLOY_DIR"
    rm -rf "$DEPLOY_DIR/*"
    
    # Clone the repository
    git clone -b "$VERSION" "$REPO_URL" "$DEPLOY_DIR"
    
    # Install dependencies
    cd "$DEPLOY_DIR"
    npm install --production
    
    # Build the application
    npm run build
    
    # Set permissions
    chown -R www-data:www-data "$DEPLOY_DIR"
    chmod -R 755 "$DEPLOY_DIR"
    
    log "Deployment completed"
}

restart_services() {
    log "Restarting services"
    systemctl restart nginx
    systemctl restart "$APP_NAME"
    
    # Verify service status
    if systemctl is-active --quiet nginx && systemctl is-active --quiet "$APP_NAME"; then
        log "Services restarted successfully"
    else
        log "ERROR: Service restart failed"
        exit 1
    fi
}

# Main deployment flow
log "Starting deployment process for $APP_NAME ($VERSION)"

create_backup
deploy_application
restart_services

log "Deployment completed successfully"
```

> **SRE Perspective:** Deployment scripts ensure consistent and repeatable deployments, reduce human error, and enable easy rollbacks if issues arise. This script includes important SRE practices: creating backups before changes, logging each step, proper error handling, and verifying functionality after deployment.

---

## 🎯 **Practical Exercises**

### **Beginner Exercise: System Information Script**

Create a simple script that displays system information:

1. Create a new file named `sysinfo.sh`:

   ```bash
   nano sysinfo.sh
   ```

2. Add the following content:

   ```bash
   #!/bin/bash
   
   # System Information Script
   
   echo "===== System Information ====="
   echo "Hostname: $(hostname)"
   echo "Current User: $USER"
   echo "Date and Time: $(date)"
   echo "Uptime: $(uptime -p)"
   echo "Kernel Version: $(uname -r)"
   
   echo -e "\n===== CPU Information ====="
   lscpu | grep "Model name" | sed 's/Model name: *//'
   
   echo -e "\n===== Memory Information ====="
   free -h | grep "Mem:" | awk '{print "Total: " $2 "  Used: " $3 "  Free: " $4}'
   
   echo -e "\n===== Disk Usage ====="
   df -h / | awk 'NR>1 {print "Total: " $2 "  Used: " $3 "  Free: " $4 "  Use%: " $5}'
   ```

3. Make the script executable:

   ```bash
   chmod +x sysinfo.sh
   ```

4. Run the script:

   ```bash
   ./sysinfo.sh
   ```

### **Intermediate Exercise: Backup Script**

Create a backup script that archives specified directories:

1. Create a new file named `backup.sh`:

   ```bash
   nano backup.sh
   ```

2. Add the following content:

   ```bash
   #!/bin/bash
   
   # Backup Script
   # Usage: ./backup.sh <source_directory> [destination_directory]
   
   # Check if source directory is provided
   if [ $# -lt 1 ]; then
       echo "Usage: $0 <source_directory> [destination_directory]"
       exit 1
   fi
   
   # Set variables
   SOURCE_DIR=$1
   DEST_DIR=${2:-"$HOME/backups"}  # Default to ~/backups if not specified
   TIMESTAMP=$(date +%Y%m%d-%H%M%S)
   BACKUP_FILE="$DEST_DIR/backup-$TIMESTAMP.tar.gz"
   
   # Check if source directory exists
   if [ ! -d "$SOURCE_DIR" ]; then
       echo "Error: Source directory $SOURCE_DIR does not exist."
       exit 1
   fi
   
   # Create destination directory if it doesn't exist
   mkdir -p "$DEST_DIR"
   
   # Create backup
   echo "Creating backup of $SOURCE_DIR..."
   tar -czf "$BACKUP_FILE" -C "$(dirname "$SOURCE_DIR")" "$(basename "$SOURCE_DIR")"
   
   # Check if backup was successful
   if [ $? -eq 0 ]; then
       echo "Backup created successfully: $BACKUP_FILE"
       echo "Backup size: $(du -h "$BACKUP_FILE" | cut -f1)"
   else
       echo "Error: Backup failed!"
       exit 1
   fi
   
   # List existing backups
   echo -e "\nExisting backups in $DEST_DIR:"
   ls -lh "$DEST_DIR" | grep "backup-" | sort
   ```

3. Make the script executable:

   ```bash
   chmod +x backup.sh
   ```

4. Run the script:

   ```bash
   ./backup.sh ~/Documents
   ```

### **Advanced Exercise: Log Rotation and Analysis**

Create a script to rotate logs and generate a summary report:

1. Create a new file named `log_manager.sh`:

   ```bash
   nano log_manager.sh
   ```

2. Add the following content:

   ```bash
   #!/bin/bash
   
   # Log Rotation and Analysis Script
   # Usage: ./log_manager.sh <log_directory> <days_to_keep>
   
   # Exit on error
   set -e
   
   # Default values
   LOG_DIR=${1:-"/var/log/custom"}
   DAYS_TO_KEEP=${2:-7}
   REPORT_DIR="$LOG_DIR/reports"
   
   # Check if log directory exists
   if [ ! -d "$LOG_DIR" ]; then
       echo "Error: Log directory $LOG_DIR does not exist."
       exit 1
   fi
   
   # Create report directory
   mkdir -p "$REPORT_DIR"
   
   # Function to rotate logs
   rotate_logs() {
       echo "Rotating logs in $LOG_DIR..."
       
       # Find log files older than DAYS_TO_KEEP
       local old_logs=$(find "$LOG_DIR" -name "*.log" -type f -mtime +"$DAYS_TO_KEEP")
       
       if [ -z "$old_logs" ]; then
           echo "No old logs to rotate."
           return
       fi
       
       # Compress old logs
       for log in $old_logs; do
           echo "Compressing $log..."
           gzip -f "$log"
       done
       
       echo "Log rotation completed."
   }
   
   # Function to generate report
   generate_report() {
       local timestamp=$(date +%Y%m%d-%H%M%S)
       local report_file="$REPORT_DIR/log_report_$timestamp.txt"
       
       echo "Generating log report..."
       
       echo "=== Log Analysis Report ===" > "$report_file"
       echo "Date: $(date)" >> "$report_file"
       echo "Directory: $LOG_DIR" >> "$report_file"
       echo "" >> "$report_file"
       
       # Get log file statistics
       echo "=== Log File Statistics ===" >> "$report_file"
       find "$LOG_DIR" -name "*.log" -type f | while read -r logfile; do
           local name=$(basename "$logfile")
           local size=$(du -h "$logfile" | cut -f1)
           local lines=$(wc -l < "$logfile")
           local modified=$(stat -c %y "$logfile" | cut -d. -f1)
           
           echo "File: $name" >> "$report_file"
           echo "Size: $size" >> "$report_file"
           echo "Lines: $lines" >> "$report_file"
           echo "Last Modified: $modified" >> "$report_file"
           echo "" >> "$report_file"
       done
       
       # Count error occurrences
       echo "=== Error Summary ===" >> "$report_file"
       grep -i "error" "$LOG_DIR"/*.log 2>/dev/null | sort | uniq -c | sort -nr >> "$report_file" || echo "No errors found." >> "$report_file"
       
       echo "Report generated: $report_file"
   }
   
   # Main execution
   echo "Starting log management..."
   rotate_logs
   generate_report
   echo "Log management completed."
   ```

3. Make the script executable:

   ```bash
   chmod +x log_manager.sh
   ```

4. Create a test log directory and files:

   ```bash
   mkdir -p ~/test_logs
   echo "INFO: System started" > ~/test_logs/app.log
   echo "ERROR: Database connection failed" >> ~/test_logs/app.log
   echo "INFO: Service initialized" > ~/test_logs/service.log
   echo "ERROR: Permission denied" >> ~/test_logs/service.log
   ```

5. Run the script:

   ```bash
   ./log_manager.sh ~/test_logs 3
   ```

---

## 📝 **Quiz: Test Your Knowledge**

### **Beginner Level Questions:**

1. What line should begin every shell script to specify the interpreter?
   - a) `#!/bin/shell`
   - b) `#!/bin/bash`
   - c) `#/bin/bash`
   - d) `script:bash`

2. How do you correctly declare a variable named `username` with the value `admin`?
   - a) `username==admin`
   - b) `username="admin"`
   - c) `$username="admin"`
   - d) `username = "admin"`

3. Which command makes a script executable?
   - a) `chmod 777 script.sh`
   - b) `chmod +x script.sh`
   - c) `chmod -r script.sh`
   - d) `chmod enable script.sh`

4. How would you start a loop that iterates over all `.txt` files in the current directory?
   - a) `for file in *.txt; do`
   - b) `for file in .txt; do`
   - c) `loop file in *.txt; do`
   - d) `foreach file in *.txt; do`

5. What is the correct way to check if a file named "data.txt" exists?
   - a) `if [ -f "data.txt" ]; then`
   - b) `if exists "data.txt"; then`
   - c) `if [ data.txt ]; then`
   - d) `if grep "data.txt"; then`

### **Intermediate Level Questions:**

1. What does `$?` represent in a shell script?
   - a) The current process ID
   - b) The exit status of the last command
   - c) The number of command line arguments
   - d) The script's execution time

2. How do you capture the output of a command and store it in a variable?
   - a) `result = $(command)`
   - b) `result = command`
   - c) `result=$(command)`
   - d) `result=`command``

3. Which line will make a script exit immediately if any command fails?
   - a) `set -a`
   - b) `set -e`
   - c) `set -x`
   - d) `exit 1`

4. What does the `local` keyword do in a shell function?
   - a) Makes the function available globally
   - b) Restricts a variable's scope to the function
   - c) Forces the function to run in a subshell
   - d) Prevents the function from accessing environment variables

5. Which command would read user input into a variable named "password" without displaying what is typed?
   - a) `read password`
   - b) `read -s password`
   - c) `read -p password`
   - d) `input password`

### **SRE Application Questions:**

1. An SRE needs to create a deployment script that backs up existing files before replacement. Which approach is most appropriate?
   - a) Delete old files to make room for new ones
   - b) Create a timestamp-named backup before deploying new files
   - c) Deploy without backups to minimize downtime
   - d) Only back up files that have been modified

2. You need to monitor a critical service and restart it if it fails. Which command combination is most appropriate?
   - a) `ps aux | grep service`
   - b) `systemctl is-active service && echo "Running" || systemctl restart service`
   - c) `kill -9 $(pgrep service) && service start`
   - d) `service status | grep "active"`

3. When implementing error handling in an SRE automation script, which practice is most important?
   - a) Silently ignore errors to prevent alerts
   - b) Log detailed error information and exit with appropriate codes
   - c) Restart the script automatically when errors occur
   - d) Send all errors to /dev/null

4. You're writing a script to analyze application logs across multiple servers. What's the most efficient approach?
   - a) Manually check each server and compile results
   - b) Use SSH to run log analysis on each server and aggregate results
   - c) Copy all logs to a central location then delete them
   - d) Ask developers to check their own logs

5. An SRE needs to deploy a configuration change to 100 servers. Which scripting approach is safest?
   - a) Deploy to all servers simultaneously
   - b) Deploy to one server, verify, then use a loop with error handling for the rest
   - c) Manually deploy to each server
   - d) Ask each server owner to make the change

---

## ❓ **FAQ: Shell Scripting**

### **Beginner FAQs**

**Q1: How do I run a shell script?**
**A:** First, make the script executable with `chmod +x script.sh`, then run it with `./script.sh`. If the script isn't in your current directory, provide the path: `/path/to/script.sh`.

**Q2: What does the shebang line (`#!/bin/bash`) do?**
**A:** The shebang line tells the system which interpreter to use when executing the script. For bash scripts, we use `#!/bin/bash`. Without this line, the script would run in the default shell, which might not be bash.

**Q3: Why doesn't my variable work inside a string with single quotes?**
**A:** Single quotes (`'`) preserve the literal value of characters. For variable expansion, use double quotes (`"`). For example, `echo "Value: $variable"` will show the variable's value, while `echo 'Value: $variable'` will literally print `Value: $variable`.

**Q4: How do I accept user input in my script?**
**A:** Use the `read` command:
```bash
echo "Enter your name:"
read name
echo "Hello, $name!"
```

**Q5: How can I add comments to my script?**
**A:** Use the `#` symbol. Everything after `#` on a line is a comment and won't be executed:
```bash
# This is a comment
echo "Hello" # This is an end-of-line comment
```

### **Intermediate FAQs**

**Q1: How do I handle errors in my shell scripts?**
**A:** Several techniques can help:
- Use `set -e` to exit the script if any command fails
- Check command return codes with `if [ $? -ne 0 ]; then`
- Implement `trap` to catch and handle errors: `trap 'echo "Error at line $LINENO"; exit 1' ERR`
- Always validate input and check if files/directories exist before using them

**Q2: What's the difference between single and double brackets in conditionals?**
**A:** Bash supports both `[ ]` (test command) and `[[ ]]` (extended test command):
- `[ ]` is more portable (works in sh) but has limitations
- `[[ ]]` is more powerful with pattern matching, logical operators, and fewer quoting issues
```bash
# Single brackets (test command)
if [ "$a" = "$b" ] && [ -f "file.txt" ]; then

# Double brackets (extended test command)
if [[ $a = $b && -f file.txt ]]; then
```
Double brackets are generally preferred in bash scripts for their flexibility and safety.

**Q3: How can I debug my shell scripts?**
**A:** Use these debugging techniques:
- Add `set -x` at the top of your script to print each command before execution
- Use `set -v` to print script lines as they are read
- Run with bash's debug mode: `bash -x script.sh`
- Add strategic `echo` statements to track execution flow
- Use `shellcheck` to analyze your script for potential issues before running it

**Q4: What's the difference between `.bashrc`, `.bash_profile`, and `.profile`?**
**A:** These files control your shell environment:
- `.bash_profile` executes for login shells (SSH sessions, terminal at login)
- `.bashrc` executes for non-login interactive shells (opening a new terminal window)
- `.profile` is the traditional initialization file for all login shells (not just bash)

Generally, put environment variables in `.bash_profile` and aliases, functions, and prompt settings in `.bashrc`. To maintain consistency, many users source `.bashrc` from their `.bash_profile`.

**Q5: How do I process command-line options with flags?**
**A:** Use the `getopts` built-in command:
```bash
#!/bin/bash

while getopts "hf:v" option; do
    case $option in
        h) # Help option
            echo "Usage: $0 [-h] [-f filename] [-v]"
            exit 0
            ;;
        f) # File option with argument
            filename=$OPTARG
            echo "File: $filename"
            ;;
        v) # Verbose option
            verbose=true
            echo "Verbose mode enabled"
            ;;
        ?) # Invalid option
            echo "Invalid option. Use -h for help."
            exit 1
            ;;
    esac
done
```

### **SRE FAQs**

**Q1: How should I structure larger shell scripts for maintainability?**
**A:** Follow these best practices:

1. **Organize with functions**:
   ```bash
   #!/bin/bash
   
   # Script metadata/documentation
   # Author: Name
   # Purpose: Description
   
   # Constants and configuration
   LOG_FILE="/var/log/myscript.log"
   MAX_RETRIES=3
   
   # Function definitions
   log() {
       local level=$1
       local message=$2
       echo "[$(date '+%Y-%m-%d %H:%M:%S')] [$level] $message" >> "$LOG_FILE"
   }
   
   check_prerequisites() {
       # Check for required commands
   }
   
   parse_arguments() {
       # Process command-line arguments
   }
   
   main() {
       # Main script execution
       log "INFO" "Starting execution"
       check_prerequisites
       parse_arguments "$@"
       # Main logic
   }
   
   # Execute main function
   main "$@"
   ```

2. **Create libraries for common functions** in separate files and source them:
   ```bash
   source /path/to/common-functions.sh
   ```

3. **Use clear variable names** and add comments for complex logic

4. **Implement proper error handling** using techniques from Q1

5. **Version control** your scripts using Git

**Q2: How can I safely handle secrets in shell scripts?**
**A:** Never hardcode sensitive information. Use these approaches instead:

1. **Environment variables**:
   ```bash
   #!/bin/bash
   
   # Check for required environment variables
   if [ -z "$API_KEY" ]; then
       echo "Error: API_KEY environment variable is not set"
       exit 1
   fi
   
   # Use the secret
   curl -H "Authorization: Bearer $API_KEY" https://api.example.com
   ```

2. **External files with restricted permissions**:
   ```bash
   # Create a secure file
   echo "my-secret-key" > ~/.api_key
   chmod 600 ~/.api_key  # Only owner can read/write
   
   # In your script
   API_KEY=$(cat ~/.api_key)
   ```

3. **Secret management tools**:
   ```bash
   # Using HashiCorp Vault
   API_KEY=$(vault kv get -field=api_key secrets/myapp)
   
   # Using AWS Secrets Manager
   API_KEY=$(aws secretsmanager get-secret-value --secret-id myapp/api_key --query SecretString --output text)
   ```

4. **Prompt user for sensitive input**:
   ```bash
   read -sp "Enter API key: " API_KEY
   echo  # Add a new line after input
   ```

**Q3: How can I implement robust timeouts for external commands?**
**A:** Use the `timeout` command or implement your own timeout logic:

```bash
# Using the timeout command
if timeout 5s some_command; then
    echo "Command completed within 5 seconds"
else
    echo "Command timed out or failed"
fi

# Manual timeout with background process and wait
some_command &
cmd_pid=$!


# Wait up to 5 seconds
if ! wait -n $cmd_pid 2>/dev/null; then
    # Command failed or is still running
    kill -9 $cmd_pid 2>/dev/null
    echo "Command timed out or failed"
else
    echo "Command completed successfully"
fi
```

For network requests, many tools like `curl` have built-in timeout options:
```bash
curl --connect-timeout 5 --max-time 10 https://api.example.com
```

**Q4: How do I implement proper logging in shell scripts for production environments?**
**A:** Create a robust logging framework:

```bash
#!/bin/bash

# Configuration
LOG_FILE="/var/log/myapp.log"
LOG_LEVEL="INFO"  # DEBUG, INFO, WARN, ERROR

# Create log directory if it doesn't exist
mkdir -p "$(dirname "$LOG_FILE")"

# Logging function
log() {
    local level=$1
    local message=$2
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    # Only log if level is at or above configured level
    case $LOG_LEVEL in
        DEBUG)
            ;;
        INFO)
            if [[ $level == "DEBUG" ]]; then return; fi
            ;;
        WARN)
            if [[ $level == "DEBUG" || $level == "INFO" ]]; then return; fi
            ;;
        ERROR)
            if [[ $level != "ERROR" ]]; then return; fi
            ;;
    esac
    
    # Format: [TIMESTAMP] [LEVEL] [SCRIPT:LINE] Message
    echo "[$timestamp] [$level] [${0##*/}:${BASH_LINENO[0]}] $message" >> "$LOG_FILE"
    
    # Also print to stderr for ERROR level
    if [[ $level == "ERROR" ]]; then
        echo "[$timestamp] [$level] $message" >&2
    fi
}

# Usage
log "DEBUG" "Debugging information"
log "INFO" "Process started"
log "WARN" "Unusual condition detected"
log "ERROR" "Failed to process request"
```

For production systems, consider sending logs to a centralized logging system like ELK (Elasticsearch, Logstash, Kibana) or using the system logger:
```bash
logger -t myapp "Critical error occurred"
```

**Q5: How can I implement retries for unreliable operations in shell scripts?**
**A:** Use a retry loop with exponential backoff:

```bash
#!/bin/bash

# Retry function with exponential backoff
retry_command() {
    local cmd=$1
    local max_attempts=${2:-5}
    local timeout=${3:-2}
    local attempt=1
    local output
    local status
    
    while [[ $attempt -le $max_attempts ]]; do
        echo "Attempt $attempt of $max_attempts: $cmd"
        
        # Execute the command
        output=$($cmd 2>&1)
        status=$?
        
        if [[ $status -eq 0 ]]; then
            echo "Command succeeded"
            echo "$output"
            return 0
        fi
        
        echo "Command failed with exit status $status"
        echo "$output"
        
        # Increase timeout exponentially with each attempt
        sleep $timeout
        timeout=$((timeout * 2))
        attempt=$((attempt + 1))
    done
    
    echo "Command failed after $max_attempts attempts"
    return 1
}

# Example usage
retry_command "curl -s https://api.example.com/data" 3 2
```

This approach is particularly useful for network operations, API calls, or any operation that might fail intermittently.

---

## 🚧 **Common Issues and Troubleshooting**

### **Beginner Issues**

#### **Issue 1: "Permission denied" when running a script**

**Symptoms:**
```
bash: ./myscript.sh: Permission denied
```

**Causes:**
- Script file doesn't have execute permission
- File system mounted with `noexec` option
- SELinux or AppArmor restrictions

**Solutions:**
```bash
# Add execute permission
chmod +x myscript.sh

# Check if file system is mounted with noexec
mount | grep noexec

# Check SELinux context (if applicable)
ls -Z myscript.sh
```

#### **Issue 2: Variables not expanding as expected**

**Symptoms:**
```
Hello, $name!  (instead of showing the actual name)
```

**Causes:**
- Using single quotes instead of double quotes
- Incorrect variable name or typo
- Variable not initialized before use

**Solutions:**
```bash
# Use double quotes for variable expansion
echo "Hello, $name!"

# Check if variable is set
if [ -z "$name" ]; then
    echo "Variable 'name' is not set"
fi

# Debug by printing variable content
echo "Variable content: [$name]"
```

#### **Issue 3: Command not found errors**

**Symptoms:**
```
./myscript.sh: line 10: somecommand: command not found
```

**Causes:**
- Command not installed on the system
- Command not in PATH
- Typo in command name

**Solutions:**
```bash
# Check if command exists
which somecommand

# Install missing command
sudo apt install package-with-command  # Debian/Ubuntu
sudo yum install package-with-command  # RHEL/CentOS

# Add directory to PATH if command is in non-standard location
export PATH=$PATH:/path/to/command/directory
```

### **Intermediate Issues**

#### **Issue 1: Script works in interactive shell but fails in cron**

**Symptoms:**
- Script runs fine when executed manually but fails when scheduled via cron

**Causes:**
- Different environment in cron (PATH, working directory, environment variables)
- Missing executable permissions
- Relative paths in script

**Solutions:**
```bash
# In your cron job, set explicit PATH
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Use absolute paths in scripts for cron
/usr/bin/command /absolute/path/to/file

# Set required environment variables
export HOME=/home/user
```

#### **Issue 2: Unexpected behavior with empty variables or parameters**

**Symptoms:**
- Script fails or behaves unexpectedly when variables are empty

**Causes:**
- Unquoted variables expanding to multiple words
- Unset variables being treated as empty strings

**Solutions:**
```bash
# Set strict mode to catch unset variables
set -u  # or set -o nounset

# Always quote variables
for file in "$directory"/*.log; do

# Use default values for potentially empty variables
echo "${name:-Unknown User}"

# Check if arguments are provided
if [ $# -eq 0 ]; then
    echo "Error: No arguments provided"
    exit 1
fi
```

#### **Issue 3: Script hangs indefinitely**

**Symptoms:**
- Script stops responding and never completes

**Causes:**
- Waiting for user input in a non-interactive environment
- Infinite loops
- Command waiting indefinitely for a resource

**Solutions:**
```bash
# Add timeout to commands that might hang
timeout 10s problematic_command

# Make sure read commands have a timeout in non-interactive scripts
read -t 10 -p "Enter value: " value

# Add loop-breaking conditions
count=0
max_iterations=100
while condition; do
    # Do work
    
    ((count++))
    if [ $count -ge $max_iterations ]; then
        echo "Maximum iterations reached, breaking"
        break
    fi
done
```

### **SRE-Level Issues**

#### **Issue 1: Race conditions in scripts**

**Symptoms:**
- Script occasionally fails or produces incorrect results
- Failures occur only under specific timing conditions

**Causes:**
- Multiple instances of the script running simultaneously
- Concurrent access to shared resources (files, databases)

**Solutions:**
```bash
# Use flock for file-based locking
(
    if ! flock -n 9; then
        echo "Another instance is running"
        exit 1
    fi
    
    # Critical section of code here
    
) 9>/var/lock/myscript.lock

# Use a PID file approach
PID_FILE="/var/run/myscript.pid"

if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if ps -p "$PID" > /dev/null; then
        echo "Script is already running with PID $PID"
        exit 1
    fi
fi

# Script is not running, so save the PID
echo $ > "$PID_FILE"

# Remove PID file on exit
trap 'rm -f "$PID_FILE"' EXIT
```

#### **Issue 2: Resource exhaustion**

**Symptoms:**
- Script consumes excessive CPU, memory, or disk space
- System performance degrades during script execution

**Causes:**
- Processing large datasets without limiting resource usage
- Creating too many subprocesses
- Memory leaks in long-running scripts

**Solutions:**
```bash
# Limit CPU usage with nice and cpulimit
nice -n 19 ./intensive_script.sh  # Lower priority
cpulimit -l 50 ./intensive_script.sh  # Limit to 50% CPU

# Limit memory usage with ulimit
ulimit -v 1000000  # Limit virtual memory to ~1GB

# Process large files in chunks
split -l 10000 large_file.txt chunk_
for chunk in chunk_*; do
    process_file "$chunk"
    rm "$chunk"  # Clean up as we go
done

# Clean up temporary files
trap 'rm -rf "$TEMP_DIR"' EXIT
```

#### **Issue 3: Handling service dependencies**

**Symptoms:**
- Script fails because a required service isn't ready
- Inconsistent results depending on service state

**Causes:**
- Attempting to use a service before it's fully initialized
- Failing to check service health before use

**Solutions:**
```bash
# Function to wait for service
wait_for_service() {
    local service=$1
    local max_attempts=${2:-30}
    local wait_time=${3:-2}
    local attempt=1
    
    echo "Waiting for $service to be ready..."
    
    while [ $attempt -le $max_attempts ]; do
        if systemctl is-active --quiet "$service"; then
            echo "$service is ready"
            return 0
        fi
        
        echo "Attempt $attempt: $service not ready, waiting ${wait_time}s..."
        sleep $wait_time
        attempt=$((attempt + 1))
    done
    
    echo "Timeout waiting for $service to be ready after $max_attempts attempts"
    return 1
}

# Wait for database before proceeding
if ! wait_for_service mysql; then
    echo "Database service is not available, exiting"
    exit 1
fi

# Check port availability
wait_for_port() {
    local host=$1
    local port=$2
    local timeout=${3:-30}
    local start_time=$(date +%s)
    
    while true; do
        if timeout 1 bash -c "< /dev/tcp/$host/$port" &>/dev/null; then
            echo "Port $port on $host is open"
            return 0
        fi
        
        current_time=$(date +%s)
        if [ $((current_time - start_time)) -ge $timeout ]; then
            echo "Timeout waiting for $host:$port"
            return 1
        fi
        
        sleep 1
    done
}

wait_for_port localhost 3306 60
```

---

## 🔄 **Real-World SRE Scenario: Database Backup and Verification**

**Situation:** As an SRE, you need to create a comprehensive database backup solution that runs nightly, verifies backup integrity, rotates old backups, and provides meaningful alerts if issues arise.

**Solution:** A robust shell script that handles all aspects of the database backup process.

```bash
#!/bin/bash

#############################################
# Database Backup Script for Production
#
# Features:
# - Creates timestamped, compressed backups
# - Verifies backup integrity
# - Rotates old backups automatically
# - Sends alerts on success/failure
# - Records metrics for monitoring
#
# Usage: ./db_backup.sh [config_file]
#############################################

# Enable strict error handling
set -eo pipefail

# Default configuration
CONFIG_FILE=${1:-"/etc/db_backup.conf"}
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_DIR="/var/log/db_backup"
LOG_FILE="$LOG_DIR/backup_${TIMESTAMP}.log"
BACKUP_DIR="/var/backup/databases"
METRICS_FILE="/var/log/db_backup/metrics.log"
RETAIN_DAYS=14
ALERT_EMAIL="sre-team@example.com"
SLACK_WEBHOOK="https://hooks.slack.com/services/XXXX/YYYY/ZZZZ"

# Create required directories
mkdir -p "$LOG_DIR" "$BACKUP_DIR"

# Source configuration if exists
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
fi

# Setup logging
log() {
    local level=$1
    local message=$2
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$timestamp] [$level] $message" | tee -a "$LOG_FILE"
}

# Error handler
handle_error() {
    local error_message="Backup failed at line $1"
    log "ERROR" "$error_message"
    send_alert "❌ Database Backup FAILED" "$error_message"
    exit 1
}

# Set error trap
trap 'handle_error $LINENO' ERR

# Send alerts
send_alert() {
    local title=$1
    local message=$2
    
    # Email alert
    echo -e "Subject: $title\n\n$message\n\nTimestamp: $(date)\nHost: $(hostname)\nLog: $LOG_FILE" | \
        sendmail "$ALERT_EMAIL"
    
    # Slack alert (if webhook is configured)
    if [ -n "$SLACK_WEBHOOK" ]; then
        curl -s -X POST -H 'Content-type: application/json' \
            --data "{\"text\":\"*$title*\n$message\n\nTimestamp: $(date)\nHost: $(hostname)\"}" \
            "$SLACK_WEBHOOK"
    fi
    
    log "INFO" "Alert sent: $title"
}

# Record metrics
record_metric() {
    local name=$1
    local value=$2
    echo "$(date +%s) $name $value" >> "$METRICS_FILE"
}

# Database connection check
check_database() {
    log "INFO" "Checking database connection"
    start_time=$(date +%s)
    
    # Test database connection
    if ! mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASSWORD" -e "SELECT 1" > /dev/null 2>&1; then
        log "ERROR" "Failed to connect to database"
        exit 1
    fi
    
    end_time=$(date +%s)
    record_metric "db_connection_time_seconds" $((end_time - start_time))
    log "INFO" "Database connection successful"
}

# Create backup
create_backup() {
    log "INFO" "Starting database backup"
    
    local start_time=$(date +%s)
    local backup_file="$BACKUP_DIR/$DB_NAME-$TIMESTAMP.sql.gz"
    
    # Create the backup with compression
    log "INFO" "Creating backup: $backup_file"
    mysqldump --single-transaction --quick --lock-tables=false \
        -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" | \
        gzip > "$backup_file"
    
    local end_time=$(date +%s)
    local backup_size=$(du -b "$backup_file" | cut -f1)
    local duration=$((end_time - start_time))
    
    record_metric "backup_size_bytes" "$backup_size"
    record_metric "backup_duration_seconds" "$duration"
    
    log "INFO" "Backup completed in $duration seconds, size: $(du -h "$backup_file" | cut -f1)"
    echo "$backup_file"
}

# Verify backup integrity
verify_backup() {
    local backup_file=$1
    log "INFO" "Verifying backup integrity: $backup_file"
    
    local start_time=$(date +%s)
    
    # Test gzip file integrity
    log "INFO" "Testing gzip file integrity"
    gzip -t "$backup_file"
    
    # Check if the backup contains real data (not just schema)
    log "INFO" "Checking backup content"
    local table_count=$(zcat "$backup_file" | grep -c "CREATE TABLE" || true)
    log "INFO" "Backup contains $table_count tables"
    
    if [ "$table_count" -lt 1 ]; then
        log "ERROR" "Backup verification failed: No tables found in backup"
        exit 1
    fi
    
    # Create SHA256 checksum
    sha256sum "$backup_file" > "${backup_file}.sha256"
    log "INFO" "Created checksum: ${backup_file}.sha256"
    
    local end_time=$(date +%s)
    record_metric "verification_duration_seconds" $((end_time - start_time))
    
    log "INFO" "Backup verification completed successfully"
}

# Rotate old backups
rotate_backups() {
    log "INFO" "Rotating backups older than $RETAIN_DAYS days"
    
    local start_time=$(date +%s)
    
    # Find and delete old backups and their checksums
    local deleted_count=$(find "$BACKUP_DIR" -name "$DB_NAME-*.sql.gz" -type f -mtime +$RETAIN_DAYS | wc -l)
    find "$BACKUP_DIR" -name "$DB_NAME-*.sql.gz" -type f -mtime +$RETAIN_DAYS -delete
    find "$BACKUP_DIR" -name "$DB_NAME-*.sql.gz.sha256" -type f -mtime +$RETAIN_DAYS -delete
    
    record_metric "deleted_backups" "$deleted_count"
    
    # Get remaining backup count and size
    local remaining_count=$(find "$BACKUP_DIR" -name "$DB_NAME-*.sql.gz" -type f | wc -l)
    local total_size=$(du -sh "$BACKUP_DIR" | cut -f1)
    
    log "INFO" "Deleted $deleted_count old backups. Remaining: $remaining_count backups ($total_size)"
}

# Main function
main() {
    log "INFO" "Starting database backup process for $DB_NAME on $(hostname)"
    
    # Start time tracking
    local script_start=$(date +%s)
    
    # Load database credentials from secure file
    if [ -f "/etc/db_backup/credentials" ]; then
        source "/etc/db_backup/credentials"
    fi
    
    # Check for required variables
    if [ -z "$DB_HOST" ] || [ -z "$DB_USER" ] || [ -z "$DB_PASSWORD" ] || [ -z "$DB_NAME" ]; then
        log "ERROR" "Missing required database configuration"
        exit 1
    fi
    
    # Check database connection
    check_database
    
    # Create backup
    backup_file=$(create_backup)
    
    # Verify backup integrity
    verify_backup "$backup_file"
    
    # Rotate old backups
    rotate_backups
    
    # Calculate execution time
    local script_end=$(date +%s)
    local total_duration=$((script_end - script_start))
    record_metric "total_script_duration_seconds" "$total_duration"
    
    # Success message
    log "INFO" "Database backup process completed successfully in $total_duration seconds"
    send_alert "✅ Database Backup Successful" "Backup completed successfully in $total_duration seconds.\nBackup: $backup_file\nSize: $(du -h "$backup_file" | cut -f1)"
    
    exit 0
}

# Execute main function
main
```

**Key SRE practices demonstrated:**

1. **Comprehensive logging** - Detailed timestamped logs for troubleshooting
2. **Error handling** - Proper error trapping and handling
3. **Metrics collection** - Recording performance data for trending and analysis
4. **Input validation** - Checking for required parameters
5. **Security considerations** - Separating credentials from the main script
6. **Verification** - Validating backup integrity
7. **Cleanup** - Rotating old backups to manage disk space
8. **Alerting** - Sending notifications for success/failure
9. **Modularity** - Using functions to organize code
10. **Documentation** - Clear comments explaining the script's purpose and usage

This script represents a production-ready solution that addresses the reliability, maintainability, and observability aspects that SREs value.

---

## 📚 **Further Learning Resources**

### **Beginner Resources**

- [Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/html/index.html) - Comprehensive introduction to bash scripting
- [LinuxCommand.org](https://linuxcommand.org/) - Excellent resource for learning shell scripting basics
- [Explainshell](https://explainshell.com/) - Interactive tool that explains shell commands
- [ShellCheck](https://www.shellcheck.net/) - Online tool to analyze shell scripts for common mistakes
- [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line) - Interactive course for beginners

### **Intermediate Resources**

- [Advanced Bash-Scripting Guide](https://tldp.org/LDP/abs/html/) - In-depth guide to advanced bash scripting techniques
- [Bash Hackers Wiki](https://wiki.bash-hackers.org/) - Community-driven documentation for bash scripting
- [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html) - Best practices for writing shell scripts
- [Learn Bash in Y Minutes](https://learnxinyminutes.com/docs/bash/) - Quick reference for bash syntax
- [Command Line Power User](https://commandlinepoweruser.com/) - Video course on advanced command-line usage

### **SRE-Specific Resources**

- [Google SRE Book - Chapter 7: The Evolution of Automation at Google](https://sre.google/sre-book/automation-at-google/) - Best practices for automation from Google's SRE team
- [The Practice of Cloud System Administration](https://www.amazon.com/Practice-Cloud-System-Administration-Distributed/dp/032194318X) - Comprehensive guide including shell scripting for cloud environments
- [Bash Cookbook](https://www.oreilly.com/library/view/bash-cookbook/0596526784/) - Solutions to common scripting problems
- [Effective DevOps](https://www.oreilly.com/library/view/effective-devops/9781491926291/) - Includes automation and script management best practices
- [Linux Foundation's SRE Fundamentals Course](https://training.linuxfoundation.org/training/introduction-to-site-reliability-engineering-and-devops/) - Includes shell scripting for SRE work

### **Online Tools and References**

- [tldr pages](https://tldr.sh/) - Simplified, practical man pages
- [DevHints.io Bash Cheatsheet](https://devhints.io/bash) - Quick reference for bash commands and syntax
- [RegExr](https://regexr.com/) - Interactive tool for testing regular expressions used in scripts
- [Crontab Guru](https://crontab.guru/) - Interactive editor for cron schedule expressions
- [Bash Pitfalls](https://mywiki.wooledge.org/BashPitfalls) - Common mistakes in bash scripts and how to avoid them

---

## 🎉 **Congratulations on Completing the 10-Day Linux Course!**

You've now completed all 10 days of this intensive Linux learning journey! Let's recap what you've learned:

- **Day 1**: Linux fundamentals, shell, navigation, getting help
- **Day 2**: File manipulation (creating, viewing, copying, moving, deleting)
- **Day 3**: Permissions and ownership management
- **Day 4**: Text processing and searching with `grep`, `find`, and pipes
- **Day 5**: Advanced text manipulation with `sed`, `awk`, `sort`, and `uniq`
- **Day 6**: Process management and system monitoring
- **Day 7**: Network basics and remote operations
- **Day 8**: User and group management
- **Day 9**: Archiving, compression, and package management
- **Day 10**: Shell scripting for automation

These skills form a solid foundation for Linux system administration and SRE work. By mastering these commands and concepts, you're well-equipped to handle a wide range of system tasks, troubleshoot issues, and create automation to make your work more efficient and reliable.

Continue practicing these skills in real-world scenarios, and consider exploring more advanced topics like:

- Configuration management tools (Ansible, Puppet, Chef)
- Containerization (Docker, Kubernetes)
- Infrastructure as Code (Terraform)
- Advanced monitoring and observability
- Performance tuning and optimization

Remember that Linux mastery comes with practice and continuous learning. Don't hesitate to reference the materials from this course as you apply these skills in your daily work.

Happy scripting!