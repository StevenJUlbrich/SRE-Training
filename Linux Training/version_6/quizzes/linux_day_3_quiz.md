
# 📝 **Quiz Questions**

## **Beginner Tier (3–4 Questions)**

1. Which numeric permission grants the owner read and write, group read, and others read?
   - A) 644  
   - B) 755  
   - C) 600
2. In `-rwxr-xr--`, which permissions does the group have?
   - A) Read and write  
   - B) Read and execute  
   - C) Read only
3. True/False: `chmod +x script.sh` sets execute permission for all users.
4. To change the owner of `example.txt` to `alice`, which command is correct?
   - A) `chown alice example.txt`  
   - B) `chmod alice example.txt`  
   - C) `sudo chgrp alice example.txt`

### **Intermediate Tier (3–4 Questions)**

1. Which command recursively sets a directory’s permissions to `770`?
   - A) `chmod 770 directory/`  
   - B) `chmod -R 770 directory/`  
   - C) `chown -R 770 directory/`
2. A file has permissions `-rw-r--r--`. Which command makes it so only the owner can read/write it, with no access for group or others?
   - A) `chmod 640 file`  
   - B) `chmod 600 file`  
   - C) `chmod 700 file`
3. True/False: Using `chown :developers file.txt` changes the owner to `developers`.
4. Match the numeric notation:
   - 700 → `rwx------`
   - 755 → `rwxr-xr-x`
   - 666 → `rw-rw-rw-`

### **SRE-Level Tier (3–4 Questions)**

1. Why is a setuid binary risky?
2. You see `-rwsr-xr-x` on `/usr/bin/passwd`. What does the `s` indicate?
   - A) Sticky bit  
   - B) setuid bit  
   - C) The owner can’t execute
3. True/False: SELinux or AppArmor can override traditional file permissions.
4. Which command best helps confirm a file’s permission bits and extended attributes?
   - A) `ls -lh /path/file`  
   - B) `stat /path/file`  
   - C) `cat /path/file`
