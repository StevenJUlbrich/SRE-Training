# Day 10 Answers

---

## Beginner Level (3 Questions)

### 1. Which command substitution syntax is recommended?

1. `` `command` ``
2. `$(command)`
3. `${command}`

**Correct Answer:** 2. `$(command)`

**Explanation:**  

- The older style uses backticks (`` `command` ``), but `$(command)` is now preferred for clarity and nesting.  
- `${command}` is not valid for command substitution in shell scripting.  
- `$(command)` also makes it easier to insert one command substitution inside another without confusion.

---

### 2. What operator do you use to check if a file exists in an `if` statement?

1. `[ -f filename ]`
2. `[ -file filename ]`
3. `[ filename -exist ]`

**Correct Answer:** 1. `[ -f filename ]`

**Explanation:**  

- `-f` checks if the specified path is a regular file.  
- `[ -file filename ]` and `[ filename -exist ]` are not valid test operators in Bash or POSIX shell.  
- Other common operators include `-d` (directory), `-e` (exists), `-s` (non-empty), etc., but for a regular file, `-f` is correct.

---

### 3. How do you export a variable so child processes see it?

1. `export MYVAR=value`
2. `make MYVAR global`
3. `global MYVAR=value`

**Correct Answer:** 1. `export MYVAR=value`

**Explanation:**  

- In shell scripting, `export` is the command that marks a variable for inheritance by child processes.  
- There is no built-in command called `make` or `global` for environment variables.  
- Once exported, running subscripts or commands can reference `MYVAR`.

---

## Intermediate Level (3 Questions)

### 1. If you have a list `servers=("server1" "server2" "server3")`, how do you iterate through it?

1. `for s in ${servers}; do ... done`
2. `for s in "${servers[@]}"; do ... done`
3. `foreach s in servers; do ... done`

**Correct Answer:** 2. `for s in "${servers[@]}"; do ... done`

**Explanation:**  

- In Bash, `${servers[@]}` expands to each element of the array.  
- Writing `for s in ${servers}` without quotes or `[@]` will not properly handle elements with spaces and could lead to unexpected splitting.  
- `foreach` is a construct in some other shells or languages (like csh or tcsh), not in standard Bash.

---

### 2. Which command would embed the current date/time in your script output?

1. `date >> output.txt`
2. `echo "The time is $(date)"`
3. `current_time <- date`

**Correct Answer:** 2. `echo "The time is $(date)"`

**Explanation:**  

- Command substitution `$(date)` captures the output of `date` and embeds it in the string.  
- `date >> output.txt` would redirect the date output to a file rather than incorporating it into a script message.  
- `current_time <- date` is not valid Bash syntax.

---

### 3. In a `case` statement, which keyword ends each pattern?

1. `;;`
2. `esac`
3. `fi`

**Correct Answer:** 1. `;;`

**Explanation:**  

- Within a `case` statement, each pattern block concludes with `;;`.  
- `esac` ends the entire `case` statement, similar to `fi` in an `if` block.  
- `fi` is used to close an `if` statement, not a `case` pattern.

---

## SRE-Level (3 Questions)

### 1. How can you handle a script error so it stops execution immediately?

1. `set -e`
2. `stop on error`
3. `exit error`

**Correct Answer:** 1. `set -e`

**Explanation:**  

- `set -e` tells Bash to exit on any command returning a non-zero status (indicating an error).  
- There is no built-in Bash command `stop on error`.  
- Simply calling `exit error` is not a universal approach; `exit` would terminate the script at that exact line, but it doesn’t automatically handle errors from all commands.

---

### 2. What is the best approach to ensure a variable must be set or the script fails?

1. `"${VAR:?Error: VAR not set}"`
2. `if [ -z "$VAR" ]; then exit 1 fi`
3. `declare require VAR`

**Correct Answer:** 1. `"${VAR:?Error: VAR not set}"`

**Explanation:**  

- In Bash, `"${VAR:?message}"` triggers an error and exits if `VAR` is not set or is empty. This is a shorthand for forcibly requiring the variable.  
- Checking `-z` in an `if` block is also valid but more verbose; it doesn’t fail automatically unless you explicitly add an `exit 1`.  
- `declare require VAR` is not valid syntax.

---

### 3. Which structure best handles multiple numeric thresholds for CPU usage (e.g., <50%, <80%, <95%)?

1. `if-elif-else`
2. `nested while`
3. `case $(cpu_usage)`

**Correct Answer:** 1. `if-elif-else`

**Explanation:**  

- For numeric comparisons with multiple ranges, `if-elif-else` is typically easier to read, as you can do something like:\n  ```bash\n  if [ $cpu_usage -gt 95 ]; then\n    # Critically high\n  elif [ $cpu_usage -gt 80 ]; then\n    # High\n  elif [ $cpu_usage -gt 50 ]; then\n    # Moderate\n  else\n    # Low\n  fi\n```\n- `case` is commonly used for string or pattern matching, although you can wrap numeric tests into a `case` with advanced patterns—but it’s less straightforward for numeric ranges.  
- `nested while` loops aren’t typically the best pattern for simple threshold checks—they’re more for repetitive actions.

---

### Summary

By reviewing these questions and explanations, learners and instructors can confirm a correct grasp of shell scripting fundamentals (variables, conditionals, loops, etc.) as well as the more advanced or SRE-focused practices (error handling, environment usage, numeric thresholds).

Use these answers to check your progress, clarify concepts, or facilitate group discussion.
