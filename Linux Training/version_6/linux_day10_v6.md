# 🚀 **Linux SRE Day 10: Shell Scripting Basics & Advanced Concepts**

---

## 📌 **Introduction**

### **Why Shell Scripting Matters for SREs**

Welcome to **Day 10** of the Linux SRE Training Path. Today’s focus is on **Shell Scripting**—the glue that holds together many system administration and SRE activities. By automating routine tasks, you reduce human error, save time, and increase overall reliability. Mastering shell scripting is a key step in evolving your skill set beyond individual commands and into robust automation.

### **Objectives by Skill Level**

- **Beginner** (3 key goals):
  1. Understand basic shell script structure (shebang, `chmod +x`, etc.)
  2. Create and use variables effectively
  3. Write simple loops (`for`, `while`) and conditionals (`if`, `case`)

- **Intermediate** (3 key goals):
  1. Incorporate command substitution and environment variables
  2. Implement debugging techniques (`set -x`, logs) and handle errors properly
  3. Use more advanced loops and branching (nested loops, robust conditionals)

- **SRE-Level** (3 key goals):
  1. Build production-ready scripts with logging, error handling, and security considerations
  2. Automate complex tasks like monitoring, health checks, and deployments
  3. Integrate shell scripts into broader SRE workflows (CI/CD, scaling, incident response)

### **Connection to Previous and Future Topics**

- **Previously** (Day 9): You studied archiving, compression, and package management. Those are crucial building blocks for packaging logs and resources—activities you’ll automate in shell scripts.
- **Upcoming**: We’ll move into **Configuration Management and Infrastructure as Code**, where your scripting skills will integrate with tools like Ansible, Puppet, or Chef for large-scale automation.

---

## 📚 **Core Concepts**

Shell scripting automates the commands and logic you’d normally execute interactively. Below are some essential concepts:

1. **Script Structure**: The shebang (`#!/bin/bash`) and execution permissions (`chmod +x`).
2. **Variables**: Used to store data for reusability and clarity.
3. **Command Substitution**: Embedding command output directly in scripts.
4. **Loops**: Automate repetition (file processing, server checks).
5. **Conditionals**: Make decisions based on system state or user input.
6. **Environment Variables**: Provide system-wide or session-wide context.
7. **Error Handling & Debugging**: Techniques like `set -e`, `set -x`, and traps for robust automation.
8. **Security & Performance**: Scripts can run with elevated privileges, so safety is key. Consider resource usage in loops and repeated commands.
9. **SRE Application**: Use scripts to reduce toil, ensure consistent deployments, run health checks, and manage log analysis.

---

## 💻 **Command Breakdown**

Below are five core scripting topics, explained with purpose, syntax tables, tiered examples, and instructional notes.

### 1. **Command: Variables (Storing and Referencing Data)**

**Command Overview:**
Variables in shell scripts store data like paths, user names, or environment parameters. SREs use them to parameterize scripts for different servers, handle dynamic log paths, or store credentials (with caution).

**Syntax & Flags:**

