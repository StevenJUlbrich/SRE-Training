# ✅ **Day 4 Quiz - Answer Key with Explanations**

## **Answers to Today's Quiz**

### **1. During an incident, you need to find all occurrences of "connection timeout" in logs, including the lines before and after each occurrence to understand the context. Which command would you use?**

**Correct Answer:** b) `grep -A 2 -B 2 "connection timeout" /var/log/application.log`

**Explanation:**
- `-A 2` shows 2 lines after each match
- `-B 2` shows 2 lines before each match
- This provides crucial context around each occurrence of the error
- Option a) shows only the matching lines without context
- Option c) uses `find` which searches for files, not text within files
- Option d) shows all lines that do NOT contain the pattern

**SRE Application:** Context is critical during incident investigation. Errors rarely exist in isolation, and the events leading up to and following an error often contain valuable diagnostic information. Using the context flags with `grep` allows you to see the sequence of events without manually searching through the entire log file.

### **2. You need to find all configuration files larger than 1MB in the /etc directory. Which command is correct?**

**Correct Answer:** `find /etc -type f -size +1M`

**Explanation:**
- `-type f` restricts the search to regular files (not directories)
- `-size +1M` specifies files larger than 1 megabyte
- We search in `/etc` where most system configuration files are stored

**SRE Application:** Unusually large configuration files often indicate problems like unchecked growth, improper rotation, or automated tools writing excessive data. In the SRE context, this command helps identify potential issues during system audits or when troubleshooting disk space problems.

### **3. To extract the number of 5xx errors from a web server log and save the count to a file, which pipeline would you use?**

**Correct Answer:** a) `grep "HTTP/1.1\" 5[0-9][0-9]" access.log | wc -l > 5xx_count.txt`

**Explanation:**
- `grep "HTTP/1.1\" 5[0-9][0-9]"` matches HTTP response codes in the 500-599 range
- `wc -l` counts the number of matching lines
- `> 5xx_count.txt` redirects the count to a file
- Option b) would incorrectly count occurrences of the pattern "5xx" itself, not HTTP status codes
- Option c) incorrectly uses `find` to search within files
- Option d) only checks the end of the log and doesn't count the matches

**SRE Application:** Counting error rates is a fundamental SRE task for establishing baselines and monitoring system health. This pipeline helps quantify the scale of a problem during an incident and can be used in scripts that trigger alerts when error rates exceed thresholds.

### **4. During system maintenance, you need to append the output of a disk space check to a log file without overwriting existing content. Which redirection operator would you use?**

**Correct Answer:** b) `df -h >> maintenance.log`

**Explanation:**
- `>>` appends output to a file without overwriting existing content
- `>` would overwrite the existing file (erasing previous maintenance notes)
- `|` is a pipe operator, not a redirection to a file
- `2>` redirects only standard error, not standard output

**SRE Application:** Maintaining accurate records during maintenance is essential for compliance, post-maintenance analysis, and handovers between team members during long maintenance windows. The append operator ensures that all maintenance steps are documented sequentially without losing information.

### **5. You suspect a security issue and need to find all files modified in the last 24 hours anywhere on the system. Which command is most appropriate?**

**Correct Answer:** c) `find / -mtime -1 -type f`

**Explanation:**
- `-mtime -1` finds files modified less than 1 day (24 hours) ago
- `-type f` restricts results to regular files (not directories)
- The search starts from the root `/` to scan the entire system
- Option a) incorrectly uses `ls` which cannot recursively search an entire filesystem
- Option b) uses incorrect syntax for `-mtime` (it should be -1 for "less than 1 day ago")
- Option d) uses `grep` incorrectly; it searches file contents, not file attributes

**SRE Application:** During security incidents, identifying recently modified files is critical for detecting unauthorized changes or malware. This command helps SREs quickly establish a timeline of potential system compromise and identify files that might need further investigation or restoration from backups.

## **SRE Application: Text Processing in Production Environments**

The commands covered today form the foundation of SRE troubleshooting workflows:

1. **Rapid Incident Response:** Using `grep` with context flags allows SREs to quickly find and understand error patterns in large log files, reducing mean time to resolution (MTTR).

2. **Proactive Monitoring:** Commands like `find` help identify potential issues (large files, permission problems, recent changes) before they affect service reliability.

3. **Root Cause Analysis:** Command pipelines combining multiple tools enable deeper analysis of complex issues by correlating data from different sources.

4. **Automation:** Redirecting command output to files enables automated reporting and dashboarding for operational issues.

5. **Knowledge Transfer:** Well-documented command pipelines preserve troubleshooting knowledge, helping teams collaborate during incidents and maintain consistent operational practices.

These text processing skills directly impact key SRE metrics like MTTR (Mean Time to Resolution) and the ability to maintain low error budgets by quickly identifying and addressing service issues.
