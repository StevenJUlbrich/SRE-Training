# Day 4: Luis's Process Hunt

*09:00 CET - Madrid, Spain*

Luis arrived at CloudCrest's Madrid office, a converted historic building that blended old-world charm with modern tech aesthetics. Warm morning light filtered through the tall windows, illuminating exposed brick walls adorned with minimalist art.

He settled at his desk and pulled up Aanya's handoff message:

> **@Luis:** I've tackled the issues Noah and Taylor identified. The analytics upload system now has:
> 
> 1. Proper directory structure with clear separation: incoming → processing → archive
> 2. Correct permissions and ownership for each service
> 3. Automated log rotation configured
> 4. A daily maintenance script that fixes permissions and moves stuck files
> 
> The immediate issues are resolved, but please monitor for any new permission errors. I've left detailed notes in `/var/app/uploads/README.md`.
> 
> Also, I noticed some unusual process forking in the analytics service logs that might explain the user permission inconsistencies. Might be worth investigating if these services are spawning child processes with different users.

"Vamos a ver," Luis muttered, sipping his cortado. He'd been with CloudCrest for three years and had a knack for tracking down mysterious process behavior. This sounded right up his alley.

He connected to the analytics server:

```bash
$ ssh luis@analytics-prod-03
```

First, Luis wanted to see Aanya's work:

```bash
$ cd /var/app/uploads
$ cat README.md
```

The README was detailed and clear. Aanya had done an excellent job organizing the directory structure and fixing permissions. Next, Luis checked the current state of the system:

```bash
$ ps aux | grep analytics
```

The output showed several analytics-related processes running:

```
analytics  3456  0.2  0.5  128916  18204 ?    Ss   02:00   0:12 /usr/bin/analytics-service
analytics  3465  0.1  0.4  126584  16328 ?    S    02:00   0:07 /usr/bin/analytics-processor
root       3471  0.0  0.3  102384  12104 ?    S    02:00   0:02 /usr/bin/analytics-archiver
www-data   4512  0.1  0.3  108472  11260 ?    S    02:15   0:03 /usr/bin/analytics-upload-handler
```

This matched what Aanya had described: multiple services running as different users. But to investigate the potential forking issue, Luis needed to look at the process relationships.

```bash
$ ps -ef f | grep analytics
```

The `-f` format would show the PPID (parent process ID), and the extra `f` flag would display the processes in a hierarchical format:

```
analytics  3456     1  0 02:00 ?    Ss   /usr/bin/analytics-service
analytics  3465  3456  0 02:00 ?    S    \_ /usr/bin/analytics-processor
analytics  5512  3465  0 03:10 ?    S        \_ /bin/bash /opt/analytics/scripts/process_batch.sh
root       5513  5512  0 03:10 ?    S            \_ /bin/mv /var/app/uploads/processing/batch_45.csv /var/app/uploads/archive/
root       3471     1  0 02:00 ?    S    /usr/bin/analytics-archiver
www-data   4512     1  0 02:15 ?    S    /usr/bin/analytics-upload-handler
www-data   5678  4512  0 09:05 ?    S    \_ /bin/cp /tmp/upload_59.csv /var/app/uploads/incoming/
```

"Aha!" Luis exclaimed. There was the smoking gun. The analytics-processor was spawning bash scripts that ran as the same user, but those scripts were executing commands like `mv` that ran as root. Similarly, the upload handler was launching `cp` commands to move files.

To confirm his findings, Luis needed to check what those scripts were doing:

```bash
$ cat /opt/analytics/scripts/process_batch.sh
```

The script revealed the issue:

```bash
#!/bin/bash
# Process analytics batch files

# Get batch ID from args
BATCH_ID=$1

if [ -z "$BATCH_ID" ]; then
    echo "Error: Batch ID required"
    exit 1
fi

# Process the batch file
echo "Processing batch: $BATCH_ID"

# Move to archive when done - using sudo to avoid permission issues
sudo mv /var/app/uploads/processing/batch_$BATCH_ID.csv /var/app/uploads/archive/

echo "Batch $BATCH_ID processed and archived"
exit 0
```

