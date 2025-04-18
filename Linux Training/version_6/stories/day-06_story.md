# Day 6: Fatima's Process Monitoring

*08:30 GST - Dubai, UAE*

Fatima arrived at CloudCrest's Dubai office just as the morning sun was beginning to heat the gleaming skyscrapers of the business district. The office occupied half a floor in one of the newer towers, its windows offering a panoramic view of the city and the distant desert beyond.

Her desk was adorned with a small collection of succulents and a framed photograph of her climbing team at the summit of Jebel Jais. Fatima was known for her methodical approach to security and her ability to untangle the most complex process issues.

She scrolled through Jin's handoff message while sipping her cardamom-infused coffee:

> **@Fatima:** I've addressed the log standardization and monitoring issues:
> 
> 1. Created a unified log format and documentation in /opt/analytics/README-logging.md
> 2. Built a suite of log processing tools:
>    - log_standardizer.sh: Converts all logs to a standard format
>    - log_analyzer.sh: Generates daily reports on log patterns
>    - log_parity_check.sh: Alerts on missing or out-of-sequence events
>    - log_sanitizer.sh: Removes sensitive data from logs
> 
> All scripts run on scheduled cron jobs, and alerts are sent to the SRE team email.
> 
> I noticed some potential security concerns with sensitive data in the logs, which my sanitizer script addresses, but you might want to further investigate the upload service's HTTPS implementation. There are hints in the logs of SSL certificate verification being disabled in some API calls.

"SSL verification disabled? That's a serious concern," Fatima muttered. But before diving into that issue, she wanted to get a complete picture of the system's current state.

She connected to the analytics server:

```bash
$ ssh fatima@analytics-prod-03
```

First, she needed to check the overall system status:

```bash
$ top
```

The output displayed the current processes, sorted by CPU usage:

```
top - 08:35:12 up 5 days, 12:43, 1 user, load average: 0.75, 0.93, 0.87
Tasks: 213 total,   1 running, 212 sleeping,   0 stopped,   0 zombie
%Cpu(s):  5.7 us,  2.1 sy,  0.0 ni, 91.8 id,  0.3 wa,  0.0 hi,  0.1 si,  0.0 st
MiB Mem :  16384.0 total,   2635.1 free,   8796.5 used,   4952.4 buff/cache
MiB Swap:   8192.0 total,   8096.1 free,     95.9 used.   5692.3 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                   
 9876 analyzer  20   0 1258740 298504  14352 S   4.3   1.8  65:23.21 analytics-service                                                         
 5432 www-data  20   0  724512 142308  12836 S   3.2   0.8  18:45.12 upload-service                                                            
 4321 analytics 20   0  684128 125484  11248 S   2.1   0.7  22:30.45 processing-service                                                        
 3210 postgres  20   0  512992  98756  10248 S   1.5   0.6  45:20.10 postgres                                                                  
12345 root      20   0   89456  15760   9968 S   0.3   0.1   2:15.33 systemd                                                                   
```

She pressed `q` to exit top and checked the system's memory and swap usage in more detail:

```bash
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           16Gi       8.6Gi       2.6Gi       295Mi       4.8Gi       5.6Gi
Swap:          8.0Gi        96Mi       7.9Gi
```

Next, she examined the disk usage:

```bash
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       120G   73G   41G  64% /
/dev/sdb1       500G  325G  150G  69% /var
```

With a basic system overview in hand, Fatima moved on to investigate the running processes in more detail:

```bash
$ ps aux | grep analytics
```

The output showed several analytics-related processes and their resource usage.

To get a more interactive view, she launched `htop`, a more feature-rich alternative to `top`:

```bash
$ htop
```

In the colorful display, she could see the process hierarchy, memory usage, and CPU load across all cores. She noticed that one of the analytics processes had spawned multiple children, some consuming more resources than expected.

She exited `htop` with `F10` and decided to check which tasks were scheduled to run via cron:

```bash
$ crontab -l
```

Jin's scripts were there, along with various other maintenance tasks:

```
# Run log standardization and parity check every hour
0 * * * * /home/jin/scripts/analytics/log_standardizer.sh
15 * * * * /home/jin/scripts/analytics/log_analyzer.sh
30 * * * * /home/jin/scripts/analytics/log_parity_check.sh
# Sanitize logs daily
0 0 * * * /home/jin/scripts/analytics/log_sanitizer.sh
```

