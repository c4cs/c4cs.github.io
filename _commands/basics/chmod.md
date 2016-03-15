---
---

chmod
-------

Changes the permissions of a file or directory.
Stands for **ch**ange file **m**od **b**its

~~~ bash
$ ls -go --time-style=+
total 40
-rw-r--r-- 1 37465  index.html
$ chmod 666 index.html
$ ls -go --time-style=+
total 40
-rw-rw-rw- 1 74981  index.html
~~~

<!--more-->

### Details
The first argument to `chmod` determines the bitset of permissions you want to change the file given in the second argument.

The bitset should correspond to rwx (read write exectue) permissions. e.g. 6 becomes 110 which is read-able write-able and not executable

The first argument should be a 3 digit number. The first digit will change the file's owners permissions, second digit will change the files group permissions, the thrid digit will change other (anybody else) permissions.



### Examples
~~~ bash
$ ls -go --time-style=+
total 40
-rw-r--r-- 1 37465  index.html
$ chmod 755 index.html
$ ls -go --time-style=+
total 40
-rwxr-xr-x 1 37465  index.html      # note the permissions have change to (rwx)(rx)(rx)
~~~



### Shortcuts can be used
~~~ bash
$ ls -go --time-style=+
total 40
-rw-r--r-- 1 37465  index.html
$ chmod -r index.html               # -r will reovke all read permissoins from everybody (or equivalently +r, -r, +x, -x)
$ ls -go --time-style=+
total 40
--w------- 1 37465  index.html      # note all read permissions have been revoked
~~~


~~~ bash
$ ls -go --time-style=+
total 40
-r--r--r-- 1 37465  index.html
$ chmod +w index.html               # you can only add write permission for yourself (owner)
$ ls -go --time-style=+
total 40
-rw-r--r-- 1 37465  index.html
~~~

