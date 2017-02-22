---
---

hash
--

`hash` is used to maintain a hash table of full pathnames of recently executed programs.
A full search of the directories in PATH is performed only if the command is not found in the hash table.

~~~ bash
$ hash
  hits	command
   4	/bin/nano
   3	/usr/local/bin/bundle
   1	/usr/bin/pip
   3	/usr/bin/git
   2	/usr/bin/factor
   5	/usr/bin/sudo
  11	/bin/ls
   1	/usr/bin/figlet
   3	/usr/bin/python
~~~

<!--more-->

### Useful Options / Tricks

#### `hash -r`
This option clears the cached hash table.  
(Note: Changing $PATH is equivalent to running this command - the hash table is invalidated.)

~~~ bash
$ hash
  hits	command
   4	/bin/nano
   3	/usr/local/bin/bundle
   1	/usr/bin/pip
   3	/usr/bin/git
   2	/usr/bin/factor
$ hash -r
$ hash
hash: hash table empty
~~~

#### `hash -d`
This options allows deletion of a hash table entry.

~~~ bash
$ hash
  hits	command
   4	/bin/nano
   3	/usr/local/bin/bundle
   1	/usr/bin/pip
   3	/usr/bin/git
   2	/usr/bin/factor
$ hash -d pip
$ hash
  hits	command
   4	/bin/nano
   3	/usr/local/bin/bundle
   3	/usr/bin/git
   2	/usr/bin/factor
~~~

#### Find if an executable program exists using `hash`
Use `hash` to find whether an exectuable program exists or not.

~~~ bash
$ hash ls && echo executable exists || echo executable doesnt exist
executable exists
$ hash gibberish123 && echo executable exists || echo executable doesnt exist
bash: hash: gibberish123: not found
executable doesnt exist
~~~

