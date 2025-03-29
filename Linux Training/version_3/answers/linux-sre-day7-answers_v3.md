# 📝 **Answer Key: Day 7 Networking Quiz**

## **Beginner Level**

### **1. How do you ping `example.com` exactly 5 times?**

**Answer:** `ping -c 5 example.com`

**Explanation:** The `-c` option (count) tells `ping` to send a specific number of packets and then stop. Without this option, `ping` would continue indefinitely until interrupted manually with Ctrl+C.

### **2. Which command shows IP addresses assigned to your network interfaces?**

**Answer:** a) `ifconfig -a`

**Explanation:** `ifconfig -a` displays all network interfaces and their configurations, including IP addresses. The `-a` flag ensures that all interfaces are shown, even those that are down. While `ip addr` (not in the options) is the more modern equivalent, `ifconfig -a` is the correct answer among the given options. Option b) `ip route` shows routing information, not interface IPs, and option c) `ss -l` shows listening sockets.

### **3. What command lists active TCP listening ports?**

**Answer:** b) `netstat -tulpn`

**Explanation:** The `netstat -tulpn` command shows TCP (`t`) and UDP (`u`) connections that are in listening (`l`) state, with the process name (`p`) and without resolving hostnames (`n`). Option a) `netstat -an` shows all connections but doesn't specifically filter for listening ports. Option c) `ping localhost` tests connectivity to the local machine and doesn't show port information.

### **4. How do you connect to a remote host `server1` using SSH as user `alice`?**

**Answer:** `ssh alice@server1`

**Explanation:** The SSH syntax is `ssh [user@]hostname`, where the username comes before the `@` symbol and the hostname or IP address comes after. This command will attempt to connect to `server1` as user `alice` and prompt for authentication.

### **5. Which command securely copies a local file `notes.txt` to a remote host's directory `/home/user`?**

**Answer:** a) `scp notes.txt user@remotehost:/home/user`

**Explanation:** The `scp` (secure copy) command uses the syntax `scp source destination`. In this case, the source is the local file `notes.txt` and the destination specifies the remote host, username, and target directory path. Option b) uses `ssh` which doesn't copy files, and option c) uses `cp` which only works locally, not between systems.

## **Intermediate Level**

### **1. Which command would show you the network path packets take to reach google.com?**

**Answer:** b) `traceroute google.com`

**Explanation:** The `traceroute` command maps the path that packets take from your computer to a destination, showing each hop along the way and the time taken. Option a) `route google.com` is incorrect as `route` displays the routing table and doesn't take a hostname parameter. Option c) `ping -p google.com` is incorrect as `-p` in ping is for specifying a pattern, not for showing path information. Option d) `netstat -r google.com` is incorrect as `netstat -r` shows the routing table but doesn't take a hostname parameter.

### **2. How would you check if a service is listening on port 3306 (MySQL) on your server?**

**Answer:** c) Both a and b are correct

**Explanation:** Both commands `ss -tlnp | grep 3306` and `netstat -an | grep 3306` can be used to check if a service is listening on port 3306 (MySQL). The `ss` command is the newer replacement for `netstat`, but both work. Option d) `ping localhost:3306` is incorrect because `ping` doesn't test port availability, only host reachability.

### **3. Which tool is most efficient for keeping directories synchronized between two servers?**

**Answer:** b) `rsync`

**Explanation:** `rsync` is specifically designed for efficient file synchronization. Unlike `scp` (option a), it only transfers files that have changed, saving time and bandwidth. Options c) `wget` and d) `curl` are for downloading files from web servers, not for synchronizing directories between systems.

### **4. To set up an SSH tunnel to access a database server behind a firewall, which command would you use?**

**Answer:** a) `ssh -L 9000:database-server:3306 user@firewall-server`

**Explanation:** This command sets up local port forwarding (`-L`), making the remote database accessible on your local port 9000. Traffic to localhost:9000 gets forwarded through firewall-server to database-server:3306. Option b) uses remote forwarding (`-R`) which is the opposite of what's needed. Option c) uses dynamic forwarding (`-D`) which sets up a SOCKS proxy. Option d) is invalid syntax.

### **5. When copying files with rsync to preserve all permissions and ownership, which option set is correct?**

**Answer:** b) `-a -v -z`

**Explanation:** The `-a` (archive) option in rsync preserves permissions, ownership, timestamps, and other file attributes. It's a shorthand that combines `-rlptgoD`. The `-v` option provides verbose output, and `-z` compresses data during transfer. The other option sets don't properly preserve all attributes.

## **SRE Application Level**

### **1. During a production incident, users report they can't reach your API service. You can ping the server, but connecting to port 443 fails. Which command sequence would best help diagnose this issue?**

**Answer:** b) `curl -v https://api-server && ssh api-server "ss -tlnp | grep 443"`

**Explanation:** This sequence first tests the HTTPS connection from the client perspective using `curl` with verbose output, which will show where exactly the connection fails. Then it SSH's into the server to check if the service is actually listening on port 443. Option a) only checks if the server is reachable and if nginx is running, but doesn't test the HTTPS connection directly. Option c) only counts established connections without testing connectivity. Option d) includes traceroute which isn't as relevant since we already know we can ping the server.

### **2. Which rsync command would most safely sync configuration files to multiple production servers?**

**Answer:** `-avz --dry-run --delete`

**Explanation:** The safest approach for production systems is to:

- Use `-a` to preserve all file attributes
- Use `-v` for verbose output to see what's happening
- Use `-z` to compress data during transfer
- Use `--dry-run` to see what would be transferred without actually making changes
- Include `--delete` to ensure consistency by removing files on the destination that don't exist on the source

The dry-run option is crucial here for safety, allowing you to review changes before actually applying them to production systems.

### **3. During capacity planning, you need to analyze connection distribution to your load balancer. Which command pipeline would give you counts of connections by source IP?**

**Answer:** a) `ss -tn | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr`

**Explanation:** This pipeline:

1. Uses `ss -tn` to list TCP connections with numeric addresses
2. Uses `awk` to extract the 5th field, which contains the remote address:port
3. Uses `cut` to separate the IP from the port number
4. Sorts the IPs so identical ones are adjacent
5. Counts unique IPs with `uniq -c`
6. Sorts numerically in reverse order to see the highest counts first

The other options don't correctly extract and count the source IPs.

### **4. Your database is experiencing intermittent connectivity issues. Which approach would provide the best longitudinal data about network quality?**

**Answer:** c) `mtr -r -c 100 database-server > mtr_report.txt`

**Explanation:** The `mtr` tool combines the functionality of traceroute and ping, showing the path packets take along with packet loss and latency statistics for each hop. The `-r` flag generates a report output, and `-c 100` sends 100 packets for statistical significance. This provides the most comprehensive view of network quality across the entire path. Option b) is a basic approach but doesn't show where in the network path issues occur. Options a) and d) are less comprehensive in showing the pattern over time.

### **5. A development team reports their new service can't connect to the authentication service. The services are on different subnets. What's the most likely issue and how would you first diagnose it?**

**Answer:** b) Firewall blocking - check with `telnet auth-service.internal 443`

**Explanation:** When services are on different subnets, the most common issue is firewall rules blocking the traffic between subnets. The `telnet` command to the specific port will quickly verify if the connection is being blocked. While options a), c), and d) are all valid troubleshooting steps, given the specific scenario of services on different subnets, checking for firewall blocking should be the first step before investigating more complex issues like routing, DNS, or TLS certificates.
