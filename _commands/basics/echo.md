---
---

echo
---
`echo` is a built in command that writes its arguments into standard input.

The general format is:
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
echo [options(s)] [string(s)] 
~~~

<!--more-->

A simple example is:

~~~bash
$ echo Hello World
Hello World
~~~

### Useful Options / Examples

#### `echo [string(s)]`
When one or more strings are provided as arguments, echo prints all strings to the screen.

~~~bash
$ echo This is an echo command.
This is an echo command.
~~~

#### `echo $var`
Along with printing out whatever is passed to it, `echo` can also print out the values of variables.

~~~bash
$ x=1
$ echo x is equal to $x.
x is equal to 1. 
~~~
 * The variable name must be present directly after the dollar-sign($), so that the shell knows to substitute the variable value for its name.

Along with other variables `echo` can also be used to print out values of system variables such as `PATH`, `HOME`, etc.

~~~bash
$ echo $PATH
/home/biswash/bin:/home/biswash/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
$ echo $HOME
/home/biswash
~~~

#### `echo -n [string(s)]`
The `-n` flag removes trailing new line characters when printing to the screen.

~~~bash
$ echo Hi! && echo This is a new-line test.
Hi!
This is a new line test.
$ echo -n Hi! && echo -n This is a new line test.
Hi!This is a new line test.-$
~~~
 * This `-n` flag removed the trailing new-line after 'Hi!' and 'This is a new line test.
'

#### `echo -e '[string(s)]'`
The `-e` flag allows special characters to be enabled.

~~~bash
$ echo 'Hi!\nThis is a special character test.'
Hi!\nThis is a special character test.
$ echo -e 'Hi!\nThis is a special character test.'
Hi!
This is a special character test.
~~~
 * When not using the `-e` flag, `\n` was printed as a normal string, however after using this flag, it reads `\n` as a new line command.

~~~bash
This is a special character test.
$ echo -e 'Hi! \bThis is a backspace test.'
Hi!This is a backspace test.
~~~

 * Some common special characters enabled by `-e` flag are the new-line character `\n`, the horizontal tab `\t`, the backspace character `\b`, etc.

#### `echo *`
`echo` can also do pattern matching.

~~~bash
$ ls
text.txt
$ echo There is *.txt text files in this directory.
There is test.txt files in this directory.
~~~
 * Here, `echo` looked for all files in the directory with .txt in their name, and printed them to the outpute instead of *.txt.

#### `echo [string(s)] > file`
`echo` is also commonly used to write items to files instead of the screen.

~~~bash
$ echo This is text. > temp.txt
$ cat temp.txt
This is text.
~~~
 * Using `echo` along with the >, we redirected the output from the screen to the file temp.txt. And using another command called `cat`, we printed the content of temp.txt onto the screen.
