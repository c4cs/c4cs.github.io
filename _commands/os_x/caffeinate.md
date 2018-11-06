---
---

caffeinate
---
`caffeinate` is a mac terminal command that prevents your mac going to sleep even while not in use and regardless of sleep settings.

~~~ bash
$ caffeinate
^C
$ 
~~~

<!--more-->

### Useful Options / Examples

### `caffeinate -d`
Create an assertion to prevent the display from sleeping.

### `-i`
Create an assertion to prevent the system from idle sleeping.


### `-m`
Create an assertion to prevent the disk from idle sleeping.

### `-s`
Prevents the whole system from going to sleep when connected to power.

#### Example command
Can use any of -d -i -m -s depending on needs.

Prevent display from sleeping.

~~~ bash
$ caffeinate -d
~~~

While firefox is open prevent display from sleeping.

~~~ bash
$ caffeinate -d /Applications/Firefox.app
~~~

Prevents sleep until terminal command is finished running. 

~~~ bash
$ caffeinate -i good_script.sh
~~~

### `caffeinate -t`
Specifies the time in seconds for how the the caffeinate command should be valid. Prevents sleep for specified number of seconds.

#### Example command
Keep your machine awake for 1 hour. 3600 seconds  = 1 hour

~~~ bash
$ caffeinate -t 3600
~~~

### `caffeinate -u`
Replicates current user activity or user is active e.g. as if someone were moving the mouse.If the display is off, this option turns the display on and prevents the display from going
           into idle sleep. If a timeout is not specified with '-t' option, then this assertion is
           default of 5 second timeout.

#### Example command
Wake up your mac for 2 second. Potentially useful if you ssh into your machine to wake up your machine.

~~~ bash
$ caffeinate -u -t 2
~~~

### `caffeinate -w`
Waits for the process with the specified pid to exit. Once the the process exits, the assertion is also released.

#### Example command
Prevents display from sleeping while process 12345 is still running.

~~~ bash
$ caffeinate -d -w 12345
~~~