She also checked the system-wide crontab:

```bash
$ sudo cat /etc/crontab
```

There, she found Aanya's maintenance script:

```
0 2 * * * /home/aanya/scripts/analytics_maintenance.sh
```

Now that she had a clear picture of the system's state and scheduled tasks, Fatima focused on the most pressing issue: the SSL verification concern Jin had mentioned.

She searched the standardized logs for SSL-related entries:

```bash
$ grep -i "ssl\|cert\|https" /var/log/analytics/unified/unified_$(date +%Y%m%d).log
```

Several concerning entries appeared:

```
2025-04-13 07:15:22 UPLOAD WARN [SSLConnector] SSL certificate verification disabled for endpoint: https://api.analytics-partner.com
2025-04-13 07:16:45 UPLOAD INFO [HTTPClient] Connected to external API with insecure flag
2025-04-13 08:01:12 UPLOAD WARN [SSLConnector] SSL certificate verification disabled for endpoint: https://metrics.analytics-partner.com
```

To find the source of these issues, Fatima examined the upload service configuration:

```bash
$ cat /etc/analytics/upload-service.conf
```

The configuration contained a problematic setting:

```
# API Connection Settings
api_url = https://api.analytics-partner.com
metrics_url = https://metrics.analytics-partner.com
verify_ssl = false  # TODO: Enable for production
```

"Someone left a development setting in production," Fatima said to herself. This was a serious security oversight that needed immediate attention.

Next, she wanted to look at the running processes in more detail to understand their relationships and resource usage:

```bash
$ ps -ef --forest
```

This command displayed processes in a tree format, showing parent-child relationships:

```
UID         PID   PPID  C STIME TTY          TIME CMD
root          1      0  0 Apr08 ?        00:00:33 /sbin/init
root       1255      1  0 Apr08 ?        00:00:12  \_ /usr/sbin/cron
root       3471   1255  0 08:00 ?        00:00:02      \_ /bin/sh /home/aanya/scripts/analytics_maintenance.sh
analytics  9876      1  0 Apr08 ?        01:05:23 /usr/bin/analytics-service
analytics  9880   9876  0 Apr08 ?        00:45:11  \_ /usr/bin/analytics-worker
analytics  9881   9880  0 Apr08 ?        00:30:22      \_ /usr/bin/analytics-processor
analytics 12345   9881  0 08:32 ?        00:00:05          \_ /bin/bash /opt/analytics/scripts/process_batch.sh 46010
```

Fatima also wanted to check which ports were being used and which processes were listening:

```bash
$ sudo ss -tulpn
```

The output showed all TCP and UDP ports in use, along with the processes that owned them:

```
Netid  State   Recv-Q  Send-Q   Local Address:Port    Peer Address:Port  Process                                                  
tcp    LISTEN  0       128      0.0.0.0:22            0.0.0.0:*          users:(("sshd",pid=1234,fd=3))                          
tcp    LISTEN  0       128      127.0.0.1:5432        0.0.0.0:*          users:(("postgres",pid=3210,fd=5))                      
tcp    LISTEN  0       128      0.0.0.0:8080          0.0.0.0:*          users:(("analytics-service",pid=9876,fd=6))            
tcp    LISTEN  0       128      0.0.0.0:8081          0.0.0.0:*          users:(("upload-service",pid=5432,fd=8))              
tcp    LISTEN  0       128      127.0.0.1:9000        0.0.0.0:*          users:(("processing-service",pid=4321,fd=7))          
```

To gather more information about long-running processes, she checked for zombie processes that might indicate issues with how child processes were being managed:

```bash
$ ps aux | grep Z
```

No zombie processes were found, which was a good sign.

With a thorough understanding of the system's processes, Fatima turned her attention to the secure implementation of log rotation and service management.

She first checked how log rotation was currently configured:

```bash
$ cat /etc/logrotate.d/analytics
```

The configuration looked solid, but she noticed it didn't include any secure measures for handling the rotated logs:

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

To enhance security, Fatima created an improved log rotation configuration with stronger permissions:

```bash
$ sudo cp /etc/logrotate.d/analytics /etc/logrotate.d/analytics.bak
$ sudo vim /etc/logrotate.d/analytics
```

She updated the configuration:

