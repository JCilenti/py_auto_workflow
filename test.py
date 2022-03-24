import sys
import os
import subprocess 
from github import Github
from pprint import pprint
import webbrowser
from selenium import webdriver
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

# create a README file here
file = open("README.md", "w")    

print(path)

print("Directory '% s' created" % new_directory)

# change to the new directory
cwd = os.getcwd()
print("Current working directory is:", cwd)

print("Directory changed!")

# needs git init here somewhere

os.system('code .')

# using selenium
driver = webdriver.Chrome(r"/home/atomas22/driver")
driver.get("https://github.com/")

# web browser
#url = "https://github.com/"
#webbrowser.open(url)

# click on new repo


#new_repo = github.Repository(new_directory)

file.close()