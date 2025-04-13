# Day 5: Jin's Text Processing

*09:00 KST - Seoul, South Korea*

Jin arrived at CloudCrest's Seoul office, located in a sleek tower in the Gangnam district. The space was minimal and efficient, much like Jin's approach to problem-solving. A small bonsai tree—the only personal item on his otherwise pristine desk—sat beside three perfectly aligned monitors.

He scrolled through Luis's handoff message while sipping his morning americano:

> **@Jin:** I've addressed the process forking issues Aanya mentioned. The analytics services were using unrestricted sudo privileges, causing the permission inconsistencies. Changes made:
> 
> 1. Restricted sudo permissions to only the necessary file operations
> 2. Modified scripts to use proper directory permissions instead of sudo where possible
> 3. Set up audit logging to monitor for unauthorized privilege escalation
> 4. Added process limits to prevent excessive forking
> 
> Everything is now working correctly, but it would be good to implement better log parity checks to ensure we can detect any similar issues in the future. The scripts in `/opt/analytics/scripts/` could use some standardization for better maintainability.

"Log parity and script standardization—right up my alley," Jin muttered to himself. He was known for his text processing wizardry, often able to extract actionable intelligence from the most chaotic log files.

Jin connected to the analytics server:

```bash
$ ssh jin@analytics-prod-03
```

First, he wanted to get a comprehensive view of the logs after all the recent changes:

```bash
$ cd /var/log
$ ls -la analytics*
```

The output showed several log files with different formats and conventions:

```
-rw-r--r-- 1 analytics analytics  4.5M Apr 13 08:34 analytics-upload.log
-rw-r--r-- 1 analytics analytics  2.1M Apr 12 23:59 analytics-upload.log.1.gz
-rw-r--r-- 1 analytics analytics  890K Apr 13 08:32 analytics-processing.log
-rw-r--r-- 1 analytics analytics  1.2M Apr 13 08:33 analytics-archiver.log
-rw-r--r-- 1 analytics analytics  545K Apr 13 08:35 analytics-api.log
```

Jin examined each log format to understand the inconsistencies:

```bash
$ head -5 analytics-upload.log
[2025-04-13 08:30:12] [INFO] Upload service started
[2025-04-13 08:30:15] [INFO] Processing upload batch #46001
[2025-04-13 08:31:02] [WARN] Slow upload detected - 12.5 seconds for file: user_data_46001.csv
[2025-04-13 08:31:45] [INFO] Successfully processed upload: user_data_46001.csv
[2025-04-13 08:32:10] [INFO] Processing upload batch #46002

$ head -5 analytics-processing.log
2025-04-13T08:30:14.522Z INFO  [ProcessingService] Service initialized
2025-04-13T08:30:17.891Z INFO  [BatchProcessor] Starting batch #46001
2025-04-13T08:31:50.104Z INFO  [DataTransformer] Transformed 1523 records
2025-04-13T08:31:52.310Z INFO  [BatchProcessor] Completed batch #46001
2025-04-13T08:32:15.765Z INFO  [BatchProcessor] Starting batch #46002

$ head -5 analytics-archiver.log
Apr 13 08:30:18 analytics-prod-03 archiver[3471]: Starting archiver service
Apr 13 08:31:55 analytics-prod-03 archiver[3471]: Archiving batch #46001
Apr 13 08:31:56 analytics-prod-03 archiver[3471]: Successfully archived batch #46001
Apr 13 08:32:45 analytics-prod-03 archiver[3471]: Archiving batch #46002
Apr 13 08:32:46 analytics-prod-03 archiver[3471]: Successfully archived batch #46002
```

"Three completely different log formats—no wonder it's hard to trace events across services," Jin observed. This would require some serious text processing to standardize.

First, Jin wanted to extract key events from all logs to create a unified timeline. He created a directory for his scripts:

```bash
$ mkdir -p ~/scripts/analytics
$ cd ~/scripts/analytics
```

Then he wrote a script to parse and standardize the different log formats:

```bash
$ vim log_standardizer.sh
```

