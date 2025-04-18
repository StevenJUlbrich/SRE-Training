# Day 7: Mina's Network Integration

*08:00 WAT - Lagos, Nigeria*

Mina arrived at CloudCrest's Lagos office, a modern space tucked into the upper floors of a high-rise in Victoria Island's business district. Through the windows, she could see the morning traffic beginning to build on the streets below as the city awakened.

Her workspace was organized yet personal—dual monitors positioned just so, a small potted aloe plant, and a framed photo of her university robotics team. Known for her exceptional networking skills and meticulous documentation, Mina was the perfect team member to bring all the week's improvements together.

She pulled up Fatima's handoff while enjoying her morning tea:

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

"A dashboard would indeed be perfect," Mina said to herself. But first, she needed to confirm the overall system stability by checking the network connectivity and traffic patterns.

She connected to the analytics server:

```bash
$ ssh mina@analytics-prod-03
```

First, she wanted to verify the basic connectivity of the system:

```bash
$ ping -c 3 google.com
PING google.com (142.250.188.206) 56(84) bytes of data.
64 bytes from lhr48s09-in-f14.1e100.net (142.250.188.206): icmp_seq=1 ttl=128 time=14.3 ms
64 bytes from lhr48s09-in-f14.1e100.net (142.250.188.206): icmp_seq=2 ttl=128 time=14.2 ms
64 bytes from lhr48s09-in-f14.1e100.net (142.250.188.206): icmp_seq=3 ttl=128 time=14.5 ms

--- google.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 14.242/14.364/14.531/0.120 ms
```

Good, general internet connectivity was working. Next, she checked connectivity to other internal services:

```bash
$ ping -c 2 db-analytics-01
$ ping -c 2 api-gateway-03
$ ping -c 2 metrics-collector-02
```

All internal services responded properly. Now she needed to check which network interfaces were available and their configurations:

```bash
$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:1a:4b:16:01:5c brd ff:ff:ff:ff:ff:ff
    inet 10.0.3.45/24 brd 10.0.3.255 scope global eth0
       valid_lft forever preferred_lft forever
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:1a:4b:16:01:5d brd ff:ff:ff:ff:ff:ff
    inet 192.168.5.45/24 brd 192.168.5.255 scope global eth1
       valid_lft forever preferred_lft forever
```

The server had two network interfaces: eth0 for the internal network and eth1 for a management network. She checked the routing table to understand how traffic was being directed:

```bash
$ ip route show
default via 10.0.3.1 dev eth0 
10.0.3.0/24 dev eth0 proto kernel scope link src 10.0.3.45 
192.168.5.0/24 dev eth1 proto kernel scope link src 192.168.5.45
```

This confirmed the default route was through the primary interface. Next, she examined active network connections:

```bash
$ ss -tuln
Netid  State   Recv-Q  Send-Q   Local Address:Port    Peer Address:Port  Process
tcp    LISTEN  0       128      0.0.0.0:22            0.0.0.0:*
tcp    LISTEN  0       128      127.0.0.1:5432        0.0.0.0:*
tcp    LISTEN  0       128      0.0.0.0:8080          0.0.0.0:*
tcp    LISTEN  0       128      0.0.0.0:8081          0.0.0.0:*
tcp    LISTEN  0       128      127.0.0.1:9000        0.0.0.0:*
```

To get more detail about which processes owned these connections, she ran:

```bash
$ sudo ss -tulnp
Netid  State   Recv-Q  Send-Q   Local Address:Port    Peer Address:Port  Process
tcp    LISTEN  0       128      0.0.0.0:22            0.0.0.0:*          users:(("sshd",pid=1234,fd=3))
tcp    LISTEN  0       128      127.0.0.1:5432        0.0.0.0:*          users:(("postgres",pid=3210,fd=5))
tcp    LISTEN  0       128      0.0.0.0:8080          0.0.0.0:*          users:(("analytics-service",pid=9876,fd=6))
tcp    LISTEN  0       128      0.0.0.0:8081          0.0.0.0:*          users:(("upload-service",pid=5432,fd=8))
tcp    LISTEN  0       128      127.0.0.1:9000        0.0.0.0:*          users:(("processing-service",pid=4321,fd=7))
```

