---
---

comm
--

`comm` is used to check for the common lines between two sorted files line by line. This command will produce three columns of output, each showing the lines unique to file1, the unique to file2 and the common lines between file1 and file2. This is useful for checking the common content between two files. 

~~~ bash
$ printf "apple\ntomato\n"> MyFruits.txt
$ printf "carrot\ntomato\n"> MyVegetables.txt
$ comm MyFruits.txt MyVegetables.txt
apple
	carrot
		tomato

~~~

<!--more-->

### Useful Options / Examples

The output of comm can be redirected into a CSV file for more convenient view and manipulate using a spreadsheet.

~~~ bash
$ comm MyFruits.txt MyVegetables.txt > common.csv
~~~


#### `comm -1`

Suppress column 1. That is to not showing the lines unique to file1 in the output. Similarly, there are comm -2(suppressing column 2, lines unique to file2), comm -3 (suppressing column 3, lines that appear in both files).

~~~ bash
$ printf "apple\ntomato\n"> MyFruits.txt
$ printf "carrot\ntomato\n"> MyVegetables.txt
$ comm -12 MyFruits.txt MyVegetables.txt
tomato
~~~


#### `comm --check-order`

This command reports if one of the input files is not in sorted

~~~ bash
$ printf "apple\ntomato\n"> MyFruits.txt
$ printf "tomato\ncarrot\n"> MyVegetables.txt
$ comm --check-order MyFruits.txt MyVegetables.txt
apple
		tomato
comm: file 2 is not in sorted order
~~~

#### comm combined usage with sort & uniq

The input file can be sorted and pipelined so that the comm command can work properly.

~~~ bash
$ printf "apple\ntomato\norange\napple\n"> MyFruits.txt
$ printf "tomato\ncarrot\nbroccoli\n"> MyVegetables.txt
$ comm <(sort MyFruits.txt|uniq) <(sort MyVegetables.txt|uniq)
apple
	broccoli
	carrot
orange
		tomato
~~~

#### 'comm -i'

The option i ignores case sensitivity.

~~~ bash
$ printf "Apple\nBanana\n"> BigFruits.txt
$ printf "apple\nbanana\n"> SmallFruits.txt
$ comm BigFruits.txt SmallFruits.txt
	apple
Apple
	banana
Banana
$ comm -i BigFruits.txt SmallFruits.txt
		apple
		banana
~~~

