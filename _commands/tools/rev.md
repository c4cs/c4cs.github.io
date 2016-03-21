---
---

rev
---

Rev reverses the lines of a file. This utility will copy the files specified in the command to standard output while reversing the order of each of the characters in every line. If no files are specified, it will use standard input and read in lines.  

The general format is:

~~~ bash
$ rev [file...]
~~~

<!--more-->

A simple example is:

~~~ bash
$ rev HelloWorld.cpp
~~~

This will output !dlroW olleH if the file was "Hello World!"

### Useful Options

### Examples

~~~ bash 
$ echo "Pat Pannuto" | rev
~~~

Will output: otunnaP taP

~~~ bash
$ rev myFile.cpp
~~~

Will output: 
oG
!eulB

If the original file said:
Go
Blue!

 
