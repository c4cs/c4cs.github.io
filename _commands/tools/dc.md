---
---
dc
----
<!-- one line explanation would go here -->
dc is a desk calculator that supports unlimited-precision arithmetic and postfix notation.

<!-- minimal example -->
~~~ bash
dc
2
3
+
p
5
*short* example of command usage and output
~~~

<!--more-->

### Note
Because it is postfix notation, the operations come AFTER the numbers

### Example
You can add  complexity to it using multiple operators
~~~ bash
dc
100
0.5
6.34
+
*
-
p
-684.00
~~~

### Useful Options

#### Printing Commands

##### 'p'
Prints the value on the top of the stack

##### 'n'
Prints the value on the top of the stack and pops it off

##### 'P'
Pops off the value on top of the stack

##### 'f'
Prints the content of the stack without changing anything

#### Stack Control

##### 'c'
Clears the stack

##### 'd'
Duplicates the top value of the stack and pushes another copy of it

##### 'r'
Reverse the order of the top two values of the stack
