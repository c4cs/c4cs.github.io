---
---

scp
-------

`scp` is used to make a _secure copy_ of files or directories to and from a remote host. Similar to "cp" except either the source or destination should be a remote host. `scp` uses _secure shell protocol_ (`ssh`) to tranfer the file to or from the server.

~~~ bash
$ scp source user@host:destination
$ scp user@host:source destination
~~~

<!--more-->

### Useful Options / Examples

#### `scp -r`
~~~ bash
$ scp -r source destination
~~~

#### Break it down
* The `-r` option asks `scp` to _recursively_ copy an entire directory, copying the directory itself along with all of its contents.

#### `ssh` alias
~~~ bash
$ scp source alias:destination
$ scp alias:source destination
~~~

#### Break it down
* If you get sick of typing out user@host, you can create an `ssh` alias by adding a few lines to `~/.ssh/config`. Change "alias" below to something short and easy to type:

~~~ sh
Host alias
	Hostname user@host
	User you
~~~

