---
---

poweroff and reboot
-------

poweroff instructs your system to power down.
reboot instructs your sysem to reboot.
~~~ bash
poweroff [flag]
reboot [flag]
~~~

### Flags
~~~
--verbose
~~~
Enables verbose messages when reboot, allowing for more informative debugging.
~~~

### Examples

#### Example command
~~~ bash
poweroff
~~~

#### Example command (equivalent to previous)
~~~ bash
halt -p
~~~

#### Example command (equivalent to previous)
~~~ bash
halt --poweroff
~~~

#### Example command
~~~ bash
reboot
~~~

### Important note
if you aren't logged in as the root user you wil need to use the sudo command:
~~~ bash
sudo poweroff
~~~

~~~ bash
sudo reboot
~~~



