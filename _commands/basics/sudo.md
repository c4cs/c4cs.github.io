---
---

sudo
---

`sudo` (super user do) is a command that allows a permitted user to execute a
command as a superuser or another user (as specified in the [sudoers
file](https://help.ubuntu.com/community/Sudoers)). In
other words, it runs the command with elevated privileges.

__Note:__ The root user has permission to do _anything_ on your system; acting
as root can be dangerous!  That is why it's best practice to only use `sudo`
when you need it, and to double check the command before running.



~~~ bash
$ sudo apt-get install wbritish
~~~

<!--more-->

### Example

~~~ bash
$ reboot
reboot: must be superuser.
$ sudo reboot
[sudo] password for XXXX:
The system is going down for reboot NOW!
~~~

We needed the elevated privileges of sudo in order to reboot from the terminal in the above example.

As shown throughout this class, sudo is extremely handy. We find ourselves often typing sudo in before a command and it's good to know what it means!


### Useful Options / Examples
There's some good commands you can run with sudo!

`sudo -b` will run the command in the background. Useful to avoid long list of output as it runs

`sudo -s` will run the shell specified with elevated privileges, giving you the `#` prompt

`sudo -h` will cause sudo to print a help message and exit

`sudo -l` will list the allowed (and forbidden) commands for the invoking user on the current host

There are many, many more which can be found online!



