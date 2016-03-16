---
---

grep
-------

grep [OPTIONS] PATTERN [FILE(S)]

grep searches the specified files for the input pattern and outputs lines with matching words to standard output.

If no files are given, grep will search for the pattern in words passed to standard input.


~~~ bash
$ grep Hello hello.cpp
cout << "Hello!" << endl;
~~~

<!--more-->

### Useful Options / Examples

####
grep -i

~~~ bash
$ grep -i hello hello.cpp
cout << "Hello!" << endl;
~~~
# Break it down
The -i flag will tell grep to ignore case. In this example, grep outputted the link including "Hello" even though we specified "hello".


#### Example command
grep -v

~~~ bash
$ grep -v Hello hello.cpp
#include <iostream>

int main() {
	return 0;
}

##### Break it down
The -v flag will tell grep to output every line that does NOT include the given pattern. In our hypothetical hello.cpp file, grep outputs every line except the line containing "Hello".



grep -c

~~~ bash
$ grep -c Hello hello.cpp
1
~~~

The -c flag counts the number of lines with the pattern instead of printing out the actual lines.



grep -l

~~~ bash
$ grep -l Hello hello.cpp goodbye.cpp
hello.cpp
~~~

The -l flag will output the filenames of the files given that contain the pattern. In this example, hello.cpp has "Hello" in it but goodbye.cpp does not, so only hello.cpp is outputted.
