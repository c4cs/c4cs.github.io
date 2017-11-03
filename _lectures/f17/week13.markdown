---
permalink: /lectures/f17/week13.html
---

class: center, middle

# A Sampling of Other Things

.copyright[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
** [Pat Pannuto](http://patpannuto.com) / Marcus Darden **
]


---

# Today

- Profiling

- Static Analysis

- Developer Surveys

---

# Profiling

## What is it?

## What's it good for?

## When will you use it

(other than 281?)

## What are its limitations

---

# Getting started with `perf`

- Install the tool

```bash
sudo apt install linux-tools-common linux-tools-`uname -r`
```

--

- Write a simple program

```c
int main() {
    return 0;
}
```

- And profile it

```bash
$ make main
cc     main.c   -o main
$ perf record ./main
$ ls
main  main.c  perf.data
$ perf report
```

???
```bash
mmdarden@c4cs-f17:~$ perf
The program 'perf' is currently not installed. You can install it by typing:
sudo apt install linux-tools-common
mmdarden@c4cs-f17:~$ sudo apt install linux-tools-common
```

```bash
mmdarden@c4cs-f17:~$ perf
WARNING: perf not found for kernel 4.4.0-31

You may need to install the following packages for this specific kernel:
    linux-tools-4.4.0-31-generic
    linux-cloud-tools-4.4.0-31-generic

You may also want to install one of the following packages to keep up to date:
    linux-tools-generic
    linux-cloud-tools-generic
mmdarden@c4cs-f17:~$ sudo apt install linux-tools-generic
```

```bash
mmdarden@c4cs-f17:~$ sudo apt install linux-tools-`uname -r`
mmdarden@c4cs-f17:~$ perf
 usage: perf [--version] [--help] [OPTIONS] COMMAND [ARGS]
```

---

# Getting something useful from `perf`

- Need a program that takes some time

```c
void child() {
	int i;
	for (i=0; i < 0xFFFFFFF; i++) { // 7 F's
		asm("nop;");
	}
}

int main() {
	int i;
	for (i=0; i < 0xFFFFFFF; i++) { // 7 F's
		asm("nop;");
	}
	child();
}
```

```bash
$ make main
cc     main.c   -o main
$ perf record ./main
$ perf report
```

---

# Understanding a little how `perf` works

```bash
$ perf record -F1 ./main
$ perf report
```

```bash
$ perf record -F100000 ./main
$ perf report
```

- What does `-F` do?
  - (Try `man perf-report`, you can use `/` to search in `man`)

???

Bonus: Try `perf script` (raw list of events)

---

# Can we profile library code?

- Let's write a lot of 0's

```c
#include <string.h>
...
for (i=0; i < 0xFFFFF; i++) { // 7 F's -> 5 F's
...
char buf[0xFFFF];
...
// asm("nop");
memset(buf, 0, 0xFFFF);
```

---

# Some libraries are uglier :(

- Add a `printf`

```c
#include <stdio.h>
...
for (i=0; i < 0xFFFFF; i++) { // 7 F's -> 5 F's
...
// asm("nop");
printf("%d\n", i);
```

## This can make profiling real code hard

 - Don't go down blind alleys (e.g. `perf annotate --stdio`)

---

# (5-10 min) Try it out

## Pick any prior code you've written and try profiling it

```bash
$ perf record ./your_program
$ perf report
```

### > The bigger the better

## Are the results what you expect?

---

# Closing thoughts on profiling

## When should you profile your code?

## How often should you profile your code?

--

<hr />

## Other questions, thoughts about profiling?

.footer[
`perf` is crazy powerful, [some other cool stuff it can do](http://www.brendangregg.com/perf.html)
]

---

# Static Analysis

## What is it?

## Why is it useful?

## When should you run it?

---

# Just a little history first

## Linting - the original static analysis

--

- The point: The line between style and correctness is blurry

--

## Today, the lines between compilers, linters, and static analyzers are blurring

---

# Static Analysis in action: cppcheck

```bash
sudo apt install cppcheck
```

## Check a single file:
```bash
mmdarden@c4cs-f17:~/share/281$ cppcheck my_compress.cpp
Checking my_compress.cpp...
[my_compress.cpp:445]: (error) Memory leak: dict
Checking my_compress.cpp: DEBUG...
Checking my_compress.cpp: DEBUG2...
```

## Check a whole project for everything
```bash
mmdarden@c4cs-f17:~/share/281$ cppcheck --enable=all .
...
```

---

# Static Analysis in action: scan-build

```bash
sudo apt install clang
```

### This tool dynamically re-writes make rules (!)
- Won't work if you've hardcoded `g++` (should be `$(CXX)`)

```make
bad: bad.cpp
    g++ bad.cpp

good: good.cpp
    $(CXX) $(CPPFLAGS) $(CXXFLAGS) good.cpp
```

```bash
mmdarden@c4cs-f17:~/share/281$ scan-build make
...
scan-build: 7 bugs found.
scan-build: Run 'scan-view /tmp/scan-build-2016-11-30' to examine bug reports
```

---

# (10 min) Try it out

## Try running `cppcheck` and `scan-build` on an old project

```bash
$ cppcheck --enable=all .
$ scan-build make
```

### Did they find any errors?

## Try running them on a current project

---

# Developer Surveys

## C4CS

## StackOverflow.com

---

# Next Week

## Two special topics lectures

### - Wed: TBD

### - Fri: TBD

## Come to at least one (like usual)

### - Consider coming to both if you can

### - Should be fun :)

<hr />

### `warning:` end-of-semester slightly shrinks the window to turn in Advanced Exercise 13

#### - Double check the OH on the course calendar!
