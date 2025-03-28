# 📝 **Day 5: Advanced Text Processing Quiz - Answer Key with Explanations**

## Beginner Level Questions

### Question 1: How would you replace all instances of "linux" with "Linux" in a file called `notes.txt`?
- a) `sed 's/Linux/linux/g' notes.txt`
- b) `sed 's/linux/Linux/g' notes.txt` 
- c) `sed -i 's/linux/Linux/' notes.txt`
- d) `awk '{gsub("linux", "Linux"); print}' notes.txt`

**Answer: b) `sed 's/linux/Linux/g' notes.txt`**

**Explanation:** This command uses `sed` (stream editor) with the substitution command `s/` to replace every occurrence of "linux" with "Linux" in the file notes.txt. The `g` flag at the end ensures that all occurrences on each line are replaced, not just the first one.

The other options are incorrect because:
- Option a) would replace "Linux" with "linux" (the opposite of what we want)
- Option c) would only replace the first occurrence of "linux" on each line because it's missing the global (`g`) flag
- Option d) would work but is using `awk`, which is more complex than needed for this simple substitution

### Question 2: Which command counts the number of lines in a file?
- a) `wc -w file.txt`
- b) `wc -l file.txt`
- c) `wc -c file.txt`
- d) `wc -m file.txt`

**Answer: b) `wc -l file.txt`**

**Explanation:** The `wc` (word count) command with the `-l` option counts the number of lines in a file. This is one of the most commonly used options for `wc` in system administration and log analysis.

The other options are incorrect because:
- `wc -w` counts words, not lines
- `wc -c` counts bytes (characters in ASCII files)
- `wc -m` counts characters, accounting for multi-byte characters in Unicode files

### Question 3: How do you sort a file called `numbers.txt` in numerical order?
- a) `sort numbers.txt`
- b) `sort -n numbers.txt`
- c) `sort -r numbers.txt`
- d) `sort -h numbers.txt`

**Answer: b) `sort -n numbers.txt`**

**Explanation:** The `sort` command with the `-n` option performs numerical sorting. Without this option, `sort` performs alphabetical sorting by default, which would produce incorrect results for numbers (e.g., "10" would come before "2").

The other options are incorrect because:
- Option a) would perform alphabetical sorting
- Option c) would perform reverse alphabetical sorting
- Option d) would perform human-readable number sorting (e.g., recognizing units like "K", "M", "G")

## Intermediate Level Questions

### Question 4: To print only the second and third fields from a space-delimited file, which command would you use?
- a) `awk '{print $2, $3}' data.txt`
- b) `awk '{print 2,3}' data.txt`
- c) `sed -n '2,3p' data.txt`
- d) `cut -f 2,3 data.txt`

**Answer: a) `awk '{print $2, $3}' data.txt`**

**Explanation:** The `awk` command processes files by fields (columns). By default, it splits each line using whitespace as the delimiter. The variables `$1`, `$2`, etc., refer to the first field, second field, and so on. The command `{print $2, $3}` prints the second and third fields from each line.

The other options are incorrect because:
- Option b) would print the literal numbers "2, 3" for each line, not the field values
- Option c) would print the 2nd and 3rd lines of the file, not fields
- Option d) would work for tab-delimited files but needs the `-d' '` option to specify space as the delimiter

### Question 5: Which command sorts data in reverse numerical order?
- a) `sort -n file.txt`
- b) `sort -nr file.txt`
- c) `sort -r file.txt`
- d) `sort -rn file.txt`

**Answer: b) `sort -nr file.txt` and d) `sort -rn file.txt` are both correct**

**Explanation:** Both options combine the `-n` flag for numerical sorting with the `-r` flag for reverse order. The order of these options doesn't matter in the `sort` command, so both `-nr` and `-rn` achieve the same result: sorting numbers from largest to smallest.

The other options are incorrect because:
- Option a) sorts numerically but in ascending order (smallest to largest)
- Option c) sorts in reverse alphabetical order, not numerically

### Question 6: How do you count the number of unique lines in a file?
- a) `uniq -c file.txt | wc -l`
- b) `sort file.txt | uniq | wc -l`
- c) `sort file.txt | uniq -c | wc -l`
- d) `wc -l file.txt | uniq`

**Answer: b) `sort file.txt | uniq | wc -l`**

