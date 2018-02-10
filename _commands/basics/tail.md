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
 * The `n` flag specifies the number of line that tail will print.

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
 * The `f` flag follows the file and outputs any new text added to the end of the file
