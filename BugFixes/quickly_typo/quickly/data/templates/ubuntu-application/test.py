#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
# Copyright 2011 Tony Byrne
#
# This file is part of Quickly ubuntu-application template
#
#This program is free software: you can redistribute it and/or modify it 
#under the terms of the GNU General Public License version 3, as published 
#by the Free Software Foundation.

#This program is distributed in the hope that it will be useful, but 
#WITHOUT ANY WARRANTY; without even the implied warranties of 
#MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
#PURPOSE.  See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along 
#with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys
import subprocess

import gettext
from gettext import gettext as _
gettext.textdomain('quickly')

from quickly import templatetools

def usage():
    templatetools.print_usage('quickly test')
def help():
    print _("""This command tests your project using the contents of the tests directory""")
templatetools.handle_additional_parameters(sys.argv, help, usage=usage)

#search and find all tests
command = ["nosetests"]
command.extend(sys.argv[1:])
return_code = subprocess.call(command)

sys.exit(return_code)

