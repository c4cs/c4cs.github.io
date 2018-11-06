---
---
 mkdir
-------
 mkdir lets the user to create a new directory

~~~ bash
$ mkdir filename # This will create a directory named filename in your current directory
$ mkdir /eecs398/week2 # This will create directory week2 in the directory named eecs398. If eecs398 does not exists, you will get an error. Read the below flags to see how you can resolve this issue
~~~

 <!--flags-->
 ### Useful Options / Examples
 There are some flags you can use while using mkdir. Some common ones are listed below:
  
  
#### Option m
 "m" stands for mode. You can use the -m or --mode flag 
 __Usage__:
`mkdir -m a=rwx mydir`
 __Functionality__:
Set the file mode (permissions, etc.) for the created directories. The syntax of mode is the same as with the chmod command.
  
  
#### Option v
 "v" stands for verbose. You can use the -v or --verbose flag
`mkdir -v eecs_hw_folder`
 __Functionality__:
If you use this flag, there will be an output once you created the directory for feedback purposes
  
#### Option p
 "p" stands for parents
 __Usage__:
`mkdir -p /eecs398/hw1/problem1`
 __Functionality__:
The parents flag is useful for if you want to make the problem1 directory in a specific folder as shown in the example, but intermediate folders like hw1 is missing, using this flag will automatically create the intermediate directories if needed instead of giving you a do not exists error if you did not set this flag.
  