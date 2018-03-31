---
---

stat
-------
Displays information about the file pointed to by [filename]
~~~ bash
$ stat stat.md
16777217 14633638 -rw-r--r-- 1 [user] staff 0 439 "Feb  9 22:08:11 2018"
"Feb  9 22:08:08 2018" "Feb  9 22:08:08 2018" "Feb  9 21:29:18 2018"
4096 8 0x40 stat.md
~~~

<!--more-->

### Useful Options / Examples
The output is structured as below:
~~~ bash
st_mode st_ino st_dev st_rdev st_nlink st_uid st_gid st_size st_atim st_mtim st_ctim st_blksize st_blocks
~~~
`st_dev` – identifier of device containing file

`st_ino` – inode number

`st_mode` – protection mode; see also Unix permissions

`st_nlink` – reference count of hard links

`st_uid` – user identifier of owner

`st_gid` – group identifier of owner

`st_rdev` – device identifier (if special file)

`st_size` – total file size, in bytes

`st_atime` – time of last access

`st_mtime` – time of last modification

`st_ctime` – time of last status change

`st_blksize` – preferred block size for file system I/O, which can depend upon both the system and the type of file system[3]

`st_blocks` – number of blocks allocated in multiples of DEV_BSIZE (usually 512 bytes).
#### Example commands
`-r` - Display raw information, That is for all the fields displayed above, display the raw, numerical value
~~~ bash
$ stat -r stat.md
16777217 14636916 0100644 1 501 20 0 1800 1518234259 1518234256
1518234256 1518229758 4096 8 64 stat.md
~~~
<!--##### Break it down-->
`-s` - Display information in `'shell output'`,  suitable for initializing variables
~~~ bash
$ stat -s stat.md
st_dev=16777217 st_ino=14637054 st_mode=0100644 st_nlink=1 st_uid=501
st_gid=20 st_rdev=0 st_size=1905 st_atime=1518234359 st_mtime=1518234357 st_ctime=1518234357 st_birthtime=1518229758 st_blksize=4096 st_blocks=8
st_flags=64
~~~
`-x` - Display information in a more easier to read format
~~~ bash
$ stat -x stat.md
File: "stat.md"
Size: 2044         FileType: Regular File
Mode: (0644/-rw-r--r--)         Uid: (  501/  [user])  Gid: (   20/   staff)
Device: 1,1   Inode: 14637091    Links: 1
Access: Fri Feb  9 22:46:25 2018
Modify: Fri Feb  9 22:46:23 2018
Change: Fri Feb  9 22:46:23 2018
~~~

