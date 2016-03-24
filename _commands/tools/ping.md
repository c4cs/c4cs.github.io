---
---

ping
--

`ping` is used to test connections to other machines on a network.

~~~ bash
$ ping 192.168.1.1
PING 192.168.1.1 (192.168.1.1): 56 data bytes
64 bytes from 192.168.1.1: icmp_seq=0 ttl=255 time=1.518 ms
$
~~~

<!--more-->

### Useful Options / Examples

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