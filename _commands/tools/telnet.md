---

telnet
-------

`telnet` is used to communicate with another host using the TELNET protocol.

~~~ bash
$ telnet
telnet>
~~~

<!--more-->

`telnet` can be used two main ways. The first is by simply typing

~~~ bash
$ telnet
~~~

this will cause it to enter command mode which is indicated by the prompt `telnet>`
When in command mode it will accept a number of possible commands such as hostname, port, username, source IP address. Exit the command mode by typing `quit`.

~~~ bash
$ telnet
telnet> open hostname.com
~~~ 

Alternatively, `telnet` can be used by specifing all the arguements in one line.

~~~ bash
$ telnet -l user host.com:8000
~~~

This command will attempt to connect to remote host host.com on port 8000 using
the login name user.

### Common Use Cases

`telnet` is one of the first protocols for communicating between computers.
It is rarely used now because it sends messages unencrypted. Other
communication protocols such as `ssh` are more secure and are used more
frequently.`telnet` can still be used to quickly check the connection to a
remote host before continuing communication using a more secure protocol. This
can be done with the command. 

~~~ bash
$ telnet host.com:8000
~~~

`telnet` can also be used to interactively follow a TCP stream. An example of that is shown here:

~~~bash
https://github.com/mterwill/networking-lecture/blob/master/notes.md#smtp
~~~

`telnet` is not completely obsolete however as it can be used to do incredible
things such as streaming a 20 minute ascii video of Star Wars 4!! Which can be
done by typing:

~~~ bash
$ telnet towel.blinkenlights.nl 23
~~~

To give you a hint the video looks something like this:

~~~ bash
                          8888888888  888    88888
                         88     88   88 88   88  88
                          8888  88  88   88  88888
                             88 88 888888888 88   88
                      88888888  88 88     88 88    888888

                      88  88  88   888    88888    888888
                      88  88  88  88 88   88  88  88
                      88 8888 88 88   88  88888    8888
                       888  888 888888888 88   88     88
                        88  88  88     88 88    8888888
~~~

### Useful Options / Examples
~~~ bash
-E Stops any character from being recognized as an escape character
-K Specifies no automatic login to the remote system
-a Attempt automatic login
-d Sets the initial value of the debug toggle to TRUE.
-l <user> Specify the user to try to connect with.
-s <src_addr> Set the source IP address for the telnet connection to <src_addr>
	which can be an IP address of a host name.
-x Turns on encryption of the data stream if possible.
-y Suppresses encryption of the data stream.
<host> Indicates the official name of the remote host.
<port> Indicates a port number, if not specified the default telnet port is used.
~~~