For a more detailed understanding of the network traffic, Mina checked the current connections:

```bash
$ sudo netstat -anp | grep EST
tcp        0      0 10.0.3.45:8080         10.0.2.156:49812      ESTABLISHED 9876/analytics-service
tcp        0      0 10.0.3.45:8081         10.0.2.201:52341      ESTABLISHED 5432/upload-service
tcp        0      0 10.0.3.45:22           192.168.150.25:49323  ESTABLISHED 1234/sshd
```

These were the current established connections to the server. Next, she wanted to understand the DNS resolution:

```bash
$ cat /etc/resolv.conf
nameserver 10.0.1.10
nameserver 10.0.1.11
search cloudcrest.internal
```

The server was using the internal DNS servers. She tested DNS resolution:

```bash
$ nslookup api-gateway-03
Server:         10.0.1.10
Address:        10.0.1.10#53

Name:   api-gateway-03.cloudcrest.internal
Address: 10.0.2.30
```

Everything looked consistent with the expected network configuration. Now, Mina wanted to verify that the analytics services could properly reach their dependencies. She wrote a simple connectivity test script:

```bash
$ vim /home/mina/scripts/connectivity_test.sh
```

```bash
#!/bin/bash
# connectivity_test.sh - Created by Mina
# Tests connectivity to all required services and APIs

LOG_FILE="/var/log/network/connectivity_$(date +%Y%m%d).log"
mkdir -p "$(dirname "$LOG_FILE")"

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
    echo "$1"
}

test_tcp_connection() {
    local host=$1
    local port=$2
    local description=$3
    
    nc -zv -w 3 "$host" "$port" &>/dev/null
    if [ $? -eq 0 ]; then
        log "✓ SUCCESS: Connection to $description ($host:$port) successful"
    else
        log "✗ FAILURE: Could not connect to $description ($host:$port)"
    fi
}

test_http_connection() {
    local url=$1
    local description=$2
    
    status_code=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 "$url")
    if [ "$status_code" -ge 200 ] && [ "$status_code" -lt 300 ]; then
        log "✓ SUCCESS: HTTP connection to $description ($url) returned status $status_code"
    else
        log "✗ FAILURE: HTTP connection to $description ($url) returned status $status_code"
    fi
}

log "Starting connectivity tests..."

# Test internal service connectivity
test_tcp_connection "db-analytics-01" 5432 "Analytics Database"
test_tcp_connection "api-gateway-03" 443 "API Gateway"
test_tcp_connection "metrics-collector-02" 8125 "Metrics Collector"
test_tcp_connection "cache-server-01" 6379 "Redis Cache"

# Test external API connectivity
test_http_connection "https://api.analytics-partner.com/v1/status" "Partner API"
test_http_connection "https://metrics.analytics-partner.com/health" "Metrics API"

# Test DNS resolution
log "Testing DNS resolution..."
for host in "db-analytics-01" "api-gateway-03" "metrics-collector-02" "cache-server-01"; do
    if nslookup "$host" &>/dev/null; then
        log "✓ SUCCESS: DNS resolution for $host works"
    else
        log "✗ FAILURE: DNS resolution for $host failed"
    fi
done

log "Connectivity tests completed."
```

She made the script executable and ran it:

```bash
$ chmod +x /home/mina/scripts/connectivity_test.sh
$ ./home/mina/scripts/connectivity_test.sh
```

All the connection tests passed, confirming that the networking aspect of the system was healthy. Now, she wanted to check if any files were being transferred via SCP or similar tools:

```bash
$ sudo lsof | grep -E 'scp|sftp'
```

No output meant no file transfers were currently in progress.

To test secure file transfer capabilities, Mina created a test file:

