# **6. Quiz Questions**

## **Beginner Level (4 Questions)**

1. Which command creates an empty file named `notes.txt`?  
   A) `mkdir notes.txt`  
   B) `touch notes.txt`  
   C) `less notes.txt`  
   D) `rm -i notes.txt`  

2. How do you view the last 5 lines of `app.log`?  
   A) `head -5 app.log`  
   B) `cat app.log 5`  
   C) `tail -n 5 app.log`  
   D) `more -d app.log`  

3. What happens if you run `rmdir mydir` when `mydir` has files inside?  
   A) `mydir` and all files are deleted  
   B) The `rmdir` command fails because the directory isn’t empty  
   C) The files are automatically moved to `/tmp`  
   D) The command partially deletes some files  

4. Which command shows the entire file contents in one go (no interactive scrolling)?  
   A) `less file.txt`  
   B) `cat file.txt`  
   C) `head file.txt`  
   D) `more file.txt`  

### **Intermediate Level (4 Questions)**

1. Which command and option combination creates the entire path `/data/projects/logs` if none of the folders exist?  
   A) `mkdir /data /data/projects /data/projects/logs`  
   B) `mkdir -p /data/projects/logs`  
   C) `mkdir -r /data/projects/logs`  
   D) `rmdir -p /data/projects/logs`  

2. If you want to copy `/etc/nginx` into `/backup/nginx` and preserve permissions, ownership, and symlinks, which flag should you use?  
   A) `cp -r /etc/nginx /backup/nginx`  
   B) `cp -p /etc/nginx /backup/nginx`  
   C) `cp -a /etc/nginx /backup/nginx`  
   D) `cp -i /etc/nginx /backup/nginx`  

3. You accidentally wrote secrets into `credentials.txt`. You must remove it without any confirmation. Which command ensures no prompt?  
   A) `rm credentials.txt`  
   B) `rm -i credentials.txt`  
   C) `rm -f credentials.txt`  
   D) `mv credentials.txt /dev/null`  

4. Which command helps you avoid overwriting an existing file?  
   A) `cp -f source.txt dest.txt`  
   B) `cp -i source.txt dest.txt`  
   C) `cp -r source.txt dest.txt`  
   D) `cp -n source.txt dest.txt` (assuming a shell that supports `-n`)  

### **SRE-Level Tier (4 Questions)**

1. During an incident, which command is most appropriate for real-time monitoring of a frequently rotated log?  
   A) `tail -f app.log`  
   B) `tail -F app.log`  
   C) `head -f app.log`  
   D) `less -N app.log`  

2. Your script renames config files atomically. Which approach is best?  
   A) `mv config.yml config.yml.bak && cp config_new.yml config.yml`  
   B) `mv config.yml config.yml.bak && mv config_new.yml config.yml`  
   C) `cp config_new.yml config.yml.bak && rm config.yml`  
   D) `tail -f config.yml && cp config_new.yml config.yml`  

3. Which command usage is best for removing large, old logs while displaying each file removed?  
   A) `rm -rf /var/log/old/`  
   B) `rm -rv /var/log/old/`  
   C) `rm -rfv /var/log/old/`  
   D) `rm -iv /var/log/old/`  

4. To avoid losing file ownership and timestamps during a directory backup, which flag should be used with `cp`?  
   A) `-a`  
   B) `-r`  
   C) `-p`  
   D) `-i`  