| Flag/Option | Syntax Example           | Description                                                       | SRE Usage Context                                       |
|-------------|--------------------------|-------------------------------------------------------------------|---------------------------------------------------------|
| `=`         | `name="Alice"`         | Assign a value to a variable (no spaces around `=`)               | Setting default parameters (e.g., backup or deploy tasks)|
| `$variable` | `echo "$variable"`     | Expands the variable’s value                                      | Referencing environment-specific details                |
| `export`    | `export MYVAR="prod"`  | Makes a variable available to child processes                     | Setting environment context for sub-scripts             |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  #!/bin/bash
  name="Alice"
  echo "Hello, $name!"
  # Output:
  # Hello, Alice!
  ```

  *Explanation*: A simple example assigning a string and printing it.

- 🟡 **Intermediate Example:**

  ```bash
  #!/bin/bash
  servername="web-prod"
  backup_dir="/var/backups"

  tar -czf "${backup_dir}/${servername}_logs.tar.gz" /var/log/$servername
  echo "Backup completed for $servername!"
  # Example Output:
  # Backup completed for web-prod!
  ```

  *Explicit context*: Parameterizing script paths makes them easier to maintain across environments.

- 🔴 **SRE-Level Example:**

  ```bash
  #!/bin/bash
  : "${APP_ENV:?Error: APP_ENV not set}"  # Fails if APP_ENV is missing

  log_file="/var/log/${APP_ENV}_app.log"
  if [ -f "$log_file" ]; then
    echo "Processing $log_file"
  else
    echo "No log file found for environment $APP_ENV"
  fi
  # Example Output:
  # Processing /var/log/staging_app.log
  ```

  *Explicit context*: This ensures critical environment variables are set, preventing mistakes in production.

**Instructional Notes:**

- 🧠 **Beginner Tip:** No spaces around `=` during assignment (e.g., `name="Alice"`).
- 🧠 **Beginner Tip:** Double-quote variables like `"$var"` to preserve whitespace.

- 🔧 **SRE Insight:** Use consistent naming (e.g., `DB_HOST`, `DB_USER`) for clarity and maintenance.
- 🔧 **SRE Insight:** For large scripts, consider default values using parameter expansion: `"${var:-default_value}"`.

- ⚠️ **Common Pitfall:** Forgetting `export` can cause child processes not to see the variable.
- ⚠️ **Common Pitfall:** Accidentally adding spaces around `=` breaks assignments.

- 🚨 **Security Note:** Do not store plain-text passwords in variables. Consider secrets managers.
- 💡 **Performance Impact:** Generally minimal, but extremely large strings can slow down loops.

---

### 2. **Command: Command Substitution (Dynamic Scripting)**

**Command Overview:**
Command substitution embeds a command’s output into another command or variable. For SREs, this is crucial when capturing dynamic data like current timestamps, resource usage, or service statuses.

**Syntax & Flags:**

| Flag/Option      | Syntax Example        | Description                                              | SRE Usage Context                                      |
|------------------|-----------------------|----------------------------------------------------------|---------------------------------------------------------|
| `$(command)`     | `timestamp=$(date)`  | Captures stdout of `command` in a variable               | Automating file naming with date/time stamps            |
| Backtick syntax  | `` `command` ``      | Older style, can be problematic with nested commands     | Legacy scripts, but often replaced by `$(...)`          |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  #!/bin/bash
  today=$(date)
  echo "The date is $today"
  # Output:
  # The date is Mon Mar 30 12:45:02 UTC 2025
  ```

  *Explanation*: Embedding the result of `date` in a variable.

- 🟡 **Intermediate Example:**

  ```bash
  #!/bin/bash
  file_count=$(ls -1 /var/log/*.log | wc -l)
  echo "There are $file_count log files in /var/log."
  # Example Output:
  # There are 15 log files in /var/log.
  ```

  *Explicit context*: SREs need to track log counts to manage rotations.

- 🔴 **SRE-Level Example:**

  ```bash
  #!/bin/bash
  cpu_idle=$(top -bn1 | grep "Cpu(s)" | awk '{print $8}' | cut -d'.' -f1)
  cpu_usage=$((100 - cpu_idle))

  if [ $cpu_usage -gt 80 ]; then
    echo "HIGH CPU Alert! Current Usage: ${cpu_usage}%"
  else
    echo "CPU Usage: ${cpu_usage}%"
  fi
  # Example Output:
  # HIGH CPU Alert! Current Usage: 92%
  ```

  *Explicit context*: Monitoring CPU usage dynamically and responding if it crosses a threshold.

**Instructional Notes:**

- 🧠 **Beginner Tip:** Prefer `$(...)` over backticks for readability and nesting.
- 🧠 **Beginner Tip:** Store command outputs in variables to reuse them.

- 🔧 **SRE Insight:** For frequent checks (like in loops), consider more efficient parsing or direct system calls.
- 🔧 **SRE Insight:** Validate the output of the command before acting on it to avoid parsing errors.

- ⚠️ **Common Pitfall:** Large data in command substitution can hurt performance. Use direct pipes if needed.
- ⚠️ **Common Pitfall:** Not handling error codes. If the command fails, you might store unexpected data.

- 🚨 **Security Note:** Be wary of user input in command substitution. Sanitize or escape to prevent injection.
- 💡 **Performance Impact:** Each substitution spawns a subshell. Minimizing them can improve speed.

---

### 3. **Command: Loops (For, While)**

**Command Overview:**
Loops automate repetitive tasks. For SREs, they’re handy when checking multiple servers, processing multiple files, or running a batch operation across a fleet.

**Syntax & Flags:**

