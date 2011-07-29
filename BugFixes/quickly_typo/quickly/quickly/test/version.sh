#!/bin/sh

## We strip a lot of this out so that it can pass in any directory/with any python

quickly --version | sed 's|: /.*||g' | sed '/.*templates\/\?/d' | VER=$(grep 'VERSION = ' setup.py | sed "s/.*'\(.*\)'/\1/") sh -c 'sed "s/^Quickly $VER/Quickly X.X.X/"'
# Quickly X.X.X
#   Python interpreter
#   Python standard library
#   
#   Quickly used library
#   Quickly data path
#   Quickly detected template directories:
# 
# Copyright 2009 Rick Spencer
# Copyright 2009-2011 Didier Roche
# Copyright 2010-2011 Michael Terry
# https://launchpad.net/quickly
# 
# quickly comes with ABSOLUTELY NO WARRANTY. quickly is free software, and
# you may use, modify and redistribute it under the terms of the GNU
# General Public License version 3 or later.
