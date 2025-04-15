# 🚀 Day 10: Shell Scripting Basics & Advanced Concepts

## 📌 Introduction

Welcome to **Day 10** of our Linux SRE Training Path! Today’s focus is on **Shell Scripting**. We’ll combine foundational learning with real SRE scenarios to develop robust scripts. By the end of this module, you’ll be able to automate repetitive tasks, incorporate best practices, and troubleshoot advanced scripting issues.

### How This Module Elevates Your SRE Skills

1. **Automation Mindset**: SREs thrive on reducing toil. Shell scripting is the gateway to automating frequent tasks.
2. **Reliability**: Structured scripts produce consistent results, reducing manual errors and improving uptime.
3. **Scalability**: Mastery of shell scripting is crucial for orchestrating tasks across fleets of servers.

### Objectives

#### Beginner-Level Objectives

1. Understand the basic structure of a shell script (including the shebang line).
2. Use variables and simple loops to automate small tasks.
3. Practice conditionals to control script flow.

#### Intermediate-Level Objectives

1. Incorporate command substitution and environment variables for dynamic scripting.
2. Utilize complex loops (e.g., nested loops) and branching logic for multi-step operations.
3. Implement script debugging techniques and logging for clearer insights.

#### SRE-Level Objectives

1. Develop production-ready scripts with robust error handling and security considerations.
2. Optimize scripts for performance and maintainability in large-scale environments.
3. Integrate advanced scripting into SRE workflows for monitoring, incident response, and automated deployment.

### Connection to Previous and Future Learning

- **Previously**: You learned about file management, system monitoring, and process control. All these commands become powerful building blocks within your scripts.
- **Next Steps**: Future modules will delve into configuration management, CI/CD pipelines, and container orchestration, where scripted automation is essential.

---

## 📚 Core Concepts

Below are the key shell scripting concepts that every SRE should master:

1. **Variables**: Holding and manipulating data within scripts.
2. **Command Substitution**: Embedding command outputs inside other commands.
3. **Loops**: Iterating over lists of items, executing tasks repeatedly (e.g., `for`, `while`).
4. **Conditionals**: Using `if`, `else`, `case` to make decisions based on conditions.
5. **Environment Variables**: Setting global context that influences system and script behavior.

These concepts allow you to create dynamic, responsive scripts that can perform sophisticated operations. Mastering each concept is fundamental for achieving reliable automation.

---

## 💻 Command Breakdown (Concept-by-Concept)

Each concept is presented in the same structured format. Examples progress through three tiers: **Beginner**, **Intermediate**, and **SRE-Level**.

---

### 1. Variables (Storing and Referencing Data)

**Command: variables (Basic Data Storage)**

**Command Overview:**  
Variables in shell scripts store data values used by commands and functions. They facilitate automation by letting you reference the same piece of information in multiple places. SREs use variables to parameterize scripts for different servers, environments, or resource paths.

**Syntax & Flags:**  

| Flag/Option | Syntax Example                   | Description                                             | SRE Usage Context                                    |
|-------------|----------------------------------|---------------------------------------------------------|-------------------------------------------------------|
| `=`         | `myvar="some_value"`           | Assigns a value to a variable (no spaces around `=`)    | Setting default parameters for backup or deploy tasks |
| `$variable` | `echo "$variable"`             | Expands the variable value                              | Referencing environment-specific details             |
| `export`    | `export VAR="production"`       | Makes a variable available to child processes           | Setting environment context for sub-scripts          |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
#!/bin/bash
name="Alice"
echo "Hello, $name!"
# Output:
# Hello, Alice!
```

*Explanation*: You assign a string to `name` and then echo it.

- 🧩 **Intermediate Example:**

```bash
#!/bin/bash
servername="web-prod"
backup_dir="/var/backups"

# Use variable interpolation in a command
tar -czf "${backup_dir}/${servername}_logs.tar.gz" /var/log/$servername

