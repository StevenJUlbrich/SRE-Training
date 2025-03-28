# ✅ **Day 2 Quiz - Answer Key with Explanations**

## **Answers to Today's Quiz**

### **1. During an incident, you need to monitor an actively written log file in real-time. Which command is most appropriate?**

**Correct Answer:** c) `tail -f /var/log/application.log`

**Explanation:**
- `tail -f` continuously monitors a file and displays new lines as they're written ("follow" mode)
- `cat` only displays the file once and exits, not showing new content
- `less` is interactive but doesn't automatically show new content (unless using `less +F`)
- `head` only shows the beginning of the file, not helpful for monitoring new entries

**SRE Application:** During active incidents, you need to see logs in real-time to correlate errors with user reports or other metrics. The `-f` (follow) option is one of the most frequently used tools in an SRE's troubleshooting arsenal.

### **2. You need to make a backup of a critical configuration file before modifying it. Which command preserves all file attributes correctly?**

**Correct Answer:** b) `cp -a /etc/service/config.xml /etc/service/config.xml.bak`

**Explanation:**
- `cp -a` preserves all file attributes including permissions, timestamps, and ownership
- Regular `cp` without options may not preserve all metadata
- `mv` would move (rename) the file rather than create a copy
- `touch` would only create an empty file

**SRE Application:** Preserving exact file attributes in backups is crucial when working with system files that may have specific permission requirements. This helps ensure you can restore the exact original state if changes cause problems.

### **3. Which command would you use to create a nested directory structure for a new application deployment?**

**Correct Answer:** `mkdir -p /opt/application/logs/debug`

**Explanation:**
- `mkdir -p` creates parent directories as needed
- Without the `-p` option, mkdir would fail if `/opt/application/logs` doesn't already exist
- This creates the full path in one command, rather than requiring multiple mkdir commands

**SRE Application:** When deploying applications or setting up new services, you often need to create entire directory structures. The `-p` option saves time and prevents errors during deployment scripts or automation.

### **4. You need to clean up old temporary files in the `/tmp` directory but want to be prompted before each deletion. Which command should you use?**

**Correct Answer:** c) `rm -i /tmp/*.old`

**Explanation:**
- `rm -i` prompts for confirmation before each file deletion
- Regular `rm` without options deletes without prompting
- `rm -f` forces deletion without prompts (the opposite of what's needed)
- `rmdir` only removes empty directories, not files

**SRE Application:** Interactive deletion is safer on production systems, especially when using wildcards that might match more files than intended. This helps prevent accidental deletion of important files.

### **5. During a post-incident analysis, you need to check the first 50 lines of a log file to understand the initial error conditions. Which command would you use?**

**Correct Answer:** b) `head -n 50 /var/log/service.log`

**Explanation:**
- `head -n 50` displays exactly the first 50 lines of the file
- `cat -n 50` is incorrect syntax; `cat` doesn't accept a number of lines parameter
- `tail -n 50` shows the last 50 lines, not the first (would show recent events, not initial conditions)
- `less -n 50` is incorrect syntax; while `less` can show line numbers with `-N`, it doesn't limit display to 50 lines

**SRE Application:** In post-incident analysis, understanding how an incident began is often critical. Application initialization errors often appear at the beginning of log files, making `head` an important tool for investigating startup issues.

## **SRE Application**

These file operations commands are foundational skills for SRE work:

1. **Incident Response**: Using `tail -f` to monitor logs in real-time or `head` to check initialization errors gives you immediate visibility into system behavior.

2. **Change Management**: Creating proper backups with `cp -a` before making configuration changes provides a safety net for rapid rollback if needed.

3. **System Organization**: Using `mkdir -p` for structured directory creation ensures consistent system organization, which is important for maintainability.

4. **Safe Operations**: Using `-i` interactive flags for destructive operations adds a verification step that can prevent costly mistakes in production.

5. **Log Analysis**: Different commands for viewing different parts of files (`head`, `tail`, `less`) let you focus your analysis on the most relevant sections of logs.

These commands form the core toolkit for day-to-day SRE operations, whether you're deploying new services, troubleshooting issues, or performing routine maintenance.
