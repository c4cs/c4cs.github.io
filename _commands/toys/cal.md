---
---

cal
-------
cal is a program that displays a calendar
<!-- one line explanation would go here -->


<!-- minimal example -->
~~~ bash
$ cal
~~~

<!--more-->

### Useful Options
~~~ bash
 Usage: cal [-mjy] [[month] year]
 -m: Display monday as the first day of the week
 -j: Display julian dates (days one-based, numbered from January 1)
 -y: Displays a calendar for the current year
~~~




#### Example command
~~~ bash
cal               "shows calendar of current month with current day highlighted"
cal -m march 2017 "shows the month of march and year 2017"
cal -j march 2017 "shows the month of march in the number of days starting from January 1st"
cal -y 2013	  "shows all 12 months in the year 2013"
~~~
