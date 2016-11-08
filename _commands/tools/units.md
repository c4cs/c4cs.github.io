---
---

units
--

`units` gives conversion rates from one scale to another. 

~~~ bash
$ units [-f unitsfile] [-q] [-v] [from-unit to-unit]...
~~~

<!--more-->

The command above will list the value you will need to multiply (*) or divide (/) your original number by to convert to your desired units listed.

The units are defined in an external data file. You can use the extensive data file that comes with this program, or you can provide your own data file to suit your needs. You can use the program interactively with prompts, or you can use it from the command line.

~~~ bash
$ units
~~~

with no command line arguments, input will be read from standard input.

Generally, use:

~~~ bash
$ units [from-unit] [to-unit]...
~~~

### Useful Examples

Below are some useful examples for units.

~~~ bash
$ units
586 units, 56 prefixes
You have: inches
You want: centimeters
	* 2.54
	/ 0.39370079
~~~

~~~ bash
$ units yds m
	* 0.9144
	/ 1.0936133
~~~

### Useful Options

Below are some important options for units.

~~~ bash
$ units --help
~~~

will display a help file and exit.

~~~bash
$ units --versions
~~~

will display version information and exit.

~~~ bash
$ units -f filename
$ units --file filename
~~~

Use filename as the units data file rather than the default units data file `units.dat`.

~~~bash
$ units --check-verbose
~~~

Like the `-check` option, this option prints a list of units that cannot be reduced.  But to help find unit  definitions that cause endless loops, it lists the units as they are checked.  If `units` hangs, then the last unit to be printed has a bad definition.