---
---

nl
-------

`nl` is a command that _numbers_ the lines of files and prints the result to the standard output.

~~~ bash
$ echo "This is an:" > beginning.txt
$ echo "example" > end.txt
$ nl beginning.txt end.txt
   1	This is an:
   2	example
~~~

<!--more-->

### Useful Options / Examples

#### Example command
`nl` does not modify the original file on its own. However, `nl`'s output can be redirected into a file for future reference.

~~~ bash
$ echo "This is an:" > beginning.txt
$ echo "example" > end.txt
$ nl beginning.txt end.txt
   1    This is an:
   2    example
$ cat beginning.txt end.txt #Note the files were not modified
This is an:
example
$ nl beginning.txt end.txt > complete.txt #Numbered output gets fed into complete.txt
$ cat complete.txt #Sends stored numbered output in complete.txt to standard output
   1    This is an:
   2    example
~~~

#### Example command

The `cat` command offers the `-n`, `--number` flag which also numbers the lines of a file. However, the `nl` command by default ignores empty lines.

~~~bash
$ echo "#include <stdio.h>
int main() {
	printf("There are some empty spaces below this line");
	

	printf("This will be line 4 when using nl or line 6 when using cat -n");
	return 0;
}" > example.c
$ cat -n example.c
     1	#include <stdio.h>
     2	int main() {
     3	        printf("There are some empty spaces below this line");
     4
     5
     6          printf("This will be line 4 when using nl or line 6 when using cat -n");
     7	        return 0;
     8	}
$ nl example.c
     1  #include <stdio.h>
     2  int main() {
     3  printf("There are some empty spaces below this line");
     

     4  printf("This will be line 4 when using nl or line 6 when using cat -n");
     5          return 0;
     6  }
~~~

#### Useful Options

`nl -b` uses a particular STYLE for numbering body lines from the following:

`a` --- number all lines

`t` --- number only nonempty lines

`n` --- number no lines

`pBRE` --- number only lines that contain a match for the basic regular expression `BRE`

Example 1: `nl -ba` numbers all lines in a file (including empty lines)

~~~bash
$ echo "#include <stdio.h>
int main() {
        printf("There are some empty spaces below this line");


        printf("This will be line 4 when using nl or line 6 when using cat -n");
        return 0;
}" > example.c
$ nl -a  example.c
     1  #include <stdio.h>
     2  int main() {
     3          printf("There are some empty spaces below this line");
     4
     5
     6          printf("This will be line 4 when using nl or line 6 when using cat -n");
     7          return 0;
     8  }
~~~

Example 2: `nl -bpA` matches the lines beginning with ‘A’ and numbers only those lines

~~~bash
$ cat sort.txt
UK
Australia
Newzealand
Brazil
America
$ nl -bpA sort.txt
       UK
     1	Australia
       Newzealand
       Brazil
     2	America
~~~

`nl -i` alters the increment of each line (by default is 1)

~~~bash
$ cat sort.txt
UK
Australia
Newzealand
Brazil
America
$ nl -i5 sort.txt
     1  UK
     6  Australia
    11  Newzealand
    16  Brazil 
    21  America
~~~
