---
---

who
--
TODO: Add documentation for this command by submitting a pull request.
<!-- one line explanation would go here -->
## Description
Displays list of all users currently logged on 

<!-- minimal example -->
### Example Output 
~~~ bash
$ Username console  Oct 12 08:20 
$ Username ttys000  Oct 20 09:35 
~~~

### Example Command
<!--more-->
~~~ bash
$ who -b 
reboot ~ Oct 12 8:20

$ who -T
Username - console  Oct 12 08:20 
Username + ttys000  Oct 20 20:04 

$ who -u
Username console  Oct 12 08:20  old  	    99
Username ttys000  Oct 20 20:04   .   	 87780

~~~

 The who utility displays a list of all users currently logged on, showing for each user the login name, tty
 name, the date and time of login, and hostname if not local.

#### Available options:
 `-a`     Same as `-bdlprTtu.` 
 
 `-b`    Time of last system boot. 
 
 `-d`    Print dead processes. 
 
 `-H`    Write column headings above the regular output.
 
 `-l`    Print system login processes (unsupported).
 
 `-m`    Only print information about the current terminal.  This is the POSIX way of saying who am i.
 
 `-p`    Print active processes spawned by launchd(8) (unsupported).
 
 `-q`    Quick mode: List only the names and the number of users currently logged on.  When this option is
         used, all other options are ignored.
         
  `-r`   Print the current runlevel.  This is meaningless on Mac OS X.
  
  `-s`   List only the name, line and time fields.  This is the default.
  
  `-T`   Print a character after the user name indicating the state of the terminal line: +' if the terminal is
         writable; -' if it is not; and ?' if a bad line is encountered.
         
  `-t`   Print last system clock change (unsupported).
  
  `-u`   Print the idle time for each user, and the associated process ID. 
  
  `am I` Returns the invoker's real user name.
  
  `file` By default, who gathers information from the file /var/run/utmpx.  An alternative file may be specified.


