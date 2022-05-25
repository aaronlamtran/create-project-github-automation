import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
username = os.getenv("GITHUB_USERNAME")
token = os.getenv("GITHUB_TOKEN")

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    g = Github(token)
    user = g.get_user();
    user.create_repo(folderName)
    print(f"\nSuccesfully created repository {folderName}\n")

if __name__ == "__main__":
    create()
