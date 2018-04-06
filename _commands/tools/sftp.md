---
---

sftp
-------
`sftp` is used to securely transfer files between a local machine and a remote machine that is accessed via SSH. SFTP stands for Secure File Transfer Protocol.
~~~ bash
$ sftp user@hostname
Password: *********
Connected to hostname.
sftp> put filename.txt
sftp> mput file1.txt file2.txt file3.txt
sftp> get file.txt
sftp> mget file1.txt file2.txt file3.txt
~~~

<!--more-->

### Useful Options / Examples

#### `sftp user@hostname`
~~~ bash
$ sftp <username>@login.engin.umich.edu
Password: **********
Connected to login.engin.umich.edu.
sftp>
~~~

This is how you begin the sftp process. It is done the same way as when you SSH into a machine, except you use the sftp command instead of the ssh command. You must have access to the machine and provide a password. You can try this by remote accessing CAEN with your uniqname@login.engin.umich.edu and providing your kerberos password as the password.

#### `sftp> ls`
~~~ bash
sftp> ls
remoteDirectory1
remoteFile1.txt
sftp> lls
localDirectory1
localFile1.txt
~~~

Use the `ls` command to print the contents of the current directory on the remote machine. Use the `lls` command to print the contents of the current directory on your local machine.


 #### `sftp> cd directory`
~~~ bash
sftp> cd remoteDirectory1
sftp> lcd localDirectory1
~~~

Use the `cd` command to change your current directory on the remote machine. Use the `lcd` command to change your current directory on your local machine.

 #### `sftp> put filename`
~~~ bash
sftp> put localFile1.txt
~~~

Upload a single file from your local machine to the remote machine.

 #### `sftp> mput filename1 filename2 filename2`
~~~ bash
sftp> mput localFile1.txt localFile2.txt localFile3.txt
~~~

Upload several files from your loacl machine to the remote machine.

 #### `sftp> put -r directory/`
~~~ bash
sftp> mkdir localDirectory1
sftp> put -r localDirectory/
~~~

To upload a directory from your local machine to the remote machine, first make a new destination directory on the remote machine, and then upload the directory from your local machine using `put`.

 #### `sftp> get filename`
~~~ bash
sftp> get remoteFile1.txt
~~~

Download a single file from the remote machine to your local machine.

 #### `sftp> mget filename1 filename2 filename2`
~~~ bash
sftp> mget remoteFile1.txt remoteFile2.txt remoteFile3.txt
~~~

Download several files from the remote machine to your local machine.

 #### `sftp> get -r directory`
~~~ bash
sftp> get -r remoteDirectory1
~~~

Download a directory and its contents from the remote machine to your local machine.

 #### `sftp> ?`
~~~ bash
sftp> ?

Available commands:
bye                                Quit sftp
cd path                            Change remote directory to 'path'
chgrp grp path                     Change group of file 'path' to 'grp'
chmod mode path                    Change permissions of file 'path' to 'mode'
chown own path                     Change owner of file 'path' to 'own'
df [-hi] [path]                    Display statistics for current directory or
filesystem containing 'path'
exit                               Quit sftp
get [-Ppr] remote [local]          Download file
reget remote [local]            Resume download file
help                               Display this help text
lcd path                           Change local directory to 'path'
lls [ls-options [path]]            Display local directory listing
lmkdir path                        Create local directory
ln [-s] oldpath newpath            Link remote file (-s for symlink)
lpwd                               Print local working directory
ls [-1afhlnrSt] [path]             Display remote directory listing
lumask umask                       Set local umask to 'umask'
mkdir path                         Create remote directory
progress                           Toggle display of progress meter
put [-Ppr] local [remote]          Upload file
pwd                                Display remote working directory
quit                               Quit sftp
rename oldpath newpath             Rename remote file
rm path                            Delete remote file
rmdir path                         Remove remote directory
symlink oldpath newpath            Symlink remote file
version                            Show SFTP version
!command                           Execute 'command' in local shell
!                                  Escape to local shell
?                                  Synonym for help
~~~

If you cannot remember how to execute a specific command, use the `?` to list all possible commands within _sftp_ with explanations of their functionality.