```
/var/log/analytics*.log {
    daily
    rotate 14
    compress
    delaycompress
    missingok
    notifempty
    create 0640 analytics analytics
    dateext
    dateformat -%Y%m%d
    sharedscripts
    su analytics analytics
    olddir /var/log/archive
    postrotate
        systemctl reload analytics-service >/dev/null 2>&1 || true
    endscript
    lastaction
        find /var/log/archive -type f -name "*.gz" -mtime +30 -exec chmod 600 {} \;
        find /var/log/archive -type f -name "*.gz" -mtime +90 -delete
    endscript
}
```

These changes would:
- Create rotated logs with more restrictive 0640 permissions
- Add date extensions to rotated logs
- Move old logs to a dedicated archive directory
- Run rotation as the analytics user, not root
- Automatically secure older logs with tighter permissions
- Delete logs older than 90 days

Next, Fatima created a directory for archived logs with proper permissions:

```bash
$ sudo mkdir -p /var/log/archive
$ sudo chown analytics:analytics /var/log/archive
$ sudo chmod 750 /var/log/archive
```

To address the SSL verification issue, she created a proper fix:

```bash
$ sudo cp /etc/analytics/upload-service.conf /etc/analytics/upload-service.conf.bak
$ sudo vim /etc/analytics/upload-service.conf
```

She changed the setting:

```
# API Connection Settings
api_url = https://api.analytics-partner.com
metrics_url = https://metrics.analytics-partner.com
verify_ssl = true  # FIXED: SSL verification enabled for security
```

To ensure these changes were properly applied, she needed to restart the upload service. But first, she wanted to make sure it wouldn't disrupt any ongoing operations:

```bash
$ ps aux | grep upload-service
$ sudo systemctl status upload-service
```

After confirming it was safe to restart, she proceeded:

```bash
$ sudo systemctl restart upload-service
```

She verified the service started successfully:

```bash
$ sudo systemctl status upload-service
```

The output showed it was running correctly:

```
● upload-service.service - Analytics Upload Service
     Loaded: loaded (/etc/systemd/system/upload-service.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2025-04-13 09:15:42 GST; 8s ago
   Main PID: 5432 (upload-service)
      Tasks: 6 (limit: 4651)
     Memory: 142.3M
     CGroup: /system.slice/upload-service.service
             └─5432 /usr/bin/upload-service

Apr 13 09:15:42 analytics-prod-03 systemd[1]: Started Analytics Upload Service.
Apr 13 09:15:43 analytics-prod-03 upload-service[5432]: Starting upload service...
Apr 13 09:15:44 analytics-prod-03 upload-service[5432]: Connected to database successfully
Apr 13 09:15:44 analytics-prod-03 upload-service[5432]: SSL verification enabled for API connections
Apr 13 09:15:45 analytics-prod-03 upload-service[5432]: Listening on port 8081
```

To monitor for any post-restart issues, Fatima set up a watch on the service's log:

```bash
$ tail -f /var/log/analytics-upload.log
```

Everything appeared to be functioning correctly with SSL verification now enabled.

To ensure the system stayed secure, Fatima created a process monitoring script that would alert on unusual resource usage:

```bash
$ vim /home/fatima/scripts/process_monitor.sh
```

