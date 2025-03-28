# 🚀 **Day 7: Networking Basics – Essential Tools and Commands for SREs**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 6:**

Yesterday, you learned about Linux process management and system monitoring. You mastered commands for viewing running processes (`ps`, `top`, `htop`), controlling process execution (`kill`, `bg`, `fg`), and gathering system information (`uname`, `df`, `du`, `free`). These skills are essential for understanding what's happening on your system and managing resources effectively.

### 📅 **Today's Topics and Importance:**

Today we'll explore **Linux networking fundamentals** that are crucial for SREs. Network connectivity is the backbone of modern distributed systems, and SREs must be proficient with networking tools to:

- Troubleshoot connectivity issues between services
- Monitor network performance and latency
- Secure network communications
- Configure network interfaces
- Diagnose routing problems
- Transfer files securely between systems

Without these skills, you'd be unable to effectively manage distributed applications or diagnose many common production issues.

### 🎯 **Learning Objectives:**

By the end of Day 7, you will be able to:

- Test network connectivity using `ping`, `traceroute`, and `mtr`
- View and configure network interfaces with `ip` and `ifconfig`
- Analyze network connections using `netstat` and `ss`
- Securely connect to remote systems with `ssh`
- Transfer files securely using `scp` and `rsync`
- Troubleshoot common networking issues in production environments

---

## 📚 **Core Concepts Explained**

### **Networking Fundamentals for SREs**

Modern systems are highly interconnected, making networking knowledge indispensable for SREs. Here's why these concepts matter:

- **Connectivity Verification**: Before complex troubleshooting, you need to confirm basic network connectivity
- **Network Configuration**: SREs must understand how interfaces, IP addresses, and routing work
- **Connection Analysis**: Identifying which processes are using network resources helps diagnose issues
- **Secure Remote Access**: SSH is the primary method for accessing and managing remote systems
- **Data Transfer**: Moving files securely between systems is a common operational task

Understanding these fundamentals allows you to quickly identify whether a problem is network-related or application-related, significantly reducing mean time to resolution (MTTR) during incidents.

### **The OSI Model: A Brief Overview**

While not a direct command-line tool, the OSI (Open Systems Interconnection) model provides a conceptual framework for understanding networking issues. As an SRE, you'll often need to determine which "layer" a problem exists in:

1. **Physical Layer**: Physical connections, cables
2. **Data Link Layer**: MAC addresses, switches
3. **Network Layer**: IP addresses, routing
4. **Transport Layer**: TCP/UDP, ports
5. **Session Layer**: Sessions between applications
6. **Presentation Layer**: Data formatting, encryption
7. **Application Layer**: HTTP, DNS, SMTP

The commands we'll learn today operate primarily at layers 3 (Network), 4 (Transport), and 7 (Application).

---

## 💻 **Commands to Learn Today**

### **1. Basic Connectivity Testing (`ping`, `traceroute`, `mtr`)**

#### **`ping` – Test Basic Connectivity**

**Purpose**: Verify reachability of hosts and measure round-trip time.

**SRE Context**: Often the first tool used during connectivity troubleshooting to determine if a host is reachable and responsive.

**Syntax:**

```bash
ping [options] destination
```

**Common options:**

- `-c count`: Send a specific number of packets
- `-i interval`: Seconds between packets
- `-w deadline`: Timeout in seconds for the entire operation

**Examples:**

Check if a host is reachable:

```bash
[sre@prod-server ~]$ ping -c 4 google.com
PING google.com (142.250.190.78) 56(84) bytes of data.
64 bytes from lax31s18-in-f14.1e100.net (142.250.190.78): icmp_seq=1 ttl=119 time=15.2 ms
64 bytes from lax31s18-in-f14.1e100.net (142.250.190.78): icmp_seq=2 ttl=119 time=15.1 ms
64 bytes from lax31s18-in-f14.1e100.net (142.250.190.78): icmp_seq=3 ttl=119 time=15.3 ms
64 bytes from lax31s18-in-f14.1e100.net (142.250.190.78): icmp_seq=4 ttl=119 time=15.0 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 15.011/15.150/15.253/0.097 ms
```

Test connectivity to an internal service:

