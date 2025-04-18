# 🏆 Synthesized Linux SRE Training Module – Day 7: Networking Basics

## 📌 Introduction

Welcome to Day 7 of your Linux SRE training! Today, we’ll explore **Linux Networking Basics** using a tiered approach—**Beginner**, **Intermediate**, and **SRE-level**. This module synthesizes the strengths of two source documents:

- **Document 2’s** clear structure and visual organization
- **Document 1’s** detailed explanations and practical examples

### Objectives by Tier

**Beginner**

1. Test network connectivity with `ping`
2. View and configure network interfaces (`ifconfig` / `ip`)
3. Identify open connections and listening services via `netstat` / `ss`

**Intermediate**

1. Use `ssh` for secure remote access
2. Transfer files securely with `scp` (and note `rsync` for advanced usage)
3. Diagnose and monitor connections for troubleshooting

**SRE-Level**

1. Integrate these tools into automated SRE workflows
2. Interpret outputs in large-scale or complex networks
3. Incorporate advanced troubleshooting (e.g., multi-service connectivity issues)

### Relevance to Previous and Future Learning

- **Previously**: We covered process management and system resource usage.
- **Today**: We focus on establishing and troubleshooting network connectivity.
- **Next**: We’ll explore user and group management, including permissions and security.

---

## 📚 Core Concepts

### Beginner: Foundational Networking

- **IP Address**: Like a home address for network traffic.
- **Network Interface**: The “mailbox” where data arrives.
- **Ports**: Identifiers for specific applications (like apartment numbers).
- **Connectivity Testing**: `ping` to verify reachability.

### Intermediate: OSI Layers & Realistic Configuration

- **Layered Approach**: OSI layers 3 (Network), 4 (Transport), 7 (Application) matter most for these tools.
- **Routing & Gateways**: Understand how traffic gets from source to destination.
- **Security Context**: Firewalls, allowing or blocking ICMP or TCP.

### SRE-Level: Large-Scale Networking

- **Multi-Host Diagnostics**: Tools like `ss` and `traceroute` help pinpoint outages.
- **Performance & Latency**: Minimizing downtime by isolating network vs. application issues.
- **Automation**: Integrate checks and logs (via scripts or CI/CD pipelines).

---

## 💻 Command Breakdown

Below we break down the key Linux networking commands in the recommended structured format, ensuring clarity and incremental learning.

### Command: `ping` (Packet INternet Groper)

**Command Overview:**

- **Purpose**: Sends ICMP echo requests to test reachability and measure latency.
- **SRE Relevance**: Quick checks for connectivity or packet loss.

**Syntax & Flags:**

| Flag/Option | Syntax Example        | Description                        | SRE Usage Context                      |
|-------------|-----------------------|------------------------------------|----------------------------------------|
| `-c`        | `ping -c 3 host`     | Send only 3 packets                | Bounded tests for scripts              |
| `-w`        | `ping -w 5 host`     | Deadline in seconds                | Avoid indefinite pings                 |
| `-i`        | `ping -i 0.2 host`   | Interval between packets           | Faster probing in short intervals      |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```
# Basic reachability
$ ping -c 2 google.com
PING google.com (142.250.190.14): 56 data bytes
64 bytes from 142.250.190.14: icmp_seq=0 ttl=115 time=12.3 ms
64 bytes from 142.250.190.14: icmp_seq=1 ttl=115 time=13.1 ms
--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss
```

- 🧩 **Intermediate Example:**

```
# Testing local network device, limiting total time
$ ping -c 4 -w 3 192.168.1.10
...
# Explanation: -w sets a 3-second overall deadline
```

- 💡 **SRE-Level Example:**

```
# Checking latency across multiple hosts quickly
$ for host in web1 db1 proxy1; do
>   ping -c 2 -w 2 $host | grep 'packets transmitted' >> /tmp/netcheck.log
> done

# Explicit context: quick round-trip test across critical hosts in parallel.
```

