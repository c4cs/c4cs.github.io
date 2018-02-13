---
---

yes
---

`yes` will continuously output lines with `y` until user uses ctrl+c to stop. `yes` Can be useful for automating
scripts.

~~~ bash
$ yes
y
y
^C
$ yes n
n
n
n
^C
~~~

<!--more-->

### Useful Options / Examples

#### `yes | rm -i *.txt`

~~~ bash
$ls -l *txt
-rw-r--r--  1 apple  staff  0 Mar 25 00:54 1.txt
-rw-r--r--  1 apple  staff  0 Mar 25 00:54 2.txt
-rw-r--r--  1 apple  staff  0 Mar 25 00:54 3.txt
$yes | rm -i *.txt
remove 1.txt? remove 2.txt? remove 3.txt? %
~~~

##### Break it down

* Pipe `yes` to the following command to automatically make the following command prove any raised question with form `[y/n]`.

* When using `rm -i` to delete normal files, the system will ask user for confirmation of removing the file. At this time, the `yes` command will be able to simplify the process of repeatedly typing in yes. Here `yes | rm -i *.txt` will continuously pipe yes to the command `rm -i` to confirm the deleting operation.

#### `yes [text] > [filename]`

~~~ bash
#!/bin/sh  
  
yes hello >hello.txt &  
PID=$!  
  
sleep 1  
kill $PID 
~~~

##### Break it down

* The yes command is convenient to generate repeated text. We can use it in shell script like above to generate a file with repeated string `hello`. Here we run the `yes hello` for 1 second to generate large number of `hello`. We can also use `yes hello | head 1000` to generate `hello` 1000 times.