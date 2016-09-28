---
---

grep
-------

`grep` is used to search files for the occurrence os string of characters matching a string (egrep can support called regular expressions often abbreviated as regex).

~~~ bash
$ grep string file
matches because it has string in it
~~~

<!--more-->

### Useful Options / Examples

#### Example command

#### `grep -i -o string file`
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

* The `-i` flag allows searches for case insensitive matches inside the the given file. As can be seen between the first and second examples above the only difference was the flag. From the first example we see a line with a substring that matches a case insensitive search. However, on the second example we dont see any output because it is a case sensitive search.
* The `-o` flag allows us to print just the matching substring from a file. For example, comparing the first and third example, we the first contains the entire line from a file while the third example only prints the word hello.
* Both flags can be used separately or together. As can be seen in examples three and four, these flags can be used to get the exact output, for example a case insensitive search (example three) or 
a case sensitive search for a word (example four).

#### Example command

#### `grep -v string file`
~~~ bash
$ grep -v hello helloworld.cpp
#include <stdio>
#include <iostream>

int main() {
}
~~~

##### Break it down

* The `-v` flag inverts the sense of matching. Instead of printing matching lines, grep will print all lines in the file that dont match the string.
* `-v` can be useful for removing lots of cout statements where you may have been using debug statements that you want to remove all at once.
* This flag can also be combined with flags from above. For example, you could use `-i` and search HELLO and would see the same result

#### Example command

#### `command flag | grep string`

~~~ bash
$ ls -l | grep cpp
-rw-rw-r--  1 albert albert   89 Mar 15 17:47 helloworld.cpp
~~~

##### Break it down

* Here is a simply example of grep being used as a filter for another command.
* The part before the pipe is `ls -l`. This is a command to list the files in long listing format. This includes (1) permissions (2) reference count (3) owner (4) last modified (5) file name. For more info on ls click [here](/commands/ls.html).
* follwing the pipe, we have grep and our string. In this command we pipe the output of our previous command into grep and filter it with a specific string. This can be useful when searching for a specific file or maybe a process running on a server.

#### Example command

#### `grep -E string file`

~~~ bash
$ ps aux | grep -E ^a
ahyerman  1510  0.0  0.0 259076  3280 ?        SN   09:32   0:00 sshd: ahyerman@pts/4
ahyerman  1511  0.0  0.0 129028  3448 pts/4    SNs  09:32   0:00 -bash
ahyerman  1740  0.0  0.0 149792  1716 pts/4    RN+  09:35   0:00 ps aux
ahyerman  1741  0.0  0.0 112644   976 pts/4    SN+  09:35   0:00 grep --color=auto ^a
~~~

##### Break it down

* The above command if again used as a filter.
* This time we are using a command to see the current processes currently running on our machine. This output is then piped to grep.
* The grep command has a `-E` flag. The `-E` stands for extended grep and works like egrep. This allows us to use a regular expression rather than just a string for searching. The regex used in the above command has the `^` symbol. This means find any line that starts with what follows. In this example, all processes run by ahyerman were shown.
* The `-E` flag can be useful when what your are searching for isnt always well formed or exactly the same every time it appears.

#### Example command

#### `grep -r string`

~~~ bash
$ grep -r "~~~ bash"
scripting/yes.md:~~~ bash
template.md:~~~ bash
basics/grep.md:~~~ bash
basics/grep.md:~~~ bash
...
basics/whoami.md:~~~ bash
basics/ls.md:~~~ bash
...
~~~

##### Break it down

* The above command preforms a recursive search on all files in a the current directory and its sub-directories. The `-r` specifies to recursively search directories.
* Above, we searched for any lines that have the bash format for an md file. We used grep to recursively search all files in our current directory and any sub directory.
* This is useful because as projects grow, as do their files. One might want to find all lines using a certain variable across many files and directories. The `-r` flag is a great way to perform the search.


