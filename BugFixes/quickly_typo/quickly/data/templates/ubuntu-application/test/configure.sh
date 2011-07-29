#!/bin/sh

cd /tmp

rm -rf test-project

quickly create ubuntu-application test-project
# Creating bzr repository and committing
# Congrats, your new project is setup! cd /tmp/test-project/ to start hacking.
# Creating project directory test-project

cd test-project

## Test configure lp-project

grep url= setup.py
#     #url='https://launchpad.net/test-project',

grep website data/ui/AboutTestProjectDialog.ui
#     <property name="website"></property>

grep lp_id .quickly

quickly configure lp-project gpoweroff
# Get Launchpad Settings
# Launchpad connection is ok
# Creating new apport crashdb configuration
# Creating new apport hooks

grep lp_id .quickly
# lp_id = gpoweroff

grep url= setup.py
#     url='https://launchpad.net/gpoweroff',

grep website data/ui/AboutTestProjectDialog.ui
#     <property name="website">https://launchpad.net/gpoweroff</property>

(echo hudson-notifier > tmp)

quickly configure lp-project < tmp
# Get Launchpad Settings
# Launchpad connection is ok
# Updating project name references in existing apport crashdb configuration

grep lp_id .quickly
# lp_id = hudson-notifier

grep url= setup.py
#     url='https://launchpad.net/hudson-notifier',

grep website data/ui/AboutTestProjectDialog.ui
#     <property name="website">https://launchpad.net/hudson-notifier</property>

## Test configure bzr

quickly configure bzr
# Usage: quickly configure bzr <bzr-branch-string>

quickly configure bzr 1 2
# Usage: quickly configure bzr <bzr-branch-string>

grep bzrbranch .quickly

quickly configure bzr lp:gpoweroff

grep bzrbranch .quickly
# bzrbranch = lp:gpoweroff

quickly configure bzr lp:hudson-notifier

grep bzrbranch .quickly
# bzrbranch = lp:hudson-notifier

## Test configure target_distribution

quickly configure target_distribution
# Usage: quickly configure target-distribution <ubuntu-release-name>

quickly configure target_distribution 1 2
# Usage: quickly configure target-distribution <ubuntu-release-name>

grep target_distribution .quickly

## For the eventual Quickly Quetzal release (note that we test both underscore and dash for this command)

quickly configure target_distribution quickly

grep target_distribution .quickly
# target_distribution = quickly

quickly configure target-distribution slowly

grep target_distribution .quickly
# target_distribution = slowly

## Test configure dependencies

grep dependencies .quickly

(echo -e one, potato \\n two potato > tmp)

quickly configure dependencies < tmp

grep dependencies .quickly
# dependencies = one, potato, two potato

(echo blarg > tmp)

quickly configure dependencies < tmp

grep dependencies .quickly
# dependencies = blarg

## test configure ppa

quickly configure ppa
# Usage: quickly configure ppa <ppa-name>
# 
# Use shell completion to find all available PPAs

quickly configure ppa 1 2
# Usage: quickly configure ppa <ppa-name>
# 
# Use shell completion to find all available PPAs

quickly configure ppa quickly-does-not-exist/does-not-exist
# Get Launchpad Settings
# Launchpad connection is ok
# User or team quickly-does-not-exist not found on Launchpad
# ERROR: configure command failed
# Aborting

quickly configure ppa bug-watch-updater/does-not-exist
# Get Launchpad Settings
# Launchpad connection is ok
# You have to be a member of bug-watch-updater team to upload to its PPAs
# ERROR: configure command failed
# Aborting

quickly configure ppa quickly/does-not-exist
# Get Launchpad Settings
# Launchpad connection is ok
# ppa:quickly:does-not-exist does not exist. Please create it on launchpad if you want to upload to it. quickly has the following PPAs available:
# daily-build - Daily build
# ppa - quickly
# ERROR: configure command failed
# Aborting

grep ppa .quickly

quickly configure ppa quickly/ppa
# Get Launchpad Settings
# Launchpad connection is ok

grep ppa .quickly
# ppa = quickly/ppa

quickly configure ppa quickly/daily-build
# Get Launchpad Settings
# Launchpad connection is ok

grep ppa .quickly
# ppa = quickly/daily-build
