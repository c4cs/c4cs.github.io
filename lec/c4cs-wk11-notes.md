Administrative
==============

 - Week9 Advanced: Open PRs have the weekend to finish

 - Final Exam: Rooms posted. Practice exam released Monday.

python
======

Build around a Reverse Polish Notation Calculator

1. git clone https://gitlab.eecs.umich.edu/ppannuto/c4cs-w16-rpn
2. Run rpn.py

Three terminal lecture:

1. A python window to experiment in
2. The source file
3. Running the program

## Anatomy of a Python script

 - Syntax
   - #comments
   - if: def:
   - whitespace

 - Fundamental data types
   - numbers
   - strings
   - (), [], {}

 - Dynamic Typing

 - Walk through how it works -- add prints, show off raise, make mistakes

 - Improvements to make:

   - Division support
      o Show off help(operator)

   - Add `except EOFError` to main while loop (ctrl-d support)


### Scripts vs modules

    >>> import rpn_basic as rpn
    >>> rpn.calculate("1 1 +")
    2.0

### __Everything is an object, everything is mutable__

    >>> rpn.OPERATORS
    {'-': <built-in function sub>, '*': <built-in function mul>, '+': <built-in function add>}

    >>> rpn.OPERATORS['add'] = rpn.OPERATORS['+']
    >>> rpn.calculate("1 1 add")
    2.0

    >>> rpn.OPERATORS['+'] = rpn.OPERATORS['-']
    >>> rpn.calculate("1 1 +")
    0.0

    >>> def funnyadd(a, b):
    ...     return a + b + 7
    ...
    >>> rpn.OPERATORS['+'] = funnyadd
    >>> rpn.calculate("2 3 +")
    12.0

    >>> rpn.OPERATORS['+'] = lambda a1,a2: a2**a1
    >>> rpn.calculate("2 3 +")
    8.0


## Python classes

A module is something akin to a singleton instance of a class

But let's convert rpn to an actual class

   - `class Calculator:`
   - Lots of indenting
   - Adding some self's
   - constructor: `__init__`
   - `calculator = Calculator()` in main

Then let's make an integer-only subclass

   - Need to call `int` instead of `float`
   - Change `truediv` to `floordiv`


## Python magic: Libraries

`import readline`. Boom. Done.

Argugment parsing


### Postscript: #!/usr/bin/env python3

Almost always the right choice to use env

Type "env python", nothing special about /usr/bin -- just no $PATH


### Postscript: The kitchen sink


