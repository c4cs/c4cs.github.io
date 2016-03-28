---
---

uptime
------

This command shows the current time followed by your computer's uptime.

~~~ bash
$ uptime
3:03 up 1 day, 6 hrs, 2 users, load averages: 1.38 1.43 1.42
~~~

<!--more-->

### Useful Options / Examples

#### `-p, --pretty`

~~~ bash
$ uptime -p
Up 3 hours, 26 minutes
~~~
* Shows uptime in a cleaner format, outputting only the time the computer was running.

#### `-V, --version`

~~~ bash
$ uptime -V
Uptime from procps-ng 3.3.9
~~~
* This option gives the version information of uptime, which comes from the procps filesystem. This filesystem contains many commands that describe the processess running the system.

#### Load Averages

* The default ouptut shows load averages for the last 1, 5, 15 minute intervals. This helps to diagnose which process is CPU hungry.

