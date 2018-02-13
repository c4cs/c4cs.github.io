`OH++` Shells
==============

## Configuration
The default shell for most machines is `bash`, the "Bourne Again Shell". When
the terminal application starts up, it calls your system default shell. When
the shell starts up, it looks for some configuration files and runs them. One
of these configuration files is called `.bashrc`. Many shells (and other
programs) follow this pattern of putting a file with a leading period
in the home directory for configuration. The "rc" in `.bashrc` stands for
"run commands", which is exactly what it is designed for. Here, we will learn
about some useful commands to add to your `.*rc` file.


## Aliases
An alias is a simple mapping of one string to another. In the context of the
command line, this is used to shorten many common commands or sequences of
commands. Remember to add these to your `~/.bashrc` file.

The alias syntax is fairly simple. Here are a few examples.

```bash
# model
alias command='new-command'

# for clearing the terminal window
alias c='clear'

# for quickly editing your shell's config file
alias erc='vi ~/.bashrc'

# for searching your history with grep
alias hgrep="fc -El 0 | grep"
# Example: hgrep "alias" returns every command with the word "alias"
```

We can also use aliases in other contexts. `git` uses a `.gitconfig` file
located in your home directory. Go ahead and add this to your git
configuration.

```
[alias]
  st = "status"
```

Now, every isntance of `git st` will be repalced with `git status`! I encourage
you to play around with this.


## Custom Functions

Tired of writing `cd` and then immediately following it with `ls`? Why not
combine the two! Writing custom functions is pretty easy. Just place the
function in your `.*rc` file and you should have access to it everyone on the
command line.

```bash
function cs () {
  cd "$@" && ls
}
```

Now, cs will allow us to cd into a directory and list the contents immediately.
It's hard to make recommendations for large functions, as this will depend on
what you use your computer for most often, but a good example of a function is
this short journaling function I stole from Matt Terwilliger's dotfiles repo.

```bash
function journal {
    file="$HOME/journals/$(date +'%Y-%m-%d').md"

    # templating
    [[ -s "$file" ]] || echo "# $(date +'%A %B %e, %Y')\n\n" > $file

    $EDITOR $file
}
# Adding an alias, to really keep things tidy. = D
alias j='journal'
```

## Other Shells
There are other shells as well. It is imporant to note that shells are pretty
similar, and aren't going to dramatically change the way you work. If you're
okay with bash, then that's fine, but there are others out there, and they do
have some pretty neat features.  Here, I've listed a few shells and some
resources related to each one.

* `fish`
  - "The friendly shell"
  - [`fish` website](https://fishshell.com/)
  - Is not `POSIX` compatible (does not play nice with `sh` scripts).
  - Amazing default features, like great tab competion and a graphical, web
    based config.
* `zsh`
  - "Like bash, but different features"
  - [A slide show about `zsh` features](http://www.slideshare.net/jaguardesignstudio/why-zsh-is-cooler-than-your-shell-16194692)
  - Easy to switch from `bash` to `zsh`.
  - Interactive setup by running `compinstall`
* `bash`
  - "The comfortable default"

### Shell Extras: Packages and Plugins
For each shell, there is an online community of users sharing their
configurations and scripts. Some shells have a system for managing these
scripts and themes. For your shell of choice, check out the plugin managers
listed below.

* [`oh-my-fish`](https://github.com/oh-my-fish/oh-my-fish)
* [`oh-my-zsh`](http://ohmyz.sh/)
* [`bash-it`](https://github.com/Bash-it/bash-it)

## Changing your default shell
You may notice that even once you install another shell, `bash` will still
start up by default. On macOS or linux, you'll usually need to add your new
shell's path to the system's list of accepted "standard" shells, which is
`/etc/shells`. Then, you'll use the `chsh` command to change your shell! Here's
what that looks like.


```bash
# Get the path of our cool shell. Here, I'll be switching to fish.
[~] λ: which fish
/usr/local/bin/fish
[~] λ: cat /etc/shells
# List of acceptable shells for chpass(1).
# Ftpd will not allow users to connect who are not using
# one of these shells.

/bin/bash
/bin/csh
/bin/ksh
/bin/sh
/bin/tcsh
/bin/zsh
[~] λ: sudo -s # enabling sudo because /etc/shells requires root permission
Password:
[~] λ: echo "$(which fish)" >> /etc/shells
[~] λ: cat /etc/shells
# List of acceptable shells for chpass(1).
# Ftpd will not allow users to connect who are not using
# one of these shells.

/bin/bash
/bin/csh
/bin/ksh
/bin/sh
/bin/tcsh
/bin/zsh
/usr/local/bin/fish
[~] λ: chsh -s $(which fish)
Changing shell for root.
```

Upon restarting your terminal, you should be greeted by your new shell.

