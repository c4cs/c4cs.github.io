---
---

cd
--

`cd` is used to _change directory_. Unlike most commands, `cd` is not
a separate program, it is a shell built-in. `cd` is a useful tool to navigate up and down the hierarchy of the file systems on your machine, and move into a given directory.

~~~ bash
$ cd ~
$ cd /home
~~~

<!--more-->

### Useful Options / Examples


#### `cd -`

Jump to the last directory that you were in. This will not always necessarily be the parent to your current directory, which would instead be the case if you were to use `cd ..`

(Note that this command prints current path after completion)

~~~ bash
Alborz-Brals-MacBook-Pro:basics abral$ pwd
/Users/abral/Desktop/Computer_Science/EECS 398 (C4CS)/adv_HW_7_2/c4cs.github.io/_commands/basics
Alborz-Brals-MacBook-Pro:basics abral$ cd /tmp
Alborz-Brals-MacBook-Pro:tmp abral$ pwd
/tmp
Alborz-Brals-MacBook-Pro:tmp abral$ cd -
/Users/abral/Desktop/Computer_Science/EECS 398 (C4CS)/adv_HW_7_2/c4cs.github.io/_commands/basics
~~~


#### `cd ..`

Another way to jump back directory

The two dot characters `..` represent the parent directory to the current directory in which we are working

~~~ bash
Alborz-Brals-MacBook-Pro:basics abral$ pwd
/Users/abral/Desktop/Computer_Science/EECS 398 (C4CS)/adv_HW_7/c4cs.github.io/_commands/basics
Alborz-Brals-MacBook-Pro:basics abral$ cd ..
Alborz-Brals-MacBook-Pro:_commands abral$ pwd
/Users/abral/Desktop/Computer_Science/EECS 398 (C4CS)/adv_HW_7/c4cs.github.io/_commands
~~~

#### `cd .`

The one dot character `.` represents the current directory in which we are working. This command simply moves us to our current directory

~~~ bash
Alborz-Brals-MacBook-Pro:basics abral$ pwd
/Users/abral/Desktop/Computer_Science/EECS 398 (C4CS)/adv_HW_7/c4cs.github.io/_commands/basics
Alborz-Brals-MacBook-Pro:basics abral$ cd .
Alborz-Brals-MacBook-Pro:basics abral$ pwd
/Users/abral/Desktop/Computer_Science/EECS 398 (C4CS)/adv_HW_7/c4cs.github.io/_commands/basics
~~~

Of course, this accomplishes nothing; however, there are other uses for the `.` character pertaining to the `cd` command. Some of the more common uses can be found on the [dot(.) page of the C4CS website](https://c4cs.github.io/commands/dot)

#### `cd`

Jump back to home directory (same as "cd ~" or "cd /home")

~~~ bash
Alborz-Brals-MacBook-Pro:basics abral$ pwd
/Users/abral/Desktop/Computer_Science/EECS 398 (C4CS)/adv_HW_7/c4cs.github.io/_commands/basics
Alborz-Brals-MacBook-Pro:basics abral$ cd
Alborz-Brals-MacBook-Pro:~ abral$ pwd
/Users/abral
~~~


#### `cd /`

Jump to the root directory 

~~~ bash
Alborz-Brals-MacBook-Pro:basics abral$ pwd
/Users/abral/Desktop/Computer_Science/EECS 398 (C4CS)/adv_HW_7/c4cs.github.io/_commands/basics
Alborz-Brals-MacBook-Pro:basics abral$ cd /
Alborz-Brals-MacBook-Pro:/ abral$ pwd
/
~~~