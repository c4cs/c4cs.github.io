---
---

time
---

<!-- one line explanation would go here -->


`time` outputs the runtime of a program that is given as an argument.

<!-- minimal example -->
~~~ bash
$ time cd

real 	0m0.008s
user 	0m0.008s
sys 	0m0.000s
~~~

<!--more-->

**real:** refers to the amount of time spent in the user program called.

**user:** refers to the amount of time spent in the process called.

**sys:** refers to the amount of time spent in the kernel during the call.

### Useful Options / Examples

There are two `time` commands available to most terminals. There is the `time` that is a shell built-in command and there is a `time` that is a command similar to `ls`. You must specify the path to the non shell built-in command because otherwise the built-in `time` command takes precedence. They work identically when called with no arguments, but you can call the non-built-in time command with some additional flags that offer more functionality. The below examples use the `/usr/bin/time` command (the non built-in command).

#### Example command

##### `time -o [FILE] [COMMAND]`
`time -o` can be used to put the output of time into a file. This method includes extra information that is not part of the default time. It has cpu usage, inputs and outputs statisics as well. Another thing to note is that the -o command can only be used when using the absolute path of the time command on some installs. Be careful as this command overwrites the contents of FILE.

~~~ bash
	$ /usr/bin/time -o myfile.txt sleep 4

myfile.txt:
	0.00user 0.00system 0:04.00elapsed 0%CPU (0avgtext+0avgdata 1788maxresident)k
	0inputs+0outputs (0major+74minor)pagefaults 0swaps
~~~

#### Example command

##### `time -o [FILE] -a [COMMAND]`
`time -o -a` allows you to append the same information as time -o into a file instead of overwriting it.

~~~ bash
	$ /usr/bin/time -o myfile.txt -a sleep 8

myfile.txt:
	0.00user 0.00system 0:00.04elapsed 0%CPU (0avgtext+0avgdata 2056maxresident)k
	0inputs+0outputs (0major+82minor)pagefaults 0swaps
	0.00user 0.00system 0:08.00elapsed 0%CPU (0avgtext+0avgdata 1848maxresident)k
	0inputs+0outputs (0major+74minor)pagefaults 0swaps
~~~
