---
---

units
---
`units` converts quantities from one unit to another unit. It can be used interactively or non-interactively.


~~~ bash
$ units '10 meters' 'feet'
# displays * 32.808399 
           / .03048
~~~

<!--more-->

### Useful Options / Examples

To view available units, look in /usr/share/units/definitions.units

### Using `units` Interactively
Brings up an interactive prompt. The line with the * gives the result. The line with the / gives the inverse of the conversion factor. In the example below, 10 meters in 32.808399 feet, and 1 foot is .03038 decameters.

~~~ bash
$ units
$ You have: 10 meters
$ You want: feet
  * 32.808399
  / .03048
~~~

### Using `units` Non-interactively
Converts the temperature from fahrenheit to celcius using one line.

~~~ bash
$ units 'tempF(32)' 'tempC'
  0
~~~

