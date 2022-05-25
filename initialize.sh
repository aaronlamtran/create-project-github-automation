#!/bin/bash

# export PATHTOGITHUBAUTO="/Users/aarontran/Documents/Hack/create-project-github-automation"
source $PATHTOGITHUBAUTO/.env

function create() {
  cwd=$(pwd)

  # exit if position input is not provided
  if [ -z "$1" ] ; then
    echo "No arguments supplied. Provide name of project after the command" && exit
  fi

  # venv
  source $PATHTOGITHUBAUTO/venv/bin/activate
  python3 $PATHTOGITHUBAUTO/create.py $1
  deactivate

  # github procedure
  cd $FILEPATH$1
  echo "# README" >> README.md
  git init
  git add README.md
  git commit -m "first commit"
  git branch -M main
  git remote add origin https://github.com/$GITHUB_USERNAME/$1.git
  git push -u origin main
  code .

  cd $cwd
}
