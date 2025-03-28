# 🚀 **Day 10: Shell Scripting Basics – Automating Linux Tasks**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 9:**

Yesterday, you learned about archiving, compression, and package management. You mastered tools like `tar`, `gzip`, and `zip` for bundling and compressing files, as well as package managers (`apt`, `yum`, `dpkg`, `rpm`) for installing and maintaining software. These skills enable you to efficiently manage files and software across Linux systems.

### 📅 **Today's Topics and Importance:**

Today, we'll explore **Shell Scripting** - the art of creating programs using shell commands. This topic is absolutely essential for SREs because:

- It allows you to automate repetitive tasks
- It enables consistent execution of complex operations
- It helps create reproducible system configurations
- It's fundamental for monitoring, maintenance, and deployment tasks
- It's the building block for more complex automation systems

Learning shell scripting turns your collection of individual Linux commands into powerful automation workflows, dramatically increasing your productivity and reliability as an SRE.

### 🎯 **Learning Objectives:**

By the end of Day 10, you will be able to:

- Create and run basic shell scripts
- Use variables and environment variables
- Accept and process command line arguments
- Implement conditional logic with `if` statements
- Create loops for repetitive tasks
- Use functions to organize and reuse code
- Process text input with common scripting patterns
- Apply best practices for script organization and error handling

---

## 📚 **Core Concepts Explained**

### **What is Shell Scripting?**

Shell scripting is a way to automate command sequences you would normally type at the command line. A shell script is simply a text file containing a series of commands that the shell can execute.

Think of shell scripting as creating "recipes" for your computer:

- **Ingredients**: Commands, variables, and data
- **Instructions**: The sequence and logic for processing
- **Result**: Automated tasks that run consistently every time

The primary shell we'll focus on is **Bash** (Bourne Again SHell), which is the default on most Linux distributions. However, the concepts apply to other shells like Zsh or Dash with minor syntax differences.

### **Why Shell Scripting is Essential for SREs**

As an SRE, you'll find that shell scripting:

1. **Reduces Toil**: Automates repetitive manual tasks
2. **Ensures Consistency**: Commands execute the same way every time
3. **Provides Accountability**: Scripts can be version-controlled and reviewed
4. **Improves Resilience**: Scripts can include error handling and recovery
5. **Simplifies Onboarding**: New team members can run complex operations without deep system knowledge

From simple backup scripts to complex deployment automation, shell scripting is a fundamental skill in the SRE toolkit.

---

## 💻 **Shell Scripting Essentials**

### **1. Creating and Running Basic Scripts**

**Creating a Script:**

1. Create a file with `.sh` extension:

   ```bash
   touch myscript.sh
   ```

2. Add the shebang line to specify the interpreter:

   ```bash
   #!/bin/bash
   ```

3. Add commands:

   ```bash
   #!/bin/bash
   echo "Hello, SRE World!"
   date
   uptime
   ```

4. Make the script executable:

   ```bash
   chmod +x myscript.sh
   ```

5. Run the script:

   ```bash
   ./myscript.sh
   ```

**SRE Context:** Even this simple script demonstrates automation fundamentals. In real-world scenarios, SREs often start by scripting repetitive command sequences like server health checks or log analysis.

### **2. Variables and Environment Variables**

**Declaring and Using Variables:**

```bash
#!/bin/bash

# Variable assignment (no spaces around equals sign)
name="SRE Team"
server_count=5
timestamp=$(date +%Y%m%d)

# Using variables (prefix with $)
echo "Hello, $name!"
echo "Managing $server_count servers"
echo "Backup filename: backup_$timestamp.tar.gz"
```

**Environment Variables:**

```bash
#!/bin/bash

# Access existing environment variables
echo "User: $USER"
echo "Home Directory: $HOME"
echo "Current Path: $PATH"

# Set a new environment variable
export APP_ENV="production"
echo "Application Environment: $APP_ENV"
```

**SRE Context:** Variables make scripts flexible and reusable. SREs commonly parametrize scripts to handle different environments (dev/staging/prod) or varying configurations without changing the core logic.

### **3. Command Line Arguments**

**Accessing Arguments:**

```bash
#!/bin/bash

# $0 is the script name
# $1, $2, etc. are the arguments
# $# is the number of arguments
# $@ represents all arguments

echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Number of arguments: $#"
echo "All arguments: $@"
```

**Example with Arguments:**

```bash
#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Usage: $0 <source_dir> <backup_dir>"
    exit 1
fi

source_dir=$1
backup_dir=$2
timestamp=$(date +%Y%m%d_%H%M%S)

echo "Creating backup of $source_dir in $backup_dir with timestamp $timestamp"
tar -czf "$backup_dir/backup_$timestamp.tar.gz" "$source_dir"
```

**SRE Context:** Command line arguments make scripts more versatile. A single backup script can handle different directories, or a monitoring script can check different services based on arguments.

### **4. Conditional Logic with `if` Statements**

**Basic If-Else Structure:**

```bash
#!/bin/bash

server="web-server-01"

if [ "$server" = "web-server-01" ]; then
    echo "This is the primary web server"
else
    echo "This is a secondary server"
fi
```

**File and Directory Tests:**

