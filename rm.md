---
---

rm
--

`rm` is used to delete one or multiple files from your current directory. Be careful when using because this does not move the item to trash, it permanetly deletes it. 

~~~ bash
$ rm file1.txt file2.txt
~~~

<!--more-->

### Useful Options / Examples

#### `rm -d`

~~~ bash
$ rm -d directory1
$ rm -d directory2
rm: directory2: Directory not empty
~~~


##### Break it down
 * The `-d` flag will remove directorys that are empty. In the example above, directory1 was empty and thus deleted while directory2 was not. 

#### `rm -R`

~~~ bash
$ rm -R directory2
~~~


##### Break it down
 * Similar to the `-d` flag, the `-R` flag attempts to remove the file hierarchy rooted in each file argument. This allows for directories with files inside to be deleted. 
 * If the `-i` option is specified, the user is prompted for confirmation before the attempt is made to remove the directory. If the user does not respond affirmatively, the file hierarchy rooted in that directory is skipped. 

#### `rm -v`

~~~ bash
$ rm -v file.txt
file.txt
~~~


##### Break it down
 
 * the `-v` command puts the rm command into verbose mode. This will print the name of the files that will be deleted.

#### `rm -f`

~~~ bash
$ rm -f file.txt
~~~

##### Break it down

 * the `-f` flag allows the user who is using the rm command to remove the write-protected file without prompting the user.

