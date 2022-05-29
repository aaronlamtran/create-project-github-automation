#!/bin/bash


function git-me() {
  cwd=$(pwd)

  # exit if position input is not provided
  if [ -z "$1" ] ; then
    echo "No arguments supplied. Provide name of project after the command"
    # echo "No arguments supplied. Provide name of project after the command" && exit
  fi

  result=$(python3 $PATHTOGITHUBAUTO/create.py "$1" 2>&1 > /dev/null)


  if [[ "$result" == "FAIL_LOCAL" ]] ; then

    echo "\nFailed to create locally. Check your path and/or if directory already exists.\n"

  elif [[ "$result" == "FAIL_REMOTE" ]] ; then

    echo "\nSuccesfully created LOCAL repository: $1\n"
    echo "\nFailed to create remotely. Check your token.\n"

  else
    # github procedure
    echo "\nSuccesfully created LOCAL repository: $1\n"
    cd $YOUR_NEW_PROJECTS_FILEPATH"$1"
    touch README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/$GITHUB_USERNAME/$1.git
    git push -u origin main
    code .
    echo "\nSuccesfully created REMOTE repository: $1\n"
    echo '\ncmd + click to view your repos:' https://github.com/${GITHUB_USERNAME}\?tab=repositories "\n"
  fi

  cd $cwd
}

function git-me-remove() {
  cwd=$(pwd)

  python3 $PATHTOGITHUBAUTO/delete.py "$1"

  echo '\ncmd + click to view your repos:' https://github.com/${GITHUB_USERNAME}\?tab=repositories "\n"



  cd $cwd
}