**Instructional Notes:**
- 🧠 **Beginner Tip:** Some hosts block ICMP — a failed ping doesn’t always mean the host is down.
- 🧠 **Beginner Tip:** Cancel ongoing pings with Ctrl+C.
- 🔧 **SRE Insight:** Integrate ping checks into scripts for uptime monitoring.
- 🔧 **SRE Insight:** Evaluate latency changes over time for capacity planning.
- ⚠️ **Common Pitfall:** Ping success doesn’t guarantee higher-layer protocols work.
- 🚨 **Security Note:** Excessive pinging can trigger intrusion detection systems.
- 💡 **Performance Impact:** Typically minimal unless used in high-frequency flood mode.

---

### Command: `ifconfig` / `ip` (Interface Configuration)

**Command Overview:**

- **Purpose**: Display and configure network interfaces.
- **SRE Relevance**: Vital for verifying IP settings, netmask, gateway, ensuring connectivity.

**Syntax & Flags:**

| Flag/Option  | Syntax Example            | Description                           | SRE Usage Context                          |
|--------------|---------------------------|---------------------------------------|--------------------------------------------|
| `ifconfig`   | `ifconfig eth0`          | Legacy command to view interface info  | Quick checks in older distributions        |
| `ip addr`    | `ip addr show eth0`      | Show details for a specific interface  | Modern approach with more functionality    |
| `ip route`   | `ip route show`          | Display routing table                  | Validate default gateways                  |
| `ip link`    | `ip link set eth0 up`    | Bring interface up or down            | Scripted reconfigurations / troubleshooting|

**Tiered Examples:**

- 🔍 **Beginner Example:**

```
# Check all interfaces with legacy ifconfig
$ ifconfig -a
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
  inet 192.168.1.101  netmask 255.255.255.0  broadcast 192.168.1.255
...
```

- 🧩 **Intermediate Example:**

```
# View current IP addressing using ip
$ ip addr show eth0
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP>
    inet 10.0.0.5/24 brd 10.0.0.255 scope global eth0
...
# Explanation: ip is script-friendly, modern, and more complete.
```

- 💡 **SRE-Level Example:**

```
# Temporarily add a secondary IP for multi-homed test
$ sudo ip addr add 10.0.0.100/24 dev eth0

# Check route to confirm traffic flow
$ ip route get 10.0.0.50
```

**Instructional Notes:**
- 🧠 **Beginner Tip:** Know the interface name (e.g., eth0, wlan0, enp0s3) before changing settings.
- 🧠 **Beginner Tip:** `ip` command is the future, but `ifconfig` is still widely referenced.
- 🔧 **SRE Insight:** Use `ip -s link` to track packet errors or dropped packets.
- 🔧 **SRE Insight:** Keep track of ephemeral addresses in container or cloud environments.
- ⚠️ **Common Pitfall:** Removing the default route on a remote server can cause immediate disconnection.
- 🚨 **Security Note:** Make sure you don’t accidentally expose services on a new IP.
- 💡 **Performance Impact:** Generally low unless reconfigured frequently in production.

---

### Command: `netstat` / `ss` (Network Statistics / Socket Statistics)

**Command Overview:**

- **Purpose**: Display active connections, listening ports, and more.
- **SRE Relevance**: Finding which process listens on a port, diagnosing stuck connections.

**Syntax & Flags:**

| Flag/Option | Syntax Example              | Description                                     | SRE Usage Context                                             |
|-------------|-----------------------------|-------------------------------------------------|---------------------------------------------------------------|
| `-t`        | `ss -t`                    | Show TCP connections only                         | Focus on key protocols like HTTP, SSH, DBs                     |
| `-u`        | `netstat -u`               | Show UDP connections                             | For DNS or SNMP                                               |
| `-l`        | `ss -l`                    | List only listening sockets                      | Identify services open to the network                         |
| `-n`        | `ss -n`                    | Don’t resolve host names (faster)                | High traffic systems / performance constraint                 |
| `-p`        | `ss -p` (requires sudo)    | Show owning processes (name/PID)                 | Diagnose conflicts or unknown listeners                        |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```
# Show all listening TCP ports using netstat
$ netstat -tln
Proto  Local Address    Foreign Address    State
TCP    0.0.0.0:22       0.0.0.0:*          LISTEN
...
```

