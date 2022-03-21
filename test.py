import sys
import os
import subprocess 
import git

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

os.system('code .')

new_repo = git.Repo(new_directory)



file.close()