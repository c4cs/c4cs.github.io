---
permalink: /lectures/f18/intro-julia.html
---

class: center, middle

# Basic ML with Julia and Azure

.copyright[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
** [Pat Pannuto](http://patpannuto.com) / Amrit Hariharan **
]

---

# Getting Ready

  - [Julia installation](https://julialang.org/downloads/platform.html)
  - [Anaconda](http://jupyter.org/install) and [Julia kernel](https://github.com/JuliaLang/IJulia.jl) installation
  - [Azure](https://azure.microsoft.com/en-us/free/students/) student offer

---

# What is Julia?

  - High performance dynamically typed language
  - WAY faster than python (almost as fast as C)
  - Designed for concurrent, parallel, and distributed computing
  - Can directly call C libraries
  - [Open source!!!](https://github.com/JuliaLang/julia)

![JuliaGithub](img/JuliaGithub.png)

---

# Why Julia?

  - Lots of easy to use libraries
  - It's basically executable math

```julia
julia> area(r) = π * r^2
area (generic function with 1 method)

julia> area(3)
28.274333882308138
```

---

class: center, middle

# Time to try it out

---

# Moving to the Cloud

--

## Why?

  - Don't have to have your computer on 24/7
  - MORE POWER

--

## Which Service?

  - AWS, Google Cloud, and Azure should all work fine
    - All should give you free credits to start too!
  - Azure has a [data science image](https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/dsvm-ubuntu-intro) with everything we need already installed

---

class: center, middle

# To the Cloud!
