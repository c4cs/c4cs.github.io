---
---

ifconfig
--

`ifconfig` is used to configure a network interface or display information about all active or inactive connections.

<div class="alert alert-warning">
<a href="/"></a>Warning: While ifconfig is still used, it is recommended to use iproute2 (Linux) or iproute2mac <a href="/commands/ip" style="font-weight:bold;">[See reference on 'ip'].</a> ip is a much more powerful tool that can do everything ifconfig can do, and lots more.
</div>

<!--more-->

### Display Interfaces

Without an argument, `ifconfig` will print all active interfaces.

`ifconfig -a` will print all inactive interfaces along with the active ones.

An interface is usually a driver type followed by its unit number. 

For example `eth0` resolves to the first ethernet interface and `en0` to the first wireless one.

##### *On Linux, wireless interfaces are called wlan0,wlan1,etc.*

~~~ bash
$ ifconfig en0    #display info about wireless connection 0

en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
  ether AA:BB:CC:DD:EE:FF
  inet6 fe80::4cd:32c1:df16:a80a%en0 prefixlen 64 secured scopeid 0x4 
  inet 192.168.1.8 netmask 0xffffff00 broadcast 192.168.1.25
  nd6 options=201<PERFORMNUD,DAD>
  media: autoselect
  status: active
~~~
- The machine has a wireless connection that is active, up, and running, with an IP address of 192.168.1.8.
- ether refers to the MAC address of the machine.
- mtu refers to the Maximum Transmission Unit or the limit on the size of packets sent.

More information on the output can be found on Linux's documentation <a href="http://linuxcommand.org/man_pages/ifconfig8.html" target="_blank">here.</a>

### Turning Interfaces On or Off

A quick and easy way to reset your connection from the command line.

~~~ bash
$ sudo ifconfig en0 down
$ sudo ifconfig en0 up
~~~

### Configure IP and MAC

~~~ bash
# Change an interfaces IP address 
$ sudo ifconfig en0 192.168.1.9

# Modify your machines MAC
$ sudo ifconfig en0 ether AA:BB:CC:DD:EE:FF
~~~
