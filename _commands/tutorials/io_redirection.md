---

I/O Redirection
---------------

The I/O redirection operators `>`, `>>`, `<`, and `|`  allow us to read and write input and output from files, and pass output from one program to another.

~~~ bash
$ echo "I love bash!" > message.txt
$ cowsay -w < message.txt
$ echo "I love bash so much!" >> message.txt
$ cosway -w < message.txt
$ cat message | grep "bash"
~~~

<!--more-->

### Basic Usage

#### `>` operator
Puts the output from the program on the left of the operator into the file named on the right of the operator. Will overwrite all of current contents of the file, and will create the file if it doesn't exist yet.

~~~ bash
$ echo "Text in a file" > message.txt
$ cat message.txt
Text in a file
~~~

#### `>>` operator
Appends the output from the program on the left of the operator to the contents of the file named on the right of the operator. Will not overwrite any of the current contents of the file, and will create the file if it doesn't already exist.

~~~ bash
$ echo "Text in a file" >> message.txt
$ echo "More text in a file" >> message.txt
$ cat message.txt 
Text in a file
More text in a file
~~~

#### `<` operator
Feeds the contents of the file on the right into the input of the program on the left. Will not modify any of the contents of the file, and will throw an error if it doesnt already exist.

~~~ bash 
$ echo "I love bash" > message.txt
$ cowsay -w < message.txt
 _____________
< I love bash >
 -------------
        \   ^__^
         \  (OO)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
~~~

#### `|` operator 
Feeds the output of the command on the left into the input of the command on the right. 

~~~ bash
$ echo "Pipes are fun!" | grep -c "Pipe"
1  
~~~

### Useful Examples

#### Stream Selection
By default, the `>`, `>>`, and `|` operators all operate on the standard output stream `stdout`, and leave the standard error stream `stderr` untouched. If we want to redirect just the error messages from a program, we can do so by selecting stream 2:

~~~ bash
$ git commit 
fatal: Not a git repository (or any of the parent directories): .git
$ git commit > git_errors.txt
$ cat git_errors.txt # will generate no output
$ git commit 2> git_errors.txt
$ cat git_errors.txt
fatal: Not a git repository (or any of the parent directories): .git
~~~

We can't directly change the input source of the `|` operator in this fashion, it always reads from `stdout`. If we want to pipe `stderr` only, we can first point `stderr` at `stdout` and then point `stdout` at nothing:

~~~ bash
$ git commit 
fatal: Not a git repository (or any of the parent directories): .git
$ git commit 2>&1 1>/dev/null | grep -c "fatal"
1
~~~

