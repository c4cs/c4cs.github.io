---
---

kill
--

<!-- one line explanation would go here -->
The kill command terminates a process (running program) without having to log out or reboot the computer.

<!-- minimal example -->
~~~ bash
$ kill [signal or option] PID
~~~

<!--more-->

### Useful Options / Examples
Options
	-<signal>
		Specify the signal to be sent. The signal can be specified by using name or number
		
	-l
		List signal names
		
	-9
		Sends an even stronger kill signal

#### Example command
Example 
	kill -9 485

##### Break it down
kills the process with the PID number 485 with a strong kill signal
#### Example command
Example
	kill 6328 925 7721

##### Break it down
kills all those processes with the default kill signal
