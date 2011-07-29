#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
# Copyright 2009 Didier Roche
#
# This file is part of Quickly
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

import os
import sys
import gettext
from gettext import gettext as _

import quicklyconfig, tools

gettext.textdomain('quickly')

def show_version():
    """ print version information """

    try:
        quickly_data_path = tools.get_quickly_data_path()
    except tools.data_path_not_found, invalid_data_path:
        quickly_data_path = (_("No quickly data path found in %s.") % invalid_data_path)
    try:
        template_directories = "\n          ".join(tools.get_template_directories())
    except tools.template_path_not_found:
        template_directories = _("No template found.")
    
    print _("""Quickly %s
  Python interpreter: %s %s
  Python standard library: %s
  
  Quickly used library: %s
  Quickly data path: %s
  Quickly detected template directories:
          %s

Copyright 2009 Rick Spencer
Copyright 2009-2011 Didier Roche
Copyright 2010-2011 Michael Terry
https://launchpad.net/quickly

quickly comes with ABSOLUTELY NO WARRANTY. quickly is free software, and
you may use, modify and redistribute it under the terms of the GNU
General Public License version 3 or later.""") % (
    quicklyconfig.__version__, sys.executable, ".".join([str(x) for x in sys.version_info[0:3]]),
    os.path.dirname(os.__file__), os.path.dirname(__file__), quickly_data_path,
    template_directories)


