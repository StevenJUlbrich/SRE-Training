# ✅ **Day 8 Quiz – Answer Key with Detailed Explanations**

## Below are the answers and explanations for Day 8's user management quiz questions

---

### **Question 1:**  

**How would you add a new user called `john` with a home directory?**

✅ **Correct Answer:**  
**c)** `useradd -m john`

**Explanation:**  

The `-m` option in the `useradd` command explicitly tells the system to create a home directory for the new user. Without this flag, many Linux distributions won't automatically create a home directory.

The other options are incorrect:

- Option a) `useradd john` - This creates the user account but typically won't create a home directory on most distributions
- Option b) `useradd -h john` - The `-h` flag actually shows the help message for the useradd command, not create a home directory
- Option d) `usermod -m john` - `usermod` modifies existing users rather than creating new ones, and the `-m` option in usermod moves an existing home directory to a new location when used with `-d`

In production environments, it's almost always best to include the `-m` flag when creating regular user accounts to ensure they have a proper home directory.

---

### **Question 2:**  

**Which command completely removes a user named `john` and their home directory?**

✅ **Correct Answer:**  
**b)** `userdel -r john`

**Explanation:**  

The `userdel` command removes a user account, and the `-r` (remove) option additionally removes:

- The user's home directory and all its contents
- The user's mail spool

This is important when you want to completely clean up all traces of a user account from the system.

The other options are incorrect:

- Option a) `userdel john` - This removes just the user account but leaves their home directory and mail spool intact
- Option c) `usermod -r john` - The `-r` flag with `usermod` isn't valid; `usermod` modifies users rather than deleting them
- Option d) `rmuser -r john` - `rmuser` isn't a standard Linux command (though it exists in some BSD variants)

As an SRE, you should carefully consider whether to use the `-r` flag. For temporary employees or service accounts, complete removal is often appropriate. For permanent employees who are leaving, you might want to preserve their home directory for a time by omitting the `-r` flag.

---

### **Question 3:**  

**You need to add user `john` to the group `staff` without removing him from other groups. Which command would you use?**

✅ **Correct Answer:**  
**a)** `usermod -aG staff john`

**Explanation:**  

This command combines two critical flags:

- `-a` (append) - This tells `usermod` to add the new group(s) to the user's existing supplementary groups rather than replacing them
- `-G` (groups) - Specifies the supplementary group(s) to add

The `-a` flag is crucial here; without it, the `-G` flag alone would replace all of john's existing supplementary groups with just `staff`.

The other options are incorrect:

- Option b) `usermod -g staff john` - The lowercase `-g` sets the user's primary group, replacing their current primary group, and doesn't affect supplementary groups
- Option c) `groupadd staff john` - `groupadd` creates new groups but doesn't add users to them; the syntax is also incorrect
- Option d) `groupmod -a john staff` - `groupmod` modifies group properties but doesn't manage group membership; this syntax is incorrect

This command is one of the most commonly used for managing group membership and is essential knowledge for SREs managing access control.

---

### **Question 4:**  

**Which file contains the encrypted passwords for user accounts?**

✅ **Correct Answer:**  
**b)** `/etc/shadow`

**Explanation:**  

The `/etc/shadow` file is a critical security file that contains:

- Encrypted (hashed) user passwords
- Password aging information
- Account expiration details
- Other security information

It's only readable by root and members of the shadow group, making it much more secure than the world-readable `/etc/passwd` file, which in older Unix systems used to contain encrypted passwords.

The other options store different information:

- Option a) `/etc/passwd` - Contains basic user account information (username, UID, GID, home directory, shell) but not passwords in modern systems
- Option c) `/etc/group` - Contains group definitions and memberships
- Option d) `/etc/users` - This file doesn't exist in standard Linux distributions

Understanding these system files is crucial for SREs, especially when troubleshooting authentication issues or performing user management operations outside of the standard commands.

---

### **Question 5:**  

**To create a service account (system user) for running a web service, which command is most appropriate?**

✅ **Correct Answer:**  
**b)** `useradd -r -s /bin/false webservice`

**Explanation:**  

This command creates an appropriate service account with several security-enhancing features:

- `-r` (system account) - Creates a system account with a lower UID (typically < 1000), clearly distinguishing it from regular user accounts
- `-s /bin/false` - Sets a non-interactive shell that prevents anyone from logging in as this user

These settings follow the principle of least privilege, a key security concept for SREs. Service accounts should only have the minimum necessary permissions to perform their function and shouldn't be usable for interactive logins.

The other options are less appropriate:

- Option a) `useradd -m webservice` - Creates a regular user with a home directory, which is unnecessary for most service accounts and adds attack surface
- Option c) `usermod -s /bin/nologin webservice` - This would modify an existing user rather than create a new one
- Option d) `groupadd -r webservice` - This creates a system group but not a user account

For production services, SREs should always create dedicated system accounts with restricted capabilities rather than running services as root or as regular user accounts.
