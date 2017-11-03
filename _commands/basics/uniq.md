---
---

uniq
------

`uniq`, often used with  `sort`, allows a user to report, or filter, repeated lines that are adjacent in a file. Some common and useful flags include -d or -u for listing lines that are duplicated or that are unique, respectfully. As well as -c for counting the number of times a line was dupicated.

<!-- minimal example -->
~~~ bash
$ sort in.txt | uniq -c 
  2 line1
  3 line2
  1 line3
~~~

<!--more-->

### Useful Options / Examples
Often used with sort, uniq will count the number of times a unique line appears in a file when given the -c flag

#### Example command
~~~ bash
$ sort in.txt | uniq -c 
  2 line1
  3 line2
  1 line3
~~~

##### Break it down
You can also use uniq to list only lines that are duplicates (-d flag) or that are unique (-u flag) 
##### Break it down

#### Example command
~~~ bash
$ sort in.txt | uniq -d
line1
line2
~~~
##### Break it down
