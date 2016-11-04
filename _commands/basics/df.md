---
---

df
--

df displays the amount of disk space available on the file system containing each file name argument. If no file name is given, the space available on all currently mounted file systems is shown. Disk space is shown in 1K blocks by default, unless the environment variable POSIXLY_CORRECT is set, in which case 512-byte blocks are used.  

~~~ bash
$ df
Filesystem     1K-blocks    Used Available Use% Mounted on
udev             1004740       0   1004740   0% /dev
tmpfs             204848   21672    183176  11% /run
/dev/sda1       49702628 5077532  42077232  11% /
...(Some more info)
~~~

<!--more-->

### Useful Options / Examples

#### `df -h`
~~~ bash
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            982M     0  982M   0% /dev
tmpfs           201M   22M  179M  11% /run
/dev/sda1        48G  4.9G   41G  11% /
...(Some more information)
~~~

##### Break it down

* Same as df, but use "human readable" formatting. 

#### `df [directory_name]`

~~~ bash
$ df Desktop/
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       49702628 5077556  42077208  11% /
~~~

#### `-a, --all`
~~~ bash
include dummy file systems.
~~~

#### `--total`
~~~ bash
display a grand total.
~~~

#### `-i, --inodes`
~~~ bash
list inode information instead of block usage.
~~~

#### `--help`
~~~ bash
display a help message and exit.
~~~

#### `-T, --print-type`
~~~ bash
print file system type.
~~~

#### `-t, --type=[TYPE]`
~~~ bash
limit listing to file systems of type [TYPE].
~~~
