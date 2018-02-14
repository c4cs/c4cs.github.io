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
~~~d

Here is a simple example of using flag:

~~~ bash
date --universal
Wed Feb 14 07:16:15 UTC 2018
~~~

For more help, run
~~~ bash
man date
~~~
to view the manual of this command.

Reference: https://linode.com/docs/tools-reference/tools/use-the-date-command-in-linux/
