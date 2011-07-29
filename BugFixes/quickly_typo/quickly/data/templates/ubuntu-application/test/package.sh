#!/bin/sh

cd /tmp

rm -rf test-project*

quickly create ubuntu-application test-project
# Creating bzr repository and committing
# Congrats, your new project is setup! cd /tmp/test-project/ to start hacking.
# Creating project directory test-project

cd test-project

bzr status

ls debian
# ls: cannot access debian: No such file or directory

quickly package | sed 's/^\.\+//'
# Ubuntu packaging created in debian/
# Ubuntu package has been successfully created in ../test-project_0.1_all.deb

bzr status
# modified:
#   test-project.desktop.in
# unknown:
#   po/

bzr diff --diff-options="-e"
# === modified file 'test-project.desktop.in'
# 6c
# Icon=/usr/share/test-project/media/test-project.svg
# .
# 

ls debian
# changelog
# compat
# control
# copyright
# rules

ls ../test-project_0.1.dsc ../test-project_0.1.tar.gz ../test-project_0.1_all.deb
# ../test-project_0.1.dsc
# ../test-project_0.1.tar.gz
# ../test-project_0.1_all.deb

grep UNKNOWN debian/*
# debian/control:Maintainer: UNKNOWN <UNKNOWN>
# debian/control:Description: UNKNOWN
# debian/control: UNKNOWN
# debian/copyright:Maintainer: UNKNOWN <UNKNOWN>
# debian/copyright:Source: UNKNOWN
# debian/copyright:License: UNKNOWN

(echo "Copyright (C) 2010 Oliver Twist <twist@example.com>" > AUTHORS)

quickly license GPL-3

sed -i "s/#author=.*,/author='Oliver Twist',/" setup.py

sed -i "s/#author_email=.*,/author_email='twist@example.com',/" setup.py

sed -i "s/#description=.*,/description='My super cool project',/" setup.py

sed -i "s/#long_description=.*,/long_description='This project will rock your socks',/" setup.py

sed -i "s|#url=.*,|url='http://example.com/test-project',|" setup.py

quickly package | sed 's/^\.\+//'
# Ubuntu packaging created in debian/
# Ubuntu package has been successfully created in ../test-project_0.1_all.deb

grep UNKNOWN debian/*

## Now we want to verify that we set project variables correctly

mkdir unpacked

cd unpacked

ar p ../../test-project_0.1_all.deb data.tar.gz | tar xz

grep -Rh "__version__ = " .
# __version__ = '0.1'

grep -Rh "__test_project_data_directory__ = " .
# __test_project_data_directory__ = '/usr/share/test-project/'