```bash
[sre@prod-server ~]$ ping -c 3 -w 2 db-server.internal
PING db-server.internal (10.0.0.15) 56(84) bytes of data.
64 bytes from db-server.internal (10.0.0.15): icmp_seq=1 ttl=64 time=0.5 ms
64 bytes from db-server.internal (10.0.0.15): icmp_seq=2 ttl=64 time=0.6 ms
64 bytes from db-server.internal (10.0.0.15): icmp_seq=3 ttl=64 time=0.5 ms

--- db-server.internal ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 0.458/0.519/0.578/0.049 ms
```

#### **`traceroute` – Display Network Path**

**Purpose**: Show the network path packets take to reach a destination.

**SRE Context**: Helps identify where in the network path packets are being delayed or dropped.

**Syntax:**

```bash
traceroute [options] destination
```

**Common options:**

- `-n`: Don't resolve hostnames (faster)
- `-T`: Use TCP SYN packets instead of UDP
- `-w timeout`: Wait time for a response

**Examples:**

Trace the route to a public website:

```bash
[sre@prod-server ~]$ traceroute -n google.com
traceroute to google.com (142.250.190.78), 30 hops max, 60 byte packets
 1  10.0.0.1  0.456 ms  0.412 ms  0.401 ms
 2  192.168.1.1  1.234 ms  1.201 ms  1.175 ms
 3  203.0.113.1  5.234 ms  5.201 ms  5.175 ms
 4  203.0.113.10  10.234 ms  10.201 ms  10.175 ms
 5  172.16.0.1  15.234 ms  15.201 ms  15.175 ms
 6  * * *
 7  142.250.190.78  20.234 ms  20.201 ms  20.175 ms
```

#### **`mtr` – Combine Ping and Traceroute**

**Purpose**: Provide continuous statistical information about each hop in a network path.

**SRE Context**: Gives a more comprehensive view of network quality over time than ping or traceroute alone.

**Syntax:**

```bash
mtr [options] destination
```

**Common options:**

- `-n`: Don't resolve hostnames
- `-r`: Report mode (text output instead of interactive)
- `-c count`: Number of pings to send to each hop
- `-w`: Wide report mode with hostnames and IPs

**Examples:**

Generate network path report:

```bash
[sre@prod-server ~]$ mtr -n -r -c 10 google.com
Start: 2023-10-16T14:30:42+0000
HOST: prod-server              Loss%   Snt   Last   Avg  Best  Wrst StDev
  1. 10.0.0.1                   0.0%    10    0.5   0.5   0.4   0.7   0.1
  2. 192.168.1.1                0.0%    10    1.2   1.3   1.1   1.5   0.1
  3. 203.0.113.1                0.0%    10    5.2   5.3   5.1   5.7   0.2
  4. 203.0.113.10               0.0%    10   10.2  10.3  10.1  10.7   0.2
  5. 172.16.0.1                 0.0%    10   15.2  15.3  15.1  15.7   0.2
  6. ???                       100.0%    10    0.0   0.0   0.0   0.0   0.0
  7. 142.250.190.78             0.0%    10   20.2  20.3  20.1  20.7   0.2
```

### **2. Network Interface Management (`ip`, `ifconfig`)**

#### **`ip` – Modern Network Interface Tool**

**Purpose**: Configure and display network interfaces, routing, and address information.

**SRE Context**: Primary tool for viewing and configuring network settings in modern Linux distributions.

**Syntax:**

```bash
ip [options] object command
```

**Common objects:**

- `addr`: IP addresses
- `link`: Network devices
- `route`: Routing table
- `neigh`: ARP or NDISC cache

**Examples:**

Display all interfaces:

```bash
[sre@prod-server ~]$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 52:54:00:a1:b2:c3 brd ff:ff:ff:ff:ff:ff
    inet 10.0.0.15/24 brd 10.0.0.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::5054:ff:fea1:b2c3/64 scope link 
       valid_lft forever preferred_lft forever
```

View routing table:

```bash
[sre@prod-server ~]$ ip route
default via 10.0.0.1 dev eth0 proto static 
10.0.0.0/24 dev eth0 proto kernel scope link src 10.0.0.15 
169.254.0.0/16 dev eth0 scope link metric 1002
```

View ARP cache (MAC address to IP mappings):

```bash
[sre@prod-server ~]$ ip neigh
10.0.0.1 dev eth0 lladdr 00:50:56:c0:00:01 REACHABLE
10.0.0.10 dev eth0 lladdr 00:50:56:c0:00:0a STALE
```

