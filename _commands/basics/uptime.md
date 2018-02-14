---
---

uptime
------

`uptime` is used to check how long your computer has been on since the last reboot. This is useful for the user as it allows the user to determine whether a restart or shut down is necessary for the computer.

~~~ bash
$ uptime
11:31 up 1 day, 1:22, 2 users, load averages 1.97 2.04 2.14
~~~

<!--more-->

### Useful Options / Examples

'uptime' gives a one line display for each of the following

The current time:

~~~bash
11:31
~~~

How long the system has been running:

~~~bash
1 day, 1:22
~~~

How many users are currently logged on:

~~~bash
2 users
~~~

The system load averages for the past 1, 5, and 15 minutes:

~~~bash
1.91 2.04 2.13
~~~

### uptime syntax
~~~bash
uptime [options]
~~~

#### uptime -p
Displays only the time the computer has been on in a readable manner

~~~bash
uptime -p
up 11 minutes
~~~

#### uptime -s
Displays the time when the system first started

~~~bash
uptime -s
2018-02-14 11:49:24
~~~







