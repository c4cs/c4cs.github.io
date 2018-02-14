---
---

tail
-------
`tail` is used to read the final few lines of text from a document. The default length is 10. 
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ tail example.txt
$ tail example1.txt example2.txt
~~~

<!--more-->

### Useful Options / Examples

#### `tail -n`

~~~ bash
$ tail -n 15 example.txt
~~~

##### Break it down
 * The `n` flag specifies the number of lines that tail will print.

#### `tail example1.txt example2.txt`

~~~bash
$ tail file1.txt file2.txt
~~~

##### Break it down
 * If you include two files in the tail command, tail will print the end of both files. 

#### `tail -c`

~~~bash
$ tail -c 500 example.txt
~~~

##### Break it down
 * The `c` flag allows you to only print the last k amount of bytes.

#### `tail -f`

~~~ bash
$ tail -f example.txt
~~~

##### Break it down
 * The `f` flag follows the file and outputs any new text added to the end of the file. For example, try opening two terminals and on one run `cat >myflie.txt` and on the other run `tail -f myfile.txt`. As you add more content to the terminal with cat open, the other terminal with tail -f will continue to print the new lines added. 
