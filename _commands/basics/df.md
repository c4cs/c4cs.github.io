---
---

df
--

df (abbreviation for disk free) is used to display the amount of availbale disk space for file systems on which the invoking user has appropriate read access.  

~~~ bash
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            982M     0  982M   0% /dev
tmpfs           201M   22M  179M  11% /run
/dev/sda1        48G  4.9G   41G  11% /
...(Some more info)
~~~

<!--more-->

### Useful Options / Examples

#### `df [directory_name]`

~~~ bash
$ df Desktop/
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       49702628 5077556  42077208  11% /
~~~

#### `--total`
~~~ bash
display a grand total.
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
