# Day 2: Noah's Log Dive

*08:00 AEDT - Sydney, Australia*

Noah sipped his flat white as the morning sun streamed through CloudCrest's Sydney office windows. His workspace was meticulously organized—three monitors perfectly aligned, mechanical keyboard positioned at exactly 15 degrees, and a small potted succulent that somehow survived despite the aggressive air conditioning.

The notification chime on his laptop pulled his attention to the incident handoff from Taylor in the US office:

> **@Taylor:** First day done! Found an issue with runaway logs in the analytics service. Fixed the immediate problem (test script + debug mode), but something feels off about `/var/app/uploads`. Logs looking weird. Can you take a peek when you start your shift? P.S. Sorry about the mess!

Noah smiled. New hires were always apologizing for things that weren't their fault. The CloudCrest "follow-the-sun" support model meant he was picking up where the US team left off—a digital relay race around the globe.

"Time to dive in," he muttered, cracking his knuckles with unnecessary drama despite no one being around to appreciate the gesture. The Sydney office wasn't as crowded as the San Francisco headquarters—just him and a handful of other night owls who kept Australia's tech infrastructure running while America slept.

Noah ssh'd into the analytics cluster and started his investigation:

```bash
$ ssh noah@analytics-prod-03
$ cd /var/log
$ ls -lh
```

The output showed the analytics-upload.log had been handled—now a reasonable 2MB instead of the 98GB monster Taylor had mentioned. But what caught Noah's attention was a series of smaller log files with inconsistent naming patterns.

```
-rw-r--r-- 1 root     root     2.1M Apr 11 22:15 analytics-upload.log
-rw-r--r-- 1 root     root     45M  Apr 11 21:30 analytics-upload.log.1.gz
-rw-r--r-- 1 analytics admin    34K  Apr 11 20:45 analytics_process.log
-rw-r--r-- 1 www-data www-data  17M  Apr 11 22:10 analytics.backend.log
-rw-r--r-- 1 syslog   adm      1.2G  Apr 11 22:16 syslog
```

"Well that's a mess," Noah whispered. "Mixed ownership, inconsistent naming... no wonder things are breaking." 

He needed to see what was actively being written to these files. The `tail` command with the follow option would let him watch the logs in real-time:

```bash
$ tail -f analytics-upload.log
```

Lines began streaming past:

```
[2025-04-11 22:16:03] INFO: Processing upload batch #45921
[2025-04-11 22:16:03] INFO: Found 20 files to process
[2025-04-11 22:16:04] WARN: Permissions mismatch on /var/app/uploads/user_analytics_20250411.csv
[2025-04-11 22:16:05] ERROR: Failed to move processed file to archive
```

Noah hit Ctrl+C to stop the output. "Permissions issues, eh? Let's check what's happening in syslog too..."

```bash
$ tail -n 100 syslog | grep "app/uploads"
```

The filtered output revealed dozens of permission denied errors. Something was definitely wrong with the upload directory's configuration.

"Let me see who's actually writing to this directory," Noah thought. He navigated to the upload path:

```bash
$ cd /var/app/uploads
$ ls -la
```

What he saw made his left eye twitch slightly:

```
drwxrwxrwx 4 root     root      4096 Apr 11 22:18 .
drwxr-xr-x 5 root     root      4096 Jan 15 09:10 ..
drwxr-xr-x 2 analytics analytics 4096 Apr 11 21:45 archive
drwxrwsr-x 2 www-data analytics  4096 Apr 11 22:16 incoming
-rw-r--r-- 1 www-data www-data  15.2M Apr 11 22:15 user_analytics_20250411.csv
-rw-r--r-- 1 analytics analytics 12.3M Apr 11 21:32 user_analytics_20250410.csv
```

"And there's our problem," Noah said, leaning back in his chair. The parent directory had wide-open 777 permissions—a big no-no for security. Files were being created with different owners depending on which service wrote them, causing the permission denied errors when another service tried to move them.

Noah needed to dig deeper into the logs. The `less` command would let him navigate through larger log files more easily:

```bash
$ less analytics.backend.log
```

He pressed `/` to search and typed "permission":

```
/permission
```

The screen jumped to the first match, highlighting dozens of permission-related errors. Using `n` to jump to the next match and `N` for previous matches, Noah pieced together what was happening.

