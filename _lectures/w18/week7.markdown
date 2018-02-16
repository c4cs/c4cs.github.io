---
permalink: /lectures/w18/week7.html
---

class: center, middle

# Unit Testing and Python

.copyright[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
** [Pat Pannuto](http://patpannuto.com) / Marcus Darden **
]

---

# Test Driven Development (TDD)

--

.center[
![:scale_img 60%](img/tdd_flow.gif)
]

---

# TDD Methodology

.left-column[
**"Strictly speaking"**
1. Add a test
2. Run the test suite
  - Note: This should fail!
3. Write the minimum code to pass tests
4. Run test suite
5. Refactor & repeat
]
.right-column[
**The pragmatist's view:**
- Add tests
- Run tests
- Write/fix code
]

--

<div style="clear: both;">
<hr />
</div>

- TDD can unfairly focus on "micro-tests"
- More tests != better tests, and do mean more maintenance

.footnote[
People study development methodologies,
[here's one](http://dl.acm.org/citation.cfm?doid=2961111.2962592)
just published that says TDD provides marginal benefit.

Takeaway? There is no "magic" way of doing things that will make your code
bug-free.
]

---

# Behavior Driven Development

.center[
.middle[
![BDD Workflow](img/bdd-workflow-600x268.png)
]
]


---

# Writing unit tests in Python

## Python??

---

# Getting started, create `rpn.py`

```python
#!/usr/bin/env python3

def calculate(arg):
    pass

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()
```
<hr />
```bash
$ python3 rpn.py
rpn calc> type anything here and hit enter
rpn calc>
```

---

# Quick refresher on RPN calculators

## Also a "stack-based" calculator

```
rpn calc> 1 1 +
2.0
rpn calc> 1 1 + 2 *
4.0
rpn calc> 1 2 3 +
Error: Malformed expression
```

---

# Create `test_rpn.py`

```python3
import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
```

- The name matters! Note that `test_rpn.py` tests `rpn.py`

<hr />
```bash
$ python3 -m unittest
F
======================================================================
FAIL: test_add (test_rpn.TestBasics)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/marcus/rpn_calc/test_rpn.py", line 8, in test_add
    self.assertEqual(2, result)
AssertionError: 2 != None

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

---

# Don't forget `git`!

```bash
$ wc -l *py
      11 rpn.py
       8 test_rpn.py
      19 total

# This is 19 lines of quality code here!
```

- Yes, we're committing *before anything works*

  - The structure is good
  - The _test harness works_

---

# And let's not forget `make` while we're at it

## Because why type 19 letters when you could type 4?

```make
test:
       	python3 -m unittest

.PHONY: test
```

.footnote[
Did this just give away a homework question? Why yes, yes it did.
]

---

# Live coding

## __PLEASE__ stop me and ask questions if you're confused

## __PLEASE__ yell at me to slow down if I go too fast

<hr />

- Implement add
  - Need a stack for the calculator
  - Need to tokenize the input
  - Need to process tokens

--

- Add test for subtract

--

- Implement subtract

--

- Tests can expect failure: malformed input

--

- On your own: Tests and implementation for multiply, divide

???

def calculate(arg):
    stack = []
    for operand in arg.split():
        if operand == '+':
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(float(operand))
    return stack.pop()

---

# Some fancy Python and the big refactor

### Motivation: Unwieldy if-else chain going

  - Gets worse as more operands are added
  - A modular design will allow flexibility

--

### Goal: Simplify parser code

  - Is it a number? Then add to stack
  - Else look up operator and execute

???

import operator
OPERATORS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.div,
        }

    for operand in expression.split():
        logging.debug("Stack: {} || Operand: {}".format(stack, operand))
        try:
            stack.append(float(operand))
        except ValueError:
            operator_fn = OPERATORS[operand]
            # !! Note: This arg order is wrong, commutative ops will work
            # though! Use this to show off value of testing!
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = operator_fn(arg1, arg2)
            stack.append(result)


---

# Attendance: Push your code to gitlab

1. Go to https://gitlab.eecs.umich.edu
2. Click "New Project"
3. Name your project **exactly**: `c4cs-w18-rpn`
4. Set your project to **publically visible**
<img src="img/gitlab-visibility.png" width="400px" />
5. Scroll down and follow the directions for **existing folder or Git repository**
  - You shouldn't need to create a repo (we already did that)
  - **Make sure you've committed all your changes!**
  - `git remote add .....`
  - `git push -u origin master`
    - Your username is your uniqname, and password is your umich.edu password
