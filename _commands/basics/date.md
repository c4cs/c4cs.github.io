---
---

date
-------

This command can get you the system time in terminal.

~~~ bash
$ date
Thu Mar 24 15:09:46 EDT 2016
~~~

<!--more-->

### Useful Options

Option 1: `date --set="24 MAR 2015 18:00:00"`

The system date will now have been changed to 24th of March 2015 and 6pm.

Option 2: `date -r filename`

This line will  tell you when the file was last modified.

Option 3: `date -u`
 
Displays current UTC time.

Option 4: `TZ='Asia/Dhaka' date`

~~~ bash
$ TZ='Asia/Dhaka' date
Mon Mar 28 03:31:33 BDT 2016
$ TZ='Asia/Ajmer' date
Sun Mar 27 21:32:44 Asia 2016
~~~

This will give you the time at the location you have entered. Just replace Asia with desired continent and Dhaka with desired city. For example, 'America/Los_Angeles' would give the time for LA. Note that not every city is in the database and wrong time can show up. For example, "Ajmer" was not in the directory and thus "Asia" showed up instead of a certain time zone.

Option 5: `date --date='TZ="Asia/Dhaka" 10:00 Mar 28'`

This line will give you what the local date and time will be when it is 10AM on the 28th of March in Dhaka. We can even replace Mar 28 and replace it with words like 'next Mon' and the code will still work.

 