```bash
#!/bin/bash

log_file="/var/log/application.log"

# Check if file exists
if [ -f "$log_file" ]; then
    echo "Log file exists"
    
    # Check if file is non-empty
    if [ -s "$log_file" ]; then
        echo "Log file contains data"
    else
        echo "Log file is empty"
    fi
else
    echo "Log file does not exist"
fi

# Check if directory exists
if [ -d "/var/log/archive" ]; then
    echo "Archive directory exists"
else
    mkdir -p /var/log/archive
    echo "Created archive directory"
fi
```

**Numeric Comparisons:**

```bash
#!/bin/bash

cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
memory_used=$(free -m | awk 'NR==2{print $3}')
disk_used=$(df -h / | awk 'NR==2{print $5}' | sed 's/%//')

echo "CPU Usage: $cpu_usage%"
echo "Memory Used: $memory_used MB"
echo "Disk Used: $disk_used%"

# Check resource thresholds
if [ $(echo "$cpu_usage > 90" | bc -l) -eq 1 ]; then
    echo "WARNING: High CPU usage detected"
fi

if [ $memory_used -gt 1024 ]; then
    echo "WARNING: Memory usage exceeds 1GB"
fi

if [ $disk_used -gt 80 ]; then
    echo "WARNING: Disk usage exceeds 80%"
fi
```

**SRE Context:** Conditional logic allows scripts to make decisions based on system state. SREs use conditions to implement intelligent monitoring, validate inputs, and handle error cases.

### **5. Loops for Repetitive Tasks**

**For Loops:**

```bash
#!/bin/bash

# Loop through a list
servers=("web-01" "web-02" "db-01" "cache-01")

for server in "${servers[@]}"; do
    echo "Checking status of $server"
    ping -c 1 "$server" &> /dev/null
    
    if [ $? -eq 0 ]; then
        echo "$server is online"
    else
        echo "$server is offline"
    fi
done

# Loop through files
echo "Log files in /var/log:"
for logfile in /var/log/*.log; do
    size=$(du -h "$logfile" | awk '{print $1}')
    echo "$logfile - $size"
done

# Numeric loop
echo "Performing 5 HTTP requests:"
for i in {1..5}; do
    echo "Request $i:"
    curl -s -o /dev/null -w "Status: %{http_code}, Time: %{time_total}s\n" http://example.com
    sleep 1
done
```

**While Loops:**

```bash
#!/bin/bash

# Monitor a process for 60 seconds
process_name="nginx"
counter=0

while [ $counter -lt 60 ]; do
    process_count=$(pgrep -c "$process_name")
    
    echo "$(date +%T) - $process_name processes: $process_count"
    
    if [ $process_count -eq 0 ]; then
        echo "WARNING: $process_name is not running! Attempting restart..."
        systemctl start "$process_name"
    fi
    
    counter=$((counter + 10))
    sleep 10
done
```

**SRE Context:** Loops enable efficient handling of multiple items (servers, files, services) with the same logic. This is essential for fleet management and batch processing tasks common in SRE work.

### **6. Functions for Code Organization**

**Defining and Using Functions:**

```bash
#!/bin/bash

# Define a function
check_service() {
    local service_name=$1
    
    echo "Checking service: $service_name"
    
    systemctl is-active --quiet "$service_name"
    if [ $? -eq 0 ]; then
        echo "$service_name is running"
        return 0
    else
        echo "$service_name is not running"
        return 1
    fi
}

restart_service() {
    local service_name=$1
    
    echo "Attempting to restart $service_name"
    systemctl restart "$service_name"
    
    # Check if restart was successful
    systemctl is-active --quiet "$service_name"
    if [ $? -eq 0 ]; then
        echo "$service_name restart successful"
        return 0
    else
        echo "$service_name restart failed"
        return 1
    fi
}

# Main script
services=("nginx" "mysql" "redis-server")

for service in "${services[@]}"; do
    if ! check_service "$service"; then
        restart_service "$service"
    fi
done

echo "Service check completed"
```

**SRE Context:** Functions make scripts modular and maintainable. SREs can create libraries of common functions for tasks like health checks, notification, or standardized logging.

### **7. Error Handling and Exit Codes**

```bash
#!/bin/bash

# Enable exit on error (script stops if any command fails)
set -e

# Function to handle cleanup on error
cleanup() {
    echo "Error occurred at line $1"
    # Perform any necessary cleanup
    echo "Cleaning up temporary files"
    rm -f /tmp/script_temp_*
}

# Trap errors and call cleanup function with line number
trap 'cleanup $LINENO' ERR

# Function to check command success
run_command() {
    "$@"
    local status=$?
    if [ $status -ne 0 ]; then
        echo "Error: Command '$*' failed with status $status"
        return $status
    fi
    return 0
}

# Main script
echo "Starting backup process"

# Check if backup directory exists
backup_dir="/backup"
if [ ! -d "$backup_dir" ]; then
    echo "Error: Backup directory does not exist"
    exit 1
fi

# Create temp file
temp_file=$(mktemp /tmp/script_temp_XXXXX)
echo "Created temporary file: $temp_file"

# Attempt database dump
echo "Dumping database"
run_command mysqldump -u dbuser -p'password' database > "$temp_file"

# Copy to backup location with timestamp
timestamp=$(date +%Y%m%d_%H%M%S)
run_command cp "$temp_file" "$backup_dir/db_backup_$timestamp.sql"

# Cleanup
rm -f "$temp_file"

echo "Backup completed successfully"
exit 0
```

