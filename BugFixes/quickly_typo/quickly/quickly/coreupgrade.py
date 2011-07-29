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

# This file is for Core upgrade. Those operations should be reduce as few
# as possible as they are launched on each quickly invocation (even shell
# completion). Prefer template upgrade (see the upgrade.py command in
# ubuntu-application template). This is for cases when we need to ugprade
# something without lauching/having access to a template command.

# here is the first usage: template renaming and modifying .quickly file
# (of course, not possible in template upgrade as "ubuntu-project" no more exists

import configurationhandler

def upgrade():
    
    # change .quickly file before getting template access
    return_code = configurationhandler.loadConfig(can_stop=False)

    if return_code == 0:
        # rename ubuntu-project in ubuntu-application
        if configurationhandler.project_config['template'] == "ubuntu-project":
            configurationhandler.project_config['template'] = "ubuntu-application"
        configurationhandler.saveConfig()