Three different services were trying to access the same files:
1. The web server (running as www-data) was receiving uploads
2. The analytics processor (running as analytics) was processing them
3. An archiver (running as root in some cases) was trying to move them

Noah opened another terminal tab to check which processes were running:

```bash
$ ps aux | grep analytics
```

The output confirmed his suspicions—multiple services with different user contexts all fighting over the same files.

Next, he needed to understand the full extent of the log bloat. The `grep` command would help search through all log files for specific patterns:

```bash
$ grep -r "Failed to move processed file" --include="*.log" /var/log
```

This recursive search returned hundreds of matches across multiple log files.

"No wonder Taylor thought something was wrong," Noah muttered. "This is a disaster waiting to happen."

To get a better sense of the growing problem, Noah monitored the directory size:

```bash
$ watch -n 5 "du -sh /var/app/uploads"
```

Every 5 seconds, the display updated, showing the directory steadily growing—about 10MB every minute. At this rate, they'd have another disk space alert by tomorrow.

Noah checked how much disk space was actually available:

```bash
$ df -h
```

The output showed the `/var` partition at 78% capacity. Not critical yet, but definitely heading there fast.

Noah glanced at the clock—still plenty of time in his shift. He started documenting his findings, preparing both an incident report and a handoff for Aanya, who would be starting her day in Bengaluru, India, after Noah finished his shift.

As he typed, he kept a terminal window open with a continuous monitoring command:

```bash
$ tail -f /var/log/analytics-upload.log | grep -i "error\|warn\|fail" --color
```

This highlighted all errors and warnings in real-time, letting him spot new issues while he worked.

After compiling his findings, Noah drafted a message to Aanya:

> **@Aanya:** Following up on Taylor's analytics service issue. Root cause: mixed ownership and permissions in `/var/app/uploads`. Three different services (web, analytics, archiver) running as different users, all fighting over the same files. 
> 
> The web server writes files as www-data, analytics processes them as the analytics user, and sometimes root tries to archive them. Check `/var/log/analytics.backend.log` for the full history.
> 
> We need proper permission management and log rotation. I'm leaving you all my findings and logs. Also noticed the uploads are growing by ~10MB per minute. Might want to prepare a backup and cleanup plan before this becomes critical.
> 
> Check my script at `/home/noah/scripts/monitor_uploads.sh` – it'll help you track changes in real-time.

Before ending his shift, Noah created a simple monitoring script for Aanya:

```bash
#!/bin/bash
# monitor_uploads.sh - Created by Noah for the analytics issue
# Shows real-time file growth and permission issues

echo "Starting upload directory monitor..."
echo "===================================="

while true; do
    clear
    echo "Current time: $(date)"
    echo "------------------------------------"
    echo "Disk usage:"
    df -h | grep "/var"
    echo "------------------------------------"
    echo "Directory size:"
    du -sh /var/app/uploads
    echo "------------------------------------"
    echo "Latest errors (last 5):"
    grep -i "error\|permission denied" --include="*.log" /var/log/analytics* | tail -5
    echo "------------------------------------"
    echo "Recent file changes:"
    find /var/app/uploads -type f -mmin -5 | wc -l
    echo "new files in last 5 minutes"
    echo "===================================="
    echo "Press Ctrl+C to exit"
    sleep 10
done
```

"That should help her hit the ground running," Noah thought as he saved the script and made it executable with `chmod +x monitor_uploads.sh`.

He ran the script one last time to make sure it worked, watching as it displayed the current state of the uploads directory, the latest errors, and file growth statistics.

With his investigation complete and handoff prepared, Noah took one last sip of his now-cold coffee. The sun was setting in Sydney as he typed his final message of the day:

> **@Aanya:** All findings documented. The immediate fire is contained, but we need a proper fix for the permissions and logging. The baton is yours! P.S. Taylor did good work spotting this on their first day.

As he packed up, Noah smiled, imagining the fresh morning sun rising in Bengaluru as Aanya would be sitting down to continue their global game of technical troubleshooting. The follow-the-sun model ensured that somewhere in the world, a CloudCrest SRE was always awake, watching, and ready to dive into logs.

*[End of Day 2]*