---
---

touch
---
`touch` Creates a new empty file and can also change timestamps on existing files. Useful for creating empty files quickly.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ touch main.cpp
~~~

<!--more-->

### Useful Options / Examples

#### `touch -a filename1 filename2 filename3 ...`

Allows you to create multiple empty files at the same time.

~~~ bash
$ touch main.cpp file1.h file1.cpp
~~~
This command is creating 3 new empty files: `main.cpp`, `file1.h`, and `file1.cpp`.

#### `touch -a filename`

Allows user to change the access time.

~~~ bash
$ touch -a main.cpp
~~~
This changes the access time for `main.cpp` to the current time. 

#### `touch -m filename`

Allows user to change modification time.

~~~ bash
$ touch -m main.cpp
~~~ 
This changes the modification time of `main.cpp` to the current time.
