# ✅ **Day 9 Quiz – Answer Key with Detailed Explanations**

## Below are the answers and explanations for Day 9's archiving, compression, and package management quiz questions

---

### **Question 1:**  

**Which command creates a compressed tar archive named `backup.tar.gz` from a directory called `documents`?**

✅ **Correct Answer:**  
**a)** `tar -czf backup.tar.gz documents`

**Explanation:**  

This command combines several key tar options:

- `-c`: Create a new archive
- `-z`: Compress the archive using gzip
- `-f`: Specify the filename for the archive
- `backup.tar.gz`: The name of the output file
- `documents`: The directory to archive

The order of options matters with tar: `-f` must be followed by the filename. This command efficiently bundles all files in the `documents` directory into a single compressed archive, making it ideal for backups, file transfers, or software distribution.

The other options are incorrect because:

- Option b) `-xzf` extracts an archive rather than creating one
- Option c) omits required flags for creation and compression
- Option d) incorrectly uses gzip's output redirection instead of tar's built-in compression

---

### **Question 2:**  

**Which option would you add to the `tar` command to view the contents of an archive without extracting it?**

✅ **Correct Answer:**  
**d)** `-t`

**Explanation:**  

The `-t` (list) option instructs tar to display the contents of an archive without actually extracting the files. This is extremely useful when you want to:

- Verify what's inside an archive before extraction
- Check if a specific file exists in an archive
- Inspect the file structure and permissions

A typical usage would be:

```bash
tar -tvf archive.tar.gz
```

Where the additional `-v` provides verbose output including file permissions, ownership, size, and modification dates.

The other options serve different purposes:

- `-c`: Creates a new archive (would overwrite an existing archive)
- `-x`: Extracts files from an archive (actually unpacks the files)
- `-v`: Provides verbose output (useful with other options but doesn't list contents by itself)

---

### **Question 3:**  

**On a Debian-based system, what command would you use to see detailed information about an installed package named "nginx"?**

✅ **Correct Answer:**  
**b)** `apt show nginx`

**Explanation:**  

The `apt show` command displays detailed information about a specific package, including:

- Package description
- Version information
- Dependencies
- Installation status
- Package size
- Maintainer information
- Download sources

This is particularly useful when you need to understand what a package does or check its dependencies before installation.

The other options are incorrect because:

- Option a) `apt list nginx` would only show basic version and installation status, not detailed information
- Option c) `apt info nginx` is not a valid apt command
- Option d) `apt query nginx` is not a valid apt command

For system administrators and SREs, understanding package information is crucial for maintaining system stability and troubleshooting dependency issues.

---

### **Question 4:**  

**On a Red Hat-based system, which command will list all installed packages?**

✅ **Correct Answer:**  
**Both b)** `yum list installed` **and c)** `rpm -qa` **are correct**

**Explanation:**  

Both commands accomplish the same goal but operate at different levels:

**`yum list installed`**:

- Uses the high-level package manager (yum)
- Presents information in a formatted way with name, version, and repository
- Groups packages by repository
- May be slower but provides more context

**`rpm -qa`**:

- Uses the low-level package management tool (rpm)
- Shows just the package names with version and release
- Outputs in an unformatted list
- Usually faster but provides less context

SREs might prefer one or the other depending on the specific task:

- Use `yum list installed` when you need to know which repository a package came from
- Use `rpm -qa` for scripting or when you need a quick, unformatted list

The other options are incorrect:

- Option a) `yum list all` would show all available packages, not just installed ones
- Option d) `rpm -l installed` is not a valid rpm command

---

### **Question 5:**  

**To extract a specific file "config.txt" from a tar archive "backup.tar", which command would you use?**

✅ **Correct Answer (fill-in-the-blank):**  

```bash
tar -xvf backup.tar config.txt
```

**Explanation:**  

This command selectively extracts only the file "config.txt" from the archive:

- `-x`: Extract files from the archive
- `-v`: Verbose mode, showing the file being extracted
- `-f`: Specify the archive filename
- `backup.tar`: The archive to extract from
- `config.txt`: The specific file to extract

This selective extraction is extremely useful in SRE work when:

