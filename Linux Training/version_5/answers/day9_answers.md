# Answer sheet for Day 9

---

## 🟢 Beginner Quiz Answers

### 1. **Question**  

**True/False**: `tar` automatically compresses files by default.

**Answer**: **False**

**Explanation**:  

- **Why correct**: By default, `tar` only archives (bundles) files without compressing them. You must use additional flags (`-z` for gzip, `-j` for bzip2, etc.) or pipe the tar output through a separate compression command to actually compress.  
- **Why not “True”**: If you assume `tar` always compresses just by using it, you’ll be surprised to see the archive is often the same size as the sum of your original files unless you add compression flags.

---

### 2. **Question**  

Which command extracts `archive.zip` into the current directory?

- a) `unzip -x archive.zip`  
- b) `gunzip archive.zip`  
- c) `unzip archive.zip`

**Answer**: **c) `unzip archive.zip`**

**Explanation**:  

- **Why c) is correct**: `unzip archive.zip` is the standard syntax for extracting a `.zip` file on Linux.  
- **Why a) is not correct**: While `unzip` does support various options, `-x` in `unzip` actually excludes specific files from extraction (it doesn’t mean “extract”). Just typing `unzip -x archive.zip` without specifying the files to exclude is either meaningless or leads to unexpected behaviors.  
- **Why b) is not correct**: `gunzip` (or `gzip -d`) is meant for `.gz` files, not `.zip` files, so it would fail.

---

### 3. **Question**  

After running `gzip file.txt`, what is the resulting filename?

**Answer**: **`file.txt.gz`**

**Explanation**:  

- **Why correct**: The `gzip` command takes the original filename (`file.txt`) and appends the `.gz` extension, producing `file.txt.gz`.  
- **Why not something else**: `tar.gz` would only appear if you used `tar -czf file.tar.gz`. Likewise, `file.txt.gzip` is not the standard extension—by default, `gzip` uses `.gz`.

---

### 4. **Question**  

Which `apt` command updates the list of available packages?

**Answer**: **`sudo apt update`**

**Explanation**:  

- **Why correct**: `sudo apt update` refreshes the local package index from repositories, so your system knows which packages (and versions) are available.  
- **Why `apt install` or `apt upgrade` aren’t correct**:  
  - `apt install` is for installing a package; it doesn’t refresh the index.  
  - `apt upgrade` upgrades installed packages once the system already knows what updates are available; it also does not refresh the index by itself (unless combined with `apt update`).

---

### 5. **Question**  

**True/False**: Installing packages with `apt` requires root or sudo privileges.

**Answer**: **True**

**Explanation**:  

- **Why correct**: On most Linux distributions, installing or removing system-wide packages affects system directories (like `/usr/bin`, `/etc`) that require elevated privileges. Hence, you typically need `root` or `sudo` privileges.  
- **Why “False” is incorrect**: Without the correct privileges, you’ll see a “Permission denied” or “Are you root?” error and the installation will fail.

---

## 🟡 Intermediate Quiz Answers

### 1. **Question**  

Which `tar` flag allows you to list contents of an archive without extracting it?

**Answer**: **`-t`** (used as `tar -tvf archive.tar`)

**Explanation**:  

- **Why `-t` is correct**: `-t` stands for “table of contents.” Using `tar -tvf archive.tar` displays the files inside the archive without extraction.  
- **Why other common flags don’t do this**:  
  - `-c` creates an archive.  
  - `-x` extracts.  
  - `-z` compresses with gzip.  
  - None of these provide a listing of the contents by themselves.

---

### 2. **Question**  

How do you preserve file permissions using `tar` while creating an archive?

**Answer**: Use the **`-p`** (preserve) option, often in combination with `-c`, `-v`, `-f`, etc. (for example, `tar -cpvf archive.tar /path`).

**Explanation**:  

- **Why correct**: The `-p` flag preserves file permissions when creating or extracting an archive. Some older tar versions only preserve permissions by default when extracting as root, but `-p` ensures explicit permission retention.  
- **Why not `-v` or `-z`**:  
  - `-v` is only “verbose” output.  
  - `-z` compresses with gzip and says nothing about preserving permissions.

---

### 3. **Question**  

**Scenario**: You ran `sudo apt update`, but `sudo apt install tree` returns “Package 'tree' has no installation candidate.” Name one possible reason why.

**Answer**:  

- The repository containing `tree` is not enabled in your system. For instance, on Ubuntu, sometimes `tree` is in the “universe” repository, which might not be enabled by default.  

**Explanation**:  

- **Why correct**: If a repository isn’t included or is out of date, apt can’t locate certain packages.  
- **Why other reasons might not apply**:  
  - A simple typo or local packaging issue might also be a cause, but the question specifically hints that “no installation candidate” usually means a missing or out-of-date repo.

---

### 4. **Question**  

How do you remove dependencies no longer required by installed packages on Ubuntu?

**Answer**: **`sudo apt autoremove`**

**Explanation**:  

- **Why correct**: The `apt autoremove` command clears out orphaned dependencies that were installed automatically but are no longer needed.  
- **Why not `apt remove`**: `apt remove` uninstalls a named package but doesn’t track leftover libs or dependencies that might still exist.

