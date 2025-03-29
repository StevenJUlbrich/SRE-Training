# 📝 **Day 3: Permissions & Ownership Quiz - Answer Key with Explanations**

## Beginner Level Questions

### Question 1: Which command displays detailed file information including permissions?
- a) `dir -l`
- b) `ls -l`
- c) `cat -l`
- d) `perms -show`

**Answer: b) `ls -l`**

**Explanation:** The `ls -l` command (list with long format) shows detailed information about files, including:
- File permissions
- Number of links
- Owner name
- Group name
- File size
- Timestamp
- Filename

The other options are incorrect because:
- `dir -l` is not a standard Linux command (though in some Linux distributions, `dir` may be aliased to `ls`)
- `cat -l` is invalid; `cat` displays file contents but doesn't have a `-l` option for showing permissions
- `perms -show` is not a standard Linux command

### Question 2: In the permission string `-rw-r--r--`, what permissions does the file owner have?
- a) Read only
- b) Read and write
- c) Read, write, and execute
- d) No permissions

**Answer: b) Read and write**

**Explanation:** The permission string `-rw-r--r--` breaks down as follows:
- First character `-` indicates this is a regular file (not a directory or other special file type)
- The next three characters `rw-` represent the owner's permissions:
  - `r` = read permission (present)
  - `w` = write permission (present)
  - `-` = execute permission (absent)

Therefore, the owner has read and write permission, but not execute permission.

### Question 3: Which command adds execute permission for the owner of a file?
- a) `chmod +x file.sh`
- b) `chmod u+x file.sh`
- c) `chmod a+x file.sh`
- d) `chmod x+u file.sh`

**Answer: b) `chmod u+x file.sh`**

**Explanation:** The `chmod u+x file.sh` command specifically adds execute permission for the user (owner) of the file. 

The other options are incorrect because:
- `chmod +x file.sh` adds execute permission for all categories (user, group, and others), not just the owner
- `chmod a+x file.sh` also adds execute permission for all categories (a = all)
- `chmod x+u file.sh` has incorrect syntax; the permission (`x`) should come after the operator (`+`), not before

## Intermediate Level Questions

### Question 4: What numeric value represents read and write permission but not execute?
- a) 7
- b) 5
- c) 6
- d) 3

**Answer: c) 6**

**Explanation:** In the numeric permission system:
- Read (r) = 4
- Write (w) = 2
- Execute (x) = 1

To represent multiple permissions, you add these values together:
- Read + Write = 4 + 2 = 6
- Read + Execute = 4 + 1 = 5
- Write + Execute = 2 + 1 = 3
- Read + Write + Execute = 4 + 2 + 1 = 7

Therefore, 6 represents read and write permission but not execute.

### Question 5: Which permission setting allows the owner to read, write, and execute, the group to read and execute, and gives no permissions to others?
- a) `chmod 640 script.sh`
- b) `chmod 750 script.sh`
- c) `chmod 755 script.sh`
- d) `chmod 770 script.sh`

**Answer: b) `chmod 750 script.sh`**

**Explanation:** To determine the correct numeric permissions, we need to calculate each digit separately:

For the owner: read (4) + write (2) + execute (1) = 7
For the group: read (4) + execute (1) = 5
For others: no permissions = 0

Therefore, 750 is the correct setting.

The other options are incorrect because:
- `chmod 640 script.sh` gives read+write (6) to owner, read (4) to group, and no permissions (0) to others, but the owner doesn't have execute permission
- `chmod 755 script.sh` gives read+write+execute (7) to owner, read+execute (5) to group, and read+execute (5) to others, but others should have no permissions
- `chmod 770 script.sh` gives read+write+execute (7) to owner, read+write+execute (7) to group, and no permissions (0) to others, but the group should only have read+execute

### Question 6: To change both the owner and group of a file to "webuser" and "webteam" respectively, which command would you use?
- a) `sudo chown webuser + webteam file.html`
- b) `sudo chown webuser:webteam file.html`
- c) `sudo chown webuser webteam file.html`
- d) `sudo chgrp webuser webteam file.html`

