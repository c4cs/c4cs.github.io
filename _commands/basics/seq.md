---
---

seq
-------

'seq' prints out a sequence of numbers to standard out. If no flags are given the seq starts at 1 and increments by 1 until the given number input is reached.
=======
`seq` is used to produce a sequence of numbers
<!-- one line explanation would go here -->


~~~ bash

$ seq 5
1
2
3
4
5
=======
$ seq 3
1
2
3

~~~

<!--more-->

### Useful Options / Examples


### Base Options
When no flags are given there are three options for 'seq'

LAST = the number which will be printed last
FIRST = the number which will be printed first, default 1
INCREMENT = the number by which the printed values are incremented, default 1
seq LAST
seq FIRST LAST
seq FIRST INCREMENT LAST


#### 'seq -f' 

Prints out values in a given sequence and formats. The formats available are '%g' for integers, '%f' for decimal, and '%e' for scientific

~~~ bash
$ seq -f "02/%02g/2018" 5
02/01/2018
02/02/2018
02/03/2018
02/04/2018
02/05/2018
~~~

##### Break it down

"seq -f "02/%02g/2018" 5" prints outs the first five days of february, printing the dates with a new line after each. The '02' determines the the leading zeros. Without it the dates would not have the leading zeros.

#### 'seq -s'

prints outs values seperated by a given seperator, the default is newline.

~~~ bash
$ seq -s " cows\n" 2 1 4
2 cows
3 cows
4 cows
~~~

#### 'seq -w'

Changes the leading zeros to match the LAST value

~~~ bash
$ seq -w 100
001
002
003
...
098
099
100
~~~

### Break it down

"seq -w 100" prints out the values from 0 to 100 but the leading zeroes are matched to the LAST value which in this case is 100. Since 100 using up tothe hundreds places, each previous value will all have zeros to the the hundreds place.

=======
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

