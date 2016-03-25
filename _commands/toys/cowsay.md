---
---

Cowsay
--
`cowsay` generates an ASCII picture of a cow saying something provided by  the  user.


~~~ bash
$ cowsay Hi There
 __________ 
< Hi There >
 ---------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
~~~

<!--more-->



### Useful Options / Examples
There are many useful options for this intersting cowsay command.
The complete list is: cowsay  `[-e  eye_string]` `[-f cowfile]` `[-h]` `[-l]` `[-n]` `[-T tongue_string]` `[-W column]` `[-bdgpstwy]`

 * `-e` allows the user to customize the cow's eyes which are defaulted to "oo" as seen above.
 * `-T` allows the user to add a tongue string to the cow image. By default there is no tongue string.
 * `-W` allows the user to customize the number of character printed in the message before the message wraps around
 * `-[-bdgpstwy]` are all options to define different pre-made cows emotional states. For example, adding the `-g` flag will result in a greedy cow to print and `-s` will result in a stoned cow to print.

#### Example Command

#### `cowsay [-bdgpstwy] [user_input]`

~~~ bash
$ cowsay -s hi there
 __________ 
< hi there >
 ---------- 
        \   ^__^
         \  (**)\_______
            (__)\       )\/\
             U  ||----w |
                ||     ||
~~~

##### Break it down

 * There are several provided modes which change the appearance of the cow depending on its particular emotional/physical state
 * The user can set this state using these flags

#### Example Command

#### `cowsay [-f cowfile] [user_string]`

~~~ bash
$ cowsay -f tux hi there
 __________ 
< hi there >
 ---------- 
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/

~~~

##### Break it down
 * The `-f` flag allows for other ascii images to be printed
 * These images are pulled from .cow files, some of which come preinstalled and the full list can be found by typing:

#### Example Command

#### `cowsay [-l]`

~~~ bash
$ cowsay -l

Cow files in /usr/local/Cellar/cowsay/3.03/share/cows:
beavis.zen bong bud-frogs bunny cheese cower daemon default dragon
dragon-and-cow elephant elephant-in-snake eyes flaming-sheep ghostbusters
head-in hellokitty kiss kitty koala kosh luke-koala meow milk moofasa moose
mutilated ren satanic sheep skeleton small sodomized stegosaurus stimpy
supermilker surgery telebears three-eyes turkey turtle tux udder vader
vader-koala www
~~~

##### Break it Down
 * The `-l` flag lists all pre-made .cow files that are immediatly at the users disposal.

#### Example Command

#### `cowsay [-e eye_string] [-T tongue_string] [-W column]`

~~~ bash
$ cowsay -e ^^ -T U -W 10 Hi there computing for computer scientists, this stuff is really interesting!
 ___________ 
/ Hi there  \
| computing |
| for       |
| computer  |
| scientist |
| s, this   |
| stuff is  |
| really    |
| interesti |
\ ng!       /
 ----------- 
        \   ^__^
         \  (^^)\_______
            (__)\       )\/\
             U ||----w |
                ||     ||
~~~

##### Break it down
 * `-e` flag allows the user to customize the cow's eyes
 * `-T` allows the user to enter a string to be used as the Cow's tongue (the string must be two characters or less)
 * `-W` specifies the number of charcters to be printed in the cow's message before the characters wrap around. The defualt is 40 if none is specified
