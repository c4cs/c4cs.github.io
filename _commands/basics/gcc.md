---
---

gcc
---
`gcc` is a GNU compiler for C.

~~~ bash
$ gcc hello.c
$ ./a.out
$ gcc hello.c -o hello
$ ./hello
~~~

<!--more-->

### Useful Options / Examples

### `gcc <filename>`
Compiles c files. The executable file generated is called ``a.out``.

~~~bash
$ gcc hello.c
$ ./a.out
$ Hello World!
~~~ 

### `gcc <filename> -o <exec_name>`
Compiles c files and creates an executable with the specified name, i.e the argument passed after `-o`.

~~~bash
$ gcc hello.c -o helloWorld
$ ./helloWorld
$ Hello World!
~~~

### `gcc -Wall`
`-Wall` enables all commonly used compiler flags. It is reccomended to always use this flag. 
This will make sure you have a 'clean' compile.
If we have the following file `sum.c` - (Note that the variable _c_ is unused)

```c
#include <stdio.h>

int main(void) {
	int c = 1;
	print f("1 + 1 is %d\n", 2);
	return 0;
}
```

Running without `-Wall` gives us no error.

~~~bash
$ gcc sum.c -o sum
$ ./sum
$ 1 + 1 is 2
~~~

However, using the flag we get a __warning__ - 

~~~bash
$ gcc -Wall sum.c -o sum
sum.c: In function ‘main’:
sum.c:4:6: warning: unused variable ‘c’ [-Wunused-variable]
  int c = 1;
      ^

~~~


### `gcc -Werror`
`-Werror` converts all warings to errors.

~~~bash
$ gcc -Wall -Werror sum.c -o sum
sum.c: In function ‘main’:
sum.c:4:6: error: unused variable ‘c’ [-Werror=unused-variable]
  int c = 1;
      ^
cc1: all warnings being treated as errors
~~~

### `gcc -O`
The `-O` flag is used to specify different optimization options.
`O0` is default. `O1 O2 O3` respectively optimize for execution time and space, 3 being the fastest.
`Os` optimizes for space.


### `gcc -d`
The `-d` flag produces debugging information.