**SRE Context:** Proper error handling is critical in production scripts. SREs need scripts that fail safely, clean up after themselves, and provide clear error information for troubleshooting.

---

## 🔍 **Common Scripting Patterns for SREs**

### **1. System Health Check Scripts**

```bash
#!/bin/bash

# Health check script for critical system components
# Usage: ./health_check.sh [email@example.com]

log_file="/var/log/system_health.log"
alert_email=${1:-"admin@example.com"}

log_message() {
    local message=$1
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$timestamp] $message" | tee -a "$log_file"
}

check_disk_space() {
    log_message "Checking disk space..."
    
    # Check each mounted filesystem
    df -h | grep -vE "tmpfs|devtmpfs" | awk 'NR>1 {print $5 " " $6}' | while read -r usage mount; do
        usage_percent=${usage%\%}
        
        if [ "$usage_percent" -gt 90 ]; then
            log_message "WARNING: High disk usage on $mount: $usage"
            return 1
        fi
    done
    
    log_message "Disk space check passed"
    return 0
}

check_memory() {
    log_message "Checking memory usage..."
    
    # Get memory details
    total_mem=$(free -m | awk 'NR==2{print $2}')
    used_mem=$(free -m | awk 'NR==2{print $3}')
    free_mem=$(free -m | awk 'NR==2{print $4}')
    
    # Calculate percentage
    used_percent=$((used_mem * 100 / total_mem))
    
    log_message "Memory: $used_mem MB used ($used_percent%), $free_mem MB free"
    
    if [ "$used_percent" -gt 90 ]; then
        log_message "WARNING: High memory usage: $used_percent%"
        return 1
    fi
    
    return 0
}

check_load_average() {
    log_message "Checking system load..."
    
    # Get number of CPU cores
    cores=$(nproc)
    
    # Get 5-minute load average
    load=$(uptime | awk -F'[a-z]:' '{print $2}' | awk '{print $2}' | tr -d ',')
    
    log_message "Load average (5min): $load (cores: $cores)"
    
    # Check if load exceeds number of cores
    if [ $(echo "$load > $cores" | bc -l) -eq 1 ]; then
        log_message "WARNING: High system load: $load"
        return 1
    fi
    
    return 0
}

check_critical_services() {
    log_message "Checking critical services..."
    
    services=("nginx" "mysql" "redis-server" "prometheus")
    failed_services=()
    
    for service in "${services[@]}"; do
        systemctl is-active --quiet "$service"
        if [ $? -ne 0 ]; then
            log_message "WARNING: Service $service is not running"
            failed_services+=("$service")
        fi
    done
    
    if [ ${#failed_services[@]} -gt 0 ]; then
        return 1
    fi
    
    log_message "All critical services are running"
    return 0
}

send_alert() {
    local subject="System Alert: $(hostname)"
    local body="The following issues were detected:\n\n$1"
    
    log_message "Sending alert email to $alert_email"
    echo -e "$body" | mail -s "$subject" "$alert_email"
}

# Main health check
log_message "Starting system health check"

issues=""

if ! check_disk_space; then
    issues+="- High disk usage detected\n"
fi

if ! check_memory; then
    issues+="- High memory usage detected\n"
fi

if ! check_load_average; then
    issues+="- High system load detected\n"
fi

if ! check_critical_services; then
    issues+="- Critical services are down\n"
fi

# Send alert if issues were found
if [ -n "$issues" ]; then
    send_alert "$issues"
    log_message "Health check detected issues"
    exit 1
else
    log_message "Health check passed - system healthy"
    exit 0
fi
```

### **2. Log Analysis Script**

