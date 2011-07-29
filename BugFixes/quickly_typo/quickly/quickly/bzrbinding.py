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

import socket
import subprocess

import gettext
from gettext import gettext as _
gettext.textdomain('quickly')

def bzr_set_login(display_name, preferred_email_adress, launchpad_name=None):
    ''' try to setup bzr whoami for commit and sshing and bzr launchpad_login if provided

        launchpadname is optional if you don't want user to use launchpad in your template
        if already setup, it will not overwrite existing data
    '''

    try:

        # retreive the current bzr login
        bzr_instance = subprocess.Popen(["bzr", "whoami"], stdout=subprocess.PIPE)
        bzr_user, err = bzr_instance.communicate()
        if bzr_instance.returncode != 0:
            return (1, err)

        # if no bzr whoami set, the default contain the @hostname string
        if '@' + socket.gethostname() in bzr_user:
            identifier = display_name + ' <' + preferred_email_adress + '>'
            subprocess.call(["bzr", "whoami", identifier])

        # if no bzr launchpad-login set, set it now !
        if launchpad_name:
            bzr_instance = subprocess.Popen(["bzr", "launchpad-login"], stdout=subprocess.PIPE)
            bzr_id, err = bzr_instance.communicate()
            if bzr_instance.returncode == 1: # no user configured
                subprocess.call(["bzr", "launchpad-login", launchpad_name])
            elif bzr_instance.returncode != 0: # other errors
                return (1, err)

    except OSError:
        return (1, _("Bzr not properly installed"))
    
    return (0, "")