```bash
$ echo "Test file for SCP transfer" > /tmp/test_transfer.txt
```

She securely copied it to another server and back:

```bash
$ scp /tmp/test_transfer.txt mina@backup-server-01:/tmp/
$ scp mina@backup-server-01:/tmp/test_transfer.txt /tmp/test_received.txt
```

Both transfers completed successfully. Mina removed the test files afterward:

```bash
$ rm /tmp/test_transfer.txt /tmp/test_received.txt
$ ssh mina@backup-server-01 "rm /tmp/test_transfer.txt"
```

With the basic networking checks completed and functioning properly, Mina moved on to her main task: creating a comprehensive monitoring dashboard that would integrate all the improvements the team had made throughout the week.

She first studied the various logs and metrics sources that were now available:

1. Jin's standardized log format
2. Aanya's directory structure
3. Luis's process hierarchy improvements
4. Fatima's process monitoring script

To bring it all together, Mina decided to implement a network-accessible dashboard using SSH tunneling to securely expose the metrics while keeping them internal to CloudCrest's network.

First, she set up a simple web server on the analytics machine to host the dashboard:

```bash
$ sudo apt update && sudo apt install -y nginx
$ sudo systemctl start nginx
$ sudo systemctl enable nginx
```

She created a folder for the dashboard files:

```bash
$ sudo mkdir -p /var/www/html/dashboard
$ sudo chown mina:mina /var/www/html/dashboard
```

Next, Mina wrote a script to collect all the metrics and generate a dashboard:

```bash
$ vim /home/mina/scripts/generate_dashboard.sh
```

