---
---

wc
-------

Print the number of bytes, words, and lines in files

~~~ bash
$ cat a.txt 
I love EECS 398.
What a great class. 
Good.

$ wc [filename] 
$ wc a.txt
3 9 44 a.txt
~~~

<!--more-->

### Useful Options / Examples

~~~ bash
$ cat a.txt
What
a great
world we live
in where Google has all the answers we need

$ cat b.txt
wc is a great command.
I love it.
~~~


#### `wc -c a.txt`
~~~ bash
$ wc -c a.txt
71 a.txt
~~~

##### Break it down
 * When the `-c`(equivalent to `--bytes`) flag is set, wc will output the number of bytes in the given file.


#### `wc -m a.txt`
~~~ bash
$ wc -m a.txt
71 a.txt
~~~

##### Break it down
 * When the `-m`(equivalent to `--chars`) flag is set, wc will output the number of characters in the given file. 

#### `wc -l a.txt`
~~~ bash
$ wc -l a.txt
4 a.txt
~~~

##### Break it down
 * When the `-l`(equivalent to `--lines`) flag is set, wc will output the number of lines in the given file.

#### `wc -L a.txt`
~~~ bash
$ wc -L a.txt
43 a.txt
~~~

##### Break it down
 * When the `-L`(equivalent to `--max-line-length`) flag is set, wc will output the length of the longest line in the given file.

#### `wc -w a.txt b.txt`
~~~ bash
$ wc -w a.txt b.txt
15 a.txt
 8 b.txt
23 total
~~~

##### Break it down
 * When the `-w`(equivalent to `--words`) flag is set, wc will output the number of words in the given file.
 * Note that it is possible to give more than one file as input and wc will give you the results for each file individually as well as a cumulative output.
