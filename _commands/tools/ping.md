---
---

ping
--

`ping` is used to test a connection to a network. You can use `ping` to check if your local machine can connect to a network or if a particular device is reachable from your machine. A `ping` may fail to reach a device if either device is blocked by a firewall.

~~~ bash
$ ping 192.168.1.1
PING 192.168.1.1 (192.168.1.1): 56 data bytes
64 bytes from 192.168.1.1: icmp_seq=0 ttl=255 time=1.518 ms
$
~~~

<!--more-->

### Useful Options / Examples

#### `ping website`

~~~ bash
$ ping google.com
PING google.com (216.58.216.206): 56 data bytes
64 bytes from 216.58.216.206: icmp_seq=0 ttl=55 time=19.213 ms
~~~

##### Break it down

 * `ping` can be used to check connections to websites or general internet connectivity as well as connections over a local network.

#### `ping -i`

~~~ bash
$ ping -i 1 192.168.1.1
~~~

##### Break it down

 * The `-i` flag tells `ping` how many seconds to wait between sending messages.

#### `ping -c`

~~~ bash
$ ping -c 5 192.168.1.1
~~~

##### Break it down

 * The `-c` flag tells `ping` how many messages to send before exiting.

#### `ping -f`

~~~ bash
$ ping -c 5 192.168.1.1
~~~

##### Break it down

 * The `-f` flag will tell `ping` to send messages as fast as it can and only report back the messages that timeout. This can be used to stress test a network.

 * when paired with `-c` you can do a controlled stress test with a limited number of messages.

#### `ping -q`

~~~ bash
$ ping -q -c 5 192.168.1.1
~~~

##### Break it down

 * The `-q` flag tells `ping` to only print out the summary of the session instead of each messages stats.

#### `ping 0`

~~~ bash
$ ping 0
~~~

##### Break it down

 * This is a special case of `ping` that pings the local network on your machine to make sure that is reachable.

 * The commands `ping localhost` and `ping 127.0.0.1` also perform this operation.