---

I/O Redirection
---------------

We often want to redirect input and output to and from files. The I/O redirection operators `<`, `>`, and `>>` allow us to do this.

~~~ bash
$ echo "I love bash!" > message.txt
$ cowsay -w < message.txt
$ echo "I love bash so much!" >> message.txt
$ cosway -w < message.txt
~~~

<!--more-->

### Good stuff coming  
