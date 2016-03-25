---
---

head
--

`head` prints the first 10 lines of a file to the standard output. If more than one file is specified, `head` will print the filename first and then print the first ten lines of the file. Since a good programmer will always put comments at the beginning of a file, printing the first few lines of a file can help us identify what is in the file.

 

~~~ bash
$ head [options] ... [file] ...
~~~

<!--more-->

### Useful Options / Examples

~~~bash
$ head p2_skeleton.py 
# -*- coding: utf-8 -*-
"""
W16 EECS 445 - Introduction to Machine Learning
Project 2- "BOT-ANY"
Skeleton Code 
"""

import numpy as np
import project2 as p2
from scipy import stats

~~~


##### Break it down
* 'head' prints the first 10 lines of p2_skeleton.py to the standard output.    



#### `head -n [number of lines] [file]`
Sometimes, 10 lines might not be an optimal number. We might want to print more or less lines depending on situation. The '-n' option allows user to specify the number of lines from a file to be printed. <br>
Remark: The `-n` flag can be substituted with `--lines`.

~~~bash
$ head -n 9 project2.py p2_skeleton.py 
==> project2.py <==
"""

W16 EECS445 Introduction to Machine Learning
Project 2 - "BOT-ANY"

This file contains the helper functions that would be used in p2_skeleton.py.
Functions in this file: get_data(), showIm(), vecToImage(), plotGallery(), PCA()

"""

==> p2_skeleton.py <==
# -*- coding: utf-8 -*-
"""
W16 EECS 445 - Introduction to Machine Learning
Project 2- "BOT-ANY"

This file contains the Skeleton Code and classes that would be used to do different types of clustering.
 
"""
~~~


##### Break it down
* The `-n 9` tells the `head` command to print the first 9 lines of the two files.
* Since 2 files are specified, the `head` command prints the filename of each file first, then prints the content of the files.


#### `head -v [file]`
We can always ask the `head` to print out the filename by adding the `-v` option.<br>
Remark: `-v` can be substituted with `--verbose`.

~~~bash
$ head -v -n 9 p2_skeleton.py 
==> p2_skeleton.py <==
# -*- coding: utf-8 -*-
"""
W16 EECS 445 - Introduction to Machine Learning
Project 2- "BOT-ANY"

This file contains the Skeleton Code and classes that would be used to do different types of clustering.
 
"""
~~~

##### Break it down
* The `-v` flag tells the `head` to print the filename even though we only specify one file.


#### `head -q [file]`
The `-q` flags tells the `head` command not to print the filename.<br>
Remark: `-q` can be substituted with `--quiet`, `--silent`.

~~~bash
$ head --quiet -n 9 project2.py p2_skeleton.py 
"""

W16 EECS445 Introduction to Machine Learning
Project 2 - "BOT-ANY"

This file contains the helper functions that would be used in p2_skeleton.py.
Functions in this file: get_data(), showIm(), vecToImage(), plotGallery(), PCA()

"""
# -*- coding: utf-8 -*-
"""
W16 EECS 445 - Introduction to Machine Learning
Project 2- "BOT-ANY"

This file contains the Skeleton Code and classes that would be used to do different types of clustering.
 
"""
~~~


##### Break it down
* After adding `-q`, the filenames are not shown.


#### `ls | head`
The `head` command can be used with other commands, for instance, ls. 

~~~bash
$ ls | head
1a.0.jpeg
1a.30.jpeg
1a.60.jpeg
1c.jpeg
1d_100.jpeg
1d_10.jpeg
1d_1600.jpeg
1d_1.jpeg
1d_2.jpeg
1d_500.jpeg
~~~

##### Break it down
* By default, the `ls` command should print all the files in the current directory to the standard output. By using `|`, the output is passed to `head` and the first 10 files of the current directory are printed.


