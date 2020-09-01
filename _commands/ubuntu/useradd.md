---
---

useradd
---
`useradd` is a low level utility that is used for adding/creating user accounts in Linux and other Unix-like operating systems.

The basic synax is as follows:

~~~ bash
$ useradd [options] username
~~~

<!--more-->

### Useful Options / Examples

### `Basic Command - No flags`

Basic Syntax:

~~~ bash
$ useradd exampleuser
~~~

This is the most basic command. The 'username' is the login name the user would log in with. Username must be unique and only one user can be added at a time. Users default home directory will be placed in the /home directory.

### `Create User with Different Home Directory -d Flag`

Basic Syntax:

~~~ bash
$ useradd -d [path/to/desired/directory] exampleuser
~~~

This command allows you to add a user with a different home directory than the default value of /home. The -d option is useful for certain users that are focused solely on a certain project. Their home directory could be set to the directory of their project for quick/easy access.

Example:

~~~ bash
$ useradd -d data/projects/Project1 exampleuser
~~~

### `Create User in Multiple Groups -G Flag`

Basic Syntax:

~~~ bash
$ useradd -G [Group List, comment delimited] exampleuser
~~~

-G command allows user to be added to specific groups upon account creation. This would be userful when creating a new Admin account. Instead of manually adding user to teach group, user could be added to the groups during creation
Example:

~~~ bash
$ useradd -G admins,webadmins exampleuser
~~~

### `Create User with Account Expiration Date -e flag`

Basic Syntax : 

~~~ bash
$ useradd -e [Date YYYY-MM-DD Format] exampleuser
~~~

The new user will only be able to login for a limited amount of time. This flag would be ideal for any seasonal or third party workers that need access to system for a limited amount of time.

Example: 

~~~ bash
$ useradd -e 2018-10-31 exampleuser
~~~

### `Create User with Custom Comments -c flag`
Basic Syntax:

~~~ bash
$ useradd -c <"Comments"> exampleuser
~~~

This option would be useful if you wanted to add additional information about the newly created user such as name, phone number or email.

Example:

~~~ bash
$ useradd -c "Example User 123-456-7890" exampleuser
~~~

