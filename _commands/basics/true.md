---
---

true
--

`true` is a command that does nothing and return a true value(0). 

~~~ bash
$ yes | true

~~~

<!--more-->

### Useful Options / Examples

#### `exec "/bin/true"`


~~~ bash
#!/usr/bin/env perl

exec "/bin/true";

END {
  print "This wont get printed .. would have if I just 'exit' or 'die'\n";
}
~~~ 
