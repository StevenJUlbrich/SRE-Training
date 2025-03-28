# ✅ **Day 10 Quiz – Answer Key with Detailed Explanations**

## Below are the answers and detailed explanations for the shell scripting quiz questions

---

### **Question 1:**  

**What line should begin a bash script file to specify which interpreter to use?**

✅ **Correct Answer:**  
**b)** `#!/bin/bash`

**Explanation:**  

This is known as the "shebang" line and tells the system which interpreter should be used to execute the script. The `#!` (shebang) characters must be the first two characters in the file, followed immediately by the path to the interpreter.

The path `/bin/bash` specifically invokes the Bash shell, which is the most common shell in Linux and provides many advanced features needed for complex scripting.

The other options are incorrect because:

- Option a) `#!/bin/sh` would use the basic POSIX shell, which lacks many Bash features
- Option c) `#/bin/bash` is missing the exclamation mark, making it a regular comment
- Option d) `bash:` isn't a valid shebang and would be treated as text

For SREs, using the correct shebang is crucial because it ensures your script runs with the expected shell and behavior, especially when scripts run from cron jobs or other automated processes where the default shell might not be Bash.

---

### **Question 2:**  

**How would you access the third command line argument in a shell script?**

✅ **Correct Answer:**  
**d)** `$3`

**Explanation:**  

In shell scripts, command line arguments are accessed using positional parameters:

- `$0` refers to the script name itself
- `$1` is the first argument
- `$2` is the second argument
- `$3` is the third argument
- And so on...

For example, if you run:

```bash
./backup.sh database1 daily 7
```

Then inside the script:

- `$0` would be `./backup.sh`
- `$1` would be `database1`
- `$2` would be `daily`
- `$3` would be `7`

Additionally, `$#` provides the number of arguments, and `$@` or `$*` represents all arguments.

Understanding argument handling is essential for creating flexible, reusable scripts that can be configured at runtime. It's especially important for SREs who develop automation tools that need to work with different targets or configurations.

---

### **Question 3:**  

**Which statement correctly checks if a file exists and is writable?**

✅ **Correct Answer:**  
**c)** `if [ -e $file ] && [ -w $file ]; then`

**Explanation:**  

This statement correctly combines two separate test conditions with the logical AND operator `&&`:

1. `[ -e $file ]` checks if the file exists
2. `[ -w $file ]` checks if the file is writable

The other options are incorrect because:

- Option a) `if [ -e $file && -w $file ]; then` - The `&&` operator cannot be used inside a single set of brackets in this context
- Option b) `if [ -e $file -a -w $file ]; then` - While the `-a` operator would work inside a single test, it's considered deprecated and less readable
- Option d) `if test -e $file -w $file; then` - This doesn't properly combine the tests

For better script robustness, you should also quote the variable:

```bash
if [ -e "$file" ] && [ -w "$file" ]; then
```

This prevents issues if the variable contains spaces or special characters. File testing is a common operation in SRE scripts, especially when validating inputs, checking log files, or verifying that configuration files can be modified.

---

### **Question 4:**  

**What is the correct syntax for a for loop that processes each item in an array?**

✅ **Correct Answer:**  
**a)** `for item in "${array[@]}"; do`

**Explanation:**  

This syntax correctly iterates through all elements of a Bash array:

- `${array[@]}` expands to all elements of the array, preserving each element as a separate entity
- The double quotes `"${array[@]}"` ensure that elements with spaces are handled correctly
- `item` becomes the variable that holds each array element during iteration

The other options are incorrect because:

- Option b) `for item in $array; do` - This treats $array as a single string, not an array
- Option c) `for (item in array); do` - This uses C-style syntax, not Bash syntax
- Option d) `foreach item in $array; do` - This uses syntax similar to languages like Python, not Bash

A complete example:

```bash
# Define an array
servers=("web-server" "db-server" "cache-server" "app-server")

# Iterate through the array with proper syntax
for server in "${servers[@]}"; do
    echo "Checking $server..."
    ping -c 1 "$server" &> /dev/null || echo "$server is unreachable!"
done
```

Arrays are essential in SRE scripts for managing groups of servers, services, or configuration files that need similar treatment. Using the correct syntax ensures reliable processing of all array elements.

---

### **Question 5:**  

**Which command captures the output of a command and assigns it to a variable?**

✅ **Correct Answer:**  
**b)** `variable=$(command)`

**Explanation:**  

This syntax is called command substitution and is the modern, preferred way to capture command output in a variable. The command inside the `$()` parentheses is executed, and its output (stdout) is assigned to the variable.

The other options are incorrect because:

- Option a) `variable = $(command)` - Spaces around the equals sign are not allowed in variable assignment in Bash
- Option c) `variable=`command`` - While backticks work similar to `$()`, they're considered legacy syntax and harder to nest
- Option d) `variable="command"` - This assigns the literal string "command" to the variable, not the output of running it

Example of proper command substitution:

```bash
# Get current date in YYYY-MM-DD format
today=$(date +%Y-%m-%d)
echo "Today is $today"

# Get uptime in seconds
uptime_seconds=$(cat /proc/uptime | awk '{print $1}' | cut -d. -f1)
echo "System has been up for $uptime_seconds seconds"
```

