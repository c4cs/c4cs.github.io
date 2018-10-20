---
---

find
---
`find` is a command line utility for finding files, directories and performing subsequent operations on them.

~~~ bash
$ find [where to start searching from]
 [expression determines what to find] [-options]
 [what to find]
~~~

<!--more-->

### Useful Options / Examples

###`find /`
Finds and prints every file on the system
```bash
$ find /
```

###`find <directory> -name <filename>`

Searches for **\<filename\>** in **\<directory\>**. In this mode, the command is case sensitive.

``` bash
$ find ./Documents -name demo.txt

#return
./demo.txt
```

###`find <directory> -iname <filename>`

Searches for **\<filename\>** in **\<directory\>**, ignoring letter case.

``` bash
$ find ./Documents -name demo.txt

#return:
./demo.txt
./Demo.txt
```


###`find <directory> -owner <username>`

Searches in **\<directory\>** for files owned by **\<username\>**.

``` bash
$ find  /data -owner userA
```



###`find <directory> -empty`

Finds all empty files and folders in **\<directory\>**

~~~ bash
$ find ./Documents -empty
~~~


###`find <directory> -perm <permission>`

Finds all files in **\<directory\>** or sub-directory with the given permissions. For example, we want to find all the world-readable files in your Documents directory so as to avoid oversharing.

~~~ bash
$ find ~/Documents -perm -o=r
~~~


###Other Options
* **exec CMD**: The file being searched which meets the above criteria and returns 0 if successfully executed.
* **-ok CMD**: The user is prompted first before searching.
* **-inum N**: Search for files with inode number ‘N’.
* **-links N**: Search for files with ‘N’ links.
* **-name demo**: Search for files that are specified by ‘demo’.
* **-newer file**: Search for files that were modified/created after ‘file’.
* **-perm octal**: Search for the file if permission is ‘octal’.
* **-print**: Display the path name of the files found by using the rest of the criteria.
* **-empty**: Search for empty files and directories.
* **-size +N/-N**: Search for files of ‘N’ blocks; ‘N’ followed by ‘c’can be used to measure size in characters; ‘+N’ means size > ‘N’ blocks and ‘-N’ means size < 'N' blocks.
* **-user name**: Search for files owned by user name or ID ‘name’.
* **! expr**: True if ‘expr’ is false.
