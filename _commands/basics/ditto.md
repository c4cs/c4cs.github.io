---
---

Ditto
-------

Ditto is an OSX command that copies the entire contents of a working directory to another, new location.

~~~ bash
ditto /old/directory/ /new/directory/
~~~

<!--more-->

### Useful Options / Examples

#### -V 
~~~ bash
ditto -V old new
>>>copying old
copying file ./bla.txt ...
10 bytes for ./bla.txt
~~~

#### Break it down
-V stands for verbose, and is a flag that prints 2 lines for every file being copied: one line displaying the name of the file, and one displaying the file size.
