--------
--------

time
--------
	
GENERAL FORM
		
	time   [ -apqvV ] [ -f FORMAT ] [ -o FILE ] [ --append ] [ --verbose ] [ --quiet ] [ --portability ]
        [ --format=FORMAT ] [ --output=FILE ] [ --version ] [ --help ] COMMAND [ ARGS ]

DESCRIPTION

	The time command prints out three separate times: the total time elapsed, the time used by system overhead and the time used to execute the utility.
	These times are reported in seconds. It takes in the COMMAND and and ARGS for the command. If the program exits non-zero it will print a warning
	message and then the exit status.
	
	If the program does not exit normally, then the time command returns 128 plus the number of the signal that caused the program to stop.

	time displays its output based on the string FORMAT. If that string nor the TIME environment variable are set, the default value is used. If the time
	environment variable is set, its value will be used.
	
	Any arguments past the COMMAND are considered arguments for the program.

	If you are using a bash shell you must explicity specify "/usr/bin/time" rather than just "time"

ACCURACY

	If the time is extremely small, this command may return zero or a question mark

	This command uses the wait3(2) system call when available so the prescision is limited by this function. If wait3(2) is not available, the command uses
	times(2) which is much less precise. Times(2) produces much less output than wait3(3) so many of the recources may be reported as zeros.

	

AVAILABLE OPTIONS

	-o FILE --output=FILE
	
		The time statistics are written to the file FILE and any contents of FILE are overwritten

	-a, --append		 

		Append the time statistics to the resource file instead of overwritting the constents. This is only helpful when the -o or --output flag is set.

	-f FORMAT , --format FORMAT

		FORMAT specifies the format used to output timing information. The types of formats are below.

	--help
	
		Print a summary of command line options

	-p, --portability 

		Use the following for format
		
		real %e
                user %U
                sys %S

	-v, --verbose

		Prints all available information with description of its meaning
	
	--quiet

		Do not report exit status of program, whether the status is zero or non-zero

	-V, --version

		Print the version number and exit

OUTPUT FORMATTING

	The default format is:
         %Uuser %Ssystem %Eelapsed %PCPU (%Xtext+%Ddata %Mmax)k
         %Iinputs+%Ooutputs (%Fmajor+%Rminor)pagefaults %Wswaps

	(%) percent sign		
		Causes the following character to be interpreted as a resource specifier.
	(\) backslash 
		Introduces a backslash escape.
		(\t) Outputs a tab
		(\n) Outputs a newline 
		(\\) Outputs a backslash
		(\*) Outputs a question mark where * is anything that is not 't', 'n' or '\' indicating an invalid command
	
	Time automatically outputs a newline at the end
	Any other text is copied verbatim

	RESOURCE SPECIFIERS
	
	      C      Name and command line arguments of the command being timed.
              D      Average size of the process's unshared data area, in Kilobytes.
              E      Elapsed real (wall clock) time used by the process, in
                     [hours:]minutes:seconds.
              F      Number of major, or I/O-requiring, page faults that occurred
                     while the process was running.  These are faults where the page
                     has actually migrated out of primary memory.
              I      Number of file system inputs by the process.
              K      Average total (data+stack+text) memory use of the process, in
                     Kilobytes.
              M      Maximum resident set size of the process during its lifetime, in
                     Kilobytes.
              O      Number of file system outputs by the process.
              P      Percentage of the CPU that this job got.  This is just user +
                     system times divided by the total running time.  It also prints a
                     percentage sign.
              R      Number of minor, or recoverable, page faults.  These are pages
                     that are not valid (so they fault) but which have not yet been
                     claimed by other virtual pages.  Thus the data in the page is
                     still valid but the system tables must be updated.
              S      Total number of CPU-seconds used by the system on behalf of the
                     process (in kernel mode), in seconds.
              U      Total number of CPU-seconds that the process used directly (in
                     user mode), in seconds.
              W      Number of times the process was swapped out of main memory.
              X      Average amount of shared text in the process, in Kilobytes.
              Z      System's page size, in bytes.  This is a per-system constant, but
                     varies between systems.
              c      Number of times the process was context-switched involuntarily
                     (because the time slice expired).
              e      Elapsed real (wall clock) time used by the process, in seconds.
              k      Number of signals delivered to the process.
 	      p      Average unshared stack size of the process, in Kilobytes.
              r      Number of socket messages received by the process.
              s      Number of socket messages sent by the process.
              t      Average resident set size of the process, in Kilobytes.
              w      Number of times that the program was context-switched
                     voluntarily, for instance while waiting for an I/O operation to
                     complete.
              x      Exit status of the command.

EXAMPLES

	To run the file project.cpp with command line args -m and input file input.txt, with the default output run the following command

		time ./project -m < input.txt

	To run the above scenario, but output the time to a text file run the follwing command

		time -o out.txt ./project -m <input.txt

	To show only the user, system and total time run the following command

		time -f "\t%E real,\t%U user,\t%S sys" ./project

*******************************************************************************************************************************************

	IF YOU'RE USING A BASH SHELL YOU NEED TO EXPLICITLY STATE THE PATH TO RUN THE COMMAND TIME.
	EACH OF THE ABOVE EXAMPLES WOULD CHANGE "time" to "/usr/bin/time"
