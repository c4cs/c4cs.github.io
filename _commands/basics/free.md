free

SYNOPSIS
       free [-b | -k | -m] [-o] [-s delay ] [-t] [-V]


DESCRIPTION
       free  displays the total amount of free and used physical and swap mem-
       ory in the system, as well as the buffers  used  by  the  kernel.   The
       shared memory column should be ignored; it is obsolete.

   Options
       The  -b  switch  displays  the amount of memory in bytes; the -k switch
       (set by default) displays it in kilobytes; the -m switch displays it in
       megabytes.

       The -t switch displays a line containing the totals.

       The -o switch disables the display of a "buffer adjusted" line.  If the
       -o option is not specified, free subtracts buffer memory from the  used
       memory and adds it to the free memory reported.

       The -s switch activates continuous polling delay seconds apart. You may
       actually specify any floating point number for delay, usleep(3) is used
       for microsecond resolution delay times.

       The -V displays version information.

reference: http://www.mediacollege.com/cgi-bin/man/page.cgi?topic=free
