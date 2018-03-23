---
---

units
---
`units` converts quantities from one unit to another unit. It can be used interactively or non-interactively.

To use interactively, type units into the command prompt:

~~~ bash
$ units
~~~

To use non-interactively:

~~~ bash
$ units [options] ['from-unit' 'to-unit']
~~~

<!--more-->

## Useful Options / Examples

To view available units, look in /usr/share/units/definitions.units

### Using `units` Interactively
Typing `units` into the terminal brings up an interactive prompt. The interactive prompt will ask for the unit that you have. Then, it will ask for the unit that you want. In the output, the line with the `*` gives the result. The line with the `/` gives the inverse of the conversion factor. In the example below, 10 meters is 32.808399 feet, and 1 foot is 0.03048 decameters.

~~~ bash
$ units
You have: 10 meters
You want: feet
  * 32.808399
  / 0.03048
~~~

### Using `units` Non-Interactively
Make conversions using one line.

~~~ bash
$ units '10 meters' 'feet'
   * 32.808399
   / 0.03048
~~~

### Useful flags:
`units --digits <integer>`

The `--digits` flag specifies the output to a certain number of digits specified by the options. 

Example:

~~~ bash
$ units --digits 3 '10 meters' 'feet'
   * 32.8
   / 0.305
~~~


`units --verbose`

The `--verbose` flag shows slightly more verbose output.

Example:

~~~ bash
$ units --verbose '10 meters' 'feet'
   10 meters = 32.808399 feet
   10 meters = (1 / 0.03048) feet
~~~


### Converting Temperatures
There is a special syntax for temperatures. Specifically, Fahrenheit can be indicated by `tempF` and Celcius can be indicated by `tempC`. To assign a value to either of these units, use a number enclosed in parentheses after the unit. `tempF(32)` means 32 degrees Fahrenheit.

Example:

~~~ bash
$ units 'tempF(32)' 'tempC'
   0
~~~

