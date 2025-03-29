# 🗝️ **Instructor Quiz Answer Key Day 4**

## 🟢 **Beginner Tier Answers**

**Question 1 (Multiple-Choice):**  
_What is the correct command to search the file `log.txt` for the word `"error"`, ignoring case sensitivity?_

- **Correct Answer:** B) `grep -i error log.txt`  
- **Explicit Explanation:** The `-i` option explicitly tells `grep` to ignore the case, ensuring matches like "ERROR," "Error," or "error" are included.

---

**Question 2 (Fill-in-the-Blank):**  
_Complete the command to explicitly find all files ending with `.log` in the current directory:_

- **Correct Answer:** `f`  
- **Completed Command:** `find . -type f -name "*.log"`
- **Explicit Explanation:** The flag `-type f` explicitly indicates searching only for regular files (not directories or symlinks).

---

**Question 3 (Scenario-based):**  
_You explicitly redirected output using `ls > files.txt`. What happens if `files.txt` already existed?_

- **Correct Answer:** B) It explicitly overwrites the existing content.
- **Explicit Explanation:** The redirection operator `>` explicitly overwrites any existing file content, unlike `>>`, which appends.

---

## 🟡 **Intermediate Tier Answers**

**Question 1 (Multiple-Choice):**  
_Which command explicitly finds files modified in the last 24 hours in `/var`?_

- **Correct Answer:** B) `find /var -mtime -1`
- **Explicit Explanation:** The `-mtime -1` explicitly indicates files modified within the last 1 day (24 hours). Positive numbers (`+1`) explicitly find files older than 1 day.

---

**Question 2 (Scenario-based):**  
_Explicitly identify which pipeline correctly counts the number of running processes explicitly containing `"httpd"`:_

- **Correct Answer:** A) `ps aux | grep "httpd" | wc -l`
- **Explicit Explanation:** `ps aux` explicitly lists processes, piping (`|`) to `grep "httpd"` explicitly filters processes containing `"httpd"`, and piping to `wc -l` explicitly counts them.

---

**Question 3 (Fill-in-the-Blank):**  
_Complete the explicit command pipeline to display the top 5 largest directories under `/var`:_

- **Correct Answer:** `head -5`
- **Completed Command:** `du -sh /var/* | sort -hr | head -5`
- **Explicit Explanation:** `head -5` explicitly selects the top 5 results from the sorted list provided by `du -sh` and `sort`.

---

## 🔴 **SRE-Level Tier Answers**

**Question 1 (Multiple-Choice):**  
_During a critical incident, you need real-time monitoring of the system logs explicitly filtering critical errors. Which command explicitly achieves this without buffering issues?_

- **Correct Answer:** B) `tail -f syslog | grep --line-buffered "ERROR\|CRITICAL"`
- **Explicit Explanation:** The explicit use of `grep --line-buffered` ensures real-time output by explicitly preventing buffering delays, critical during incident response.

---

**Question 2 (Scenario-based):**  
_An SRE needs to explicitly summarize HTTP errors (`4xx`, `5xx`) from an access log quickly. Which command pipeline explicitly achieves this accurately?_

- **Correct Answer:** B) `grep "HTTP/1.1\" [45]" access.log | awk '{print $9}' | sort | uniq -c`
- **Explicit Explanation:** This pipeline explicitly extracts HTTP status codes (`4xx` and `5xx`), sorts, and counts their occurrences, providing a quick, accurate summary of errors.

---

**Question 3 (Fill-in-the-Blank):**  
_Complete the explicit command pipeline to remove files older than 30 days from `/tmp` and explicitly log deleted files:_

- **Correct Answer:** `>>`
- **Completed Command:** `find /tmp -type f -mtime +30 -exec rm -v {} \; >> cleanup.log`
- **Explicit Explanation:** The explicit use of `>> cleanup.log` appends detailed output of removed files explicitly logged by `rm -v`, preserving a record of deleted items.
