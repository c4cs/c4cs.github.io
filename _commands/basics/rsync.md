---
---

rsync
--

`rsync` is file copying tool. It can be used locally or to and from a host. It is most commonly used to copy only the changes made to a file. 

~~~ bash
$ rsync dir1/file dir2/
~~~

<!--more-->

### Useful Options / Examples

#### `rsync -r source dest`

recursively transer files. Helpful for sending directories. This functions as `cp -r` or `scp -r` would, except with the benefit of only copying the differences between the source and destination files.

#### `rsync -t source dest`

preserve modification times

~~~bash
$ ls -l test_dir1
total 168
-rw-r--r-- 1 user user 171035 Mar 24 17:55 rsync_docs.txt

$ ls -l test_dir2
total 12
-rw-r--r-- 1 user user 10862 Mar 24 17:56 rsync_docs.txt

$ rsync -t test_dir1/rsync_docs.txt  test_dir2/rsync_docs.txt 

$ ls -l test_dir1/
total 168
-rw-r--r-- 1 user user 171035 Mar 24 17:55 rsync_docs.txt

$ ls -l test_dir2/
total 168
-rw-r--r-- 1 user user 171035 Mar 24 17:55 rsync_docs.txt
~~~

#### Breakdown

We can see that the modification time for the rsync_docs.txt in test_dir2/ was synced to be the same as the modification time of the rsync_docs.txt in test_dir1/


#### `rsync -v source dest`

print extra information about the transer like bytes transfered and speedup.
See *Comparing with scp* below for an example

#### `rsync -W source dest`

Transfer whole file (not just the changes made). Functionally this will be the same as just using scp.

### Comparing with scp

~~~bash
$ ls
rsync_docs.txt

$ rsync -v <uniquename>@login.engin.umich.edu:~/test_file/rsync_docs.txt rsync_docs.txt
sent 1,500 bytes  received 1,059 bytes  86.75 bytes/sec
total size is 171,035  speedup is 66.84

$ scp <uniquename>@login.engin.umich.edu:~/test_file/rsync_docs.txt . 
100%  167KB 167.0KB/s   00:00    
~~~

#### Breaking it down

For this example, There is a file on CAEN that contains the rsync documentation. There is also an identical file in the current directory. Running rsync with -v will print out some interesting data on bytes transfered, transfer speed, and speedup. scp serves as our benchmark for rsync. It serves the same purpose that cp does locally, but across a network. It will transfer the entire file everytime it is called.


We can see that rsync sent 1,500 bytes and recieved 1,059 bytes. Compared to scp's received 167,000 bytes there is a clear improvement.  The speedup time listed in the rsync reflects this as well. 


Rsync is comapring the file contained locally with the one on CAEN to see if there are any differences. In our example we have two identical files so the data transfered is predictably very small.

