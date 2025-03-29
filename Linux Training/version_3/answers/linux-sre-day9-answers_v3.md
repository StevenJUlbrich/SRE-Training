# ✅ Day 9 Quiz: Archiving, Compression & Package Management - Answer Key with Explanations

## Beginner Level Questions

### **1. Which command creates a compressed tar archive named `backup.tar.gz` from a directory called `documents`?**

**Correct Answer: a) `tar -czf backup.tar.gz documents`**

**Explanation:**  
The `tar` command with these specific options creates a compressed archive:

- `-c`: Create a new archive
- `-z`: Compress the archive using gzip
- `-f`: Specify the filename of the archive (must be followed by the actual filename)
- `backup.tar.gz`: The name for the compressed archive
- `documents`: The directory to be archived

Option b) uses `-x` which is for extraction, not creation. Option c) is missing the required options. Option d) attempts to use `gzip` directly, which doesn't preserve the directory structure properly.

### **2. What command extracts files from a zip archive called `archive.zip`?**

**Correct Answer: c) `unzip archive.zip`**

**Explanation:**  
The `unzip` command is specifically designed to extract files from zip archives. It's the correct tool to use with `.zip` files.

Option a) `gzip archive.zip` would attempt to compress the already compressed zip file, not extract it.
Option b) `tar -xvf archive.zip` is incorrect because `tar` doesn't handle zip files directly without additional plugins or flags.

### **3. Which command would you use to update the package lists on a Debian/Ubuntu system?**

**Correct Answer: a) `sudo apt update`**

**Explanation:**  
The `apt update` command refreshes the local package index with the latest information from the configured repositories. This is always the first step before installing or upgrading packages on Debian/Ubuntu systems.

Option b) `sudo apt upgrade` performs the actual upgrade of installed packages but doesn't update the package lists.
Option c) `sudo apt install` is used for installing specific packages.
Option d) `sudo apt search` is used for searching available packages.

### **4. On a Debian/Ubuntu system, what command installs a new package?**

**Correct Answer: b) `sudo apt install package-name`**

**Explanation:**  
The `apt install` command is used to install packages on Debian/Ubuntu systems. The command needs root privileges (via `sudo`) and follows the pattern `apt install` followed by the package name(s) to install.

Option a) `sudo apt get package-name` is incorrect syntax.
Option c) `sudo apt update package-name` is used for updating package lists, not installing packages.
Option d) `sudo apt-get package-name` is missing the `install` action.

### **5. What happens when you run the command `gzip data.txt`?**

**Correct Answer: b) It replaces data.txt with a compressed file named data.txt.gz**

**Explanation:**  
By default, `gzip` compresses the specified file and replaces it with a compressed version, adding the `.gz` extension. The original file is removed after successful compression.

Option a) is incorrect because `gzip` doesn't keep both files by default (you need the `-k` flag to keep the original).
Option c) is incorrect because `gzip` compresses files, while extraction is done with `gunzip`.
Option d) is incorrect because `gzip` preserves the original filename and adds `.gz` as extension, not replacing the extension entirely.

## Intermediate Level Questions

### **1. Which option would you add to the `tar` command to view the contents of an archive without extracting it?**

**Correct Answer: d) `-t`**

**Explanation:**  
The `-t` (or `--list`) option tells `tar` to list the contents of an archive without extracting it. This is useful for seeing what's inside an archive before deciding whether to extract it.

Option a) `-c` is for creating archives.
Option b) `-x` is for extracting archives.
Option c) `-v` is for verbose output (showing file names), but doesn't list archive contents on its own.

### **2. On a Red Hat-based system, which command will list all installed packages?**

**Correct Answer: c) `rpm -qa`**

**Explanation:**  
The `rpm -qa` command lists all installed packages on a Red Hat-based system:

- `rpm` is the package manager
- `-q` specifies a query operation
- `-a` means "all packages"

Option a) `yum list all` would list all available packages, not just installed ones.
Option b) `yum list installed` would also work but is not one of the options.
Option d) `rpm -l installed` is incorrect syntax for rpm.

### **3. When running `tar -xf archive.tar somefile`, what does it do?**

**Correct Answer: b) Extracts only the file named "somefile"**

**Explanation:**  
When you specify filenames after the archive name in a `tar` extraction command, `tar` will only extract those specific files from the archive rather than the entire archive contents.

Option a) is incorrect because the command is not extracting the entire archive.
Option c) is incorrect because the `-x` flag specifies extraction, not creation.
Option d) is incorrect because the command extracts the file, not just tests for its existence.

