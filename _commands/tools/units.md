---
---

units
---
TODO: Add documentation for this command by submitting a pull request.
`units` converts quantities from one unit to another unit. It can be used interactively or non-interactively.


~~~ bash
$ units '10 meters' 'feet'
# displays * 32.808399 
#          / .03048
~~~

<!--more-->

### Useful Options / Examples

### To see available units, look in /usr/share/units/definitions.units

### Example Command

#### Using `units` Interactively

~~~ bash
$ units
$ You have: 10 meters
$ You want: feet
  * 32.808399
  / .03048
~~~

### Brings up an interactive prompt. The line with the '*' gives the result. The line with the '/' gives the inverse of the conversion factor. In the example above, 10 meters is 32.808399 feet, and 1 foot is .03048 decameters.

#### Using `units` Non-interactively

~~~ bash
$ units 'tempF(32)' 'tempC'
$ 0
~~~

### Converts the temperature from fahrenheit to celcius in one line.

