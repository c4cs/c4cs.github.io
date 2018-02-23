---
---

date
-------
<!-- one line explanation would go here -->
`date` returns a system time specified by the user.
<!-- minimal example -->
~~~ bash
$ date
Tue Feb  6 12:42:38 EST 2018
$ date +%Y%m%d
20180206
~~~

<!--more-->

This command returns the standard current time. With different options and parameters, it can also return other system time with different formats.

### Useful Options / Examples

The syntax for using options is:

~~~ bash
date [options]
~~~

The useful options include:

~~~ bash
%a  show abbreviated weekday name (eg. Mon)
%b  show abbreviated month name (eg. Jan)
%c  show date and time
%s  show the current seconds from 1970-01-01 00:00:00 UTC
~~~

Here are some examples of using options:

~~~ bash
$ date +%a%b
TueFeb
~~~

~~~ bash
$ date +%s
1517939576
~~~

The syntax for using flags is:

~~~ bash
date [-u|--utc|--universal] [MMDDhhmm[[CC]YY][.ss]]
~~~

Here is a simple example of using flag:

"date -u" shows the current system time in UTC.
~~~ bash
date --universal
Wed Feb 14 07:16:15 UTC 2018
~~~

"date -s" sets the current system time to the string specified. 
~~~ bash
date -s "02/23/2018 02:23:00"
Fri Feb 23 02:23:00 EST 2018
~~~

"date -r FILE" returns the last modified time of FILE.
~~~ bash
date -r 398
Fri Feb 16 01:49:10 EST 2018
~~~

"date -f FILE" returns the time as the file specified.
Contents in thie file TIMEFILE:
~~~ bash
now
02/11/2018 02:23:00
01/01/2000 00:00:00
~~~
~~~ bash
date -f TIMEFILE
b 23 14:49:51 EST 2018
b 11 02:23:00 EST 2018
n 1 00:00:00 EST 2000
~~~

For more help, run
~~~ bash
man date
~~~
to view the manual of this command.

Reference: https://linode.com/docs/tools-reference/tools/use-the-date-command-in-linux/
