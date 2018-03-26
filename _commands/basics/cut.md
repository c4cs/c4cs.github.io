---
---

cut
-------

`cut` is for cutting sections from each line of files and writing the result to standard output. 

~~~ bash
$ cut [OPTIONS] [FILE]
~~~

<!--more-->
It can be used to cut parts of a line by byte position, character and delimiter. It can also be used to cut data from file formats like CSV.
With no FILE, or when FILE is -, read standard input.

#### Useful Options / Examples
~~~bash

| Command |                | Description |

| -b, --bytes=LIST |       | select only these bytes |

| -c, --characters=LIST |  | select only these characters |

| -d, --delimiter=DELIM |  | use DELIM instead of TAB for field  delimeter |                               

| -f, --fields=LIST |      | select only these fields;  also print any 
                            that contains no delimiter character, unless
                            the -s option is specified |

~~~

For the following example, we will assume this is our csv file (people.csv)

~~~bash
Bill, Jones, Male, 20
Sally, Smith, Female, 21
Joe, Morgan, Male, 31
Alexandra, Smith, Female, 71
~~~

#### Example command
~~~bash
$ cut -d ',' -f 1 people.csv
Bill
Sally
Joe
Alexandra

##A cool thing we can do is redirect these changes to a new file##
$ cut -d ',' -f 1 people.csv > newPeople.csv 
~~~

##### Break it down
Here we took the original csv file, which had random peoples first name, last name, gender, and age. We wanted only the first name. To do this we use cut and specify a delimeter with `-d ','` to specify we want to read up until the comma. To then tell cut we only want the first row of information we use `-f 1`. Lastly we specify the file that we want to cut from. A smart thing to do is use `cat | cut ....` so that changes can be seen before they are made. Also, the changes can be redirected to a new file using the `>` operator and the end of the whole statement. 

#### Example command
~~~bash
$ cut -c '1,2,3' people.csv
Bil
Sal
Joe
Ale
~~~

##### Break it down
Here cut use the cut command with the `-c` flag. Using this with `1,2,3` specifys that we want the first, second, and third character on each line. Once again it is always wise to do `cat | cut ...` so that changes can be seen before they are saved.