echo "Backup completed for $servername!"
# Example Output:
# Backup completed for web-prod!
```

*Explicit context*: In an operations environment, storing `servername` and `backup_dir` as variables is more flexible than hardcoding paths.

- 💡 **SRE-Level Example:**

```bash
#!/bin/bash
# Parameterizing environment with an env variable
: "${APP_ENV:?Need to set APP_ENV}"  # This fails if APP_ENV is not set

log_file="/var/log/${APP_ENV}_app.log"
if [ -f "$log_file" ]; then
  echo "Processing log file: $log_file"
else
  echo "No log file for environment $APP_ENV"
fi
# Example Output:
# Processing log file: /var/log/staging_app.log
```

*Explicit context*: This script enforces that `APP_ENV` must be set, preventing accidental usage in the wrong environment.

**Instructional Notes:**

- 🧠 **Beginner Tip:** Use double quotes around variable references (`"$var"`) to handle spaces correctly.
- 🧠 **Beginner Tip:** No spaces around the `=` sign: `myvar=value` is valid, `myvar = value` is not.

- 🔧 **SRE Insight:** Name variables consistently. E.g., `DB_USER`, `DB_PASSWORD`, `DB_HOST`. This improves readability and reduces errors.
- 🔧 **SRE Insight:** Use parameter expansion (e.g., `"${var:-default_value}"`) to handle unset or empty variables gracefully.

- ⚠️ **Common Pitfall:** Declaring variables with spaces around `=` or forgetting quotes can cause unexpected word splitting.
- ⚠️ **Common Pitfall:** Not exporting variables when child processes need them.

- 🚨 **Security Note:** Never store secrets in plaintext variables if possible. Use secure storage or environment injection from a secrets manager.
- 💡 **Performance Impact:** Variables themselves are lightweight. However, extremely large strings or arrays in memory can slow down a script.

---

### 2. Command Substitution (Embedding Command Output)

**Command: command substitution (Dynamic Scripting)**

**Command Overview:**  
Command substitution allows the output of one command to be inserted into another command. This is accomplished via `$(...)` or backticks (`` `...` ``). In SRE contexts, you might embed the result of a resource query, date command, or system statistic.

**Syntax & Flags:**  

| Flag/Option      | Syntax Example        | Description                                              | SRE Usage Context                               |
|------------------|-----------------------|----------------------------------------------------------|------------------------------------------------|
| `$(command)`     | `var=$(date +%Y%m%d)` | Captures command output in a variable                    | Automating file naming with timestamps          |
| Backtick syntax  | `` var=`date` ``      | Older syntax, can cause issues with nested commands      | Typically replaced by modern `$(...)` usage     |
| Escaped backticks| `` `command \`args\`` `` | Rare scenario for nested backticks                       | Not recommended in new scripts                 |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
#!/bin/bash
today=$(date)
echo "The date is $today"
# Output (example):
# The date is Wed Mar 20 12:34:56 UTC 2025
```

*Explanation*: You capture the current date/time and store it in a variable.

- 🧩 **Intermediate Example:**

```bash
#!/bin/bash
file_count=$(ls -1 /var/log/*.log | wc -l)
echo "There are $file_count log files in /var/log."
# Example Output:
# There are 15 log files in /var/log.
```

*Explicit context*: Counting log files helps SREs track log rotation or usage.

- 💡 **SRE-Level Example:**

```bash
#!/bin/bash
# Checking CPU usage in real time
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

*Explicit context*: We embed multiple commands to parse CPU usage and respond if usage passes a threshold.

**Instructional Notes:**

- 🧠 **Beginner Tip:** Prefer `$(...)` over backticks for clarity and easier nesting.
- 🧠 **Beginner Tip:** Quoting the result of command substitution can avoid whitespace issues.

- 🔧 **SRE Insight:** Combine command substitution with parameter expansion to handle edge cases or default values.
- 🔧 **SRE Insight:** Store large or complex outputs in temporary files instead if performance or readability is impacted.

- ⚠️ **Common Pitfall:** Using command substitution inside a loop for thousands of iterations can degrade performance.
- ⚠️ **Common Pitfall:** Not verifying that the substituted command ran successfully before using the value.

- 🚨 **Security Note:** If you’re capturing user input (e.g., from a form) to embed in a command, sanitize it to avoid command injection.
- 💡 **Performance Impact:** Running many sub-commands can slow scripts. For large data tasks, consider direct piping or more efficient parsing.

---

### 3. Loops (For, While)

**Command: loops (Iteration Constructs)**

**Command Overview:**  
Loops let you process multiple items, lines, or numbers repeatedly. SREs use loops for tasks like checking multiple servers, rotating log files, or running batch updates.

**Syntax & Flags:**  

| Flag/Option  | Syntax Example                  | Description                                                       | SRE Usage Context                       |
|-------------|---------------------------------|-------------------------------------------------------------------|-----------------------------------------|
| `for`       | `for i in {1..5}; do ... done`  | Iterates over a list or range                                     | Checking multiple hosts or services     |
| `while`     | `while [ condition ]; do ... done` | Continues loop until condition is false                         | Monitoring a process until it’s stable  |
| `break`     | `break`                          | Exits the loop immediately                                        | Early termination on error condition    |
| `continue`  | `continue`                       | Skips current iteration and continues                             | Skipping invalid entries in batch tasks |

**Tiered Examples:**

- 🔍 **Beginner Example:**

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

*Explanation*: A simple numeric loop.

- 🧩 **Intermediate Example:**

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

*Explicit context*: Checking the status of multiple servers in a single script.

- 💡 **SRE-Level Example:**

```bash
#!/bin/bash
while true; do
  active_sessions=$(ss -t | grep ESTAB | wc -l)
  echo "Active TCP sessions: $active_sessions"

  if [ "$active_sessions" -gt 100 ]; then
    echo "High load: $active_sessions sessions"
    # Potentially trigger alert or scale-up logic
  fi

  # Sleep 30s then recheck
  sleep 30
done
# Example Output (recurring):
# Active TCP sessions: 40
# Active TCP sessions: 45
# Active TCP sessions: 101
# High load: 101 sessions
```

*Explicit context*: A `while` loop continuously monitors network sessions, typical for SRE production oversight.

**Instructional Notes:**

- 🧠 **Beginner Tip:** Always ensure your loop terminates or has a break condition to avoid infinite loops.
- 🧠 **Beginner Tip:** Use arrays to store multiple items and iterate with `for`.

- 🔧 **SRE Insight:** Combine loops with parallelization tools (e.g., `xargs -P`) for faster multi-server tasks.
- 🔧 **SRE Insight:** Use `break` or `continue` strategically for error handling or to skip irrelevant cases.

- ⚠️ **Common Pitfall:** Infinite loops can hang a system or script. Always plan an exit condition.
- ⚠️ **Common Pitfall:** Using the wrong test or missing quotes can cause unexpected breakage in loops.

- 🚨 **Security Note:** Use caution when looping over user-provided lists, especially if the script executes commands on each item.
- 💡 **Performance Impact:** Large loops can be CPU-intensive. For huge data sets, use more efficient data processing tools or offload to specialized pipelines.

---

### 4. Conditionals (If, Case)

**Command: conditionals (Decision Making)**

**Command Overview:**  
Conditionals allow a script to react differently based on the system state or user input. SREs rely on conditionals to handle errors, check resource usage, or manage different operational paths.

**Syntax & Flags:**

| Flag/Option  | Syntax Example                              | Description                                                  | SRE Usage Context                    |
|-------------|---------------------------------------------|--------------------------------------------------------------|--------------------------------------|
| `if`        | `if [ "$var" = "something" ]; then ... fi` | Basic branching condition                                    | Checking environment or input        |
| `elif`      | `elif [ condition ]; then ... fi`           | Additional condition to evaluate if previous `if` fails      | Multi-level checks                   |
| `else`      | `else ... fi`                                | Fallback if none of the conditions are true                  | Default or error-handling path       |
| `case`      | `case $var in pattern) ... ;; esac`          | Multi-branch structure based on pattern matching            | Evaluating multiple distinct values  |

**Tiered Examples:**

- 🔍 **Beginner Example:**

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

*Explanation*: A simple if-else that checks numeric input.

- 🧩 **Intermediate Example:**

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

*Explicit context*: Handling different HTTP status codes in a web application environment.

- 💡 **SRE-Level Example:**

```bash
#!/bin/bash
mem_free=$(free -m | awk 'NR==2{print $4}')

if [ "$mem_free" -lt 512 ]; then
  echo "CRITICAL: Available memory below 512 MB!"
  # Potentially trigger an alert or auto-scale event
elif [ "$mem_free" -lt 1024 ]; then
  echo "WARNING: Available memory below 1 GB"
else
  echo "Memory levels are stable."
fi
# Example Output:
# CRITICAL: Available memory below 512 MB!
```

*Explicit context*: Conditionals handle different thresholds for memory usage in production.

**Instructional Notes:**

- 🧠 **Beginner Tip:** Use bracket-based tests like `[ -f file ]`, `[ $var -gt 5 ]`, etc.
- 🧠 **Beginner Tip:** Always close each `if` with `fi`, and each `case` pattern with `;;`.

- 🔧 **SRE Insight:** Chain multiple checks for robust gating logic in production scripts. For example, only proceed if CPU usage is below 80% AND memory is above 1GB.
- 🔧 **SRE Insight:** `case` statements are ideal for dissecting multiple distinct states (e.g., HTTP codes, environment names).

- ⚠️ **Common Pitfall:** Using `==` vs. `=` incorrectly or mixing up `-eq` with `=` can break your logic.
- ⚠️ **Common Pitfall:** Strings containing special characters (like `[` or `]`) can cause syntax errors if not quoted.

- 🚨 **Security Note:** Always validate external inputs before making system changes or running commands in condition blocks.
- 💡 **Performance Impact:** Minimal overhead for typical usage. Complex nested conditionals can reduce readability—prefer clarity for large scripts.

---

### 5. Environment Variables (Global Context)

**Command: environment variables (Global Configuration)**

**Command Overview:**  
Environment variables define system-wide or session-wide data that child processes inherit. SREs rely on them to store environment-specific configuration (e.g., `PATH`, `LANG`, `APP_ENV`), ensuring flexible deployment across multiple environments.

**Syntax & Flags:**

| Flag/Option      | Syntax Example                 | Description                                             | SRE Usage Context                                  |
|------------------|--------------------------------|---------------------------------------------------------|-----------------------------------------------------|
| `export`         | `export MYVAR="some_value"`    | Makes a variable available to child processes           | Setting environment for sub-scripts                |
| `env`            | `env`                           | Lists all environment variables                         | Debugging environment issues                       |
| `printenv`       | `printenv MYVAR`                | Prints a specific environment variable                 | Checking values within scripts                     |
| `.bashrc/.zshrc` | `vi ~/.bashrc`                  | Shell startup files that can define environment values  | Persistent environment configuration for each user |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```bash
#!/bin/bash
export MYAPP_PORT=8080

echo "MYAPP_PORT is set to $MYAPP_PORT"
# Output:
# MYAPP_PORT is set to 8080
```

*Explanation*: You export a variable so child processes can also see it.

- 🧩 **Intermediate Example:**

```bash
#!/bin/bash
# Checking if a required environment variable is set
if [ -z "$DB_HOST" ]; then
  echo "Please set DB_HOST before running this script."
  exit 1
fi

echo "Connecting to database at $DB_HOST..."
# Potential connection command would go here
```

*Explicit context*: Ensures the environment is correctly configured before proceeding.

- 💡 **SRE-Level Example:**

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

*Explicit context*: Large-scale SRE deployments often maintain environment files to standardize configuration.

**Instructional Notes:**

- 🧠 **Beginner Tip:** Use `export VARNAME=value` to make a variable globally visible.
- 🧠 **Beginner Tip:** Place persistent exports in `~/.bashrc` or `~/.zshrc`, then reload with `source ~/.bashrc`.

- 🔧 **SRE Insight:** Keep environment variables consistent across staging and production but with environment-specific values.
- 🔧 **SRE Insight:** Secure environment variables that contain secrets or credentials, ensuring only authorized users can read them.

- ⚠️ **Common Pitfall:** Overriding critical system variables like `PATH` without including original values can break commands.
- ⚠️ **Common Pitfall:** Using too many environment variables can make scripts brittle and reliant on external context.

- 🚨 **Security Note:** If storing secrets in environment variables, restrict permission on the scripts or files that set them.
- 💡 **Performance Impact:** Setting environment variables is lightweight. Just avoid monstrous PATH or large data.

---

## 🛠️ System Effects

Shell scripting can influence your system in several ways:

1. **Filesystem and Metadata**: Scripts often create, modify, or remove files and directories. Permissions and ownership changes in scripts can affect system stability.
2. **System Resources**: Intensive loops or command substitutions can spike CPU usage. Large I/O operations (e.g., compressing logs) can saturate disk resources.
3. **Security Implications**: Running scripts with elevated privileges or passing unvalidated user input can lead to vulnerabilities (e.g., code injection, accidental file deletion).
4. **Monitoring & Observability**: Scripts that rotate logs or parse system metrics can make events more traceable, but also risk losing data if not carefully implemented (e.g., failing to archive logs properly).

---

## 🎯 Hands-On Exercises

Below are exactly 3 exercises for each skill tier (Beginner, Intermediate, SRE-Level). Work through them in order to build confidence.

### Beginner Exercises (3)

1. **Hello Script**: Create a script `hello.sh` that asks for your name, then prints a welcome message. Make it executable and run it.
2. **Simple Math**: Write a script `math.sh` that reads two numbers from the user, adds them, and displays the sum.
3. **File Checker**: Build a script `file_check.sh` that checks if a file named `data.txt` exists. If it does, print “File found!”; otherwise, print “No file.”

### Intermediate Exercises (3)

1. **Server Status Loop**: Create `check_servers.sh` that iterates through an array of server names, pings each one, and records the reachability in a log file.
2. **Backup Automation**: Write `auto_backup.sh` that uses command substitution to create a timestamped backup of `/etc` into `/tmp/backups`. Test it with different directories.
3. **Conditional Cleanup**: Develop `cleanup_logs.sh` that checks the size of each log file in `/var/log`. If any file is above 10MB, compress it. Otherwise, leave it as is.

### SRE-Level Exercises (3)

1. **Resource Threshold Monitor**: Implement `monitor_resources.sh` that checks CPU, memory, and disk usage every 60 seconds. Trigger an alert (display a message or send email) if thresholds are exceeded.
2. **Environment-Based Deploy**: Build `deploy_app.sh` that uses an environment variable `APP_ENV` (dev/staging/prod) to decide which configuration file to deploy. Include error handling if `APP_ENV` is not set.
3. **Multi-Server Loop**: Write `distributed_cmd.sh` that reads a list of remote servers from a file and runs a specified command on each server via SSH, saving results individually. Include checks for SSH connectivity and command exit codes.

---

## 📝 Quiz Questions

Test your comprehension. Solutions are for instructors only.

### Beginner Level (3)

1. Which command substitution syntax is recommended?
   1. `` `command` ``
   2. `$(command)`
   3. `${command}`
2. What operator do you use to check if a file exists in an `if` statement?
   1. `[ -f filename ]`
   2. `[ -file filename ]`
   3. `[ filename -exist ]`
3. How do you export a variable so child processes see it?
   1. `export MYVAR=value`
   2. `make MYVAR global`
   3. `global MYVAR=value`

### Intermediate Level (3)

1. If you have a list `servers=("server1" "server2" "server3")`, how do you iterate through it?
   1. `for s in ${servers}; do ... done`
   2. `for s in "${servers[@]}"; do ... done`
   3. `foreach s in servers; do ... done`
2. Which command would embed the current date/time in your script output?
   1. `date >> output.txt`
   2. `echo "The time is $(date)"`
   3. `current_time <- date`
3. In a `case` statement, which keyword ends each pattern?
   1. `;;`
   2. `esac`
   3. `fi`

### SRE-Level (3)

1. How can you handle a script error so it stops execution immediately?
   1. `set -e`
   2. `stop on error`
   3. `exit error`
2. What is the best approach to ensure a variable must be set or the script fails?
   1. `"${VAR:?Error: VAR not set}"`
   2. `if [ -z "$VAR" ]; then exit 1 fi`
   3. `declare require VAR`
3. Which structure best handles multiple numeric thresholds for CPU usage (e.g., <50%, <80%, <95%)?
   1. `if-elif-else`
   2. `nested while`
   3. `case $(cpu_usage)`

---

## 🚧 Troubleshooting

Below are three realistic scenarios you may encounter while writing shell scripts.

1. **Scenario**: *Script terminates unexpectedly after running a command.*  
   - **Cause**: The script might have `set -e` enabled and the last command returned a non-zero exit code.
   - **Resolution**: Check the command’s exit status with `echo $?` or wrap the command in a conditional. If the command can fail safely, consider using `|| true` or adding error handling logic.
   - **Prevention**: Document which commands can return non-zero codes and handle them gracefully.

2. **Scenario**: *Variables are empty or not recognized in a sub-script.*  
   - **Cause**: Variables were not exported, or you used `sh subscript.sh` which invoked a different shell that doesn’t load your environment.
   - **Resolution**: Use `export MYVAR=value` or pass variables as arguments. Ensure you call the script with the same shell that defines those variables.
   - **Prevention**: Standardize on one shell and environment file, using `source /path/to/envfile`.

3. **Scenario**: *Infinite loop consumes 100% CPU.*  
   - **Cause**: The loop condition never becomes false, or a `while true` block lacks a break condition.
   - **Resolution**: Add an exit condition or a `break`. Alternatively, schedule a time-based stop.
   - **Prevention**: Thoroughly plan loops, especially `while true` scenarios, to ensure they have exit conditions.

---

## ❓ FAQ

Below are exactly 9 frequently asked questions (3 per tier).

### Beginner FAQ (3)

1. **Q**: Why does my script say `Permission denied` when I try to run it?
   **A**: You must make it executable with `chmod +x script.sh`. Also ensure the shebang (`#!/bin/bash`) is correct.
2. **Q**: Can I store numbers in variables and do math?
   **A**: Yes. Use shell arithmetic like `num=$((5 + 2))`. Always avoid spaces inside `$(( ))`.
3. **Q**: How do I see what variables are set?
   **A**: Run `env` or `printenv` to see environment variables. For local script variables, just `echo "$var"`.

### Intermediate FAQ (3)

1. **Q**: How can I pass arguments to my script?
   **A**: Your script can access them via `$1`, `$2`, etc. E.g., `./myscript.sh arg1 arg2`, then inside the script, `echo $1` prints `arg1`.
2. **Q**: Why do my loops fail when dealing with filenames that have spaces?
   **A**: You need to quote variables (`"$file"`). Otherwise, whitespace breaks the loop items.
3. **Q**: Is `case` only for strings?
   **A**: Typically yes, but you can convert numeric expressions to strings or use pattern ranges. For advanced numeric logic, use `if-elif`.

### SRE-Level FAQ (3)

1. **Q**: How do I structure large scripts to remain maintainable?
   **A**: Use functions for logical grouping, adopt consistent naming, and possibly maintain a separate library file. Keep each script focused on a specific domain.
2. **Q**: How do I handle secrets in environment variables?
   **A**: Prefer external secrets managers. If you must store them locally, restrict file permissions. Avoid committing secrets to version control.
3. **Q**: How do I debug complex scripts in production?
   **A**: Use `set -x` for command tracing, maintain robust logging, and consider ephemeral test environments to replicate issues.

---

## 🔥 SRE Scenario

**Scenario**: You’ve noticed intermittent CPU spikes and random application restarts. You suspect memory leaks or excessive disk usage. You need an on-demand script to investigate.

**Task**: A single script performs these 5–7 steps, each step explained:

1. **Collect system metrics**: The script runs `top -bn1` and `df -h` to gather CPU, memory, and disk usage.  
   *Reasoning*: Quick view of resource consumption.
2. **Analyze logs**: The script looks in `/var/log/app/` for error patterns via `grep -i "error"`.  
   *Reasoning*: Verify if restarts correlate with application errors.
3. **Check running processes**: Use `ps aux --sort=-%mem` to see if any process uses excessive memory.  
   *Reasoning*: Identifies memory leak suspects.
4. **Verify environment configs**: Source `env.prod` if available, ensuring the correct environment is loaded.  
   *Reasoning*: Make sure the environment settings haven’t drifted from what’s expected.
5. **Conditional alerts**: If memory usage is above 90% or disk usage above 85%, the script prints a critical warning or sends an email.
6. **Optional triggers**: If usage is too high, automatically restart certain services.  
   *Reasoning*: Quick fix in a near-outage scenario.
7. **Exit with code**: If thresholds are exceeded, exit with a non-zero code.  
   *Reasoning*: Helps orchestrators or CI/CD pipelines catch health check failures.

By bundling these steps, you combine conditionals, loops, environment variables, and command substitution in a realistic SRE scenario.

---

## 🧠 Key Takeaways

1. **Command Summary (5)**:
   - **Variables**: Store data, parametrize scripts.
   - **Command Substitution**: Dynamically embed other command outputs.
   - **Loops**: Automate repetitive tasks across servers or items.
   - **Conditionals**: Direct your script based on system or user conditions.
   - **Environment Variables**: Provide global context and consistent configurations.

2. **Operational Insights (3)**:
   1. **Fail Fast**: Use `set -e` or conditional checks to avoid running with partial failures.
   2. **Version Control**: Keep your scripts in Git for traceability and collaboration.
   3. **Security Posture**: Restrict sensitive data exposure by sanitizing inputs and protecting environment files.

3. **Best Practices (3)**:
   1. Write modular code: separate logic into functions or multiple files.
   2. Validate user input and environment assumptions (e.g., `$VAR` or existence of `file`).
   3. Document usage, arguments, and dependencies at the top of each script.

4. **Next Topic Preview**: We will transition into **Configuration Management and Infrastructure as Code**. This will build on your scripting knowledge, showing how to manage entire fleets with Ansible, Puppet, or Chef.

---

## 📚 Further Learning Resources

### 🔍 Beginner (2–3)

1. **"Learn Shell Scripting Step by Step"** – [https://www.howtoforge.com/tutorial/bash-scripting-tutorial/](https://www.howtoforge.com/tutorial/bash-scripting-tutorial/).  
   *Teaches basic bash syntax, loops, and conditionals.*
2. **"The Linux Command Line"** – [https://linuxcommand.org/tlcl.php](https://linuxcommand.org/tlcl.php).  
   *Introduces shell essentials and gradually moves into scripting.*
3. **"ShellCheck Online Tool"** – [https://www.shellcheck.net/](https://www.shellcheck.net/).  
   *Lint your scripts to identify common beginner mistakes.*

### 🧩 Intermediate (2–3)

1. **"Advanced Bash-Scripting Guide"** – [https://tldp.org/LDP/abs/html/](https://tldp.org/LDP/abs/html/).  
   *Covers deeper scripting constructs, arrays, functions, and more.*
2. **"Google Shell Style Guide"** – [https://google.github.io/styleguide/shellguide.html](https://google.github.io/styleguide/shellguide.html).  
   *Provides best practices and patterns for maintainable scripts.*

### 💡 SRE-Level (2–3)

1. **"Linux System Administrator’s Guide"** – [https://www.kernel.org/doc/Documentation/admin-guide/](https://www.kernel.org/doc/Documentation/admin-guide/).  
   *Includes advanced topics that SREs frequently encounter.*
2. **"Google SRE Book – Automation Chapter"** – [https://sre.google/sre-book/](https://sre.google/sre-book/).  
   *Insights into how Google automates tasks at scale.*

---

## Final Note

With this module, you’ve acquired the practical scripting skills needed to reduce manual toil, enforce consistency, and elevate reliability in Linux environments. Keep experimenting, refining, and documenting your shell scripts. The path to advanced SRE mastery continues as we move toward configuration management and large-scale orchestration.

**Congratulations** on completing Day 10 – Shell Scripting Basics & Advanced Concepts! You are now better equipped to tackle real-world reliability engineering challenges with well-structured, secure, and scalable scripts.
