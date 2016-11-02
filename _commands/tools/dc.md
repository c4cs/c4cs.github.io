---
---
dc
----

`dc` stands for 'desk calculator'. Typing this command into a terminal will open a [postfix notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) calculator.

~~~ bash
$ dc
2
15
*
p
30
~~~

<!--more-->


### Common arithmetic operations
-  `+` is the **addition** operator. It pops off the two most recent values and pushes their sum to the stack.
-  `-` is the **subtraction** operator. It pops off the two most recent values and pushes their difference to the stack. The first item off the stack (item entered most recently) is subtracted from the second item.
-  `*` is the **multiplication** operator. It pops off the two most recent values and pushes their product to the stack.
-  `/` is the **division** operator. It pops off the two most recent values and pushes their quotient to the stack. The first item popped off the stack is the divisor, and the second is the dividend.
-  `%` is the **modulus** operator. It pops off the two most recent values and pushes the remainder of their division to the stack. The first item popped off the stack is the divisor, and the second is the dividend.
-  `^` is the **exponentiation** operator. It pops off the two most recent values and raises the second item to the power of the first. 
-  `v` is the **square root** operator. It pops off the top stack value, computes its square root, and pushes it back onto the stack. Unless you manually change the precision value (using the `k` command) from the default zero value, it will return the nearest integer value of the square root.


##### Example using square root operator
~~~~ bash
$ dc        #launches the calculator
39          #pushes 39 to the stack
v           #push the square root of 39 to the stack
p           #print the top stack value
6           #the nearest integer of the sqrt(39)
3           #I want to see three decimal places of precision
k           #sets the precision to be the top stack value 
39          #pushes 39 to stack again
v           #recompute square root (should have more precision now)
p           #prints the new value
6.244       #And...it works.
~~~~

### Dealing with the stack (and other tricks)

- `p` will **print** the top value of the stack
- `n` will also **print** the top value of the stack, but with no newline afterwards
- `f` will print the entirety of the stack
- `c` will **clear the stack** of all its values. 
- `d` will **duplicate the top value** of the stack.
- `r` will **reverse** the top two values on the stack
- `k` will take the top value of the stack and use it to **set the precision value** (see the above example for more)
- `q` will **quit** the calculator

##### Combining commands trick

 You can combine commands by typing them on the same line. For example
 
 ~~~~ bash
 $ dc       
 5 8-p      #pushes 5 to the stack, then 8 (note the whitespace character!), 
            #then '-', then prints the result
 -3
 ~~~~

##### Example using stack commands
~~~~ bash
$ dc        #launches the calculator
250         #pushes 250 to the stack
1000        #pushes 1000 to the stack  
r           #But wait! You just realized you want to compute 1000-250, not 250-1000. 
            #Using the 'r' command will reverse these two and give you the positive value 

-           #subtract the top value on the stack from the second value
p           #print the top of the stack
750         
10          #push 10 to the stack
20          #push 20 to the stack
30          #push 30 to the stack
f           #display contents of stack from most recent to least recent
30          #contents of the stack
20          #          |
10          #          |
750         #          v
c           #clears the stack
f           #now when you print the stack, you get nothing
            #empty stack, cursor will be blinking on this line
q           #quit the calculator and return to the terminal
~~~~
