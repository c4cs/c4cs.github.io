Package managers
================

  - why do they exist
  - how to find what you need?

People were confused by “sh”, “pip” and not enough direction here
so what’s pip and what does it do?
  - installs library so we can use it
    .. which means?
  - where’s the file
    >>> import os
           os.__file__
           import arrow
           arrow.__file__
           import sys
           sys.path
  - ppannuto/python-saleae to show requirements, multiple files
  - Virtual environments

Other package managers we’ve seen?
  apt-get / aptitude 
  ruby / get / bundle

Everyone has one
  Javascript -> node -> npm
  Rust -> Cargo -> Crates.io
  Java -> Maven

So do tools!
  Visual Studio -> nuget
  Vim -> pathogen
  Sublime -> package control

Oddball:
  C / C++  —> `aptitude install "library_name"-dev`
                 —> e.g. wk9 advanced, installed zlib1g-dev


Finding Packages
==============

Google!
apt-cache search (aptitude search)
  — aside: `apt-*` vs `aptitude`
  — similar to git “porcelain” commands (“git commit” vs “git hash-object” “git update-index” “git write-tree”)
       except we use the ugly ones day-to-day, *shrug*

—————————

Syncing state

ssh
  - ssh-keygen
  - ssh-copyid

scp
rsync

Syncing state w/ CAEN

sshfs
or git

Or AFS — check out advanced!