#### **`ifconfig` – Traditional Interface Configuration Tool**

**Purpose**: Display and configure network interfaces (older but still common).

**SRE Context**: While gradually being replaced by `ip`, many tutorials and existing scripts still use `ifconfig`.

**Syntax:**

```bash
ifconfig [interface] [options]
```

**Examples:**

Display all interfaces:

```bash
[sre@prod-server ~]$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.15  netmask 255.255.255.0  broadcast 10.0.0.255
        inet6 fe80::5054:ff:fea1:b2c3  prefixlen 64  scopeid 0x20<link>
        ether 52:54:00:a1:b2:c3  txqueuelen 1000  (Ethernet)
        RX packets 1234567  bytes 906543210 (864.5 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 765432  bytes 123456789 (117.7 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 54321  bytes 12345678 (11.7 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 54321  bytes 12345678 (11.7 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

### **3. Connection Analysis (`netstat`, `ss`)**

#### **`netstat` – Network Statistics**

**Purpose**: Display network connections, routing tables, interface statistics, etc.

**SRE Context**: Helps identify which processes are using network connections and which ports are in use.

**Syntax:**

```bash
netstat [options]
```

**Common options:**

- `-t`: TCP connections
- `-u`: UDP connections
- `-l`: Listening sockets
- `-p`: Show process using the socket
- `-n`: Don't resolve names (faster)
- `-a`: Show all sockets

**Examples:**

View listening TCP ports and their associated processes:

```bash
[sre@prod-server ~]$ sudo netstat -tlnp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1234/sshd
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      5678/postfix
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      9012/nginx
tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN      9012/nginx
```

View all active connections:

```bash
[sre@prod-server ~]$ netstat -an
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
tcp        0      0 10.0.0.15:22            10.0.0.100:54321        ESTABLISHED
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN
tcp        0      0 10.0.0.15:80            10.0.0.101:12345        ESTABLISHED
udp        0      0 0.0.0.0:123             0.0.0.0:*
```

#### **`ss` – Socket Statistics (Modern Alternative)**

**Purpose**: Similar to netstat but faster and with more features.

**SRE Context**: Preferred over `netstat` for performance and additional information.

**Syntax:**

```bash
ss [options]
```

**Common options:**

- `-t`: TCP sockets
- `-u`: UDP sockets
- `-l`: Listening sockets
- `-p`: Show process using the socket
- `-n`: Don't resolve names
- `-a`: All sockets
- `-s`: Summary statistics

**Examples:**

View listening ports:

```bash
[sre@prod-server ~]$ sudo ss -tlnp
State      Recv-Q Send-Q Local Address:Port               Peer Address:Port
LISTEN     0      128    *:22                           *:*                 users:(("sshd",pid=1234,fd=3))
LISTEN     0      100    127.0.0.1:25                   *:*                 users:(("postfix",pid=5678,fd=13))
LISTEN     0      128    *:80                           *:*                 users:(("nginx",pid=9012,fd=6))
LISTEN     0      128    *:443                          *:*                 users:(("nginx",pid=9012,fd=7))
```

View established connections:

```bash
[sre@prod-server ~]$ ss -tn state established
State      Recv-Q Send-Q Local Address:Port               Peer Address:Port
ESTAB      0      0      10.0.0.15:22                  10.0.0.100:54321
ESTAB      0      0      10.0.0.15:80                  10.0.0.101:12345
```

View summary statistics:

```bash
[sre@prod-server ~]$ ss -s
Total: 290 (kernel 312)
TCP:   12 (estab 2, closed 0, orphaned 0, synrecv 0, timewait 0/0), ports 9