**Explanation:** This command pipeline works in three steps:
1. `sort file.txt` - Sorts the file to bring duplicate lines together (required for `uniq`)
2. `uniq` - Filters out duplicate lines, keeping only unique ones
3. `wc -l` - Counts the number of lines after duplicates have been removed

The other options are incorrect because:
- Option a) counts each unique line with its occurrence count, which doesn't directly give the count of unique lines
- Option c) counts the number of lines after `uniq -c`, which includes count information
- Option d) tries to filter the output of `wc -l` through `uniq`, which doesn't make sense as `wc -l` outputs just a single number

## SRE Application Level Questions

### Question 7: During a performance investigation, you need to replace all occurrences of "debug" with "DEBUG" in a log file but preserve the original file. Which command should you use?
- a) `sed 's/debug/DEBUG/g' logfile.txt`
- b) `sed -i 's/debug/DEBUG/g' logfile.txt`
- c) `sed 's/debug/DEBUG/g' logfile.txt > logfile.txt`
- d) `sed 's/debug/DEBUG/g' logfile.txt > logfile_modified.txt`

**Answer: d) `sed 's/debug/DEBUG/g' logfile.txt > logfile_modified.txt`**

**Explanation:** This command performs the substitution and redirects the output to a new file (`logfile_modified.txt`), thus preserving the original file.

The other options are incorrect because:
- Option a) displays the modified content to the terminal, but doesn't save it to a file
- Option b) modifies the file in-place, which would not preserve the original file
- Option c) attempts to both read from and write to the same file in the same operation, which would result in an empty file (the file is truncated before `sed` can read from it)

In production environments, preserving original files before making changes is a critical best practice, especially for logs and configuration files.

### Question 8: To identify the top 5 most frequent error types in a log file where errors are formatted as "ERROR: [error_type]", which command pipeline would you use?
- a) `grep "ERROR" application.log | cut -d' ' -f2 | sort | uniq -c`
- b) `grep "ERROR" application.log | awk '{print $2}' | sort | uniq -c | sort -nr | head -5`
- c) `grep "ERROR" application.log | sed 's/ERROR: \[\(.*\)\]/\1/' | sort | uniq -c | sort -nr | head -5`
- d) `grep "ERROR" application.log | sort | head -5`

**Answer: c) `grep "ERROR" application.log | sed 's/ERROR: \[\(.*\)\]/\1/' | sort | uniq -c | sort -nr | head -5`**

**Explanation:** This pipeline extracts error types from log entries and finds the most common ones:
1. `grep "ERROR" application.log` - Extracts lines containing "ERROR"
2. `sed 's/ERROR: \[\(.*\)\]/\1/'` - Uses regex to extract the content between brackets after "ERROR: "
3. `sort` - Sorts the error types alphabetically to group identical types
4. `uniq -c` - Counts occurrences of each error type
5. `sort -nr` - Sorts numerically in reverse order (highest counts first)
6. `head -5` - Takes only the top 5 entries

The other options are incorrect because:
- Option a) doesn't sort by frequency or limit to top 5
- Option b) incorrectly assumes the error type is in the second field
- Option d) simply shows the first 5 error lines without any analysis of frequency or types

This type of analysis is crucial for SREs to identify systemic issues and prioritize fixes based on impact.

### Question 9: You need to count the distribution of HTTP status codes in a web server log where the status code is the 9th field. Which command would you use?
- a) `awk '{print $9}' access.log | sort`
- b) `awk '{print $9}' access.log | sort | uniq`
- c) `awk '{print $9}' access.log | sort | uniq -c`
- d) `awk '{print $9}' access.log | sort | uniq -c | sort -nr`

**Answer: d) `awk '{print $9}' access.log | sort | uniq -c | sort -nr`**

**Explanation:** This pipeline provides a complete analysis of HTTP status code distribution:
1. `awk '{print $9}' access.log` - Extracts just the 9th field (status code) from each log line
2. `sort` - Sorts the status codes to group identical codes
3. `uniq -c` - Counts occurrences of each status code
4. `sort -nr` - Sorts numerically in reverse order, showing most frequent codes first

The other options are incomplete because:
- Option a) only extracts and sorts status codes without counting them
- Option b) shows unique status codes but doesn't count them
- Option c) counts the occurrences but doesn't sort by frequency

For SREs, this pattern of aggregating and sorting by frequency is essential for understanding system behavior, identifying issues (like high rates of 5xx errors), and reporting on service health.