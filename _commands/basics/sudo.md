---
---

sudo
---

<!--more-->

`sudo` (super user do) is a command that allows a permitted user to execute a command as a superuser or another user (as specified in the sudoers file). In other words, it runs the command with elevated privileges. 

### Examples

~~~ bash
$ reboot
reboot: must be superuser.
$ sudo reboot
[sudo] password for XXXX:
The system is going down for reboot NOW!
~~~

We needed the elevated privileges of sudo in order to reboot from the terminal in the above example.

~~~ bash
$ sudo apt-get install wbritish
~~~

By having sudo in the command we ran the command with elevated privileges and were able to install the british-english word list. This was used in homework 5 to give sufficient privileges to instal British-English word list.

### Useful Options / Examples
There's some good commands you can run with sudo!

sudo -b will run the command in the background.Useful to avoid long list of output as it runs

sudo -s will run the shell specificed with elevated privlages, giving you the #prompt

sudo -h will cause sudo to print a help message and exit

sudo -l will list the allowed (and forbidden) commands for the invoking user on the current host

There are many, many more which can be found online!



