# 6. 📝 Quiz Questions

### 6.1 🟢 Beginner Quiz

1. True/False: `tar` alone compresses files without extra flags.
2. Which command extracts files from a zip archive called `archive.zip`?
   - a) `tar -xvf archive.zip`
   - b) `gzip -d archive.zip`
   - c) `unzip archive.zip`
3. What happens to `file.txt` when you run `gzip file.txt`?
4. Which `apt` command updates the local package index?
5. True/False: `apt install` can be run successfully without `sudo` on most systems.

### 6.2 🟡 Intermediate Quiz

1. Which `tar` flag lists the contents of an archive without extracting?
2. How do you remove packages automatically installed as dependencies but no longer needed on Debian/Ubuntu?
3. Scenario: You ran `sudo apt update`, but `sudo apt install tree` reports "Package 'tree' has no installation candidate." Give one likely cause.
4. Which gzip option keeps the original file after compression?
5. Scenario: You have a directory of 1,000 log files that must be compressed individually. Which gzip flag do you use to compress an entire directory structure?

### 6.3 🔴 SRE-Level Quiz

1. Your monitoring system reports CPU spikes each night at 2 AM due to a tar+gzip backup job. Suggest two performance-conscious strategies.
2. How would you replicate a Red Hat server’s packages onto a new system without direct internet access?
3. Is basic `zip -e` encryption sufficient for extremely sensitive data? Why or why not?
4. You need to partially restore only `/etc/nginx/nginx.conf` from a multi-GB tar.gz archive. Which `tar` options accomplish that?
5. Yum updates keep failing due to a repository connectivity issue. Name two troubleshooting steps.
