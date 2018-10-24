---
---

$ (Dollar sign prefix to a variable)
-------

'$variable'
The prefix '$' lets the shell interpret 'variable' as a variable.

~~~ bash
$ echo $PATH
/home/username/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/mnt/c/Program Files (x86)
~~~

<!--more-->

### Useful Options / Examples

#### 'MY_VAR="10"; echo $MY_VAR'
~~~ bash
$ MY_VAR=10; echo $MY_VAR
10
~~~


##### Break it down
* MY_VAR has value 10, and '$' must be used to print this value.

#### 'EXEC="./correct.out"; $EXEC'
~~~bash
$ EXEC="./correct.out"; $EXEC
correct output
~~~

##### Break it down

* The terminal replaces the $EXEC with its value, and reads it as if it was typed by the user. Therefore, the terminal runs the executable 'correct.out'.