```bash
#!/bin/bash

# Parse application logs for errors and generate a summary report
# Usage: ./analyze_logs.sh [log_file] [report_file]

# Default values
log_file=${1:-"/var/log/application.log"}
report_file=${2:-"./log_report_$(date +%Y%m%d).txt"}

# Check if log file exists
if [ ! -f "$log_file" ]; then
    echo "Error: Log file $log_file does not exist"
    exit 1
fi

# Create report header
cat > "$report_file" << EOF
========================================
LOG ANALYSIS REPORT
========================================
Log File: $log_file
Generated: $(date)
========================================

EOF

# Extract date range
first_log_date=$(head -1 "$log_file" | grep -oE "[0-9]{4}-[0-9]{2}-[0-9]{2}")
last_log_date=$(tail -1 "$log_file" | grep -oE "[0-9]{4}-[0-9]{2}-[0-9]{2}")

echo "Log Date Range: $first_log_date to $last_log_date" >> "$report_file"
echo "Total Log Entries: $(wc -l < "$log_file")" >> "$report_file"
echo "" >> "$report_file"

# Error summary
echo "ERROR SUMMARY:" >> "$report_file"
echo "----------------------------------------" >> "$report_file"
grep "ERROR" "$log_file" | cut -d ' ' -f 4- | sort | uniq -c | sort -nr | head -10 | while read -r count message; do
    echo "$count occurrences: $message" >> "$report_file"
done
echo "" >> "$report_file"

# Warning summary
echo "WARNING SUMMARY:" >> "$report_file"
echo "----------------------------------------" >> "$report_file"
grep "WARN" "$log_file" | cut -d ' ' -f 4- | sort | uniq -c | sort -nr | head -10 | while read -r count message; do
    echo "$count occurrences: $message" >> "$report_file"
done
echo "" >> "$report_file"

# Request pattern analysis
echo "TOP REQUESTED ENDPOINTS:" >> "$report_file"
echo "----------------------------------------" >> "$report_file"
grep "Request: " "$log_file" | grep -oE "path=[^ ]+" | cut -d= -f2 | sort | uniq -c | sort -nr | head -10 | while read -r count path; do
    echo "$count requests: $path" >> "$report_file"
done
echo "" >> "$report_file"

# Response time analysis
echo "SLOW REQUESTS (>1000ms):" >> "$report_file"
echo "----------------------------------------" >> "$report_file"
grep "Response time:" "$log_file" | grep -oE "Response time: [0-9]+ ms" | grep -oE "[0-9]+" | 
    awk '$1 > 1000 {print $1}' | sort -n | uniq -c | sort -nr | while read -r count time; do
    echo "$count requests took $time ms" >> "$report_file"
done
echo "" >> "$report_file"

# Error timeline
echo "ERROR TIMELINE:" >> "$report_file"
echo "----------------------------------------" >> "$report_file"
grep "ERROR" "$log_file" | grep -oE "^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}" | sort | uniq -c | 
    while read -r count datetime; do
    echo "$datetime:00 - $count errors" >> "$report_file"
done

echo "" >> "$report_file"
echo "========================================" >> "$report_file"
echo "End of Report" >> "$report_file"

echo "Log analysis complete. Report saved to $report_file"
```

### **3. Automated Deployment Script**

```bash
#!/bin/bash

# Automated deployment script for web application
# Usage: ./deploy.sh [version]

# Set strict error handling
set -e

# Configuration
APP_NAME="mywebapp"
DEPLOY_DIR="/var/www/$APP_NAME"
BACKUP_DIR="/var/www/backups"
REPO_URL="https://github.com/company/$APP_NAME.git"
LOG_FILE="/var/log/deployments.log"

# Version to deploy
VERSION=${1:-"master"}

# Functions
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

notify_slack() {
    local message="$1"
    local webhook_url="https://hooks.slack.com/services/TXXXXX/BXXXXX/XXXXXX"
    
    curl -s -X POST -H 'Content-type: application/json' \
        --data "{\"text\":\"$message\"}" \
        "$webhook_url" > /dev/null
}

create_backup() {
    local timestamp=$(date +%Y%m%d_%H%M%S)
    local backup_file="$BACKUP_DIR/${APP_NAME}_${timestamp}.tar.gz"
    
    log "Creating backup to $backup_file"
    
    if [ -d "$DEPLOY_DIR" ]; then
        mkdir -p "$BACKUP_DIR"
        tar -czf "$backup_file" -C "$DEPLOY_DIR" .
        log "Backup completed: $(du -h "$backup_file" | cut -f1)"
    else
        log "No existing deployment to backup"
    fi
}

deploy_application() {
    log "Deploying $APP_NAME version: $VERSION"
    
    # Create or clear deploy directory
    mkdir -p "$DEPLOY_DIR"
    rm -rf "$DEPLOY_DIR/*"
    
    # Clone the repository
    log "Cloning repository from $REPO_URL"
    git clone -b "$VERSION" --depth 1 "$REPO_URL" "$DEPLOY_DIR"
    
    # Install dependencies
    log "Installing dependencies"
    cd "$DEPLOY_DIR"
    npm install --production
    
    # Build application
    log "Building application"
    npm run build
    
    # Set permissions
    log "Setting permissions"
    chown -R www-data:www-data "$DEPLOY_DIR"
    chmod -R 755 "$DEPLOY_DIR"
}

restart_services() {
    log "Restarting services"
    systemctl restart nginx
    systemctl restart "$APP_NAME"
}

verify_deployment() {
    log "Verifying deployment"
    
    # Wait for application to start
    sleep 5
    
    # Check if service is running
    systemctl is-active --quiet "$APP_NAME"
    local service_status=$?
    
    # Check if web endpoint is responding
    http_status=$(curl -s -o /dev/null -w "%{http_code}" http://localhost/health)
    
    if [ $service_status -eq 0 ] && [ "$http_status" = "200" ]; then
        log "Deployment verification successful"
        return 0
    else
        log "Deployment verification failed. Service status: $service_status, HTTP status: $http_status"
        return 1
    fi
}

# Main deployment process
log "Starting deployment of $APP_NAME version $VERSION"
notify_slack "🚀 Deployment started for $APP_NAME version $VERSION"

# Step 1: Create backup
create_backup

# Step 2: Deploy new version
deploy_application

# Step 3: Restart services
restart_services

# Step 4: Verify deployment
if verify_deployment; then
    log "Deployment completed successfully"
    notify_slack "✅ Deployment of $APP_NAME version $VERSION completed successfully"
    exit 0
else
    log "Deployment failed"
    notify_slack "❌ Deployment of $APP_NAME version $VERSION failed"
    exit 1
fi
```

