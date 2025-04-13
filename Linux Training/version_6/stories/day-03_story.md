# Day 3: Aanya's File Management

*09:45 IST - Bengaluru, India*

Aanya arrived at CloudCrest's Bengaluru office fifteen minutes early, as usual. She preferred the quiet moments before her colleagues trickled in—time to enjoy her masala chai and mentally prepare for the day ahead. The office was perched on the 14th floor of a gleaming tower in the city's tech corridor, offering sweeping views of the bustling metropolis below.

Her phone pinged with the notification she was expecting:

> **@Noah:** All findings documented. The immediate fire is contained, but we need a proper fix for the permissions and logging. The baton is yours! P.S. Taylor did good work spotting this on their first day.

"Let's see what we're dealing with today," Aanya muttered, setting down her chai and pulling up Noah's detailed handoff notes. The situation was clear: mixed file ownership, inadequate log rotation, and a permissions nightmare in the `/var/app/uploads` directory.

Aanya connected to the analytics server:

```bash
$ ssh aanya@analytics-prod-03
$ cd /var/app/uploads
$ ls -la
```

The permissions were just as messy as Noah had described. Before making any changes, Aanya knew she needed to create proper backups—the first rule of system administration.

"Always backup before you act," she reminded herself, a mantra from her first mentor.

```bash
$ mkdir -p /tmp/analytics_backup_$(date +%Y%m%d)
$ cp -rp /var/app/uploads/* /tmp/analytics_backup_$(date +%Y%m%d)/
```

The `cp` command with `-r` (recursive) and `-p` (preserve permissions) would create an exact duplicate of the directory structure while maintaining all the original file attributes.

Next, she checked the current size of the logs Noah had mentioned:

```bash
$ du -sh /var/log/analytics*
15M   /var/log/analytics-upload.log
45M   /var/log/analytics-upload.log.1.gz
34K   /var/log/analytics_process.log
17M   /var/log/analytics.backend.log
```

The logs were growing fast, just as Noah had warned. Time to establish a proper log rotation scheme. Aanya moved to the logrotate configuration directory:

```bash
$ cd /etc/logrotate.d/
$ sudo touch analytics
$ sudo vim analytics
```

In the new file, she crafted a proper log rotation configuration:

```
/var/log/analytics*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0644 analytics analytics
    sharedscripts
    postrotate
        systemctl reload analytics-service >/dev/null 2>&1 || true
    endscript
}
```

This configuration would:
- Rotate logs daily
- Keep 7 days of history
- Compress old logs
- Create new log files with proper permissions
- Reload the service after rotation to ensure log file handles are updated

With that in place, Aanya moved on to the core issue: the messy permissions in the uploads directory. She executed Noah's monitoring script to get a real-time view:

```bash
$ /home/noah/scripts/monitor_uploads.sh
```

The script confirmed what she already knew—multiple services fighting over the same files with different user contexts. Time to fix it properly.

First, she created a properly structured directory hierarchy:

```bash
$ cd /var/app
$ sudo mkdir -p uploads/{incoming,processing,archive}
```

Next, she needed to set appropriate permissions and ownership:

```bash
$ sudo chown -R www-data:analytics uploads/incoming
$ sudo chmod 770 uploads/incoming
$ sudo chown -R analytics:analytics uploads/processing
$ sudo chmod 750 uploads/processing
$ sudo chown -R analytics:analytics uploads/archive
$ sudo chmod 750 uploads/archive
```

This would ensure:
- The web server (www-data) could write to the incoming directory
- The analytics service (analytics user) could read from incoming and would own processing
- All processed files would move to archive with appropriate permissions

To prevent future permission issues with new files, Aanya set the "setgid" bit on the directories:

```bash
$ sudo chmod g+s uploads/incoming
$ sudo chmod g+s uploads/processing
$ sudo chmod g+s uploads/archive
```

The "setgid" bit would ensure any new files created in these directories would inherit the group ownership automatically.

Now came the task of moving existing files to their proper locations:

```bash
$ find /var/app/uploads -type f -name "*.csv" -mtime -1 -exec sudo mv {} /var/app/uploads/incoming/ \;
$ find /var/app/uploads -type f -name "*.csv" -mtime +1 -exec sudo mv {} /var/app/uploads/archive/ \;
```

These commands would move recent CSV files to the incoming directory and older ones directly to archive.

Aanya checked her work:

```bash
$ ls -la /var/app/uploads/incoming
$ ls -la /var/app/uploads/processing
$ ls -la /var/app/uploads/archive
```

The directory structure looked clean, with proper ownership and permissions.

Next, she needed to adjust the service configurations to use the new directory structure. She moved to the configuration files:

```bash
$ cd /etc/analytics
$ ls -la
```

She found several configuration files:

```
-rw-r--r-- 1 root root 2.1K Apr 11 21:30 upload.conf
-rw-r--r-- 1 root root 1.8K Apr 11 21:30 processing.conf
-rw-r--r-- 1 root root 1.5K Apr 11 21:30 archiver.conf
```

Time to modify each one:

```bash
$ sudo cp upload.conf upload.conf.bak
$ sudo vim upload.conf
```

She edited the file to point to the new incoming directory:

```
upload_dir: /var/app/uploads/incoming
```

Next, the processing configuration:

```bash
$ sudo cp processing.conf processing.conf.bak
$ sudo vim processing.conf
```