| Flag/Option | Syntax Example                | Description                                             | SRE Usage Context                                     |
|-------------|-------------------------------|---------------------------------------------------------|-------------------------------------------------------|
| `for`       | `for i in {1..5}; do ... done` | Iterates over a range or list                           | Checking multiple hosts or log files                 |
| `while`     | `while [ condition ]; do ... done` | Repeats until the condition fails                  | Monitoring processes until they stabilize            |
| `break`     | `break`                       | Exits the current loop immediately                     | Early termination on error                           |
| `continue`  | `continue`                    | Skips current iteration                                | Skips invalid entries in a batch operation           |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  #!/bin/bash
  for i in {1..3}; do
    echo "Count: $i"
  done
  # Output:
  # Count: 1
  # Count: 2
  # Count: 3
  ```

  *Explanation*: Basic numeric loop.

- 🟡 **Intermediate Example:**

  ```bash
  #!/bin/bash
  servers=("web-01" "web-02" "db-01")

  for s in "${servers[@]}"; do
    echo "Pinging $s..."
    ping -c 1 "$s" &> /dev/null
    if [ $? -eq 0 ]; then
      echo "$s is reachable"
    else
      echo "$s is offline"
    fi
    echo "---"
  done
  # Example Output:
  # Pinging web-01...
  # web-01 is reachable
  # ---
  # Pinging web-02...
  # web-02 is offline
  # ---
  # Pinging db-01...
  # db-01 is reachable
  # ---
  ```

  *Explicit context*: Checking connectivity across multiple servers.

- 🔴 **SRE-Level Example:**

  ```bash
  #!/bin/bash
  while true; do
    active_sessions=$(ss -t | grep ESTAB | wc -l)
    echo "Active TCP sessions: $active_sessions"

    if [ "$active_sessions" -gt 100 ]; then
      echo "High load: $active_sessions sessions"
      # Potential alert logic here
    fi

    sleep 30  # Wait and check again
  done
  # Example Output:
  # Active TCP sessions: 42
  # Active TCP sessions: 101
  # High load: 101 sessions
  ```

  *Explicit context*: Continuous monitoring loop for network connections.

**Instructional Notes:**

- 🧠 **Beginner Tip:** Always include a way out in `while true` loops (break or `sleep` + user break).
- 🧠 **Beginner Tip:** Quote variables to handle filenames with spaces (`for file in "*.log"`).

- 🔧 **SRE Insight:** Combine loops with parallel execution (e.g., `xargs -P`) for large-scale tasks.
- 🔧 **SRE Insight:** Use logs or counters inside loops to track progress, especially for production tasks.

- ⚠️ **Common Pitfall:** Infinite loops can spike CPU usage if not carefully controlled.
- ⚠️ **Common Pitfall:** Using unquoted expansions can break loops when encountering special characters.

- 🚨 **Security Note:** Validate input lists to avoid malicious or unexpected items in loops.
- 💡 **Performance Impact:** Loops that spawn many processes can be expensive. Consider in-process operations.

---

### 4. **Command: Conditionals (If, Case)**

**Command Overview:**
Conditionals let you adapt script behavior based on system state. SREs leverage conditionals to check resource levels, respond to errors, or handle configuration differences.

**Syntax & Flags:**

| Flag/Option  | Syntax Example                              | Description                                                  | SRE Usage Context                                 |
|--------------|---------------------------------------------|--------------------------------------------------------------|---------------------------------------------------|
| `if`         | `if [ "$var" = "something" ]; then ... fi` | Basic branching                                             | Checking environment or input                     |
| `elif`       | `elif [ condition ]; then ... fi`           | Adds another condition if the previous one fails             | Multi-level checks (warn/critical)               |
| `else`       | `else ... fi`                               | Fallback condition                                         | Default or error-handling path                   |
| `case`       | `case $var in pattern) ... ;; esac`          | Pattern matching for multiple discrete values               | Handling multiple environment names or error codes|

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  #!/bin/bash
  read -p "Enter a number: " number

  if [ $number -gt 10 ]; then
    echo "$number is greater than 10!"
  else
    echo "$number is 10 or less."
  fi
  # Example Interaction:
  # Enter a number: 9
  # 9 is 10 or less.
  ```

  *Explanation*: Simple numeric comparison.

