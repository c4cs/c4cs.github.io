---
---

date
-------
TODO: Add documentation for this command by submitting a pull request.
<!-- one line explanation would go here -->
The date command displays the date and time your machine in the format of:
Day, Month, Date, Military Time, Time zone, Year
<!-- minimal example -->
~~~ bash
$ date [flags]
~~~

<!--more-->

### Useful Options / Examples
--date: Convert seconds since the epoch (January 1, 1970) to a date


-u: Display the date in UTC (Coordinated Universal) time.

TZ=\<location\>: Display the date and time at the location


#### Example command
Example: 
$ date --date='@1518562161'
 
##### Break it down
This will display "Tue Feb 13 17:49: 21 EST 2018"
The first date calls the date command
The --date converts time to date
The ='@...' specifies the number of seconds since January 1, 1970

#### Example command
Example:
$ date -u

##### Break it down
This will display the universal coordinated time (UTC)
The flag -u indicates you want UTC instead of the time on your current system.