```bash
#!/bin/bash
# log_standardizer.sh - Created by Jin
# Standardizes different log formats to a common format

# Output file
OUTPUT_DIR="/var/log/analytics/unified"
mkdir -p "$OUTPUT_DIR"
OUTPUT_FILE="$OUTPUT_DIR/unified_$(date +%Y%m%d).log"

# Temporary files
TEMP_DIR="/tmp/analytics_logs"
mkdir -p "$TEMP_DIR"

# Process upload logs - [YYYY-MM-DD HH:MM:SS] [LEVEL] Message
process_upload_log() {
    sed -r 's/\[(.*)\] \[(.*)\] (.*)/\1 UPLOAD \2 \3/' "$1" > "$TEMP_DIR/upload.tmp"
}

# Process processing logs - YYYY-MM-DDThh:mm:ss.SSSZ LEVEL [Component] Message
process_processing_log() {
    sed -r 's/(.*)T(.*)Z (.*) \[(.*)\] (.*)/\1 \2 PROCESSING \3 \5/' "$1" > "$TEMP_DIR/processing.tmp"
}

# Process archiver logs - MMM DD HH:MM:SS hostname program[PID]: Message
process_archiver_log() {
    # Convert month name to number
    sed -r 's/^([A-Z][a-z]{2}) ([0-9]{2}) ([0-9:]{8}).*archiver\[[0-9]+\]: (.*)/2025-04-\2 \3 ARCHIVER INFO \4/' "$1" > "$TEMP_DIR/archiver.tmp"
}

# Process analytics API logs
process_api_log() {
    # Another format processing rule for API logs
    sed -r 's/.*API.*/2025-04-13 00:00:00 API INFO &/' "$1" > "$TEMP_DIR/api.tmp"
}

# Main processing
echo "Starting log standardization..."

# Process each log type
process_upload_log "/var/log/analytics-upload.log"
process_processing_log "/var/log/analytics-processing.log"
process_archiver_log "/var/log/analytics-archiver.log"
process_api_log "/var/log/analytics-api.log"

# Combine all logs and sort by timestamp
cat "$TEMP_DIR"/*.tmp | sort > "$OUTPUT_FILE"

echo "Unified log created at $OUTPUT_FILE"

# Clean up
rm -rf "$TEMP_DIR"
```

He made the script executable and tested it:

```bash
$ chmod +x log_standardizer.sh
$ ./log_standardizer.sh
```

Next, Jin wanted to analyze the unified log to find patterns and potential issues. He created another script for this purpose:

```bash
$ vim log_analyzer.sh
```

```bash
#!/bin/bash
# log_analyzer.sh - Created by Jin
# Analyzes unified logs for patterns and anomalies

UNIFIED_LOG="/var/log/analytics/unified/unified_$(date +%Y%m%d).log"
REPORT_FILE="/var/log/analytics/reports/daily_report_$(date +%Y%m%d).txt"

mkdir -p "/var/log/analytics/reports"

echo "CloudCrest Analytics Log Analysis" > "$REPORT_FILE"
echo "Date: $(date)" >> "$REPORT_FILE"
echo "---------------------------------------" >> "$REPORT_FILE"

# Count events by service
echo -e "\n== Event Counts by Service ==" >> "$REPORT_FILE"
awk '{print $3}' "$UNIFIED_LOG" | sort | uniq -c | sort -nr >> "$REPORT_FILE"

# Count events by severity
echo -e "\n== Event Counts by Severity ==" >> "$REPORT_FILE"
awk '{print $4}' "$UNIFIED_LOG" | sort | uniq -c | sort -nr >> "$REPORT_FILE"

# Find slow operations (taking more than 10 seconds)
echo -e "\n== Slow Operations ==" >> "$REPORT_FILE"
grep -i "slow\|timeout\|[0-9]\{2\}\.[0-9] seconds" "$UNIFIED_LOG" >> "$REPORT_FILE"

# Find error patterns
echo -e "\n== Common Error Patterns ==" >> "$REPORT_FILE"
grep -i "error\|fail\|exception" "$UNIFIED_LOG" | 
  awk '{$1=""; $2=""; $3=""; $4=""; print $0}' | 
  sed 's/^[ \t]*//' | 
  sort | 
  uniq -c | 
  sort -nr | 
  head -10 >> "$REPORT_FILE"

# Track batch processing times
echo -e "\n== Batch Processing Times ==" >> "$REPORT_FILE"
echo "BatchID | Upload Time | Processing Time | Archive Time | Total Time" >> "$REPORT_FILE"
echo "---------------------------------------------------------------" >> "$REPORT_FILE"

# This requires complex awk processing to correlate events across logs
grep -i "batch #[0-9]\+" "$UNIFIED_LOG" | 
  awk '
    /Processing upload batch/ {upload_time[$NF] = $1 " " $2}
    /Completed batch/ {process_time[$NF] = $1 " " $2}
    /Successfully archived batch/ {
      archive_time[$NF] = $1 " " $2;
      if (upload_time[$NF] && process_time[$NF]) {
        cmd = "date -d\"" archive_time[$NF] "\" +%s";
        cmd | getline archive_epoch;
        close(cmd);
        
        cmd = "date -d\"" upload_time[$NF] "\" +%s";
        cmd | getline upload_epoch;
        close(cmd);
        
        total = archive_epoch - upload_epoch;
        printf "%-7s | %-11s | %-15s | %-12s | %d seconds\n", 
          $NF, upload_time[$NF], process_time[$NF], archive_time[$NF], total;
      }
    }
  ' >> "$REPORT_FILE"

# Look for potential security issues
echo -e "\n== Potential Security Issues ==" >> "$REPORT_FILE"
grep -i "sudo\|permission\|denied\|unauthorized" "$UNIFIED_LOG" >> "$REPORT_FILE"

echo "Analysis complete. Report saved to $REPORT_FILE"
```

