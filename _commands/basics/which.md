---
---

which
--

`which` is used to show the full path for each of the executables that you give it. Since command-line commands are also executables, `which` is usually used to find full paths to shell commands. By default, `which` will only give the first full path found for the given executable.

~~~ bash
$  which ls
/bin/ls
~~~

<!--more-->

### Useful Options / Examples


### `which ls vim emacs which`
~~~ bash
$  which ls vim emacs which
/bin/ls
/usr/bin/vim
/usr/bin/emacs
/usr/bin/which
~~~

##### Break it Down
 * The which command can be followed by any number of executables and will find the full paths that 
   are used to execute those commands had you typed them into your terminal. So, if you typed `ls`, you are actually executing /bin/ls. If you had typed `vim hello.cpp`, you are executing `/usr/bin/vim hello.cpp`. 
 * The command searches your `$PATH` to find the executables for the command. In the examples above, 
   `/usr/bin` and `/bin` were both in my PATH environment variable, which allowed `which` to find the commands above.


### `which -a test.sh`
~~~ bash
$  which test.sh
/Users/username/test.sh

$  which -a test.sh
/Users/username/test.sh
/Users/username/Documents/test.sh
~~~

##### Break it Down
 * For the `-a` option, I created two temporary .sh files with the same name and made them executables to
   show what the option does. I have also added `/Users/username` and `/Users/username/Documents` to my PATH to allow `which` to be able to find the executables named test.sh. One test.sh is placed in 
   `/Users/username` and the other in `/Users/username/Documents`. 
 * The first example shows the command without the `-a` option. The `which` command only shows one path
   to test.sh. However, once you use `-a`, two show up. `which -a` will use your PATH environment variable and search for all instances of the argument you give to `which` and print them out. So, in my example, `which` has found two instances of test.sh, one in `/Users/username` and the other in `/Users/username/Documents`.


### `which` Return Codes
~~~ bash
$ which ls
/bin/ls
$ echo $?
0

$ which nonexistentexe
$ echo $?
1

$ which ls which
/bin/ls
/usr/bin/which
$ echo $?
0

$ which ls nonexistentexe
/bin/ls
$ echo $?
1
~~~

##### Break it Down
 * Using `which` returns 0 if there were matches for the command found, and 1 if the command was not
   found.
 * If you have multiple arguments and at least one of the commands are not found, the return code
   is 1, signaling failure. Thus, only when all commands are found does `which` return 0 for success.


### Using `which` with builtin commands
~~~ bash
$ which history help
$ echo $?
1
~~~

##### Break it Down
 * Shell builtin commands are commands or functions that are executed directly in the
   shell. It does not use an executable program that the shell loads and executes like it does for `ls` or `which`. As a result, `which` will not give you a path to the executable for commands such as `history` or `help` or `logout` because there is no executable in the first place.     

