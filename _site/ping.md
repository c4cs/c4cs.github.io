ping
====

```
ping
```
is used to test the ability of the source computer to reach a destination computer.

The format is


```
$ ping domain_name
```

A basic example is

```
$ ping IP_adress_of_remote_host
``` 

This will ping the IP address of a remote host to verify that you can communicate through a router.

ping Command examples
====================

```
ping -n 7 -l 1500 www.google.com
```

In this example we ping the hostname *www.google.com* . The 
```
-n
```
option tells the command to send 7 ICMP Echo Requests, and the
```
-l
```
option sets the packets size for each request to 1500 bytes.

The default would be 4 ICMP Echo Requests and 32 bytes.

Other instances in which we can use the ping command are:

* to verify that TCP/IP is configured correctly on the local computer.

```
ping 127.0.0.1
```

* to verify that the IP address of the local computer  was added to the network correctly.

```
ping IP_address_of_local_host
```

Other options
=====

```
-n
```
Determines the number of echo requests to send. 

```
-w
```
Enables you to adjust the timeout (in milliseconds). 

```
-l
```
Enables you to adjust the size of the ping packet. 

```
-f
```
Sets the **Do Not Fragment** bit on the ping packet.

```
/?
```
Provides command Help.