---

### 5. **Question**  

**Scenario**: You have a directory of 1000 log files. Which `gzip` flag will compress them **recursively**?

**Answer**: **`-r`**

**Explanation**:  

- **Why correct**: The `-r` option tells `gzip` to traverse directories and compress all matching files within them.  
- **Why not `-d`**: That decompresses.  
- **Why not `-k`**: That keeps the original file but doesn’t handle recursion.  
- **Why not `-9`**: That’s just a higher compression level, not recursion.

---

## 🔴 SRE-Level Quiz Answers

### 1. **Question**  

**Scenario**: Your monitoring shows CPU spikes at 3 AM every day. You discover a scheduled job uses `tar -czf /backups/production.tar.gz /var/www`. Suggest two performance-related solutions.

**Answer**:  

1. **Throttle or Nice the compression job**: Use `nice` or `ionice` to lower the priority and reduce resource contention, e.g.  

   ```bash
   ionice -c3 nice -n19 tar -czf /backups/production.tar.gz /var/www
   ```  

2. **Split or schedule the job off-peak**: Instead of one massive archive at 3 AM, break it into smaller partial archives, or run it at a time of lower traffic, or even spread it out over multiple increments.

**Explanation**:  

- **Why correct**: Both solutions aim to reduce the system load during peak hours or minimize the CPU usage for compression tasks.  
- **Why alternatives might be less effective**:  
  - Simply ignoring or force-killing the job leaves you without a backup.  
  - Doing the same job earlier might conflict with other scheduled tasks. You need specific solutions that lower impact or shift timing.

---

### 2. **Question**  

Name one method to replicate a package environment across multiple Debian-based servers.

**Answer**:  

- **Using `dpkg --get-selections` and `dpkg --set-selections`**. For example:  

  ```bash
  dpkg --get-selections > pkg_list.txt
  # On the target server:
  dpkg --set-selections < pkg_list.txt
  apt-get dselect-upgrade
  ```

**Explanation**:  

- **Why correct**: This approach copies exact package selections from one server to another.  
- **Why alternatives might differ**:  
  - You could also script with Ansible or Chef, but that’s more elaborate. The question specifically wants a known Debian-based trick for replicating environment states.

---

### 3. **Question**  

**Scenario**: You used zip with the **default** encryption on a log archive containing sensitive data. Is this sufficiently secure for highly confidential information? Why or why not?

**Answer**:  

- **No**, it is **not** sufficiently secure. Default zip encryption is relatively weak and can be cracked with moderate effort.

**Explanation**:  

- **Why correct**: Traditional “ZipCrypto” encryption is outdated and easily brute-forced. If you must use zip, choose AES encryption (when supported) or another stronger encryption method entirely.  
- **Why saying “Yes” is incorrect**: The default encryption is known to be vulnerable and not recommended for high-security data.

---

### 4. **Question**  

How would you automate partial extraction of only config files from a massive `.tar.gz`?

**Answer**:  

- Use `tar` with explicit filenames or wildcard patterns after the archive name, for example:  

  ```bash
  tar -xzvf huge_archive.tar.gz etc/myapp/*.conf -C /tmp/config_restore
  ```

  This only extracts `.conf` files for “myapp.”

**Explanation**:  

- **Why correct**: By specifying the partial path to the files you want, `tar` only extracts those files without decompressing everything.  
- **Why other approaches**: You could manually extract everything and remove the unneeded files, but that wastes CPU, I/O, and time.

---

### 5. **Question**  

**Scenario**: On a RHEL system, you need to patch critical vulnerabilities but `yum update` is failing due to repo connectivity issues. Outline the steps to troubleshoot.

**Answer** (example outline):  

1. **Check Internet Connectivity**: `ping google.com` or `curl -I https://repo-url`  
2. **Examine Repo Config**: Look in `/etc/yum.repos.d/` for correct base URLs.  
3. **Clean & Rebuild Cache**: `sudo yum clean all && sudo yum makecache`  
4. **Try a Different Mirror**: Adjust the `baseurl` or enable different repositories if the default is down.  
5. **Check Firewall/Proxy**: Confirm no internal firewall is blocking your repo domain.

**Explanation**:  

- **Why correct**: These steps systematically address the typical root causes of “repo connectivity issues”—DNS problems, invalid repo config, or local network restrictions.  
- **Why ignoring the problem**: Doesn’t solve the patching requirement.  
- **Why re-running `yum update` repeatedly**: May not fix underlying connectivity or config issues.

---

### Additional Notes on Scenario/Open-Ended Questions

For the scenario-based questions (especially in the SRE tier), there aren’t multiple-choice options. Instead, the correct “answers” revolve around how well you identify best practices and relevant commands. The key is to demonstrate knowledge of the relevant tools and strategies rather than picking from a list of predefined options.

---

## Final Remarks

- **Focus on Correct vs. Incorrect**: Where multiple-choice was provided (Beginner/Intermediate), we explained why the chosen answer is correct and why the others are not.  
- **Scenario/Open-Ended**: For SRE-level questions, correctness is judged on how closely your answer aligns with established best practices and real-world reliability considerations.  

Use these explanations to reinforce your understanding of why certain commands and approaches work best in given contexts.
