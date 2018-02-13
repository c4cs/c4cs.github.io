---
permalink: /lectures/w17/week12.html
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


# Creating a Python Package for PyPi

## One-time Actions

Register an account at https://testpypi.python.org/pypi

## Per-project Actions

1. Clone the sample project `git clone https://github.com/pypa/sampleproject.git <myproject>`
2. Edit the source files
3. Edit the meta files (LICENSE.txt, MANIFEST.in, README.rst, setup.py)
4. Prep your package `python setup.py sdist`
5. Register your project on testpypi (follow "Package submission" link, upload `PKG-INFO`)
6. Upload your files (follow "files" link, upload tarball from `dist`)

## Use it!

1. `pip install -i https://testpypi.python.org/pypi c4cs-python`
2. Start python, `import c4cs`
