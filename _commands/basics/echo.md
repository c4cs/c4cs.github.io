---
---

echo
--

`echo` is used to output whatever it is given into stdout. Often useful see the value of environment variables. 

~~~ bash
$ echo "Hello World!"
Hello World!
$ echo $USER
<your username>
~~~

<!--more-->

### Useful Options / Examples

#### `echo -e [string...]`

~~~ bash
$ echo "Hello \tWorld\n"
Hello \tWorld\n 
$ echo -e "Hello \tWorld\n"
Hello   World 

$ 
~~~


##### Break it down
 * The `-e` flag will have echo evaluate the escaped characters inside the string.
   `\n` will be printed as a newline instead of as the literal characters.
 * This flag is also needed to use color in the output. Otherwise the
   values will be printed instead of interpreted.

#### `echo [string...with color]`

<pre>
$ echo "\033[31mHello \033[36mWorld\033[m"  
\033[31mHello \033[36mWorld\033[m
$ echo -e "\033[31mHello \033[36mWorld\033[m"  
<span style="color:red;">Hello</span><span style="color:blue;"> World</span>
$ echo "$(tput setaf 1)Hello $(tput setaf 4)World$(tput sgr0)"
<span style="color:red;">Hello</span><span style="color:blue;"> World</span>
</pre>

##### Break it down
 
 * There are two examples of adding color to echo output. The first requires the `-e` flag
   since it works with raw escape codes. Otherwise the values will be printed instead of 
   interpreted.  The second, using `tput` is considered to be better since it is more
   portable and much more readable. Note that it does not require the `-e` flag.
 * The final value resets the color, `\033[m` and `$(tput sgr0)`, to the default so that the
   color does not run into your prompt.
 * `tput setaf` sets the foreground color, the text color. tput colors go from [1,7] by default
   but can be bumped up to [1,256]

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
$ $((1 + 1))
-bash: 2: command not found
~~~

##### Break it down
 * echo can also be used to print the output of expressions that would not put their result
   into stdout.
 * This will keep bash from trying to interpret the output as command.
 * The idea behind this is very similar to the first example of printing out a environment
   variable
 * If you're building a complicated bash command precede it with echo to make sure all the
   variables and expressions expand in the expected way.