```bash
#!/bin/bash
# generate_dashboard.sh - Created by Mina
# Collects all metrics and generates a comprehensive dashboard

DASHBOARD_DIR="/var/www/html/dashboard"
METRICS_DIR="$DASHBOARD_DIR/metrics"
GRAPHS_DIR="$DASHBOARD_DIR/graphs"

mkdir -p "$METRICS_DIR" "$GRAPHS_DIR"

# Get current system status
generate_system_status() {
    {
        echo "# System Status as of $(date)"
        echo "## CPU Usage"
        top -bn1 | head -n 5
        
        echo -e "\n## Memory Usage"
        free -h
        
        echo -e "\n## Disk Usage"
        df -h
        
        echo -e "\n## Network Interfaces"
        ip -br addr show
    } > "$METRICS_DIR/system_status.md"
}

# Generate network metrics
generate_network_metrics() {
    {
        echo "# Network Metrics as of $(date)"
        echo "## Active Connections"
        ss -tuln
        
        echo -e "\n## Connection Count by State"
        ss -s
        
        echo -e "\n## Recent Connection Attempts"
        grep "connection" /var/log/syslog | tail -10
    } > "$METRICS_DIR/network_metrics.md"
}

# Generate process metrics from Fatima's script
generate_process_metrics() {
    {
        echo "# Process Metrics as of $(date)"
        echo "## Top CPU Consumers"
        ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head -11
        
        echo -e "\n## Top Memory Consumers"
        ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%mem | head -11
        
        echo -e "\n## Process Hierarchy"
        ps -ef --forest | grep -E 'analytics|upload|processing' | grep -v grep
    } > "$METRICS_DIR/process_metrics.md"
}

# Generate log metrics from Jin's logs
generate_log_metrics() {
    {
        echo "# Log Metrics as of $(date)"
        echo "## Log Counts by Service"
        grep -o 'UPLOAD\|PROCESSING\|ARCHIVER\|API' /var/log/analytics/unified/unified_$(date +%Y%m%d).log | sort | uniq -c
        
        echo -e "\n## Error Count by Service (Last 24 Hours)"
        grep -i 'error' /var/log/analytics/unified/unified_$(date +%Y%m%d).log | grep -o 'UPLOAD\|PROCESSING\|ARCHIVER\|API' | sort | uniq -c
    } > "$METRICS_DIR/log_metrics.md"
}

# Generate file metrics from Aanya's structure
generate_file_metrics() {
    {
        echo "# File Metrics as of $(date)"
        echo "## Directory Sizes"
        du -sh /var/app/uploads/* | sort -hr
        
        echo -e "\n## Recent File Changes"
        find /var/app/uploads -type f -mmin -60 | wc -l
        echo "files changed in the last hour"
        
        echo -e "\n## File Counts by Directory"
        echo "Incoming: $(find /var/app/uploads/incoming -type f | wc -l) files"
        echo "Processing: $(find /var/app/uploads/processing -type f | wc -l) files"
        echo "Archive: $(find /var/app/uploads/archive -type f | wc -l) files"
    } > "$METRICS_DIR/file_metrics.md"
}

# Generate main index.html
generate_index() {
    cat > "$DASHBOARD_DIR/index.html" << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="60">
    <title>CloudCrest Analytics Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }
        .header { background: #2c3e50; color: white; padding: 20px; margin-bottom: 20px; }
        .dashboard { display: flex; flex-wrap: wrap; }
        .card { background: white; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                margin: 10px; padding: 15px; min-width: 300px; flex: 1; }
        .status-ok { color: green; }
        .status-warning { color: orange; }
        .status-critical { color: red; }
        pre { background: #f9f9f9; padding: 10px; border-radius: 3px; overflow-x: auto; }
    </style>
</head>
<body>
    <div class="header">
        <h1>CloudCrest Analytics Dashboard</h1>
        <p>Last Updated: $(date)</p>
    </div>
    
    <div class="dashboard">
        <div class="card">
            <h2>System Status</h2>
            <pre>$(cat "$METRICS_DIR/system_status.md")</pre>
        </div>
        
        <div class="card">
            <h2>Network Status</h2>
            <pre>$(cat "$METRICS_DIR/network_metrics.md")</pre>
        </div>
        
        <div class="card">
            <h2>Process Status</h2>
            <pre>$(cat "$METRICS_DIR/process_metrics.md")</pre>
        </div>
        
        <div class="card">
            <h2>Log Analysis</h2>
            <pre>$(cat "$METRICS_DIR/log_metrics.md")</pre>
        </div>
        
        <div class="card">
            <h2>File Storage</h2>
            <pre>$(cat "$METRICS_DIR/file_metrics.md")</pre>
        </div>
    </div>
    
    <div class="footer">
        <p>CloudCrest SRE Team - Follow-the-Sun Model</p>
    </div>
</body>
</html>
EOF
}

# Main execution
generate_system_status
generate_network_metrics
generate_process_metrics
generate_log_metrics
generate_file_metrics
generate_index

echo "Dashboard generated at $DASHBOARD_DIR/index.html"
```

She made the script executable and set up a cron job to run it every 5 minutes:

```bash
$ chmod +x /home/mina/scripts/generate_dashboard.sh
$ crontab -e
```

Added:

```
# Generate the dashboard every 5 minutes
*/5 * * * * /home/mina/scripts/generate_dashboard.sh
```

For the initial generation, she ran the script manually:

```bash
$ /home/mina/scripts/generate_dashboard.sh
```

Now she needed to set up secure access to the dashboard. Instead of exposing it directly to the internet, Mina configured it to only be accessible via SSH tunneling:

```bash
$ sudo vim /etc/nginx/sites-available/dashboard
```

```
server {
    listen 127.0.0.1:8090;
    server_name localhost;
    
    location / {
        root /var/www/html/dashboard;
        index index.html;
    }
}
```

She enabled the site and reloaded Nginx:

```bash
$ sudo ln -s /etc/nginx/sites-available/dashboard /etc/nginx/sites-enabled/
$ sudo nginx -t
$ sudo systemctl reload nginx
```

To access the dashboard from outside the server, Mina created instructions for the team:

```bash
$ vim /home/mina/dashboard_access.txt
```

