---
---

nslookup
------- 

~~~ bash
nslookup www.google.com
~~~

<!--more-->


#### Example command
~~~ 
nslookup microsoft.com
~~~

The response would be: 

~~~
Server:		141.211.125.17
Address:	141.211.125.17#53

Non-authoritative answer:
Name:	microsoft.com
Address: 23.100.122.175
Name:	microsoft.com
Address: 23.96.52.53
Name:	microsoft.com
Address: 191.239.213.197
Name:	microsoft.com
Address: 104.40.211.35
Name:	microsoft.com
Address: 104.43.195.251
~~~

* Here 141.211.125.17 is the address of our system's DNS. #53 indicates that we are communicating with it on port 53, 
which is the standard port number DNS's use to accept queries. 
* Below this is the lookup info of microsoft.com. Here we get 5 different addresses which indicates that when you access 
microsoft.com you may be directed to any of these servers. 

#### Example command
~~~ 
nslookup 31.13.74.36
~~~

##### Break it down
This is the reverese lookup using the IP address
The response would be: 

~~~
Server:		141.211.125.17
Address:	141.211.125.17#53

Non-authoritative answer:
36.74.13.31.in-addr.arpa	name = edge-star-mini-shv-01-ord1.facebook.com.

Authoritative answers can be found from:
74.13.31.in-addr.arpa	nameserver = ns4.facebook.com.
74.13.31.in-addr.arpa	nameserver = ns5.facebook.com.
74.13.31.in-addr.arpa	nameserver = ns3.facebook.com.
74.13.31.in-addr.arpa	nameserver = a.ns.facebook.com.
74.13.31.in-addr.arpa	nameserver = b.ns.facebook.com.
a.ns.facebook.com	internet address = 69.171.239.12
a.ns.facebook.com	has AAAA address 2a03:2880:fffe:c:face:b00c:0:35
b.ns.facebook.com	internet address = 69.171.255.12
b.ns.facebook.com	has AAAA address 2a03:2880:ffff:c:face:b00c:0:35
ns3.facebook.com	internet address = 66.220.151.20
ns3.facebook.com	has AAAA address 2a03:2880:fffe:c:face:b00c:0:35
ns4.facebook.com	internet address = 69.171.245.32
ns4.facebook.com	has AAAA address 2a03:2880:ffff:c:face:b00c:0:35
ns5.facebook.com	internet address = 66.220.145.65
ns5.facebook.com	has AAAA address 2a03:2880:fffe:c:face:b00c:0:35
~~~

* These are the DNS addresses associated with facebook.com
* An AAAA record is what associates a domain name with the specific IP address, so that the browser knows where to go to access the website. 
* AAAA is associated with IPv6 (Internet Protocol version 6) records and A is associated with IPv4 records. The eight groups of four hexademinal digits seperated by colons is the IPv6 address. 
