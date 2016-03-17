---
---

rsync
--

`rsync` is file copying tool. It can be used locally or to and from a host. It is most commonly used to copy only the changes made to a file. 

~~~ bash
$ rsync dir1/file dir2/
~~~

<!--more-->

### Useful Options / Examples

#### `rsync -r`

recursive

#### `rsync -t`

preserve modification times

#### `rsync -W`

Transfer whole file (not just the changes made)
