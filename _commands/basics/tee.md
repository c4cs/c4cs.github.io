---
---

tee
-------

'tee' is used to split standard input to be both saved in a file or variable and sent to the standard output. It is named after and behaves much like a T-splitter real-life pipe used in plumbing.

~~~ bash
$ tee [option(s)] [destination file(s)]
~~~

<!--more-->

### Useful Options / Examples

#### program-call | tee output
~~~ bash
$ program | tee output.txt
~~~

##### Break it down
 * 'tee' is commonly used with a program call, by piping the output of the program into the 'tee' command. This allows a user to easily write the output of their program call into a file, while also getting a chance to see this output displayed.
 * The above commands would write the output of calling "program" into the file "output.txt" and would simultaneously write this output to the standard output.
 * If the user specifies a dash ('-') instead of a filename, the output will simply be written to the standard output twice.

#### command | tee 1 2 3
~~~ bash
$ command | tee output1.txt output2.txt output3.txt
~~~

##### Break it down
 * Output can be 'tee'-d into multiple files, in addition to still being displayed in the standard output.
 * The above commands would write the output of calling "command" into the files "output1.txt", "output2.txt", and "output3.txt", as well as writing to the standard output.

#### command | tee -a -i output
~~~ bash
$ command | tee -a -i output.txt
~~~

##### Break it down
 * The -a flag specifies that output should appended to the end of the indicated file(s), instead of overwriting them.
 * The -i flag specifies that the command should ignore interrupt signals
