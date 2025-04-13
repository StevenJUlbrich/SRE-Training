# 📝 Quiz Questions

## Beginner (3-4)

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
