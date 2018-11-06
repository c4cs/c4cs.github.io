---
---

printf
-------

print formatted ouput.
works like the c function of the same name.

~~~ bash
printf FORMAT ARGS

example:
printf "My name is \"%s\".\n The args can be nums %i." "Ryan" 2

output:
"My name is Ryan.
The args can be nums 2."
~~~

<!--more-->

### Useful Options / Examples

Like most commands printf also has a --help option
Some other interesting things to note:

#### variable types

%i = integer

%d = decimal

%o = octal

%x = hex

%u = unsigned int

%c = character

%s = string

%f = float

%e = scientific float (engineering)

%p = pointer

%% = percent sign

#### modifiers

You can modify the variables in different ways:
number = amount of space to occupy
\- = pad to the left
.number = max amount of characters to use

##### Examples

"%8s" "hi"

"      hi"

"%-8s" "hi"

"hi      "

"%.4s" "hello everyone"

"hell"
