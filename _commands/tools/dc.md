---
---

dc
-------

Short for "Desk Calculator", dc is an arbitrary-precision arithmetic package.
It supports arbitrary, unlimited-precision arithmetic and uses reverse-polish (postfix) notation.

~~~ bash
$ dc    # Starts the calculator
$ 2     # put 2 on the stack
$ 2 * p # multiply by 2 and print
$ 4     # output
$ 1 - p # subtract 1 and print
$ 3     # output
$ 2 / p # divide by 2 and print
$ 1     # output
~~~

<!--more-->

### Usage
This is the output from the help options.

~~~ bash
Usage: dc [OPTION] [file ...]
  -e, --expression=EXPR    evaluate expression
  -f, --file=FILE          evaluate contents of file
  -h, --help               display this help and exit
  -V, --version            output version information and exit

Email bug reports to:  bug-dc@gnu.org .
~~~


### Options

#### `-V, --version`

Print out the version information of dc and a Copyright notice, then exit.

~~~ bash
$ dc -V
$ dc --version
~~~

#### `-h, --help`

Print a usage message briefly summarizing these command-line options and the bug-reporting address, then exit.

~~~ bash
$ dc -h
$ dc --help
~~~

#### `-e script, --expression=script`

Add the commands in script to the set of commands to be run while processing the input.

~~~ bash
$ dc -e <script>
$ dc --expression=<script>
~~~

#### `-f script-file, --file=script-file`

Add the commands contained in the file script-file to the set of commands to be run while processing the input.

~~~ bash
$ dc -f <script-file>
$ dc --file=<script-file>
~~~

### Useful commands

#### Set precision `k`

Sets the decimal precision. Most arithmetic operations are affected by the "precision value". The default precision value is zero, which means that all arithmetic except for addition and subtraction produces integer results.

~~~ bash
$ k
$ 3 k
~~~

If you use only k with nothing preceding it it will use the top value on the stack.

#### Clear stack `c`

Clears the contents of the stack

~~~ bash
$ c
~~~

#### Comment `#`

Will interpret rest of the line as a comment.

~~~ bash
$ 2 + #This will be ignored
~~~


### Printing commands

#### `p`

Prints the value on top of the stack. Does not alter the stack. Prints a newline.

~~~ bash
$ p
~~~

#### `n`

Prints the value on top of the stack. Pops the top value off of the stack. Does not print a newline.

~~~ bash
$ n
~~~

#### `f`

Prints the entire stack without changing it. This is useful for figuring out what a command did.

~~~ bash
$ f
~~~

### Arithmetic operations

### Addition `+`

Pops two values off the stack and adds them together and then pushes back on to the stack.

~~~ bash
$ +
~~~
Takes the top two values and adds them and pushes the result

~~~ bash
$ 2 +
~~~
Pushes 2 on to the stack and then pops off top two values and adds them.

### Subtraction `-`

Pops two values off the stack and subtracts the first one popped from the second one popped and then pushes the result back on to the stack.

~~~ bash
$ +
~~~
Takes the top two values and subtracts the first popped from second popped and pushes the result

~~~ bash
$ 2 +
~~~
Pushes 2 on to the stack and then pops the top two values subtracting the first popped from second popped and pushes the result.

### Multiplication `*`

Pops two values, multiplies them, and pushes the result. The number of fraction digits in the result depends on the current precision value and the number of fraction digits in the two arguments.

~~~ bash
$ *
$ 2 *
~~~


### Division `*`

Pops two values, divides second popped by the first, and pushes the result. The number of fraction digits in the result depends on the precision value.

~~~ bash
$ /
$ 2 /
~~~

### Modulo `%`

Pops two values, pushes the remainder of dividing the second popped by the first popped.

~~~ bash
$ %
$ 2 %
~~~


### Exponent `^`

Pops two values, pushes the result of raising the second popped to the power of the first popped.

~~~ bash
$ ^
$ 2 ^
~~~


### Square root `v`

Pops one value and computes the square root of the value and pushes it on to the stack. The precision value specifies the number of digits in the result.

~~~ bash
$ ^
$ 2 ^
~~~

## Similar commands
This command is similar to `bc`
