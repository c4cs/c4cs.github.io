---
permalink: /lectures/w17/week15b.html
---

class: center, middle

# Virtual Private Servers
_alex chojnacki_

---

# The history of computing in a nutshell

1. Began with dumb terminals attached to smart mainframes

--

1. Moved to stronger individual computers, "PC's"

--

1. Back to dumb devices connected to supercomputers.
  * _What can you even do on
   a phone with no internet connection?_


---

# What is a VPS?

--

_Okay, yeah, it's a "virtual private server" ..._

---

# What does Wikipedia say about it?

> _"A VPS runs its own copy of an operating system, and customers have superuser-level access to that operating system instance, so they can install almost any software that runs on that OS. For many purposes they are functionally equivalent to a dedicated physical server, and being software-defined, are able to be much more easily created and configured." -- Wikipedia_




???
Aside from "customer", it sounds the same as our normal VM.

1. How is a VPS similar to our VirtualBox images from this description?
1. Are there any advantages we can think of?

Alike
- disposable
- can install whatever we want

Different
- Easily (automajically) configurable
- We can pay $$$ to get better resources
- Create and destroy instances as they are needed
- There's no GUI _(usually)!_

--

# Advantages
* They are easily configurable ...
* We can make as many as we want ...
* We can make them as powerful as we need ...
* We can create and destroy them instantly ...

---
class: center, middle

![Netflix Traffic](http://www.internetphenomena.com/wp-content/uploads/2010/10/Netflix-Time-of-Day.png)

---
class: center, middle

# How do I make one?

---

# Vagrant

* A "headless" VM
* Provisioning support built-in
* Often times more convenient without the GUI
* Provisioning mechanism

```bash
thealex :: $ vagrant init hashicorp/precise64
...
thealex :: $ vagrant up
...
thealex :: $ vagrant ssh
```

--

_Why is provisioning cool?_ **::** What if I want to make 50 VMs at once and they all need the same config?

---

# Docker

* A "lightweight" VM
* Quicker than vagrant, but much less contained
    - Where vagrant/virtualbox virtualise the hardware, docker utilizes a clever namespace trick in order to run processes in 'isolated' environments while avoiding any hardware virtualisation.
* Rich ecosystem of third-party images and environments

```
docker run -it ubuntu bash
```

--

## AWS, Linode, DigitalOcean, etc.

* Disposable servers in the cloud!

---


# Alright, so what can I do with them?

--

* Host personal website/app
* Temporarily "rent" a more powerful PC
* Host chatbots like GitHub's `hubot`

--

.center[_Use your imagination!_]

---

## Why would I ever use AWS for compute power?

--

### I hear neural networks are all the rage ...

http://arxiv.org/pdf/1508.06576v2.pdf

https://github.com/jcjohnson/neural-style

---

# Installing dependencies

```bash
luarocks install sys
luarocks install image
luarocks install loadcaffe
luarocks install torch
export LD_LIBRARY_PATH=/home/ubuntu/torch-distro/install/lib:/home/ubuntu/torch-distro/install/lib:/home/ubuntu/cudnn-6.5-linux-x64-v2-rc2

# clone the project and install
git clone https://github.com/jcjohnson/neural-style
cd neural-style
sh models/download_models.sh
```

--

- What is `luarocks`?
- What is `export LD_LIBRARY_PATH` doing?
- What about the sh command?

---

# How do we get my image onto the server?

- email it to myself?
- Click and drag to the ... just stop -- no.

--

- `scp`!

`scp -i ~/Downloads/c4cs-neural-style.pem ubuntu@ec2-52-70-134-147.compute-1.amazonaws.com:neural-style/output.png .`

- maybe even a python webserver ... `http://52.70.134.147`
---

# Card Demo

--

## Problem

- Wrote a bunch of notes with `word::definition` pairs

- Wanted a flash card app on my phone

--

## Solution

- Simple project using node.js, mongo, express.js

- Written in an afternoon

--

- ... or two.

--

http://104.131.102.44:3000/


---

# A few notes about the class

From the first slide of the course ...

```
## What this class is about
- This is not "Tools for Computer Scientists"

- Though, we will cover a lot of cool tools

- The goal is to give you the ability to pick up, learn, and use tools effectively
```

_Hopefully ..._

- ... you've followed a guide and needed to improvise.

--

- ... you've learned a tool or two that surprised you.

--

- ... you're more confident approaching new problems.

--

.center[__You know more than you think you know,__]
.center[__and nothing on a command line is hard ... __]

--

.center[__ ... the second time ...  __]

