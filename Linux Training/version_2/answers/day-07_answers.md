# ✅ **Day 7 Quiz – Answer Key with Detailed Explanations**

## Here are the answers and explanations for Day 7's networking quiz questions

---

### **Question 1:**  

**You're responding to an alert that your web service is unreachable. Which command would you use first to check if the server is reachable at the network level?**

✅ **Correct Answer:**  
**b)** `ping web-server`

**Explanation:**  

`ping` is the most fundamental network connectivity test that checks if a host is reachable at the IP level. It sends ICMP echo request packets and waits for replies, providing information about packet loss and round-trip time. This is typically the first step in network troubleshooting because:

- It verifies basic network connectivity
- It works at a lower network layer than application protocols
- It provides immediate feedback on whether packets can reach the destination
- It helps distinguish between network connectivity issues and application-specific problems

The other options are valid tools but would typically be used after confirming basic connectivity:

- `ssh web-server` tests SSH connectivity specifically (application layer), which may fail even if the network is functional
- `traceroute web-server` analyzes the network path, which is more detailed but slower
- `netstat -an` only shows local network connections, not remote connectivity

---

### **Question 2:**  

**During a performance investigation, you need to identify which process is listening on port 3306 (MySQL). Which command would be most appropriate?**

✅ **Correct Answer (fill-in-the-blank):**

```bash
sudo ss -tlnp | grep 3306
```

**Explanation:**  

This command combines several powerful options of the `ss` (socket statistics) command:

- `sudo`: Required to see process information associated with sockets
- `ss`: Modern replacement for netstat, more efficient for showing socket information
- `-t`: Show only TCP connections
- `-l`: Show only listening sockets
- `-n`: Don't resolve names (faster and shows numeric ports)
- `-p`: Show the process using each socket
- `| grep 3306`: Filter for the specific MySQL port

Alternatively, `sudo netstat -tlnp | grep 3306` would work similarly but is considered less efficient on modern systems.

This command will show you not just that port 3306 is open, but exactly which process (with PID) is using it, which is critical for performance investigations.

---

### **Question 3:**  

**You need to set up a secure tunnel to access a database that's only available on the internal network. Which SSH command would accomplish this?**

✅ **Correct Answer:**  
**c)** `ssh -L 3306:db-server:3306 user@jump-host`

**Explanation:**  

This command creates a local port forwarding tunnel using SSH:

- `-L 3306:db-server:3306`: This creates a tunnel where:
  - `3306` (first number): The local port on your machine
  - `db-server`: The destination server (from the jump-host's perspective)
  - `3306` (second number): The destination port on the db-server
  - `user@jump-host`: The SSH server that has access to the internal network

After running this command, you can connect to the database using `localhost:3306` on your local machine, and the traffic will be securely tunneled through the jump-host to the internal db-server.

The other options:

- Option a) forwards to localhost on the jump-host, not to the database server
- Option b) sets up remote port forwarding (opposite direction)
- Option d) uses an invalid `-t` flag instead of `-L`

---

### **Question 4:**  

**To synchronize a configuration directory to multiple servers while ensuring files deleted locally are also removed from the servers, which command would you use?**

✅ **Correct Answer:**  
**c)** `rsync -avz --delete config_dir/ server:/etc/app/`

**Explanation:**  

This `rsync` command is designed for a complete synchronization:

- `-a`: Archive mode (preserves permissions, timestamps, etc.)
- `-v`: Verbose output (shows what's happening)
- `-z`: Compress data during transfer (saves bandwidth)
- `--delete`: The critical flag that removes files on the destination that no longer exist on the source
- `config_dir/`: Source directory (trailing slash is important as it copies the contents, not the directory itself)
- `server:/etc/app/`: Destination path

The `--delete` option is what makes this answer correct for ensuring that files deleted locally are also removed from the servers.

Other options:

- Option a) using `scp` doesn't handle deletions
- Option b) using `rsync` without `--delete` won't remove files
- Option d) `--backup` creates backups of changed files but doesn't delete

---

### **Question 5:**  

**You're investigating network latency between your application server and database server. Which command would provide the most comprehensive view of the network path including latency statistics?**

✅ **Correct Answer:**  
**c)** `mtr -r db-server`

**Explanation:**  

`mtr` (My TraceRoute) is a network diagnostic tool that combines the functionality of `ping` and `traceroute` into a single, more powerful utility:

- It shows the entire network path like `traceroute`
- It continuously sends packets to each hop like `ping`
- It collects and analyzes statistics about packet loss, jitter, and latency
- The `-r` flag produces a report instead of an interactive display

The output includes:

- Loss percentage for each hop
- Average/min/max round-trip times
- Standard deviation of latency (indicates jitter or inconsistent performance)
- Statistics gathered over multiple packets, giving a more reliable view

This provides the most comprehensive view of network performance compared to:

- `ping`: Shows latency to the endpoint only, not intermediate hops
- `traceroute`: Shows the path but with limited statistics
- `ss -t`: Shows active TCP connections but not the network path or latency

---

### **Question 6:**  

**When transferring a large directory (50GB) of critical log files from one server to another, which command would be most appropriate to ensure data integrity and allow for resumption if interrupted?**

✅ **Correct Answer:**  
`rsync -avz --partial --progress logs/ remoteserver:/backup/logs/`

**Explanation:**  

This rsync command is ideal for large, critical transfers:

- `-a` (archive) preserves metadata including permissions, ownership, and timestamps
- `-v` (verbose) provides detailed output about what's being transferred
- `-z` (compress) reduces bandwidth usage by compressing data during transfer
- `--partial` keeps partially transferred files if the transfer is interrupted, allowing resumption
- `--progress` shows real-time progress information

Together, these options ensure:

1. Data integrity through preservation of file attributes
2. Efficient transfer through compression
3. Resilience against network interruptions
4. Visibility into the transfer progress

For critical data, these features are essential compared to alternatives like `scp` which would require restarting the entire transfer if interrupted.

---

### **Question 7:**  

**You suspect network packet loss is causing application timeouts. Which command would help confirm this hypothesis by showing packet loss statistics over time?**

✅ **Correct Answer:**  
`ping -i 0.5 -c 100 application-server | grep "packet loss"`

**Explanation:**  

This command uses `ping` to detect packet loss:

- `-i 0.5` sets the interval between pings to 0.5 seconds
- `-c 100` sends exactly 100 ping packets
- `application-server` is the target host to check
- `| grep "packet loss"` filters output to show only the summary statistics

The result will show a percentage of packet loss, like `5 packets transmitted, 4 received, 20% packet loss`.

This approach is effective because:

1. It sends a statistically significant number of packets (100)
2. It uses a relatively fast interval (0.5 seconds) to capture intermittent issues
3. It focuses on the packet loss metric which directly correlates with application timeouts
4. It's lightweight and non-intrusive to the network

Packet loss above 1-2% is generally considered problematic and would support your hypothesis that network issues are causing application timeouts.
