#!/bin/bash

python3 git_script.py 
cd /home/atomas22/Projects
read dirname
mkdir $dirname
cd $dirname
touch README.md
git init
pwd


