---
---

time
--

`time` writes a message to standard output giving timing statistics about the program that was run.

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
