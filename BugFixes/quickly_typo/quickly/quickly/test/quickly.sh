#!/bin/sh

rm -fr /tmp/quickly-test

quickly quickly ubuntu-application
# ERROR: No destination template name provided.
# Usage: quickly quickly [origin-template] destination-template

export HOME=/tmp/quickly-test; quickly quickly ubuntu-application test-template
# Copy ubuntu-application to create new /tmp/quickly-test/quickly-templates/test-template template

export HOME=/tmp/quickly-test; quickly quickly ubuntu-application test-template
# /tmp/quickly-test/quickly-templates/test-template already exists.
# ERROR: quickly command failed
# Aborting

ls /tmp/quickly-test/quickly-templates/test-template -1F
# available_licenses/
# commandsconfig
# help/
# icons/
# internal/
# project_root/
# store/
# test/

cat /tmp/quickly-test/quickly-templates/test-template/commandsconfig
# # define parameters for commands, putting them in a list seperated
# # by ';'
# # if nothing specified, default is to launch command inside a project
# # only and not be followed by a template
# COMMANDS_LAUNCHED_IN_OR_OUTSIDE_PROJECT = tutorial
# COMMANDS_LAUNCHED_OUTSIDE_PROJECT_ONLY = create
# COMMANDS_FOLLOWED_BY_COMMAND = 
# COMMANDS_EXPOSED_IN_BAR = create;design;edit;package;release;save;share;tutorial
# 
# [ubuntu-application]
# IMPORT=add;configure;create;debug;design;edit;license;package;release;run;save;share;submitubuntu;test;tutorial;upgrade

diff -qr data/templates/ubuntu-application/available_licenses /tmp/quickly-test/quickly-templates/test-template/available_licenses

diff -qr data/templates/ubuntu-application/help /tmp/quickly-test/quickly-templates/test-template/help

diff -qr data/templates/ubuntu-application/icons /tmp/quickly-test/quickly-templates/test-template/icons

diff -qr data/templates/ubuntu-application/internal /tmp/quickly-test/quickly-templates/test-template/internal

diff -qr data/templates/ubuntu-application/project_root /tmp/quickly-test/quickly-templates/test-template/project_root

diff -qr data/templates/ubuntu-application/store /tmp/quickly-test/quickly-templates/test-template/store

diff -qr data/templates/ubuntu-application/test /tmp/quickly-test/quickly-templates/test-template/test
