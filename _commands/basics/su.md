---
---

su
---

`su` (substitute user) is a command to change a login session's owner
without the owner having to first log out of the session. (as specified 
in the [su Command](https://www.techonthenet.com/linux/commands/su.php)). In
other words, it is called the switch user command

__Note:__ It is most commonly employed to change the ownership from
an ordinary user to the administrative user. Therefore it is often
refered as the superuser command.

~~~ bash
$sudo su root
~~~

<!--more-->

### Example
Let's suppose there is a user named alex.
By default, the root account is disabled and doesn't have any password.
To access root, we can run:

~~~ bash
$ sudo su root
[sudo] password for alex: 
root@alex-VirtualBox:/home/alex#
~~~

Another way to login as root user:

~~~ bash
$ sudo -s
[sudo] password for alex:
~~~

Here it asks for alex's password not root password.

### Useful Options / Examples
There's some good commands you can run with su!

`su -c` will run the command that directly follows it on the same line

~~~ bash
$ su -c 'ls /home/alex'
~~~

`su -` will change the current directory and environment to what would be expected if the new user had logged on to a new session. 

If you are a superuser on the box and would like to masquerade as user alex,
you can run:

~~~ bash
$ sudo su - alex
~~~

