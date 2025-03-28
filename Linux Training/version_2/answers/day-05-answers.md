# ✅ **Day 5 Quiz - Answer Key with Explanations**

## **Answers to Today's Quiz**

### **1. During a performance investigation, you need to replace all occurrences of "debug" with "DEBUG" in a log file but preserve the original file. Which command should you use?**

**Correct Answer:** d) `sed 's/debug/DEBUG/g' logfile.txt > logfile_modified.txt`

**Explanation:**
- This command performs the substitution and writes the output to a new file `logfile_modified.txt`, preserving the original file
- Option a) `sed 's/debug/DEBUG/g' logfile.txt` only outputs to the terminal but doesn't save the changes
- Option b) `sed -i 's/debug/DEBUG/g' logfile.txt` modifies the file in-place, which doesn't preserve the original
- Option c) `sed 's/debug/DEBUG/g' logfile.txt > logfile.txt` attempts to write to the same file being read, which would result in an empty file

**SRE Application:** When analyzing production logs, it's essential to preserve the original data for audit trails and to prevent data loss. Creating a modified copy ensures you can always reference the original if needed, especially during incident investigations.

### **2. You're analyzing a CSV file with fields separated by commas and need to extract the third column. Which command is most appropriate?**

**Correct Answer:** `awk -F',' '{print $3}' data.csv`

**Explanation:**
- `-F','` sets the field separator to a comma, which is necessary for CSV files
- `{print $3}` prints the third field of each line
- Without specifying the field separator, awk would use whitespace as the default delimiter, which wouldn't work correctly for CSV files

**SRE Application:** SREs often need to extract specific metrics or values from structured data files like CSVs. Being able to correctly specify field separators is crucial when working with data exports from monitoring systems or when analyzing performance data.

### **3. To identify the top 5 most frequent error types in a log file where errors are formatted as "ERROR: [error_type]", which command pipeline would you use?**

**Correct Answer:** c) `grep "ERROR" application.log | sed 's/ERROR: \[\(.*\)\]/\1/' | sort | uniq -c | sort -nr | head -5`

**Explanation:**
- `grep "ERROR" application.log` extracts all error lines
- `sed 's/ERROR: \[\(.*\)\]/\1/'` uses a capture group to extract just the error type within brackets
- `sort | uniq -c` counts the occurrences of each error type
- `sort -nr` orders the results numerically in reverse (highest counts first)
- `head -5` limits the output to the top 5 results
- The other options either extract incorrect fields or don't properly process the error format

**SRE Application:** Categorizing errors by type and frequency helps SREs prioritize fixes and understand the impact of different issues. This pipeline demonstrates how to extract structured information from semi-structured logs, a common requirement in incident analysis.

### **4. During capacity planning, you need to find directories consuming the most disk space and sort them by size. Which command pipeline is correct?**

**Correct Answer:** a) `du -h /var | sort -hr | head -10`

**Explanation:**
- `du -h /var` displays the disk usage of directories under /var in human-readable format
- `sort -hr` sorts the output numerically in reverse order based on human-readable sizes (G, M, K)
- `head -10` limits the output to the top 10 largest directories
- Option b) uses `find` which doesn't measure directory sizes
- Option c) uses `ls -la` which only shows the sizes of directory entries, not the total size of their contents
- Option d) incorrectly filters for only gigabyte-sized directories

**SRE Application:** Disk space management is a common SRE task, especially for preventing disk-full incidents. This command helps identify the largest directories, which is often the first step in managing disk space on production systems.

### **5. You need to count the distribution of HTTP status codes in a web server log where the status code is the 9th field. Which command would you use?**

**Correct Answer:** d) `awk '{print $9}' access.log | sort | uniq -c | sort -nr`

**Explanation:**
- `awk '{print $9}' access.log` extracts the 9th field (HTTP status code)
- `sort` organizes the status codes
- `uniq -c` counts the occurrences of each unique status code
- `sort -nr` sorts the results numerically in reverse order (highest counts first)
- Option a) only extracts the status codes without counting them
- Option b) shows unique status codes without counts
- Option c) counts the status codes but doesn't sort them by frequency

**SRE Application:** Analyzing HTTP status code distribution helps SREs understand error rates and service health. This pattern (extract > sort > count > sort by count) is one of the most common and useful text processing workflows for log analysis in SRE practice.

## **SRE Application: Advanced Text Processing in Production Environments**

These advanced text processing tools form the backbone of SRE log analysis and data processing workflows:

1. **Post-Incident Analysis:** SREs use these tools to piece together what happened during an incident, looking for patterns across multiple log sources and correlation between events.

2. **Configuration Management:** Tools like `sed` help automate configuration changes across multiple files and servers, reducing the risk of human error during deployments.

3. **Capacity Planning:** The ability to extract, process, and analyze metrics from various sources using `awk`, `sort`, and other tools helps SREs make data-driven decisions about resource allocation.

4. **Automated Reporting:** Combining these tools into scripts enables automated health checks and reporting that provide ongoing visibility into system performance.

5. **Alert Tuning:** By analyzing patterns in logs, SREs can identify signal-to-noise ratios and refine alerting thresholds to reduce alert fatigue while still catching real issues.

The true power of these tools comes from combining them in pipelines that transform raw log data into actionable insights. Mastering these tools significantly enhances an SRE's ability to manage complex systems effectively and respond quickly to production issues.
