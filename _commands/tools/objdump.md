---
---

objdump
-------
<!-- one line explanation would go here -->
`objdump` gives you information about an object file or executable.

<!-- minimal example -->
~~~ bash
$ gcc -std=c99 -c hello.c
$ objdump -r hello.o > hello_relocation.info
~~~

<!--more-->

`objdump` can be really useful when you want to understand more about the internals of executable and linkable format (ELF) files or disassemble an executable (output its corresponding assembly code).

### Useful Options / Examples

For the following examples, we'll be using the C file `add.c` compiled with the C99 standard and shown below.

~~~ C
int i = 5;

int main() {
    static int j = 2;
    int k = i + j;
}
~~~

~~~ bash
$ gcc -std=c99 -c add.c
$ gcc -std=c99 add.c -o add
$ ls | grep add
add
add.c
add.o
~~~

The `-std=c99` flag tells `gcc` to compile with the C99 standard, and the `-c` flag tells it to make an object file.

### `objdump -d`

`objdump -d` disassembles the executable sections of the argument executable or object file. In other words, it shows you the assembly code equivalent of the actual machine code that your CPU runs.

~~~ bash
$ objdump -d add > disassembly
$ head -n 10 disassembly

add:     file format elf64-x86-64


Disassembly of section .init:

0000000000400390 <_init>:
  400390:   48 83 ec 08             sub    $0x8,%rsp
  400394:   48 8b 05 5d 0c 20 00    mov    0x200c5d(%rip),%rax        # 600ff8 <_DYNAMIC+0x1d0>
  40039b:   48 85 c0                test   %rax,%rax
~~~

The output is extensive, so we only show the first 10 lines here. The first line tells you the file format of the input file and the assembly language used. In this case, the file format is ELF-64, and the assembly language is x86-64.

Next, you'll see the actually assembly code. Each section of assembly code begins with a line that tells you which section of your file that the following code is of. In the limited output above, we're looking at a part of the `.init` section.
