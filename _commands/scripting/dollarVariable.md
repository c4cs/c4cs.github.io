---
---

$ (Dollar sign prefix to a variable)
-------

'$variable'
The dollar sign prefix is used to print the value of 'variable'.

~~~ bash
echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
~~~

<!--more-->

### Useful Options / Examples

#### 'VARX="5"; echo $VARX'
~~~ bash
$ VARX=5; echo $VARX
5
~~~


##### Break it down
* The variable VARX has the value 5, and in order to print this value, $ must be used.

#### 'EXEC="./hello.out"; $EXEC'
~~~bash
$ EXEC="./hello.out"; $EXEC
Hello World!
~~~ 

##### Break it down

* The terminal replaces the $EXEC with its value, and reads it as if it was typed by the user. Therefore, the terminal runs the executable 'hello.out'. 