He made this script executable as well:

```bash
$ chmod +x log_analyzer.sh
$ ./log_analyzer.sh
```

The report provided valuable insights into the system's behavior. Jin noticed several patterns that needed addressing, but before implementing fixes, he wanted to verify how events were correlated across logs.

To do this, Jin created a log parity check script that would alert on inconsistencies:

```bash
$ vim log_parity_check.sh
```

```bash
#!/bin/bash
# log_parity_check.sh - Created by Jin
# Checks for log parity issues (events missing from one service's logs that appear in others)

UNIFIED_LOG="/var/log/analytics/unified/unified_$(date +%Y%m%d).log"
ALERT_FILE="/var/log/analytics/alerts/parity_alert_$(date +%Y%m%d%H%M).txt"

mkdir -p "/var/log/analytics/alerts"

echo "CloudCrest Analytics Log Parity Check" > "$ALERT_FILE"
echo "Date: $(date)" >> "$ALERT_FILE"
echo "---------------------------------------" >> "$ALERT_FILE"

# Extract all batch IDs
ALL_BATCHES=$(grep -o "batch #[0-9]\+" "$UNIFIED_LOG" | sed 's/batch #//' | sort -n | uniq)

# Check each batch for parity across services
echo -e "\n== Missing Log Entries ==" >> "$ALERT_FILE"
for batch in $ALL_BATCHES; do
    # Count occurrences in each service log
    UPLOAD_COUNT=$(grep -c "UPLOAD.*batch #$batch" "$UNIFIED_LOG")
    PROCESSING_COUNT=$(grep -c "PROCESSING.*batch #$batch" "$UNIFIED_LOG")
    ARCHIVER_COUNT=$(grep -c "ARCHIVER.*batch #$batch" "$UNIFIED_LOG")
    
    # Check for parity issues
    if [ $UPLOAD_COUNT -eq 0 ]; then
        echo "ALERT: Batch #$batch missing from UPLOAD logs" >> "$ALERT_FILE"
    fi
    
    if [ $PROCESSING_COUNT -eq 0 ]; then
        echo "ALERT: Batch #$batch missing from PROCESSING logs" >> "$ALERT_FILE"
    fi
    
    if [ $ARCHIVER_COUNT -eq 0 ]; then
        echo "ALERT: Batch #$batch missing from ARCHIVER logs" >> "$ALERT_FILE"
    fi
done

# Check for sequence inconsistencies
echo -e "\n== Sequence Issues ==" >> "$ALERT_FILE"
for batch in $ALL_BATCHES; do
    # Get timestamps of key events
    UPLOAD_START=$(grep "UPLOAD.*Processing upload batch #$batch" "$UNIFIED_LOG" | head -1 | awk '{print $1 " " $2}')
    PROCESS_START=$(grep "PROCESSING.*Starting batch #$batch" "$UNIFIED_LOG" | head -1 | awk '{print $1 " " $2}')
    PROCESS_END=$(grep "PROCESSING.*Completed batch #$batch" "$UNIFIED_LOG" | head -1 | awk '{print $1 " " $2}')
    ARCHIVE_START=$(grep "ARCHIVER.*Archiving batch #$batch" "$UNIFIED_LOG" | head -1 | awk '{print $1 " " $2}')
    
    # Check if events occurred in the expected sequence
    if [ -n "$UPLOAD_START" ] && [ -n "$PROCESS_START" ]; then
        if [[ "$UPLOAD_START" > "$PROCESS_START" ]]; then
            echo "ALERT: Batch #$batch processing started before upload (U: $UPLOAD_START, P: $PROCESS_START)" >> "$ALERT_FILE"
        fi
    fi
    
    if [ -n "$PROCESS_END" ] && [ -n "$ARCHIVE_START" ]; then
        if [[ "$ARCHIVE_START" < "$PROCESS_END" ]]; then
            echo "ALERT: Batch #$batch archiving started before processing completed (P: $PROCESS_END, A: $ARCHIVE_START)" >> "$ALERT_FILE"
        fi
    fi
done

# Check for excessive time gaps
echo -e "\n== Excessive Time Gaps ==" >> "$ALERT_FILE"
for batch in $ALL_BATCHES; do
    # Get timestamps of key events
    UPLOAD_START=$(grep "UPLOAD.*Processing upload batch #$batch" "$UNIFIED_LOG" | head -1 | awk '{print $1 " " $2}')
    PROCESS_START=$(grep "PROCESSING.*Starting batch #$batch" "$UNIFIED_LOG" | head -1 | awk '{print $1 " " $2}')
    
    if [ -n "$UPLOAD_START" ] && [ -n "$PROCESS_START" ]; then
        # Convert to epochs for comparison
        UPLOAD_EPOCH=$(date -d "$UPLOAD_START" +%s)
        PROCESS_EPOCH=$(date -d "$PROCESS_START" +%s)
        
        # Calculate time difference in seconds
        TIME_DIFF=$((PROCESS_EPOCH - UPLOAD_EPOCH))
        
        # Alert if gap is more than 5 seconds
        if [ $TIME_DIFF -gt 5 ]; then
            echo "ALERT: Excessive delay ($TIME_DIFF seconds) between upload and processing for batch #$batch" >> "$ALERT_FILE"
        fi
    fi
done

# Count alerts
ALERT_COUNT=$(grep -c "ALERT:" "$ALERT_FILE")

if [ $ALERT_COUNT -gt 0 ]; then
    echo -e "\n$ALERT_COUNT parity issues detected."
    
    # Send alert if there are issues
    mail -s "CloudCrest Analytics: Log Parity Issues Detected" sre-team@cloudcrest.example < "$ALERT_FILE"
else
    echo -e "\nNo parity issues detected." >> "$ALERT_FILE"
fi

echo "Parity check complete. Results saved to $ALERT_FILE"
```

