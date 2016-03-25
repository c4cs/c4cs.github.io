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

#### Load Times

##### The load averages output show usage for the last 1, 5, 15 minute intervals. This helps to diagnose which process is CPU hungry.

#### -p, --pretty

##### Shows the output in pretty format
~~~ bash
$ uptime -p
Up 3 hours, 26 minutes
~~~

#### -V, --version

##### This is probably the most useful option becuase it gives the version information.
~~~ bash
$ uptime -V
Uptime from procps-ng 3.3.9
~~~

