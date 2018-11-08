---
permalink: /lectures/f18/week10.html
---

class: center, middle

# Package Managers

.copyright[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
** [Pat Pannuto](http://patpannuto.com) / Marcus Darden **
]


---


# Package Managers

* What are they?
* What do they do?
* Let's name a few...


---


# Creating an installable python package

## One-time Actions

1. Upgrade the python toolchain

```console
$ sudo apt-get update
$ sudo apt-get install python3 python3-pip python3-venv python3-wheel python3-setuptools
```



---


# Creating an installable python package

## Per-project Actions

1. Create a python virtual environment for your project

```console
$ mkdir <projectdir>  # If creating from scratch
$ cd <projectdir>
$ python3 -m venv env
```


---


# Creating an installable python package

## Per-project Actions

2. Add a `setup.py` to your project

```python
from setuptools import setup

setup(
    name='c4cs_fa18_<uniqname>',
    version='0.1.0',
    packages=['<packagename>'],
    entry_points={
        'console_scripts': [
            '<packagename> = <path>.<module>:<function>'
        ]
    },
)
```


---


# Creating an installable python package

## Per-project Actions

3. Create a python package

```console
$ mkdir <packagename>
$ touch <packagename>/__init__.py
```

4. Edit or move your source code into the `<packagename>` folder
    - Remember to add a shebang at the top of executable files
    - `#!/usr/bin/env python3`
5. Install it locally

```console
$ pip3 install .  # Add -e or --editable to enable local editing
```


---


# Adding a package to PyPI (The Python Package Index)

## One-time Actions

1. Register an account at https://test.pypi.org
2. Create a ~/.pypirc file

```
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username: mmdarden

[testpypi]
repository: https://test.pypi.org/legacy/
username: mmdarden
password: <your-very-very-insecure-password-here>

```
    - I haven't figured out how to work the password more securely
    - An issue was raised and closed, but doesn't seem to have fixed this


---


# Adding a package to PyPI (The Python Package Index)

## Per-project Actions

1. Add some more info to `setup.py`
    - Project stuff:
        - `license='MIT'`
        - `description='<some-text-here>'`
        - `url='<gitlab-repo-address>'`
    - User stuff:
        - `author='<your-name>'`
        - `author_email='<duh>'`
2. Upload your package `python setup.py sdist upload -r testpypi`
3. `pip3 install -i https://test.pypi.org/pypi c4cs-f18-python`
4. Start python, `import c4cs`

More at [https://python-packaging.readthedocs.io/en/latest/minimal.html]


---


# Creating a Simple Python Package for PyPI

## It's your turn!!

* Make a PyPI package (on TestPyPI) of your RPN Calculator
* Name the package `f18_rpn_<uniqname>`

