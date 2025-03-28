# ✅ **Day 3 Quiz - Answer Key with Explanations**

## **Answers to Today's Quiz**

### **1. An SRE notices that an application is failing with "Permission denied" errors when trying to write to its log file. The application runs as user `appuser`. What command would fix this issue?**

**Correct Answer:** c) `sudo chown appuser /var/log/app.log`

**Explanation:**
- The core issue is that the application (running as `appuser`) doesn't own the log file
- Changing ownership to `appuser` allows the application to write to its log
- Option a) `chmod 777` would be a severe security risk (anyone could write to logs)
- Option b) `chmod 644` would only provide read permissions, not write
- Option d) `chmod +r` only adds read permission, not write permission needed for logging

**SRE Application:** This scenario is extremely common in production troubleshooting. Applications often fail after deployment or system updates because of permission issues. Always check ownership first, especially when applications run as non-root users.

### **2. You need to set permissions on a critical configuration file so that the owner has read and write access, while the group and others have only read access. Which command would you use?**

**Correct Answer:** `chmod 644 /etc/application/config.conf`

**Explanation:**
- `6` (4+2+0) for owner: read (4) + write (2) permissions
- `4` for group: read-only permissions
- `4` for others: read-only permissions
- The resulting permission is `rw-r--r--`

**SRE Application:** This is the standard permission pattern for configuration files - allowing the owner (often root) to modify the file while ensuring services can read the configuration.

### **3. Which permission setting allows the owner to read, write, and execute, the group to read and execute, and gives no permissions to others?**

**Correct Answer:** b) `chmod 750 script.sh`

**Explanation:**
- `7` (4+2+1) for owner: read, write, execute
- `5` (4+0+1) for group: read and execute
- `0` (0+0+0) for others: no permissions
- The resulting permission is `rwxr-x---`

**SRE Application:** This permission pattern is common for scripts that should only be executable by the owner and members of a specific group (like a team of SREs) but not by other users on the system.

### **4. A junior SRE has accidentally changed permissions on the `/etc` directory. What is the correct command to recursively restore default permissions (755 for directories, 644 for files) without compromising security?**

**Correct Answer:** c) (This requires a more complex approach, not a single command)

**Explanation:**
- Option a) `chmod -R 777 /etc` would make everything world-writable (severely insecure)
- Option b) `chmod -R 755 /etc` would incorrectly make all files executable
- Option d) `chmod -R 644 /etc` would make directories inaccessible (not executable)
- The correct approach requires separate commands for files and directories:
  ```bash
  find /etc -type f -exec chmod 644 {} \;
  find /etc -type d -exec chmod 755 {} \;
  ```

**SRE Application:** This highlights the importance of understanding how to apply different permissions to files versus directories. In production systems, using a single recursive chmod command can cause widespread issues.

### **5. During a security audit, you need to identify files with the setuid bit set. Which command would you use?**

**Correct Answer:** a) `find / -type f -perm -4000 -ls`

**Explanation:**
- `-type f` limits to regular files
- `-perm -4000` searches for the setuid bit (4000 in octal)
- `-ls` provides detailed listing of matching files
- Option b) would only check files in the root directory and might miss setuid binaries
- Options c) and d) don't search for setuid files at all

**SRE Application:** Setuid files are a potential security risk as they execute with the owner's permissions rather than the executing user's. Regular security audits should identify and validate all setuid files on the system.

## **SRE Application: Permission Strategy**

These permissions and ownership concepts are fundamental to SRE work for several reasons:

1. **Security Defense-in-Depth**: Proper permissions form a crucial layer in security. Even if other security measures are breached, proper permissions can limit the blast radius of an attack.

2. **Service Isolation**: In multi-service environments, permissions ensure one service cannot interfere with another's files, logs, or configurations.

3. **Automated Deployments**: Modern CI/CD pipelines need to correctly set permissions when deploying applications, making this knowledge essential for automation.

4. **Troubleshooting Efficiency**: Permission issues are among the most common causes of application failures after deployment. Quickly identifying and resolving permission problems reduces incident duration.

5. **Regulatory Compliance**: Many compliance standards (PCI-DSS, HIPAA, etc.) have specific requirements around file permissions that SREs must implement and maintain.

Understanding Linux permissions isn't just about running commands - it's about designing secure, reliable systems that operate efficiently even in complex, multi-user, multi-service environments.