- 🟡 **Intermediate Example:**

  ```bash
  #!/bin/bash
  status_code=404

  case $status_code in
    200)
      echo "OK: Everything is good"
      ;;
    404)
      echo "Not Found: Resource missing"
      ;;
    500)
      echo "Internal Server Error: Check logs"
      ;;
    *)
      echo "Unhandled status code: $status_code"
      ;;
  esac
  # Example Output:
  # Not Found: Resource missing
  ```

  *Explicit context*: Handling different HTTP responses in a script.

- 🔴 **SRE-Level Example:**

  ```bash
  #!/bin/bash
  mem_free=$(free -m | awk 'NR==2{print $4}')
  if [ "$mem_free" -lt 512 ]; then
    echo "CRITICAL: Memory below 512 MB!"
    # Trigger alert, scale up, or log event
  elif [ "$mem_free" -lt 1024 ]; then
    echo "WARNING: Memory below 1 GB"
  else
    echo "Memory levels OK."
  fi
  # Example Output:
  # CRITICAL: Memory below 512 MB!
  ```

  *Explicit context*: Different thresholds for memory usage tied to escalation policies.

**Instructional Notes:**

- 🧠 **Beginner Tip:** Close an `if` block with `fi` and a `case` block with `esac`.
- 🧠 **Beginner Tip:** Use integer comparisons like `-lt`, `-gt` for numbers, and `=` or `!=` for strings.

- 🔧 **SRE Insight:** Chain multiple conditions (CPU < 80%, memory > 1GB) to ensure robust gating.
- 🔧 **SRE Insight:** Use logging within condition blocks to track decision points in production.

- ⚠️ **Common Pitfall:** Using `==` incorrectly for numbers. Also mixing up `[ $var -eq "text" ]` can fail.
- ⚠️ **Common Pitfall:** Missing a `;;` in `case` blocks can cause fall-through logic.

- 🚨 **Security Note:** Validate external inputs before performing system actions in an `if`.
- 💡 **Performance Impact:** Minimal overhead for checking conditions; more complex logic can hamper readability.

---

### 5. **Command: Environment Variables (Global Configuration)**

**Command Overview:**
Environment variables are accessible to child processes and unify configuration across sessions. SREs set environment variables to standardize runs across dev, staging, and prod.

**Syntax & Flags:**

| Flag/Option      | Syntax Example                | Description                                             | SRE Usage Context                                 |
|------------------|-------------------------------|---------------------------------------------------------|---------------------------------------------------|
| `export`         | `export MYVAR="some_value"` | Makes a variable available to child processes           | Setting environment context for sub-scripts       |
| `env`            | `env`                         | Lists all current environment variables                 | Debugging environment issues                      |
| `printenv`       | `printenv PATH`               | Prints a specific environment variable                  | Checking values within scripts                    |
| `.bashrc`, `.zshrc` | `vi ~/.bashrc`                | Shell startup files for defining persistent variables   | Configuring user-level environment               |

**Tiered Examples:**

- 🟢 **Beginner Example:**

  ```bash
  #!/bin/bash
  export MYAPP_PORT=8080
  echo "MYAPP_PORT is set to $MYAPP_PORT"
  # Output:
  # MYAPP_PORT is set to 8080
  ```

  *Explanation*: Exports a variable for child processes to see.

- 🟡 **Intermediate Example:**

  ```bash
  #!/bin/bash
  if [ -z "$DB_HOST" ]; then
    echo "Please set DB_HOST before running this script."
    exit 1
  fi

  echo "Connecting to database at $DB_HOST..."
  # Proceed with further commands
  ```

  *Explicit context*: Ensures environment pre-conditions.

- 🔴 **SRE-Level Example:**

  ```bash
  #!/bin/bash
  # Source a dedicated environment file for production
  source /etc/myapp/env.production

  if [ "$APP_ENV" = "production" ]; then
    echo "Production environment loaded. PATH=$PATH"
  else
    echo "Environment mismatch: APP_ENV=$APP_ENV"
  fi
  # Example Output:
  # Production environment loaded. PATH=/usr/local/bin:/usr/bin:/bin:/opt/myapp/bin
  ```

  *Explicit context*: Large SRE environments keep config in consistent files so all services share the same references.

**Instructional Notes:**

- 🧠 **Beginner Tip:** To make variables persist, add `export VAR=value` to `~/.bashrc` or `~/.zshrc`.
- 🧠 **Beginner Tip:** Use `echo "$VAR"` or `printenv VAR` to confirm the variable is set.