**Answer: b) `sudo chown webuser:webteam file.html`**

**Explanation:** The correct syntax for changing both owner and group with `chown` is to separate the username and group name with a colon `:`.

The other options are incorrect because:
- `sudo chown webuser + webteam file.html` uses an invalid syntax with the `+` symbol
- `sudo chown webuser webteam file.html` would try to change the owner to "webuser" and then treat "webteam" and "file.html" as separate files to be processed
- `sudo chgrp webuser webteam file.html` is incorrect because `chgrp` only changes the group, not the owner, and has incorrect syntax (it would try to change the group to "webuser" and then treat "webteam" and "file.html" as separate files)

## SRE Application Level Questions

### Question 7: An SRE notices that an application is failing with "Permission denied" errors when trying to write to its log file. The application runs as user `appuser`. What command would fix this issue?
- a) `chmod 777 /var/log/app.log`
- b) `chmod 644 /var/log/app.log`
- c) `sudo chown appuser /var/log/app.log`
- d) `sudo chmod +r /var/log/app.log`

**Answer: c) `sudo chown appuser /var/log/app.log`**

**Explanation:** The issue is that the application running as `appuser` can't write to its log file. The most appropriate solution is to change the ownership of the log file to `appuser` so the application can write to it.

The other options are incorrect or problematic because:
- `chmod 777 /var/log/app.log` (option a) would make the file writable by everyone, creating a serious security vulnerability
- `chmod 644 /var/log/app.log` (option b) sets read/write for owner and read-only for group and others, but doesn't address who the owner is
- `sudo chmod +r /var/log/app.log` (option d) only adds read permission, but the application needs write permission to update the log

From an SRE perspective, giving ownership to the specific application user follows the principle of least privilege, ensuring the app can write logs without unnecessary security risks.

### Question 8: During a security audit, you need to identify files with the setuid bit set. Which command would you use?
- a) `find / -type f -perm -4000 -ls`
- b) `ls -l / | grep s`
- c) `chmod -R -s /`
- d) `chown -R root:root /`

**Answer: a) `find / -type f -perm -4000 -ls`**

**Explanation:** This command finds all files (`-type f`) from the root directory that have the setuid bit set (`-perm -4000`) and displays detailed information about them (`-ls`).

The setuid bit (4000) is a special permission that allows users to run an executable with the permissions of the file owner. It's important to audit these files as they can be security risks if compromised.

The other options are incorrect because:
- `ls -l / | grep s` only looks for the setuid bit in files directly in the root directory, not recursively, and the pattern 's' might match other text
- `chmod -R -s /` would recursively remove the setuid bit from all files (extremely dangerous and potentially system-breaking)
- `chown -R root:root /` would recursively change ownership of all files to root (extremely dangerous and would break system functionality)

### Question 9: A junior SRE has accidentally changed permissions on the `/etc` directory. What is the correct command to recursively restore default permissions (755 for directories, 644 for files) without compromising security?
- a) `sudo chmod -R 777 /etc`
- b) `sudo chmod -R 755 /etc`
- c) (This requires a more complex approach, not a single command)
- d) `sudo chmod -R 644 /etc`

**Answer: c) (This requires a more complex approach, not a single command)**

**Explanation:** Setting the same permissions for both files and directories is incorrect because:
1. Directories need execute permission to be accessible
2. Many files in `/etc` require specific permissions for security

The correct approach would be a combination of commands that set different permissions for files versus directories:
```bash
sudo find /etc -type d -exec chmod 755 {} \;  # Set 755 for directories
sudo find /etc -type f -exec chmod 644 {} \;  # Set 644 for regular files
```

The other options are incorrect because:
- `sudo chmod -R 777 /etc` would create a severe security vulnerability by making all configuration files writable by everyone
- `sudo chmod -R 755 /etc` would incorrectly set execute permissions on all files
- `sudo chmod -R 644 /etc` would remove execute permissions from directories, making them inaccessible

This question illustrates an important SRE concept: sometimes there isn't a single simple command to fix complex issues, and a more thoughtful approach is required.