---
permalink: /lectures/f18/week3.html
---

class: center, middle

# Shells, Environment, Scripting, and Bash
## (in 80 minutes[!])

.copyright[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
** [Pat Pannuto](http://patpannuto.com) / Marcus Darden **
]


---


# Q: How does a program start?

???

Lots of answers to this
 - "double click" something
 - spotlight something (or magic ubuntu menu that's the same)
 - type it into a terminal

--

## The jobs of a _shell_

 - Spawn (launch) new programs
 - Handle input and output to programs
 - Kill and clean up old programs

--

### What shells have you used?

???

 - All the text ones: bash, csh, zsh, fish, (I'm sure there are more)
 - KEY POINT: The desktop is also a "shell", it does all these jobs!
              Indeed, the desktop in Gnome is called the "unity shell"




---

# Let's poke around how the [Desktop] shell works

```bash
$ cp /usr/share/applications/firefox.desktop ~/Desktop/
$ chmod +x ~/Desktop/firefox.desktop
```

--

## What makes `firefox.desktop` work?

???

 - Change "Name=..."
 - What's the point of Name[ar] and friends?
 - What might "Keywords=..." do?
 --> click ubuntu icon in top corner, try typing each keyword, what's first?
 --> can't change this as easily, doesn't read from files on ~/Desktop/
 - What about this "Exec=..."
 --> Exec=gnome-calculator

--

## How does the [desktop] shell:

 - Spawn (launch) new programs
 - Handle input and output to programs
 - Kill and clean up old programs




---

# Let's poke around how the [bash] shell works

```bash
$ firefox
<Ctrl-C>
$ firefox &
$ jobs
$ fg
<Ctrl-Z>
$ bg

$ echo "hello" > test
$ cat test

$ true && echo "hello"
$ false && echo "nope" || echo "whaaaat?"
```
--

## How does the [bash] shell:

 - Spawn (launch) new programs
 - Handle input and output to programs
 - Kill and clean up old programs




---

# Where's `firefox` anyway?

```bash
$ firefox              # This works
$ gcc hello.c -o hello # This works
$ hello                # This doesn't
$ ./hello              # This works
```

## Your _environment_ affects program behavior

  - Even shells! (they're a program too)



---

# Changing the environment will change program behavior

  - In this case, how a shell performs the search for programs
```bash
$ PATH=$PATH:/home/username/    # Assuming "hello" is in this folder
$ hello                         # Now this works!
$ PATH=/home/username           # What if you'd done this instead?
```
  - Also saw a brief example of environment variables in last week's homework


---

# Your programs can use the environment too

```c++
#include <iostream>
using namespace std;
int main(int argc, char *argv[], char *envp[]) {
  cout << "argc: " << argc << endl;
  cout << "envp[0]: " << envp[0] << endl;
  // while (*envp++) {  // Try this one, too!
  //     cout << *envp << endl;
  // }
  return 0;
}
```

```bash
$ ./a.out
$ HELLO=world ./a.out
$ lower=fine many=okaytoo ./a.out
$ export IamPermanent=ish
$ ./a.out
$ # Try uncommenting the while loop, did you find the missing ones?
$ ./a.out | less      # This may explain some of the funny colors
```

---

# Now what about _scripting_?

--

## Surprise! You've been scripting this whole time!

 - Typing commands into the bash shell and running a bash script are _the same_
```bash
$ cat test.sh
echo "hello" > test
cat test
true && echo "hello"
false && echo "nope" || echo "whaaaat?"
$ chmod +x test.sh # What is this doing?
$ ./test.sh
```

--

 - How to write a bash script?

    - Try things out in the terminal
    - Copy things that work into a file ($ history)
    - Run that file
    - Repeat



---

# Bash is old...

## But useful, especially for really short things

## But has ugly and finicky syntax

 - `VARIABLE=test` != `VARIABLE = test` :(

## But running programs is really easy

  - (it's what it was built for after all)
  - `g++ -O3 -m32 thread.o libinterrupt.a test1.cpp -ldl -o test1`
  - `./test1`

## But doing much more is tricky

  - Validate program output (`diff`?), what if it varies?
  - Rule of thumb: More than 50-100 lines, more than a shell script



---

# Closing remarks

- **Try one of the Advanced Exercises**

- We're at the end of Segment 1
- Reminder: You must submit to staff at OH
