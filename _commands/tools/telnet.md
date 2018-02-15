---
---
telnet
---
`telnet` is a command that uses the Telnet protocol. Telnet (short for TErminal NETwork) is a protocol designed to provide a command line interface for remotely communicating with a device or system. `telnet` can invoked on its own, or it can be invoked with a host and port argument.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ telnet
telnet>
$ telnet examplesite.com 22
Trying 1.2.3.4...
Connected to examplesite.com
~~~

<!--more-->

### Useful Options / Examples

#### `telnet [hostname] [port]`

Providing the hostname and port after the 'telnet' command will automatically connect to the hostname on the port given. This is the most common use case for this tool. 

#### `telnet -b [address]`

Binds a local socket to the specified address

~~~ bash
$ telnet -b 1.2.3.4
1.2.3.4 bound to port 22.
~~~

#### `telnet send [arguments]`

Send a telnet protocol character sequence the remote host that currently has an open connection.Following are some useful arguments.

* ip - This will send a TELNET IP (interrupt process) string sequence which can be used to abort the current process running on the remote machine.

* ayt - Sends a TELNET AYT(ARE YOU THERE)? string sequence to the remote machine to check if the machine is active. The remote machine can choose whether or not to respond.

#### `telnet status`

Will give the status of telnet and the status of any open connections to remote machines. In addition, it will also give information about escape sequences and any other settings that have been configured.

~~~ bash
$ telnet
telnet> status
No connection.
Escape character is '^]'.
telnet>
~~~ 

#### Sending Email

One of the most useful features of telnet, is that if the host that is connected to has an open SMTP port, the tool can be used to send emails to that host. You start the command similarly to opening a regular connection, but open on port 25 which is the SMTP port.

~~~ bash
$ telnet examplemailserver.com 25
~~~

If the command worked, you will receive a response along the lines of the following.

~~~ bash
220 examplemailserver.com Example Mail Server 1.0
~~~