- 🧩 **Intermediate Example:**

```
# Using ss with process info
$ sudo ss -tlnp
State   Recv-Q  Send-Q Local Address:Port  Peer Address:Port  Process
LISTEN  0       128    0.0.0.0:80         0.0.0.0:*          users:( ("nginx",pid=909,fd=6) )
...
# Explanation: see which processes own which ports.
```

- 💡 **SRE-Level Example:**

```
# Filter established connections to a microservice on port 8080
$ ss -tn state established '( sport = :8080 or dport = :8080 )'
ESTAB 0  0 10.0.0.12:8080  10.0.0.44:53210  users:( ("java",pid=1234,fd=55) )
# Explicit context: helps pinpoint traffic for critical services.
```

**Instructional Notes:**
- 🧠 **Beginner Tip:** Start with `-tln` to see listening TCP services.
- 🧠 **Beginner Tip:** `netstat` is older, `ss` is faster and more modern.
- 🔧 **SRE Insight:** Combine with grep/awk for advanced filtering.
- 🔧 **SRE Insight:** Useful for real-time capacity checks in production.
- ⚠️ **Common Pitfall:** Without `sudo`, you may not see process owners.
- 🚨 **Security Note:** Watch for unexpected listeners (possible malware).
- 💡 **Performance Impact:** Typically low overhead to run occasionally.

---

### Command: `ssh` (Secure Shell)

**Command Overview:**

- **Purpose**: Securely log into remote servers, forward ports.
- **SRE Relevance**: Foundation for remote ops; can be automated.

**Syntax & Flags:**

| Flag/Option | Syntax Example                      | Description                                | SRE Usage Context                                 |
|-------------|-------------------------------------|--------------------------------------------|---------------------------------------------------|
| `-p`        | `ssh -p 2222 user@host`            | Connect on non-default port                 | Bypass standard 22, e.g., custom firewall ports    |
| `-i`        | `ssh -i ~/.ssh/key.pem user@host`   | Use specified key file                      | Different keys for dev, staging, prod             |
| `-L`        | `ssh -L 8080:localhost:80 user@host`| Local port forwarding                       | Tunneling for internal web or database access     |
| `-N -f`     | `ssh -N -f user@host`               | No shell, run in background                 | Keep tunnels open without interactive session     |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```
# Simple remote login
$ ssh alice@server.example.com
(alice@server.example.com's password)
[alice@server ~]$
```

- 🧩 **Intermediate Example:**

```
# Connect with a custom key and port
$ ssh -p 2200 -i ~/.ssh/dev_key bob@staging.example.com
Last login: Tue Mar 28 09:35:11 2025 from 10.0.0.15
```

- 💡 **SRE-Level Example:**

```
# Creating a local tunnel to access an internal service
$ ssh -L 9090:internal-app:9090 user@bastion -N -f

# Explanation: local port 9090 is securely forwarded to 'internal-app:9090'.
# Used in production to securely connect to restricted services.
```

**Instructional Notes:**
- 🧠 **Beginner Tip:** Type `exit` or `logout` to end an SSH session.
- 🧠 **Beginner Tip:** Key-based auth can avoid repetitive passwords.
- 🔧 **SRE Insight:** Managing `~/.ssh/config` with short aliases is essential in large fleets.
- 🔧 **SRE Insight:** Use agent forwarding (`-A`) for multi-hop connections.
- ⚠️ **Common Pitfall:** Wrong file permissions on private keys (`chmod 600`) cause authentication failures.
- 🚨 **Security Note:** Keep keys safe; never share private keys.
- 💡 **Performance Impact:** Typically minimal, but can increase CPU usage with large data streams.

