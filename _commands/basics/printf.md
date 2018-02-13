---
---

printf
--

`printf` is used to format and output data.

~~~ bash
$ printf format [argument]
$ printf "%f\n" 7
7.000000
$ printf "%d\n " 0xF
15
~~~

<!--more-->

### Useful Options / Examples

#### `printf`
~~~ bash
$ printf "%f\n" 5
~~~

#### Break it down

* Prints out the number 5 as a float on a new line. The default is to print with 6 decimals.

~~~ bash
$ printf "\t\"Quotations\"\t\n"
	"Quotations"	
$
~~~

#### Break it down

* This command takes advantage of the ability for `printf` to use whitespace by adding tabs into the output using \t to add tabs and a newline at the end

* This command also demonstrates how to add characters to strings that would normally give a command to `printf`. Quotations usually specify what is meant to be fed into `printf`, but using \\" allows an actual double quote to be inserted into the string.

~~~ bash
$ printf "put a number here: %d and a different one here: %d\n" 21 45
put a number here: 21 and a different one here: 45
~~~

#### Break it down

* This command takes advantage of being able to insert decimal numbers into strings using the %d to refer to decimals

~~~ bash
$ whatIMade="variable"
$ myVariable=56
$ printf "I made a %s and its value is %d. Wow!\n" $whatIMade $myVariable
I made a variable and its value is 56. Wow!
~~~

#### Break it down

* Variables can be referenced and used in place of strings, decimals, or other types

#### Using printf in a script
The script input:

~~~ bash
#/bin/bash
line===============================
line=$line$line

header="\n %-10s %8s %10s %11s\n"
format=" %-10s %08d %10s %11.2f\n"

width=43

printf "$header" "ITEM NAME" "ITEM ID" "COLOR" "PRICE"

printf "%$width.${width}s\n" "$line"

printf "$format" \
Triangle 13  red 20 \
Oval 204449 "dark blue" 65.656 \
Square 3145 orange .7
~~~

After running script:

~~~ bash

ITEM NAME   ITEM ID      COLOR       PRICE
===========================================
 Triangle   00000013        red       20.00
 Oval       00204449  dark blue       65.66
 Square     00003145     orange        0.70
~~~

#### Break it down
* Using a script to be able to set up different variables to format terminal output to make a table
* header and format specify strings, decimals, and floats that are of a certain length to make table columns consistent



