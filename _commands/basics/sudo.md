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

The `-u` (user) option causes `sudo` to run the specified command as a user other than root.

##### Example

`sudo -u c4cs ls /home/Document`

This command lists the contents of `/home/Documents` as the user c4cs