---

## 🎯 **Practical Exercise: Creating a System Monitoring Dashboard**

In this exercise, you'll create a shell script that generates a simple monitoring dashboard as HTML, showing key system metrics. This demonstrates how scripts can collect, process, and present operational data.

```bash
#!/bin/bash

# system_dashboard.sh - Generate a system monitoring dashboard as HTML
# Usage: ./system_dashboard.sh [output_file]

output_file=${1:-"/var/www/html/dashboard.html"}
interval=${2:-60}  # Update interval in seconds

generate_dashboard() {
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    
    # Get system metrics
    local hostname=$(hostname)
    local uptime=$(uptime -p)
    local kernel=$(uname -r)
    
    # CPU usage
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
    
    # Memory information
    local mem_total=$(free -m | awk 'NR==2{print $2}')
    local mem_used=$(free -m | awk 'NR==2{print $3}')
    local mem_percentage=$((mem_used * 100 / mem_total))
    
    # Disk usage
    local disk_info=$(df -h / | awk 'NR==2{print $5 " " $2 " " $3}')
    local disk_percentage=$(echo "$disk_info" | cut -d' ' -f1 | tr -d '%')
    local disk_total=$(echo "$disk_info" | cut -d' ' -f2)
    local disk_used=$(echo "$disk_info" | cut -d' ' -f3)
    
    # Network stats
    local connections=$(netstat -ant | wc -l)
    local established=$(netstat -ant | grep ESTABLISHED | wc -l)
    
    # Process information
    local process_count=$(ps aux | wc -l)
    local process_top=$(ps aux --sort=-%cpu | head -6 | tail -5 | awk '{print $11 " (" $3 "% CPU, " $4 "% MEM)"}')
    
    # Generate HTML
    cat > "$output_file" << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>System Dashboard - $hostname</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .dashboard {
            max-width: 1000px;
            margin: 0 auto;
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
        .metrics {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-bottom: 20px;
        }
        .metric-card {
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .metric-title {
            font-weight: bold;
            margin-bottom: 10px;
            color: #555;
        }
        .progress-bar {
            height: 20px;
            background-color: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
            margin-top: 10px;
        }
        .progress-fill {
            height: 100%;
            border-radius: 10px;
        }
        .processes {
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .footer {
            text-align: center;
            font-size: 12px;
            color: #777;
            margin-top: 20px;
        }
        .refresh-link {
            display: block;
            text-align: center;
            margin: 20px 0;
        }
    </style>
    <meta http-equiv="refresh" content="$interval">
</head>
<body>
    <div class="dashboard">
        <div class="header">
            <h1>System Dashboard - $hostname</h1>
            <p>Last updated: $timestamp</p>
            <p>Uptime: $uptime | Kernel: $kernel</p>
        </div>
        
        <div class="metrics">
            <div class="metric-card">
                <div class="metric-title">CPU Usage</div>
                <div class="metric-value">$cpu_usage%</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: $cpu_usage%; background-color: $([ $(echo "$cpu_usage > 80" | bc -l) -eq 1 ] && echo "#ff4d4d" || echo "#4caf50");"></div>
                </div>
            </div>
            
            <div class="metric-card">
                <div class="metric-title">Memory Usage</div>
                <div class="metric-value">$mem_used MB / $mem_total MB ($mem_percentage%)</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: $mem_percentage%; background-color: $([ "$mem_percentage" -gt 80 ] && echo "#ff4d4d" || echo "#2196f3");"></div>
                </div>
            </div>
            
            <div class="metric-card">
                <div class="metric-title">Disk Usage</div>
                <div class="metric-value">$disk_used / $disk_total ($disk_percentage%)</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: $disk_percentage%; background-color: $([ "$disk_percentage" -gt 80 ] && echo "#ff4d4d" || echo "#ff9800");"></div>
                </div>
            </div>
            
            <div class="metric-card">
                <div class="metric-title">Network Connections</div>
                <div class="metric-value">Total: $connections | Established: $established</div>
            </div>
        </div>
        
        <div class="processes">
            <div class="metric-title">Top CPU Processes (Total: $process_count)</div>
            <ul>
EOF

    # Add process list to HTML
    for process in $process_top; do
        echo "<li>$process</li>" >> "$output_file"
    done

    # Complete HTML
    cat >> "$output_file" << EOF
            </ul>
        </div>
        
        <div class="footer">
            <p>Generated by system_dashboard.sh script | Refresh interval: ${interval}s</p>
        </div>
    </div>
</body>
</html>
EOF

    echo "Dashboard updated at $timestamp"
}

# Create initial dashboard
generate_dashboard

# If running interactively with second parameter, update at intervals
if [ -t 0 ] && [ -n "$interval" ]; then
    echo "Dashboard will refresh every $interval seconds. Press Ctrl+C to stop."
    while true; do
        sleep $interval
        generate_dashboard
    done
fi
```

To use this script:

1. Save it as `system_dashboard.sh`
2. Make it executable: `chmod +x system_dashboard.sh`
3. Run it: `./system_dashboard.sh /var/www/html/dashboard.html 30`
   - First parameter is the output file location
   - Second parameter is the refresh interval in seconds

This script demonstrates several important concepts:

- Using variables to make the script configurable
- Collecting system metrics with various commands
- Processing and formatting data for presentation
- Generating HTML output from bash
- Running in an interactive mode with a refresh loop

As an SRE, you could extend this script to include additional monitoring metrics, send alerts on threshold violations, or integrate with existing monitoring systems.

---

## 📝 **Quiz: Shell Scripting Fundamentals**

Test your understanding of today's material:

1. What line should begin a bash script file to specify which interpreter to use?
   - a) `#!/bin/sh`
   - b) `#!/bin/bash`
   - c) `#/bin/bash`
   - d) `bash:`

2. How would you access the third command line argument in a shell script?
   - a) `$0`
   - b) `$1`
   - c) `$2`
   - d) `$3`

3. Which statement correctly checks if a file exists and is writable?
   - a) `if [ -e $file && -w $file ]; then`
   - b) `if [ -e $file -a -w $file ]; then`
   - c) `if [ -e $file ] && [ -w $file ]; then`
   - d) `if test -e $file -w $file; then`

4. What is the correct syntax for a for loop that processes each item in an array?
   - a) `for item in "${array[@]}"; do`
   - b) `for item in $array; do`
   - c) `for (item in array); do`
   - d) `foreach item in $array; do`

5. Which command captures the output of a command and assigns it to a variable?
   - a) `variable = $(command)`
   - b) `variable=$(command)`
   - c) `variable=`command``
   - d) `variable="command"`

---

## ❓ **FAQ for SREs: Shell Scripting**

**Q1: How should I structure larger shell scripts to make them maintainable?**

**A:** For larger scripts, follow these practices:

1. **Use a standard structure:**

   ```bash
   #!/bin/bash
   
   # Script metadata comment block (purpose, usage, author, date)
   
   # Constants and configuration
   CONFIG_FILE="/etc/myapp.conf"
   LOG_DIR="/var/log/myapp"
   
   # Function definitions
   function_name() {
     # ...
   }
   
   # Main execution begins here
   main() {
     # Script logic
   }
   
   # Call main function
   main "$@"
   ```

2. **Modularize with functions:**
   - Group related operations into functions
   - Keep functions focused on a single responsibility
   - Use meaningful function names

3. **Source common libraries:**

   ```bash
   # In a common library file (common.sh)
   log() {
     echo "[$(date)] $1" >> "$LOG_FILE"
   }
   
   # In your main script
   source /path/to/common.sh
   ```

4. **Use version control:**
   - Keep scripts in a git repository
   - Document changes with good commit messages
   - Use branches for feature development

Following these practices makes scripts easier to maintain, debug, and collaborate on.

**Q2: What's the most effective way to debug shell scripts?**

**A:** Use these techniques for effective debugging:

1. **Enable debug mode:**

   ```bash
   # At the beginning of the script
   set -x  # Print commands and arguments as they are executed
   
   # Or run the script with 
   bash -x ./script.sh
   ```

2. **Set strict error handling:**

   ```bash
   set -e  # Exit immediately if a command fails
   set -u  # Exit if an undefined variable is used
   set -o pipefail  # Fail if any command in a pipeline fails
   ```

3. **Add debug logging:**

   ```bash
   debug() {
     if [ "$DEBUG" = "true" ]; then
       echo "[DEBUG] $1" >&2
     fi
   }
   
   # Then in your script
   debug "Value of variable: $variable"
   ```

4. **Check syntax without executing:**

   ```bash
   bash -n script.sh
   ```

5. **Use a linter like ShellCheck:**

   ```bash
   shellcheck script.sh
   ```

These techniques help identify issues before they cause problems in production environments.

**Q3: How can I parse complex data formats like JSON in shell scripts?**

**A:** While bash isn't ideal for complex data formats, several approaches work:

1. **Using `jq` for JSON parsing:**

   ```bash
   # Install jq
   apt-get install jq
   
   # Parse JSON
   api_response=$(curl -s https://api.example.com/data)
   status=$(echo "$api_response" | jq -r '.status')
   items=$(echo "$api_response" | jq -r '.items[]')
   
   # Iterate through items
   echo "$api_response" | jq -r '.items[] | .name' | while read -r name; do
     echo "Processing item: $name"
   done
   ```

2. **For YAML, use `yq`:**

   ```bash
   # Parse YAML
   config_value=$(yq r config.yaml 'services.web.port')
   ```

3. **For XML, use `xmlstarlet`:**

   ```bash
   # Extract value from XML
   server_name=$(xmlstarlet sel -t -v "//server/name" config.xml)
   ```

4. **Simple parsing with `grep`, `sed`, and `awk`:**

   ```bash
   # Extract value from a key=value file
   port=$(grep "^port=" config.ini | sed 's/port=//')
   ```

When working with complex data regularly, consider scripting in languages like Python that have better native support for these formats.

**Q4: How do I handle secrets and sensitive data in shell scripts?**

**A:** Handle sensitive data securely using these approaches:

