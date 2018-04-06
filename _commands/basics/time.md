---
---

time
--

`time` writes a message to standard output giving timing statistics about the program that was run. It outputs the times in 3 categories: real time, user time, and system time. 

~~~ bash 
$ time ./executable
real    0m0.116s
user    0m0.004s
sys     0m0.008s
~~~

<!--more-->

### Useful Options / Examples

`time [-p] command [arguments...]`

`time` can be used with the flag `-p` to print the timing summary in a portable POSIX format

~~~bash
$ time -p ls
real    0m0.116s
user    0m0.004s
sys     0m0.008s
~~~

### Output Description

The statistics printed consist of:

The elapsed real time between invocation and termination.	(real	0m0.116s)

The user CPU time.						(user	0m0.004s)

The system CPU time.						(sys	0m0.008s)

The real time is the true runtime of the program, from the start and finish of the call. The user time is the amount of CPU time spent in user mode-code within the process - in other words, the time spent by the CPU to execute the process. Lastly, the system time is the amount of CPU time spent within the kernel (in supervisor mode). The sum of user time and system time is the total amount of time that the CPU spends during the process, as opposed to the real time, which is more applicable to the amount of time that the user waits for during the process.
