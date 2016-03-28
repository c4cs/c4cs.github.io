---
---

Ditto
-------

Ditto is an OSX command that copies the entire contents of a working directory to another, new location.

~~~ bash
ditto /old/directory/ /new/directory/
~~~

<!--more-->

### Details
Ditto perserves file resources forks and metadata, in addition to ownership attributes. This ensures a more exact copy than cp. Ditto can also be used to copy a file or direct to a source that doesn't exist - in that case, ditto will automatically create the source for the user.


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

#### --norsrc
~~~ bash
ditto --nosrc /old /new
~~~

#### Break it down
The --norsrc flag allows you to copy files and directories without copying their accompanying metadata and resource forks.

#### --password
~~~ bash
ditto --password /old /new
~~~

#### Break it down
The --password flag allows the user to copy password protected zip archives. Ditto will prompt a user for a password if the --password flag is included, and will print an error message if it is not specified where it is needed.

#### --nopreserveHFSCompression
~~~ bash
ditto --nopreserveHFSCompression /old /new
~~~

#### Break it down
The --nopreserveHFSCompression flag deviates from ditto's default operations, causing the compression of files compressed using HFS compression to not be preserved. It is only supported on Mac OSX 10.6 or later, and is one reason to use ditto over cp.

#### --zLibCompressionLevel
~~~ bash
ditto --zLibCompressionLevel 5 /old /new
~~~

#### Break it down
The --zLibCompressionLevel flag allows the user to specify a compression level from 0 to 9 when copying a PKZip archive.


#### -X
~~~ bash
ditto -X /old /new
~~~

#### Break it down
The -X flag allows is used to prevent descending into directories with a different device id when copying multiple directories.

