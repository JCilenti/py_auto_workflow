from importlib.resources import path
import sys
import os
from github import Github
from pprint import pprint


# check for total # of arguments
def check_args():
    n = len(sys.argv)
    print("total number of args: ", n)
    if n < 2:
        print("Not enough arguments supplied")

# create a dir based off argv[1]
def create_dir():
    global cwd
    global new_directory
    new_directory = str(sys.argv[1])
    parent_dir = "/home/atomas22/Projects"
    path = os.path.join(parent_dir, new_directory) # full dir
    os.mkdir(path)
    os.chdir(path)
    print("Directory '% s' created" % new_directory)
    # change to the new directory
    cwd = os.getcwd()
    print("Current working directory is:", cwd)
    os.chdir(cwd)
    print("Directory changed!")
    return cwd

# authenticate with Github and create repo
def create_git_instance():
    g = Github("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")
    user = g.get_user()
    repo = user.create_repo(new_directory)
    print(repo)

# stage changes for push and open in VSCode
def finishing_up():
    cwd = os.getcwd()
    os.chdir(cwd)
    print(cwd)
    os.system("git init")
    os.system("touch README.md")
    os.system("git add .")
    os.system("code .")


if __name__ == '__main__':
    check_args()
    create_dir()
    create_git_instance()
    finishing_up()

