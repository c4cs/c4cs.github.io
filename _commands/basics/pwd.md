---
---

pwd
--

`pwd` is used to _print working directory_


~~~ bash
$ cd ~
$ pwd
/home/c4cs
$ cd /usr/games
$ pwd
/usr/games
$ ls
cowsay  cowthink  espdiff  fortune
~~~

<!--more-->


### Useful Options / Examples

- #### `pwd` with symlinks

#### `pwd`
* Normally pwd will print directory through symlinks.

~~~ bash
$ ln -s /tmp/ tmp_sym
$ cd tmp_sym
$ pwd       #with no arguments
/home/c4cs/tmp_sym
~~~

#### `pwd -P`
*  Can bypass this through physical (-P) pwd

~~~ bash
$ ln -s /tmp/ tmp_sym
$ cd tmp_sym
$ pwd -P
/tmp
~~~

