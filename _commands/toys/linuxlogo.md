---
---

linuxlogo
-------
`linuxlogo`  is a Linux command line utility that generates a color ANSI picture of logo with a few system information.

To use `linuxlogo`, simply type:

~~~ bash
$ sudo apt install linuxlogo
$ linuxlogo 
~~~

<!--more-->

### Useful Commands / Examples
There are several flags that can change the information or color of the command output.
- `-a` generate the linux logo without color
- `-u` also display system uptime
- `-l` print LOGO only and exclude all other System Information

Another interesting flag is `-L`. There are a lots of built-in logos for various Linux distributions, which can also be accessed and printed using `-L` flag.
- `-L list` list other built-in logos for various Linux distributions
- `-L NUM` print logo with number NUM, where NUM is described in the list
- `-L NAME` print logo with name NAME, where NUM is described in the list

#### Example command

~~~bash
$ linuxlogo 
~~~
![linuxlogo](https://www.tecmint.com/wp-content/uploads/2015/06/Get-Default-OS-Logo.png)

~~~bash
$ linuxlogo -L 1
~~~
![linuxlogo](https://www.tecmint.com/wp-content/uploads/2015/06/Print-AIX-Logo.png)



Visit [here](https://www.tecmint.com/linux_logo-tool-to-print-color-ansi-logos-of-linux/) for more information.
