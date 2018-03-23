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
$dc
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
~~~ bash
$dc
4
4
+
p
8
~~~

##### 'n'
Prints the value on the top of the stack and pops it off
~~~ bash
$dc
10
10
+
n
20    
p
dc: stack empty
~~~

##### 'P'
Pops off the value on top of the stack
~~~ bash
$dc
10
10
+
P
p
dc: stack empty
~~~

##### 'f'
Prints the content of the stack without changing anything
~~~ bash
$dc
10
10
+
f
20
~~~

#### Stack Control

##### 'c'
Clears the stack
~~~ bash
$dc
10
10
10
c
p
dc: stack empty
~~~

##### 'd'
Duplicates the top value of the stack and pushes another copy of it
~~~ bash
$dc
10
d
f
10
10
~~~

##### 'r'
Reverse the order of the top two values of the stack
~~~ bash
$dc
1
2
3
4
r
f
3
4
2
1
~~~

##### 'q'
Exits out
~~~ bash
$dc
10
20
+
q
~~~