---

### Command: `scp` (Secure Copy)

**Command Overview:**

- **Purpose**: Copy files securely over SSH.
- **SRE Relevance**: Deploy configs, collect logs, handle quick file transfers.

**Syntax & Flags:**

| Flag/Option | Syntax Example                                        | Description                         | SRE Usage Context                              |
|-------------|-------------------------------------------------------|-------------------------------------|-----------------------------------------------|
| `-r`        | `scp -r local_dir user@host:/remote/dir`             | Recursive copy of directories       | Back up or deploy entire directories           |
| `-P`        | `scp -P 2222 file user@host:/path`                    | Connect via non-standard SSH port   | Servers behind custom firewall ports           |
| `-i`        | `scp -i ~/.ssh/key file user@host:/path`             | Use specific SSH key                | Distinguish multiple key pairs                 |
| `-p`        | `scp -p file user@host:/path`                         | Preserve file timestamps            | Maintain file attributes for auditing          |

**Tiered Examples:**

- 🔍 **Beginner Example:**

```
# Copy a single file to remote server
$ scp notes.txt sam@host:/home/sam/
notes.txt                100%   15KB 2.0MB/s   00:00
```

- 🧩 **Intermediate Example:**

```
# Copy a directory from remote to local, preserving timestamps and attributes
$ scp -rp user@host:/var/log/ /tmp/backup_logs

# Explanation: good for investigating logs locally.
```

- 💡 **SRE-Level Example:**

```
# Parallel copying from multiple servers
$ for srv in web1 web2 db1; do
>   scp -i ~/.ssh/prod_key $srv:/var/log/app.log /backup/logs/$srv-app.log &
> done
$ wait

# Explanation: gather logs quickly in a single step.
```

**Instructional Notes:**
- 🧠 **Beginner Tip:** Remember the syntax: `scp [local -> remote]` or `[remote -> local]`.
- 🧠 **Beginner Tip:** Use absolute paths if you’re unsure where files are.
- 🔧 **SRE Insight:** For large or partial sync, `rsync` is more efficient.
- 🔧 **SRE Insight:** Incorporate `scp` in deployment scripts for simple updates.
- ⚠️ **Common Pitfall:** Overwriting paths if you get source/destination reversed.
- 🚨 **Security Note:** Same SSH-based security considerations apply.
- 💡 **Performance Impact:** Encryption overhead can be high for very large transfers.

---

## 🛠️ System Effects

- **Filesystem**: `scp` writes files to remote/local systems; watch for disk space.
- **System Resources**: Ping, netstat, ip are low overhead; scp can consume CPU during large transfers.
- **Security**: Exposed interfaces or incorrect SSH configurations can create vulnerabilities.
- **Monitoring**: Tools like `netstat/ss` can confirm normal or suspicious connections.

---

## 🎯 Hands-On Exercises

### Beginner (3 Exercises)

1. **Ping a Remote Host**: `ping -c 3 google.com` and observe latency.
2. **Check Interfaces**: Run `ifconfig -a` (or `ip addr`) to identify your IP address.
3. **List Listening Ports**: `netstat -tln` or `ss -tln` and interpret which ports are open.

### Intermediate (3 Exercises)

1. **Key-Based SSH**:
   - Generate a key (`ssh-keygen -t ed25519`)
   - Copy key to remote server (`ssh-copy-id`) or manual copy
   - Connect with `ssh -i yourkey user@host`
2. **Add/Remove a Route**:
   - `ip route add 10.0.2.0/24 dev eth0`
   - `ip route del 10.0.2.0/24 dev eth0`
3. **scp a Directory**:
   - `scp -r /path/to/mydir user@server:/remote/dir`
   - Verify files on the remote side.

### SRE-Level (3 Exercises)

1. **Automated Ping Script**:
   - Write a short shell script to ping a list of servers.
   - Log results (success/failure) to a file.
