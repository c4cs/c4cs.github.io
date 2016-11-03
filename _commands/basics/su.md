---
---

su
---

`su` (substitute user) is a command to change a login session's owner
without the owner having to first log out of the session. (as specified 
in the [su Command](https://www.techonthenet.com/linux/commands/su.php)). In
other words, it is called the switch user command

__Note:__ It is most commonly employed to change the ownership from
an ordinary user to the administrative user. Therefore it is oftern
refered as the superuser command.



~~~ bash
$ su root
~~~

<!--more-->

### Example

~~~ bash
$ su root
Password:
$ sudo alex
Password:
~~~

By default, the root account is disabled and doesn't have any password. To create
one, we can run as follow:

~~~ bash
$ sudo passwd root
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
~~~

Another way to login as root user:

~~~ bash
$ sudo -s
[sudo] password for alex:
~~~


### Useful Options / Examples
There's some good commands you can run with su!

`su -c` will run the command that directly follows it on the same line

~~~ bash
$ su -c 'ls /home/alex'
~~~

`su -` will change the current directory and environment to what would be expected if the new user
had logged on to a new session. The following example will lead to the home directory of a user named
alex.

~~~ bash
$ su - alex
~~~ 




