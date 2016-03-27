---
---

sleep
--

`sleep` is a Unix command used to suspend program execution for a specified period of time. The default unit is seconds, but minutes, hours, or days may also be specified. 


~~~ bash
$ sleep 10
~~~

<!--more-->

### Arguments/Examples


#### sleep + number
`sleep` takes in one numerical argument. If no unit is specified, it is assumed to be in seconds.

~~~ bash
$ sleep 30
~~~
This causes the terminal to wait for 30 seconds.

~~~ bash 
$ sleep 3600
~~~
The above command causes the terminal to wait for 1 hour.



#### Changing Units
`sleep` can also be specified in minutes, hours, and days.

~~~ bash
$ sleep 10m
~~~
The above command tells the terminal to wait for 10 minutes.

~~~ bash
$ sleep 1h
~~~
Now the above command tells the terminal to wair for 1 hour. The same pattern is used for days, but a 'd' is specified instead of an 'h' or an 'm'. 

##### WARNING!!!
The sleep command doesn't support units (minutes, hours, etc) on OS X. Instead you have to do the math and convert to seconds. To hold up the terminal for 1 hour on OS X, you could execute:

~~~ bash
$ sleep 3600
~~~
OR
~~~ bash
$ sleep $((60 * 60))
~~~


##### NOTE
It is invalid to write 'sleep 2h30m' or 'sleep 2h 30m': 'sleep' only accepts one input. Alternatively, valid options include:

~~~ bash 
$ sleep 2.5h
~~~

OR

~~~ bash
$ sleep 2h; sleep 30m
~~~



#### Useful Examples

~~~ bash
$ sleep 1h; <command>
~~~

In the above example, the terminal will sleep for 1 hour before executing the specified command that follows. 

~~~ bash
$ (sleep 1h; <command>) &
~~~

In the above example, the terminal delays the execution of the specified command for 1 hour, but it waits in the background so that the terminal may still be used. 

~~~ bash
$ sleep 20m
 <ctrl> + z
~~~
 The 'ctrl' + z key stroke pauses a sleep command. 


~~~ bash
while true
do
    command
    sleep 20m
done
~~~
`sleep` can be used in loop to execute a command every so often. Do you want to mess with that weird OSU fan in your family? Make their computer start playing The Victors every 20 minutes!




### Options
None
