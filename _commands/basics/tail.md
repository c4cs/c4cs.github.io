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
$ tail -f -n 5 input.txt
		*x = y1- (floor(b/a) *x1);
		*y = x1;
		return gcd;
	}
	return 1000;
[waiting for more]
~~~

##### Break it down
* Shows the last 5 lines of input.txt. The -f command causes tail to not stop but rather waits for additional data to be added to file

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
* Shows the lines of input.txt in reverse order. The default -r option is to display all of the input but this may be changed with the -b, -c, and -n  flags. In this example, we showed the last 5 lines.

#### `man tail`

##### Break it down
* Shows the documentation for tail.