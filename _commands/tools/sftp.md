---
---

sftp
-------

`sftp` is short for SSH File Transfer Protocol, also known as Secure File Transfer Protocol, enables secure file transfer capabilities 
between networked hosts. Unlike the `scp`, `sftp` additionally provides remote file system management functionality, allowing applications 
to resume interrupted file transfers, list the contents of remote directories, and delete remote files.


### Useful Options / Examples

We can establish an SSH connection and then open up an SFTP session using that connection by issuing the following command:
~~~ bash
$ sftp username@remote_hostname_or_IP
~~~
<!--more-->

#### Break it down

* We can navigate remote files/ directories using same commands as usual, e.g `cd`, `ls`, `ls -a`, `pwd`, `mkdir`, ... ...

* To navigate local files/ directories, add '`l`' infront of the command, e.g `lcd`, `lls`, `lls -a`, `lpwd`, `lmkdir`, ... ...

#### Break it down

* If we would like download files/ directories from our remote host, we can do so by issuing the following command:

~~~ bash
sftp> get remoteFile
sftp> get -r remoteDirectory
~~~
<!--more-->

We can copy the remote file to a different name by specifying the name afterwards:

~~~ bash
sftp> get remoteFile localFile
~~~
<!--more-->

* Transferring files/ directories to the remote system is just as easily accomplished by using the appropriately named "put" command:

~~~ bash
sftp> put localFile
sftp> put -r localDirectory
~~~
<!--more-->


#### Break it down

* `!` enables you to exit to the Unix shell prompt, where you can enter commands. To get back to SFTP, enter `exit`. 
If you combine ! with a command (e.g., `!pwd`), SFTP will execute the command without dropping you to the Unix prompt.

* `exit` (or `quit`)	let you close the connection to the remote computer and exit SFTP.

* `help` (or `?`)	to get help on the use of SFTP commands.
