# The SRE's First Day

Taylor clutched the coffee cup a little too tightly as the elevator climbed to the 42nd floor. The CloudCrest Technologies logo glowed on the wall opposite—a stylized cloud with binary raindrops falling beneath it. First day jitters were normal, Taylor reasoned, but starting as a Site Reliability Engineer at a company that managed infrastructure for half the Fortune 500? That was next-level anxiety.

*You've got this. Four years of computer science. Three internships. That home lab that annoyed your roommates. You're ready.*

The doors slid open to reveal an open workspace humming with quiet energy. Rows of standing desks faced floor-to-ceiling windows, the San Francisco skyline a perfect backdrop to the tech paradise within.

"You must be Taylor!" A woman with curly hair and rectangular glasses approached, hand extended. "I'm Sophia, SRE Team Lead. Welcome to CloudCrest. How was traffic?"

"Not bad. I—"

Three loud pings interrupted, emanating from every monitor in the room. Taylor watched as twenty heads simultaneously swiveled toward their screens.

"Well," Sophia's smile tightened slightly. "Looks like you're getting the real CloudCrest experience on day one. We've got an incident."

Taylor's stomach dropped. "Is it serious?"

"Disk usage alert on one of our analytics clusters. Could be nothing, could be something. Perfect training opportunity." She gestured toward an empty desk. "Drop your stuff and shadow me."

Within minutes, Taylor was perched beside Sophia at her standing desk, watching as she opened a terminal window and connected to a remote server.

"First rule of SRE," Sophia said, fingers flying across the keyboard. "Always know where you are before you do anything."

She typed a command:

```
pwd
```

"/home/sophia," appeared on the screen.

"That's 'print working directory,'" Sophia explained. "Think of it as your 'You Are Here' marker in the Linux filesystem mall."

Taylor nodded. "So you always know your starting point before navigating?"

"Exactly. Now let's see what we're working with."

Sophia typed:

```
cd /var/log
```

"That's 'change directory,'" Taylor offered, eager to show some knowledge.

"Good! You know the basics. Most important command you'll use. Linux is like a big building with rooms and hallways. `pwd` tells you which room you're in, and `cd` lets you move to different rooms."

The prompt changed to show they were now in /var/log.

"This directory is where most logs live," Sophia continued. "Think of it as the system's journal where it writes down everything that happens. Let's see what we have here."

```
ls -l
```

The screen filled with files, dates, and permissions.

"'List,'" Taylor said. "With the long format flag."

"Look at you! Not your first rodeo after all." Sophia pointed at the screen. "See these files? Each service writes its events here. We need to find which logs are growing too fast."

She typed:

```
ls -lh
```

"The '-h' makes the sizes human-readable," Taylor noted, seeing the file sizes now displayed in MB and GB instead of bytes.

"Right. And... bingo." Sophia pointed at a file named analytics-upload.log that was 98GB. "That shouldn't be more than a few hundred MB."

A voice called from across the room. "Sophia! Singapore team needs you on that database migration call. Can't reschedule."

Sophia sighed. "Taylor, I hate to do this to you on your first day, but duty calls. Can you keep digging into this? We need to figure out why that log file is so huge and fix it before the disk fills completely."

Before Taylor could protest, Sophia was moving toward a conference room, calling back: "Just navigate around and gather info. Don't change anything yet! I'll be back in 30 minutes."

And just like that, Taylor was alone with a terminal connected to a production server and an impending disk space crisis.

*Deep breath. You've studied for this.*

Taylor started with the basics:

```
pwd
```

Still in /var/log. Good. Next:

```
ls -lh analytics-upload.log
```

The file details appeared, confirming its massive 98GB size and showing it was last modified just seconds ago—still actively growing.

*What's writing to it so quickly?*

Taylor remembered another command:

```
cd /etc
```

The Linux filesystem had been explained in Taylor's OS class. If /var/log held logs, /etc was where configuration files lived.

```
ls | grep analytics
```

This combined command would list files and filter for ones containing "analytics." Several matches appeared, including "analytics-upload.conf" and "analytics-services".

Taylor moved forward:

```
cd analytics-services
```

"No such file or directory," the terminal reported.

*Right. I need to specify if it's a directory.*

```
ls -l analytics-services
```

It was a file, not a directory. Taylor needed to read it:

```
less analytics-services
```

A configuration file appeared, listing services and their paths. One entry caught Taylor's eye:

```
upload_service: /opt/analytics/bin/upload_processor
config: /etc/analytics/upload.conf
log: /var/log/analytics-upload.log
debug: true
```

*Debug mode! That could explain the verbose logging.*

Taylor navigated to check the config:

```
cd /etc/analytics
```

```
ls -l
```

Several files appeared, including upload.conf. But there was something wrong with the permissions—it was world-writable.

Taylor wasn't familiar with the specific flags needed to check file details. Time to consult the manual:

```
man ls
```

A page of documentation appeared. Taylor scrolled through it, finding the explanation for each flag. The -a flag would show hidden files, and combining it with -l would give full details.

```
ls -la
```

Now Taylor could see that upload.conf had "777" permissions—readable, writable, and executable by everyone. That was definitely not secure for a production configuration file.

But what was causing the massive logging? Taylor decided to peek at the actual logs:

```
cd /var/log
```

```
tail analytics-upload.log
```

The last few lines of the log file appeared, showing thousands of repeated error messages:

```
[ERROR] Failed to upload file: FileNotFoundError: /var/app/uploads/analytics/user_data_12345.csv
[ERROR] Failed to upload file: FileNotFoundError: /var/app/uploads/analytics/user_data_12346.csv
[ERROR] Failed to upload file: FileNotFoundError: /var/app/uploads/analytics/user_data_12347.csv
```

It was trying to find files that didn't exist, over and over, and logging each failure.

Taylor needed to check the upload directory:

```
cd /var/app/uploads/analytics
```

```
ls -l
```

The directory was empty. Where were these files supposed to come from?

Taylor remembered another useful command to find related processes:

```
ps aux | grep upload
```

This showed all running processes, filtered to show only those with "upload" in the name. The output revealed a script running as root:

```
root     12345  0.2  0.1 12345 1234 ?    S    08:15   0:24 /bin/bash /opt/analytics/bin/generate_test_uploads.sh
```

A test script was running in production? Taylor navigated there:

```
cd /opt/analytics/bin
```

```
ls -l generate_test_uploads.sh
```

The script had execute permissions and a modification time of earlier that morning. Someone must have left a test script running that was trying to process non-existent files, filling up the log with errors.

Just as Taylor was piecing everything together, Sophia returned.

"Any progress?" she asked, sliding back to her standing desk.

Taylor nodded, suddenly feeling more confident. "I think I found the issue. There's a test script running that's looking for files that don't exist, and because debug mode is enabled in the config, it's logging every single failure."

Sophia's eyebrows raised. "Show me."

Taylor walked through the investigation step by step, navigating through the directories and showing the relevant files and permissions.

"Look at you, Sherlock! That's exactly right." Sophia was impressed. "Someone left a test script running. Let's fix it."

Together, they:
1. Disabled the test script
2. Fixed the insecure permissions on the config file
3. Turned off debug mode
4. Compressed the massive log file

As they worked, Sophia explained more about the Linux filesystem.

"Think of the Linux directory structure like a well-organized library," she said. "The root directory '/' is the main entrance. Then we have specialized sections: /etc is where configuration books are kept, /var is where things that vary or grow live—like logs, /home is where users have their own reading rooms, and /usr/bin is where all the executable tools are stored."

"And knowing how to navigate between them with `cd`, check your location with `pwd`, and see what's around you with `ls` is like having a map of the library," Taylor added.

"Exactly! And `man` is like having a librarian you can ask for help with any book. Never underestimate the power of `man`," Sophia grinned.

By the end of the day, the incident was resolved, the disk space freed up, and Taylor had navigated a real SRE challenge.

"Not bad for day one," Sophia said as they packed up. "Most people's first day is just setting up their laptop and filling out HR forms."

Taylor smiled. "I learned more in the past few hours than in a semester of classes."

"That's the SRE life. See you bright and early tomorrow—who knows what you'll be debugging next!"

As Taylor headed home, the anxiety from the morning had transformed into excitement. The commands—`pwd`, `ls`, `cd`, `man`—were no longer just theory but practical tools that had helped solve a real problem. The Linux filesystem was no longer an abstract concept but a structured environment to explore and protect.

Day one complete. Only one thought remained: what would day two bring?