### **4. What does the command `apt autoremove` do?**

**Correct Answer: b) Removes packages that were automatically installed as dependencies but are no longer needed**

**Explanation:**  
The `apt autoremove` command identifies and removes packages that were installed automatically as dependencies for other packages, but are no longer needed because those other packages have been removed.

Option a) is incorrect because it doesn't remove all packages.
Option c) is incorrect because it doesn't reinstall broken packages.
Option d) is incorrect because it doesn't specifically target duplicate packages.

### **5. Which command would preserve the original file when compressing with gzip?**

**Correct Answer: b) `gzip -k file.txt`**

**Explanation:**  
The `-k` (or `--keep`) option tells `gzip` to keep the original file rather than deleting it after compression. This results in both the original file and the compressed `.gz` file being present after compression.

Option a) `-p` is not a valid option for `gzip`.
Option c) `-o` is not used for preserving the original file.
Option d) `-s` is not a valid option for preserving files in `gzip`.

## SRE Application Questions

### **1. You need to backup a web application with proper permissions before a major update. Which tar command options would be most appropriate?**

**Correct Answer: c) `tar -czpf backup.tar.gz /var/www/app`**

**Explanation:**  
The correct options for preserving permissions during backups are:

- `-c`: Create a new archive
- `-z`: Compress the archive using gzip
- `-p`: Preserve permissions, ownership, and timestamps
- `-f`: Specify the filename

The `-p` flag is crucial here as it ensures all file permissions, ownership, and timestamp information are preserved in the archive, which is essential for correctly restoring web applications where file permissions often matter for security and functionality.

Options a) and b) are missing the critical `-p` flag.
Option d) uses `-x` for extraction rather than creation.

### **2. You discover a critical package has a security vulnerability. What is the proper sequence to update just this package?**

**Correct Answer: b) `apt update && apt install --only-upgrade package-name`**

**Explanation:**  
The correct procedure for updating a single package with security issues is:

1. `apt update` - First refresh the package repository information
2. `apt install --only-upgrade package-name` - Then upgrade just that specific package

This sequence ensures you have the latest information about available package versions before attempting to upgrade only the vulnerable package without affecting other packages.

Option a) would install the package if not present but might not upgrade an existing installation.
Option c) has incorrect syntax; `apt upgrade` doesn't accept single package names.
Option d) is incorrect as `dpkg -i` requires a local package file, not a package name.

### **3. During a system audit, you need to find out which package installed the file `/usr/bin/nginx`. Which command would you use on a Red Hat-based system?**

**Correct Answer: a) `rpm -qf /usr/bin/nginx`**

**Explanation:**  
The `rpm -qf` command queries the package database to find which package owns a specific file:

- `-q` specifies a query operation
- `-f` means "find the package that owns this file"

This is the exact command needed to determine which package installed a specific file on a Red Hat-based system.

Option b) would only find packages with "nginx" in their name.
Option c) has incorrect syntax; `yum provides` needs a pattern, not an existing path.
Option d) is incorrect as `yum info` provides information about a package, not which package owns a file.

### **4. You need to create an encrypted archive of sensitive configuration files to transfer to another server. Which command would you use?**

**Correct Answer: b) `zip -e -r configs.zip /etc/app/`**

**Explanation:**  
The `zip` command with these options creates an encrypted archive:

- `-e`: Encrypt the archive (prompts for password)
- `-r`: Recursively include all files and subdirectories
- `configs.zip`: The name for the encrypted archive
- `/etc/app/`: The directory containing configuration files to archive

This is the only option that provides encryption, which is crucial when transferring sensitive configuration files.

Option a) uses `tar` without encryption.
Option c) is incorrect as `tar` doesn't have a built-in `--encrypt` option.
Option d) is incorrect as `gzip` doesn't provide encryption.

### **5. You need to examine what filesystem changes a package made during installation. Which approach is most effective?**

**Correct Answer: b) Use `dpkg -L package-name` or `rpm -ql package-name`**

**Explanation:**  
These commands list all files installed by a package:

- `dpkg -L package-name` (Debian/Ubuntu)
- `rpm -ql package-name` (RHEL/CentOS)

This approach is most effective because it shows exactly which files were placed on the filesystem by that specific package, allowing you to see all changes made during installation.

Option a) might provide some information but often doesn't detail exactly what files were installed.
Option c) would be extremely time-consuming and impractical.
Option d) wouldn't provide reliable information about already installed packages.
