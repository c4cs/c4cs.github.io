---
---
## Updating your PS1 permanently 
-------------

Here you will find a small walk through on updating your `PS1` permanantley in your `/ .bashrc` file 

1.What is a `PS1`?


	PS1 stands for Prompt String 1. It's the thing that appears when you open your terminal something like:

	username-desktop:~$

2.What can we do with `PS1`?

	We can actually do a lot! We can write bash scripts to change our command prompts denpending on what file we are in or we can create a new static PS1. 

	We can take a generic prompt like username-desktop:~$
	and turn it into something like [Sat Feb 28 1:00 PM] username:~$

	or something that has git integration such as:
	username[master]~

3.Beginning to code your `PS1`.
	
	Your PS1 is made up of a mixture of characters. 
	For example here's code that would make up a PS1 prompt. 

	PS1="\u\h\[\e[32m\]\W\[\e[m\]\[\e[31m\]\d\[\e[m\]"

	Now this may look daunting initially but the characters are actually straight forward 

	`\u`=the username of the current user
	`\h`=the hostname up to the first .
	`\W`=the basename of the current working directory
	`\d`=the date in "Weekday Month Date" format (e.g., "Monday June 14")

	So when all is said and compiled your prompt would say something like:
	usernamehostnamedirectorySat Feb 10

	It's important to note here that whatever order you put your characters in is the order they will appear when the prompt appears. Likewise, if you want some space in bewteen the different companents, add a space. 
	EX:

	PS1="\u\d"
	usernameSat Feb 10

	PS1="\u \d"

	username Sat Feb 10


4.Understanding the brackets and numbers.

	You're probably wondering what all those brackets, numbers and other letters do. They allow us to add color to our prompt! 

	Let's continue with our current example:

	PS1="\u\h\[\e[32m\]\W\[\e[m\]\[\e[31m\]\d\[\e[m\]"

	We know what the first two characters mean: username and hostname. 

	Next we see this string of brackets, slashes and numbers then \W, let's break it down shall we?

	[=begin in a sequence of non-printing characters, which can be use to embed into the prompt

	]=end the sequence of non-printing characters

	[\e[32m\]\W\[\e[m\]

	1.\e[ :starts color scheme 
	2.32: the color code for green
	3. \e[m: stop color scheme 

	So in theis example when our working directory gets printed, it will be printed green.
	There are many color codes and commands to use when customizing your PS1, go look them up and play around!

5.Changing your PS1 permanently
	
	To permanently change your PS1 youmust modify your bashrc file. 
	To do this you must open it in a text editor. 

	vim / .bashrc

	Navigate till you find this block of code

	# uncomment for a colored prompt, if the terminal has the capability; turned
	# off by default to not distract the user: the focus in a terminal window
	# should be on the output of commands, not on the prompt
	#force_color_prompt=yes

	if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
	fi

	if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;36m\][\d \@]\[\033[1;33m\] \u:\w \[\e[37m\]\$ '
	else
    	PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
	fi

	Add your code to the 'PS1=' and add your code to after the debain part of your bashrc file. 

	Save your changes and restart your terminal. 

Have fun!

Useful Links:

1.[Linux Juggernaut](https://www.linuxnix.com/linuxunix-shell-ps1-prompt-explained-in-detail/)

2.[If you want something to generate the PS1 for you](http://ezprompt.net/)

3. [More on colors](https://unix.stackexchange.com/questions/124407/what-color-codes-can-i-use-in-my-ps1-prompt)

4. [Even more on colors](https://www.cyberciti.biz/faq/bash-shell-change-the-color-of-my-shell-prompt-under-linux-or-unix/)
