---
---

diff
-------

`diff` is a tool to help debug as it takes in two files and prints the lines that are different. Prints nothing if they are the same. This is useful for checking output against correct output for test cases.

~~~ bash
$ echo "hi" > file1.txt
$ echo "hi" > file2.txt
$ echo "bye" >> file2.txt
$ diff file1.txt file2.txt
1a2
> bye
~~~

<!--more-->

### Useful Options / Examples

### `diff -q`

`diff -q` uses quiet mode on the diff. Prints nothing if they are the same.

~~~ bash
$ echo "hi" > file1.txt
$ echo "hi" > file2.txt
$ echo "bye" >> file2.txt
$ diff -q file1.txt file2.txt
Files file1.txt and file2.txt differ
$ echo "hi" > file3.txt
$ diff -q file1.txt file3.txt
~~~

### `diff -u`

`diff -u` uses unified mode on the diff. Prints nothing if they are the same. Shows both files combined in one. words with + in front need to be added while those with - in front need to be deleted.

~~~ bash
$ echo "hi" > file1.txt
$ echo "hi" > file2.txt
$ echo "bye" >> file2.txt
$ diff -u file1.txt file2.txt 
--- file1.txt	2018-10-24 22:48:55.349763378 -0400
+++ file2.txt	2018-10-24 22:59:03.265989078 -0400
@@ -1 +1,2 @@
 hi
+bye
~~~

### `diff -i`

`diff -i` checks if they're different without regards to case. Prints nothing if they are the same.

~~~ bash
$ echo "hi" > file1.txt
$ echo "Hi" > file4.txt
$ diff -i file1.txt file4.txt 
$ diff file1.txt file4.txt 
1c1
< hi
---
> Hi
~~~

### `diff -y`

`diff -y` prints the files, with | or > in front of lines to indicate differences, side by side each other. Prints both files even if they are the same.

~~~ bash
$ echo "hi" > file1.txt
$ echo "hi" > file3.txt
$ echo "Hi" > file4.txt
$ diff -y file1.txt file4.txt 
$ diff file1.txt file4.txt 
hi							      |	Hi
$ diff -y file1.txt file3.txt 
hi								hi
~~~
