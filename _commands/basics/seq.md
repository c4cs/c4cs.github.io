---
---

seq
-------
'seq' prints out a sequence of numbers to standard out. If no flags are given the seq starts at 1 and increments by 1 until the given number input is reached.

~~~ bash
$ seq 5
1
2
3
4
5
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

