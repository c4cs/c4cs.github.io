---
---

sudo
-------

`sudo` stands for *Super User DO* and allows the user to run any command as the root user

~~~ bash
sudo shutdown -r now
~~~

The above command shuts down the system as the root user

---

### Useful Options / Examples

#### `sudo -u`

The `-u` (user) option causes `sudo` to run the specified command as a user other than root

##### Example

`sudo -u c4cs ls /home/Document`

This command lists the contents of `/home/Documents` as the user c4cs

#### `sudo -v`

The `-v` (validate) option updates the users timestamp and extends the `sudo` timeout for 5 minutes

Assuming one already has sudo access, running this command will allowing them to continue using the same sudo privledges for 5 minutes without authentication

#### `sudo -k`

The `-k` (kill) option removes a user's timestamp from `sudo` and takes away their root privledges

The next sudo command will require a password

### `sudo -b`

The `-b` (background) option will run the command listed in `sudo` in the background

#### Example

`sudo -b g++ hugeFile0.cpp hugeFile1.cpp hugeFile2.cpp -o largeExecutable`

This command will compile the three given files (potentially taking a very long time) in the background as the root user
