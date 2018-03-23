---
---

sleep
--
The sleep command makes your script, terminal, or anything else that is bash executable go to sleep for however long you specify 

<!-- minimal example -->
~~~ bash
$ sleep 5s
~~~
 
<!--more-->

### Useful Options / Examples
The default command is sleep [NUMBER] [OPTION] and the number is interpreted by bash as in seconds however in the option arguement you can specify the sleep delay in seconds, minutes, hours, or days 

`s` - seconds

`m` - minutes

`h` - hours

`d` - days


Floating point numbers can also be used 

#### Example command

~~~ bash
$ sleep 3m
~~~~

This command causes the terminal to sleep for 3 minutes

#### Example command

~~~ bash
$ sleep 3.5s
~~~

This command causes the terminal to sleep for 3.5 seconds
