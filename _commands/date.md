---
---

date
-------

The date command is used to print out, or change the value of, the system's time and date information.

~~~ bash
date [OPTION] ... [+FORMAT]
~~~

<!--more-->

### Useful Options / Examples

#### date [-u|--utc|--universal] [MMDDhhmm[[CC]YY][.ss]]

##### OPTION:  -u, --utc, --universal 	 Print or set Coordinated Universal Time.

##### FORMAT: MMDDhhmm Month, Day, Hour, Minute    CCYY Century, Year

#### date -s "02/10/2018 11:30:00"

##### Set the system date and time to February 10, 2018, 11:30 AM

#### date "+DATE: %m/%d/%y%nTIME: %H:%M:%S"

##### Outputs the date and time in the following format: DATE: 02/08/01   TIME: 16:44:55