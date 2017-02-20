---
---

asciiview
-------

`asciiview` generates an ASCII image based on any png file provided by the user.

~~~ bash
$ asciiview filename.png
~~~

<!--more-->

### Install

~~~ bash
$ sudo apt-get install aview
~~~

### Controls
Once you run the command successfully, it will open a separate window to display the acsii image. There are several useful optoins to view, modify, and save the image.

*	If the image is out of the window range, you can move it by `a,w,d,x` or `A,W,D,X`.
*	If the image is too small/large, you can use `+/-` to zoom in/out.
*	Use `.` or `,` to increase or decrease contrast.
*	Use `>` or `<` to increase or decrease brightness.
*	Press `s` if you want to save the image. `asciiview` supports many formats (text, html, and etc.).
*	Press `q` to exit.

### Example
If you can't find a cow in the image, remove your glasses or move away from the screen!

~~~ bash
$ asciiview cow.png
                j#0000000!!400000!!!40Lad009!!400000!!400000001                 
                j#000000L.:../\ad00000000000w==:.!..:-j#0000001                 
                j#0000000,:::: 0000000000@99;=;;.:::-_000000001                 
                j#000!4aaaaaaad000000000t:;;;=;=;.,aaaaad!40001                 
                j#!\a000#0#0#0000000000A==;=;=;;==;d###000La!41                 
                j "400B!000000P\aaaaa!00As\aaaaa-;n#000P!000!                   
                j#00LJ__00000P_000##00,41d0####0#/#0000L_"a0001                 
                j#00'd1j0000010000'  01j 0P  j0001#0000& @ 4001                 
                j#0'd01j#0000LJ400LadP_0L"0aa#00!_000008 {;:401                 
                j#'d00Lj#000000La00Lad0000aa##La00000083_wv;.41                 
                jP?9000,4000000000000000000#00000000083'j#0#0"1                 
                j';;=400,*N#00000000!!!!!!!40000000#3O'j4000&('                 
                j.=;=;00W_"UN0000P\aW######La!000H837\j4#0008n                  
                j.=;=;4000m_"OHN'J#W' -WW' ?WW,*O37'j3m0000#!:                  
                j =;=;=9000Wm_"! HHQLaaWWa_H5%(="\j34*99999-:-                  
                j1!q:=;=;0000W!:.""%3%%%3%3%7~\_X3mW;::;;:::: 1                 
                j#-OHws;;00000Aw:::...+++'__X3XWW0006===::::._1                 
                j#L-O4N#0000000000ws::;:::*WW00000000s:::::-\01                 
                j#0L-33OH0000000000#0s;=;=;;4000000#H):::-.\#01                 
                j#00L/33O3UHN000000000s;;=;;d000#H3O3{::--a#001                 
                j#0000a"3O3O3O3HHHHN000AwaxHRR3O33O3On:.\d00001                 
                j#000000a/""...::..-333OO3O"'..::...""_d0000001                 
                j#0000000!.::: .::::.-O3O7'.:::: -::: 400000001                 
                j#000000P.:::  ::-:.:.=O3':::::-:  ::: 00000001                 
                j#000000L -:.  :::-:- _00,-.::.::  ::  00000001
~~~

### Additional Command
`asciiview` is based on `aview`, which only show files in PNM format. You can explore more by typing `aview --help`. Enjoy & have fun!