The script was using `sudo` without any restrictions, which explained why some operations were running as root. This was a significant security issue.

Luis continued his investigation, looking for other scripts:

```bash
$ find /opt/analytics -name "*.sh" -type f
```

He found several more scripts, including:

```
/opt/analytics/scripts/process_batch.sh
/opt/analytics/scripts/handle_upload.sh
/opt/analytics/scripts/cleanup.sh
/opt/analytics/scripts/archive_old.sh
```

He examined each one and found similar patterns—unrestricted sudo usage or direct calls to move files without proper permissions handling.

Luis also checked the sudo configuration:

```bash
$ sudo cat /etc/sudoers.d/analytics
```

Which showed:

```
# Allow analytics users to run specific commands
analytics ALL=(ALL) NOPASSWD: ALL
www-data ALL=(ALL) NOPASSWD: /bin/cp, /bin/mv
```

This was extremely permissive, essentially giving these service accounts unlimited sudo privileges—a security nightmare.

To understand how this affected file ownership, Luis ran a command to show recent file operations:

```bash
$ sudo ausearch -f /var/app/uploads -i | tail -20
```

The output confirmed his suspicions—numerous file operations with mismatched user contexts.

Luis decided to address this problem systematically. First, he created a backup of the existing sudoers configuration:

```bash
$ sudo cp /etc/sudoers.d/analytics /etc/sudoers.d/analytics.bak
```

Then he drafted a more restricted configuration:

```bash
$ sudo vim /etc/sudoers.d/analytics
```

Modified to:

```
# Restricted permissions for analytics users
analytics ALL=(root) NOPASSWD: /bin/mv /var/app/uploads/processing/* /var/app/uploads/archive/*
www-data ALL=(root) NOPASSWD: /bin/cp /tmp/* /var/app/uploads/incoming/*
```

This would limit sudo privileges to only the specific paths needed.

Next, Luis turned his attention to fixing the scripts. He edited each one to remove unnecessary sudo calls where Aanya's directory permission changes had already solved the issue:

```bash
$ sudo vim /opt/analytics/scripts/process_batch.sh
```

Changed to:

```bash
#!/bin/bash
# Process analytics batch files - UPDATED BY LUIS

# Get batch ID from args
BATCH_ID=$1

if [ -z "$BATCH_ID" ]; then
    echo "Error: Batch ID required"
    exit 1
fi

# Process the batch file
echo "Processing batch: $BATCH_ID"

# With proper directory permissions, we can move files directly
# No sudo needed since both directories are owned by analytics:analytics
mv /var/app/uploads/processing/batch_$BATCH_ID.csv /var/app/uploads/archive/

echo "Batch $BATCH_ID processed and archived"
exit 0
```

He repeated this process for each script, removing unnecessary sudo calls and using the proper directory permissions that Aanya had established.

To further monitor process behavior, Luis set up process auditing:

```bash
$ sudo auditctl -w /opt/analytics/scripts/ -p x -k analytics-scripts
```

This would log any execution of scripts in the analytics directory.

After making these changes, Luis needed to test them. Rather than restarting the services immediately, he set up a monitoring terminal:

```bash
$ watch -n 1 "ps -ef f | grep analytics"
```

In another terminal, he triggered a test upload:

```bash
$ sudo -u www-data /opt/analytics/scripts/handle_upload.sh test_upload
```

The process hierarchies appeared correct, with no unexpected privilege escalations. Next, he checked file ownership in the directories:

```bash
$ ls -la /var/app/uploads/incoming/
$ ls -la /var/app/uploads/processing/
$ ls -la /var/app/uploads/archive/
```

All files had the expected ownership and permissions based on Aanya's directory structure.

Satisfied with his tests, Luis proceeded to restart the services:

```bash
$ sudo systemctl restart analytics-upload-service
$ sudo systemctl restart analytics-processing-service
$ sudo systemctl restart analytics-archiver-service
```

He monitored the logs for any errors:

```bash
$ tail -f /var/log/analytics*.log
```

Everything looked good—no permission errors or unexpected behavior.

To ensure these changes wouldn't be reverted, Luis added a comment to Aanya's README.md file:

```bash
$ sudo vim /var/app/uploads/README.md
```

He added:

```
## Process Management
- Services should NOT use unrestricted sudo
- Scripts should rely on proper directory permissions instead of privilege escalation
- Process hierarchy has been fixed to maintain consistent user contexts
- Sudo privileges have been restricted to specific paths only

Last updated: [date] by Luis
```

For additional security, Luis created a script to monitor for any unauthorized sudo usage:

```bash
$ vim /home/luis/scripts/monitor_sudo_usage.sh
```

```bash
#!/bin/bash
# monitor_sudo_usage.sh - Created by Luis
# Monitors for unauthorized sudo usage in analytics processes

LOG_FILE="/var/log/analytics_security.log"

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

log "Starting sudo usage monitoring"

# Monitor sudo logs for analytics users
sudo ausearch -m USER_CMD -i | grep -E 'analytics|www-data' | grep -v "cmd=/bin/mv\|cmd=/bin/cp" > /tmp/sudo_violations.tmp

if [ -s /tmp/sudo_violations.tmp ]; then
    log "WARNING: Unauthorized sudo usage detected:"
    cat /tmp/sudo_violations.tmp >> "$LOG_FILE"
    
    # Send alert
    mail -s "CloudCrest: Unauthorized sudo usage detected" sre-team@cloudcrest.example < /tmp/sudo_violations.tmp
fi

# Clean up
rm /tmp/sudo_violations.tmp

log "Sudo monitoring completed"
```

He made it executable and added it to the crontab to run hourly:

```bash
$ chmod +x /home/luis/scripts/monitor_sudo_usage.sh
$ sudo crontab -e
```

Added:

```
0 * * * * /home/luis/scripts/monitor_sudo_usage.sh
```

As a final safety measure, Luis set up process limits for the analytics services to prevent excessive forking:

```bash
$ sudo vim /etc/systemd/system/analytics-service.service
```

Added:

```
[Service]
...
LimitNPROC=100
```

He repeated this for each analytics service unit file.

With all changes in place, Luis conducted one more round of testing and monitoring to ensure everything was functioning correctly under load. He used a stress test script to simulate multiple uploads:

```bash
$ for i in {1..20}; do
    sudo -u www-data /opt/analytics/scripts/handle_upload.sh test_$i &
done
```

He monitored the processes and file operations:

```bash
$ watch -n 1 "ps -ef f | grep analytics"
$ watch -n 1 "ls -la /var/app/uploads/{incoming,processing,archive}"
```

All twenty test files moved correctly through the pipeline with proper ownership and permissions. The system was now functioning securely and efficiently.

As his workday drew to a close, Luis prepared a handoff for Jin in South Korea:

> **@Jin:** I've addressed the process forking issues Aanya mentioned. The analytics services were using unrestricted sudo privileges, causing the permission inconsistencies. Changes made:
> 
> 1. Restricted sudo permissions to only the necessary file operations
> 2. Modified scripts to use proper directory permissions instead of sudo where possible
> 3. Set up audit logging to monitor for unauthorized privilege escalation
> 4. Added process limits to prevent excessive forking
> 
> Everything is now working correctly, but it would be good to implement better log parity checks to ensure we can detect any similar issues in the future. The scripts in `/opt/analytics/scripts/` could use some standardization for better maintainability.

The setting sun cast long shadows across the Madrid office as Luis closed his terminal sessions. Across the world in Seoul, Jin would soon be starting his day, ready to continue their global chain of system improvement.

*[End of Day 4]*