Transport Total     IP        IPv6
*         312       -         -
RAW       0         0         0
UDP       4         3         1
TCP       12        10        2
INET      16        13        3
FRAG      0         0         0
```

### **4. Remote Access and File Transfer (`ssh`, `scp`, `rsync`)**

#### **`ssh` – Secure Shell**

**Purpose**: Create secure encrypted connections to remote systems.

**SRE Context**: Primary method for remote server administration, used constantly in daily SRE work.

**Syntax:**

```bash
ssh [options] [user@]hostname [command]
```

**Common options:**

- `-i identity_file`: Use a specific private key
- `-p port`: Connect to a specific port
- `-L local_port:host:remote_port`: Local port forwarding
- `-R remote_port:host:local_port`: Remote port forwarding
- `-f`: Background mode
- `-N`: Don't execute a remote command (useful with port forwarding)

**Examples:**

Connect to a remote server:

```bash
[sre@prod-server ~]$ ssh admin@app-server-prod-1
admin@app-server-prod-1's password: 
Last login: Mon Oct 16 10:15:20 2023 from 10.0.0.15
[admin@app-server-prod-1 ~]$
```

Connect with a specific key:

```bash
[sre@prod-server ~]$ ssh -i ~/.ssh/prod_key.pem admin@app-server-prod-2
Last login: Mon Oct 16 11:30:45 2023 from 10.0.0.15
[admin@app-server-prod-2 ~]$
```

Execute a remote command without logging in:

```bash
[sre@prod-server ~]$ ssh admin@app-server-prod-1 "df -h | grep /data"
/dev/xvdb        500G  123G  377G  25% /data
```

Set up a tunnel to access a service behind a firewall:

```bash
[sre@prod-server ~]$ ssh -L 8080:internal-app:80 admin@jump-host -N -f
```

#### **`scp` – Secure Copy**

**Purpose**: Securely copy files between hosts over SSH.

**SRE Context**: Used for transferring configuration files, logs, backup data, and other files between systems.

**Syntax:**

```bash
scp [options] [[user@]src_host:]file1 [[user@]dest_host:]file2
```

**Common options:**

- `-r`: Recursive copy (directories)
- `-p`: Preserve file attributes
- `-i identity_file`: Use a specific private key
- `-P port`: Specify SSH port

**Examples:**

Copy a file to a remote server:

```bash
[sre@prod-server ~]$ scp config.yaml admin@app-server-prod-1:/etc/app/
config.yaml                                     100%  1234     2.1MB/s   00:00
```

Copy a file from a remote server:

```bash
[sre@prod-server ~]$ scp admin@app-server-prod-1:/var/log/app/error.log ./
error.log                                       100%  5432     3.2MB/s   00:01
```

Copy an entire directory recursively:

```bash
[sre@prod-server ~]$ scp -r config_files admin@app-server-prod-1:/etc/app/
config_files/main.yaml                          100%  1234     2.1MB/s   00:00
config_files/db.yaml                            100%  3456     2.8MB/s   00:01
config_files/cache.yaml                         100%  2345     2.5MB/s   00:00
```

#### **`rsync` – Remote Sync**

**Purpose**: Synchronize files and directories between locations efficiently.

**SRE Context**: More efficient than `scp` for transferring large amounts of data or keeping directories in sync.

**Syntax:**

```bash
rsync [options] source destination
```

**Common options:**

- `-a`: Archive mode (preserves permissions, timestamps, etc.)
- `-v`: Verbose output
- `-z`: Compress data during transfer
- `--delete`: Delete files in destination that don't exist in source
- `-n` or `--dry-run`: Show what would be transferred without actually transferring

**Examples:**

Synchronize local directory to remote server:

```bash
[sre@prod-server ~]$ rsync -avz config_files/ admin@app-server-prod-1:/etc/app/config/
sending incremental file list
main.yaml
db.yaml
cache.yaml

sent 6789 bytes  received 123 bytes  4608.00 bytes/sec
total size is 7045  speedup is 1.02
```

Synchronize from remote to local with deletion:

```bash
[sre@prod-server ~]$ rsync -avz --delete admin@app-server-prod-1:/var/log/app/ ./app_logs/
receiving incremental file list
deleting old_error.log
error.log
access.log
debug.log

received 543210 bytes  sent 987 bytes  181399.00 bytes/sec
total size is 542100  speedup is 0.99
```

Perform a dry run to see what would change:

```bash
[sre@prod-server ~]$ rsync -avz --delete --dry-run config_files/ admin@app-server-prod-1:/etc/app/config/
sending incremental file list
main.yaml
db.yaml
would delete cache.yaml

sent 123 bytes  received 45 bytes  112.00 bytes/sec
total size is 3456  speedup is 20.57
```

---

## 🔍 **SRE Perspective: Common Networking Tasks**

### **1. Service Connectivity Validation**

When a service is reported as unavailable, follow these steps:

```bash
# Step 1: Check if the host is reachable
ping -c 3 service-host.example.com

