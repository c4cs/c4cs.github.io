---
---

grep
-------

`grep` is used to search files for the occurrence os string of characters matching a string (egrep can support called regular expressions often abbreviated as regex).

~~~ bash
$ grep regex file
line in file matching regex
~~~

<!--more-->

### Useful Options / Examples

#### Example command

####  grep -i -o string file
~~~ bash
$ grep -i HelLo helloworld.cpp
	cout << "hello world\n" << endl;
~~~
~~~ bash
$ grep HelLo helloworld.cpp
$ 
~~~
~~~ bash
$ grep -i -o HELLO helloworld.cpp
hello
~~~
~~~ bash 
$`grep -o hello helloworld.cpp
hello
~~~

##### Break it down

* The -i flag allows searches for case insensitive matches inside the the given file. As can be seen between the first and second examples above the only difference was the flag. From the first example we see a line with a substring that matches a case insensitive search. However, on the second example we dont see any output because it is a case sensitive search.
* The -o flag allows us to print just the matching substring from a file. For example, comparing the first and third example, we the first contains the entire line from a file while the third example only prints the word hello.
* Both flags can be used separately or together. As can be seen in examples three and four, these flags can be used to get the exact output, for example a case insensitive search (example three) or 
a case sensitive search for a word (example four).

#### Example command

####  grep -v string file
~~~ bash
$ grep -v hello helloworld.cpp
#include <stdio>
#include <iostream>

int main() {
}
~~~

##### Break it down

* The -v command inverts the sense of matching. Instead of printing matching lines, grep will print all lines in the file that dont match the string.
* -v can be useful for removing lots of cout statements where you may have been using debug statements that you want to remove all at once.
* This flag can also be combined with flags from above. For example, you could use -i and search HELLO and would see the same result

#### Example command

#### command flag | grep string

~~~ bash
$ ls -l | grep cpp
-rw-rw-r--  1 albert albert   89 Mar 15 17:47 helloworld.cpp
~~~

##### Break it down

* Here is a simply example of grep being used as a filter for another command.
* The part before the pipe is ls -l. This is a command to list the files in long listing format. This includes (1) permissions (2) reference count (3) owner (4) last modified (5) file name. For more info on ls click [here](https://c4cs.github.io/commands/basics/ls.html).
* follwing the pipe, we have grep and our string. In this command we pipe the output of our previous command into grep and filter it with a specific string. This can be useful when searching for a specific file or maybe a process running on a server.