He made this script executable too:

```bash
$ chmod +x log_parity_check.sh
$ ./log_parity_check.sh
```

The parity check revealed several missing entries and sequence issues. To address these problems, Jin decided to implement a standardized logging library that all services could use.

He first checked the source code location of the analytics services:

```bash
$ ls -la /opt/analytics/src
```

He found several service implementations in different languages. Rather than modifying each one directly, Jin decided to create a standardized log format template and documentation.

```bash
$ vim /opt/analytics/README-logging.md
```

```markdown
# CloudCrest Analytics Logging Standards

## Overview
This document defines the standardized logging format for all CloudCrest analytics services.

## Log Format
All logs must follow this format:
```
[YYYY-MM-DD HH:MM:SS.sss] [SERVICE] [LEVEL] [COMPONENT] [CORRELATION_ID] Message
```

### Fields
- **Timestamp**: ISO-8601 format with milliseconds
- **Service**: Service name (UPLOAD, PROCESSING, ARCHIVER, API)
- **Level**: Log level (INFO, WARN, ERROR, DEBUG)
- **Component**: Component within the service
- **Correlation ID**: A unique identifier for tracking related events (batch ID, request ID)
- **Message**: The actual log message

## Implementation
Each service should use the provided logging library or wrapper.

## Example
```
[2025-04-13 10:15:32.456] [UPLOAD] [INFO] [FileHandler] [batch#46001] File received: user_data.csv
```
```

Next, Jin created a script to process incoming logs and enforce the standard format:

```bash
$ vim /opt/analytics/bin/log_standardizer.sh
```

```bash
#!/bin/bash
# Central log processing script
# Usage: echo "Log message" | log_standardizer.sh SERVICE LEVEL COMPONENT CORRELATION_ID

SERVICE=$1
LEVEL=$2
COMPONENT=$3
CORRELATION_ID=$4

# Read the log message from stdin
read -r MESSAGE

# Create the standardized log entry
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S.%3N')
LOG_ENTRY="[$TIMESTAMP] [$SERVICE] [$LEVEL] [$COMPONENT] [$CORRELATION_ID] $MESSAGE"

# Write to the appropriate log file
echo "$LOG_ENTRY" >> "/var/log/analytics-$SERVICE.log"

# For critical issues, also send to a central alert log
if [ "$LEVEL" == "ERROR" ] || [ "$LEVEL" == "FATAL" ]; then
    echo "$LOG_ENTRY" >> "/var/log/analytics/alerts/critical.log"
fi
```

He made the script executable and set appropriate permissions:

```bash
$ chmod +x /opt/analytics/bin/log_standardizer.sh
$ sudo chown analytics:analytics /opt/analytics/bin/log_standardizer.sh
```

To automate log management, Jin created a cron job for his log parity check:

```bash
$ crontab -e
```

Added:

```
# Run log standardization and parity check every hour
0 * * * * /home/jin/scripts/analytics/log_standardizer.sh
15 * * * * /home/jin/scripts/analytics/log_analyzer.sh
30 * * * * /home/jin/scripts/analytics/log_parity_check.sh
```

Finally, Jin wanted to create a script that would sanitize sensitive information from logs. He had noticed some logs contained authentication tokens and potentially sensitive data:

```bash
$ vim /home/jin/scripts/analytics/log_sanitizer.sh
```

```bash
#!/bin/bash
# log_sanitizer.sh - Created by Jin
# Sanitizes sensitive information from log files

LOG_DIR="/var/log"
SANITIZED_DIR="/var/log/sanitized"

mkdir -p "$SANITIZED_DIR"

# Patterns to sanitize
# - IP addresses
# - Authentication tokens
# - Email addresses
# - Credit card numbers
# - API keys

# Process each log file
for log_file in "$LOG_DIR"/analytics*.log; do
    base_name=$(basename "$log_file")
    sanitized_file="$SANITIZED_DIR/$base_name"
    
    # Create a sanitized copy
    cat "$log_file" | \
    # Sanitize IP addresses
    sed -r 's/([0-9]{1,3}\.){3}[0-9]{1,3}/[REDACTED_IP]/g' | \
    # Sanitize authentication tokens (Bearer or Auth followed by string)
    sed -r 's/(Bearer|Auth|Token|token)( |: | Token: | token: )([a-zA-Z0-9_.-]+)/\1\2[REDACTED_TOKEN]/g' | \
    # Sanitize email addresses
    sed -r 's/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}/[REDACTED_EMAIL]/g' | \
    # Sanitize credit card numbers (simple pattern)
    sed -r 's/[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}/[REDACTED_CC]/g' | \
    # Sanitize API keys (common formats)
    sed -r 's/api[_-]?key[=:]["'\'']?[a-zA-Z0-9]{16,}["'\'']/api_key=[REDACTED_API_KEY]/gi' \
    > "$sanitized_file"
    
    echo "Sanitized $log_file -> $sanitized_file"
done

echo "Log sanitization complete"
```

He made this script executable:

```bash
$ chmod +x /home/jin/scripts/analytics/log_sanitizer.sh
```

And added it to his crontab:

```bash
$ crontab -e
```

Added:

```
# Sanitize logs daily
0 0 * * * /home/jin/scripts/analytics/log_sanitizer.sh
```

With all these scripts in place, Jin wrote up a detailed handoff for Fatima in Dubai:

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

Jin took one last look at his scripts, satisfied with the organized approach to log management. As night fell in Seoul, he knew that in Dubai, Fatima would soon be starting her day, continuing the never-ending challenge of maintaining CloudCrest's complex infrastructure.

*[End of Day 5]*