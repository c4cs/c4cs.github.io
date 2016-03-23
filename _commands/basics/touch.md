---
---

touch
-------

	
'touch' command is used to create new, empty files; it can create several files simultaneously. 

~~~ bash
~/temp$ ls
~/temp$ touch file1 file2
~/temp$ ls
file1  file2
~/temp$ cat file1
~/temp$ 
~~~

'touch' will only change the last access time for the existing files with the same name instead of automatically overwriting them.

<!--more-->

### Useful Options / Examples

#### 'touch -a' and 'touch -m'

~~~ bash
~/temp$ stat file1
  File: ‘file1’
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 801h/2049d	Inode: 159692      Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/ bisheng)   Gid: ( 1000/ bisheng)
Access: 2016-03-23 15:39:43.382476140 -0400
Modify: 2016-03-23 15:39:43.382476140 -0400
Change: 2016-03-23 15:39:43.382476140 -0400
 Birth: -
~/temp$ touch -a file1
~/temp$ stat file1
  File: ‘file1’
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 801h/2049d	Inode: 159692      Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/ bisheng)   Gid: ( 1000/ bisheng)
Access: 2016-03-23 15:39:54.214474489 -0400
Modify: 2016-03-23 15:39:43.382476140 -0400
Change: 2016-03-23 15:39:54.214474489 -0400
 Birth: -
~/temp$ touch -m file1
~/temp$ stat file1
  File: ‘file1’
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 801h/2049d	Inode: 159692      Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/ bisheng)   Gid: ( 1000/ bisheng)
Access: 2016-03-23 15:39:54.214474489 -0400
Modify: 2016-03-23 15:43:41.599195528 -0400
Change: 2016-03-23 15:43:41.599195528 -0400
 Birth: -
~~~

##### Break it down

'touch -a' can change the last access time of the file while 'touch -m' can change the last modify time of the file. 
'stat file' can see the specific timestamp of a file.

#### 'touch -r'

~~~ bash
~/temp$ touch -r file2 file1
~/temp$ stat file2
  File: ‘file2’
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 801h/2049d	Inode: 159671      Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/ bisheng)   Gid: ( 1000/ bisheng)
Access: 2016-03-23 15:28:29.551766821 -0400
Modify: 2016-03-23 15:28:29.551766821 -0400
Change: 2016-03-23 15:28:29.551766821 -0400
 Birth: -
~/temp$ stat file1
  File: ‘file1’
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 801h/2049d	Inode: 159692      Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/ bisheng)   Gid: ( 1000/ bisheng)
Access: 2016-03-23 15:28:29.551766821 -0400
Modify: 2016-03-23 15:28:29.551766821 -0400
Change: 2016-03-23 15:49:34.114178163 -0400
 Birth: -
~~~

##### Break it down
'touch -r file2 file1' can make file1 use the timestamp of file2's. 

#### 'touch -d' and 'touch -t'

~~~ bash
~/temp$ touch -d '1 April 2016 12:12' file1 
~/temp$ stat file1
  File: ‘file1’
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 801h/2049d	Inode: 159692      Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/ bisheng)   Gid: ( 1000/ bisheng)
Access: 2016-04-01 12:12:00.000000000 -0400
Modify: 2016-04-01 12:12:00.000000000 -0400
Change: 2016-03-23 15:53:47.992762028 -0400
 Birth: -
~/temp$ touch -t 201701010000.00 file2
~/temp$ stat file2
  File: ‘file2’
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 801h/2049d	Inode: 159671      Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/ bisheng)   Gid: ( 1000/ bisheng)
Access: 2017-01-01 00:00:00.000000000 -0500
Modify: 2017-01-01 00:00:00.000000000 -0500
Change: 2016-03-23 15:55:35.018293510 -0400
 Birth: -

~~~

##### Break it down
'touch -d' and 'touch -t' can change the timestamp of a time to some specific time. 'touch -d' is followed by a string in the format of 'date, month, year, minute:second'; 'touch -t' is followed by [[CC]YY]MMDDhhmm[.ss].



