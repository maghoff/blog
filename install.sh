#!/bin/bash

echo sudo apt-get install python python-gdata markdown
sudo apt-get install python python-gdata markdown


# The following assumes that ~/bin will be put in your PATH by ~/.profile. Ubuntu
# does this by default, but only when ~/bin exists, so you might want to re-login.

mkdir -p ~/bin
ln -s `pwd`/blog.py ~/bin/blog
