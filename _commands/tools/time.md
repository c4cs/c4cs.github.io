--------

time
--------
	
GENERAL FORM
		
	time   [ -apqvV ] [ -f FORMAT ] [ -o FILE ] [ --append ] [ --verbose ] [ --quiet ] [ --portability ]
        [ --format=FORMAT ] [ --output=FILE ] [ --version ] [ --help ] COMMAND [ ARGS ]

DESCRIPTION

	The time command prints out three separate times: the total time elapsed, the time used by system overhead and the time used to execute the utility.

	If the program exits non-zero it will print a warning message and then the exit status.	If the program does not exit normally, then the time command 
	returns 128 plus the number of the signal that caused the program to stop.

	If you are using a bash shell you must explicity specify "/usr/bin/time" rather than just "time"

	If the time is extremely small, this command may return zero or a question mark

AVAILABLE OPTIONS

	-o FILE --output=FILE
		The time statistics are written to the file FILE and any contents of FILE are overwritten

	-a, --append		 
		Append the time statistics to the resource file instead of overwritting the constents. This is only helpful when the -o or --output flag is set.
	
	-v, --verbose
		Prints all available information with description of its meaning

EXAMPLES

	To run the file project.cpp with command line args -m and input file input.txt, with the default output run the following command

		/usr/bin/time ./project -m < input.txt

	To run the above scenario, but output the time to a text file run the follwing command

		/usr/bin/time -o out.txt ./project -m <input.txt

	To show only the user, system and total time run the following command

		/usr/bin/time -f "\t%E real,\t%U user,\t%S sys" ./project

