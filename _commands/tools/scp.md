---
---

scp
-------
`scp`, or _Secure Copy_, is used to securely transfer files based on the _Secure Shell protocol_ (`ssh`). Unlike `cp`, `scp` can transfer files from or to a remote host.

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

The `-r` option asks `scp` to _recursively_ copy an entire directory, copying the directory itself along with all of its contents.

### Optional Preliminary Steps

#### `ssh` alias
~~~ bash
$ scp source alias:destination
$ scp alias:source destination
~~~

If you're going to be typing a remote host multiple times, one of the first things you should do is create an alias (e.g. `caen`). This is achieved simply by adding a few lines to `~/.ssh/config`, as shown in the example below.

~~~ sh
Host caen
	Hostname uniqname@login-course-2fa.engin.umich.edu
	User uniqname
~~~

