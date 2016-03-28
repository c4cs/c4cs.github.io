---
---

time
---
`time` prints out the total time elapsed, the time used by system overhead and the time used to execute the utility.
	
<!--more-->

### Situation

If you simply want to output the time it takes to run a command
	
~~~ bash
$ time ./project -m < input.txt
~~~

### Meaning:
`time` calls the bash time command, `./project`is the program you are trying to run,
`-m` is a flag for that program and `< input.txt `is the input file for the program.
Anything that appears after `./project` is taken like it would be without using the time command.
This will output the following:

~~~ bash
0.00user 0.00system 0:00.00elapsed 
0%CPU (0avgtext+0avgdata 3312maxresident)k
0inputs+0outputs (0major+135minor)pagefaults 0swaps
~~~

Where the user, system and elapsed times are in seconds.

### Situation:
	
If you want to output the time information to a file

~~~ bash
$ time -o out.txt ./project
~~~

### Meaning:
The `-o` flag (which is the same as `--output`) tells the computer to redirect the output for the
time command to the file `out.txt`. This flag will overwrite the file `out.txt`, however, if you
do not want to overwrite the file see the example below.

### Situation:
If you want to output the time information to a file but you do not want to overwrite said file

~~~ bash
$ time -a out.txt ./project
~~~
	
### Meaning:
The `-a` flag followed by a file `out.txt` tells the program to redirect the output from the time
command to the file `out.txt` but instead of overwritting the file, append the information to it.

### Situation:
If you only want to print out the user, system and total time

~~~ bash
$ time -f "\t%E real,\t%U user,\t%S sys" ./project
~~~

### Meaning:
The `-f` flag followed by the string `\t%E real,\t%U user,\t%S sys` tells the computer to format
the out put in the form:
 
	real	0m10.081s
	user	0m3.858s
	sys	0m0.408s

the `\t%E` real means print the string real followed by a tab (due to the `\t`) and then the elapsed time (wall-clock time)
used by the program. The `\t%U` user means print the string user followed by a tab and the total number of CPU-seconds that
the process used. Finally the `\t%S` sys prints the string `sys` followed by a tab and then the the total number of CPU-seconds
used by the system due to the program in seconds.

### Situation:
If you want to output as much information as possible about how long your code took to run

~~~bash
$ time -v ./project
~~~
	
### Meaning:
The `-v` (or `--verbose`) flag tells the computer to print out all of the time information it has. The output would look
something like the following:

	Command being timed: "./project"
	User time (seconds): 0.00
	System time (seconds): 0.00
	Percent of CPU this job got: 0%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:00.00
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 3236
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 0
	Minor (reclaiming a frame) page faults: 135
	Voluntary context switches: 2
	Involuntary context switches: 7
	Swaps: 0
	File system inputs: 24
	File system outputs: 0
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0
 		
### Situation:
If you want to do something that is not described above

~~~ bash
$ man time
~~~
	
### Meaning:
This will birng you to the manual page for time
