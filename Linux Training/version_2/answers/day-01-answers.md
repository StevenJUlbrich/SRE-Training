# ✅ **Day 1 Quiz - Answer Key with Explanations**

## **Answers to Today's Quiz**

### **1. Which command displays your current location in the filesystem?**

**Correct Answer:** b) `pwd`

**Explanation:**

- `pwd` stands for "Print Working Directory" and displays your current location
- `dir` is primarily used in Windows/DOS environments, not standard Linux
- `loc` is not a standard Linux command
- `cd` is used to change directories, not display your current location

### **2. You need to check the timestamps of log files during an incident. Which command shows the most recently modified files first?**

**Correct Answer:** c) `ls -lt`

**Explanation:**

- `-l` provides the long listing format that includes timestamps
- `-t` sorts files by modification time (newest first)
- Combined, `ls -lt` gives a detailed listing sorted by time
- `ls -r` would reverse the default sort order (alphabetical by default)
- `ls -a` only shows hidden files, doesn't affect sorting
- `ls -h` makes file sizes human-readable, doesn't affect sorting

### **3. How do you list all files, including hidden ones, with detailed information in human-readable format?**

**Correct Answer:** b) `ls -lah`

**Explanation:**

- `-l` provides the long format listing with detailed information
- `-a` shows all files including hidden ones (those starting with a dot)
- `-h` displays file sizes in human-readable format (KB, MB, GB)
- All three options can be combined as shown: `ls -lah`

### **4. During an incident, you need to quickly look up the options for the `grep` command. Which is the fastest way?**

**Correct Answer:** b) `grep --help`

**Explanation:**

- `grep --help` gives a concise summary of options directly in the terminal
- `man grep` provides comprehensive documentation but takes longer to navigate
- `info grep` provides detailed documentation in a structured format but is slower to access
- `help grep` is not a standard command for most Linux distributions

### **5. In the Linux filesystem hierarchy, which directory typically contains log files that SREs need to examine during troubleshooting?**

**Correct Answer:** c) `/var/log`

**Explanation:**

- `/var/log` is the standard directory for system and application log files
- `/log` typically doesn't exist in standard Linux distributions
- `/usr/log` is not a standard directory in the Filesystem Hierarchy Standard
- `/etc/log` would be incorrect; `/etc` contains configuration files, not logs

## **SRE Application**

Understanding these commands is fundamental for SRE work. When responding to incidents, you need to:

1. **Understand your environment** - Using `pwd` ensures you're in the right location before executing commands
2. **Quickly locate recent changes** - Using `ls -lt` helps you identify recent file modifications that might relate to an incident
3. **Find all relevant files** - Using `ls -lah` ensures you don't miss hidden configuration files
4. **Get command help efficiently** - Using `--help` during incidents saves precious time
5. **Know where to look for evidence** - Understanding the filesystem hierarchy points you to logs in `/var/log` and configurations in `/etc`

As you progress in your SRE journey, these basic commands become second nature, allowing you to focus more on problem-solving and less on "how do I navigate this system?"
