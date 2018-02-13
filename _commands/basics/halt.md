---
---

halt
--

`halt`, together with `poweroff`, `reboot` are commands you can run as root to stop the system hardware. Specifically, `halt` instructs the hardware to stop all CPU functions. These commands require superuser privileges. If you are not logged in as root, you will need to prefix the command with `sudo` or the signal will not be sent.

~~~ bash
$ sudo halt
[sudo] password for xxx: 
~~~

<!--more-->

### Options/Examples

#### `halt -p`


Invoking `halt` with option `-p` would instruct the `halt` command to instead behave as `poweroff`.



#### `halt --verbose`


It would output slightly more verbose messages when rebooting, which can be useful for debugging problems with shutdown.


#### `halt --help`


It would print a short help text and exit.


### Exit Status


On success, 0 is returned, a non-zero failure code otherwise.