# Step 2: Check if the specific port is open
nc -zv service-host.example.com 8080

# Step 3: Check if the service process is running and listening
ssh admin@service-host.example.com "sudo ss -tlnp | grep 8080"

# Step 4: Check the service logs
ssh admin@service-host.example.com "sudo tail -n 50 /var/log/myservice/error.log"

# Step 5: Test basic functionality
curl -v http://service-host.example.com:8080/health
```

### **2. Network Performance Monitoring**

For investigating latency issues:

```bash
# Continuous ping to monitor stability
ping -i 0.2 -c 1000 destination | tee ping_results.txt

# Analyze ping statistics for patterns
grep "time=" ping_results.txt | cut -d "=" -f 4 | cut -d " " -f 1 > latencies.txt
sort -n latencies.txt | awk '{sum+=$1; cnt++} END {printf "Min: %s\nMax: %s\nAvg: %.2f\nMedian: %s\n", $1, $(NR), sum/cnt, (NR%2==1)?$(int(NR/2)+1):($(int(NR/2))+$(int(NR/2)+1))/2}'

# Use mtr for detailed path analysis
mtr -rwc 50 destination > mtr_report.txt
```

### **3. Distributed Service Debugging**

In microservices environments, network tools help trace request flows:

```bash
# Step 1: Identify which services are involved
grep "request-id: abc123" /var/log/*/app*.log

# Step 2: Check connections between them
ss -tnp | grep service2

# Step 3: Check for network issues between services
mtr -n -r -c 10 service2-host > path_analysis.txt

# Step 4: Monitor traffic patterns
sudo tcpdump -i eth0 host service2-host -n
```

---

## 🎯 **Practical Exercise: Network Troubleshooting Scenario**

Let's practice a realistic SRE networking scenario. In this exercise, we'll simulate troubleshooting a web application that's experiencing connectivity issues.

Imagine you're on call and receive an alert: "Web application is returning 502 Bad Gateway errors."

Here's how you would systematically troubleshoot this issue:

1. **Check Basic Connectivity**

   First, verify connectivity to the web server:

   ```bash
   # Connect to your jump host or bastion host
   ssh jump-host.example.com
   
   # From there, test connectivity to the web server
   ping -c 3 web-server.internal
   ```

2. **Verify Service Status**

   Check if the web server (e.g., Nginx) is running:

   ```bash
   ssh web-server.internal "sudo systemctl status nginx"
   ```

3. **Check Open Ports**

   Verify that the web server is listening on the expected ports:

   ```bash
   ssh web-server.internal "sudo ss -tlnp | grep nginx"
   ```

4. **Examine Web Server Logs**

   Look for errors in the web server logs:

   ```bash
   ssh web-server.internal "sudo tail -n 50 /var/log/nginx/error.log"
   ```

5. **Check Connectivity to Backend Services**

   If the web server is a reverse proxy, verify it can reach the backend application:

   ```bash
   ssh web-server.internal "ping -c 3 app-server.internal"
   ssh web-server.internal "curl -I http://app-server.internal:8080/health"
   ```

6. **Check the Backend Application**

   Verify the application server is running:

   ```bash
   ssh app-server.internal "sudo systemctl status app-service"
   ssh app-server.internal "sudo ss -tlnp | grep 8080"
   ssh app-server.internal "sudo tail -n 50 /var/log/app-service/app.log"
   ```

7. **Check Database Connectivity**

   If the application depends on a database, check connectivity:

   ```bash
   ssh app-server.internal "ping -c 3 db-server.internal"
   ssh app-server.internal "nc -zv db-server.internal 5432"
   ```

8. **Document Findings and Resolution**

   Create a summary of your investigation:

   ```bash
   # Create a report directory
   mkdir -p ~/incident_reports/502_errors_$(date +%Y%m%d)
   
   # Copy relevant logs
   scp web-server.internal:/var/log/nginx/error.log ~/incident_reports/502_errors_$(date +%Y%m%d)/
   scp app-server.internal:/var/log/app-service/app.log ~/incident_reports/502_errors_$(date +%Y%m%d)/
   
   # Document steps taken and resolution
   echo "# 502 Bad Gateway Incident - $(date)" > ~/incident_reports/502_errors_$(date +%Y%m%d)/README.md
   echo "## Investigation Steps" >> ~/incident_reports/502_errors_$(date +%Y%m%d)/README.md
   # Add your steps and findings
   ```

The above exercise follows a methodical approach to network troubleshooting, starting with basic connectivity and working through the service stack to identify the root cause of the issue.

---

## 📝 **Quiz: Networking Essentials for SREs**

Test your understanding of today's material:

1. You're responding to an alert that your web service is unreachable. Which command would you use first to check if the server is reachable at the network level?
   - a) `ssh web-server`
   - b) `ping web-server`
   - c) `traceroute web-server`
   - d) `netstat -an`

2. During a performance investigation, you need to identify which process is listening on port 3306 (MySQL). Which command would be most appropriate?

   ```bash
   # Fill in the blank
   sudo _______ | grep 3306
   ```

3. You need to set up a secure tunnel to access a database that's only available on the internal network. Which SSH command would accomplish this?
   - a) `ssh -L 8080:localhost:3306 user@jump-host`
   - b) `ssh -R 3306:db-server:3306 user@jump-host`
   - c) `ssh -L 3306:db-server:3306 user@jump-host`
   - d) `ssh -t 3306:db-server:3306 user@jump-host`

4. To synchronize a configuration directory to multiple servers while ensuring files deleted locally are also removed from the servers, which command would you use?
   - a) `scp -r config_dir/* server:/etc/app/`
   - b) `rsync -avz config_dir/ server:/etc/app/`
   - c) `rsync -avz --delete config_dir/ server:/etc/app/`
   - d) `rsync -avz --backup config_dir/ server:/etc/app/`

5. You're investigating network latency between your application server and database server. Which command would provide the most comprehensive view of the network path including latency statistics?
   - a) `ping db-server`
   - b) `traceroute db-server`
   - c) `mtr -r db-server`
   - d) `ss -t`

---

## ❓ **FAQ for SREs: Networking Edition**

**Q1: How can I determine if a network issue is within my infrastructure or external?**

**A:** Use a systematic approach to isolate the problem:

1. Test connectivity from multiple points in your network:

   ```bash
   # From your application server
   ping external-service.com
   
   # From a different data center or cloud region
   ssh dc2-server "ping external-service.com"
   
   # From outside your network entirely (if possible)
   curl -Is https://downforeveryoneorjustme.com/external-service.com
   ```

2. Use traceroute to identify where the path breaks:

   ```bash
   traceroute -n external-service.com
   ```

3. Check your edge routers and firewalls for issues:

   ```bash
   ssh edge-router "show interface errors"
   ssh firewall "show session table | include external-service.com"
   ```

If the issue is reproducible only from within your infrastructure, it's likely internal. If it's reproducible from multiple external locations, it's likely an issue with the external service.

**Q2: How do I securely copy files between servers without using password authentication?**

**A:** Use SSH key-based authentication with these steps:

1. Generate an SSH key pair if you don't already have one:

   ```bash
   ssh-keygen -t ed25519 -C "your_email@example

I'll continue with the FAQ section of Day 7:

**A:** Use SSH key-based authentication with these steps:

1. Generate an SSH key pair if you don't already have one:

   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

2. Copy your public key to the destination server:

   ```bash
   ssh-copy-id user@remote-server
   ```

3. Alternatively, copy the key manually:

   ```bash
   cat ~/.ssh/id_ed25519.pub | ssh user@remote-server "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
   ```

4. Now you can use `scp` or `rsync` without password prompts:

   ```bash
   scp important-file.txt user@remote-server:/destination/path/
   rsync -avz config/ user@remote-server:/etc/app/config/
   ```

For added security, consider using SSH config files to manage multiple servers and keys:

```bash
# In ~/.ssh/config
Host prod-server
    HostName prod-server.example.com
    User admin
    IdentityFile ~/.ssh/prod_key

Host staging-server
    HostName staging-server.example.com
    User admin
    IdentityFile ~/.ssh/staging_key
```

**Q3: How do I troubleshoot intermittent network connectivity issues?**

**A:** Intermittent issues are challenging but can be approached methodically:

1. Set up continuous monitoring:

   ```bash
   # Run ping continuously and log timestamps of failures
   while true; do ping -c 1 target-host > /dev/null || echo "Failed at $(date)" >> ping_failures.log; sleep 5; done
   ```

2. Create a cronjob that tests connectivity and logs results:

   ```bash
   # Add to crontab (*/1 * * * * = every minute)
   */1 * * * * /path/to/test_connectivity.sh >> /var/log/connectivity_tests.log 2>&1
   ```

3. Look for patterns in the logs:

   ```bash
   # Check if failures align with specific times
   grep "Failed" ping_failures.log | cut -d' ' -f3-4 | sort | uniq -c
   ```

4. Correlate with other system events:

   ```bash
   # Look for system events around failure times
   for time in $(grep "Failed" ping_failures.log | cut -d' ' -f3-4); do
     grep -B 5 -A 5 "$time" /var/log/syslog
   done
   ```

5. Check for network saturation around failure times:

   ```bash
   # Install iftop or nethogs for bandwidth monitoring
   sudo iftop -i eth0
   ```

**Q4: How do I securely transfer large files between servers efficiently?**

**A:** For large file transfers, consider these approaches:

1. Use `rsync` with compression and partial transfer support:

   ```bash
   rsync -avz --partial --progress large_file.tar user@remote-server:/destination/
   ```

2. For very large files, consider splitting them:

   ```bash
   # Split a file into 1GB chunks
   split -b 1G large_file.tar large_file.tar.part_
   
   # Transfer each part
   for part in large_file.tar.part_*; do
     rsync -avz --progress $part user@remote-server:/destination/
   done
   
   # Reassemble on the destination
   ssh user@remote-server "cd /destination && cat large_file.tar.part_* > large_file.tar"
   ```

3. Consider using specialized tools for massive transfers:

   ```bash
   # Install and use 'aria2' for parallel downloads
   aria2c -x 16 -s 16 http://source-server/large_file.tar
   ```

4. For transfers between cloud regions/providers, consider using their native transfer tools:

   ```bash
   # Example with AWS S3
   aws s3 cp s3://source-bucket/large_file.tar s3://destination-bucket/
   ```

---

## 🚧 **Common Issues and Troubleshooting**

### **Issue 1: SSH Connection Refused or Timed Out**

**Possible causes:**

- SSH service not running
- Firewall blocking port 22
- Network connectivity issues
- Host unreachable

**Solutions:**

```bash
# Check if you can reach the host at all
ping remote-host

