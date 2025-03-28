# 📝 **Day 2: File Operations Quiz - Answer Key with Explanations**

## Beginner Level Questions

### Question 1: Which command creates an empty file or updates a file's timestamp?
- a) `mkdir`
- b) `touch`
- c) `cat`
- d) `cp`

**Answer: b) `touch`**

**Explanation:** The `touch` command serves two primary purposes:
1. Creating empty files when the specified filename doesn't exist
2. Updating the access and modification timestamps of existing files

The other options have different functions:
- `mkdir` creates directories, not regular files
- `cat` displays file contents or concatenates files
- `cp` copies files or directories

### Question 2: To create a directory called "photos", you would type:
- a) `dir photos`
- b) `mkdir photos`
- c) `touch photos`
- d) `cd photos`

**Answer: b) `mkdir photos`**

**Explanation:** The `mkdir` (make directory) command is specifically designed to create new directories in Linux systems. 

The other options are incorrect because:
- `dir photos` is not a standard Linux command (though in some systems it might be an alias for `ls`)
- `touch photos` would create an empty regular file named "photos", not a directory
- `cd photos` attempts to change directory to "photos" but doesn't create it

### Question 3: Which command would you use to rename a file from "old.txt" to "new.txt"?
- a) `cp old.txt new.txt`
- b) `mv old.txt new.txt`
- c) `rn old.txt new.txt`
- d) `name old.txt new.txt`

**Answer: b) `mv old.txt new.txt`**

**Explanation:** In Linux, the `mv` (move) command is used for both moving files to different locations and renaming files. When both the source and destination are in the same directory, it functions as a rename operation.

The other options are incorrect because:
- `cp old.txt new.txt` would create a copy with the new name, leaving the original file intact
- `rn old.txt new.txt` is not a standard Linux command
- `name old.txt new.txt` is not a standard Linux command

## Intermediate Level Questions

### Question 4: Which option of `mkdir` allows you to create nested directories like "a/b/c" all at once?
- a) `-r`
- b) `-p`
- c) `-n`
- d) `-m`

**Answer: b) `-p`**

**Explanation:** The `-p` option (parents) of `mkdir` creates parent directories as needed. Without this option, trying to create a directory when its parent doesn't exist would result in an error.

The other options are incorrect because:
- `-r` is not a standard option for `mkdir` (though it's used with other commands like `cp` for recursive operations)
- `-n` is not a standard option for `mkdir`
- `-m` sets the permission mode for directories but doesn't help with creating nested directories

### Question 5: How do you list all lines of a file with line numbers?
- a) `cat -n file.txt`
- b) `less -N file.txt`
- c) Both a and b
- d) Neither a nor b

**Answer: c) Both a and b**

**Explanation:** Both commands can display file contents with line numbers, but they work differently:
- `cat -n file.txt` displays the entire file at once with line numbers
- `less -N file.txt` displays the file in a paginated, scrollable view with line numbers

These are complementary tools for different situations:
- `cat -n` is better for smaller files where you want to see everything at once
- `less -N` is better for larger files where pagination and searching are needed

### Question 6: Which command would you use to copy a directory and all its contents while preserving file attributes?
- a) `cp dir1 dir2`
- b) `cp -r dir1 dir2`
- c) `cp -a dir1 dir2`
- d) `mv dir1 dir2`

**Answer: c) `cp -a dir1 dir2`**

**Explanation:** The `-a` (archive) option of `cp` is specifically designed for making backups as it:
1. Copies directories recursively (-r)
2. Preserves file permissions
3. Preserves ownership (if you have sufficient privileges)
4. Preserves timestamps
5. Preserves links

The other options are incorrect or incomplete because:
- `cp dir1 dir2` without any options won't copy a directory's contents
- `cp -r dir1 dir2` copies recursively but doesn't preserve all file attributes
- `mv dir1 dir2` moves/renames the directory rather than copying it

## SRE Application Level Questions

### Question 7: During an incident, you need to monitor a log file that's being actively written to. Which command is most appropriate?
- a) `cat /var/log/app.log`
- b) `more /var/log/app.log`
- c) `tail -f /var/log/app.log`
- d) `head /var/log/app.log`

**Answer: c) `tail -f /var/log/app.log`**

**Explanation:** The `tail -f` command is specifically designed for real-time monitoring of log files:
- The `-f` (follow) option keeps the file open and continuously displays new lines as they are written
- This makes it ideal for watching logs during active incidents to see errors as they occur

The other options are incorrect because:
- `cat /var/log/app.log` displays the entire file once but won't show new entries without running it again
- `more /var/log/app.log` provides pagination but doesn't update with new content
- `head /var/log/app.log` shows only the first 10 lines (by default) and then exits

SREs frequently use `tail -f` during incident response to observe system behavior in real-time.

### Question 8: You need to make changes to a critical configuration file. What should you do first?
- a) Edit the file directly with a text editor
- b) Make a backup with `cp -a config.file config.file.bak`
- c) Run `touch config.file` to update the timestamp
- d) Delete the file and create a new one

**Answer: b) Make a backup with `cp -a config.file config.file.bak`**

**Explanation:** Making a backup before modifying critical files is a fundamental SRE best practice:
1. It allows for quick recovery if changes cause problems
2. It provides an audit trail of what was changed
3. Using the `-a` option ensures all file attributes are preserved

The other options are incorrect because:
- Editing the file directly without a backup creates risk of unrecoverable errors
- Updating the timestamp with `touch` provides no protection or rollback ability
- Deleting and recreating the file would lose all original content and attributes

In production environments, SREs might use an even more robust backup approach with timestamped filenames:
```bash
cp -a config.file config.file.$(date +%Y%m%d-%H%M%S).bak
```

### Question 9: A server is running out of disk space due to log files. Which sequence of commands would help identify and address the issue?
- a) `rm -rf /var/log/*`
- b) `ls -l /var/log; cat /var/log/*`
- c) `du -h /var/log | sort -hr; tail -n 10 /var/log/large.log; mv large.log /tmp/`
- d) `touch /var/log/newfile.log`

**Answer: c) `du -h /var/log | sort -hr; tail -n 10 /var/log/large.log; mv large.log /tmp/`**

**Explanation:** This sequence follows a methodical troubleshooting approach:
1. `du -h /var/log | sort -hr` identifies the largest log files by size
2. `tail -n 10 /var/log/large.log` examines recent entries in the large log file
3. `mv large.log /tmp/` moves the file to free up space while preserving its contents for analysis

The other options are incorrect because:
- `rm -rf /var/log/*` is dangerously destructive, removing all logs without analysis
- `ls -l /var/log; cat /var/log/*` only lists files and then tries to display all logs (which could overwhelm the terminal and doesn't solve the space issue)
- `touch /var/log/newfile.log` creates a new empty file, which doesn't help with disk space issues

This methodical approach exemplifies how SREs should address system issues: identify the problem, gather information, then take appropriate action while preserving important data.