- You need to restore a single configuration file from a backup
- You want to check the contents of a specific file without extracting everything
- You're recovering a critical file that was accidentally deleted

Without specifying the filename, tar would extract all contents of the archive, which could be inefficient and unnecessarily use disk space for large archives.

---

### **Question 6:**  

**Which compression utility typically achieves the highest compression ratio but takes the longest time?**

✅ **Correct Answer:**  
**xz**

**Explanation:**  

Different compression utilities offer different trade-offs between compression ratio, speed, and memory usage:

- **xz**: Provides the highest compression ratio (smallest file size) but is the slowest and most memory-intensive
- **bzip2**: Offers medium compression with medium speed
- **gzip**: Provides faster compression with good ratios
- **zip**: Often prioritizes compatibility over highest compression

This knowledge is important for SREs when:

- Backing up large amounts of data where storage costs are a concern (use xz)
- Compressing files that need to be transferred quickly (use gzip)
- Creating archives that need to be opened on multiple platforms (use zip)

For example, when backing up log files that aren't accessed frequently but need to be kept for compliance, using `tar -cJf logs_archive.tar.xz logs/` with xz compression would be ideal to minimize storage costs.

---

### **Question 7:**  

**On a Debian-based system, what's the difference between `apt remove` and `apt purge` for software removal?**

✅ **Correct Answer:**  
**`apt remove` removes the binary packages but keeps configuration files, while `apt purge` removes both the binary packages and the configuration files.**

**Explanation:**  

Understanding the difference between these commands is crucial for system management:

- **`apt remove package`**:
  - Removes the binaries and libraries of the package
  - Keeps configuration files in case you want to reinstall later
  - Preserves user data related to the package
  - Example: `apt remove nginx` removes the Nginx binaries but keeps config files in /etc/nginx/

- **`apt purge package`**:
  - Removes everything, including configuration files
  - Provides a "clean slate" if you plan to reinstall differently
  - Still preserves data in user home directories
  - Example: `apt purge nginx` removes both Nginx binaries and all configuration files

SREs should choose the appropriate command based on intent:

- Use `remove` when you might reinstall with the same configuration later
- Use `purge` when you want to completely eliminate a package without traces

Note that neither command removes dependencies that were automatically installed. For that, you would need to additionally run `apt autoremove`.

---

### **Question 8:**  

**What command would you use to check which package provides a specific file on a Red Hat-based system?**

✅ **Correct Answer:**  
**`rpm -qf /path/to/file`**

**Explanation:**  

The `rpm -qf` command (query file) identifies which installed package owns a particular file. This is extremely valuable when:

- Troubleshooting to understand which package might be causing a problem
- Determining which package to reinstall if a file is corrupted
- Learning which package provides a particular binary or library

For example:

```bash
rpm -qf /usr/sbin/nginx
```

Might return: `nginx-1.20.1-9.el8.x86_64`

For files not yet installed, you can use:

```bash
yum provides "*/filename"
```

This capability to trace files back to their source packages is essential for system troubleshooting and maintenance. When a critical file is causing issues, knowing which package owns it helps SREs quickly identify whether the problem is with package installation, configuration, or the file itself.

---

### **Question 9:**  

**Which command would create a recursive directory structure in a zip archive while maintaining file permissions?**

✅ **Correct Answer:**  
**`zip -r -p archive.zip directory/`**

**Explanation:**  

This command creates a proper recursive zip archive with preserved permissions:

- **`zip`**: The basic zip utility
- **`-r`**: Recursive option (include subdirectories)
- **`-p`**: Preserve Unix file permissions
- **`archive.zip`**: The name of the zip file to create
- **`directory/`**: The directory to zip, including all its contents

The recursive flag `-r` is essential when archiving directory structures, as without it, zip would only include files in the current directory level and ignore subdirectories.

The permissions flag `-p` is particularly important in system administration and SRE contexts, where file permissions often contain critical security settings. Without this flag, files might be extracted with default permissions rather than their original secure settings.

This command is useful when:

- Creating backups that need to be accessed on multiple platforms
- Sharing application files with precise permission requirements
- Packaging configuration directories where permissions are critical for security

Understanding these options ensures that your zip archives correctly preserve the structure and security attributes of your original files.
