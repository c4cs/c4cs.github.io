---
---

sudo
---

`sudo` allows a user to execute a command as a different user (with the default being the root user). `sudo` is useful when commands need to be performed with elevated privileges, such as installing system updates.

~~~ bash
$    sudo apt-get update
~~~

<!--more-->

### Useful Options / Examples

#### `sudo -ll`

This allows a user to find out all of the root commands that they are able to execute and all the users they are able to execute these commands as. `sudo -l` could be used to do this, but for long lists, `sudo -ll` produces a cleaner output.

~~~ bash
user@computer-VirtualBox:~/c4cs.github.io$ sudo -ll
[sudo] password for user: 
Matching Defaults entries for user on computer:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin
User user may run the following commands on computer:
Sudoers entry:
    RunAsUsers: ALL
    RunAsGroups: ALL
    Commands:
	ALL
~~~

#### `sudo -u`

This allows a user to carry out a command as another user. It will execute the command as the specified target user.

~~~bash
$    sudo -u serverUser rails db:drop
[sudo] password for currentUser:
~~~

#### `sudo -b` or `sudo &`

This runs a sudo command in the background, allowing the current terminal session to still be used while the command is running. Note that most interactive commands will not work correctly in background mode.

~~~bash
$    sudo -b matlab
~~~

#### `sudo !!`

Runs the previous command with `sudo`.

~~~bash
$    user@computer:~$ apt-get update
Reading package lists... Done
W: chmod 0700 of directory /var/lib/apt/lists/partial failed - SetupAPTPartialDirectory (1: Operation not permitted)
E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)
E: Unable to lock directory /var/lib/apt/lists/
W: Problem unlinking the file /var/cache/apt/pkgcache.bin - RemoveCaches (13: Permission denied)
W: Problem unlinking the file /var/cache/apt/srcpkgcache.bin - RemoveCaches (13: Permission denied)
$    user@computer:~$ sudo !!
sudo apt-get update
[sudo] password for user: 
Hit:1 http://us.archive.ubuntu.com/ubuntu xenial InRelease
Get:2 http://us.archive.ubuntu.com/ubuntu xenial-updates InRelease [102 kB]    
Hit:3 http://ppa.launchpad.net/canonical-chromium-builds/stage/ubuntu xenial InRelease
Get:4 http://security.ubuntu.com/ubuntu xenial-security InRelease [102 kB]     
Get:5 http://us.archive.ubuntu.com/ubuntu xenial-backports InRelease [102 kB]  
Get:6 http://us.archive.ubuntu.com/ubuntu xenial-updates/universe amd64 Packages [540 kB]
Fetched 846 kB in 0s (1,149 kB/s)                                              
Reading package lists... Done
~~~

#### `sudo -n`

This runs the command specified without prompting the user for their password. The `-n` flag stands for _non-interactive_. This is particularly useful when writing shell-scripts.

#### `sudo -v`

This extends the verification timeout period and allows users to continue to carry out `sudo` commands without having to enter the password for a longer period of time.

### Related Commands

[su](../commands/su)