Command substitution is one of the most powerful features for SREs writing shell scripts. It allows you to dynamically generate values, process command output, and make decisions based on system state - essential for monitoring, validation, and automation tasks.

---

### **Question 6:**  

**What's the purpose of using the `set -e` command at the beginning of a bash script?**

✅ **Correct Answer:**  
**The script will exit immediately if any command returns a non-zero status (error).**

**Explanation:**  

`set -e` is a crucial option for script reliability. By default, bash scripts continue executing even if individual commands fail. With `set -e`, the script stops as soon as any command fails (returns a non-zero exit code).

This behavior is especially valuable for SRE scripts because:

1. It prevents partial execution of critical operations
2. It avoids cascading failures where one error leads to more serious problems
3. It makes error detection immediate rather than discovering problems later

For example, in a deployment script:

```bash
#!/bin/bash
set -e  # Stop if any command fails

# Without set -e, these would continue even after failures
cd /app/release
git pull  # If this fails, we don't want to continue!
npm install
npm run build
systemctl restart app-service
```

Often, you'll combine it with other safety options:

```bash
set -e  # Exit on error
set -u  # Exit if undefined variable is used
set -o pipefail  # Exit if any command in a pipeline fails
```

For highly critical scripts, this approach ensures you fail fast and explicitly rather than continuing in an unpredictable state.

---

### **Question 7:**  

**What's the difference between single quotes (') and double quotes (") in shell scripting?**

✅ **Correct Answer:**  
**Double quotes allow variable expansion and command substitution, while single quotes preserve everything literally.**

**Explanation:**  

This distinction is fundamental in shell scripting:

**Double quotes (`"..."`):**

- Allow variable expansion: `"Hello, $name"` becomes `Hello, John`
- Allow command substitution: `"Today is $(date)"` becomes `Today is Mon Feb 10 14:30:22 PST 2025`
- Allow certain backslash escape sequences: `"Line 1\nLine 2"` (newline)
- Preserve spaces and most special characters

**Single quotes (`'...'`):**

- Treat everything inside literally
- No variable expansion: `'Hello, $name'` remains `Hello, $name`
- No command substitution: `'Today is $(date)'` remains `Today is $(date)`
- No escape sequences: `'Line 1\nLine 2'` remains `Line 1\nLine 2`

This difference is crucial in SRE work. For example:

```bash
# Security implications:
password="secret123"

# Unsecure - password expanded:
ssh user@server "echo $password > /tmp/pwd.txt"  # ⚠️ Password visible in 'ps' output

# Secure - password not expanded:
ssh user@server 'echo $password > /tmp/pwd.txt'  # 💡 $password references a variable on the remote server

# For configuration templating:
template='server { listen $PORT; }'
PORT=8080
echo "$template" | sed "s/\$PORT/$PORT/"  # Expands to: server { listen 8080; }
```

Understanding quote behavior helps prevent security issues, data corruption, and unexpected behavior in scripts.

---

### **Question 8:**  

**When writing a shell function, what command is used to provide a return value?**

✅ **Correct Answer:**  
**`return <value>`**

**Explanation:**  

In shell scripting, the `return` command specifies the exit status of a function. However, it's important to understand that:

1. The return value must be an integer between 0-255
2. 0 typically indicates success, while non-zero values indicate different error conditions
3. The return value is not the same as function output (which is sent to stdout)

Example of proper function return values:

```bash
# Function that checks if a service is running
check_service() {
    local service_name="$1"
    
    systemctl is-active --quiet "$service_name"
    return $?  # Returns the exit status of the systemctl command
}

# Using the function
if check_service "nginx"; then
    echo "Nginx is running"
else
    echo "Nginx is not running, exit code: $?"
fi
```

To return actual data from a function, you would use echo/printf and command substitution:

```bash
get_server_uptime() {
    uptime | awk '{print $3}'
}

# Capture the output
server_uptime=$(get_server_uptime)
echo "Server has been up for $server_uptime"
```

Understanding the distinction between return codes (for status) and function output (for data) is essential for writing robust scripts that can be used in pipelines and conditional logic.

---

### **Question 9:**  

**What's the best way to check if a required command is available before using it in a shell script?**

✅ **Correct Answer:**  
**Use the `command -v` utility to check if the command exists in the PATH.**

**Explanation:**  

Checking for required dependencies is a best practice in shell scripting, especially for SRE automation that might run on different systems. The `command -v` approach is the most reliable method:

```bash
# Check for a required command
if ! command -v aws &> /dev/null; then
    echo "Error: AWS CLI is not installed or not in the PATH"
    echo "Please install it with: pip install awscli"
    exit 1
fi

# Now safely use the command
aws s3 ls
```

This approach is better than alternatives because:

1. It works across all POSIX-compliant shells (not just Bash)
2. It checks not just if the command exists but if it's executable
3. It handles aliases and built-in commands correctly
4. It follows the PATH, just like the shell does when executing commands

Other common methods have drawbacks:

- `which aws` - Not available on all systems and returns non-standard exit codes
- `type aws` - Output format varies across shells
- `hash aws` - Only checks commands that have been run already in the current shell

For SRE scripts that often depend on system utilities, cloud CLIs, or custom tools, this validation approach prevents cryptic errors and provides helpful installation instructions when dependencies are missing.
