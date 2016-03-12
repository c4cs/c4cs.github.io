---
---

pwd
--

`pwd` is used to **P**rint the **W**orking (current) **D**irectory to the screen.

~~~ bash
:directory/subdirectory username$ pwd
/Users/username/directory/subdirectory
~~~

<!--more-->

### Useful Options / Examples

#### `pwd -P`
~~~ bash
$ pwd -P
/actual/file/path/without/symlinks
~~~

##### Break it down

 * The `-P` option returns the actual (**P**hysical) file path, with no symlinks. 