```bash
#!/bin/bash
# process_monitor.sh - Created by Fatima
# Monitors critical processes and resource usage

LOG_DIR="/var/log/monitoring"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/process_monitor_$(date +%Y%m%d).log"
ALERT_THRESHOLD_CPU=80  # CPU percentage
ALERT_THRESHOLD_MEM=75  # Memory percentage
ALERT_THRESHOLD_DISK=85 # Disk usage percentage

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

send_alert() {
    local subject="$1"
    local message="$2"
    log "ALERT: $subject - $message"
    mail -s "CloudCrest Alert: $subject" sre-team@cloudcrest.example <<< "$message"
}

log "Starting process monitoring..."

# Check critical processes
EXPECTED_PROCESSES=("analytics-service" "upload-service" "processing-service" "postgres")
for process in "${EXPECTED_PROCESSES[@]}"; do
    if ! pgrep -x "$process" > /dev/null; then
        send_alert "Process not running" "Critical process $process is not running!"
    else
        log "Process $process is running"
    fi
done

# Check for CPU hogs
CPU_HOGS=$(ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head -n 10)
HIGH_CPU=$(echo "$CPU_HOGS" | awk -v threshold=$ALERT_THRESHOLD_CPU '$4 > threshold {print}')
if [ -n "$HIGH_CPU" ]; then
    send_alert "High CPU Usage" "Processes exceeding ${ALERT_THRESHOLD_CPU}% CPU usage:\n\n$HIGH_CPU"
else
    log "No processes exceeding CPU threshold"
fi

# Check for memory hogs
MEM_HOGS=$(ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%mem | head -n 10)
HIGH_MEM=$(echo "$MEM_HOGS" | awk -v threshold=$ALERT_THRESHOLD_MEM '$5 > threshold {print}')
if [ -n "$HIGH_MEM" ]; then
    send_alert "High Memory Usage" "Processes exceeding ${ALERT_THRESHOLD_MEM}% memory usage:\n\n$HIGH_MEM"
else
    log "No processes exceeding memory threshold"
fi

# Check disk usage
DISK_USAGE=$(df -h | grep -vE '^tmpfs|^devtmpfs|^udev')
HIGH_DISK=$(echo "$DISK_USAGE" | awk -v threshold=$ALERT_THRESHOLD_DISK '{ if (int($5) > threshold) print }')
if [ -n "$HIGH_DISK" ]; then
    send_alert "High Disk Usage" "Filesystem usage exceeding ${ALERT_THRESHOLD_DISK}%:\n\n$HIGH_DISK"
else
    log "No filesystems exceeding disk threshold"
fi

# Check for zombie processes
ZOMBIES=$(ps aux | grep -w Z)
if [ -n "$ZOMBIES" ]; then
    send_alert "Zombie Processes Detected" "Found zombie processes:\n\n$ZOMBIES"
else
    log "No zombie processes found"
fi

# Check systemd service status
for service in analytics-service upload-service processing-service; do
    STATUS=$(systemctl is-active "$service")
    if [ "$STATUS" != "active" ]; then
        send_alert "Service Not Active" "Service $service is $STATUS!"
    else
        log "Service $service is active"
    fi
done

log "Process monitoring completed successfully"
```

She made the script executable and added it to her crontab:

```bash
$ chmod +x /home/fatima/scripts/process_monitor.sh
$ crontab -e
```

Added:

```
# Run process monitoring every 15 minutes
*/15 * * * * /home/fatima/scripts/process_monitor.sh
```

To secure log access, Fatima implemented a more restrictive user policy for log access:

```bash
$ sudo groupadd log-readers
$ sudo usermod -a -G log-readers fatima
$ sudo usermod -a -G log-readers jin
$ sudo usermod -a -G log-readers luis
$ sudo usermod -a -G log-readers aanya
$ sudo usermod -a -G log-readers noah
$ sudo usermod -a -G log-readers taylor
```

Then she set appropriate permissions on the log directories:

```bash
$ sudo chown -R analytics:log-readers /var/log/analytics
$ sudo chmod -R 750 /var/log/analytics
$ sudo chmod -R 750 /var/log/analytics/unified
$ sudo chmod -R 750 /var/log/analytics/reports
$ sudo chmod -R 700 /var/log/analytics/alerts  # Only analytics user can access alerts
```

Finally, Fatima wanted to ensure system security wasn't compromised by any suspicious processes. She looked for any unusual processes or open connections:

```bash
$ sudo lsof -i
```

The output showed all open network connections. She carefully inspected each one to ensure there were no unauthorized connections.

She also checked for any processes running with root privileges that shouldn't have them:

```bash
$ sudo ps -U root -u root u
```

After verifying everything was in order, Fatima prepared a handoff message for Mina in Lagos:

> **@Mina:** I've addressed several process monitoring and security concerns:
> 
> 1. Fixed a critical security issue - SSL verification was disabled in the upload service
> 2. Implemented more secure log rotation with proper permissions and retention policies
> 3. Created a comprehensive process monitoring script that runs every 15 minutes
> 4. Implemented a restricted user policy for log access with the new log-readers group
> 
> All services are now running correctly with proper resource usage. I've also verified there are no zombie processes or unexpected high-CPU operations.
> 
> The system seems to be stabilizing well after all our team's improvements this week. You might want to look into building a visualization dashboard for our monitoring data, as we now have strong foundations for tracking system health.

As the afternoon sun cast long shadows through the Dubai office, Fatima gathered her things and prepared to head out. In Lagos, Mina would soon be starting her workday, continuing CloudCrest's around-the-world approach to maintaining their critical infrastructure.

*[End of Day 6]*