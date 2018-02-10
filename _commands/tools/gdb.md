

# Yo figuring out da GDB bro

# Exploring GDB

GDB is the GNU Project debugger. It allows you to go figure out the behavior of your
program by inspecting variable values, control flow of your program, seeing snapshots
of your program, etc.

## Starting GDB

Starting GDB is simple! When you are compiling your C++ or C code, change your optimization
flag to -g.

'g++ -Wall -Werror -g -std=c++11 testprogram.cpp -o testprogram.exe'

Then, after compiling the program, run the program.

'gdb testprogram.exe'

If gdb shows the error 'No symbol table is loaded' then, -g could be missing.


## Beginning to run your program

Just start your program by pressing start. Then, gdb will set a breakpoint at the beginning
of int main().  

How does GDB work?

