---
---

nl
-------

nl numbers the lines in a file

~~~ bash
cat list1.txt

a
b
c

nl list1.txt

1 a
2 b
3 c
~~~

<!--more-->

### Useful Options / Examples

#### Example command

-v, --starting-line-number=NUMBER &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  first line number is NUMBER

~~~bash
cat list1.txt

a  
b  
c  

nl -v3 list1.txt

3 a  
4 b  
5 c  
~~~

##### Break it down

The -v3 causes the the first line to be numbered 3 and then each line after the first is numbered sequentially from 3

#### Example command

-s, --number-separator=STRING &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  add STRING after each line number


~~~bash
cat list1.txt

a  
b  
c  

nl -s:\  list1.txt

1: a  
2: b  
3: c  
~~~

##### Break it down

The :s\(space) causes each line to have a :(space) after the number

