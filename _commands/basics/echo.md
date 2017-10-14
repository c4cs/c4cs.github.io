---
---

echo
---

`echo` is used to display message on screen, and write given string to standard output, with each a space between each and a newline after the last one.  `echo` is implemented as builtin command in many command shells like bash, ksh, csh.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ echo "Hello World"
Hello World
$ echo Hello World
Hello World
~~~

<!--more-->


### Useful Options / Examples

#### Example command
`echo` output can be redirected into a file for easy use. 
~~~ bash
$ echo Hello World > example.txt
$ cat example.txt
Hello World
~~~
#### Example command
`echo` output can also be appended to a file.
~~~ bash
$ echo Hello > example.txt
$ echo This is a new line. >> example.txt
$ cat example.txt 
Hello
This is a new line.
~~~
#### Example command
##### `echo -n` 
`-n` is a usefule flag if you don't want the trailing newline after the string

~~~ bash
$ echo -n "Hello World." > example.txt
$ echo " There is not new line before me." >> example.txt
$ cat example.txt
Hello World. There is not new line before me.
~~~

##### `echo -e`
`-e` flag is used to enable the backslash-escaped characters in following table:
~~~ bash
$ echo -e -n "Hello World.\nThis is a new line.\n"
Hello World.
This is a newline.
~~~
|       |                                        Backslash-escaped characters                                        |
|-------|:----------------------------------------------------------------------------------------------------------:|
|   \\\  |                                    a literal backslash character ("\\").                                    |
|   \a  |                                                  An alert.                                                 |
|   \b  |                                                 Backspace.                                                 |
|   \c  |                                    Produce no further output after this.                                   |
|   \e  |                        The escape character; equivalent to pressing the escape key.                        |
|   \f  |                                                  Form feed                                                 |
|   \n  |                                                  New line                                                  |
|   \r  |                                               Carriage Return                                              |
| \t    |                                               Horizontal tab                                               |
| \v    |                                                Vertical tab                                                |
| \\    |                                                  Backslash                                                 |
| \NNN  | The character whose ASCII code is NNN(octal); if NNN is not a valid octal number, it is printed literally. |
| \xnnn | The character whose ASCII code is the hexadecimal value nnn.                                               |


