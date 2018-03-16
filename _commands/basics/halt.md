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


Invoking `halt` with option `-p` would instruct the `halt` command to instead behave as `poweroff`. `poweroff` is a terminal command that would allow a system administrator to shutdown the system.

~~~ bash
$ poweroff --help
poweroff [OPTIONS...]

Power off the system.

     --help      Show this help
     --halt      Halt the machine
  -p --poweroff  Switch off the machine
     --reboot    Reboot the machine
  -f --force     Force immediate halt/power-off/reboot
  -w --wtmp-only Don't halt/power-off/reboot, just write wtmp record
  -d --no-wtmp   Don't write wtmp record
     --no-wall   Don't send wall message before halt/power-off/reboot
 
~~~



#### `halt --verbose`


It would output slightly more verbose messages when rebooting, which can be useful for debugging problems with shutdown.


#### `halt --help`


It would print a short help text and exit.

~~~ bash
halt [OPTIONS...]

Halt the system.

     --help      Show this help
     --halt      Halt the machine
  -p --poweroff  Switch off the machine
     --reboot    Reboot the machine
  -f --force     Force immediate halt/power-off/reboot
  -w --wtmp-only Don't halt/power-off/reboot, just write wtmp record
  -d --no-wtmp   Don't write wtmp record
     --no-wall   Don't send wall message before halt/power-off/reboot
~~~


### Exit Status


On success, 0 is returned, a non-zero failure code otherwise.

