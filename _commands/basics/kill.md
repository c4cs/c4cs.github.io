---
---

kill
--

`kill` is used to send a signal to a process.

~~~ bash
$kkill [-s] [-l] PID(s)
~~~

--signal: Specify the signal to be sent.
-l: List signal names. 

<!--more-->

### Useful Options / Examples


#### `$ kill -9 PID`

Kills a signal using its PID. 
-9 stands for the SIGKILL signal.

#### `$ ps ux`

Displays all the running applications together with its PID.

~~~ bash
USER   PID  %CPU %MEM      VSZ    RSS   TT  STAT STARTED      TIME COMMAND
name     579   7.8  1.3  3655068 213376   ??  S     8:50PM   0:27.94 /Application
name     470   3.4  2.1  3631392 344480   ??  S     8:32PM   1:36.03 /Application
~~~

#### `$ kill -l`

~~~ bash
 1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL
 5) SIGTRAP	 6) SIGABRT	 7) SIGEMT	 8) SIGFPE
 9) SIGKILL	10) SIGBUS	11) SIGSEGV	12) SIGSYS
13) SIGPIPE	14) SIGALRM	15) SIGTERM	16) SIGURG
17) SIGSTOP	18) SIGTSTP	19) SIGCONT	20) SIGCHLD
21) SIGTTIN	22) SIGTTOU	23) SIGIO	24) SIGXCPU
25) SIGXFSZ	26) SIGVTALRM	27) SIGPROF	28) SIGWINCH
29) SIGINFO	30) SIGUSR1	31) SIGUSR2
~~~

Lists the available signal choices in a tabular format.

#### `$ kill -9 -1`

Kills all processes that can be killed.
