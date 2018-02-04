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

##### Break it down
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

##### Break it down
 * The `FIRST` argument is where the sequence will start. 
 * The `INCREMENT` argument determines how the sequence increments by.
 * The `LAST` argument is where the sequence will end.

#### Bash Script

~~~ bash
> for i in $(seq 3)
> do
>   echo "i is now $i"
> done
i is now 1
i is now 2
i is now 3
~~~

##### Break it down
 * In a for loop `seq` can be used to increment the incrementer value.