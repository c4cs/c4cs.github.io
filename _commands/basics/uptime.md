---
---

uptime
-------

`uptime` prints out how long your system has been up and running.

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


### `uptime -p`
Displays the uptime in a nicer, **p**rettier format.

`uptime --pretty` can also be used.

~~~ bash
$ uptime -p
up 10 hours, 25 minutes
~~~


### `uptime -s`
Displays the uptime **s**ince, in yyyy-mm-dd HH:MM:SS format.

`uptime --since` can also be used.

~~~ bash
$ uptime -s
2018-10-24 11:47:53 
~~~

### `uptime -V`
Displays your **V**ersion of uptime.

`uptime --version` can also be used.
 
~~~ bash
$ uptime -V
uptime from procps-ng 3.3.12 
~~~

### `uptime -h`
Displays a short **h**elp page, similar to this page. 

`uptime --help` can also be used.

~~~ bash
$ uptime -h

Usage:
 uptime [options]

Options:
 -p, --pretty   show uptime in pretty format
 -h, --help     display this help and exit
 -s, --since    system up since
 -V, --version  output version information and exit
~~~