- 🔧 **SRE Insight:** Keep environment files under version control (without secrets), and manage updates carefully.
- 🔧 **SRE Insight:** For secret data, rely on external secret managers or encrypted files with restricted permissions.

- ⚠️ **Common Pitfall:** Overriding `PATH` without including its original value can break commands.
- ⚠️ **Common Pitfall:** Having environment variables differ drastically between dev/staging/prod can cause deploy surprises.

- 🚨 **Security Note:** Avoid storing plaintext secrets in environment variables. Use secure injection or ephemeral storage.
- 💡 **Performance Impact:** Minimal to set environment variables, but large PATH or numerous variables can complicate scripts.

---

## 🛠️ **System Effects**

When writing shell scripts, be mindful of:

1. **Filesystem & Metadata**: Scripts may create or modify files, set permissions, or change ownership. This can impact backups, logs, and system stability.
2. **System Resources**: Loops or repeated commands can spike CPU or memory usage if not controlled. Large I/O (e.g., compressing gigabytes of logs) can stress disks.
3. **Security Implications**: Running scripts with `sudo` or elevated privileges can introduce risks if the script isn’t carefully validated.
4. **Monitoring & Visibility**: Scripts for log rotation or resource checks can help or hinder observability. Plan carefully to avoid losing vital data.

---

## 🎯 **Hands-On Exercises**

Below are exactly **3 exercises per tier**, designed to deepen your practical skills.

### **Beginner Exercises (3)**

1. **Hello Script**
   - Create a script `hello.sh`.
   - It should ask for your name (`read name`) and then print a welcome message.
   - Make it executable and run it: `chmod +x hello.sh && ./hello.sh`.

2. **Simple Math**
   - Write a script `math.sh`.
   - Prompt the user for two numbers.
   - Add them together using shell arithmetic: `sum=$((num1 + num2))`.
   - Print the result.

3. **File Checker**
   - Build a script `file_check.sh`.
   - Check if `data.txt` exists in the current directory.
   - If it does, print “File found!”; if not, print “No file.”

### **Intermediate Exercises (3)**

1. **Server Status Loop**
   - Create `check_servers.sh`.
   - Store an array of server names in a variable.
   - For each server, ping it and log the reachability in a file `server_status.log`.

2. **Backup Automation**
   - Write `auto_backup.sh`.
   - Use command substitution to generate a timestamp: `timestamp=$(date +%Y%m%d-%H%M%S)`.
   - Archive `/etc` into `/tmp/backups/backup-$timestamp.tar.gz`.
   - Test with different source directories.

3. **Conditional Cleanup**
   - Develop `cleanup_logs.sh`.
   - Check the size of each `.log` file in `/var/log`.
   - If size > 10 MB, compress it (e.g., `gzip`).
   - Otherwise, leave it as is.

### **SRE-Level Exercises (3)**

1. **Resource Threshold Monitor**
   - Implement `monitor_resources.sh`.
   - Check CPU, memory, and disk usage every 60 seconds.
   - If usage passes thresholds (e.g., CPU > 80%, memory < 512 MB, disk > 85%), display or email an alert.

2. **Environment-Based Deploy**
   - Build `deploy_app.sh`.
   - Use `APP_ENV` to decide which config file to deploy (e.g., `dev`, `staging`, `prod`).
   - Include error handling if `APP_ENV` is missing.

3. **Multi-Server Loop**
   - Write `distributed_cmd.sh`.
   - Read a list of remote servers from `servers.txt`.
   - For each, SSH and run a specified command, saving results locally.
   - Check for SSH connectivity issues and handle non-zero exit codes.

---

## 📝 **Quiz Questions**

### **Beginner Level (3–4)**

1. Which syntax is preferred for command substitution?
   - a) `` `command` ``  
   - b) `$(command)`  
   - c) `${command}`  

2. Which operator checks if a file named `myfile` exists?
   - a) `[ -x myfile ]`  
   - b) `[ -f myfile ]`  
   - c) `[ file myfile ]`  

3. How do you export a variable named `DB_HOST`?
   - a) `DB_HOST = 1.2.3.4`
   - b) `set DB_HOST=1.2.3.4`
   - c) `export DB_HOST=1.2.3.4`

4. Which line is needed at the start of a bash script?
   - a) `#!/bin/sh`
   - b) `#!/bin/bash`
   - c) `bash script`

