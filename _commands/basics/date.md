---
---

date
-------
<!-- one line explanation would go here -->
`date` returns a system time the user specified.
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

~~~ bash
$ date --help
~~~
Run this command to display a list of options.

The useful options include:

~~~ bash
%a  show abbreviated weekday name (eg. Mon)
%b  show abbreviated month name (eg. Jan)
%c  show date and time
%s  show the current seconds from 1970-01-01 00:00:00 UTC
~~~

For more help, run
~~~ bash
man date
~~~
to view the manual of this command.

#### Example command

~~~ bash
$ date +%s
1517939576
~~~

##### Break it down

#### Example command

~~~ bash
$ date +%a%b
TueFeb
~~~

##### Break it down

Reference: https://linode.com/docs/tools-reference/tools/use-the-date-command-in-linux/
