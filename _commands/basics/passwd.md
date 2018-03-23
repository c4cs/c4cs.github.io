---
---

passwd
-------
`passwd` is used to change the password of a user account
<!-- one line explanation would go here -->

<!-- minimal example -->

~~~ bash
$ passwd [OPTION] [USER]
~~~

<!--more-->

### Useful Options / Examples
A user can run `passwd` to change their own password and a superuser can use `passwd` to change another user's password.

#### `passwd`

~~~ bash
$ passwd
Changing password for [USER].
(current) UNIX password:
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
~~~

##### Break it down
 * `passwd` with no options or user specified will change the password of the user running the command.

#### `sudo passwd [OTHER_USER]`

~~~ bash
$ sudo passwd other
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
~~~

##### Break it down
 * If you have superuser privileges, you can modify the password of other users.
 * Prefix the command with `sudo` to run it as a superuser.
 * This will allow you to change the password for another user and not be prompted for their password.

#### `sudo passwd -S [OTHER_USER]`

~~~ bash
$ sudo passwd -S other
other P 10/17/2017 0 99999 7 -1
~~~

##### Break it down
* The `-S` option displays password information for a given user.
* The 7 fields correspond to the following values:
    1. User's login name
    2. Password usability ('L' if locked, 'NP' if there is no password, 'P' if there is a usable password)
    3. Date of last password change
    4. Minimum password age (days)
    5. Maximum password age (days)
    6. Warning period before a required password change
    7. Number of days to change a password after the maximum password age is reached

#### `sudo passwd -l [OTHER_USER]`

~~~ bash
$ sudo passwd -l other
passwd: password expiry information changed.
$ sudo passwd -S other
other L 10/17/2017 0 99999 7 -1
~~~

##### Break it down
* The `-l` option allows a superuser to lock another user's account by disabling their password.
* To have their password unlocked, a user will need to contact a superuser to unlock it.
* User's who have had their password locked can still login using other authentication methods (SSH).

#### `sudo passwd -u [OTHER_USER]`

~~~ bash
$ sudo passwd -u other
passwd: password expiry information changed.
$ sudo passwd -S other
other P 10/17/2017 0 99999 7 -1
~~~

##### Break it down
* The `-u` option allows a superuser to unlock another user's account by enabling their previous password.

#### `sudo passwd -d [OTHER_USER]`

~~~ bash
$ sudo passwd -d other
passwd: password expiry information changed.
$ sudo passwd -S other
other NP 10/17/2017 0 99999 7 -1
~~~

##### Break it down
* The `-d` option allows a superuser to delete another user's password.
* This will disable logins for a users account, without disabling their account completely.

#### `sudo passwd -e [OTHER_USER]`

~~~ bash
$ sudo passwd -e other
passwd: password expiry information changed.
$ sudo passwd -S other
other P 01/01/1970 0 99999 7 -1
~~~

##### Break it down
* The `-e` option allows a superuser to expires another user's account which will require that user to change their password.
