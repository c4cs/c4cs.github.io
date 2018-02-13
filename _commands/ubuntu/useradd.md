---
---

useradd
--------

`useradd` is used to create a new user or update default new user information 

On Debian, `adduser` should be used instead.  


~~~ bash
$ useradd [options] username
~~~


<!--more-->

### Details
`useradd` edits /etc/passwd, /etc/shadow, /etc/group, and /etc/gshadow files for new user account.

`useradd` creates and populates a home director for new user

`useradd` sets permissions and ownerships to home directory


### Useful Options

#### `useradd -d`

~~~bash
$ useradd -d /projects/users helloworld

# To verify location of the new home directory
$ cat /etc/passwd | grep helloworld
helloworld:x:500:500::/projects/users:/bin/bash
~~~

 * The `-d` flag option allows you to choose the location of the new home directory
 * By default the `useradd` command creates the home directory under /home directory with username

 
 
#### `useradd -u`

~~~bash
$ useradd -u 750 newUser

# To verify UID
$ cat /etc/passwd | grep newUser
newUser:x:750:750::/home/newUser:/bin/bash
~~~

 * Every user has its own unique identification numer (UID). By default, new user accounts are assigned UID 500, 501, 502, and so on
 * The `-u` flag option allows you to choose a specific UID

 

#### `useradd -e`

~~~bash
$ useradd -e 2016-10-10 expireUser

# To verify when account expires
$ chage -l expireUser
Last password change								: Mar 27, 2016
Password expires									: never
Password inactive									: never
Account expires										: Oct 10, 2016
Minimum number of days between password change		: 0
Maximum number of days between password change		: 99999
Number of days of warning before password expires	: 7

~~~

 * By default, `useradd` creates accounts that never expire
 * The `-e` flag option allows you to create temporary accounts 
 * Use the date in YYYY-MM-DD format for desired date

 

#### `useradd -f`

~~~bash
$ useradd -f 20 inactive	
~~~

 * The `-f` option will permanently disable an account after the desired amount of days after a password has expired. 
 

### Final details
After adding a new user with `useradd`, the new account will be locked.
To unlock the user account, you'll need to set a password with the `passwd` command.

~~~bash
$ useradd newperson
$ passwd newperson
Changing password for user newperson
New password:
Retype new password:
passwd: all authentication tokens updated successfully
~~~
