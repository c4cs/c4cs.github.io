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

# Why vim?

Because vim is [Difficult, But Awesome.](http://tvtropes.org/pmwiki/pmwiki.php/Main/DifficultButAwesome)

[vim is infamous among programmers for its steep learning curve.](https://www.reddit.com/r/ProgrammerHumor/comments/33a6p7/)
Because vim was designed to be used in a command-line interface, it's entirely
controlled with keyboard shortcuts. Most of the "standard" keyboard shortcuts
that we're familiar with (e.g. `CTRL-a` for "select all", `CTRL-c` for "copy")
either won't work in vim, or they won't do what you'd expect without some
prior setup.

That reliance on keyboard commands is a blessing and a curse. On one hand, it
makes vim difficult to learn. On the other hand, because you can control vim
without ever removing your hands from the keyboard, skilled vim users can edit
code [very, _very_ quickly.](https://youtu.be/o6omymj1JZI)

### Using vim, you can...

**...record macros to make writing test cases less repetitive...**

![test-cases](../static/commands/img/test_cases.gif)

[Link](http://vim.wikia.com/wiki/Macros)

**...select text and toggle between uppercase and lowercase...**

![toggle-case](../static/commands/img/toggle_text.gif)

[Link](http://vim.wikia.com/wiki/Switching_case_of_characters)

**...and edit text in blocks, not just line-by-line or character-by-character.**

![visual-block-copypaste](../static/commands/img/visual_block.gif)

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

# Introduction to Modal Editing
`vimtutor` covers the basics of using vim better than we can here, but it
doesn't spend much time explaining one of vim's less intuitive features: modal
editing.

Unlike a word processor like Google Docs, or an IDE like Xcode, vim's behavior
(i.e. what will happen when you press a key) changes based on its current
**mode**. The modes you'll use most frequently in vim are **normal** mode,
**insert** mode, and **visual** mode,

## Insert Mode
We'll start with insert mode because it's the easiest to understand.

![insert-mode](../static/commands/img/insert_mode.gif)

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

## Normal Mode

Normal mode, as its name suggests, is the mode you'll spend the most time using.
You start in normal mode when you launch vim, and you return to normal mode
when you exit another.

This is counterintuitive for many people because they're used to text editors
and word processors that almost always "stay in insert mode" (e.g. nano,
gedit, Microsoft Word, LibreOffice Writer, etc.) Many novice vim users spend
_all_ of their time in insert mode, only entering normal mode to save their work
and to close vim.

Editing exclusively in normal mode defeats the entire purpose of using vim! By
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
![normal-nav](../static/commands/img/normal_nav.gif)

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

## Visual Mode

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

![visual-normal](../static/commands/img/visual_normal.gif)

#### `-- VISUAL LINE --`

Used for selecting entire lines of text at a time. The mode you'll probably use
most frequently, at least when programming. To use, move the cursor to the first
line you want to select, then press `V`.

![visual-line](../static/commands/img/visual_line.gif)

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

![visual-block](../static/commands/img/visual_block.gif)

---

# The `.vimrc`

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
installation will be [completely unusable by anybody except
yourself](https://xkcd.com/1806/).)

The settings in Tim Pope's [sensible.vim](https://github.com/tpope/vim-sensible)
are a good starting point for a personal `.vimrc`. You can find many online
quick-start guides offering tips for vim beginners, as well.

## Version Control and the `.vimrc`

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

## An Aside: `.vimrc` Bloat

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

# vim Plugins

Many of the niceties that you're used to having in a more modern text editor
aren't baked into vim by default. In theory, you could implement these
yourself in vimscript, but writing a time- and memory-efficient implementation
of tab autocompletion in vimscript is far more effort than it's worth.

Thankfully, you don't need to. vim has a vibrant community of plugin authors
that have already done much of the heavy lifting. Of these, [Tim Pope](https://github.com/tpope)
and [Martin Grenfell (a.k.a. scrooloose)](https://github.com/scrooloose)
are some of the most prolific.

## Plugin Managers

Because vimscript is an interpreted language, having access to a vimscript
executable is the same as having the original vimscript source code. This allows
developers of vim plugins to distribute their plugins through GitHub. Installing
these plugins is a matter of `git clone`ing the plugins into the appropriate
directories on your machine.

Although vim does have built-in support for plugins, that support is fairly
rudimentary. You'll want to use a plugin manager to install and update plugins,
especially as the complexity of your vim installation grows.

Two of the most popular plugin managers are:

### pathogen.vim
Tim Pope's pathogen.vim is notable in that it [effectively created the standard
layout](http://stevelosh.com/blog/2011/09/writing-vim-plugins/be-pathogen-compatible)
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

---

# An Aside: vim vs. neovim

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


---

# Using vim vs. Using an IDE

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

But, **if you're willing to put in the time, you can make vim work like an
IDE.** You can accomplish this with the use of plugins.

Installing and configuring these plugins is a bit of a pain, unfortunately. You
can find a good list of plugins that provide IDE-like functionality
[here.](http://vim.wikia.com/wiki/Use_Vim_like_an_IDE)


---

# Things to Learn

Some neat features that vim offers without needing to install plugins. (There's
some overlap between the information given here and some of the sections
above, but these should go into more detail.)

* [Mapping Keys in Vim](http://vim.wikia.com/wiki/Mapping_keys_in_Vim_-_Tutorial_(Part_1))
  * Changing keymappings is one of the simplest and most important parts of
  configuring your vim installation.
  * Might we recommend `inoremap jk <ESC>` and `vnoremap jk <ESC>`? That lets you
    exit insert mode and visual mode by hitting `j` and then `k` in quick
    succession. It's faster than hitting `<ESC>`, you don't have to move your
    left hand, and it lets you finish a text insertion or text selection with
    your fingers already on the home row.
* [HJKL, WB, E: Real Vim Users Don't Use Arrow Keys](http://vim.wikia.com/wiki/Moving_around)
  * `hjkl`, the basic navigation keys, are accessible without moving your hands
  from the home row. `w`, `b`, and `e` make it much less annoying to navigate
  within a line.
* [`count`: Repeat the Next Command `n` Times](http://vimdoc.sourceforge.net/htmldoc/intro.html#count)
  * Relatively self-explanatory. If `j` in normal mode moves you down by one
  line, `10j` moves you down ten lines. Pressing `i` in normal mode, then
  typing `harbaugh` and hitting `<ESC>` inserts the text `harbaugh` into your
  file. Pressing `10i` in normal mode and doing the same inserts _ten_
  `harbaugh`s into your file. And so on.
  * If only there was a way to see how far away a given line was from your
  current position? That would make jumping between blocks of code much
  faster...
* [Rapid File Navigation with Relative Line Numbering](https://jeffkreeftmeijer.com/vim-number/)
  * Jump around your text files like a jackrabbit that's been fed coffee
  grounds. _Nothing_ but coffee grounds, _till the end of its days._
* [Text Searching](http://vim.wikia.com/wiki/Searching)
  * Find something in the current file.
* [Search Patterns (a.k.a. Regular Expressions)](http://vim.wikia.com/wiki/VimTip188)
  * What if you don't want to search for the specific string `"12345 Arbor
  St."`, but instead want to search for all address-like strings in the
  current file?
* [Search and Replace](http://vim.wikia.com/wiki/Search_and_replace)
  * Like find and replace, but much more powerful.
  * Supports standard search and replace (i.e. find this exact string, replace
  it with this exact string), but also regular expressions ("regex"), ranges
  (i.e. replace between this line and this line) as well as command-line-esque
  "flags" for special behavior.
* [Mr. Worldwide: The `g`lobal Command](http://vim.wikia.com/wiki/Power_of_g)
  * Let's say you have a Linux log file that's tens of thousands of lines long,
  and you want to delete every line that doesn't contain the string
  `"NetworkManager"`. You can do this with a single vim command.
* [Recording Macros and Macro Playback](http://vim.wikia.com/wiki/Macros)
  * Record a series of keystrokes that you can play back by hitting `@` followed
  by a letter. For when you need to repeat a short, repetitive, complicated
  task that would be hard to automate programmatically.
  * These macros pair nicely with the special navigation keys given above (`w`,
  `e`, `b`, etc.), since they're more "intelligent". Recording basic
  navigational movements (`hjkl`) is akin to hardcoding a program to only
  read in a specific number of lines.
* [Visual Selection](http://vim.wikia.com/wiki/VimTip386)
  * Highlight text without using the mouse. Highlight character-by-character or
  line-by-line. Highlight rectangular boxes of text.
  * Pairs very nicely with vim's special navigation keys, especially when you
  couple them with `count`.
* [Toggle Case](http://vim.wikia.com/wiki/Switching_case_of_characters)
  * That thing you've probably wanted to be able to do in text editors for a
  while.
* [Copy-Pasting: Yanking and Registers](http://vim.wikia.com/wiki/Copy,_cut_and_paste)
  * Copy-pasting to/from the system clipboard, if that functionality is enabled
  on your machine.
  * Having multiple places into which you can copy-paste. Handy, in some
  situations.
* [Paste Mode: When the `+` Register Doesn't Work](https://stackoverflow.com/questions/2514445/)
  * There are some places where you don't have access to the system clipboard
  (e.g. Windows Subsystem for Linux, while SSHing into CAEN). This gives you
  the ability to paste in those situations, though you can't copy.
* [Split Buffers](http://vimcasts.org/episodes/working-with-windows/)
  * View multiple files side-by-side, or open multiple views of the same file at
  different positions.
  * If you use neovim, you can open a terminal side-by-side with a text file
  and copy-paste from one into the other.
* [Folding](http://vim.wikia.com/wiki/Folding)
  * Collapse a selected text range, hiding it from view. Open it again if you're
  interested in what's there, hide it again if it's getting in the way.
* [The `vimdiff` Command](http://vimcasts.org/episodes/comparing-buffers-with-vimdiff/)
  * Open two files side-by-side in a vertical split. Automatically fold sections
  of the files that are identical. Highlight the lines that are different.
  * `vimdiff` is actually just an alias for `vim -d`. If you use neovim, you can
  launch a `vimdiff` inside neovim using `nvim -d`.
* [Tabs in Vim](http://vim.wikia.com/wiki/Using_tab_pages)
  * For when you start working on those large coding projects.

---

# Plugin Recommendations

Some of these require a great deal of hair-pulling and frustration to properly
set up. These plugins are loosely sorted by usefulness and ease of installation,
with more useful/easier to install plugins near the top.

**vim-surround**
([GitHub Link](https://github.com/tpope/vim-surround))

Convenient keymappings for working with text that lies "between" things, whether
they be curly braces, parenthesis, quotation marks, HTML tags, and more.

**vim-unimpaired**
([GitHub Link](https://github.com/tpope/vim-unimpaired))

Convenient keymappings wrapping around some of vim's less intuitive commands.

**nerdtree**
([GitHub Link](https://github.com/scrooloose/nerdtree))

A file explorer for vim that opens in a "sidebar" (actually a narrow vertical
split.)

**localvimrc**
([GitHub Link](https://github.com/embear/vim-localvimrc))

Load special `.lvimrc` files in when in certain directories. Useful when hopping
between two codebases adhering to different style guides (e.g. one indents with
tabs, the other spaces). Pairs nicely with neomake and syntastic, since it lets
you set your syntax checker's compiler settings per-project by putting `.lvimrc`
files in those projects' directories.

**fugitive**
([GitHub Link](https://github.com/tpope/vim-fugitive))

git integration within vim. On top of letting you `git status`, `git commit`,
`git pull`, etc., also allows you to [browse the entire git history of a
particular file.](http://vimcasts.org/episodes/fugitive-vim-exploring-the-history-of-a-git-repository/)

**syntastic**
([GitHub Link](https://github.com/vim-syntastic/syntastic))

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

**neomake**
([GitHub Link](https://github.com/neomake/neomake))

Another syntax checker for vim whose main selling point is asynchronous
execution (i.e. syntax checking won't momentarily freeze vim, since it happens
"in the background"). Originally written for neovim, but now compatible with
vim as well. [It doesn't seem that syntastic will get async support anytime
soon, unfortunately.](https://github.com/vim-syntastic/syntastic/issues/699#issuecomment-285039618)

Note that neomake is like syntastic in that its "makers" won't `#include`
directories unless provided with the appropriate command line flags. Again, you
can configure this in your `.vimrc`, or in `.lvimrc` files if you have
localvimrc installed.

**vim-easytags**
([GitHub Link](https://github.com/xolox/vim-easytags))

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

**tagbar**
([GitHub Link](https://github.com/majutsushi/tagbar))

Lets you open a sidebar listing function definitions in the current file. Useful
when working with very large `.cpp` files. Because it relies on ctags, pairs
well with vim-easytags, which makes ctag generation a background process.

**vim-snippets**
([GitHub Link](https://github.com/honza/vim-snippets))

Create "templates" that you can drop into text files. Useful for writing
documents in LaTeX, inserting comment blocks of predetermined length, and so on.
The backend for plugins like UltiSnips.

**UltiSnips**
([GitHub Link](https://github.com/SirVer/ultisnips))

Provides a convenient interface for creating, editing, and inserting snippets.

**vimtex**
([GitHub Link](https://github.com/lervag/vimtex))

A bunch of things that are handy for editing TeX files. Among other things, lets
you do the thing where you view a "live" compiled PDF of your current TeX file next
to your editor in SumatraPDF or similar.

### Uncooperative (But Very Useful) Plugins

Some assembly required.

**lldb.nvim**
([GitHub Link](https://github.com/dbgx/lldb.nvim))

Mentioned above. neovim only. Gives you an IDE-like debugging interface from
inside neovim where you can step through code, set breakpoints on lines, etc.
Uses `clang` and some additional Python code as a backend.

Installing `clang` on Ubuntu so that lldb.nvim can use it is a bit
squirrely. See [this question](https://stackoverflow.com/a/31005690) on
StackOverflow for more information.

#### Autocompletion

**YouCompleteMe**
([GitHub Link](https://github.com/Valloric/YouCompleteMe))

Autocompletion for vim. A bit bulky; written before vim had native async
support and without the benefit of neovim's remote plugins, so installing it
requires compiling an executable. More "tried and true" than the others,
however.

**deoplete**
([GitHub Link](https://github.com/Shougo/deoplete.nvim))

Autocompletion for neovim that uses neovim's async API. Less bulky than
`YouCompleteMe`, but getting its `C++` semantic completion to work is
_exceptionally_ squirrely.

**nvim-completion-manager**
([GitHub Link](https://github.com/roxma/nvim-completion-manager))

Autocompletion for neovim using neovim's async API. Allegedly better-written
than deoplete.
