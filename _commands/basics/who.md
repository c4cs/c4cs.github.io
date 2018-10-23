---
---

who
---

`who` provides information about logins and currently logged-in users.

~~~ bash
$ who -H 
NAME		LINE		TIME			COMMENT
noahtutt	tty7		2018-10-21 11:46	(:0)
$ who -bH
NAME		LINE		TIME			PID COMMENT
		system boot	2018-10-21 11:46	
~~~

<!--more--->

### Useful Options / Examples

#### `who`
With no arguments, who prints the name, shell location, time of login, and any comments for the current user.

~~~ bash
$ who
noahtutt	tty7		2018-10-21 11:46	(:0)

#### `who -H`
Adds header information to the output of `who`. Can make the output easier to read or parse.

~~~ bash
$ who -H
NAME		LINE		TIME			COMMENT
noahtutt	tty7		2018-10-21 11:46	(:0)
~~~

#### `who -b`
Prints time of the last system boot. Note that, while the system boot process is recorded, it doesn't have an owner name or a process ID.

~~~ bash
$ who -bH
NAME		LINE		TIME			PID COMMENT
		system boot	2018-10-21 11:46	
~~~

### `who -r`
Prints the current run-level of the operating system. 

~~~ bash
$ who -r
		run-level 5	2018-10-21 11:46
~~~ 

The run-level of a Linux OS corresponds to a certain set of services that are expected to be running. Runlevel 5 corresponds to an operating system that is  
