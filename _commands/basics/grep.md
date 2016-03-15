---
---

grep
-------

`grep` is used to search files for the occurence os string of characters matching a special pattern (sometimes called a regex or regular expression).

~~~ bash
$ grep regex file
line in file matching regex
~~~

<!--more-->

### Useful Options / Examples

#### Example command

####  grep -i -o regex file
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

####  grep -v regex file
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

