---
---

tail
-------

Tail displays the last part(s) of a file

~~~ bash
$ tail input.txt
$ tail -f -n 15 input.txt
~~~

<!--more-->

### Useful Options / Examples

#### `tail input.txt`

~~~ bash
$ tail input.txt
	}
else {
		int x1 =0;
		int y1=0;
		int gcd = inverse_helper(b%a, a, &x1, &y1);
		*x = y1- (floor(b/a) *x1);
		*y = x1;
		return gcd;
	}
	return 1000;
~~~

##### Break it down
* Shows the last 10 lines of input.txt

#### `tail -f -n 5 input.txt`


~~~ bash
# Or /var/log/system.log on OS X
$ tail -f -n 5 /var/log/syslog
Mar 26 13:46:01 nuclear avahi-daemon[623]: Invalid legacy unicast query packet.
Mar 26 13:46:01 nuclear avahi-daemon[623]: Received response from host 141.212.11.247 with invalid source port 56203 on interface 'eth0.0'
Mar 26 13:46:01 nuclear avahi-daemon[623]: Invalid legacy unicast query packet.
Mar 26 13:46:01 nuclear avahi-daemon[623]: Received response from host 141.212.11.247 with invalid source port 56203 on interface 'eth0.0'
Mar 24 23:13:56 nuclear console-kit-daemon[4027]: GLib-CRITICAL: Source ID 14892 was not found when attempting to remove it
[waiting for more]
~~~

##### Break it down
* Shows the last 5 lines of input.txt. The `-f` command causes tail to not stop but rather waits for additional data to be added to file

#### `tail -r -n 5 input.txt`

~~~ bash
$ tail -r -n 5 input.txt
return 1000;
	}
		return gcd;
		*y = x1;
		*x = y1- (floor(b/a) *x1);
~~~

##### Break it down
* Shows the lines of input.txt in reverse order. The default `-r` option is to display all of the input but this may be changed with the `-b`, `-c`, and `-n`  flags. In this example, we showed the last 5 lines.
