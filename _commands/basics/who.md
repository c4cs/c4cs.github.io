---
---

who
--

Displays list of all users currently logged on

~~~ bash
$ who
Username console  Oct 12 08:20
Username ttys000  Oct 20 09:35
~~~

<!--more-->
The who utility displays a list of all users currently logged on, showing for each user the login name, tty
name, the date and time of login, and hostname if not local.

#### Available options with examples:
`-a`     Same as `-bdlprTtu`. This command processes the system database used for user information.

`-b`    Time of last system boot.

~~~ bash
$ who -b
reboot ~ Oct 12 8:20
~~~

`-d`    Print dead processes. This command shows the zombie processes or processes that have already been executed.

`-H`    Write column headings above the regular output.

`-l`    Print system login processes (unsupported). This command shows the terminals where a user can log in.

`-m`    Only print information about the current terminal.  This is the POSIX way of saying who am i.

~~~ bash
$ who -m
Norinlava ttys000  Oct 29 18:35
~~~

`-p`    Print active processes spawned by launchd(8) (unsupported).

`-q`    Quick mode: List only the names and the number of users currently logged on.  When this option is
used, all other options are ignored.

`-r`   Print the current runlevel.  This is meaningless on Mac OS X.

`-s`   List only the name, line and time fields. This is the default.

`-T`   Print a character after the user name indicating the state of the terminal line: '+' if the terminal is
writable; '-' if it is not; and '?' if a bad line is encountered.

~~~ bash
$ who -T
Username - console  Oct 12 08:20
Username + ttys000  Oct 20 20:04
~~~

`-t`   Print last system clock change (unsupported).

`-u`   Print the idle time for each user, and the associated process ID.

~~~ bash
$ who -u
Username console  Oct 12 08:20  old  	    99
Username ttys000  Oct 20 20:04   .   	 87780
~~~

`am I` Returns the invoker's real user name.

`file` By default, who gathers information from the file `/var/run/utmpx`.  An alternative file may be specified.
