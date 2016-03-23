---
---

chown/chgrp
-----------

`chown`/`chgrp` changes the user that _owns_ the file or the _group_ that owns the file.

~~~ bash
$ ls -l file
-rw-r--r--  1 ppannuto  ... file
$ sudo chown root file
$ ls -l file
-rw-r--r--  1 root      ... file
~~~

<!--more-->

### Useful Options / Examples