2. **SSH Tunneling**:
   - `ssh -L 3306:db-internal:3306 user@bastion -N -f`
   - Verify local MySQL client can connect via `localhost:3306`.
3. **Parallel Log Retrieval**:
   - Use a loop to `scp` logs from multiple servers simultaneously.
   - Observe the performance benefits.

---

## 📝 Quiz Questions

### Beginner (3-4)

1. **(MCQ)** Which command tests basic connectivity?
   - a) `ssh`  b) `ping`  c) `scp`  d) `netstat`
2. **(Short Answer)** What command lists IP addresses in the modern approach?
3. **(MCQ)** Which option in `ping` sets how many packets are sent?
   - a) `-w`  b) `-c`  c) `-i`  d) `-p`
4. **(Short Answer)** Which command shows open/listening ports on your system?

### Intermediate (3-4)

1. **(MCQ)** Which command logs you into a remote host via the default SSH port?
   - a) `ssh user@host`  b) `ssh -p 25 user@host`  c) `scp user@host:/file .`
2. **(Short Answer)** Which command do you use to remove a route?
3. **(Scenario)** You tried to connect with `ssh -i ~/.ssh/key user@host` but got `Permission denied`. What might be wrong?
4. **(MCQ)** Which command can show the process ID bound to a specific port?
   - a) `netstat -p`  b) `ss -p`  c) Both a & b  d) Neither

### SRE-Level (3-4)

1. **(Scenario)** You suspect port `8080` is in use by a rogue process. How do you confirm?
2. **(MCQ)** For zero-downtime route changes, which step is essential?
   - a) Immediately remove the existing route
   - b) Add a backup route and test connectivity
   - c) Wait for traffic to fail before making changes
3. **(Scenario)** You need to copy logs from 10 servers to a central location every night. Suggest an efficient approach.
4. **(Short Answer)** Write a command using `ss` to filter for established connections on port 443.

---

## 🚧 Troubleshooting

### Scenario 1: Can’t ping or SSH a New Server

- **Symptoms**: `ping` times out, `ssh: no route to host`.
- **Causes**: Firewall blocks or no IP assigned.
- **Diagnosis**: Check interface config on the server (`ifconfig/ip`), ensure the firewall allows 22.
- **Resolution**: Assign correct IP/gateway, open port 22.
- **Prevention**: Standardize setup scripts.

### Scenario 2: Service Stopped Listening on Port 80

- **Symptoms**: Web requests fail.
- **Causes**: Service crashed or changed to another port.
- **Diagnosis**: `sudo ss -tlnp | grep :80` to see if anything is listening.
- **Resolution**: Restart the service or revert port setting.
- **Prevention**: Monitor services, check logs frequently.

### Scenario 3: Slow scp Over VPN

- **Symptoms**: Transfers are very slow.
- **Causes**: VPN overhead, high latency or packet loss.
- **Diagnosis**: Compare local vs remote speed, `mtr`, or iperf.
- **Resolution**: Use `rsync --partial --progress` with compression.
- **Prevention**: Ensure adequate bandwidth, consider adjusting ciphers.

---

## ❓ FAQ

### Beginner (3)

1. **Q**: Why does ping fail on some hosts?
   **A**: They may block ICMP or have a firewall.
2. **Q**: How do I stop a running ping?
   **A**: Press `Ctrl+C`.
3. **Q**: Why is `ifconfig` not found on my system?
   **A**: Some distros don’t include net-tools by default; use `ip` instead.

### Intermediate (3)

1. **Q**: How can I keep an SSH session alive?
   **A**: Configure `ServerAliveInterval` in `~/.ssh/config`.
2. **Q**: Why won’t my new route persist after reboot?
   **A**: OS-level config is needed (e.g., /etc/network/interfaces or netplan in Ubuntu).
3. **Q**: Which is more efficient, scp or rsync?
   **A**: `rsync` is more efficient for incremental file copies; `scp` is simpler for quick single copies.

