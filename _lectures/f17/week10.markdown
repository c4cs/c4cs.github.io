---
permalink: /lectures/f17/week10.html
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


# Creating a Simple Python Package for PyPI

## One-time Actions

Register an account at https://test.pypi.org

Create a ~/.pypirc file

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
```


---


# Creating a Simple Python Package for PyPI

## Per-project Actions

1. Clone the sample project `git clone https://github.com/pypa/sampleproject.git <myproject>`
2. Edit the source files
3. Edit the meta files (LICENSE.txt, MANIFEST.in, README.rst, setup.py, setup.cfg)
4. Upload your package `python setup.py sdist upload -r testpypi`

## Use it!

1. `pip3 install -i https://test.pypi.org/pypi c4cs-f17-python`
2. Start python, `import c4cs`


---


# Creating a Simple Python Package for PyPI

## It's your turn (attendance)!!

* Make a PyPI package (on TestPyPI) of your RPN Calculator
* Name the package f17-rpn-<uniqname>
