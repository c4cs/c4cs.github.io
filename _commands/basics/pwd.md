---
---

pwd
--

`pwd` is used to print the working directory. It is useful to see which directory you are currently controlling.

~~~ bash
$ pwd
/home/AndrewBoland/Desktop
$ cd ..
$ pwd
/home/AndrewBoland
~~~

<!--more-->

### Useful Options / Examples

#### `pwd -L`

~~~ bash
$ pwd -L
/home/AndrewBoland/Desktop/Pictures
~~~


##### Break it down
 * In the example above, Pictures is a symbolic link that has been placed in the directory `/home/AndrewBoland/Desktop`. The original location is in the directory `/home/AndrewBoland`
 * The `-L` option will use PWD from environment, even if it contains symbolic links.
 * If a symbolic link is created on the desktop and the user is in the symbolic link directory, the symbolic link's directory will be printed.

#### `pwd -P`

~~~ bash
$ pwd -P
/home/AndrewBoland/Pictures
~~~

##### Break it down
 * In the example above, Pictures is a symbolic link that has been placed in the directory `/home/AndrewBoland/Desktop`. The original location is in the directory `/home/AndrewBoland`
 * The `-P` option will avoid all symbolic links when printing the directory.
 * If a symbolic link is created and the user is in the symbolic link's directory, the symbolic link directory will not be printed and the directory from which the symbolic link came from will be printed.