```
# CloudCrest Analytics Dashboard Access Instructions

## Secure Access via SSH Tunnel

To access the dashboard securely, create an SSH tunnel with:

    ssh -L 8090:localhost:8090 username@analytics-prod-03

Then navigate to http://localhost:8090 in your web browser.

This ensures the dashboard is only accessible to authorized team members with SSH access.

For any questions, contact the SRE team.

- Mina
```

She sent this to the team via email.

To complete her work, Mina created a detailed documentation file summarizing all the improvements the team had made throughout the week:

```bash
$ vim /home/mina/sre_improvements.md
```

```markdown
# CloudCrest Analytics Platform Improvements
*Compiled by Mina - April 13, 2025*

## Overview
This document summarizes the improvements made to the analytics platform by the 
SRE team over the past week using our follow-the-sun model.

## Day 1: Initial Issue Discovery (Taylor, USA)
- Identified runaway logging in the analytics service
- Found test script running in production with debug mode enabled
- Fixed immediate disk space issues

## Day 2: Log Investigation (Noah, Australia)
- Discovered mixed ownership in log files
- Found inconsistent naming patterns
- Identified permission denied errors in uploads directory

## Day 3: File Management Solutions (Aanya, India)
- Implemented proper directory structure (incoming/processing/archive)
- Set appropriate permissions and ownership
- Added setgid bit to directories to maintain consistent group ownership
- Created automated maintenance script

## Day 4: Process Permissions Resolution (Luis, Spain)
- Discovered process forking issues and sudo misuse
- Restricted sudo privileges to specific paths
- Modified scripts to use proper directory permissions
- Added process auditing and monitoring

## Day 5: Text Processing Improvements (Jin, South Korea)
- Standardized logging formats across all services
- Implemented log parity checks
- Created a log sanitization system to remove sensitive data
- Added alerts for sequence inconsistencies

## Day 6: Process Monitoring Security (Fatima, UAE)
- Fixed SSL verification (previously disabled)
- Implemented secure log rotation with proper retention
- Created comprehensive process monitoring
- Implemented restricted user policy for log access

## Day 7: Network Integration (Mina, Nigeria)
- Verified network connectivity to all services
- Created secure dashboard for monitoring system health
- Implemented SSH tunneling for secure dashboard access
- Documented all improvements for future reference

## Ongoing Maintenance
- All logs are now properly rotated and archived
- Process monitoring runs every 15 minutes
- Dashboard updates every 5 minutes
- Log parity checks run hourly
- Maintenance script runs daily at 2 AM

## Next Steps
The team should continue to monitor the dashboard for any anomalies and further refine
the automation processes. Consider implementing centralized logging and more sophisticated
alerting based on the metrics we now have available.
```

Before finishing her day, Mina reviewed the complete system one more time to ensure everything was working correctly. She checked the dashboard, verified all scripts were running as scheduled, and confirmed that no new issues had appeared.

Satisfied with her work, Mina prepared a handoff message for Taylor, who would start her shift in a few hours in the US:

> **@Taylor:** I've completed the integration of all our team's improvements from this week. The analytics platform is now stable, secure, and well-monitored:
> 
> 1. All networking connections are verified and functional
> 2. Created a comprehensive dashboard that shows system health, available via SSH tunnel
> 3. Verified that all scheduled maintenance scripts are running properly
> 4. Created detailed documentation of all improvements
> 
> The system has come a long way since your first day! The runaway logs that you discovered led us to uncover and fix several deeper issues. The platform is now in much better shape, with proper permissions, process management, log standardization, and monitoring.
> 
> I've attached instructions for accessing the dashboard in an email. Let me know if you have any questions when you start your shift.

As the afternoon sun shone over Lagos, Mina reflected on how the team had worked together across time zones to solve a complex set of interconnected issues. The follow-the-sun model had allowed them to continuously improve the system without any downtime, with each team member building on the work of those before them.

Soon, Taylor would be starting her day in the US, completing the global circle of SREs who kept CloudCrest's infrastructure running smoothly around the clock and around the world.

*[End of Day 7]*