1. **Never hardcode secrets:**

   ```bash
   # Bad
   PASSWORD="SecretP@ssw0rd"
   
   # Good
   PASSWORD=$(cat /path/to/secret/file)  # File with restricted permissions
   ```

2. **Use environment variables:**

   ```bash
   # In a secure wrapper script or CI/CD system
   export DATABASE_PASSWORD="secret"
   
   # In your script
   if [ -z "$DATABASE_PASSWORD" ]; then
     echo "Error: Required secret DATABASE_PASSWORD is not set"
     exit 1
   fi
   ```

3. **Use secret management tools:**

   ```bash
   # Fetch from HashiCorp Vault
   PASSWORD=$(vault kv get -field=password secret/database)
   
   # Or from AWS Secrets Manager
   PASSWORD=$(aws secretsmanager get-secret-value --secret-id db-password --query SecretString --output text)
   ```

4. **Mask secrets in logs:**

   ```bash
   # Redact sensitive info in logs
   log_cmd_output() {
     output=$("$@" 2>&1)
     # Redact passwords and tokens
     sanitized=$(echo "$output" | sed -E 's/(password|token|key)=\S+/\1=REDACTED/g')
     echo "$sanitized"
   }
   ```

5. **Clear variables when done:**

   ```bash
   # Clear sensitive data when no longer needed
   PASSWORD=""
   ```

These practices help prevent accidental exposure of sensitive information.

---

## 🚧 **Common Issues and Troubleshooting**

### **Issue 1: Script Permissions Problems**

**Symptoms:**

- "Permission denied" when trying to execute a script
- Script runs with unexpected permissions

**Causes:**

- Incorrect execute permission setting
- Script running as the wrong user
- Issues with setuid or setgid bits

**Solutions:**

```bash
# Make script executable
chmod +x script.sh

# Check who owns the script
ls -l script.sh

# If needed, change ownership
chown appropriate_user:appropriate_group script.sh

# Check if script is running with correct permissions
sudo -u expected_user ./script.sh
```

### **Issue 2: Variable Expansion Problems**

**Symptoms:**

- Variables not expanding as expected
- "Bad substitution" errors
- Empty variable values

**Causes:**

- Incorrect quoting
- Using single quotes instead of double quotes
- Trying to use array elements incorrectly

**Solutions:**

```bash
# Proper variable expansion with double quotes
echo "Value: $variable"  # Correct

# Problems with single quotes
echo 'Value: $variable'  # Incorrect - will print literal $variable

# Debugging variable content
echo "Variable content: [$variable]"

# Checking if variable is defined and non-empty
if [ -z "$variable" ]; then
  echo "Variable is empty or undefined"
fi

# Correct array usage
for item in "${array[@]}"; do  # Correct
  echo "$item"
done
```

---

## 🔄 **Real-World SRE Scenario: Automated Database Backup Script**

**Situation:** You need to create a robust automated database backup solution that runs nightly, verifies the backup integrity, rotates old backups, and sends notifications on completion or failure.

**SRE Response Using Today's Commands:**

