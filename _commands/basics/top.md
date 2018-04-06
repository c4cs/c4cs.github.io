---
---

top
--
top is a command that shows all the running processes in your Linux environment.

<!-- minimal example -->
~~~ bash
top
top -s 5
top -c a
top -n 5
~~~

Using it is as simple as inputting "top" into your command line. 

You should see a dynamic table that shows you the breakdown of all the running processes. 
To continue using your terminal, you can push top into the background by inputting "ctrl+c", and return to it by typing "fg".

There are many flags that you can use for top, but the main ones are probably:

### Useful Options / Examples
There are many flags that you can use for top, but the main ones are probably:
#### Example command
 -s [number]: specifies the delay interval between table updates.
##### Break it down
  -s 10: the -s specifies a flag for top, and the 10 after that specifies that you want the intervals between updates to be 10 seconds.
#### Example command
 -n [number]: specifies the number of processes to show in the table
##### Break it down
  -n 5: the -n specifies a flag for top, and 5 after that specifies that you only want to see 5 processes in the table.
