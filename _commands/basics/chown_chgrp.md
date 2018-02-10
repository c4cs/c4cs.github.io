---
---

chown/chgrp
-----------
`chown` (or `chgrp`) is used to change the *owner* or *group* of a given file (or both!)

<!-- minimal example -->
~~~ bash
## Change *Owner* ##
$ ls -l magicfile
-rw-rw-r-- 1 bestowner bestgroup 3130 Feb 10 12:02 magicfile

$ chown mehowner magicfile

$ ls -l magicfile
-rw-rw-r-- 1 mehowner bestgroup 3130 Feb 10 12:03 alias.md

## Change *Group* ##
$ ls -l magicfile
-rw-rw-r-- 1 bestowner bestgroup 3130 Feb 10 12:04 magicfile

$ chown :plebgroup magicfile

$ ls -l magicfile
-rw-rw-r-- 1 bestowner plebgroup 3130 Feb 10 12:05 alias.md

## Change Owner **and** Group ##
$ ls -l magicfile
-rw-rw-r-- 1 bestowner bestgroup 3130 Feb 10 12:02 magicfile

$ chown mehowner:plebgroup magicfile

$ ls -l magicfile
-rw-rw-r-- 1 mehowner plebgroup 3130 Feb 10 12:03 alias.md
~~~

<!--more-->

### Useful Options / Examples

#### Example command

##### Break it down

#### Example command

##### Break it down
