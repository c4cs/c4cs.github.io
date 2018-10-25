---
---

uptime
-------

`uptime` tells you how long your system has been up and running.

~~~ bash
$ uptime
21:57:05 up 10:09,  1 user,  load average: 0.23, 0.35, 1.06
~~~

<!--more-->

### Useful Options / Examples

#### Description of Output
`uptime` displays the following information in one line when it is ran:

* The current time
* How long the system has been up (the 'up time')
* The number of users on the system
* The system load average in
	* The past 1 minute
	* The past 5 minutes, and
	* The past 15 minutes

#### `uptime -p`
Prints the uptime in a nicer, **p**rettier format
~~~ bash
$ uptime -p
up 10 hours, 25 minutes
~~~


