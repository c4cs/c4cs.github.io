---
---

date
-------
The date command is used to print out, or change the value of, the system's time and date information
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$date

output - Thu Feb 8 16:47:32 MST 2001
~~~

<!--more-->

### Useful Options / Examples

Format -- a sequence of characters which specifies how output will appear:

"%%" - A literal percent sign ("%")

%a - The abbreviated weekday name (Mon, Tues, Wed, Th, Fri)

%A - The full weekday name (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday)

%b - The abbreviated month name
 
%B - Locale's full month name

%H - Hour(00..23)

%n - A newline

%T - Time; same as %H:%M:%S

%Y - year

#### Example command

`ls -al > output_$(date+"%m_%d_%Y")`

##### Break it down

In bash, this command will generate a directory listing with ls, and redirect the output to a file 
which includes the current day, month, and year in the file name. It does this using bash command 
substitution, running the date command in a subshell and inserting that output into the original command.
