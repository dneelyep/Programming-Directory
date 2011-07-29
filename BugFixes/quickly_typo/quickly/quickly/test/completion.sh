#!/bin/sh

quickly shell-completion
# ERROR: No command provided in command line
# Usage:
#     quickly [OPTIONS] command ...
# 
# Options:
#     -t, --template <template>  Template to use if it differs from default
#                                project template
#     --staging                  Target launchpad staging server
#     --verbose                  Verbose mode
#     -h, --help                 Show help information
# 
# Commands:
#     create <template> <project-name> (template is mandatory for this command)
#     quickly <template-origin> <template-dest> to create a create derived template
#     getstarted to get some starting hints
# 
# Examples:
#     quickly create ubuntu-application foobar
#     quickly push 'awesome new comment system'
#     quickly -t cool-template push 'awesome new comment system'

quickly shell-completion quickly
# ERROR: No command provided in command line
# Usage:
#     quickly [OPTIONS] command ...
# 
# Options:
#     -t, --template <template>  Template to use if it differs from default
#                                project template
#     --staging                  Target launchpad staging server
#     --verbose                  Verbose mode
#     -h, --help                 Show help information
# 
# Commands:
#     create <template> <project-name> (template is mandatory for this command)
#     quickly <template-origin> <template-dest> to create a create derived template
#     getstarted to get some starting hints
# 
# Examples:
#     quickly create ubuntu-application foobar
#     quickly push 'awesome new comment system'
#     quickly -t cool-template push 'awesome new comment system'

## The idea here is to 'depth-first' search completion results.  If we have a list of commands, we try the first one and then again iterate its completion results until we get an empty result.  We also try several different ways of providing templates to commands.

## The use of the word 'foo' is to mark where shell-completion is trying to complete

quickly shell-completion quickly -
# --help --staging --template --verbose --version -h -t

HOME=/ quickly shell-completion quickly -t foo
# ubuntu-application ubuntu-cli ubuntu-flash-game ubuntu-pygame

quickly shell-completion quickly foo
# commands create getstarted help quickly tutorial

## This next one doesn't actually list all the commands, because quickly also checks if we're in a project and thus whether such commands would actually work

quickly shell-completion quickly -t ubuntu-pygame foo
# commands create getstarted help quickly tutorial

quickly shell-completion quickly commands foo
# 

HOME=/ quickly shell-completion quickly create foo
# ubuntu-application ubuntu-cli ubuntu-flash-game ubuntu-pygame

quickly shell-completion quickly create ubuntu-application foo
# 

quickly shell-completion quickly getstarted foo
# 

HOME=/ quickly shell-completion quickly help foo
# commands getstarted help quickly ubuntu-application ubuntu-cli ubuntu-flash-game ubuntu-pygame

quickly shell-completion quickly help commands foo
# 

quickly shell-completion quickly -t ubuntu-application help foo
# add commands configure create debug design edit getstarted help license package quickly release run save share submitubuntu test tutorial upgrade

quickly shell-completion quickly help ubuntu-application foo
# add commands configure create debug design edit getstarted help license package quickly release run save share submitubuntu test tutorial upgrade

quickly shell-completion quickly help ubuntu-application add foo
# 

HOME=/ quickly shell-completion quickly quickly foo
# ubuntu-application ubuntu-cli ubuntu-flash-game ubuntu-pygame

quickly shell-completion quickly quickly -t ubuntu-application foo
# 

quickly shell-completion quickly quickly ubuntu-application foo
# 

HOME=/ quickly shell-completion quickly tutorial foo
# ubuntu-application ubuntu-pygame

quickly shell-completion quickly -t ubuntu-application tutorial foo
# 

quickly shell-completion quickly tutorial ubuntu-application foo
# 

## Now do most of that over again, but inside a project

cd /tmp

rm -fr test-project

quickly create ubuntu-application test-project
# Creating bzr repository and committing
# Congrats, your new project is setup! cd /tmp/test-project/ to start hacking.
# Creating project directory test-project

cd test-project

quickly shell-completion quickly -
# --help --staging --template --verbose --version -h -t

HOME=/ quickly shell-completion quickly -t foo
# ubuntu-application ubuntu-cli ubuntu-flash-game ubuntu-pygame

quickly shell-completion quickly foo
# add commands configure debug design edit getstarted help license package quickly release run save share submitubuntu test tutorial upgrade

quickly shell-completion quickly -t ubuntu-pygame foo
# commands configure debug edit getstarted help license package quickly release run save share test tutorial

quickly shell-completion quickly add foo
# dialog help-guide help-topic indicator

quickly shell-completion quickly add dialog foo
# 

quickly shell-completion quickly add indicator foo
# 

quickly shell-completion quickly commands foo
# 

quickly shell-completion quickly configure foo
# bzr dependencies lp-project ppa target-distribution

quickly shell-completion quickly configure bzr foo
# 

quickly shell-completion quickly configure dependencies foo
# 

quickly shell-completion quickly configure lp-project foo
# 

## For this one, we provide an actual string to finish completing, to help make the results consistent between users

quickly shell-completion quickly configure ppa quickly/
# quickly/daily-build quickly/ppa

quickly shell-completion quickly configure target-distribution foo
# 

quickly shell-completion quickly debug foo
# 

quickly shell-completion quickly design foo
# 

quickly shell-completion quickly edit foo
# 

quickly shell-completion quickly getstarted foo
# 

HOME=/ quickly shell-completion quickly help foo
# add commands configure create debug design edit getstarted help license package quickly release run save share submitubuntu test tutorial upgrade

quickly shell-completion quickly help commands foo
# 

quickly shell-completion quickly -t ubuntu-application help foo
# add commands configure create debug design edit getstarted help license package quickly release run save share submitubuntu test tutorial upgrade

quickly shell-completion quickly help ubuntu-application foo
# add commands configure create debug design edit getstarted help license package quickly release run save share submitubuntu test tutorial upgrade

quickly shell-completion quickly help ubuntu-application add foo
# 

quickly shell-completion quickly license foo
# Apache-2.0 BSD GPL-2 GPL-3 LGPL-2 LGPL-3 MIT

quickly shell-completion quickly license MIT foo
# 

quickly shell-completion quickly package foo
# 

quickly shell-completion quickly quickly foo
# 

quickly shell-completion quickly quickly -t ubuntu-application foo
# 

quickly shell-completion quickly quickly ubuntu-application foo
# 

quickly shell-completion quickly release -
# --help --ppa --staging --template --verbose --version -h -t

quickly shell-completion quickly release --ppa quickly/
# quickly/daily-build quickly/ppa

quickly shell-completion quickly release foo
# 

quickly shell-completion quickly run foo
# 

quickly shell-completion quickly save foo
# 

quickly shell-completion quickly share -
# --help --ppa --staging --template --verbose --version -h -t

quickly shell-completion quickly share --ppa quickly/
# quickly/daily-build quickly/ppa

quickly shell-completion quickly share foo
# 

quickly shell-completion quickly tutorial foo
# 

quickly shell-completion quickly -t ubuntu-application tutorial foo
# 

quickly shell-completion quickly tutorial ubuntu-application foo
# 

quickly shell-completion quickly upgrade foo
# 
