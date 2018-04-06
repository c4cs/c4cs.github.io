---
---

kill
--
`kill` is a command that ends a process by specifying its PID (process ID), either via a signal or forced termination. 
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
#List the running process

$ ps
PID TTY TIME CMD
1293 pts/5 00:00:00 MyProgram

#Then Kill it

$ kill 1293
[2]+ Terminated MyProgram
~~~

<!--more-->

### Note

The `kill` command has a misleading name because it does not actually kill processes. Rather, it sends signals to them. Each process is supplied with a set of standard signal handlers by the operating system in order to deal with incoming signals. When no signal is explicitly included in the command, signal 15, named `SIGTERM`, is sent by default. If this fails, the stronger signal 9, called `SIGKILL`, should be used. Note that the lower the signal number, the stronger the kill signal will be.



### Useful Options / Examples

To terminate a process, you can use `kill`. But first you need the pid of your process, which you can get by using `ps`, `pidof` or `pgrep`.

#### Example command

~~~bash

ps -A  #to get the pid, can be combined with grep

#-or-

pidof <name>

#-or-

pgrep <name>

kill <pid>

~~~

#### Break it down

`-A` flag for `ps` (process status) is to list all processes, it's useful to find out what's the name of the process you want to kill if you don't know it exactly.

`pidof` -- finds the process ID of a running program.

`pgrep` -- searches for all the named processes that can be specified as extended regular expression 
patterns, and—by default, returns their process ID. add `-l` flag to list PID and process name concurrently.

#### Example command

~~~bash

$ps

PID TTY          TIME CMD

20250 pts/18   00:00:00 MyProgram

$kill 20250
#no output

$ps -ef
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 16:19 ?        00:00:01 /sbin/init splash
root         2     0  0 16:19 ?        00:00:00 [kthreadd]
root         4     2  0 16:19 ?        00:00:00 [kworker/0:0H]
root         6     2  0 16:19 ?        00:00:00 [ksoftirqd/0]
......
yourname     1260  1116  0 16:19 ?        00:00:00 upstart-udev-bridge --daemon --u
yourname     1264  1116  0 16:19 ?        00:00:01 dbus-daemon --fork --session --a
......
yourname     2828  2334  1 16:57 pts/18   00:00:00 bash
yourname     2838  2828  0 16:57 pts/18   00:00:00 ps -ef
yourname     20250 2828  1 16:57 pts/18   00:00:00 MyProgram

$kill -9 20250
#no output

~~~

#### Break it down

Suppose the PID of a frozen or crashed program is found to be 20250, the following can usually terminate the process:

`kill 20250`

`ps -ef` or `ps -efl` can then be used to confirm that the process really has stopped.

`-e` Writes information to standard output about all processes, except kernel
processes.

`-f` Generates a full listing.

If the process has not stopped, then the more forceful `-9` option should be used, i.e.,

`kill -9 20250`

#### Similar Command

~~~bash
pkill -- End processes by a full or partial name.
$ps

PID TTY          TIME CMD

20250 pts/18   00:00:00 MyProgram

$pkill MyProgram
~~~

#### Break it down

Now instead of figuring out the PID of the process you want to terminate, you can try to terminate your program by just specifying the program name using `pkill`. Note that you can also specify which signal to send to kill the process, `pkill [signal]`. This option is only valid when given as the first argument to `pkill`. `pkill` has a lot more flags than `kill`. For more information, `man pkill` in the terminal.

### Common Kill Signals

~~~bash

Signal Name      Signal Value       Effect

SIGHUP		       1	    Hangup

SIGINT		       2	    Interrupt from keyboard

SIGQUIT		       3	    Quit

SIGABRT		       6	    Abort

SIGKILL		       9	    Kill signal

SIGTERM		       15	    Termination signal - allow an orderly shutdown

SIGSTOP		       17,19,23	    Stop the process

~~~

#### check out kill signal names

To get a full list of the signal names you can type `kill -l` in the terminal and see the full list. You can also get the corresponding signal name based on its exit status.

~~~bash
$kill -l 1

HUP

$kill -l 2

INT

~~~

#### kill process by signal names instead of signal number
Suppose the PID of a frozen or crashed program is found to be 20250, then the following three commands are equivalent :

`kill -s KILL 20250`

`kill -KILL 20250`

`kill -9 20250` 

### Conclusion

Obvious signs of misbehaving processes are programs that crash (i.e., appear to freeze or otherwise stop operating as expected) or that cannot be shut down normally (e.g., by clicking on a button or using using a menu command). The first step in such situation is to obtain the PID(s) of the offending process(es) by `ps`. And the next step is to `kill` \<PID\>. 
