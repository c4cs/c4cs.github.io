---
---

time
---

time prints out the total time elapsed, the time used by system overhead and the time used to execute the utility.
If you are using a bash shell you must specify /usr/bin/time not just time.
If the time is very small it may just print zeros or a ?.

---
---
	
General Form:
---

~~~ bash	
	$ time   [ -apqvV ] [ -f FORMAT ] [ -o FILE ] [ --append ] [ --verbose ] [ --quiet ] [ --portability ]
          [ --format=FORMAT ] [ --output=FILE ] [ --version ] [ --help ] COMMAND [ ARGS ]
~~~

---
---
Options

---

	-o FILE --output=FILE
		The time statistics are written to the file FILE and any contents of FILE are overwritten

	-a, --append		 
		Append the time statistics to the resource file instead of overwritting the constents. This is only helpful when the -o or --output flag is set.
	
	-v, --verbose
		Prints all available information with description of its meaning
---
---

Examples
---

	To run the file project.cpp with command line args -m and input file input.txt, with the default output run the following command
~~~ bash
		/usr/bin/time ./project -m < input.txt
~~~
	To run the above scenario, but output the time to a text file run the follwing command
~~~ bash
		/usr/bin/time -o out.txt ./project -m <input.txt
~~~
	To append and not overwrite the text file run the follwing command
~~~ bash
		/usr/bin/time -o out.txt -a ./project -m <input.txt
~~~
	To show only the user, system and total time run the following command
~~~ bash
		/usr/bin/time -f "\t%E real,\t%U user,\t%S sys" ./project
~~~
	
