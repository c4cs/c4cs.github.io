---
---

GDB
-------

An overview on the GNU debugger GDB.  

~~~ bash
*short* example of command usage and output
~~~

<!--more-->


## Starting GDB

Starting GDB is simple! When you are compiling your C++ or C code, change your optimization
flag to -g.

`g++ -Wall -Werror -g -std=c++11 testprogram.cpp -o testprogram.exe`

Then, after compiling the program, run the program.

`gdb testprogram.exe`

If gdb shows the error 'No symbol table is loaded' then, -g could be missing.


## Beginning to run your program

Just start your program by pressing start. Then, gdb will set a breakpoint at the beginning
of int main().  

`start`

Then, to continue, you can use 'next', which will step to the next line of the program 
without jumping into function calls or you can use 'step', which will allow you to step
to the next line, and if there is a function call, step into that function.


## But what if I cannot see my code?

TUI Mode to the rescue!  Try 'cntrl + x + a' and you will be amazed.
If the visuals ever get messed up try 'cntrl + l'


## Breakpoints

`break linenum` will allow you to set a breakpoint on a particular line
`info breakpoints` will allow you to list all of the breakpoints
`delete linenum` will allow you to delete the breakpoint on a particular line

If you want to save your breakpoints for next time, before you exit try this.
`save breakpoints myfile.txt`
Then, next time, after starting gdb, try this.
'source myfile.txt'

## Inspecting the synbol table

In GDB, you have many ways to inspect values.

To inspect local variables, try this.
'info locals'
To inspect arguments to a function, try this.
'info args'
To inspect the information about a stack frame, try this.
'info frame'
To print the value of a variable, try this. Hint: You can also print dereferenced variables.
'print variablename'


## Pulling apart segfaults

If you program segfaults in GDB, it will talk about a core dump.  You can inspect
this core dump with this command.
'backtrace'


## Learning more!  
https://sourceware.org/gdb/onlinedocs/gdb/index.html#SEC_Contents