### **Intermediate Level (3–4)**

1. Given `servers=("srv1" "srv2" "srv3")`, how do you loop through them?
   - a) `for s in ${servers}; do`
   - b) `for s in "${servers[@]}"; do`
   - c) `foreach s in servers; do`

2. How do you embed the current date/time in your script output?
   - a) `echo "The time is $(date)"`
   - b) `current_time <- date`
   - c) `echo "The time is $current_time"`, ignoring any assignment

3. Which command will show all environment variables?
   - a) `ls env`
   - b) `env`
   - c) `varlist`

4. Which file is typically used to set user-specific environment variables permanently?
   - a) `/etc/profile`
   - b) `/usr/local/envvars`
   - c) `~/.bashrc` or `~/.zshrc`

### **SRE-Level (3–4)**

1. How can you make a script stop on the first error?
   - a) `set -e`
   - b) `stop on error`
   - c) `exit 1`

2. Which structure handles numeric thresholds (like CPU usage <80%, <95%) gracefully?
   - a) `if-elif-else`
   - b) `case $(cpu_usage)`
   - c) `until loop`

3. What’s a recommended way to ensure a variable must be set or the script fails?
   - a) `if [ -z "$VAR" ]; then exit 1 fi`
   - b) `"${VAR:?Need to set VAR}"`
   - c) `declare secure VAR`

4. How do SREs typically manage secret environment variables?
   - a) Hardcode them in the script
   - b) Use a secrets manager or restricted files
   - c) Store in a public Git repo for easy reference

---

## 🚧 **Troubleshooting**

Below are three scenarios illustrating common shell scripting pitfalls.

1. **Scenario**: Script terminates unexpectedly after a failing command.
   - **Cause**: `set -e` is active, so the script exits on any non-zero return code.
   - **Resolution**: Check the exit status of commands with `$?`; handle known failures or wrap them with `|| true` if they’re non-critical.
   - **Prevention**: Only use `set -e` if you want a strict fail-fast approach. Document which commands may return non-zero codes.

2. **Scenario**: Script variables aren’t recognized in a child script.
   - **Cause**: Variables aren’t exported, or you used a different shell that doesn’t load the same environment.
   - **Resolution**: `export VAR` or pass them as arguments. Make sure all child scripts run with the same interpreter.
   - **Prevention**: Keep environment setting consistent, and test sub-scripts in the same shell.

3. **Scenario**: Infinite loop hogs CPU.
   - **Cause**: A `while true` loop with no exit condition or a loop condition that never becomes false.
   - **Resolution**: Add a break condition, limit iterations, or use a `sleep`.
   - **Prevention**: Thoroughly design loops for resource checks, especially if continuous monitoring is needed.

---

## ❓ **FAQ**

### **Beginner FAQ (3)**

1. **Q**: Why does my script show `Permission denied`?
   **A**: You need to make it executable: `chmod +x script.sh`. Also confirm your shebang line (`#!/bin/bash`).

2. **Q**: How do I store numeric data and do math in a script?
   **A**: Use shell arithmetic with `(( ))` or `$(( ))`. Example: `sum=$((num1 + num2))`.

3. **Q**: Can I prompt the user for input?
   **A**: Yes. Use `read variable`. For silent input (e.g., passwords), use `read -s variable`.

### **Intermediate FAQ (3)**

1. **Q**: How do I pass command-line arguments to my script?
   **A**: They appear as `$1`, `$2`, etc. For example, `./script.sh arg1 arg2`, then `echo $1` outputs `arg1`.

2. **Q**: Why are filenames with spaces causing loop errors?
   **A**: You must quote variables. For example, `for file in "*.log"; do echo "$file"; done`.

3. **Q**: How do I debug my script?
   **A**: Use `set -x` to see each command before execution, or run `bash -x script.sh`. Add `echo` statements for clarity.

### **SRE-Level FAQ (3)**

1. **Q**: How do I handle large scripts for maintainability?
   **A**: Break them into functions or multiple files. Use consistent naming, add comments, and possibly keep libraries of shared functions.

2. **Q**: How do I handle secrets and credentials?
   **A**: Store them securely (e.g., Vault, AWS Secrets Manager). If using local files, restrict permissions (chmod 600). Never commit secrets to version control.

