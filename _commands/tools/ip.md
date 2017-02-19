---
---
ip
----

`ip` is a powerful networking tool that when simply used will display information on kernel-resident interfaces. Much like `ifconfig`, it can turn devices on/off and set IP and MAC addresses. `ip` also wraps popular commands like `netstat`, `ndp`, `arp`, and `route` into its functionality.

~~~ bash
# Close the first ethernet connection 
$ ip link set dev eth0 down
~~~

<!--more-->

### Mac Users

`iproute2mac` is available through Homebrew as a compatible version. 

It is NOT fully compatible though. It's source and documentation can be found on github <a href="https://github.com/brona/iproute2mac" target="_blank">here.</a>

Also, `en0` is the equivalent to Linux's `wlan0` wireless interface.

### ip vs. ifconfig

##### Display ethernet interface 1

~~~ bash
$ ifconfig eth1

$ ip addr show eth1
~~~

#####  Turn eth1 off

~~~ bash
$ ifconfig eth1 down

$ ip link set eth1 down
~~~

#####  Set eth1 IP to 192.168.1.1

~~~ bash
$ ifconfig eth1 192.168.1.1

$ ip addr add 192.168.1.1/24 dev eth1
~~~

### MAC Address

~~~ bash
$ ip link set dev eth0 AA:BB:CC:DD:EE:FF    #custom MAC
$ ip link set eth0 address random           #random MAC
$ ip link set eth0 address factory          #restore MAC to default
~~~

### Neighbor (ARP)

The `neigh` or `n` command displays the neighbor table or ARP cache.

This displays a list of protocol addresses for all hosts sharing the same link.

`arp -n -a` displays the same table just in a different format.

~~~ bash
$ ip neigh en0

192.168.1.255 dev en0 INCOMPLETE
224.0.0.251 dev en0 lladdr AA:BB:CC:DD:EE:FF REACHABLE
239.255.255.250 dev en0 lladdr AA:BB:CC:DD:EE:FF REACHABLE
~~~
  - [IP] dev [interface] [MAC] [STATUS]
  
### Routing Tables

The `route` or `r` command will show the kernels main routing table.

`netstat -r` has a similar output.

~~~ bash
$ ip r

127.0.0.0/8 via 127.0.0.1 dev lo0
192.168.1.0/24 dev en0  scope link
192.168.1.1/32 dev en0  scope link
192.168.1.8/32 dev en0  scope link
224.0.0.0/4 dev en0  scope link
255.255.255.255/32 dev en0  scope link

~~~
