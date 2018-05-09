---
---

vi
----


`vi` is a text editor for programmers, designed to facilitate optimal efficiency
when writing code.

To open `vi`, simply type the following:

~~~ bash
$ vi [filename]
~~~


<!--more-->

This will open a file with the name specified. If there is an
existing file with that name, it will open that file, however if no file is
found with that name, a new, empty one will be created.

Since its creation, the developers have also released `vim (vi improved)`, an
updated version with more features, such as support for more programming
languages, compatibility with more OS's, and features like multilevel undo/redo.
On some Linux distributions, the `vi` executable provided is actually vim.
Despite this, some programmers still prefer `vi` over vim for its simplicity
and ease of access.

---

Table of Contents
================================================================================
- [Why vim?](#why-vim)
- [Introduction to Modal Editing](#introduction-to-modal-editing)
  - [Insert Mode](#insert-mode)
  - [Normal Mode](#normal-mode)
  - [Visual Mode](#visual-mode)
- [The `.vimrc`](#the-vimrc)
  - [Version Control and the `.vimrc`](#version-control-and-the-vimrc)
  - [An Aside: `.vimrc` Bloat](#an-aside-vimrc-bloat)
- [vim Plugins](#vim-plugins)
  - [Plugin Managers](#plugin-managers)
- [Editorial Notes](#editorial-notes)
  - [vim vs. neovim](#vim-vs-neovim)
  - [Using vim vs. Using an IDE](#using-vim-vs-using-an-ide)
- [Things to Learn](#things-to-learn)
- [Plugin Recommendations](#plugin-recommendations)
  - [Essentials](#essentials)
  - [File Navigation](#file-navigation)
  - ["IDE-Like"](#ide-like)
  - [Snippets](#snippets)
  - [Miscellany](#miscellany)
- [External Links](#external-links)

---

Why vim?
================================================================================

Because vim is [Difficult, But Awesome.](http://tvtropes.org/pmwiki/pmwiki.php/Main/DifficultButAwesome)

[vim is infamous among programmers for its steep learning curve.](https://www.reddit.com/r/ProgrammerHumor/comments/33a6p7/)
Because vim was designed to be used in a command-line interface, it's entirely
controlled with keyboard shortcuts. Most of the "standard" keyboard shortcuts
that we're familiar with (e.g. `CTRL-a` for "select all," `CTRL-c` for "copy")
either won't work in vim, or they won't do what you'd expect without some
prior setup.

That reliance on keyboard commands is a blessing and a curse. On one hand, it
makes vim difficult to learn. On the other hand, because you can control vim
without ever removing your hands from the keyboard, skilled vim users can edit
code [very, _very_ quickly.](https://youtu.be/o6omymj1JZI)

### Using vim, you can...

**...record macros to make writing test cases less repetitive...**

<!-- Use `.img-responsive` class from bootstrap.css for adaptive resizing.   -->
<!-- Link: https://www.w3schools.com/bootstrap/bootstrap_ref_all_classes.asp -->

<img class="img-responsive" src="../static/commands/img/test_cases.gif" alt="test cases">

[Link](http://vim.wikia.com/wiki/Macros)

**...select text and toggle between uppercase and lowercase...**

<img class="img-responsive" src="../static/commands/img/toggle_text.gif" alt="toggle-case">

[Link](http://vim.wikia.com/wiki/Switching_case_of_characters)

**...and edit text in blocks, not just line-by-line or character-by-character.**

<img class="img-responsive" src="../static/commands/img/visual_block.gif" alt="visual-block-copypaste">

[Link](http://vim.wikia.com/wiki/VimTip386)

And more!

### Here are some basic commands to get you started:

- `esc` - enter command mode
- `h`, `j`, `k`, `l` - move cursor left, up, down, and right respectively.
- `i` - enter insert mode
- `s` -Delete character and enter insert mode
- `a` - insert after character
- `v + [direction]` - select text with cursor
- `:w` - write/save file
- `:q` - quit vim
- `dw` delete word
- `d$` delete to the end of the line
- `dd` delete entire line
- `y` - yank/copy selected text
- `p` - put/paste yanked text
- `r + [character]` - replace character at cursor with specified character
- `u` - undo action
- `ce` - replace text until end of word
- `/ + [search phrase]` - search file for specified phrase

For a more complete tutorial, run:

~~~~ bash
$ vimtutor
~~~~
in a Linux terminal, or visit [this link.](http://www.openvim.com/)

---

Introduction to Modal Editing
================================================================================
`vimtutor` covers the basics of using vim better than we can here, but it
doesn't spend much time explaining one of vim's less intuitive features: modal
editing.

Unlike a word processor like Google Docs, or an IDE like Xcode, vim's behavior
(i.e. what will happen when you press a key) changes based on its current
**mode**. The modes you'll use most frequently in vim are **normal** mode,
**insert** mode, and **visual** mode,

Insert Mode
--------------------------------------------------------------------------------
We'll start with insert mode because it's the easiest to understand.

<img class="img-responsive" src="../static/commands/img/insert_mode.gif" alt="insert-mode">

Insert mode is the mode that lets you insert text into a file. Using insert mode
is similar to editing text files in nano. You can move your cursor using the
arrow keys, `Home`, `End`, `PgUp`, `PgDn`, and most of the other navigation keys
you're used to using. `Backspace` and `Del` do what you'd expect, and you add
text just by typing.

Shortcuts like `CTRL-LeftArrow` and `CTRL-RightArrow` (for moving the cursor one
word left or one word right, respectively) may or may not work, depending on
your terminal or your current shell environment. `CTRL-Backspace` (for deleting
the entire last word) almost certainly won't work. Thankfully, the
[equivalent bash shortcuts](http://teohm.com/blog/shortcuts-to-move-faster-in-bash-command-line/) will!

Here's a snippet of some bash shortcuts that you may want to use:

|  Ordinary         | Function                  | bash Equivalent   |
| ----------------- | ------------------------- | ----------------- |
| `CTRL-Backspace`  | Deletes previous word.    | `CTRL-w`          |
| `CTRL-LeftArrow`  | Move one word back.       | `META-b`          |
| `CTRL-RightArrow` | Move one word forward     | `META-f`          |
| `Home`            | Move to start of line.    | `CTRL-a`          |
| `End`             | Move to end of line.      | `CTRL-e`          |


(Note: the `META` key is usually the `ALT` key. You may have to do some
finagling to get it working on your machine.)

(Also, most of the shortcuts above aren't that useful in insert mode, with the sole
exception of `CTRL-w` for deleting a word. We'll explain why when we cover
normal mode.)

There are many ways to **enter insert mode**:

- `i`:  Enters insert mode at the cursor's current position.
- `a`:  Enters insert mode, moving the cursor to the position _after_ the
  current character.
- `I`\*:  Enters insert mode at the start of the current line.
- `A`:  Enters insert mode at the end of the current line.
- `s`:  _Substitute._ Delete the currently selected text and enter insert mode.
- `r<CHAR>`:  _Replace_ the currently selected character(s) with `<CHAR>`.\*\*

(\* Literally `SHIFT-i`. Typing an `i` with `CAPS LOCK` turned on will also
work!)

(\*\* Replace is a bit of a special case: it doesn't actually enter insert mode,
and it's a special command in and of itself. It replaces every character that
you have highlighted with the next character you type and immediately returns
you to normal mode.)

Normal Mode
--------------------------------------------------------------------------------

Normal mode, as its name suggests, is the mode that you'll normally be using.
You start in normal mode when you launch vim, and you return to normal mode
when you exit another.

This is counterintuitive for many people because they're used to editors
that always "stay in insert mode" (e.g. nano, gedit, Microsoft Word, LibreOffice
Writer, etc.) Many novice vim users spend _all_ of their time in insert mode,
only entering normal mode to save their work and to close vim.

Editing exclusively in insert mode defeats the entire purpose of using vim! By
itself, insert mode is nothing but a less capable clone of nano. Insert mode
exists just because, were it omitted, vim wouldn't be a text editor. The bulk of
vim's most useful features lie in normal mode and in visual mode.

Normal mode's featureset can be roughly divided into the following categories:
**basic editor essentials**, **navigation**, and **doing weird stuff**,

### Basic Editor Essentials

Things like [saving files](http://vim.wikia.com/wiki/Saving_a_file),
[opening new files, opening new tabs, splitting the
current window (i.e. opening multiple files side-by-side)](https://askubuntu.com/questions/537935/),
and [closing vim](https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/)
are done from within normal mode.

You can almost always **return to normal mode** by pressing `<ESC>`.

### Navigation

You'll recall that we recommend _not_ using the `META-b` and `META-f` shortcuts
to skip back/forward one word from within insert mode. That's because one of the
primary purposes of normal mode is fast file navigation.

Normal mode has a number of keybindings that make navigating files easier. We
provide a non-exhaustive list of them below:

#### Basic Navigation Keys

- `hjkl`:   Respectively, move (left/down a line/up a line/right).
- `CTRL-u`: Go up half a page.
- `CTRL-b`: Go up a full page.
- `CTRL-d`: Go down half a page.
- `CTRL-f`: Go down a full page.
- `gg`\*:   Go to the start of the file.
- `G`:      Go to the end of the file.

(\* no re)

#### Navigation Within a Line

- `w`:  Move the cursor to the start of the next word.
- `W`:  Move the cursor to the start of the next [WORD](https://stackoverflow.com/questions/22931032/).
- `b`:  Move the cursor to the start of the current word.
- `B`:  Move the cursor to the start of the current WORD.
- `e`:  Move the cursor to the end of the current word.
- `0`:  Move the cursor to the start of the current line.
- `^`:  Move the cursor to the first non-whitespace character in the
  current line.
- `$`:  Move the cursor to the end of the current line.

#### Search Within a Line

- `f<CHAR>`:    Search for the next instance of `<CHAR>` in the current line.
- `F<CHAR>`:    Search _backwards_ in the current line for the nearest instance
  of `<CHAR>`.
- `;` (after an `f` search): Jump to the next instance of `<CHAR>` in the
  current line.
- `,` (after an `f` search): Jump backwards to the nearest instance of `<CHAR>`
  in the current line.
- `;` (after an `F` search): Jump backwards to the nearest instance of `<CHAR>`
  in the current line.
- `,` (after an `F` search): Jump forwards to the nearest instance of `<CHAR>`
  in the current line.

#### Demonstrative Screencast
<img class="img-responsive" src="../static/commands/img/normal_nav.gif" alt="normal-nav">

### Doing Weird Stuff

- `u`:      Undo the last action.
- `CTRL-r`: Redo the last undone action.
- `<<`:   Decrease the indentation of the current line
- `>>`:     Increase the indentation of the current line
- `d<MOTION>`:  Cut the characters the cursor would cross over if you were to
  perform `<MOTION>`.
- `dd`:     Cut the current line.
- `=<MOTION>`: Fix the indentation of the lines the cursor would cross over if
  you were to perform `<MOTION>`.
- `zz`:     Center the screen on the cursor.
- `zt`:     Move the screen so that the current line is at the top.
- `zb`:     Move the screen so that the current line is at the bottom.

Visual Mode
--------------------------------------------------------------------------------

Modern text editors, web browsers, PDF viewers, etc. allow you to select ranges
of text by clicking and dragging with the mouse. In vim, you would do the same
using visual mode.

`:help` gives the following description of visual mode:

    Visual mode is a flexible and easy way to select a piece of text for an
    operator.  It is the only way to select a block of text.

[Operators](http://vimdoc.sourceforge.net/htmldoc/motion.html) allow you to
edit text in bulk. Cutting, copying ("yanking"), and pasting ("putting") in vim
requires the use of operators.

### Cut, Copy, and Paste

Basic copy-pasting makes use of the unnamed register (`""`). This register is
like a bucket filled with the text most recently grabbed by any of the
following:

- Text deleted using the `c`, `d`, or `x` operators,
- Text replaced using the `s` operator.
- Text "yanked" using the `y` operator.

To copy and paste text, highlight some text in visual mode, then yank with `y`.
Move the cursor where you want, then paste it there using `p`. (You can insert
the pasted text at the position before the cursor with `P`.)

To cut text, highlight text in visual mode, delete it with `c`, `d`, or `x` (or
`s`), then paste using the same process described above.

The screencasts in the subsections below demonstrate how this works.

### The Different Visual Modes

#### `-- VISUAL --`

The basic visual selection mode. Analogous to highlighting text in an "ordinary"
text editor by holding down the left mouse button and dragging the cursor over
text.

To use, move the cursor to the start of the text, then press `v`. Move the
cursor to the end of the text that you want to select. Note that you can --
and generally should -- use the "special" normal mode navigation keys (`w`, `$`,
etc.) to select the text range you want. Moving the cursor backwards
(`b`, `k`, etc.) will also work.

<img class="img-responsive" src="../static/commands/img/visual_normal.gif" alt="visual-normal">

#### `-- VISUAL LINE --`

Used for selecting entire lines of text at a time. The mode you'll probably use
most frequently, at least when programming. To use, move the cursor to the first
line you want to select, then press `V`.

<img class="img-responsive" src="../static/commands/img/visual_line.gif" alt="visual-line">

#### `-- VISUAL BLOCK --`

Used for select rectangular blocks of text. Though it can be used for cutting
and pasting, it's often used to perform precise edits on multiple consecutive
lines at a time.

Visual block mode has special behavior when used in conjunction with insert
mode. Selecting a visual block and substituting it by pressing `s` allows you
to replace each line in your selected block with the text you type. Selecting a
visual block and prepending text with `I` will prepend text onto each line, while
`A` will append text onto each line.

This mode is one of the most compelling arguments to indent with spaces, or at
least to indent with tabs and use spaces for alignment.

To use, move the cursor to a corner of the text you want to select, then press
`CTRL-v`.

<img class="img-responsive" src="../static/commands/img/visual_block.gif" alt="visual-block">

---

The `.vimrc`
================================================================================

Unlike more basic text editors like gedit, vim's interface and functionality
are both _extremely_ configurable. vim has its own scripting language
(appropriately named
[vimscript](http://learnvimscriptthehardway.stevelosh.com/)) that lets you
customize vim in a number of ways, either by editing your `.vimrc`
configuration file, or by writing plugins.

The **`.vimrc`** is a [dotfile](https://askubuntu.com/questions/94780/) that
lives in your home directory (e.g. `/home/your_name/.vimrc`, or `~/.vimrc` for
short). It's written entirely in vimscript, and vim will
[source](http://vimdoc.sourceforge.net/htmldoc/repeat.html#:source) it (i.e.
execute the contents of the file, line-by-line) whenever you launch vim.

The `.vimrc` is a config file, first and foremost. It's like a text-only
version of the `Edit > Preferences` menu in a GUI text editor. You can use it to
change settings (e.g. whether or not to show line numbers, what colorscheme to
use) or change vim's default keymappings to suit your needs. Changing these
settings is just a matter of editing your `.vimrc` in a text editor, saving, and
then opening a new instance of vim.

A vim user's `.vimrc` is a very personal thing. It's like working on a car that
you drive every day. Putting in that added effort is a non-negligible amount of
work, but once it's done, the car runs _exactly_ how you'd like.

(Unlike a car, however, once you customize vim enough, your vim
installation will be [completely unusable by anybody except yourself.](https://xkcd.com/1806/))

The settings in Tim Pope's [sensible.vim](https://github.com/tpope/vim-sensible)
are a good starting point for a personal `.vimrc`. You can find many online
quick-start guides offering tips for vim beginners, as well.

Version Control and the `.vimrc`
--------------------------------------------------------------------------------

Because the `.vimrc` is literally just a text file, it makes your vim
installation very portable. Oftentimes, vim users will manage their `.vimrc`
using a version control system such as git, storing it "in the cloud" on sites
like GitHub or BitBucket. If a vim-using Michigan student doesn't have access
to their laptop and wants to edit a text file on a CAEN computer, installing
their personal vim configuration is just a matter of:

    git clone https://billy_magic@bitbucket.org/billy_magic/vimrc.git ~/vim_config
    ln -s ~/vim_config/.vimrc ~/.vimrc

What this command does is:

    git clone https://billy_magic@bitbucket.org/billy_magic/vimrc.git ~/vim_config
        ^ clone a local copy of a git repository...
                      ^ ...from billy_magic's personal BitBucket account...
                                                                      ^ ...and store
                                                                      it in a folder
                                                                      named vim_config
                                                                      in his home directory.
    ln -s ~/vim_config/.vimrc ~/.vimrc
    ^ Then making a symlink...
          ^ ...pointing to the .vimrc in that folder...
                              ^ ...and putting that symlink in the default location
                              for a .vimrc. Now, when vim tries to read ~/.vimrc, Linux
                              will redirect it to ~/vim_config/.vimrc

This student will have immediate access to the exact same keymappings and
settings that they normally use in vim. Because their `git clone`d `.vimrc`
exists in their home directory on CAEN, those settings will be loaded
automatically whenever they log into a CAEN computer.

The beautiful thing about doing this is that, if Billy Magic modifies his
`.vimrc` on his personal computer and `git push`es his changes, all he has to do
to copy those same changes to CAEN is `cd ~/vim_config && git pull`.

This is especially handy if you're prone to accidentally nuking the bajeezus out
of your Linux installations. You still have to reinstall everything from
scratch, but reinstalling vim and restoring your settings will take minutes at
most.

An Aside: `.vimrc` Bloat
--------------------------------------------------------------------------------

Placing your entire vim configuration in the file named `.vimrc` is a lot like
writing an entire EECS project in `main()`: it's perfectly doable with simple
projects for classes like ENGR 101 and EECS 183, but things will get ugly _fast_
if you attempt the same in EECS 281. Similarly, maintaining a `.vimrc` is easy
when you've just started using vim, but it'll grow more difficult as that
`.vimrc` grows in size.

Remember that vimscript is a Turing complete programming language in and of
itself. You will, at times, need to debug your `.vimrc`. This is much easier if
you separate your `.vimrc` into smaller `.vim` files that you `source` in your
`.vimrc`.

[You can find more information on how to do that here.](https://www.gregjs.com/vim/2016/do-yourself-a-favor-and-modularize-your-vimrc-init-vim/)

---

vim Plugins
================================================================================

Many of the niceties that you're used to having in a more modern text editor
aren't baked into vim by default. In theory, you could implement these
yourself in vimscript, but writing a time- and memory-efficient implementation
of tab autocompletion in vimscript is far more effort than it's worth.

Thankfully, you don't need to. vim has a vibrant community of plugin authors
that have already done much of the heavy lifting. Of these, [Tim Pope](https://github.com/tpope)
and [Martin Grenfell (a.k.a. scrooloose)](https://github.com/scrooloose)
are some of the most prolific.

Plugin Managers
--------------------------------------------------------------------------------

Because vimscript is an interpreted language, having access to a vimscript
executable is the same as having the original vimscript source code. This allows
developers of vim plugins to distribute their plugins through GitHub. Installing
these plugins is a matter of `git clone`ing the plugins into the appropriate
directories on your machine.

Although vim does have built-in support for plugins, that support is fairly
rudimentary. You'll want to use a plugin manager to install and update plugins,
especially as the complexity of your vim installation grows.

Some of the most popular plugin managers are:

### pathogen.vim
Tim Pope's pathogen.vim is notable in that it [effectively created the standard layout](http://learnvimscriptthehardway.stevelosh.com/chapters/43.html)
of a vim plugin. It is actually considered bad programming practice among
vim developers to write a plugin that _doesn't_ use a pathogen-compatible
directory structure.

pathogen.vim takes its name from the fact that it modifies vim's
`runtimepath`. Without going into too much detail, that means that vim will
`source` the vimscript files of plugins provided that the plugin:

1. Adheres to the pathogen-standardized directory structure
2. Was cloned into `~/.vim/bundle`

In simpler terms, once you've installed pathogen.vim (both the plugin itself,
and the lines you need to add to your `.vimrc`), you can install plugins by
doing this:

    cd ~/.vim/bundle
    git clone https://github.com/plugin_author/the_plugin_you_want_to_install.git

More detailed instructions can be found [on pathogen's GitHub page.](https://github.com/tpope/vim-pathogen)

### Vundle
You can think of Vundle as being a convenient wrapper around the functionality
of pathogen.vim. They both do essentially the same thing, but pathogen.vim is a bit
leaner while Vundle has a few features that simplify managing lots of plugins at
the same time.

Manually `git clone`ing the GitHub repositories of the plugins you want directly
into your `~/.vim/bundle` folder can be tedious; automating the process of doing
that, generating helptags (so that `:help <PLUGIN_NAME>` will actually do
something), and `git pull`ing when you want to update your plugins is doable,
but it's non-trivial work that requires a bit of shell scripting.

To use Vundle, you add some lines to your `.vimrc`, list the plugins you want to
install between them, and run the vim command `:PluginInstall`. To update your
plugins, you run `:PluginUpdate`. To remove the cloned repositories of plugins
that you no longer list in your `.vimrc`, you run `:PluginClean`.

More detailed instructions can be found [on Vundle's GitHub page.](https://github.com/VundleVim/Vundle.vim)

### vim-plug
vim-plug is nearly identical to Vundle in real world use, including its
command syntax. `:PlugInstall` installs plugins, `:PlugUpgrade` updates them,
and `:PlugClean` uninstalls plugins that you no longer list in your `.vimrc`.

Ironically, despite claiming to be a minimalist plugin manager, vim-plug
actually has more features than Vundle. **For this reason, we recommend using
vim-plug** over Vundle. Some of vim-plug's added features are listed below.

Full documentation and installation instructions can be found [on vim-plug's GitHub page.](https://github.com/junegunn/vim-plug)

#### Post-Update Hooks
Post-update hooks are terminal commands that vim-plug will run automatically
after a plugin has been installed or updated. This is useful when working with
plugins that require additional installation steps beyond cloning from GitHub.
[fuzzyfind,](https://github.com/junegunn/fzf) for instance, has to be
`./install`ed after being cloned.

    " (Example taken from vim-plug README, with added comments.)
    " PlugInstall and PlugUpdate will clone fzf into ~/.fzf
    " and run its install script.
    Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }

#### Multithreaded Plugin Installation
Rather than installing or updating each of your plugins one-after-the-other,
vim-plug can install/update several plugins simultaneously.
[vim-plug's developer demonstrates this here.](https://raw.githubusercontent.com/junegunn/i/master/vim-plug/40-in-4.gif)

Note that you aren't limited by the number of logical cores on your computer.
Even if your laptop has a quad-core CPU, not only can you still execute the
command `:PlugUpdate 9001` without errors, it will also be noticeably faster
than executing `:PlugUpdate 4`. Take EECS 482 if you'd like to understand why.

#### Lazy-Loading
Ordinarily, vim will load all your plugins on startup. If you have a large
`.vimrc` with many plugins, this might make vim's startup process frustratingly
slow. Instead of loading plugins on startup, you can **lazy-load** a plugin
only when you actually need to use it, after which it will remain loaded until
you close vim.

    " (Example adapted from vim-plug README.)
    " Lazy-load NERDTree only when the user executes `:NERDTreeToggle`.
    Plug 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle' }
    " Lazy-load vim-easytags only when editing a C++ file.
    Plug 'xolox/vim-easytags', { 'for': 'cpp' }

---

Editorial Notes
================================================================================

Some editorial comments that don't quite fit into any other section.

vim vs. neovim
--------------------------------------------------------------------------------

vim is an _old_ piece of software, and it's largely maintained by one person,
[Bram Moolenaar](https://en.wikipedia.org/wiki/Bram_Moolenaar). It contains a
great deal of legacy code for decades-old computer systems, and the fact that it
only has one maintainer slows the speed of its development.

In 2014, a few programmers decided to make their own fork of vim to try and
fix these issues. Enter [neovim](https://github.com/neovim/neovim/wiki/Introduction).
neovim is to vim as Linux Mint is to Ubuntu: it's a different flavor of
the same basic thing. On top of vim's featureset, neovim offers:

- A "remote plugins" API that allows developers to write plugins in languages
  other than vimscript (usually, Python). These tend to be faster and more
  capable than plugins written in vimscript.
- Nicer default settings to reduce the time you need to spend fiddling with the
  `.vimrc` right after installation. For instance, neovim enables mouse support
  by default.
- Native support for multithreading ("asynchronous jobs"). Newer versions of vim
  do support this, but they didn't when neovim was first released. In the past,
  vim and its plugins would run entirely on a single thread; this meant that
  resource-hungry plugins (like autocompletion plugins, syntax checkers, ctags
  generators, and so on) would block the code handling vim's user interface,
  effectively freezing it until that plugin finished what it was doing.
- A terminal emulator. Yes, you can run an instance of neovim inside neovim.

neovim's killer app is probably [lldb.nvim](https://youtu.be/rd654OxlmQs),
an integrated graphical debugger similar to what you can use in an IDE. Similar
plugins are available for vim, however, notably [vim-lldb](https://github.com/gilligan/vim-lldb),
from which lldb.nvim was forked.

vim has the advantage of being preinstalled on most modern Linux machines,
including CAEN. Sticking with standard vim means that you can carry your vim
installation with you to practically any Linux machine you ever need to use.
neovim, on the other hand, is (arguably) easier to set up for a first-timer,
and supports a broader range of plugins, many of which aren't compatible with
vim proper. Even so, it's still largely cross-compatible with vim: switching
to vim on a machine that doesn't have neovim is usually just a matter of
losing one or two plugins that you might have liked using.

Whether to use vim or neovim is mostly a matter of personal choice. Use
whichever is most comfortable for you!


Using vim vs. Using an IDE
--------------------------------------------------------------------------------

A "vanilla" installation of vim is like a supercharged version of a standard
text editor, but it doesn't have many of the niceties that would make it useful
for a programmer. It doesn't include, for instance:

- An automatic drop-down menu for text autocompletion
- Code linting/syntax checking
- A graphical debugger
- A (good) file browser

And so on. For these reasons, many programmers will recommend using vim for
small, repetitive tasks -- things that can be done quickly and easily with vim's
robust text editing tools -- while performing the actual "meat" of development and
debugging in an IDE like Visual Studio or Xcode.

**If all you need is a working IDE, you're probably better off using a
purpose-built IDE.** You won't necessarily have access to the most awesome parts
of vim (e.g.  macros, "visual block" text selection, etc.), but the time that
costs you is easily outweighed by the time you'd save using an IDE's graphical
debugger and syntax checkers. With stock vim, your only real way to check for
syntax errors is to `make` your code and read through the errors, and your only
debugging tools are those that you can run from the command line in another
terminal. Command line debuggers like GDB and LLDB are very capable, but for
small tasks like setting breakpoints and inspecting variable values, you're
better off with an IDE.

But, **if you're willing to put in the time, you can make vim work like an IDE.**
You can accomplish this with the use of plugins.

Installing and configuring these plugins is a bit of a pain, unfortunately. You
can find a good list of plugins that provide IDE-like functionality
[here,](http://vim.wikia.com/wiki/Use_Vim_like_an_IDE) and in this page's list
of plugin recommendations.


---

Things to Learn
================================================================================

Some neat features that vim offers without needing to install plugins. (There's
some overlap between the information given here and some of the sections
above, but these should go into more detail.)

- [Mapping Keys in Vim](http://vim.wikia.com/wiki/Mapping_keys_in_Vim_-_Tutorial_(Part_1))
  - Changing keymappings is one of the simplest and most important parts of
    configuring your vim installation.
  - Might we recommend `inoremap jk <ESC>` and `vnoremap jk <ESC>`? That lets you
    exit insert mode and visual mode by hitting `j` and then `k` in quick
    succession. It's faster than hitting `<ESC>`, you don't have to move your
    left hand, and it lets you finish a text insertion or text selection with
    your fingers already on the home row.
- [HJKL, WB, E: Real Vim Users Don't Use Arrow Keys](http://vim.wikia.com/wiki/Moving_around)
  - `hjkl`, the basic navigation keys, are accessible without moving your hands
  from the home row. `w`, `b`, and `e` make it much less annoying to navigate
  within a line.
- [`count`: Repeat the Next Command `n` Times](http://vimdoc.sourceforge.net/htmldoc/intro.html#count)
  - Relatively self-explanatory. If `j` in normal mode moves you down by one
  line, `10j` moves you down ten lines. Pressing `i` in normal mode, then
  typing `harbaugh` and hitting `<ESC>` inserts the text `harbaugh` into your
  file. Pressing `10i` in normal mode and doing the same inserts _ten_
  `harbaugh`s into your file. And so on.
  - If only there was a way to see how far away a given line was from your
  current position? That would make jumping between blocks of code much
  faster...
- [Rapid File Navigation with Relative Line Numbering](https://jeffkreeftmeijer.com/vim-number/)
  - Jump around your text files like a jackrabbit that's been fed coffee
  grounds. _Nothing_ but coffee grounds, _till the end of its days._
- [Text Searching](http://vim.wikia.com/wiki/Searching)
  - Find something in the current file.
- [Search Patterns (a.k.a. Regular Expressions)](http://vim.wikia.com/wiki/VimTip188)
  - What if you don't want to search for the specific string `"12345 Arbor
  St."`, but instead want to search for all address-like strings in the
  current file?
- [Search and Replace](http://vim.wikia.com/wiki/Search_and_replace)
  - Like find and replace, but much more powerful.
  - Supports standard search and replace (i.e. find this exact string, replace
  it with this exact string), but also regular expressions ("regex"), ranges
  (i.e. replace between this line and this line) as well as command-line-esque
  "flags" for special behavior.
- [Mr. Worldwide: The `g`lobal Command](http://vim.wikia.com/wiki/Power_of_g)
  - Let's say you have a Linux log file that's tens of thousands of lines long,
  and you want to delete every line that doesn't contain the string
  `"NetworkManager"`. You can do this with a single vim command.
- [Recording Macros and Macro Playback](http://vim.wikia.com/wiki/Macros)
  - Record a series of keystrokes that you can play back by hitting `@` followed
  by a letter. For when you need to repeat a short, repetitive, complicated
  task that would be hard to automate programmatically.
  - These macros pair nicely with the special navigation keys given above (`w`,
  `e`, `b`, etc.), since they're more "intelligent." Recording basic
  navigational movements (`hjkl`) is akin to writing a program with hardcoded
  magic numbers.
- [Visual Selection](http://vim.wikia.com/wiki/VimTip386)
  - Highlight text without using the mouse. Highlight character-by-character or
  line-by-line. Highlight rectangular boxes of text.
  - Pairs very nicely with vim's special navigation keys, especially when you
  couple them with `count`.
- [Toggle Case](http://vim.wikia.com/wiki/Switching_case_of_characters)
  - That thing you've probably wanted to be able to do in text editors for a
  while.
- [Copy-Pasting: Yanking and Registers](http://vim.wikia.com/wiki/Copy,_cut_and_paste)
  - Copy-pasting to/from the system clipboard, if that functionality is enabled
  on your machine.
  - Having multiple places into which you can copy-paste. Handy, in some
  situations.
  - Note that enabling clipboard support requires some additional setup.
    - For standard vim, try `sudo apt remove vim && sudo apt install vim-gtk`.
    - For both standard vim and neovim, try `sudo apt install xclip`.
- [Paste Mode: When the `+` Register Doesn't Work](https://stackoverflow.com/questions/2514445/)
  - There are some places where you don't have access to the system clipboard
  (e.g. Windows Subsystem for Linux, while SSHing into CAEN).
  - This gives you the ability to paste in those situations, though you can't copy.
- [Buffers](http://vim.wikia.com/wiki/Vim_buffer_FAQ)
  - Any "thing" into which a vim user can enter text is a buffer.
  - More of a minor technicality than a major concept, but helpful when trying
    to understand helpdocs or autocommands.
- [Split Buffers](http://vimcasts.org/episodes/working-with-windows/)
  - View multiple files side-by-side, or open multiple views of the same file at
  different positions.
  - If you use neovim, you can open a terminal side-by-side with a text file
  and copy-paste from one into the other.
- [Folding](http://vim.wikia.com/wiki/Folding)
  - Collapse a selected text range, hiding it from view. Open it again if you're
  interested in what's there, hide it again if it's getting in the way.
- [The `vimdiff` Command](http://vimcasts.org/episodes/comparing-buffers-with-vimdiff/)
  - Open two files side-by-side in a vertical split. Automatically fold sections
  of the files that are identical. Highlight the lines that are different.
  - `vimdiff` is actually just an alias for `vim -d`. If you use neovim, you can
  launch a `vimdiff` inside neovim using `nvim -d`.
- [Tabs in Vim](http://vim.wikia.com/wiki/Using_tab_pages)
  - For when you start working on those large coding projects.
- [Syntax Highlighting and Highlight Groups](https://jordanelver.co.uk/blog/2015/05/27/working-with-vim-colorschemes/)
  - With the appropriate configuration, vim will apply syntax highlighting to
    the files that you open. It'll underline hyperlinks and color them light
    blue, color code comments in a faded teal, and so on.
  - This behavior is fully configurable through **highlight groups.**
  - By tweaking highlight groups, you can change the font color that vim uses when
    rendering literal strings, comments, and reserved words.
- [CursorLine and CursorColumn](http://vim.wikia.com/wiki/Highlight_current_line)
  - Make your cursor more visible. Underline the current line; highlight the
    current column. Makes it a bit easier to keep text space-aligned.
  - The appearance of the cursorline and cursorcolumn can be customized using
    their highlight groups (`:help hl-CursorLine`, `:help hl-CursorColumn`).
- [The Leader Key](http://vim.wikia.com/wiki/Mapping_keys_in_Vim_-_Tutorial_(Part_3)#Map_leader)
  - You will rarely bind mappings that use only one key, mainly because these
    bindings are highly likely to override vim's default keymappings.
  - vim users typically trigger their keymappings with key _sequences._
    However, these sequences may feel weirdly arbitrary, or be hard to remember.
  - To work around this, vim users will bind a `<Leader>` key that they will use
    as a "prefix" in many of their keymappings.
  - As an example, `vnoremap <Leader>s :sort<cr>` (where we `let mapleader=","`
    in our `.vimrc`) makes it possible to alphabetize lines of text by
    highlighting them in visual line mode, then hitting the comma key and `s` in
    quick succession.
  - If we decide that we want to use a different leader key in the future, we
    just `let mapleader=` something else.
  - **We recommend that you `let mapleader="\Space"`.**  Using the comma key as a
    leader is fairly common, but that shadows the "search backwards in line"
    function that the comma key normally provides.  Unlike the comma key,
    [the spacebar](https://superuser.com/questions/693528/) is easily accessible
    and otherwise useless.
- [Swapfiles](http://vimdoc.sourceforge.net/htmldoc/recover.html)
  - Similar to how Microsoft Word will store unsaved changes in backup files (in
    case you lose power before saving, etc.), vim will store unsaved changes in
    swapfiles.
  - You'll likely discover this when you first close a terminal window with an
    active vim instance. When you try to reopen the file you were editing, vim
    will notice the swapfile and throw up its version of Word's "Document
    Recovery" dialog.
  - If you find this annoying, then consider [relocating your swapfiles](https://github.com/tpope/vim-obsession/issues/18#issuecomment-69852130)
- [Autocommands](http://learnvimscriptthehardway.stevelosh.com/chapters/12.html)
  - Automatically run commands when certain events (e.g. loading files with
    a certain extension, moving the cursor into a different buffer) occur.
- [Automatically Reload Files That Were Modified Outside of Vim](https://unix.stackexchange.com/a/383044)
  - vim instances launched in a terminal usually don't support this by default,
    though they _really_ should.
- [Folding](http://vim.wikia.com/wiki/Folding)
  - Collapse portions of a file that you don't want to look at. Expand them when
    you do.
- [listchars: Professional Whitespace Pedantry](http://vimcasts.org/episodes/show-invisibles/)
  - Make vim show you whitespace characters: newlines, tabs,
    non-breaking-spaces, trailing whitespace. Avoid accidentally indenting with
    tabs when a file is indented with spaces, and vice versa.
- [Spellcheck](http://vimcasts.org/episodes/spell-checking/)
  - Spellcheck your code comments, markdown files, git commits. Never again will
    your code comments speak of "matrixes" and "varibles." _Never. Again._

---

Plugin Recommendations
================================================================================

This is a "grab bag" of plugins that we've found useful in the past. Don't go
through and blindly install every plugin on this list; start by installing the
ones that interest you, then gradually build your `.vimrc` from there.

---

Essentials
--------------------------------------------------------------------------------

These come _strongly_ recommended. While their usefulness isn't immediately
obvious, these are some of the most _useful_ vim plugins available. They provide
functionality whose absence you will _mourn_ if you're ever forced to use
a non-vim text editor or a "vanilla" vim installation.

#### [vim-surround](https://github.com/tpope/vim-surround)

Keymappings that make it easy to work with a piece of text's "surroundings."
Makes it possible to quickly (i.e. literally four keystrokes) replace the double
quotes surrounding a paragraph with single quotes, replace an erroneous set of
curly braces with parentheses, and quickly edit or insert HTML tags.

#### [vim-rsi](https://github.com/tpope/vim-rsi)

Enable readline-style keybindings in insert mode and on the vim command line.

These are the "`META-b` to go back a word," "`META-f to go forward a word"
bindings we mentioned in the earlier section on normal mode navigation.
Interestingly, these actually don't work by default when typing vim commands,
which can be a source of aggravation if you realize that you mistyped the second
argument of a five-argument command. Instead of mashing the left arrow key, or
using the mouse like a pleb, use readline keybindings!

Note that the "rsi" in "vim-rsi" stands for "readline-style insertion" and not
"repetitive stress injury," although this plugin definitely helps to prevent the
latter.

#### [vim-unimpaired](https://github.com/tpope/vim-unimpaired)

Keymappings wrapping around some of vim's less intuitive commands
(e.g. "next buffer," "next location in the location list," etc.)

#### [tabular](https://github.com/godlygeek/tabular)

Visually select a large block of text, hit a few keystrokes, and instantly
space-align everything in that highlighted block. [Check this screencast for more details.](http://vimcasts.org/episodes/aligning-text-with-tabular-vim/)

#### [ReplaceWithRegister](https://github.com/vim-scripts/ReplaceWithRegister)

Deleting a chunk of text into the unnamed register (`""`), visually selecting
another chunk of text, and then pasting the previously deleted text "on top" of
it will clobber the unnamed register. (vim acts as if the "replaced" text was
deleted, and shunts it into `""`.)

ReplaceWithRegister makes it possible to paste "on top of" existing text
without clobbering the `""` register.

---

File Navigation
--------------------------------------------------------------------------------

Filesystem navigation and navigation within an open file.

#### [nerdtree](https://github.com/scrooloose/nerdtree)

A file explorer for vim that opens in a "sidebar" (actually a narrow vertical
split.)


#### [BufExplorer](https://github.com/jlanzarotta/bufexplorer)

Quickly switch between any of the buffers (e.g. files, etc.) that vim has open.
Handy for quickly reopening files without having to launch NERDtree or navigate
through a complicated folder structure with `:edit`.


#### [vim-easymotion](https://github.com/easymotion/vim-easymotion)

Highlight every occurrence of a particular character on your screen and overlay
a letter on top of it. Choose the character you "want," press it on your
keyboard, and watch your cursor instantly jump to that location.

[Easier to understand with a screencast.](https://camo.githubusercontent.com/d5f800b9602faaeccc2738c302776a8a11797a0e/68747470733a2f2f662e636c6f75642e6769746875622e636f6d2f6173736574732f333739373036322f323033393335392f61386539333864362d383939662d313165332d383738392d3630303235656138333635362e676966)


#### [fuzzyfind](https://github.com/junegunn/fzf)

Search through your file system, git commits, buffers, etc. by drunkenly
slapping your keyboard. This is an exaggeration, _but only slightly._

---

"IDE-Like"
--------------------------------------------------------------------------------

#### [localvimrc](https://github.com/embear/vim-localvimrc)

Load special `.lvimrc` files in when in certain directories. Useful when hopping
between two codebases adhering to different style guides (e.g. one indents with
tabs, the other spaces). Pairs nicely with neomake and syntastic, since it lets
you set your syntax checker's compiler settings per-project by putting `.lvimrc`
files in those projects' directories.

#### [fugitive](https://github.com/tpope/vim-fugitive)

git integration within vim. On top of letting you `git status`, `git commit`,
`git pull`, etc., also allows you to [browse the entire git history of a
particular file.](http://vimcasts.org/episodes/fugitive-vim-exploring-the-history-of-a-git-repository/)


### Syntax Checkers and Linters

[Linting](https://stackoverflow.com/questions/8503559/what-is-linting) is a form
of static code analysis that checks for "red flags" in code (i.e. the sorts of
things that `-Wall -Werror -Wconversion -pedantic` will warn you about.) This
term is often used interchangeably with "syntax checking" or "compilation
checking."

Linter plugins _massively_ accelerate the ["edit, compile, run"](https://chortle.ccsu.edu/java5/Notes/chap06/ch06_10.html)
cycle that programmers often use when fixing syntax errors.  If you still
follow the process of: editing code in a text editor, running g++ from
a separate terminal window, reading the compilation errors from the terminal,
and then opening those files in your editor, now is the time to stop.

#### [syntastic](https://github.com/vim-syntastic/syntastic)

The most popular syntax checker for vim. Runs your code through an external
syntax checker (usually `g++`, for us EECS students) and tells you when you're
doing something wrong.

Needs some extra configuration when working within large codebases. If your
code `#include`s system headers (for libraries like `boost`) or even just `.h`
or `.hpp` files from another directory, you'll have to provide syntastic with
the appropriate `-isystem` and `-I` flags. See the GitHub README's section on
[passing arguments to a syntax checker.](https://github.com/vim-syntastic/syntastic#faqargs)

Note that this is done in a `.vimrc` file. With localvimrc, it can be done in a
`.lvimrc` file as well.

#### [neomake](https://github.com/neomake/neomake)

Another syntax checker for vim whose main selling point is asynchronous
execution (i.e. syntax checking won't momentarily freeze vim, since it happens
"in the background"). Originally written for neovim, but now compatible with
vim as well. [It doesn't seem that syntastic will get async support anytime
soon, unfortunately.](https://github.com/vim-syntastic/syntastic/issues/699#issuecomment-285039618)

Note that neomake is like syntastic in that its "makers" won't `#include`
directories unless provided with the appropriate command line flags. Again, you
can configure this in your `.vimrc`, or in `.lvimrc` files if you have
localvimrc installed.

#### [ALE](https://github.com/w0rp/ale)

Asynchronous Linter Engine. Functionally identical to neomake/syntastic, except
that it runs its syntax checks _completely_ asynchronously without the user
having to invoke its checks manually.

Also offers semantic autocompletion through [Language Server Protocol,](#the-language-server-protocol)
as well as the ability to "fix" detected linter errors programmatically.

### Project Navigation

#### [vim-easytags](https://github.com/xolox/vim-easytags)

Automatically generate [ctags](https://en.wikipedia.org/wiki/Ctags) from
inside vim. Move your cursor over a custom type and hit `CTRL-]` to jump to the
definition of that type. Pairs well with tagbar.

_Make sure to turn on its async support._ vim-easytags stores its ctags in a
sorted list; as time goes on, that list becomes large, and having your vim
freeze every ten minutes or so to update that list will get annoying after a
while.

Also, don't recursively generate ctags from within `/usr/include` because you
want to be able to `CTRL-]` custom types from open-source libraries. You'll get a
tags file that's literally gigabytes in size.

#### [tagbar](https://github.com/majutsushi/tagbar)

Lets you open a sidebar listing function definitions in the current file. Useful
when working with very large `.cpp` files. Because it relies on ctags, pairs
well with vim-easytags, which makes ctag generation a background process.


### Autocompletion

#### [YouCompleteMe](https://github.com/Valloric/YouCompleteMe)

Autocompletion for vim. A bit bulky; written before vim had native async
support and without the benefit of neovim's remote plugins, so installing it
requires compiling a large executable. More "tried and true" than the others,
but also large and cumbersome.

#### [deoplete](https://github.com/Shougo/deoplete.nvim)

Asynchronous autocompletion for neovim (natively) and vim (with some auxiliary
plugins). Supports autocompletion from a variety of sources, ranging from common
programming languages like Python and C++ to browser windows to active tmux
panes.

Actively maintained and well-supported.

#### [nvim-completion-manager](https://github.com/roxma/nvim-completion-manager)

Autocompletion for neovim using neovim's async API. Serves the same purpose as
deoplete, but is generally easier to install and configure. Comes with
"out-of-the-box" support for common autocompletion sources (e.g. the current
buffer, ctags, other tmux panes, local filepaths, etc.) More heavily
parallelized than deoplete, and potentially faster. Has better documentation.

As of the time of writing (April 2018), nvim-completion-manager is no longer
maintained, but is still more than stable enough for daily use.


### The Language Server Protocol

The [Language Server Protocol](https://microsoft.github.io/language-server-protocol/)
(abbreviated as **LSP**) is a generic interface that provides "language-specific
smarts" for any text editor that supports it. These "smarts" include, among
other things:

- Semantic autocompletion (of variable names accessible in the current scope,
  member functions of custom types, `#define` macros, object types from
  `#include`d libraries, etc.)
- "Go-to definition" (whereby a programmer can "mouse-over" a variable, hit
  a hotkey, and jump to where that variable was first declared)
- "Tooltip" Documentation (whereby a programmer can "mouse-over" a function call
  and see relevant snippets from that item's documentation)
- Symbol Renaming (whereby a programmer can, for instance, intelligently
  "bulk-rename" all occurrences of a local variable `int foo` _without_
  clobbering a `double foo` declared in a different variable scope)

A number of text editors support LSP (i.e. have working "language clients"),
including Eclipse, VSCode, Sublime Text, Atom, emacs, and (neo)vim.

The core idea behind the LSP is the fact that _any language server will work
with any language client._ [Rather than,](https://langserver.org/) say, writing
five different implementations of semantic Python autocompletion for five
different text editors (and then having to write five different implementations
of Rust autocompletion for those same five editors, and so on), one can simply
write five language clients for those five editors, and then write a [single
Python language server](https://github.com/palantir/python-language-server) that
will work with all of them.

The use of LSP requires the installation of a **language client** for your text
editor, and **language servers** for the programming languages you wish to use.

#### [LanguageClient-neovim](https://github.com/autozimu/LanguageClient-neovim/)

Currently the best language client available for (neo)vim. Despite its name,
this plugin does work with "ordinary" vim. That said, its semantic
autocompletion works best when used alongside an autocompletion plugin, such as
deoplete or nvim-completion-manager.

#### [Language Servers](https://langserver.org/#implementations-server)

The following is a list of the language servers that we recommend, along with
(possibly outdated) notes about how to install them and get them working.

For **Python,** we recommend [python-language-server.](https://github.com/palantir/python-language-server)
Unlike many plugins on this page, python-language-server (abbreviated as `pyls`)
has a nearly painless installation process (`pip install --user --upgrade jedi
python-language-server`) and is most likely to work "out of the box." Because of
this, and because many upper-level EECS courses use Python, we recommend
installing `pyls` as a sanity check to verify that your LSP installation
actually works.

For **C/C++** we recommend either [clangd](https://clang.llvm.org/extra/clangd.html)
or [cquery](https://github.com/cquery-project/cquery). While both are almost
functionally identical, they have different strengths, most of which involve
their installation processes.

*Note,* however, that both cquery and clangd use [LLVM's clang](https://en.wikipedia.org/wiki/Clang)
as a backend. Consequently, both require working clang installations, and both
require [up-to-date `compile_commands.json` files](https://github.com/cquery-project/cquery/wiki/compile_commands.json)
for the current project.

**clangd** is more likely to work "out of the box," but its installation process
is a bit frustrating. As of the time of writing, clangd is not in Ubuntu's
standard package repositories, and functional binaries are only available with
clang versions 6 and newer. The author typically installs `clangd` onto Ubuntu
machines with the following:

```
$ # Grab LLVM repository's public key
$ # NOTE: this may "hang"; if it does, interrupt it with CTRL-C and try running it again.
$ wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key | sudo apt-key add -
$
$ # Add the LLVM PPA, to enable `sudo apt install` of more recent clang packages
$ sudo apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-6.0 main"
$ sudo apt-get update
$ $INSTALLCMD clang*6.0 clang-tools-6.0
$
$ # Use clang-6.0 for everything
$ # NOTE: if you're actually using clang for schoolwork, DON'T run this blindly,
$ #       since it may break your preexisting clang installation.
$ sudo update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-6.0 100
$ sudo update-alternatives --install /usr/bin/clang clang /usr/bin/clang-6.0 100
$ sudo update-alternatives --install /usr/bin/clangd clangd /usr/bin/clangd-6.0 100
```

**cquery** was designed to allow rapid semantic autocompletion from the entire
codebase of Google Chromium. It does this by caching _everything_ into memory.
This works well with small codebases (e.g. EECS projects) and computers with
large (`>= 16GiB`) amounts of memory.

Installation involves either [downloading and extracting prebuilt binaries](https://github.com/cquery-project/cquery/releases)
or [building cquery itself from source.](https://github.com/cquery-project/cquery/wiki/Getting-started)

###  Debuggers

#### [vim-vebugger](https://github.com/idanarye/vim-vebugger)

A "no-frills" vim front-end for several commonly used debuggers. Allows
users to set breakpoints, open a debugger console in a split, inspect variable
values, and so on. Supports GDB and LLDB (for C/C++) and PDB (for Python), among
others.

#### [lldb.nvim](https://github.com/dbgx/lldb.nvim)

Provides an "IDE-like" debugging interface for C/C++ inside neovim, allowing the
user to set breakpoints, inspect variable values, and traverse the stack, among
other things. It acts as a front-end for [LLDB](http://lldb.llvm.org/), which is
clang's equivalent of gcc's GDB, and allows the user to explicitly invoke LLDB
"commands" through vim's command-line.

While extremely useful, this plugin is a massive pain to install and configure.
While clangd requires clang-6.0 or above, lldb.nvim requires clang-3.8 _or
lower_ due to [issues with LLDB's Python API.](https://github.com/dbgx/lldb.nvim/issues/51#issuecomment-294894345)
For this reason, lldb.nvim is no longer actively maintained, and it experiences
occasional crashes when used to debug large projects.

It is possible to install and use lldb.nvim alongside clangd. To achieve this,
one must `sudo apt install clang lldb` (which, on Ubuntu 16.04, installs
clang-3.8 and lldb-3.8). Further, one must also [fix the symlinks](https://stackoverflow.com/a/31005690)
that LLDB attempts to install. (Note that the respondent in the link installed
clang-3.6, so you will have to tweak his code to work properly with clang-3.8.)

---

Snippets
--------------------------------------------------------------------------------

#### [vim-snippets](https://github.com/honza/vim-snippets)

Create "templates" that you can drop into text files. Useful for writing
documents in LaTeX, inserting comment blocks of predetermined length, and so on.
The backend for plugins like UltiSnips.

#### [UltiSnips](https://github.com/SirVer/ultisnips)

Provides a convenient interface for creating, editing, and inserting snippets.

Miscellany
--------------------------------------------------------------------------------

#### [vimtex](https://github.com/lervag/vimtex)

A bunch of things that are handy for editing TeX files. Among other things, lets
you do the thing where you view a "live" compiled PDF of your current TeX file next
to your editor in SumatraPDF or similar.

#### [vim-airline](https://github.com/vim-airline/vim-airline)

Add useful information to vim's statusline, including:

- The current git branch (if any)
- The current filetype
- The currently active spellfile
- A wordcount (in markdown files, TeX files, etc.)

Also makes the statusline look pretty.

---


External Links
================================================================================

* [Bram Moolenaar's "Seven habits of effective text editing"](http://moolenaar.net/habits.html)
* [/r/vim on Reddit](https://reddit.com/r/vim)
* [/r/neovim on Reddit](https://reddit.com/r/neovim)
* [vim Wiki](vim.wikia.com)
* [_Learn Vimscript the Hard Way_ by Steve Losh](http://learnvimscriptthehardway.stevelosh.com/)
* [Steve Losh's Blog](http://stevelosh.com/blog/)
* [Steve Losh's twitch.tv](https://www.twitch.tv/stevelosh/)
* [_Practical Vim_ by Drew Neil](https://www.goodreads.com/book/show/13607232-practical-vim)
