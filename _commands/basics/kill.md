---
---

kill
--
The kill command is used on Linux systems to terminate process by its process id without having to reboot the system.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
The syntax is kill [signal or option] PID(s)
$kill 27410         Means killing a current running process with process id 27410
~~~

<!--more-->

### Useful Options / Examples

#### Example command

### `kill -9 PID`
Actually, `kill` is a command to send signals to the specified process, each process has a set of standard handlers by the operating systems, and signal 9 called SIGKILL can almost guarantee to kill a process if the default signal 15 can't kill it.

#### Example command

### `kill -l` 
Although `kill -9 PID` is the most common kill commands and you probably don't need to know more, but if you really need to know the full list of about 60 different signals, type `kill -l`

#### Example command

### `ps -aux | less` 
Yes, you want to kill a process, but you first need to know the process id of that process. By the command above you can see brief information of current running processes including its PID, thus you can kill that process by its process id shown below "PID". The following is partial result of this command.                                                                


~~~
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1 119620  1128 ?        Ss   13:26   0:00 /sbin/init splash
root         2  0.0  0.0      0     0 ?        S    13:26   0:00 [kthreadd]
root         4  0.0  0.0      0     0 ?        S<   13:26   0:00 [kworker/0:0H]
root         6  0.0  0.0      0     0 ?        S<   13:26   0:00 [mm_percpu_wq]
root         7  0.0  0.0      0     0 ?        S    13:26   0:00 [ksoftirqd/0]
root         8  0.0  0.0      0     0 ?        S    13:26   0:00 [rcu_sched]
root         9  0.0  0.0      0     0 ?        S    13:26   0:00 [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    13:26   0:00 [migration/0]
~~~
