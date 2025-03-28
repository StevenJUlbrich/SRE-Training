# 📝 **Day 4: Text Processing & Searching Quiz - Answer Key with Explanations**

## Beginner Level Questions

### Question 1: Which symbol is used to pipe the output of one command to another?
- a) `>`
- b) `>>`
- c) `|`
- d) `<`

**Answer: c) `|`**

**Explanation:** The pipe symbol (`|`) is specifically designed to connect commands by sending the output of one command as input to another. This allows for powerful command chaining where data flows from left to right through a series of processing steps.

The other options are incorrect because:
- `>` redirects output to a file (overwriting it)
- `>>` redirects output to a file (appending to it)
- `<` redirects input from a file to a command

### Question 2: Which command would you use to search for the word "error" in a file?
- a) `find "error" file.txt`
- b) `grep "error" file.txt`
- c) `locate "error" file.txt`
- d) `search "error" file.txt`

**Answer: b) `grep "error" file.txt`**

**Explanation:** The `grep` command is specifically designed to search for patterns within file content. It stands for "Global Regular Expression Print" and is used to find lines that match a specified pattern.

The other options are incorrect because:
- `find` is used to search for files and directories, not content within files
- `locate` is used to quickly find filenames in a database, not search within file content
- `search` is not a standard Linux command

### Question 3: To save the output of a command to a file (overwriting any existing content), which operator would you use?
- a) `>`
- b) `>>`
- c) `|`
- d) `<`

**Answer: a) `>`**

**Explanation:** The `>` operator redirects the standard output of a command to a file, overwriting any existing content in that file. It's commonly used when you want to create a new file or replace an existing file with fresh content.

The other options are incorrect because:
- `>>` appends output to a file without overwriting existing content
- `|` pipes output from one command to another command
- `<` redirects input from a file to a command

## Intermediate Level Questions

### Question 4: To perform a case-insensitive search with grep, which option do you use?
- a) `-c`
- b) `-n`
- c) `-i`
- d) `-v`

**Answer: c) `-i`**

**Explanation:** The `-i` option (or `--ignore-case`) makes `grep` perform a case-insensitive search, meaning it will match both upper and lowercase instances of the pattern. For example, searching for "error" with `-i` will find "error", "Error", "ERROR", etc.

The other options are incorrect because:
- `-c` counts the number of matching lines instead of displaying them
- `-n` shows line numbers with matching lines
- `-v` inverts the match, showing only non-matching lines

### Question 5: If you want to find all files modified in the last 24 hours, which find option would you use?
- a) `-time 24`
- b) `-modified 1`
- c) `-mtime -1`
- d) `-newer 1day`

**Answer: c) `-mtime -1`**

**Explanation:** The `-mtime -1` option to `find` searches for files that were modified less than 1 day ago. The minus sign before the number is critical here:
- `-mtime -1` means "less than 1 day ago" (i.e., within the last 24 hours)
- `-mtime 1` would mean "exactly 1 day ago"
- `-mtime +1` would mean "more than 1 day ago"

The other options are incorrect because:
- `-time 24` is not a valid `find` option
- `-modified 1` is not a valid `find` option
- `-newer 1day` is not a valid `find` option (though `-newer` can be used with a reference file)

### Question 6: What will the command `ls | grep "^d"` show?
- a) All files that start with the letter "d"
- b) All directories
- c) All hidden files
- d) All files larger than "d" bytes

**Answer: b) All directories**

**Explanation:** The command combines `ls` with `grep "^d"` to filter the output. In the long listing format produced by `ls -l` (which is implied here), directories start with the letter 'd' in the first column of the permission string. The regular expression `^d` matches lines that start with the letter 'd'.

The other options are incorrect because:
- If looking for filenames starting with 'd', you would need `ls | grep "^d"` only if using `ls -l`, otherwise you'd need `ls | grep "^d.*$"`
- Hidden files start with a dot (.) not 'd'
- File sizes are not part of the basic output format that would match this pattern

## SRE Application Level Questions

### Question 7: During an incident, you need to find all occurrences of "connection timeout" in logs, including the lines before and after each occurrence. Which command would you use?
- a) `grep "connection timeout" /var/log/application.log`
- b) `grep -A 2 -B 2 "connection timeout" /var/log/application.log`
- c) `find /var/log -name "connection timeout"`
- d) `grep -v "connection timeout" /var/log/application.log`

**Answer: b) `grep -A 2 -B 2 "connection timeout" /var/log/application.log`**

**Explanation:** The command uses `grep` with context options:
- `-A 2` shows 2 lines After each match
- `-B 2` shows 2 lines Before each match

This provides critical context around each occurrence of the error, which is essential during incident investigation to understand what led to the timeout and what happened afterward.

The other options are incorrect because:
- Option a) only shows the lines containing the pattern, without any context
- Option c) incorrectly uses `find` to search for files, not content within files
- Option d) uses `-v` which inverts the search, showing only lines that do NOT contain the pattern

### Question 8: To extract the number of 5xx errors from a web server log and save the count to a file, which pipeline would you use?
- a) `grep "HTTP/1.1\" 5[0-9][0-9]" access.log | wc -l > 5xx_count.txt`
- b) `grep -c "5[0-9][0-9]" access.log > 5xx_count.txt`
- c) `find access.log -name "5[0-9][0-9]" | wc -l > 5xx_count.txt`
- d) `tail access.log | grep "5[0-9][0-9]" > 5xx_count.txt`

**Answer: a) `grep "HTTP/1.1\" 5[0-9][0-9]" access.log | wc -l > 5xx_count.txt`**

**Explanation:** This pipeline correctly:
1. Uses `grep` with a regular expression to find HTTP status codes in the 500-599 range
2. Pipes the matches to `wc -l` to count them
3. Redirects the count to a file named 5xx_count.txt

The other options are incorrect because:
- Option b) uses `-c` which counts matches, but the pattern "5[0-9][0-9]" might match other numbers in the log that aren't status codes
- Option c) incorrectly uses `find` to search for files, not content
- Option d) only examines the end of the log file with `tail` and doesn't count the matches

### Question 9: You suspect a security issue and need to find all files with world-writable permissions anywhere on the system. Which command is most appropriate?
- a) `ls -la / | grep "w"`
- b) `find / -type f -perm -o=w`
- c) `grep -r "777" /etc/passwd`
- d) `chmod -R o-w / --list`

**Answer: b) `find / -type f -perm -o=w`**

**Explanation:** This command uses `find` to search the entire filesystem for:
- `-type f` - regular files (not directories)
- `-perm -o=w` - files that have write permission for "others" (the world)

This pattern will find files that could pose a security risk because they can be modified by any user on the system.

The other options are incorrect because:
- Option a) only lists files in the root directory, not recursively, and `grep "w"` would match any 'w' in the output, not just permissions
- Option c) incorrectly searches for text in the /etc/passwd file, which has nothing to do with finding world-writable files
- Option d) is not a valid command; `chmod` doesn't have a `--list` option
