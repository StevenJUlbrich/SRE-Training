# Day 9 Answser Sheet

## 🟢 6.1 Beginner Quiz Answers

1. **True/False**: `tar` alone compresses files without extra flags.  
   **Answer**: **False**  
   **Explanation**: By default, `tar` only archives (packages multiple files into one) but does **not** compress unless you use additional flags like `-z` (gzip) or `-j` (bzip2).

2. Which command extracts files from a zip archive called `archive.zip`?  
   - a) `tar -xvf archive.zip`  
   - b) `gzip -d archive.zip`  
   - c) **`unzip archive.zip`**  
   **Answer**: **c) `unzip archive.zip`**  
   **Explanation**: The `unzip` utility is specifically designed to extract `.zip` files. `tar` and `gzip` handle `.tar` or `.tar.gz`, but not standard `.zip` archives.

3. What happens to `file.txt` when you run `gzip file.txt`?  
   **Answer**: The original `file.txt` is replaced by a compressed file called `file.txt.gz`.  
   **Explanation**: By default, `gzip` removes the original file after creating the compressed version. If you want to keep the original file, you must use the `-k` (keep) flag.

4. Which `apt` command updates the local package index?  
   **Answer**: `sudo apt update`  
   **Explanation**: This command retrieves the latest package lists from the repositories. Without it, the system won’t know about newly available packages or updates.

5. **True/False**: `apt install` can be run successfully without `sudo` on most systems.  
   **Answer**: **False**  
   **Explanation**: Installing or removing system packages typically requires superuser (root) privileges. Hence, you must prefix commands with `sudo` or switch to the root user.

---

## 🟡 6.2 Intermediate Quiz Answers

1. Which `tar` flag lists the contents of an archive without extracting?  
   **Answer**: `-t`  
   **Explanation**: `tar -tvf archive.tar` (or `tar -tzf archive.tar.gz` for gzip-compressed archives) displays the archive’s contents without performing an extraction.

2. How do you remove packages automatically installed as dependencies but no longer needed on Debian/Ubuntu?  
   **Answer**: `sudo apt autoremove`  
   **Explanation**: This command scans for “orphaned” packages (installed only to satisfy dependencies) that are no longer required and removes them to free up space.

3. **Scenario**: You ran `sudo apt update`, but `sudo apt install tree` reports “Package ‘tree’ has no installation candidate.” Give one likely cause.  
   **Possible Answers**:  
   - The repositories that contain the `tree` package are not enabled or missing.  
   - The distribution’s package sources may be out-of-date or pointing to an unsupported release.  
   - A typo or mismatch in package naming.  
   **Explanation**: If a package has “no installation candidate,” it often means the package manager cannot find it in the active sources. Checking repository configuration and ensuring the package name is correct typically resolves the issue.

4. Which gzip option keeps the original file after compression?  
   **Answer**: `-k`  
   **Explanation**: By default, `gzip` deletes the original file once compression is complete. The `-k` (keep) flag prevents this deletion.

5. **Scenario**: You have a directory of 1,000 log files that must be compressed individually. Which gzip flag do you use to compress an entire directory structure?  
   **Answer**: `-r` (recursive)  
   **Explanation**: `gzip -r /path/to/logs` compresses all files within the specified directory (and subdirectories). Each file is individually compressed into its own `.gz` counterpart.

---

## 🔴 6.3 SRE-Level Quiz Answers

1. Your monitoring system reports CPU spikes each night at 2 AM due to a tar+gzip backup job. Suggest two performance-conscious strategies.  
   **Sample Answers**:  
   - **Schedule Off-Peak or Throttle**: Use `nice` or `ionice` to lower the priority of the compression job. This way, the backup process won’t compete aggressively with critical services.  
   - **Split or Incremental Archives**: Compress smaller sets of files more frequently to avoid a massive one-time spike.  
   - **Use Faster Compression Settings**: For instance, `gzip -1` might be less CPU-intensive if the highest compression ratio is not critical.  
   **Explanation**: Lowering CPU priority, distributing backup tasks, or changing compression strategies can reduce resource contention.

2. How would you replicate a Red Hat server’s packages onto a new system without direct internet access?  
   **Possible Answers**:  
   - Use `yumdownloader --resolve package-name` on a connected system to download RPMs (including dependencies). Then transfer those `.rpm` files to the offline server.  
   - Set up a local repository via `createrepo /path/to/rpms` and configure `/etc/yum.repos.d/local.repo` on the offline server to point to that path. Then `yum install local-package.rpm`.  
   **Explanation**: Copying the RPM files or creating a local mirror allows installations on an air-gapped system.

3. Is basic `zip -e` encryption sufficient for extremely sensitive data? Why or why not?  
   **Answer**: **No**  
   **Explanation**: Basic zip encryption is relatively weak and can be brute-forced or exploited with known vulnerabilities. For high-security requirements, stronger encryption tools (e.g., GPG, AES-256) or more robust zip/encryption implementations are recommended.

4. You need to partially restore only `/etc/nginx/nginx.conf` from a multi-GB tar.gz archive. Which `tar` options accomplish that?  
   **Answer**:  
   - `tar -xzvf backup.tar.gz etc/nginx/nginx.conf -C /restore_location`  
   - Possibly use `--strip-components` if the paths inside the archive differ.  
   **Explanation**: You can specify the exact path to extract and optionally direct it to a different folder with `-C`. `--strip-components` helps remove parent directory layers if needed.

5. Yum updates keep failing due to a repository connectivity issue. Name two troubleshooting steps.  
   **Sample Answers**:  
   - **Check Network and Mirror**: Confirm you can reach the repository host via `ping` or `curl`. Switch to a different mirror if the primary one is down.  
   - **Clean and Rebuild Metadata**: `sudo yum clean all` followed by `sudo yum makecache` can fix local corruption.  
   - **Inspect Repo Config**: Look for typos or invalid URLs in `/etc/yum.repos.d/`.  
   **Explanation**: Often, these issues stem from misconfigurations or mirror downtime. Checking connectivity, clearing caches, and validating `.repo` files are standard steps.
