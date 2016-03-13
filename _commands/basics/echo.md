---
---

echo
--

`echo` is used to output whatever it is given into stdio. Often useful see the value of enviromental variables.

~~~ bash
$ echo "Hello World!"
Hello World!
$ echo $USER
<your username>
~~~

<!--more-->

### Useful Options / Examples

#### `echo -e [string...]`

<pre>
$ echo "Hello \tWorld!\n"
Hello \tWorld\n 
$ echo -e "Hello \tWorld!\n"
Hello   World 

$ echo -e "\033[31mHello \033[36mWorld\033[m"  
<span style="color:red;">Hello</span><span style="color:cyan;"> World</span>
$ echo "\033[31mHello \033[36mWorld\033[m"
\033[31mHello \033[36mWorld\033[m
</pre>

##### Break it down
 * The `-e` flag will have echo evaluate the expression inside the string and used
   escaped characters. \n will be printed as a newline instead of as the literal
   characters.
 * This flag is also needed to use color in the output. Otherwise the
   values will be printed instead of interpreted.
 * The final value resets the color, "\033[m", to the default so that the
   color does not run into your prompt.


#### `echo -n [string...]`

~~~ bash
$ echo -n "Test "; echo "Should be on the same line"
Test Should be on the same line
~~~

##### Break it down

 * echo default prints a newline at the end of the input string.
 * The `-n` flag will have echo not print the new line character at the end. 


#### `echo $(expression)` 

~~~ bash
$ echo $((1 + 1))
2
~~~

##### Break it down

 * echo can also be used to print the output of expressions that would not put their result
   into stdio

