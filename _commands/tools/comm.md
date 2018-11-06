---
---

comm
-------

comm is used to compare two text files, sorted lexically(alphabetically), by printing 
three columns of mutually exclusive output:
Column 1: Lines only in file 1
Column 2: Lines only in file 2
Column 3: Lines common to both files

~~~ bash
comm file1 file2
~~~


### Useful Options / Examples
There are 4 optional tags for comm:
+ "-1" supresses printing column 1
+ "-2" supresses printing column 2
+ "-3" supresses printing column 3
+ "-i" ignores case, so "apple" and "Apple" are treaed as identical


#### Example command
```
cat file1
2
3
4
5
7
9

cat file2
1
2
4
6

comm file1 file 2
        1
                2
3
				 4
5
        6
7 
9
```
##### Break it down
In the above example, we can see that the left column contains the items only in file1,
the middle column contains only items in file2, and the right column contains items
appearing in both files
