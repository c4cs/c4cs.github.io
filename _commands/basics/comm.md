---
---

comm
---
Compares two sorted files line by line and writes three columns to standard output.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
# content of file1.txt
$ cat file1.txt
abc
def
ghi

# content of file2.txt
$ cat file2.txt
abc
ghi
klm

# compare file1.txt and file2.txt: first column showing unique lines of first file, 
# second column showing unique lines of second file, thrird column showing matched 
# lines of both files
$ comm file1.txt file2.txt
		abc
def
		ghi
	klm
~~~

<!--more-->
~~~ bash
# suppress first column
$ comm -1 file1.txt file2.txt
	abc
	ghi
klm

# suppress second column
$ comm -2 file1.txt file2.txt
	abc
def
	ghi

# suppress third column
$ comm -3 file1.txt file2.txt
def
	klm
~~~
### Useful Options / Examples

#### Example command

##### Break it down

#### Example command

##### Break it down
