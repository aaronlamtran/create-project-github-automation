#! /usr/bin/python
import sys
import os
from github import Github
from dotenv import load_dotenv
from re import search
import shutil

load_dotenv()

path = os.getenv("YOUR_NEW_PROJECTS_FILEPATH")
token = os.getenv("GITHUB_TOKEN")

def delete():
    repo_name = str(sys.argv[1])

    if not repo_name:
      print("No arguments supplied. Provide name of project after the command")
      exit()

    try:
      dir_path = path + str(repo_name)
      dir_exists = os.path.isdir(dir_path)
      if not dir_exists:
        next()
      else:
        decision = input('Are you really sure you want to delete this repository LOCALLY? (YES/NO)\n')
        if decision == "yes":
          shutil.rmtree(dir_path)
          print(f"Succesfully deleted LOCAL repository: {dir_path}")
        else:
          print('Ok. No action taken.  Moving on... ')
          next()
    except Exception:
      print('\nLOCAL directory does not exist\n')

    try:
      g = Github(token)
      repo = g.get_user().get_repo(repo_name)
      decision = input('Are you really sure you want to delete this repository REMOTELY? (YES/NO)\n')
      if repo and decision == "yes":
        repo.delete()
        print(f"\nSuccesfully deleted REMOTE repository: {repo}\n")
    except Exception:
      print('Failed to delete REMOTELY. Remote directory does not exist')


if __name__ == "__main__":
    delete()

