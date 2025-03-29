# Day 10: Shell Scripting - Quiz Answer Key with Explanations

## Beginner Level Questions

### **1. What line should begin every shell script to specify the interpreter?**

**Correct Answer: b) `#!/bin/bash`**

**Explanation:**
The first line of a shell script should start with `#!` (called the "shebang" or "hashbang") followed by the path to the interpreter that should execute the script. For bash scripts, this is typically `/bin/bash`. This line tells the system which program should be used to interpret the commands in the script. Without this line, the script would run in the default shell, which might not be bash, potentially causing unexpected behavior.

Options a) and c) have incorrect syntax, and option d) is not a valid shebang line format.

### **2. How do you correctly declare a variable named `username` with the value `admin`?**

**Correct Answer: b) `username="admin"`**

**Explanation:**
In bash, variables are assigned using the format `variable=value`. There should be no spaces around the equals sign. Option a) uses incorrect syntax with double equals signs (`==`), which is used for comparison, not assignment. Option c) incorrectly places the `$` symbol before the variable name during assignment; the `$` is only used when referencing a variable's value, not when assigning it. Option d) includes spaces around the equals sign, which bash interprets as a command followed by arguments rather than a variable assignment.

### **3. Which command makes a script executable?**

**Correct Answer: b) `chmod +x script.sh`**

**Explanation:**
The `chmod` command changes file permissions. The `+x` option specifically adds execute permission to the file, which allows it to be run as a script. Option a) `chmod 777 script.sh` would also work technically, but it grants read, write, and execute permissions to everyone (owner, group, and others), which is a security risk and not recommended. Options c) and d) use invalid syntax or non-existent options.

### **4. How would you start a loop that iterates over all `.txt` files in the current directory?**

**Correct Answer: a) `for file in *.txt; do`**

**Explanation:**
The correct syntax for a `for` loop in bash that iterates over files is `for variable in pattern; do`. In this case, `file` is the variable that will hold each filename during iteration, and `*.txt` is a pattern that matches all files with the `.txt` extension in the current directory. Option b) would only match a literal file named `.txt`. Option c) uses invalid syntax. Option d) uses `foreach`, which is not a valid bash loop construct (though it exists in some other shells like csh).

### **5. What is the correct way to check if a file named "data.txt" exists?**

**Correct Answer: a) `if [ -f "data.txt" ]; then`**

**Explanation:**
In bash, file tests are performed using the test command, which can be written as `[ ]`. The `-f` test operator specifically checks if a file exists and is a regular file (not a directory or device file). Options b) and c) use incorrect syntax. Option d) attempts to use `grep`, which is a text-searching tool, not a file existence checking tool.

## Intermediate Level Questions

### **1. What does `$?` represent in a shell script?**

**Correct Answer: b) The exit status of the last command**

**Explanation:**
In bash, `$?` is a special variable that contains the exit status (return code) of the most recently executed command. Exit status values range from 0 to 255, with 0 typically indicating success and any non-zero value indicating some form of error or failure. This variable is extremely useful for error checking and conditional execution based on command success or failure. Option a) refers to `$$`, which contains the process ID of the current shell. Option c) would be `$#`, which holds the number of command-line arguments. Option d) is not represented by any standard bash variable.

### **2. How do you capture the output of a command and store it in a variable?**

**Correct Answer: c) `result=$(command)`**

**Explanation:**
This syntax is called command substitution. The `$(command)` format executes the command and returns its output, which is then assigned to the variable `result`. Option a) includes spaces around the equals sign, which is invalid for variable assignment in bash. Option b) would attempt to assign the string "command" to the variable, not the command's output. Option d) uses backticks (`` ` ``) which is an older form of command substitution that still works but has limitations when nesting commands, and is generally less preferred than the `$()` syntax.

### **3. Which line will make a script exit immediately if any command fails?**

**Correct Answer: b) `set -e`**

**Explanation:**
The bash option `set -e` (or `set -o errexit`) causes the script to exit immediately if any command returns a non-zero exit status (indicating failure). This is useful for ensuring that scripts don't continue execution after encountering errors. Option a) `set -a` (or `set -o allexport`) automatically marks variables for export to the environment, which doesn't affect error handling. Option c) `set -x` (or `set -o xtrace`) enables debug output, showing each command before execution. Option d) `exit 1` would simply exit the script immediately with status code 1, not based on command failure.

