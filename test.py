import sys
import os
import subprocess 
from github import Github
from pprint import pprint
import webbrowser
import time

# check for total # of arguments
n = len(sys.argv)
print("total number of args: ", n)
if n < 2:
    print("Not enough arguments supplied")

# create a dir based off argv[1]
new_directory = str(sys.argv[1])
parent_dir = "/home/atomas22/Projects"

# full path

path = os.path.join(parent_dir, new_directory)
os.mkdir(path)
os.chdir(path)

print("Directory '% s' created" % new_directory)

# change to the new directory
cwd = os.getcwd()
print("Current working directory is:", cwd)

print("Directory changed!")

g = Github("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")
user = g.get_user()
repo = user.create_repo(new_directory)
print(repo)


cwd = os.getcwd()
print(cwd)
os.chdir(cwd)
os.system("git init")
os.system("touch README.md")
os.system("git add .")
os.system("git commit -m 'Initial commit'")
os.system("git push -u origin master")
os.system('code .')
