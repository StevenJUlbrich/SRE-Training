# Day 5 Answser Sheet

## **Beginner Level (4 Questions)**

### 1. How do you replace all instances of `apple` with `Apple` in `fruit.txt` using sed?

**Answer:**

```bash
sed 's/apple/Apple/g' fruit.txt
```

**Explanation:**

- `s/apple/Apple/g` is the substitution command in sed.
- `apple` is the pattern to find; `Apple` is the replacement text.
- The `g` at the end stands for “global,” which means “replace all occurrences on each line,” rather than stopping after the first match.

---

### 2. Which part of a line does `$3` represent in an awk command?

**Answer:**

- `$3` represents the **third field** (column) in the current input line.

**Explanation:**

- By default, awk splits each line into fields using whitespace.
- `$1` is the first field, `$2` is the second, `$3` is the third, and so on.
- `$0` would represent the entire line as a single string.

---

### 3. By default, does `sort` sort data numerically or lexicographically?

**Answer:**

- **Lexicographically** (alphabetically).

**Explanation:**

- If you have numbers in a file such as `2`, `10`, `100`, lexicographic order would place `10` before `2`.
- To sort them numerically, you must use the `-n` (numeric) option.

---

### 4. What does `wc -l logfile.txt` show?

**Answer:**

- It shows the **number of lines** in `logfile.txt`.

**Explanation:**

- `wc` stands for “word count,” but it can also count lines, words, or bytes depending on the option used.
- The `-l` option specifically counts lines.

---

## **Intermediate Level (4 Questions)**

### 1. How would you remove lines beginning with `#` in a file using sed?

**Answer:**

```bash
sed '/^#/d' filename
```

**Explanation:**

- The regex `^#` matches any line starting (`^`) with a `#`.
- The `d` command in sed deletes these matching lines.
- This is often used to remove commented lines from configuration or data files.

---

### 2. Why is sorting usually necessary before using `uniq`?

**Answer:**

- Because **uniq only detects and merges duplicates that appear on consecutive lines**.

**Explanation:**

- If duplicates are scattered throughout the file, `uniq` will miss them unless they’re grouped together.
- `sort` groups identical lines, ensuring that all duplicates become adjacent, so `uniq` can properly identify them.

---

### 3. What does `awk '$3 > 50 {print $0}' data.txt` do?

**Answer:**

- It **prints the entire line (`$0`)** whenever the **third field (`$3`)** is **greater than 50**.

**Explanation:**

- awk applies the condition `$3 > 50` to each line.
- If the condition is true, `{print $0}` executes, printing the entire line.

---

### 4. Why might running `sort -nr big.log` consume significant system resources?

**Answer:**

- Sorting a **large file** is **CPU- and memory-intensive**. The system may create large temporary files and use extensive memory to reorder lines.

**Explanation:**

- The `-n` (numeric) and `-r` (reverse) flags don’t themselves reduce resource usage; they simply change sorting criteria.
- As file size grows (multi-GB logs, for example), sorting operations become expensive, impacting performance.

---

## **SRE-Level (4 Questions)**

### 1. What is a key risk of using `sed -i` on production configuration files?

**Answer:**

- You may **overwrite or corrupt** the configuration file if something goes wrong (e.g., a crash, a bad pattern), and there is **no automatic backup**.

**Explanation:**

- The `-i` option edits a file “in place,” so if the process is interrupted or the command is incorrect, you could end up with a partially edited (or totally broken) file.
- In production, consider creating manual backups or using version control before running in-place edits.

---

### 2. How can advanced regex in `sed` or `awk` help parse multiline or complex structured data?

**Answer:**

- Advanced regex can **match patterns spanning multiple lines**, handle more intricate record delimiters, or extract fields with unusual separators.

**Explanation:**

- `sed` offers hold and pattern spaces for multiline operations.
- `awk` can change its record separator (`RS`) for multiline processing or use more complex patterns to parse structured data.
- This is crucial for logs that store large messages or multi-line configurations.

---

### 3. Give one advantage of chaining `grep`, `awk`, `sort`, `uniq`, and `wc` in a single pipeline

**Answer (example advantage):**

- **Efficiency**: You can **filter**, **extract**, **sort**, **count duplicates**, and **measure total lines** all in **one pass**, **reducing overhead** and avoiding intermediate files.

**Explanation:**

- Each command in the pipeline does a small part of the work and passes results to the next command.
- This “assembly line” approach is faster and more elegant than running each operation separately and writing intermediate results to disk.

---

### 4. How might you use `wc` to detect abnormal log growth patterns?

**Answer:**

- Periodically run `wc -l` on the log, **compare the new line count with an older snapshot**, and **trigger an alert** if growth exceeds a threshold.

**Explanation:**

- For instance, you can use a script that checks log size every minute (or every few seconds):

  ```bash
  prev_count=0
  while true; do
    current_count=$(wc -l < /var/log/your_app.log)
    if (( current_count - prev_count > 1000 )); then
      echo \"Large spike in log entries!\"
    fi
    prev_count=$current_count
    sleep 60
  done
  ```

- This helps identify sudden surges in log entries, often indicating an incident or system fault.

---

**End of Answer Sheet**  

This completes the answer sheet for all quiz questions from the merged Day 5 training document, with each response expanded to show the “why” or “how” behind the solution.
