---
---

comm
---
`comm` is a tool that compares two sorted files and write the common lines and unique lines to standard output.

~~~ bash
$ comm [OPTION]... FILE1 FILE2
~~~

<!--more-->

# General guidelines:

* `comm` command only works for two files that are already sorted.
* options can be specified for more specific functionalities.


## Basic syntax: 

~~~ bash
$ comm [OPTION]... FILE1 FILE2
~~~

This will output three columns of results: first column is the lines unique to FILE1, second column is lines unique to FILE2 and third column is lines common to both files. This is when option is not specified.

### Common Examples

Name1 and Name2 are files with different names in them. <br />
First file **Name1** has the name *{Alex, Andrew, Boris, Amanda, Samantha}* <br />
Second file **Name2** has the name *{Patrick, Billon, Neil, Amanda, Samantha}* <br />
Run `comm` command on these two files

~~~ bash
$ comm [OPTION]... Name1 Name2
~~~

First row will display *{Alex, Andrew, Boris}* <br />
Second row will display *{Patrick, Billon, Neil}* <br />
Third row will display *{Amanda, Samantha}* <br />

Some common options for `comm` command: 

```
1. -1                        :suppress first column.
2. -2                        :suppress second column.
3. -3                        :suppress third column.
4. – -check-order            :check if input is correctly sorted.
5. – -nocheck-order          :check for correctly sorted input is skipped.
6. – -output-delimiter=STR   :separate columns with string STR
7. – -help                   :show help message.
8. – -version                :display version information.
```
>Note: 1,2,3 can be used together to suppress multiple columns.

~~~ bash
$ comm [-12]... Name1 Name2
~~~


