---
---
df
-------


Example of command usage and output
~~~ bash
$df

Filesystem               1K-blocks     Used  Available Use% Mounted on
/dev/mapper/vg1-lv_root  255494800 12306556  230186724   6% /
devtmpfs                   8149492        0    8149492   0% /dev
tmpfs                      8175728   103820    8071908   2% /dev/shm
tmpfs                      8175728     8876    8166852   1% /run
tmpfs                      8175728        0    8175728   0% /sys/fs/cgroup
tmpfs                       307200     6052     301148   2% /var/lib/sss/db
/dev/sda4                   495844   158214     312030  34% /boot
/dev/sda1                   507904    36652     471252   8% /boot/efi
/dev/mapper/vg1-lv_tmp    30832548    45440   29197860   1% /tmp
AFS                     2147483647        0 2147483647   0% /afsSIZE Format
~~~


`df` displays the amount of disk space available on the file system containing each file name argument. If no file name is given, the space available on all currently mounted file systems is shown. Disk space is shown in 1 K blocks by default, unless the environment variable POSIXLY_CORRECT is set, in which case 512-byte blocks are used.


Display values are in units of the first available SIZE from --block-size, and the DF_BLOCK_SIZE, BLOCK_SIZE and BLOCKSIZE environment variables. Otherwise, units default to 1024 bytes (or 512 if POSIXLY_CORRECT is set).

SIZE is an integer and optional unit (example: 10M is 10*1024*1024). Units are K, M, G, T, P, E, Z, Y (powers of 1024) or KB, MB, ... (powers of 1000).
tmpfs                      1635148       32    1635116   1% /run/user/99515263

<!--more-->



If an argument is the absolute file name of a disk device node containing a mounted file system, df shows the space available on that file system rather than on the file system containing the device node (which is always the root file system). df cannot show the space available on unmounted file systems, because on most kinds of systems doing so requires very system-specific knowledge of file system structures.


### Useful Options / Example

~~~ bash
$ df -h
~~~

Display all file systems and their disk usage but uses human readable formatting.

~~~ bash
bash-4.2$ df -h
Filesystem               Size  Used Avail Use% Mounted on
/dev/mapper/vg1-lv_root  244G   12G  220G   6% /
devtmpfs                 7.8G     0  7.8G   0% /dev
tmpfs                    7.8G  102M  7.7G   2% /dev/shm
tmpfs                    7.8G  8.7M  7.8G   1% /run
tmpfs                    7.8G     0  7.8G   0% /sys/fs/cgroup
tmpfs                    300M  6.0M  295M   2% /var/lib/sss/db
/dev/sda4                485M  155M  305M  34% /boot
/dev/sda1                496M   36M  461M   8% /boot/efi
/dev/mapper/vg1-lv_tmp    30G   45M   28G   1% /tmp
AFS                      2.0T     0  2.0T   0% /afs
tmpfs                    1.6G   32K  1.6G   1% /run/user/99515263
~~~


#### Example command
~~~ bash
$df example_folder
~~~
Display the amount of free space in the public_html directory
~~~ bash
$df example_folder
Filesystem      1K-blocks  Used  Available Use% Mounted on
AFS            2147483647     0 2147483647   0% /home/divshar
~~~

#### Options


| Command | Description |
| --- | --- |
| -a, --all | Include dummy file systems. |
| -B, --block-size=SIZE | Scale sizes by SIZE before printing them. E.g., '-BM' prints sizes in units of 1,048,576 bytes. See "SIZE Format" below for more information. |
| --total | Display a grand total. |
| -h, --human-readable | Print sizes in human readable format (e.g., 1K 234M 2G). |
| -H, --si | Same as -h, but use powers of 1000 instead of 1024. |
| -i, --inodes | List inode information instead of block usage. |
| -k | Like --block-size=1K. |
| -l, --local | Limit listing to local file systems. |
| --no-sync | Do not invoke a sync before getting usage info, which is the default setting. |
| -P, --portability | Use the POSIX output format. |
| --sync | Invoke a sync before getting usage info. |
| -t, --type=TYPE | Limit listing to file systems of type TYPE. |
| -T, --print-type | Print file system type. |
| -x, --exclude-type=TYPE | Limit listing to file systems not of type TYPE. |
| -v | Ignored; included for compatibility reasons. |
| --help | Display a help message and exit. |
| --version | Output version information and exit. |




