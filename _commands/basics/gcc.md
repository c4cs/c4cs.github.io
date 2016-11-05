---
---

gcc flags
--

`gcc` is a compiler command that has the ability to execute options or 'Flags' when compiling.  These flags can be grouped and executed via the command line:

`-o` places output in a filename of your choice.  If you do not use the `-o` flag the output file will have the name and extention: 'a.out'.

`-g` turns on debugging information. 

`-Werror` makes all warnings into errors.

`-Wall` enables all the warnings.

`-O` enables optimization.

__NOTE__: See below for details.

~~~ bash
$ gcc test.c -o test
$ gcc -g test.c
$ gcc -Werror -Wall -O test.c
~~~
<!--more-->

### Useful Options / Examples

#### `-o`
~~~ bash
$ gcc test.c -o test
$ gcc test.c -o out
~~~

##### Break it down

In the first line of code, test.c is being compiled and outputted to the file specified file named test.  The filename is specified after the `-o` option.  Input: test.c, Output: test.  In the Second line, the input file is test.c and the ouput file name will be 'out.out'.



#### `-g`
~~~ bash
$ gcc -g test.c
~~~

##### Break it down

This option compiles test.c with debugging information.  It builds the binary executable file with additional debugging information that is helpful when debugging.  Additionally,all optimization should be turned off.





#### `-Werror`
~~~ bash
$ gcc -Werror test.c
~~~

##### Break it down

This option makes all warnings into errors.  Test.c will not compile with this flag if there are any warnings produced.





#### `-Wall`
~~~ bash
$ gcc -Wall test.c
~~~

##### Break it down

This option is short for "warn all".  This option turns on almost all warnings when compiling.









#### `-O`
~~~ bash
$ gcc -O test.c
$ gcc -O1 test.c
~~~

##### Break it down

In the first line of code, the `-O` option instructs the compiler to try and reduce code size and execution time, without performing any optimizations that take a great deal of compilation time.  There are additional variations to the `-O` option that use alternative methods to optimize a file.  Examples include:  `-O1`, `-O2`, `-O3` and `-Os`.


`-O1` Further Optimizes where the compilation takes somewhat more time, and a lot more memory for a large function.


`-O2` Optimizes even more. GCC performs nearly all supported optimizations that do not involve a space-speed tradeoff.


`-O3` Optimize yet more. `-O3` turns on all optimizations specified by `-O2` and also turns on the `-finline-functions`, `-funswitch-loops`, `-fpredictive-commoning`, `-fgcse-after-reload`, `-ftree-loop-vectorize`, `-ftree-loop-distribute-patterns`, `-fsplit-paths -ftree-slp-vectorize`, `-fvect-cost-model`, `-ftree-partial-pre`, `-fpeel-loops` and `-fipa-cp-clone` options.


`-Os` Optimize for size. This option enables all `-O2` optimizations that do not typically increase code size. It also performs further optimizations designed to reduce code size.





