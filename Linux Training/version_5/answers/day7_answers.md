# Day 7 – Quiz Answers with Explanations

Below are the quiz questions from the Day 7 networking exercises and their detailed answers, including why the correct choices are right and why the incorrect options are not.

---

## Beginner Tier

### Q1. Which command checks connectivity to a remote host?

**Options**:

1. `ls`
2. `ping`
3. `scp`
4. `ssh`

**Correct Answer**: `ping`

**Explanation**:

- **Correct**: `ping` sends ICMP echo requests to a target host to check if it’s reachable. It measures round-trip time and packet loss, indicating basic network connectivity.
- **Incorrect**:
  - `ls`: lists files and directories on the local filesystem.
  - `scp`: securely copies files between hosts, but it is not designed to simply test connectivity.
  - `ssh`: used for logging in to remote systems securely, rather than just testing if they’re online.

---

### Q2. Which command displays your machine’s IP address using the newer syntax?

**Correct Answer**: `ip addr show`

**Explanation**:

- **Correct**: The `ip` command is the modern replacement for `ifconfig`. Running `ip addr show` displays IP addresses, netmasks, and interface details.
- **Incorrect**:
  - `ifconfig`: older/legacy command, whereas the question specifically asks for the “newer syntax.”
  - `netstat`: primarily shows connections and routing, not specifically your interface’s IP address (though it can be used in some contexts).  

---

### Q3. Which command shows listening TCP ports?

**Options**:

1. `ping -t`
2. `netstat -tln`
3. `ssh -L`
4. `scp -r`

**Correct Answer**: `netstat -tln`

**Explanation**:

- **Correct**: `netstat -tln` or `ss -tln` show TCP connections that are listening (`-l`), in numeric format (`-n`), focusing on TCP (`-t`).
- **Incorrect**:
  - `ping -t`: modifies time-to-live or repeated pings, but does not show listening ports.
  - `ssh -L`: sets up local port forwarding, which is different from listing system-wide listening ports.
  - `scp -r`: copies files/folders securely over SSH.

---

## Intermediate Tier

### Q1. If you see a server listening on port 22, it is most likely

**Options**:

1. A web server
2. SSH service
3. A database
4. DNS resolver

**Correct Answer**: SSH service

**Explanation**:

- **Correct**: Port 22 is the default port for SSH connections.
- **Incorrect**:
  - A web server is typically on port 80 (HTTP) or 443 (HTTPS).
  - Databases listen on ports like 3306 (MySQL), 5432 (PostgreSQL), 27017 (MongoDB), etc.
  - DNS runs on port 53.

---

### Q2. How can you securely copy `data.txt` to user `admin` on host `server1`, preserving timestamps?

**Correct Answer**: `scp -p data.txt admin@server1:/destination/path`

**Explanation**:

- The `-p` flag preserves timestamps and file modes.
- You specify the remote user (`admin`), host (`server1`), and the remote path. `scp` uses SSH under the hood for secure transfer.

---

### Q3. You tried to `ssh` into a new server but received `Permission denied (publickey)`. What steps might resolve this?

**Correct Answer**:

- Ensure you’ve uploaded your public key to `~/.ssh/authorized_keys` on the remote server with proper permissions.
- Confirm local private key (`~/.ssh/id_rsa`, for example) is secure (`chmod 600`).
- Check `/etc/ssh/sshd_config` on the server to confirm `PubkeyAuthentication yes`.
- If using a custom key file, use `ssh -i /path/to/private_key user@host`.

**Explanation**:

- Typically this error indicates SSH is configured to accept only public key authentication, and your key isn’t recognized or is incorrectly set up.

---

## SRE-Level Tier

### Q1. You suspect a port conflict for port `8080`. Which command precisely identifies the PID using that port?

**Correct Answer**: `ss -tlnp | grep :8080`

**Explanation**:

- `ss` is the modern alternative to `netstat` for listing sockets.
- The flags: `-t` = TCP, `-l` = listening, `-n` = numeric addresses, `-p` = show PID/Program name.
- `grep :8080` filters to connections on port 8080.

---

### Q2. Which of the following is NOT a recommended step for zero-downtime route changes?

**Options**:

1. Add a backup route first
2. Immediately remove the existing route
3. Validate connectivity on the new route
4. Monitor logs to ensure stable connections

**Correct Answer**: Immediately remove the existing route

**Explanation**:

- Removing the existing route right away could drop traffic and cause downtime before validating that the new route works. You want to add the backup route, verify that it’s handling traffic, then remove the old route.

---

### Q3. You want to automate copying logs from 10 servers to a central server each night. Which commands or approach might be most efficient and why?

**Correct Answer**:

- Scripts that run `scp` or `rsync` in a loop, often scheduled via `cron` or a systemd timer.
- For large or repetitive data, `rsync` is more efficient since it syncs deltas and can compress.

**Explanation**:

- `scp` is simple but copies everything fresh each time. `rsync` can skip unchanged files and compress, saving bandwidth and time. Using a scheduler ensures it happens automatically.

---

### Q4. Provide a one-liner using `ss` or `netstat` that filters all established connections on port 443, ignoring DNS resolution

**Correct Answer**: `ss -tn state established '( sport = :443 or dport = :443 )'`

**Explanation**:

- `-t` = TCP only.
- `-n` = numeric output (no DNS resolution).
- `state established` = show only established sockets.
- `( sport = :443 or dport = :443 )` = source or destination is port 443 (HTTPS).
