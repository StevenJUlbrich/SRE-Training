# Day 10 Shell Scripting module

These answers reflect standard Linux and Bash best practices, as well as SRE considerations.

---

## Beginner Level

### 1. Which syntax is preferred for command substitution?

- **Question**:  
  a) `` `command` ``  
  b) `$(command)`  
  c) `${command}`  

- **Correct Answer**: **b) `$(command)`**  
- **Explanation**: The `$(command)` form is modern and allows for easier nesting. The older `` `command` `` syntax can become hard to read and maintain when you need multiple substitutions. `${command}` is not valid for command substitution in Bash (it is used for parameter expansion, not running a command).

---

### 2. Which operator checks if a file named `myfile` exists?

- **Question**:  
  a) `[ -x myfile ]`  
  b) `[ -f myfile ]`  
  c) `[ file myfile ]`  

- **Correct Answer**: **b) `[ -f myfile ]`**  
- **Explanation**: `-f` checks whether a file exists and is a regular file. Option `-x` tests if a file is executable, and `[ file myfile ]` is not valid Bash test syntax.

---

### 3. How do you export a variable named `DB_HOST`?

- **Question**:  
  a) `DB_HOST = 1.2.3.4`  
  b) `set DB_HOST=1.2.3.4`  
  c) `export DB_HOST=1.2.3.4`  

- **Correct Answer**: **c) `export DB_HOST=1.2.3.4`**  
- **Explanation**: In Bash, `export` is needed to make the variable available to child processes. Also note that the `=` must not have spaces around it. The `set` command has different functionality, and `DB_HOST = 1.2.3.4` (with spaces) is invalid.

---

### 4. Which line is needed at the start of a bash script?

- **Question**:  
  a) `#!/bin/sh`  
  b) `#!/bin/bash`  
  c) `bash script`  

- **Correct Answer**: **b) `#!/bin/bash`**  
- **Explanation**: The shebang (`#!`) indicates which interpreter to use. If you want Bash specifically, `#!/bin/bash` is standard. Using `#!/bin/sh` often implies a more generic POSIX shell that might not support all Bash features. Simply writing `bash script` is not a shebang line—it's just a command to run a script named `script`.

---

## Intermediate Level

### 1. Given `servers=("srv1" "srv2" "srv3")`, how do you loop through them?

- **Question**:  
  a) `for s in ${servers}; do`  
  b) `for s in "${servers[@]}"; do`  
  c) `foreach s in servers; do`  

- **Correct Answer**: **b) `for s in "${servers[@]}"; do`**  
- **Explanation**: In Bash, `"${servers[@]}"` correctly expands all elements of the array even if they contain spaces. Option (a) omits quotes and can break on spaces, while (c) is not valid syntax in standard Bash (more like a csh/tcsh style).

---

### 2. How do you embed the current date/time in your script output?

- **Question**:  
  a) `echo "The time is $(date)"`  
  b) `current_time <- date`  
  c) `echo "The time is $current_time"`, ignoring any assignment  

- **Correct Answer**: **a) `echo "The time is $(date)"`**  
- **Explanation**: `$(date)` is the correct command substitution in Bash. Option (b) is not valid Bash syntax, and (c) would require that `$current_time` is already set, which the question doesn’t describe.

---

### 3. Which command will show all environment variables?

- **Question**:  
  a) `ls env`  
  b) `env`  
  c) `varlist`  

- **Correct Answer**: **b) `env`**  
- **Explanation**: The `env` command lists all the environment variables in your current shell session. `ls env` attempts to list files in a directory named `env`, which isn’t what you want. `varlist` is not a standard Linux command.

---

### 4. Which file is typically used to set user-specific environment variables permanently?

- **Question**:  
  a) `/etc/profile`  
  b) `/usr/local/envvars`  
  c) `~/.bashrc` or `~/.zshrc`  

- **Correct Answer**: **c) `~/.bashrc` or `~/.zshrc`**  
- **Explanation**: These are the per-user shell startup files. `/etc/profile` is a global login shell script, while `/usr/local/envvars` is not a default convention on most systems.

---

## SRE-Level

### 1. How can you make a script stop on the first error?

- **Question**:  
  a) `set -e`  
  b) `stop on error`  
  c) `exit 1`  

- **Correct Answer**: **a) `set -e`**  
- **Explanation**: In Bash, `set -e` forces the script to exit if any command returns a non-zero status (error). `stop on error` is not a valid Bash command, and simply having `exit 1` in the script does not automatically exit on *any* command failure—it just manually exits where placed.

---

### 2. Which structure handles numeric thresholds (like CPU usage <80%, <95%) gracefully?

- **Question**:  
  a) `if-elif-else`  
  b) `case $(cpu_usage)`  
  c) `until loop`  

- **Correct Answer**: **a) `if-elif-else`**  
- **Explanation**: When you have multiple numeric thresholds, using an `if-elif-else` chain (e.g., `< 50`, `< 80`, `< 95`) is typically clearer. A `case` statement can handle distinct pattern matching (often used for strings), while an `until` loop is for repeating tasks until a condition is met—less suitable for direct numeric threshold checking logic.

---

### 3. What’s a recommended way to ensure a variable must be set or the script fails?

- **Question**:  
  a) `if [ -z "$VAR" ]; then exit 1 fi`  
  b) `"${VAR:?Need to set VAR}"`  
  c) `declare secure VAR`  

- **Correct Answer**: **b) `"${VAR:?Need to set VAR}"`**  
- **Explanation**: The `${VAR:?message}` expansion in Bash will cause the script to exit with an error and print `message` if `VAR` is unset or empty. Option (a) does work in principle but is more verbose; (b) is the concise idiomatic shell way. Option (c) is not valid for forcibly requiring a variable’s existence in standard Bash.

---

### 4. How do SREs typically manage secret environment variables?

- **Question**:  
  a) Hardcode them in the script  
  b) Use a secrets manager or restricted files  
  c) Store in a public Git repo for easy reference  

- **Correct Answer**: **b) Use a secrets manager or restricted files**  
- **Explanation**: Hardcoding secrets in the script is insecure. Storing them in a public repository is a major security risk. The safest approach is to leverage a dedicated secrets manager (e.g., HashiCorp Vault, AWS Secrets Manager) or use an encrypted file with minimal permissions that the script reads on runtime.

---

**Note**: While multiple approaches or partial solutions sometimes work, these answers reflect common Bash conventions and best practices for reliability and security—especially in SRE contexts.
