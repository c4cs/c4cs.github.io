---
---

chmod
-------
<!--TODO: Add documentation for this command by submitting a pull request.-->
<!-- one line explanation would go here -->
`chmod` (change mode) is the command to change permissions to system objects (files and directories).

<!-- minimal example -->
~~~ bash
$ chmod u+x filename
~~~


<!--more-->

### Useful Options / Examples

#### `chmod`

~~~bash
$ chmod [references][operator][modes] file ...
~~~

References include:

1. `u` for user
2. `g` for group
3. `o` for other
 
Operators include:

1. `+` adds specified modes to specified classes
2. `-` removes specified nodes to specified classes
3. `=` will set specified classes to exact specified modes

Modes include:

1. `r` (read)
2. `w` (write)
3. `x` (execute)

----

#### `chmod [reference(s)][operator][mode(s)] file`

~~~bash
$ chmod u+x file 
$ chmod g-w, uo=rw file 
~~~

##### Break it down

* The first command will add write permission for file to user
* The second command will remove write permission for group, and set user and other to have read and write permissions only

----

#### `chmod --reference=[file1] [file2]`

~~~bash
$ chmod --reference=file1 file2 
~~~

##### Break it down

* Sets file2's permissions to be the same as file1

----

#### `chmod -R [reference(s)][operator][mode(s)] directory`

~~~bash
$ chmod -R u+x directory-name/
~~~

##### Break it down

* Adds execute permission to users for all files under directory 

----

#### `chmod [reference(s)][operator][mode(s)] *`

~~~bash
$ chmod u+x *
~~~

##### Break it down

* Adds execute permision to users for all subdirectories under directory

----
