---
---

chmod
-------

Changes the permissions of a file or directory.
Stands for **ch**ange file **mod**e bits

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

The binary representation of the first argument should correspond to the modes (ie. read write exectue - rwx - permissions) you want to set the given file to. For example, if you want to set the mode to read-able, write-able and not executable, this is represented in binary as 110, which corresponds to 6 in octal. In this example, 6 should be given as one of the digits in the first argument.

The first argument should be a 3 digit octal number. The first digit will change the file's owners permissions, second digit will change the files group permissions, the thrid digit will change other (anybody else) permissions.

Note: `chmod` only changes the mode bits. To change the owner of this file or group that owns this file, use [chown/chgrp](/commands/chown_chgrp.html)


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
-rw-rw-rw- 1 37465  index.html
$ chmod -r index.html               # -r will set all read mode bits to 0
$ ls -go --time-style=+
total 40
--w------- 1 37465  index.html      # note all read mode bits are now 0
$ chmod +x index.html               # +x will make this file execute-able for all classes
$ ls -go --time-style=+
total 40
--wx--x--x 1 37465  index.html
~~~


~~~ bash
$ ls -go --time-style=+
total 40
-rw-rw-rw- 1 37465  index.html
$ chmod g-rw index.html             # removes rw mode bits from group (g)
$ ls -go --time-style=+
total 40
-rw----rw- 1 37465  index.html
$ chmod o-w index.html              # not o here stands for others (not owner)
$ chmod u-w index.html              # u refers to owner
$ ls -go --time-style=+
total 40
-r-----r-- 1 37465  index.html
~~~


