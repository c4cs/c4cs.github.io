---
---

tcpdump
-------

tcpdump is a tool that allows you to view a dump of traffic on a network. By default, tcpdump will let you view the dump on your local network.

~~~ bash
$ tcpdump 
~~~

<!--more-->

### Useful Options / Examples

#### Example command

tcpdump -S host <hostname>

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
22:59:52.280865 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110040938:110042368, ack 2068573116, win 65535, length 1430
22:59:52.280869 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110042368, win 65535, length 0
22:59:52.284719 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110042368:110045228, ack 2068573116, win 65535, length 2860
22:59:52.284737 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110045228, win 65535, length 0
22:59:52.284764 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110045228:110048088, ack 2068573116, win 65535, length 2860
22:59:52.284768 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110048088, win 65535, length 0
22:59:52.284782 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110048088:110050252, ack 2068573116, win 65535, length 2164
22:59:52.284785 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110050252, win 65535, length 0
22:59:52.291162 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110050252:110051682, ack 2068573116, win 65535, length 1430
22:59:52.291178 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110051682, win 65535, length 0
22:59:52.291206 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110051682:110057402, ack 2068573116, win 65535, length 5720
22:59:52.291210 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110057402, win 65535, length 0
22:59:52.298169 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110057402:110061692, ack 2068573116, win 65535, length 4290
22:59:52.298185 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110061692, win 65535, length 0
22:59:52.298213 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110061692:110067272, ack 2068573116, win 65535, length 5580
22:59:52.298217 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110067272, win 65535, length 0
22:59:52.311929 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110067272:110071562, ack 2068573116, win 65535, length 4290
22:59:52.311947 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110071562, win 65535, length 0
22:59:52.311976 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110071562:110081572, ack 2068573116, win 65535, length 10010
22:59:52.311983 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110081572, win 65535, length 0
22:59:52.408516 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110081572:110084203, ack 2068573116, win 65535, length 2631
22:59:52.408532 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110084203, win 65535, length 0
22:59:52.408559 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110084203:110085633, ack 2068573116, win 65535, length 1430
22:59:52.408564 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110085633, win 65535, length 0
22:59:52.415046 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110085633:110091353, ack 2068573116, win 65535, length 5720
22:59:52.415063 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110091353, win 65535, length 0
22:59:52.415089 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110091353:110092458, ack 2068573116, win 65535, length 1105
22:59:52.415299 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [P.], seq 2068573116:2068573162, ack 110092458, win 65535, length 46
22:59:52.415515 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [.], ack 2068573162, win 65535, length 0
22:59:52.820267 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [P.], seq 2068573162:2068573471, ack 110092458, win 65535, length 309
22:59:52.820852 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [.], ack 2068573471, win 65535, length 0
22:59:52.970387 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110092458:110092543, ack 2068573471, win 65535, length 85
22:59:52.972855 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [P.], seq 110092543:110092589, ack 2068573471, win 65535, length 46
22:59:52.973051 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [.], ack 110092589, win 65535, length 0
22:59:52.973194 IP 10.0.2.15.59170 > bud02s22-in-f196.1e100.net.https: Flags [P.], seq 2068573471:2068573517, ack 110092589, win 65535, length 46
22:59:52.973558 IP bud02s22-in-f196.1e100.net.https > 10.0.2.15.59170: Flags [.], ack 2068573517, win 65535, length 0
23:00:02.046795 IP 10.0.2.15.56854 > bud02s22-in-f196.1e100.net.http: Flags [.], ack 109761678, win 31844, length 0
23:00:02.047116 IP bud02s22-in-f196.1e100.net.http > 10.0.2.15.56854: Flags [.], ack 1151493304, win 65535, length 0
23:00:12.062722 IP 10.0.2.15.56854 > bud02s22-in-f196.1e100.net.http: Flags [.], ack 109761678, win 31844, length 0
23:00:12.062908 IP bud02s22-in-f196.1e100.net.http > 10.0.2.15.56854: Flags [.], ack 1151493304, win 65535, length 0
~~~
##### Break it down
-The -S flag prints absolute TCP sequence numbers versus relative
-host <hostname> lets you specify a specific hostname to track requests and responses from a specific host (i.e. Google, Yahoo, eecs.umich.edu, etc.)
#### Example command

tcpdump -S "tcp[tcpflags] & (tcp-syn|tcp-ack|tcp-fin) != 0"

~~~ bash
$ sudo tcpdump -S "tcp[tcpflags] & (tcp-syn|tcp-ack|tcp-fin) != 0"
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on enp0s3, link-type EN10MB (Ethernet), capture size 262144 bytes
23:13:35.006934 IP 10.0.2.15.44258 > ec2-204-236-230-155.compute-1.amazonaws.com.https: Flags [.], ack 210881678, win 32660, length 0
23:13:35.007386 IP ec2-204-236-230-155.compute-1.amazonaws.com.https > 10.0.2.15.44258: Flags [.], ack 2435184464, win 65535, length 0
23:13:38.226091 IP live.github.com.https > 10.0.2.15.47844: Flags [P.], seq 75075962:75075993, ack 2779464789, win 65535, length 31
23:13:38.226285 IP 10.0.2.15.47844 > live.github.com.https: Flags [P.], seq 2779464789:2779464824, ack 75075993, win 39760, length 35
23:13:38.226541 IP live.github.com.https > 10.0.2.15.47844: Flags [.], ack 2779464824, win 65535, length 0
23:13:45.022884 IP 10.0.2.15.44258 > ec2-204-236-230-155.compute-1.amazonaws.com.https: Flags [.], ack 210881678, win 32660, length 0
23:13:45.023070 IP ec2-204-236-230-155.compute-1.amazonaws.com.https > 10.0.2.15.44258: Flags [.], ack 2435184464, win 65535, length 0
23:13:45.370676 IP 192.30.252.92.https > 10.0.2.15.41720: Flags [P.], seq 4164241:4164272, ack 185496046, win 65535, length 31
23:13:45.370845 IP 10.0.2.15.41720 > 192.30.252.92.https: Flags [P.], seq 185496046:185496081, ack 4164272, win 39760, length 35
23:13:45.371076 IP 192.30.252.92.https > 10.0.2.15.41720: Flags [.], ack 185496081, win 65535, length 0
...
... (continues)
~~~
##### Break it down
-This command will let you watch the 3-way handshake between different clients and servers that are functioning on your network. Specifies that tcpflags are active and that at least one of the syn, ack, or fin flags are selected.
-You can save this output or the above output with the redirection >.
-NOTE: you can obviously combine the above two and specify a specific host to watch the 3-way handshake on for more specified traffic monitoring.

