---
---

wc
---
'wc' is a command used to find out the number of lines, word count, byte or character counts in the files specified.

~~~ bash
$ wc [options] filenames
~~~

<!--more-->

### Basic Usage

~~~ bash
$ wc filename.txt
12 16 112 filename.txt
~~~

Here, the file called filename.txt has **12** lines, **16** words, and has a byte count of **112**.

### Useful Options

~~~ bash
wc -l : Prints the number of lines in a file.
wc -w : prints the number of words in a file.
wc -c : Displays the count of bytes in a file.
wc -m : prints the count of characters from a file.
wc -L : prints only the length of the longest line in a file.
~~~
