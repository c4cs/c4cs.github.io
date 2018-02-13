---
---

factor
--
`factor` prints all of the prime factors of a number.

<!-- minimal example -->
~~~ bash
$ factor 42
42: 2 3 7
~~~

<!--more-->

### Useful Options / Examples

#### `factor [number]`

`factor` can take in one parameter, and that is a positive integer. `factor` will parse through all of the prime factors of the number and return them to the console in an easy to read manner.

~~~ bash
$ factor 51
51: 3 17
~~~

#### `factor [number_1] [number_2] [number_3]`

`factor` can take in more than one parameter, but they must all be positive integers. It will print the prime factors of each number on a new line.

~~~ bash
$ factor 20 30 40
20: 2 2 5
30: 2 3 5
40: 2 2 2 5
~~~

#### `factor [number_1] [number_2] [number_3] > factors.txt`

As with any other command, the output of `factor` can be piped to an output file. You can use the `cat` command to print the output of the file to the terminal.

~~~ bash
$ factor 20 30 40 > factors.txt
$ cat factors.txt
20: 2 2 5
30: 2 3 5
40: 2 2 2 5
~~~