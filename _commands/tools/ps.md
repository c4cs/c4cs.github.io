---
---

ps
-------

`ps` provides a snapshot of current processes

~~~ bash
#Shows four items of information for each process currently under the current user and from this terminal
#PID: Process ID
#TTY: Terminal Type (name of console that user logged into)
#TIME: System time used on process
#CMD: Name of command that launched process
`ps`
  PID TTY          TIME CMD
 1612 pts/17   00:00:00 bash
25671 pts/17   00:00:07 gedit
26195 pts/17   00:00:00 ps
~~~

<!--more-->

### Useful Options / Examples
For any example, you can pipe to `less` by using `| less` after any command to allow you to scroll

### Example Command

#### `ps -aux`
~~~ bash
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.5 119340  3828 ?        Ss   14:02   0:01 /sbin/init spla
root         2  0.0  0.0      0     0 ?        S    14:02   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    14:02   0:00 [ksoftirqd/0]
~~~

### Break it down
* `a`: Shows processes from all users
* `u`: Displays process' owner (USER)
* `x`: Also show processes which are not attached to a terminal

### Example Command

#### `ps -fp 3476,26520`
~~~ bash
 PID  PPID  C STIME TTY          TIME CMD
yosami    3476   934  0 14:07 ?        00:00:00 deja-dup --prompt
yosami   26520   934  0 15:19 ?        00:00:00 /usr/lib/x86_64-linux-gnu/notify-osd
~~~

### Break it down
* `f`: Show full formatting
* `p`: Filter by process id's the following integers separated by comma's. 
In this example, I filtered for procces id's (PPID) that were equal to 34766 and 26520

### Example Command

#### `ps -aux | grep bash`
~~~ bash
i    1612  0.0  0.4  27296  3164 pts/17   Ss   14:04   0:00 bash
yosami   26294  0.0  0.6  27176  4756 pts/2    Ss+  14:51   0:00 bash
yosami   26317  0.0  0.7  27288  5716 pts/18   Ss   14:52   0:00 bash
yosami   26710  0.0  0.2  13696  2068 pts/18   S+   15:28   0:00 grep --color=auto bash
~~~

### Break it down
* Here, we are doing the same thig as `ps -aux`, but we are now piping the output to bash
* Grep will then filter out any results that do not contain the string: "bash"

### Example Command

#### `ps aux --sort=-pcpu`
~~~ bash
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
yosami    1209 12.9 20.1 1233468 152908 ?      Ssl  14:03  14:06 compiz
yosami   26751  9.2  9.3 688380 70752 pts/17   Sl+  15:40   1:05 ruby2.1 /usr/lo
root       917  5.5 11.3 419240 86440 tty7     Ss+  14:03   6:05 /usr/bin/X -cor
~~~

### Break it down
* We are using `ps -aux`, which determines the contents of the results, but we sorting the results using `--sort`. The - sign means we are sorting according to a descending order and the pcpu means we are sorting according to CPU Usage or %CPU.
