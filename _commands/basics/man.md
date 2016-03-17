---
---

man
--

`man` allows users to format/display the user "manual" that is built into Linux. This manual holds a catalogue of commands and other aspects of the Linux OS.

~~~ bash
$ man [command]
$ man ls
$ man strcmp
~~~

<!--more-->

### Useful Examples

#### `man png`
~~~ bash
$ man png
PNG(5)                   File Formats Manual                  PNG(5)

NAME
       png - Portable Network Graphics (PNG) format
...
~~~

##### Break it down

 * Typically, you can enter the name of a user command after `man,` but it is also possible to use man to learn about file extensions, such as `png`.
 * Not only are user commands and file extentions built in to the manual, but also system calls, library functions, special files, games, math library functions, a tcl function, and other miscellaneous categories.

#### `man 3 printf`
~~~ bash
$ man 3 printf
printf(3)                   BSD Library Functions Manual                  printf(3)

NAME
    printf, fprintf, sprintf, snprintf, asprintf, dprintf, vprintf,
    vfprintf, vsprintf, vsnprintf, vasprintf, vdprintf -- formatted
    output conversion
...
~~~

##### Break it down

 * Most commands/functions are unique, but there are cases where a command/function has multiple versions.
 * `3` refers to the third section's `printf` function. There is another version in section 1. If the `3` was not specified (`man printf`), `man` would automatically open up the lowest numbered section, causing some confusion.

#### `man -a printf`
~~~ bash
$ man -a printf
~~~

##### Break it down

 * Similar to the last example, `printf` is a function with many versions. Sometimes, a user may not know that there are multiple versions to a command/function.
 * `-a` forces `man` to display all manual pages for `printf`, not just the first one in the lowest numbered section.

#### `man -k .`
~~~ bash
$ man -k .
ldap.conf (5)        - LDAP configuration file/environment variables
adduser.conf (5)     - configuration file for adduser(8) and addgroup(8) .
anacrontab (5)       - configuration file for anacron
subdomain.conf (5)   - configuration file for fine-tuning the behavior of the...
deluser.conf (5)     - configuration file for deluser(8) and delgroup(8) .
hosts.equiv (5)      - list of hosts and users that are granted "trusted" r c...
mailcap.order (5)    - the mailcap ordering specifications
modules (5)          - kernel modules to load at boot time
interfaces (5)       - network interface configuration for ifup and ifdown
updatedb.conf (5)    - a configuration file for updatedb(8)
slabinfo (5)         - kernel slab allocator statistics
...
~~~

##### Break it down

 * This command lets you see a list of all man pages
 * `-k` is the `apropos` command, which lets you search the manual page names and descriptions
 * The `.` is a regex that means "any character"
 * Additonally, since man pages are divided into sections, typing `man -k . -s 2` will list all man pages within section 2. 

#### `man [command] | col -x -b | groff -man -Tps > command.ps`
~~~ bash
$ man [command] | col -x -b | groff -man -Tps > command.ps
$
~~~

##### Break it down

 * In some cases, it is helpful to print out a man page so you have a
 hard copy handy. This command will format the man page and output it
 as a `.ps` file, which is print-ready
 * `man [command]` is your typical `man` command, which will get piped
 into other useful user commands that perform text formatting
  * `col -x -b` filters reverse line feeds from the piped `man` input.
  `-b` prints only the last character written to each column position
  (no backspaces). `-x` outputs multiple spaces instead of tabs.
  * `groff -man -Tps` will perform front-end formatting for documents.
  `man` ensures the traditional man page format. `-T` sets the output
  device to a specified format; in this case, we have specified the
  output to `ps`. However, other supported files include ascii, cp1047,
  dvi, html, latin1, lbp, lj4, utf8, X75, and X100.
  * `command.ps` is the file name that the formatted text will be
  outputed to. Make sure the format is the same as what is specified 
  in `groff`.
