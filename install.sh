#!/bin/bash

echo sudo apt-get install python python-gdata markdown
sudo apt-get install python python-gdata markdown

mkdir -p ~/bin
ln -s `pwd`/blog.py ~/bin/blog