Updated to use the new directories:

```
input_dir: /var/app/uploads/incoming
output_dir: /var/app/uploads/processing
archive_dir: /var/app/uploads/archive
```

Finally, the archiver configuration:

```bash
$ sudo cp archiver.conf archiver.conf.bak
$ sudo vim archiver.conf
```

Updated to use only the archive directory:

```
archive_source: /var/app/uploads/processing
archive_destination: /var/app/uploads/archive
```

With the configurations updated, Aanya needed to restart the services:

```bash
$ sudo systemctl restart analytics-upload-service
$ sudo systemctl restart analytics-processing-service
$ sudo systemctl restart analytics-archiver-service
```

Now she monitored the log files to ensure everything was working correctly:

```bash
$ tail -f /var/log/analytics-upload.log
```

The log showed files being properly written to the incoming directory with the correct permissions. Success!

To prevent future confusion, Aanya created a detailed README.md file describing the directory structure and expected permissions:

```bash
$ sudo vim /var/app/uploads/README.md
```

```markdown
# Analytics Upload Directory Structure

## Overview
This directory contains data for the CloudCrest analytics processing pipeline.

## Directory Structure
- `/var/app/uploads/incoming`: Owned by www-data:analytics (770)
  * New files arrive here from the web service
  
- `/var/app/uploads/processing`: Owned by analytics:analytics (750)
  * Files actively being processed
  
- `/var/app/uploads/archive`: Owned by analytics:analytics (750)
  * Completed files stored for audit and backup

## Service Flow
1. Web service writes to incoming
2. Processing service moves files from incoming to processing
3. Processing service moves completed files to archive

## Log Rotation
Logs are rotated daily with 7-day retention. See /etc/logrotate.d/analytics

Last updated: [date] by Aanya
```

With the directory structure fixed, log rotation configured, and clear documentation added, Aanya moved on to her final task: automation.

She created a script that would clean up any lingering issues and verify the proper setup:

```bash
$ vim /home/aanya/scripts/analytics_maintenance.sh
```

```bash
#!/bin/bash
# analytics_maintenance.sh - Created by Aanya
# Daily maintenance for analytics directories

# Set variables
INCOMING="/var/app/uploads/incoming"
PROCESSING="/var/app/uploads/processing"
ARCHIVE="/var/app/uploads/archive"
LOG_FILE="/var/log/analytics_maintenance.log"

# Ensure log file exists with proper permissions
if [ ! -f "$LOG_FILE" ]; then
    touch "$LOG_FILE"
    chown analytics:analytics "$LOG_FILE"
    chmod 644 "$LOG_FILE"
fi

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

log "Starting analytics maintenance script"

# Fix any wrong permissions
log "Checking directory permissions"
chown www-data:analytics "$INCOMING"
chmod 770 "$INCOMING"
chmod g+s "$INCOMING"

chown analytics:analytics "$PROCESSING"
chmod 750 "$PROCESSING"
chmod g+s "$PROCESSING"

chown analytics:analytics "$ARCHIVE"
chmod 750 "$ARCHIVE"
chmod g+s "$ARCHIVE"

# Move stuck files (older than 1 day) from incoming to processing
log "Checking for stuck files in incoming"
find "$INCOMING" -type f -mtime +1 -exec mv {} "$PROCESSING" \;

# Move stuck files (older than 3 days) from processing to archive
log "Checking for stuck files in processing"
find "$PROCESSING" -type f -mtime +3 -exec mv {} "$ARCHIVE" \;

# Archive old files (older than 30 days) by compressing them
log "Compressing old archive files"
find "$ARCHIVE" -type f -mtime +30 -name "*.csv" -exec gzip {} \;

# Check disk usage and report
USAGE=$(df -h | grep "/var" | awk '{print $5}' | sed 's/%//')
log "Current disk usage: $USAGE%"

if [ "$USAGE" -gt 80 ]; then
    log "WARNING: Disk usage above 80%"
    # Send alert
    mail -s "CloudCrest Analytics: High Disk Usage" sre-team@cloudcrest.example <<< "Disk usage is at $USAGE%. Please investigate."
fi

log "Maintenance completed successfully"
```

She made the script executable and added it to the crontab to run daily:

```bash
$ chmod +x /home/aanya/scripts/analytics_maintenance.sh
$ sudo crontab -e
```

Added the line:

```
0 2 * * * /home/aanya/scripts/analytics_maintenance.sh
```

This would run the maintenance script at 2 AM every day.

Aanya ran the script once manually to ensure it worked:

```bash
$ sudo /home/aanya/scripts/analytics_maintenance.sh
$ cat /var/log/analytics_maintenance.log
```

The log confirmed everything was working as expected.

As her shift was coming to an end, Aanya prepared a handoff for Luis in Madrid, who would be starting his day soon:

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

Aanya took one final look at Noah's monitoring script:

```bash
$ /home/noah/scripts/monitor_uploads.sh
```

The output showed everything was now functioning smoothly. Directory sizes were stable, and no new permission errors were appearing in the logs.

Satisfied with her work, Aanya closed her terminal windows and prepared to head out. As the afternoon sun slanted through the Bengaluru office windows, she gathered her things, knowing that halfway across the world in Madrid, Luis would soon be sitting down with his morning coffee, ready to take the baton in their never-ending relay race of system reliability.

*[End of Day 3]*