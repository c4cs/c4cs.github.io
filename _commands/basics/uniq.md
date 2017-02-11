---
---

uniq
--

`uniq` is used to _filter consecutive repeated lines from a file or input._ The first line of each consecutive group of repeated lines is retained. Repeated lines that are not consecutive are treated as unique instances and will not be filtered.

~~~ bash
$ cat numbers.txt
1
2
2
3
2
4
4
$ uniq numbers.txt
1
2
3
2
4
~~~

<!--more-->

_Notice that the 2 that follows the 3 is not filtered, even though it is repeated. This is because the second 2 is not part of a consecutive group of repeated lines._

### Useful Options / Examples

#### `uniq -u`

##### Break it down

 * This is the default action if no flag is specified
 * The `-u` option tells `uniq` to filter out only those lines that are unique, with non-consecutive repeated lines being treated as unique instances
 * Refer to the example above. No flag is specified, so the deafult `-u` option is used
 * The `-u` option is most commonly used with [sort](/commands/sort) to first sort a file and then remove consecutive duplicated lines (see example below)

~~~ bash
$ cat numbers.txt
2
2
0
2
1
1
3
4
4
$ cat numbers.txt | sort | uniq
0
1
2
3
4
~~~

#### `uniq -d`

~~~ bash
$ cat numbers.txt
2
2
0
2
1
1
3
4
4
$ uniq -d numbers.txt
2
1
4
~~~

##### Break it down

 * The `-d` option tells `uniq` to only print the first duplicate of each group of duplicate lines
 * Lines that are unique are omitted

#### `uniq -D`

~~~ bash
$ cat numbers.txt
2
2
0
2
1
1
3
4
4
$ uniq -D numbers.txt
2
2
1
1
4
4
~~~

##### Break it down

 * The `-D` option tells `uniq` to print all duplicate lines, instead of just the first duplicate of each group of duplicate lines

#### `uniq -c`

~~~ bash
$ cat numbers.txt
2
2
0
2
1
1
3
4
4
$ uniq -c numbers.txt
2 2
1 0
1 2
2 1
1 3
2 4
~~~

##### Break it down

 * The `-c` option tells `uniq` to print all unique lines, retaining the first line of consecutive repeated lines, and also generate a count of the number of consecutive repeated lines. For unique lines, the count will be 1.
 * The first column is the count, and the second column is the filtered output






