---
---

tcpdump
-------

tcpdump is a tool that allows you to view a dump of traffic on a network. By default, tcpdump will let you view the dump on your local network.
You can use packet analyzing tools like Wireshark to analyze tcpdumps and pcap files.

~~~ bash
$ tcpdump 
~~~

<!--more-->

### Useful Options / Examples

Prerequisites
- AS ROOT (to obtain root access, follow step 4 here: http://www.wikihow.com/Become-Root-in-Ubuntu, or see SUDO NOTE at bottom) do the following steps:

~~~ bash
 groupadd pcap
 usermod -a -G pcap user
 chgrp pcap /usr/sbin/tcpdump
 chmod 750 /usr/sbin/tcpdump
 setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump
~~~

This is needed to be able to do tcpdump without sudo.

#### Example command

`tcpdump -S host <hostname>`

~~~ bash
$ sudo tcpdump -S host www.google.com
22:59:51.864876 IP 10.0.2.15.56854 > bud02s22-in-f196.1e100.net.http: Flags [P.], seq 1151492736:1151493304, ack 109760840, win 30168, length 568: HTTP: GET / HTTP/1.1
22:59:51.865629 IP bud02s22-in-f196.1e100.net.http > 10.0.2.15.56854: Flags [.], ack 1151493304, win 65535, length 0
22:59:52.031854 IP bud02s22-in-f196.1e100.net.http > 10.0.2.15.56854: Flags [P.], seq 109760840:109761678, ack 1151493304, win 65535, length 838: HTTP: HTTP/1.1 302 Found
22:59:52.031870 IP 10.0.2.15.56854 > bud02s22-in-f196.1e100.net.http: Flags [.], ack 109761678, win 31844, length 0
22:59:52.035854 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [P.], seq 2068573025:2068573116, ack 110036572, win 65320, length 91
22:59:52.036112 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [.], ack 2068573116, win 65535, length 0
22:59:52.277901 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110036572:110036648, ack 2068573116, win 65535, length 76
22:59:52.280812 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110036648:110040938, ack 2068573116, win 65535, length 4290
22:59:52.280833 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110040938, win 65535, length 0
...
... (continues)
~~~

##### Break it down

-The `-S` flag prints absolute TCP sequence numbers versus relative
-host <hostname> lets you specify a specific hostname to track requests and responses from a specific host (i.e. Google, Yahoo, eecs.umich.edu, etc.)

#### Example command

`tcpdump -S "tcp[tcpflags] & (tcp-syn|tcp-ack|tcp-fin) != 0"`

~~~ bash
$ tcpdump -S "tcp[tcpflags] & (tcp-syn|tcp-ack|tcp-fin) != 0"
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on enp0s3, link-type EN10MB (Ethernet), capture size 262144 bytes
23:13:35.006934 IP 10.0.2.15.44258 > ec2-204-236-230-155.compute-1.amazonaws.com.https: Flags [.], ack 210881678, win 32660, length 0
23:13:35.007386 IP ec2-204-236-230-155.compute-1.amazonaws.com.https > 10.0.2.15.44258: Flags [.], ack 2435184464, win 65535, length 0
23:13:38.226091 IP live.github.com.https > 10.0.2.15.47844: Flags [P.], seq 75075962:75075993, ack 2779464789, win 65535, length 31
23:13:38.226285 IP 10.0.2.15.47844 > live.github.com.https: Flags [P.], seq 2779464789:2779464824, ack 75075993, win 39760, length 35
23:13:38.226541 IP live.github.com.https > 10.0.2.15.47844: Flags [.], ack 2779464824, win 65535, length 0
23:13:45.022884 IP 10.0.2.15.44258 > ec2-204-236-230-155.compute-1.amazonaws.com.https: Flags [.], ack 210881678, win 32660, length 0
23:13:45.023070 IP ec2-204-236-230-155.compute-1.amazonaws.com.https > 10.0.2.15.44258: Flags [.], ack 2435184464, win 65535, length 0
...
... (continues)
~~~

##### Break it down

- This command will let you watch the 3-way handshake between different clients and servers that are functioning on your network. Specifies that tcpflags are active and that at least one of the syn, ack, or fin flags are selected.
- You can save this output or the above output with the redirection >.
- You can obviously combine the above two and specify a specific host to watch the 3-way handshake on for more specified traffic monitoring.
- SUDO NOTE: if you don't want to follow the above steps to become root user, you CAN use `sudo -s` or `sudo su` to drop into a root prompt. 
  See https://c4cs.github.io/commands/basics/sudo.html for more info on sudo, its uses and its dangers.
