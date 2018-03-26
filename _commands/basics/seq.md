---
---

seq
-------
`seq` is used to produce a sequence of numbers
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ seq 3
1
2
3
~~~

<!--more-->

### Useful Options / Examples

#### `seq -s [SEPERATOR] `

~~~ bash
$ seq -s " " 3
1 2 3
$ seq -s " | " 3
1 | 2 | 3
~~~

 * `-s` is the seperator between the numbers. For the default the seperator is equal to '\n', the end of line character. Takes in a string value.

#### `seq -f [FORMAT] `
 
~~~ bash
$ seq -f "01/%02g/2016" 3
01/01/2016
01/02/2016
01/02/2016
~~~

* `-f` Sets a format for the sequence. In this case, a date like format was chosen.

#### `seq [FIRST] [LAST]`

~~~ bash
$ seq 5 10
5
6
7
8
9
10
~~~

 * Putting in two number arguments prints a list of numbers starting from the 
first number to the second number

#### `seq [FIRST] [INCREMENT] [LAST]`

~~~ bash
$ seq 2 2 10
2
4
6
8
10
~~~

 * The `FIRST` argument is where the sequence will start. 
 * The `INCREMENT` argument determines how the sequence increments by.
 * The `LAST` argument is where the sequence will end.

#### Bash Script

##### Input

~~~ bash
> for i in $(seq 3)
> do
>   echo "i is now $i"
> done
~~~

##### Output

~~~ bash
i is now 1
i is now 2
i is now 3
~~~

 * In a for loop `seq` can be used to increment the incrementer value.