3. **Q**: How can I incorporate logging and monitoring?
   **A**: Write logs to a file or use `logger` to send data to syslog. Integrate with your monitoring platform (Prometheus, ELK) for long-term analysis.

---

## 🔥 **SRE Scenario: Comprehensive Database Backup**

Shell scripts are invaluable for robust backups. Below is a production-ready snippet demonstrating advanced SRE practices—logging, error handling, verification, and rotation.

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

set -eo pipefail  # Fail on command error or pipeline failure

CONFIG_FILE=${1:-"/etc/db_backup.conf"}
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_DIR="/var/log/db_backup"
LOG_FILE="$LOG_DIR/backup_${TIMESTAMP}.log"
BACKUP_DIR="/var/backup/databases"
METRICS_FILE="/var/log/db_backup/metrics.log"
RETAIN_DAYS=14
ALERT_EMAIL="sre-team@example.com"
SLACK_WEBHOOK="https://hooks.slack.com/services/XXXX/YYYY/ZZZZ"

mkdir -p "$LOG_DIR" "$BACKUP_DIR"

if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
fi

log() {
    local level=$1
    local message=$2
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$timestamp] [$level] $message" | tee -a "$LOG_FILE"
}

handle_error() {
    local error_message="Backup failed at line $1"
    log "ERROR" "$error_message"
    send_alert "❌ Database Backup FAILED" "$error_message"
    exit 1
}
trap 'handle_error $LINENO' ERR

send_alert() {
    local title=$1
    local message=$2
    # Email alert
    echo -e "Subject: $title\n\n$message\n\nTimestamp: $(date)\nHost: $(hostname)\nLog: $LOG_FILE" | sendmail "$ALERT_EMAIL"
    # Slack alert
    if [ -n "$SLACK_WEBHOOK" ]; then
        curl -s -X POST -H 'Content-type: application/json' \
            --data "{\"text\":\"*$title*\n$message\n\nTimestamp: $(date)\nHost: $(hostname)\"}" \
            "$SLACK_WEBHOOK"
    fi
    log "INFO" "Alert sent: $title"
}

record_metric() {
    local name=$1
    local value=$2
    echo "$(date +%s) $name $value" >> "$METRICS_FILE"
}

check_database() {
    log "INFO" "Checking database connection"
    local start_time=$(date +%s)
    if ! mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASSWORD" -e "SELECT 1" &> /dev/null; then
        log "ERROR" "Failed to connect to database"
        exit 1
    fi
    local end_time=$(date +%s)
    record_metric "db_connection_time_seconds" $((end_time - start_time))
    log "INFO" "Database connection successful"
}

