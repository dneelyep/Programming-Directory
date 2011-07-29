#!/bin/sh

cd /tmp

rm -rf test-project

rm -rf subdir

HOME=/ quickly create
# ERROR: No template specified for command create.
# Usage: quickly create <template> <project-name>
# Candidate templates are: ubuntu-application, ubuntu-cli, ubuntu-flash-game, ubuntu-pygame

quickly create ubuntu-application
# ERROR: No project name specified.
# Usage: quickly create <template> <project-name>

quickly create ubuntu-application 42
# ERROR: unpermitted character in name.
# The name must start with a letter and contain only letters, spaces, dashes (-), and digits.

quickly create ubuntu-application test_project
# ERROR: unpermitted character in name.
# The name must start with a letter and contain only letters, spaces, dashes (-), and digits.

quickly create ubuntu-application test-pröject
# ERROR: unpermitted character in name.
# The name must start with a letter and contain only letters, spaces, dashes (-), and digits.

quickly create ubuntu-application "test project"
# Creating bzr repository and committing
# Congrats, your new project is setup! cd /tmp/test-project/ to start hacking.
# Creating project directory test-project

quickly create ubuntu-application test-project
# There is already a file or directory named test-project
# ERROR: pre_create command failed
# Aborting

quickly create ubuntu-application subdir/test-project
# Creating bzr repository and committing
# Congrats, your new project is setup! cd /tmp/subdir/test-project/ to start hacking.
# Creating project directory test-project
