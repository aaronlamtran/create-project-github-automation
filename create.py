#! /usr/bin/python
import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("YOUR_NEW_PROJECTS_FILEPATH")
token = os.getenv("GITHUB_TOKEN")

def main():
    folderName = str(sys.argv[1])

    try:
        dir_exist = os.path.isdir(path + folderName)
        if dir_exist:
            sys.exit('FAIL_LOCAL')
        os.makedirs(path + str(folderName))
    except Exception:
        sys.exit('FAIL_LOCAL')

    try:
        g = Github(token)
        user = g.get_user();
        user.create_repo(folderName)
    except Exception:
        sys.exit('FAIL_REMOTE')


if __name__ == "__main__":
    main()

