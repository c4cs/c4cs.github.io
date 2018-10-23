---
---

sleep
-------

sleep delays for a specified amount of time

~~~ bash
sleep 1 #delays for 1 second
sleep 1m #delays for 1 minute
sleep 1h #delays for 1 hour
sleep 4s 5s #delays for 9 seconds
sleep 2m 30s #delays for 2 minutes and 30 seconds
sleep 1.45 #delays for 1.45 seconds
~~~

<!--more-->

### Useful Options / Examples
There are several useful suffixes for sleep. These need to come directly after the specified floating point number provided.
* s #sleep for specified number of seconds, this is the default
* m #sleep for specified number of minutes
* h #sleep for specified number of hours
* d #sleep for specified number of days

Additionally, the following command options can be specified:
* --help #display and exit
* --version #output version info and exit

Furthermore, when multiple times are specified after sleep, sleep will delay for the sum of the provided times. Times may be provided in any combination of seconds, minutes, hours, or days. They can also be provided as floating point numbers.

#### Example command

~~~ bash
sleep 1
~~~

##### Break it down
sleeps for 1 second, since seconds are the default when no additional option is provided

#### Example command
~~~ bash
sleep 1m 30s
~~~

##### Break it down
sleeps for 1 minute and 30 seconds