# Check if port 22 is open
nc -zv remote-host 22

# Check if SSH is running on a different port
nmap -p 1-65535 remote-host | grep "open"

# If you have access to the server console
sudo systemctl status sshd
sudo journalctl -u sshd
```

### **Issue 2: SCP or RSYNC Transfer Failure**

**Possible causes:**

- Disk space limitations
- Permission issues
- Network interruptions

**Solutions:**

```bash
# Check disk space on remote host
ssh user@remote-host "df -h"

# Check permissions on destination directory
ssh user@remote-host "ls -ld /destination/directory"

# For rsync, use partial flag to enable resume
rsync -avz --partial --progress source/ user@remote-host:/destination/

# For network issues, try smaller batch sizes
rsync -avz --size-only --progress --bwlimit=5000 source/ user@remote-host:/destination/
```

### **Issue 3: Network Name Resolution Problems**

**Possible causes:**

- DNS server issues
- `/etc/hosts` file misconfiguration
- Split DNS environments

**Solutions:**

```bash
# Test DNS resolution
dig hostname.example.com

# Check DNS servers
cat /etc/resolv.conf

# Try using a specific DNS server
dig @8.8.8.8 hostname.example.com

# Add entry to hosts file for critical services
echo "10.0.0.5 important-service.internal" | sudo tee -a /etc/hosts
```

---

## 🔄 **Real-World SRE Scenario: Debugging a Microservice Connectivity Issue**

**Situation:** Users are reporting intermittent 502 Bad Gateway errors when trying to access the checkout service. The checkout service depends on payment, inventory, and user profile services.

**SRE Response Using Today's Commands:**

1. Verify the symptoms:

   ```bash
   # Access the service endpoint directly
   curl -v https://checkout.example.com/health
   ```

2. Check the edge proxy/load balancer:

   ```bash
   # SSH to the proxy server
   ssh lb-server

   # Check if the proxy is forwarding traffic correctly
   sudo ss -tnp | grep checkout
   
   # Check proxy error logs
   sudo tail -n 100 /var/log/nginx/error.log | grep checkout
   ```

3. Check the checkout service itself:

   ```bash
   # SSH to the checkout service host
   ssh checkout-server
   
   # Check if the service is running
   sudo systemctl status checkout-service
   
   # Check if it's listening on the expected port
   sudo ss -tlnp | grep checkout-service
   
   # Check application logs
   sudo tail -n 100 /var/log/checkout-service/app.log
   ```

4. Test connectivity to dependent services:

   ```bash
   # From the checkout server, test each dependency
   ping -c 3 payment-service.internal
   ping -c 3 inventory-service.internal
   ping -c 3 user-profile-service.internal
   
   # Test specific ports
   nc -zv payment-service.internal 8080
   nc -zv inventory-service.internal 8080
   nc -zv user-profile-service.internal 8080
   ```

5. Investigate network path issues:

   ```bash
   # Check the route to problematic dependencies
   traceroute -n payment-service.internal
   
   # Get more detailed statistics
   mtr -n -r -c 10 payment-service.internal
   ```

6. Check for intermittent issues:

   ```bash
   # Set up continuous monitoring
   while true; do curl -s -o /dev/null -w "%{http_code}\n" https://payment-service.internal/health; sleep 1; done
   ```

7. Identify the root cause:

   ```bash
   # In this scenario, we discovered an issue with DNS resolution
   dig payment-service.internal
   
   # Check DNS settings
   cat /etc/resolv.conf
   
   # Test with a specific DNS server
   dig @10.0.0.53 payment-service.internal
   ```

8. Implement a fix:

   ```bash
   # Add entry to hosts file as temporary workaround
   echo "10.0.5.12 payment-service.internal" | sudo tee -a /etc/hosts
   
   # Restart the checkout service
   sudo systemctl restart checkout-service
   
   # Monitor for resolution
   tail -f /var/log/checkout-service/app.log
   ```

9. Document the incident:

   ```bash
   # Create a report with all findings
   vi ~/incidents/checkout-502-$(date +%Y%m%d).md
   ```

This scenario demonstrates how networking tools help SREs systematically troubleshoot complex distributed systems by testing connectivity, checking service status, analyzing network paths, and identifying configuration issues.

---

## 🔒 **Network Security Considerations for SREs**

As an SRE, security should be integrated into your networking practices:

1. **SSH Key Management**:
   - Rotate SSH keys periodically
   - Use passphrase-protected keys
   - Consider using ssh-agent for convenience

   ```bash
   # Start ssh-agent and add your key
   eval $(ssh-agent)
   ssh-add ~/.ssh/id_ed25519
   ```

2. **Port Forwarding Security**:
   - Always bind to localhost when creating tunnels
   - Use the `-N` flag to prevent command execution

   ```bash
   # Secure forwarding example
   ssh -L 127.0.0.1:8080:internal-service:80 -N -f jumphost
   ```

3. **Network Traffic Analysis**:
   - Use secure protocols (HTTPS, SSH, SFTP)
   - Analyze network traffic for unusual patterns

   ```bash
   # Basic traffic monitoring
   sudo tcpdump -i eth0 -n "port 443"
   ```

4. **Firewall Configuration**:
   - Implement principle of least privilege for network access

   ```bash
   # Check firewall status
   sudo ufw status
   
   # Allow only necessary services
   sudo ufw allow 22/tcp
   sudo ufw allow 443/tcp
   ```

---

## 📚 **Further Learning Resources**

- [Linux Network Administrators Guide](https://www.tldp.org/LDP/nag2/index.html)
- [SSH Mastery by Michael W. Lucas](https://mwl.io/nonfiction/tools#ssh)
- [Traceroute and MTR Explained](https://www.digitalocean.com/community/tutorials/how-to-use-traceroute-and-mtr-to-diagnose-network-issues)
- [TCP/IP Illustrated by Richard Stevens](https://www.amazon.com/TCP-Illustrated-Protocols-Addison-Wesley-Professional/dp/0321336313)
- [Google SRE Book - Chapter 8: Release Engineering](https://sre.google/sre-book/release-engineering/)
- [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)

---

🎓 **Day 7 completed!** Tomorrow, we'll explore user and group management in Linux, a crucial skill for maintaining secure and well-organized systems. You'll learn how to create and manage users, assign them to groups, and control their permissions and access rights.
