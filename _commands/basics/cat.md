---
---

cat
-------

`cat` is a command that _concatenates_ files and prints the concatenated files to the standard output.

~~~ bash
$ echo "This is an:" > beginning.txt
$ echo "example" > end.txt
$ cat beginning.txt end.txt
This is an:
example
~~~

<!--more-->

### Useful Options / Examples

#### Example command
`cat`'s output can be redirected into a file for easy use. It can also be useful for printing out an entire file to the screen.

~~~ bash
$ echo "This is an:" > beginning.txt
$ echo "example" > end.txt
$ cat beginning.txt end.txt
This is an:
example
$ cat beginning.txt end.txt > complete.txt #Output gets fed into complete.txt
$ cat complete.txt #This prints the whole file to standard output
This is an:
example
~~~

#### Example command

The `cat` command can be useful when trying to read a small piece of code. The `-n`, `--number` flag is useful for this because it numbers the output lines.

~~~bash
$ echo "#include <stdio.h>
int main() {
	printf("This is an example of how to use cat to see line numbers in a file");
	printf("How useful is that??");
	return 0;
}" > example.c
$ cat -n example.c
     1	#include <stdio.h>
     2	int main() {
     3	        printf(This is an example of how to use cat to see line numbers in a file);
     4	        printf(How useful is that??);
     5	        return 0;
     6	}
~~~

#### Example command

The `cat` command can take no arguments. If it is run with no arguments, it simply copies standard input into standard output. This is useful for making quick files.

~~~bash
$ cat > main.c
#include <stdio.h>
int main() {
	printf("See how easy this is?");
	return 0;
}
//Ctrl+D stops standard input

$ cat main.c
#include <stdio.h>
int main() {
	printf("See how easy this is?");
	return 0;
}
~~~

#### Example command

The `cat` command can can also use heredocs to take in input. You can then use redirection to direct this input into an output file, as shown below.

~~~bash
$ cat << HEREDOCEND > outfile.txt
EECS 398 is a 1 credit minicourse. This 1-credit seminar is designed to teach the essentials of 
using a computer effectively for EECS students. While the target audience is CS/CE/DS students, 
any student wishing to learn how to use their computer much more effectively is encouraged to join. 
Topics covered include shells, environment, scripting, Makefiles, compilers, debugging tools, and 
version control. The last month of the course will be open to student input for remaining useful topics to cover.
HEREDOCEND

$ cat outfile.txt
EECS 398 is a 1 credit minicourse. This 1-credit seminar is designed to teach the essentials of 
using a computer effectively for EECS students. While the target audience is CS/CE/DS students, 
any student wishing to learn how to use their computer much more effectively is encouraged to join. 
Topics covered include shells, environment, scripting, Makefiles, compilers, debugging tools, and 
version control. The last month of the course will be open to student input for remaining useful topics to cover.

~~~
