---
---

sort
--

`sort` is used to _sort a file or input_. 

~~~ bash
$ cat letters.txt
b
z
e
a
$ sort letters.txt
a
b
e
z
~~~

<!--more-->

### Useful Options / Examples

#### `sort -r`

~~~ bash
$ sort -r letters.txt
z
e
b
a
~~~

##### Break it down

 * The `-r` option tells `sort` to sort the input in the opposite order  
 * The `letters.txt` is the file that is used as input 

#### `sort -n`

~~~ bash
$ cat numbers.txt
3
6
3
16
23
7
2
23
1
$ sort -n numbers.txt
1
2
3
3
6
7
16
23
23
~~~

##### Break it down

 * The `-n` option tells `sort` to sort the input as numbers rather 
   than as characters

#### `sort -u`

~~~ bash
$ sort -n -u numbers.txt
1
2
3
6
7
16
23
~~~

##### Break it down

 * The `-u` option works the same way as the `uniq` command, namely
   it removes any duplicate lines while sorting

