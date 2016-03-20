---
---

scp
-------

`scp` is used to make a _secure copy_ of files or directories to and from a remote host. Similar to "cp" except either the source or destination should be a remote host. You'll want to run this command from your local machine.

~~~ bash
$ scp source user@host:destination
$ scp user@host:source destination
~~~

<!--more-->

### Useful Options / Examples

#### `scp -r`
~~~ bash
$ scp -r source dest
~~~

#### Break it down
* The `-r` option asks `scp` to _recursively_ copy an entire directory

#### `scp -c`
~~~ bash
$ scp -c source dest
~~~

##### Break it down
* The `-c` option asks `scp` to select a _cipher_ to encrypt the data being transferred.

