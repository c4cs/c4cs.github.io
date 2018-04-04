---
---

sort
--
`sort` is a standard command that sorts and outputs the input it was given.  

<!-- minimal example -->
~~~ bash
$ sort names
  Aaron
  Brian
~~~

<!--more-->

### Useful Options / Examples

By default, a blank space is the default field separator. This can be changed with the `-t` flag, and following it with a `$'\t'` will let you use tab separated values

~~~ bash 
$ sort -k2,2 -t $'\t' phonebook 
  Doe, John	 555-1234
  Fogarty, Suzie 555-2314
  Doe, Jane	 555-3214
  Avery, Cory	 555-4132
  Smith, Brett	 555-4321
~~~

The `-n` flag sorts numerical input.

~~~ bash
$ sort -n numbers
  1
  5
  9
  10
  17
~~~

The `-k` flag specifies the column by which your input gets sorted. `n` specifies `sort` will sort numbers, and `-k 2` 
specifies that the second column will be used for sorting.

~~~ bash
$ sort -k 2n ages
  Derrick 25
  Fabio   23
  Aaron   20
  Brian   19
~~~

The `-k x,y` option lets you sort on a column that might be composed of more 
than one field. In this example, the list is sorted by pay, and ties are broken by name.

~~~ bash
$ sort -k2,2 -k1,1 n pay
  Aaron   1000
  Brian   1000
  Fabio   2000
  Derrick 3000
~~~

The `-r` option reverses the results of the sort.

For more useful flags, type `$ man sort`
