---
---

tmux
--

`tmux` is a terminal multiplexer. It allows the user to access seperate terminal sessions inside a single terminal window. `tmux` is especially useful in remote access.

#### To get started
For Linux

```bash
$ sudo apt-get install tmux
```

For OSX

```
$ brew install tmux
```
Now you have installed tmux. 

To start tmux, simply type `$ tmux`. To quit, type `$ exit`.

#### Key binding
`tmux` can be controlled using a key combination as a prefix key, (which is ctrl+b by default), followd by a command. The following are the most frequently used commands.

```
%			split virtically into two panes
"			split horizontally into two panes
!			break the current pane out of the window
x			kill the current pane
c			create a new window
&			kill the current window
n			switch to the next window
p			switch to the previous window
f			promt a search in the current window
,			rename the current window
Up/Down		switch to the up/down pane
Left/Right	switch to the eft/right pane
```

####
