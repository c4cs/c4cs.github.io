---
---

expand
--

`expand` a command that convert tabs to spaces.

~~~ bash
$ expand [OPTION] [FILE]
~~~

<!--more-->

### Description
 * Convert tabs in each `FILE` to spaces, writing to standard output. With no `FILE`, or when `FILE` is `-`, read standard input.

### Flags
 * `-i, --initial`, do not convert tabs after non blanks.
 * `-t, --tabs=NUMBER`, have tabs NUMBER characters apart, not 8.
 * `-t, --tabs=LIST`, use comma separated list of explicit tab positions.
 * `--help`, display this help and exit
 * `--version`, output version information and exit


### Examples(Description)

~~~ bash
$ cat example.c
#include <stdio.h>
int main() {
		// everything with two taps inside the function
                printf(This is an example of how to use cat to see line numbers in a file);
                printf(How useful is that??);
                return 0;
}
$ expand -t 2 example.c
#include <stdio.h>
int main() {
    // convert taps into 2 spaces
    printf(This is an example of how to use cat to see line numbers in a file);
    printf(How useful is that??);
    return 0;
}
~~~


#### Possible Issue
~~~ bash
$ expand file.txt > file.txt
~~~
 * This would fail as the file.txt truncated before `expand` can read the file.txt

#### Solution to the Issue
~~~ bash
$ echo "$(expand file.txt)" > file.txt
~~~
 * This will guarantee `expand` reads the file.txt before it write to file.txt

