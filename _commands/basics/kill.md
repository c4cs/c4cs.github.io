---
---

kill
--

`kill` is used to send signal to a process or to kill a process.
We typically use kill PID, where you know the PID of the process.
By default `kill` generates SIGTERM, to safely end a process.


~~~ bash
$ kill 7243
~~~

<!--more-->

### Useful Options / Examples

#### `kill [-s] %pid`
~~~ bash
$ ps -ef | grep vim
username    7243  7222  9 22:43 pts/2    00:00:00 vim

$ kill -9 7243
~~~

##### Break it down
 * `ps -ef` will print out all the processes running on the user's machine.
 Piping with `| grep vim` will only output processes with the name
 given, in this case only vim processes are printed. `kill -9 7243` is using
 SIGTERM -9 to send the end process (kill) signal to process 7243, which
 will kill that vim process.


#### `killall`
~~~ bash
$ killall -9 firefox
~~~

##### Break it down
 * `killall` allows a user to kill processes (using signal -9) by name, here the firefox process is being killed


#### `pkill`
~~~ bash
$ pgrep -l sample
12406 sample-server.p
12425 sample-server.p
12430 sample-garbagec

$ pkill -9 sample
~~~

##### Break it down
 * `pgrep` displays the process ID and process name of the matching processes. `pkill` can send signal
 to any process by specifying the full name or partial name. So there is no need for you to find out
 the PID of the process to send the signal.