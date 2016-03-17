---
---

echo
-------

Prints out a line of text out to the terminal.

~~~ bash
$ echo "I love EECS 398!"
I love EECS 398!
~~~

<!--more-->

### Useful Options / Examples

#### `echo -e` vs `echo -E`
~~~ bash
$ echo -e "I love \nEECS 398!"
I love 
EECS 398!
$ echo -E "I love \nEECS 398!"
I love \nEECS 398!
$ echo "I love \nEECS 398!"
I love \nEECS 398!
~~~
##### Break it down
`echo` with the `-e` flag will recongize the escape character `'\'` and allow sequences such as `'\a'` (alert), `'\n'` (new line), `'\\'` (backslash).
When the `-E` flag is specified, the escape character `'\'` is treated as ordinary text. The latter is also default behavior if neither flag is specified.

#### `echo -n`
~~~ bash
$ echo -n "I love EECS 398!"
I love EECS 398!$ echo "I love EECS 398!"
I love EECS 398!
~~~

##### Break it down
`echo` with the `-n` flag will not print a new line character at the end of the string. This causes the next bash prompt to appear right next to the text.
By default `echo` will print the newline character if the flag is not specified.