### **4. What does the `local` keyword do in a shell function?**

**Correct Answer: b) Restricts a variable's scope to the function**

**Explanation:**
The `local` keyword declares a variable that is only accessible within the scope of the function where it's defined. When the function exits, the variable is no longer available. This helps prevent naming conflicts with variables in the main script or other functions. Option a) is incorrect; the `local` keyword actually does the opposite, restricting rather than making the variable globally available. Option c) is incorrect; `local` doesn't force the function to run in a subshell. Option d) is incorrect; local variables can still access environment variables.

### **5. Which command would read user input into a variable named "password" without displaying what is typed?**

**Correct Answer: b) `read -s password`**

**Explanation:**
The `read` command captures user input into a variable. The `-s` (silent) option suppresses the display of the characters as they are typed, which is essential when entering passwords or other sensitive information. Option a) would display the characters as they are typed. Option c) uses `-p`, which is for displaying a prompt, not hiding input. Option d) uses an invalid command.

## SRE Application Questions

### **1. An SRE needs to create a deployment script that backs up existing files before replacement. Which approach is most appropriate?**

**Correct Answer: b) Create a timestamp-named backup before deploying new files**

**Explanation:**
Creating timestamped backups before making changes is a best practice in SRE and system administration. This approach provides a clear record of what was in place before the change, allows for easy identification of when the backup was made, and enables straightforward rollback if needed. Option a) would lose the existing files, making recovery impossible. Option c) ignores backups entirely, creating significant risk. Option d) is incomplete, as it would miss files that haven't been modified but might still be important for the system's functionality.

### **2. You need to monitor a critical service and restart it if it fails. Which command combination is most appropriate?**

**Correct Answer: b) `systemctl is-active service && echo "Running" || systemctl restart service`**

**Explanation:**
This command uses logical operators to create a conditional execution chain. It first checks if the service is active with `systemctl is-active service`. If that succeeds (returns exit code 0), it executes the command after `&&` (echo "Running"). If it fails (the service is not active), it executes the command after `||` (restart the service). This is an elegant, efficient way to implement basic service monitoring and automatic recovery. Option a) only checks if the process exists but doesn't take any action. Option c) incorrectly forces a kill and restart without first checking the service state. Option d) uses incorrect syntax that wouldn't work.

### **3. When implementing error handling in an SRE automation script, which practice is most important?**

**Correct Answer: b) Log detailed error information and exit with appropriate codes**

**Explanation:**
Proper error handling is crucial for automation scripts, especially in SRE contexts. Logging detailed error information helps with troubleshooting, while appropriate exit codes enable other systems to understand what went wrong and react accordingly. This practice supports both human debugging and automated error handling. Option a) would hide problems, potentially leading to cascading failures. Option c) might create loops of failures without addressing root causes. Option d) would discard valuable error information needed for troubleshooting.

### **4. You're writing a script to analyze application logs across multiple servers. What's the most efficient approach?**

**Correct Answer: b) Use SSH to run log analysis on each server and aggregate results**

**Explanation:**
Running analysis directly on each server and then aggregating the results is generally the most efficient approach for distributed log analysis. It minimizes data transfer (only sending results rather than raw logs), utilizes the processing power of each server, and can be executed in parallel for faster results. Option a) is manual and not scalable. Option c) would create unnecessary data transfer and potential storage issues. Option d) delegates responsibility inappropriately and doesn't provide centralized monitoring or consistency.

### **5. An SRE needs to deploy a configuration change to 100 servers. Which scripting approach is safest?**

**Correct Answer: b) Deploy to one server, verify, then use a loop with error handling for the rest**

**Explanation:**
This approach follows the "canary deployment" pattern, which is a best practice in SRE. By first deploying to a single server and verifying functionality, you can catch potential issues before affecting the entire infrastructure. The subsequent automated deployment with proper error handling balances efficiency with safety. Option a) is risky as it could cause widespread issues simultaneously. Option c) is impractical for large-scale environments and prone to human error. Option d) delegates responsibility inappropriately and lacks standardization.