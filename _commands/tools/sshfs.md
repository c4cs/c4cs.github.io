---
---

sshfs
-------

`sshfs` is used to mount a remote ssh server to a local mountpoint to allow the _secure_ transfer of files or directories to and from a remote host. Similar to "scp" except instead of having to manually transfer the files from the command line, files can be simply "mv" or "cp" into a folder. `sshfs` uses the _secure shell protocol_ (`ssh`) to transfer the file to or from the server and the "FUSE" libraries to produce the mountpoint.

~~~ bash
$ sshfs mnt_pnt user@host:dest_folder
~~~
<!--more-->

### Useful Options / Examples

#### `sshfs -o reconnect`
~~~ bash
$ sshfs -o reconnect mnt_pnt user@host:dest_folder
~~~

#### Break it down
* The `-o reconnect` tells `sshfs` to automatically reconnect to the remote server if the connection is lost.


#### `sshfs -o sshfs_sync`
~~~ bash
$ sshfs -o sshfs_sync mnt_pnt user@host:dest_folder
~~~

#### Break it down
* The `-o sshfs_sync` tells `sshfs` to immediately write the changes out to the ssh server instead of caching them locally. This is useful if remotely building code since any changes that are locally cached would not be built on the server.  

#### `sshfs -o no_readahead`
~~~ bash
$ sshfs -o no_readahead mnt_pnt user@host:dest_folder
~~~

#### Break it down
* The `-o no_readahead` tells `sshfs` to read all files directly from the server instead of a local cache of the files. This is useful for reading files that may update such as a build report or a program output.



