<!--more-->

---
---

sudo
---

Are you tired of getting "Access Denied?". Never fear, sudo is here!
`sudo` (super user do) is a command that allows a permitted user to execute a command as a superuser or another user (as specified in the sudoers file). In other words, it runs the command with elevated privileges. This is very useful to have and we have seen this in use many times already in EECS 398 when we install various packages.

For example, if you wanted to reboot but you kept getting "Access Denied!", you could instead try


~~~ bash
$ reboot
reboot: must be superuser.
sudo reboot
[sudo] password for XXXX:
The system is going down for reboot NOW!
~~~

Another example is in homework 5 when we needed to install the british-english worst list

~~~ bash
$ sudo apt-get install wbritish
~~~---
---

sudo
---


`sudo` (super user do) is a command that allows a permitted user to execute a command as a superuser or another user (as specified in the sudoers file). In other words, it runs the command with elevated privileges. 

For example, if you wanted to reboot but you kept getting "Access Denied!", you could instead try


~~~ bash
$ reboot
reboot: must be superuser.
sudo reboot
[sudo] password for XXXX:
The system is going down for reboot NOW!
~~~

Another example is in homework 5 when we needed to install the british-english worst list

~~~ bash
$ sudo apt-get install wbritish
~~~

By having sudo in the command we ran the command with elevated privileges and were able to install the british-english word list.

### Useful Options / Examples
There's some good commands you can run with sudo!

sudo-b will run the command in the background.Useful to avoid long list of output as it runs

sudo-s will run the shell specificed with elevated privlages, giving you the #prompt

sudo su - will make you the root user and load you custom user environment variables.






### Useful Options / Examples
There's some good commands you can run with sudo!

sudo-b will run the command in the background.Useful to avoid long list of output as it runs

sudo-s will run the shell specificed with elevated privlages, giving you the #prompt

sudo su - will make you the root user and load you custom user environment variables.





