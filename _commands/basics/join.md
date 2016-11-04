---
---

join
--

`join` is used to combine two files based on matching content in each file.

~~~ bash
$ cat a.txt
1 h
2 t
3 e
4 a
$ cat b.txt
1 i
2 o
3 h
4 h
$ join a.txt b.txt
1 h i
2 t o
3 e h
4 a h
~~~

<!--more-->

### Useful Options / Examples

#### `join -1 FIELD -2 FIELD`

~~~ bash
$ join -1 1 -2 1 a.txt b.txt
1 h i
2 t o
3 e h
4 a h
~~~

##### Break it down

 * The `-1` and `-2` option tells `join` to combine the file based on a specific column in the two files. In this case, join is combining the two files based on column 1 in a.txt (based on `-1` flag) and column 1 in b.txt (based on `-2` flag). 

#### `join -t`

~~~ bash
$ cat scores.txt
Bob,A,00
John,B,01
Carl,C,02
$ cat id.txt
00,bob12
01,john234
02,carl44
$join -t, -1 3 -2 1 scores.txt id.txt
00,Bob,A,bob12
01,John,B,john234
02,Carl,C,carl44
~~~

##### Break it down

 * The `-t` option tells `join` what field delimiter to use. The default field delimiter is space.

#### `join -o`
~~~ bash
$ cat scores.txt
Bob,A,00
John,B,01
Carl,C,02
$ cat id.txt
00,bob12
01,john234
02,carl44
$ join -t, -o 1.1,2.1 -1 3 -2 1 scores.txt id.txt
Bob,00
John,01
Carl,02
~~~


##### Break it down

 * The `-o` option tells join to only return the columns specified. In this case, we only return the matching fields of column 1 from the first file (scores.txt) and column 2 from the second file (id.txt).

Note: `join` can be combined with <a href="sort">`sort`</a> if the files you want to join are out of order.
