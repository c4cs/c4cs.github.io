---
---

true
--

`true` a statement that logically evaluates to true. It is often used to check whether statements evaluated succesfully or not. It is the logical inverse of 'false', also a unix command.

~~~ bash
$ true
$ rm -rf directory || true
~~~

<!--more-->

### Useful Options / Examples

#### `true`

This just logically evaluates to true. This is most useful in scripting 

~~~ bash
while true
do
   echo 'infinite loop'
done
~~~

#### `rm -rf directory || true`

This is useful because sometimes we want to make sure that a command that could end with an error will return with exit status zero, to make sure that a script will continue running.

