---
---

sort
--
"Sort" is a standard command that sorts and outputs the input it was given.  
Blank space is the default field separator, see below how to change.

<!-- minimal example -->
~~~ bash
$ sort names
  Aaron
  Brian
~~~

<!--more-->

### Useful Options / Examples

The `-t` flag, followed by `$'\t'` will let you use tab separated values

~~~ bash 
$ sort -k2,2 -t $'\t' phonebook 
  Doe, John	 555-1234
  Fogarty, Suzie 555-2314
  Doe, Jane	 555-3214
  Avery, Cory	 555-4132
  Smith, Brett	 555-4321
~~~

The `-n` flag lets you sort numerical input.

~~~ bash
$ sort -n numbers
  1
  5
  9
  10
  17
~~~

The `-k` flag lets you choose the column by which your input gets sorted.

~~~bash
$ sort -k 2n ages
  Derrick 25
  Fabio   23
  Aaron   20
  Brian   19
~~~

In the previous command, `n` specifies sort will sort numbers, and `-k 2` 
specifies that the second column will be used for sorting.


The `-k x,y` option lets you sort on a column that might be composed of more 
than one field. 

~~~bash
$ sort -k2,2 -k1,1 n pay
  Aaron   1000
  Brian   1000
  Fabio   2000
  Derrick 3000
~~~
In the above case, the list is sorted by pay, and ties are broken by name.

The `-r` option lets you reverse the results of the sort.

For more useful flags, type 
`$ man sort`

