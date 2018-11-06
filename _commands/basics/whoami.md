---
---

whoami
-------

The whoami command will display the current user login name of the session.

~~~ bash
whoami
current_username
~~~

<!--more-->

### Useful Options / Examples

#### Who is sudo?
~~~ bash
whoami
meugur # your username will show up here
sudo whoami
root
~~~

##### In this situation, running 'sudo' will cause the current user to be root. So, when you run 'sudo whoami', the output indicates that the user is root when calling 'sudo'. This is an example of how 'whoami' could be useful in determining what permissions you currently have, if for some reason you are running into issues.

#### Equivalent to the whoami command is the 'id -un' command.
~~~ bash
id -un
meugur
sudo id -un
~~~

##### 'id -un' in this case returns the current user, and similarly, when run with 'sudo' it will return root. For more information on 'id', try out 'man id'.

#### Options

~~~ bash
whoami --help
~~~

##### Displays more information on the command.

~~~ bash
whoami --version
~~~

##### Displays the current version and author information of whoami.


