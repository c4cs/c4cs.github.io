---
---

su
---
<!-- one line explanation would go here -->
su, described as "super user", "switch user", or "substitute user", allows a user to execute commands with the privileges of another user by starting another shell instance. This is different from sudo, which does not activate the root shell and runs only a single command.

<!-- minimal example -->
~~~ bash
johndoe@example:~$ su janedoe
Password:
janedoe@example:/home/johndoe$ exit
logout
johndoe@example:~$
~~~

<!--more-->

### Useful Options / Examples
The syntax for su is su [options] [username]  
with options:  
-c, --command COMMAND  
-, -l, --login    

#### Example command
~~~ bash
johndoe@example:~$ su -c 'ls /home/janedoe' - janedoe
~~~

##### This command switches to janedoe's account and lists the contents of janedoe's home directory


#### Example command
~~~ bash
johndoe@example:~$ su -l janedoe
~~~

##### This command provides the login environment of the user.