create_backup() {
    log "INFO" "Starting database backup"
    local start_time=$(date +%s)
    local backup_file="$BACKUP_DIR/$DB_NAME-$TIMESTAMP.sql.gz"

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

verify_backup() {
    local backup_file=$1
    log "INFO" "Verifying backup integrity: $backup_file"

    gzip -t "$backup_file"
    local table_count=$(zcat "$backup_file" | grep -c "CREATE TABLE" || true)

    if [ "$table_count" -lt 1 ]; then
        log "ERROR" "Backup verification failed: No tables found"
        exit 1
    fi

    sha256sum "$backup_file" > "${backup_file}.sha256"
    log "INFO" "Backup verification successful"
}

rotate_backups() {
    log "INFO" "Rotating backups older than $RETAIN_DAYS days"
    local deleted_count=$(find "$BACKUP_DIR" -name "$DB_NAME-*.sql.gz" -type f -mtime +$RETAIN_DAYS | wc -l)
    find "$BACKUP_DIR" -name "$DB_NAME-*.sql.gz" -type f -mtime +$RETAIN_DAYS -delete
    find "$BACKUP_DIR" -name "$DB_NAME-*.sql.gz.sha256" -type f -mtime +$RETAIN_DAYS -delete
    record_metric "deleted_backups" "$deleted_count"
    local remaining_count=$(find "$BACKUP_DIR" -name "$DB_NAME-*.sql.gz" -type f | wc -l)
    local total_size=$(du -sh "$BACKUP_DIR" | cut -f1)
    log "INFO" "Deleted $deleted_count old backups. Remaining: $remaining_count backups ($total_size)"
}

main() {
    log "INFO" "Starting database backup process for $DB_NAME"
    local script_start=$(date +%s)

    if [ -f "/etc/db_backup/credentials" ]; then
        source "/etc/db_backup/credentials"
    fi

    if [ -z "$DB_HOST" ] || [ -z "$DB_USER" ] || [ -z "$DB_PASSWORD" ] || [ -z "$DB_NAME" ]; then
        log "ERROR" "Missing required DB configuration"
        exit 1
    fi

    check_database
    backup_file=$(create_backup)
    verify_backup "$backup_file"
    rotate_backups

    local script_end=$(date +%s)
    local total_duration=$((script_end - script_start))
    record_metric "total_script_duration_seconds" "$total_duration"

    log "INFO" "Backup process completed in $total_duration seconds"
    send_alert "✅ Database Backup Successful" \
        "Backup completed in $total_duration seconds.\nBackup: $backup_file\nSize: $(du -h "$backup_file" | cut -f1)"
}

main
```

**Key SRE Practices**:

- **Logging** with timestamps and levels
- **Error Handling** using `trap` and `set -eo pipefail`
- **Verification**: Ensuring backups contain actual data
- **Rotation**: Automatic deletion of old files
- **Alerting**: Slack and email notifications
- **Metrics**: Collecting performance data

---

## 🧠 **Key Takeaways**

1. **Command Summary (5)**:
   - **Variables**: Store critical values for flexibility.
   - **Command Substitution**: Dynamically gather system data.
   - **Loops**: Repeat tasks across multiple targets.
   - **Conditionals**: Adapt behavior to system conditions.
   - **Environment Variables**: Maintain consistent config across dev/staging/prod.

2. **Operational Insights (3)**:
   1. **Fail Fast**: Use strict error handling (`set -e`) for reliability.
   2. **Auditability**: Log every major action for post-incident reviews.
   3. **Security**: Validate inputs, protect secrets, and limit privileged operations.

3. **Best Practices (3)**:
   1. **Modularize**: Break large scripts into smaller functions or files.
   2. **Validate**: Check environment variables, arguments, and resource states.
   3. **Document & Version**: Keep scripts in source control and include usage examples.

4. **Next Topic Preview**: We’ll expand these skills into **Configuration Management and Infrastructure as Code** to manage fleets of servers systematically.

---

## 📚 **Further Learning Resources**

### 🟢 **Beginner (2–3)**

1. **"Learn Shell Scripting Step by Step"** – [https://www.howtoforge.com/tutorial/bash-scripting-tutorial/](https://www.howtoforge.com/tutorial/bash-scripting-tutorial/)
   - Ideal for reinforcing basics of variables, conditionals, and loops.
2. **"The Linux Command Line"** – [https://linuxcommand.org/tlcl.php](https://linuxcommand.org/tlcl.php)
   - Starts with command-line fundamentals and grows into scripting.
3. **"ShellCheck Online"** – [https://www.shellcheck.net/](https://www.shellcheck.net/)
   - Catch common beginner mistakes in your scripts.

### 🟡 **Intermediate (2–3)**

1. **"Advanced Bash-Scripting Guide"** – [https://tldp.org/LDP/abs/html/](https://tldp.org/LDP/abs/html/)
   - Explores complex constructs (arrays, functions, traps).
2. **"Google Shell Style Guide"** – [https://google.github.io/styleguide/shellguide.html](https://google.github.io/styleguide/shellguide.html)
   - Presents best practices for maintainable scripts.

### 🔴 **SRE-Level (2–3)**

1. **"Google SRE Book – Automation Chapter"** – [https://sre.google/sre-book/](https://sre.google/sre-book/)
   - Real-world guidance on large-scale automation strategies.
2. **"Linux System Administrator’s Guide"** – [https://www.kernel.org/doc/Documentation/admin-guide/](https://www.kernel.org/doc/Documentation/admin-guide/)
   - Covers advanced system topics relevant to SRE.
3. **"Effective DevOps"** – [https://www.oreilly.com/library/view/effective-devops/9781491926291/](https://www.oreilly.com/library/view/effective-devops/9781491926291/)
   - Addresses collaboration and automation best practices at scale.

---

## 🎉 **Congratulations**

You’ve completed **Day 10**: Shell Scripting Basics & Advanced Concepts. By combining the fundamentals of variables, loops, conditionals, and environment management with best-practice SRE patterns, you’re equipped to create scripts that reduce toil and enhance reliability. Continue refining these skills, and soon you’ll integrate them into even larger automation ecosystems.
