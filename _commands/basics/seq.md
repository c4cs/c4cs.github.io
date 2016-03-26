---
---

seq
-------

`seq`prints a sequence of numbers to standard ouput.

~~~ bash
$ seq [options]... [*FIRST* [*STEP*]] *LAST*... 
~~~

<!--more-->

where `seq` prints numbers from *FIRST* to *LAST* by an increment *STEP*.
Default: *FIRST* & *STEP* are both 1. Each number is printed on its own line. Seq can be used on all real numbers.

EXAMPLE

~~~ bash
$ seq 3
1
2
3
~~~

### Useful Options / Examples

#### `-f, --format=`*FORMAT*

prints all numbers using *FORMAT*, where the default is `%g`. *FORMAT* must contain one of the following float output formats: `%g`, `%e`, `%f`, where `%g` is the default. 
NOTE: `%g` is included in the example below to show where to include a float output format in the command.

EXAMPLE:

~~~ bash
$ seq -f "tyler%02g" 10
~~~

will produce:

tyler01  
tyler02  
tyler03  
tyler04  
tyler05  
tyler06  
tyler07  
tyler08  
tyler09  
tyler10  

#### `-s, --seperator=`*STRING*

separates numbers with *STRING*, where default is a newline. Output terminates with newline.

EXAMPLE:

~~~ bash
$ seq -s' ' 0 2 10
~~~ 

will produce:

0 2 4 6 8 10

#### `-w, --equal-width=`

prints all numbers with same width by padding with leading zeros. 

EXAMPLE:

~~~ bash
$ seq -w 50 50 250
~~~ 

will produce:

050  
100  
150  
200  
250  

---
