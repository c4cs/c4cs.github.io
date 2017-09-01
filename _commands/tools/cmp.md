---
---

cmp
-------

`cmp` is a tool used to compare two files byte by byte.

~~~ bash
$ echo "Hello" > file1.txt
$ echo "H3llo" > file2.txt
$ cmp file1.txt file2.txt
file1.txt file2.txt differ: char 2, line 1
~~~

<!--more-->

### Useful Options / Examples

#### `cmp file1.txt file2.txt`

Running `cmp` on two files will produce no output if the two files are the same. If the two files differ, the command will output the byte and line number where the first difference occured. Note: the line and byte numbers are counted beginning with 1, not 0.

For example:

~~~ bash
$ echo "Hello" > file1.txt
$ echo "H3llo" > file2.txt
$ cmp file1.txt file2.txt
file1.txt file2.txt differ: char 2, line 1
~~~

##### Break it down
* The first difference occurs at the second character of the first line. This is accurate since file1 has an e where file2 has a 3. 

#### `cmp -b file1.txt file2.txt`

The `-b` flag prints the first byte that is different between the two files.

For example:

~~~ bash
$ echo "Hello" > file1.txt
$ echo "H3llo" > file2.txt
$ cmp -b file1.txt file2.txt
file1.txt file2.txt differ: byte 2, line 1 is 145 e  63 3
~~~

##### Break it down
* Besides just printing the location of the first byte difference (hence "...differ: byte 2, line 1...), the differing byte location and byte value is printed. "145 e" denotes the decimal byte number and the byte value in file1 and "63 3" denotes the same from file2, respectively. 

#### `cmp -l file1.txt file2.txt`

The `-l` flag outputs the byte number that is different, following by the differing byte from the first input file then the differing byte from the second input file.  

For example:

~~~ bash
$ echo "123" > file1.txt
$ echo "Hello" > file2.txt
$ cmp -l file1.txt file2.txt
1  61 110
2  62 145
3  63 154
4  12 154
cmp: EOF on file1.txt
~~~

##### Break it down
* At byte 1, file1.txt had a byte value of 61 while file2.txt had a byte value of 110.
* Because file2.txt was longer than file1.txt, the cmp call on the last byte caused an error. This will happen anytime the two files passed in as input to cmp are of different lengths. 

#### `cmp -s file1.txt file2.txt`

The `-s` flag doesn't print anything. It just returns an exit status. This is useful for writing shell scripts where you don't need something to output but would like to use `cmp` in program decision making. 

For example, in a bash script you might see:

~~~ bash
if cmp -s "$file1" "$file2"
then
   echo "The files match"
   # execute some code
else
   echo "The files are different"
   # do something else
fi
~~~

#### `cmp` vs `diff`

cmp and diff are similar in that they both compare files. [Experiments](https://github.com/murukeshm/scratchpad/tree/master/diff-cmp) show that there aren't too large of a performance difference between them either. So when should you use which?

Use cmp or diff -q if you don't have a large desktop or terminal window to display the text. They provide just a single line of info about the difference between files. If terminal window size isn't an issue, just use diff. 