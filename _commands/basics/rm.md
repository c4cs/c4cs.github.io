---
---

rm
--

`rm` is used to delete one or multiple files from your current directory. 

~~~ bash
$ rm file1.txt file2.txt

~~~

<!--more-->

### Useful Options / Examples

#### `rm -d`

~~~ bash
$ rm -d directory1

~~~


##### Break it down
 * The `-d` flag will remove directorys even if they are not empty. 
 * This flag is needed in order to delete any directory, without the `-d` flag, rm will only be able to delete files.

#### `rm -v`

~~~ bash
$ rm -v file.txt
file.txt

~~~


##### Break it down
 
 * the '-v' command puts the rm command into verbose mode. This will print the name of the files that will be deleted.

#### `echo -f`

~~~ bash
$ rm -f file.txt

~~~

##### Break it down

 * the '-f' flag allows the user who is using the rm command to remove the write-protected file without prompting the user.



