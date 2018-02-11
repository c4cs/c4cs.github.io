---
---

date
-------
`date` displays the current date, or a calculated date in a desired format. Can also be used by the root user to set the system's clock.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ date
Sun Feb 11 15:17:03 EST 2018
$ date -d "1995-12-5"
Tue Dec  5 00:00:00 EST 1995
~~~

<!--more-->

### Useful Options / Examples

#### `date -d "YEAR-MONTH-DAY" or VALID DATE MONTH STRING`

Display a specific date. List of valid date month strings can be found online.


~~~ bash
connor@connor-VirtualBox:~$ date -d "1995-12-5"
Tue Dec  5 00:00:00 EST 1995
~~~



~~~ bash
connor@connor-VirtualBox:~$ date -d now
Sun Feb 11 15:56:48 EST 2018
~~~



~~~ bash
connor@connor-VirtualBox:~$ date -d yesterday
Sat Feb 10 15:57:58 EST 2018
~~~



~~~ bash
connor@connor-VirtualBox:~$ date -d last-tuesday
Tue Feb  6 00:00:00 EST 2018
~~~



#### `date +"Formatting String"`

Display a desired formatted version of the date using the full list of format options that can be found at 
https://www.computerhope.com/unix/update.htm

Here are some examples of formatted strings.



~~~ bash
connor@connor-VirtualBox:~$ date +"Abbreviated weekday name = %a"
Abbreviated weekday name = Sun
~~~



~~~ bash
connor@connor-VirtualBox:~$ date +"Full weekday name = %A"
Abbreviated weekday name = Sunday
~~~



~~~ bash
connor@connor-VirtualBox:~$ date +"Military Hour = %H Regular Hour = %I"
Military Hour = 15 Regular Hour = 03
~~~



~~~ bash
connor@connor-VirtualBox:~$ date +"Time = %T = %H:%M:%S"
Time = 15:48:53 = 15:48:53
~~~



~~~ bash
connor@connor-VirtualBox:~$ date +"What day of the year is %m-%d? It is the %j day of the year"
What day of the year is 02-11? It is the 042 day of the year
~~~




#### `TZ="VALID TIMEZONE" date`

Time zone can be changed by updating the timezone variable to a valid timezone that can be found in /usr/share/zoneinfo/.



~~~ bash
connor@connor-VirtualBox:~$ TZ=PST date
Sun Feb 11 21:04:17 PST 2018
~~~




#### `date --set="VALID DATE TIME STRING"`

Set the system's time to the given date and time.


~~~ bash
connor@connor-VirtualBox:~$ date --set="20180211 16:10"
connor@connor-VirtualBox:~$ date now
Sun Feb 11 16:10:01 EST 2018
~~~




#### `Using date in a script`

Script Input:

~~~ bash
#/bin/bash
DATE=`date`
echo $DATE
TIME1=`date -d "$DATE" +"%T"`
echo $TIME1
TIME2=`date -d "$DATE" +"%H:%M:%S"`
echo $TIME2
if [ "$TIME1" == "$TIME2" ]
then
	echo "Formatting worked"
else
	echo "Formatting didn't work"
fi
~~~


Terminal Output after running:

~~~ bash
Sun Feb 11 16:34:05 EST 2018
16:34:05
16:34:05
Formatting worked
~~~




