---
---

pwd
--

`pwd` stands for print working directory. `pwd` outputs the full pathname of the current work director. 

~~~ bash
$ pwd
/home/bo/Desktop
~~~

`pwd` can also be used to store the full path to the current directory. 

~~~ bash
x=$(pwd)
~~~

### Useful Options / Examples 

#### `pwd -L`

~~~ bash
$ ln -s . test
$ cd test && pwd
/home/bo/Desktop/test
$ /bin/pwd
/home/bo/Desktop
$ /bin/pwd -L
/home/bo/Desktop/test
~~~

##### Break it down
* `--logical` If the contents of the environment variable 'PWD' provide an absolute name of the current directory with no '.' or '..' components, but possibly with symbolic links, then output those contents. Otherwise, fall back to default -P handling. 
* The `-L` option displays the logical current working directory. Built in 'pwd' includes symlinks by default except when `-P` is used. `/bin/pwd` ignore symlinks and prints out the actual directory. For `/bin/pwd` to get the same result as the built in `pwd`, you must use the `-L` option. 

#### `pwd -P`

~~~ bash
$cd ~/bin
$pwd
/home/bo/bin
$pwd -P
/home/bo/realdata/scripts/utils
~~~

##### Break it down
* `--physical` Print a fully resolved name for the current directory. That is, all components of the printed name will be actual directory names--none will be symbolic links. 
