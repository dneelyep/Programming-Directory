#!/bin/sh

cd /tmp

rm -rf test-project

quickly create ubuntu-application test-project
# Creating bzr repository and committing
# Congrats, your new project is setup! cd /tmp/test-project/ to start hacking.
# Creating project directory test-project

cd test-project

bzr status

(echo "Copyright (C) 2010 Oliver Twist <twist@example.com>" > AUTHORS)

(echo "My super cool project" > README)

bzr status
# modified:
#   AUTHORS
# unknown:
#   README

quickly save
# adding README
# Committing to: /tmp/test-project/
# modified AUTHORS
# added README
# Committed revision 2.

bzr log -r -1 | grep '^  ' | sed 's/^  //'
# quickly saved

bzr status

mkdir new-folder

(echo "New File!" > new-folder/new-file)

bzr status
# unknown:
#   new-folder/

quickly save added new-file
# adding new-folder
# adding new-folder/new-file
# Committing to: /tmp/test-project/
# added new-folder
# added new-folder/new-file
# Committed revision 3.

bzr log -r -1 | grep '^  ' | sed 's/^  //'
# added new-file