### SRE-Level (3)

1. **Q**: How do I push SSH key updates to 100+ servers?
   **A**: Use configuration management or orchestration tools (Ansible, Chef, etc.).
2. **Q**: Why do I see many TIME_WAIT connections?
   **A**: Normal in high-traffic systems; TCP keeps closed connections briefly.
3. **Q**: How do I handle ephemeral container networking?
   **A**: Automate with scripts or container orchestration that updates DNS/routes on the fly.

---

## 🔥 SRE Scenario: Multi-Service Connection Failure

**Incident**: Your microservice-based e-commerce site sees intermittent 503 errors.

1. **Confirm Issue**: `curl -I https://checkout.example.com` times out.
2. **Check Listening Ports**: On the checkout host, `ss -tlnp | grep checkout-service`.
3. **Ping Dependencies**: `ping -c 3 payment.example.com`.
4. **Investigate Logs**: `scp payment-host:/var/log/payment-service.log ./`.
5. **Set up Tunnels**: `ssh -L 3306:db-host:3306 user@bastion` to confirm DB is reachable.
6. **Root Cause**: Payment service listens only on localhost (127.0.0.1) but should be 0.0.0.0.
7. **Resolution**: Update config, restart service, confirm with `netstat/ss`.

---

## 🧠 Key Takeaways

1. **Command Summary**
   - `ping`: Quick connectivity test
   - `ifconfig/ip`: Interface management
   - `netstat/ss`: Connection checks
   - `ssh`: Secure remote access
   - `scp`: Secure file transfer
2. **Operational Insights**
   - Always confirm network connectivity before deeper application-level checks.
   - Logging and automation reduce manual overhead.
3. **Best Practices**
   - Keep interface configs consistent.
   - Secure remote access (SSH keys, passphrase protection).
   - Only open required ports for production.
4. **Preview of Next Topic**
   - **User & Group Management**: Permissions, security, and roles for multi-user Linux environments.

---

## 📚 Further Learning Resources

### 🔍 Beginner (2-3)

1. [Linux Journey - Networking Nomad](https://linuxjourney.com/lesson/network-basics)
   - Overviews IP, ping, ifconfig.
   - Great for absolute beginners.
2. [Ubuntu Network Configuration Basics](https://ubuntu.com/server/docs/network-configuration)
   - Step-by-step for interface config on Ubuntu.
3. [SSH.com - Beginners SSH Guide](https://www.ssh.com/academy/ssh)
   - Intro to SSH usage and principles.

### 🧩 Intermediate (2-3)

1. [Red Hat’s Networking with Linux Commands](https://www.redhat.com/sysadmin/networking-linux-commands)
   - Explores `ip`, `ss`, and routing.
2. [The Art of Command Line - Networking Section](https://github.com/jlevy/the-art-of-command-line)
   - Tips for `ssh`, `scp`, advanced net usage.
3. [SSH Mastery by Michael W. Lucas](https://mwl.io/nonfiction/tools#ssh)
   - Deeper dive into SSH configurations.

### 💡 SRE-Level (2-3)

1. [Google SRE Book - Chapter 8: Release Engineering](https://sre.google/sre-book/release-engineering/)
   - While not exclusively about networking, it shows big-scale practices.
2. [TCP/IP Illustrated by Richard Stevens](https://www.amazon.com/TCP-Illustrated-Protocols-Addison-Wesley-Professional/dp/0321336313)
   - Comprehensive TCP/IP deep dive.
3. [High Performance Browser Networking](https://hpbn.co/)
   - Focuses on latency, optimization, and advanced network topics.

---

# 🎉 End of Day 7: Networking Basics

You’ve explored essential Linux networking commands from beginner to SRE-level contexts. Keep practicing! Networking is foundational to nearly every aspect of systems reliability. Tomorrow, we’ll tackle **User & Group Management**, covering permission structures and security best practices. Good luck in your continued learning!