```bash
#!/bin/bash

#######################################
# Database Backup Script for Production
# 
# This script:
# - Creates nightly database backups
# - Verifies backup integrity
# - Rotates old backups
# - Sends email notifications
#
# Usage: ./db_backup.sh [config_file]
#######################################

# Exit on error
set -e

# Default configuration
CONFIG_FILE=${1:-"/etc/db_backup.conf"}
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="/var/log/db_backup/backup_${TIMESTAMP}.log"
NOTIFICATION_EMAIL="sre-team@example.com"
BACKUP_DIR="/backup/databases"
RETENTION_DAYS=14
DB_HOST="localhost"
DB_PORT="3306"
DB_USER="backup_user"
DB_NAME="production_db"

# Load configuration if available
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
fi

# Ensure log directory exists
mkdir -p "$(dirname "$LOG_FILE")"

# Setup logging
log() {
    local level=$1
    local message=$2
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$timestamp] [$level] $message" | tee -a "$LOG_FILE"
}

# Initialize log
log "INFO" "Starting database backup process"
log "INFO" "Using configuration: $CONFIG_FILE"

# Handle errors and send notifications
trap 'handle_error $LINENO' ERR

handle_error() {
    local line_no=$1
    log "ERROR" "Backup failed at line $line_no"
    
    # Send error notification
    send_notification "❌ Database Backup FAILED" "Error occurred at line $line_no. Check log: $LOG_FILE"
    
    exit 1
}

# Send notification
send_notification() {
    local subject="$1"
    local message="$2"
    
    log "INFO" "Sending notification: $subject"
    
    # Send email
    echo -e "Subject: $subject\n\n$message\n\nServer: $(hostname)\nTimestamp: $(date)\n\nLog tail:\n$(tail -n 10 "$LOG_FILE")" | \
        sendmail "$NOTIFICATION_EMAIL"
    
    # If you have Slack integration
    if [ -n "$SLACK_WEBHOOK" ]; then
        curl -s -X POST -H 'Content-type: application/json' \
            --data "{\"text\":\"$subject\n$message\"}" \
            "$SLACK_WEBHOOK"
    fi
}

# Verify database connection
verify_db_connection() {
    log "INFO" "Verifying database connection"
    
    # Test MySQL connection
    if ! mysql -h "$DB_HOST" -P "$DB_PORT" -u "$DB_USER" -p"$DB_PASSWORD" -e "SELECT 1" >/dev/null 2>&1; then
        log "ERROR" "Cannot connect to database"
        exit 1
    fi
}

# Create backup directory
prepare_backup_dir() {
    log "INFO" "Preparing backup directory: $BACKUP_DIR"
    
    # Ensure backup directory exists
    mkdir -p "$BACKUP_DIR"
    
    # Set secure permissions
    chmod 700 "$BACKUP_DIR"
}

# Perform the backup
create_backup() {
    local backup_file="$BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql.gz"
    
    log "INFO" "Creating backup: $backup_file"
    
    # Performance optimization: use single transaction for InnoDB
    mysqldump --single-transaction --quick --lock-tables=false \
        -h "$DB_HOST" -P "$DB_PORT" -u "$DB_USER" -p"$DB_PASSWORD" \
        "$DB_NAME" | gzip > "$backup_file"
    
    # Check if backup succeeded
    if [ $? -eq 0 ] && [ -f "$backup_file" ]; then
        log "INFO" "Backup created successfully: $(du -h "$backup_file" | cut -f1)"
        echo "$backup_file"  # Return the backup filename
    else
        log "ERROR" "Backup creation failed"
        exit 1
    fi
}

# Verify the backup integrity
verify_backup() {
    local backup_file="$1"
    
    log "INFO" "Verifying backup integrity: $backup_file"
    
    # Check if the gzip file is valid
    if ! gzip -t "$backup_file"; then
        log "ERROR" "Backup file is corrupted (gzip test failed)"
        exit 1
    fi
    
    # Check if the SQL dump has expected structures
    tables_count=$(zcat "$backup_file" | grep -c "CREATE TABLE" || true)
    
    if [ "$tables_count" -lt 1 ]; then
        log "ERROR" "Backup verification failed: No tables found in backup"
        exit 1
    fi
    
    log "INFO" "Backup verified successfully (contains $tables_count tables)"
}

# Create a checksum file
create_checksum() {
    local backup_file="$1"
    
    log "INFO" "Creating checksum for: $backup_file"
    
    # Create SHA256 checksum
    sha256sum "$backup_file" > "${backup_file}.sha256"
    
    log "INFO" "Checksum created: ${backup_file}.sha256"
}

# Rotate old backups
rotate_backups() {
    log "INFO" "Rotating backups older than $RETENTION_DAYS days"
    
    # Find and delete old backups
    find "$BACKUP_DIR" -name "${DB_NAME}_*.sql.gz" -type f -mtime +$RETENTION_DAYS -delete
    find "$BACKUP_DIR" -name "${DB_NAME}_*.sql.gz.sha256" -type f -mtime +$RETENTION_DAYS -delete
    
    # Count remaining backups
    local remaining=$(find "$BACKUP_DIR" -name "${DB_NAME}_*.sql.gz" -type f | wc -l)
    log "INFO" "Rotation complete. Remaining backups: $remaining"
}

# Main backup process
main() {
    local start_time=$(date +%s)
    
    # Step 1: Verify database connection
    verify_db_connection
    
    # Step 2: Prepare backup directory
    prepare_backup_dir
    
    # Step 3: Create backup
    local backup_file=$(create_backup)
    
    # Step 4: Verify backup integrity
    verify_backup "$backup_file"
    
    # Step 5: Create checksum
    create_checksum "$backup_file"
    
    # Step 6: Rotate old backups
    rotate_backups
    
    # Calculate execution time
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    
    log "INFO" "Backup completed successfully in $duration seconds"
    
    # Send success notification
    local backup_size=$(du -h "$backup_file" | cut -f1)
    send_notification "✅ Database Backup Successful" \
        "Database: $DB_NAME\nBackup: $backup_file\nSize: $backup_size\nDuration: $duration seconds"
}

# Execute the main function
main

exit 0
```

This comprehensive backup script demonstrates many of the shell scripting concepts covered today:

- Function-based organization
- Error handling with traps
- Logging
- Configuration management
- Data verification
- Notification system
- Process orchestration

It's a real-world example of how shell scripting enables SREs to create reliable automation for critical operational tasks.

---

## 📚 **Further Learning Resources**

- [The Linux Command Line: A Complete Introduction](https://linuxcommand.org/tlcl.php) - Excellent book with in-depth chapters on bash scripting
- [Advanced Bash-Scripting Guide](https://tldp.org/LDP/abs/html/) - Comprehensive guide to advanced shell scripting techniques
- [ShellCheck](https://www.shellcheck.net/) - Online tool to analyze shell scripts for common errors and best practices
- [Bash Hackers Wiki](https://wiki.bash-hackers.org/) - Community-driven documentation for bash scripting
- [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html) - Best practices for writing shell scripts in a professional environment
- [Google SRE Book - Chapter 7: The Evolution of Automation at Google](https://sre.google/sre-book/automation-at-google/)
- [Linux Foundation Certifications](https://training.linuxfoundation.org/certification-catalog/) - For those interested in formal Linux certifications

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

Happy Linux adventures!
