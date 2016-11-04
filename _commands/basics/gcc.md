---
---

gcc flags
--

`gcc` is a compiler command that has the ability to execute options or 'Flags' when compiling.  These flags can be grouped and executed via the command line:

`-o` places output in a file.

`-g` turns on debugging information. 

`-Werror` makes all warnings into errors.

`-Wall` enables all the warnings.

`-ar` creates an archive instead of a program.

~~~ bash
$ gcc test.c -o test
$ gcc -g test.c
$ gcc -Werror test.c
$ gcc -Wall test.c
$ gcc -ar test.c
~~~







<!--more-->

### Useful Options / Examples

#### `-o`
~~~ bash
$ gcc test.c -o test
~~~

##### Break it down
~~~ bash
This is a very simple example where test.c is being compiled and outputted to the test file.  The output filename is specified after the flag.  Input: test.c, Output: test
~~~





#### `-g`
~~~ bash
$ gcc -g test.c
~~~

##### Break it down
~~~ bash
This option compiles test.c with debugging information.  It builds the binary executable file with additional debugging information that is helpful when debugging.  Additionally,all optimization should be turned off.
~~~








#### `-Werror`
~~~ bash
$ gcc -Werror test.c
~~~

##### Break it down
~~~ bash
This option makes all warnings into errors.  Test.c will not compile with this flag if there are any warnings produced.
~~~







#### `-Wall`
~~~ bash
$ gcc -Wall test.c
~~~

##### Break it down
~~~ bash
`-Wall` is short for "warn all".  This option turns on almost all warnings when compiling.
~~~








#### `-ar`
~~~ bash
$ gcc -ar test.c
~~~

##### Break it down
~~~ bash
The `-ar` option creates an archive (a static library) instead of a program. The resulting file will have an .a ending.
~~~


