---
---

cd
-------

cd allows the user to change their working directory

~~~ bash
cd eecs398
cd wk06
cd advancedhw
~~~
If the user started in home and executed these three commands,
pwd would output "~/eecs398/wk06/advancedhw"

<!--more-->

### Useful Options / Examples

There are multiple shortcuts that can be used with cd:
  
  
#### Option .

"." represents your current directory

__Usage__:
`cd ./<subdirectory>`

__Functionality__:
Can be used to limit typing when you are "deep" in your system
For example, if you wanted to move a file from
`~/eecs398/wk06/hw`
down to
`~/eecs398/wk06/hw/problem1`
you could just go to the hw directory and use 
`mv <filename> ./problem1`
When using cd, omitting the "." will do the same thing, i.e. you can
cd into directories in your working directory with just their names
  
  
#### Option ..

".." represents the directory containing your current directory

__Usage__:
`cd ..`

__Functionality__:
Moves "up" one directory, changes your working directory to the directory 
containing your current directory 
This also works for longer paths, so if you are in 
`~/eecs398/wk06/advancedhw`
and you want to go to 
`~/eecs398/wk06/hw`
you can just use
`cd ../hw`
  
  
#### Option ~

"~" represents your home directory

__Usage__:
`cd ~`

__Functionality__:
This takes you all the way back to your home directory
Allows you to accomplish multiple iterations of "cd .." in one command
Omitting the ~ will do the same thing, i.e. cd without a command will 
default to the home directory
  
  
#### Option -

"-" represents the previous working directory

__Usage__:
`cd -`

__Functionality__:
Returns you to you previous working directory
This allows you to switch back and forth between directories
that are "far apart".  If you are in
`~/eecs398/wk06/advancedhw`
and you use "cd ~", you will be in your home directory.  If you then
use "cd -", you will be back in 
`~/eecs398/wk06/advancedhw`
