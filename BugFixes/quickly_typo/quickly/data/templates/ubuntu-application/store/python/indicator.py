#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

"""Code to add AppIndicator."""

import gtk

from python_name_lib.helpers import get_media_file

import gettext
from gettext import gettext as _
gettext.textdomain('project_name')

import appindicator

class Indicator:
    def __init__(self, window):
        self.indicator = appindicator.Indicator('project_name','distributor-logo',appindicator.CATEGORY_APPLICATION_STATUS)
        self.indicator.set_status(appindicator.STATUS_ACTIVE)
    
        #Can use self.icon once appindicator python api supports custom icons.
        #icon = get_media_file("project_name.svg")
        #self.indicator.set_icon(icon)
 
        #Uncomment and choose an icon for attention state. 
        #self.indicator.set_attention_icon("ICON-NAME")
        
        self.menu = gtk.Menu()

        # Add items to Menu and connect signals.
        
        #Adding preferences button 
        #window represents the main Window object of your app
        self.preferences = gtk.MenuItem("Preferences")
        self.preferences.connect("activate",window.on_mnu_preferences_activate)
        self.preferences.show()
        self.menu.append(self.preferences)

        self.quit = gtk.MenuItem("Quit")
        self.quit.connect("activate",window.on_mnu_close_activate)
        self.quit.show()
        self.menu.append(self.quit)

        # Add more items here                           

        self.menu.show()
        self.indicator.set_menu(self.menu)
    
def new_application_indicator(window):
    ind = Indicator(window)
    return ind.indicator
