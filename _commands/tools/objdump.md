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

Next, you'll see the disassembled code. Each section of disassembly begins with a line that tells you which section of your file that the following code is of. In the limited output above, we're looking at a part of the `.init` section.

Each section of disassembly consists of several columns. 

The first column tells you the address that the code will be located at runtime. 

The second tells you the machine code in hex of the corresponding instruction. 

The next two columns have the assembly language equivalent of the machine code.


### `objdump -t`

`objdump -t` displays the symbol table of your argument file.

~~~ bash
$ objdump -t add.o

add.o:     file format elf64-x86-64

SYMBOL TABLE:
0000000000000000 l    df *ABS*  0000000000000000 add.c
0000000000000000 l    d  .text  0000000000000000 .text
0000000000000000 l    d  .data  0000000000000000 .data
0000000000000000 l    d  .bss   0000000000000000 .bss
0000000000000004 l     O .data  0000000000000004 j.1703
0000000000000000 l    d  .note.GNU-stack    0000000000000000 .note.GNU-stack
0000000000000000 l    d  .eh_frame  0000000000000000 .eh_frame
0000000000000000 l    d  .comment   0000000000000000 .comment
0000000000000000 g     O .data  0000000000000004 i
0000000000000000 g     F .text  000000000000001c main
~~~

The symbol table has five columns. 

The first displays the corresponding symbol's address.

The second tells you the flags that are enabled for the symbol. In the output above, some of the flags are separated by whitespace, making them seem like different columns, but that's because some flags are disabled. Some examples of flags are: `l` for local, `g` for global, `d` for debugging, `f` for file, `F` for function, and `O` for object. There are a number of other flags, but we won't cover all of them here.

The third column tells you where the symbol lives. For example, `.data` means the data segment, `text` means the text segment, and `*ABS*` means absolute (the symbol doesn't live anywhere in particular).

The fourth shows you the symbol's size or alignment.

The fifth tells you the symbol's name.


### `objdump -r`

`objdump -r` displays the relocation table of your argument file. This command is most useful with object files.

~~~ bash
$ objdump -r add.o

add.o:     file format elf64-x86-64

RELOCATION RECORDS FOR [.text]:
OFFSET           TYPE              VALUE 
0000000000000006 R_X86_64_PC32     i-0x0000000000000004
000000000000000c R_X86_64_PC32     .data


RELOCATION RECORDS FOR [.eh_frame]:
OFFSET           TYPE              VALUE 
0000000000000020 R_X86_64_PC32     .text
~~~

The relocation table has three columns.

The first column tells you the offset where the relocated symbol address should go.

The second tells you the type of the symbol.

The third tells you the symbol and the offset that should be added to it after resolving the symbol's new location.

The `-r` flag can be used with the `-d` flag to get the relocation information interspersed in the disassembly.

~~~ bash
$ objdump -dr add.o

add.o:     file format elf64-x86-64


Disassembly of section .text:

0000000000000000 <main>:
   0:   55                      push   %rbp
   1:   48 89 e5                mov    %rsp,%rbp
   4:   8b 15 00 00 00 00       mov    0x0(%rip),%edx        # a <main+0xa>
                        6: R_X86_64_PC32    i-0x4
   a:   8b 05 00 00 00 00       mov    0x0(%rip),%eax        # 10 <main+0x10>
                        c: R_X86_64_PC32    .data
   10:  01 d0                   add    %edx,%eax
   12:  89 45 fc                mov    %eax,-0x4(%rbp)
   15:  b8 00 00 00 00          mov    $0x0,%eax
   1a:  5d                      pop    %rbp
   1b:  c3                      retq 
~~~


### Other flags

There are a number of other flags that you can use with `objdump` to get more information about an object file. Because there are so many, we only covered the most useful ones here. You can read about the rest [here](https://linux.die.net/man/1/objdump).
