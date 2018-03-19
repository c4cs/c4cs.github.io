---
---

poweroff
--------

`poweroff` is used allow a system administrator to poweroff the system

~~~ bash
$ poweroff [options]
~~~


<!--more-->

### Details
 * When called with --force or when in runlevel 0 or 6, this tool invokes the
   reboot system call itself and directly reboots the system.
 * Otherwise, this simply invokes the shutdown tool with the appropriate
   arguments without passing REBOOTCOMMAND argument.

### Useful Options

#### `poweroff --f`
#### `poweroff --force`

~~~bash
$ poweroff -f
~~~

 * Does not invoke shutdown, and instead performs the actual command you would expect from the name.



#### `poweroff -p`

~~~bash
$ poweroff -p
~~~

 * Instructs the halt command to instead behave as poweroff


#### `poweroff -w`
#### `poweroff -wtmp-only`

~~~bash
$ poweroff -w

~~~

 * Does not call shutdown or the reboot system call.
 * Instead only writes the shutdown record to /var/log/wtmp.



#### `poweroff --verbose`

~~~bash
$ poweroff --verbose
~~~

 * `--verbose` will output slightly more verbose messages when rebooting.
 * Useful for debugging problems with shutdown.


### Final details
If you aren't logged in as the system administrator, you must insert a `sudo` to before the poweroff command like so:

~~~bash
$ sudo poweroff
~~~

