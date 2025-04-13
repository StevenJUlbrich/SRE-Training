
# 📝 **Quiz Questions**

## **Beginner Level (3–4)**

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
