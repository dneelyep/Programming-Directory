# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Gettings Things Gnome! - a personal organizer for the GNOME desktop
# Copyright (c) 2008-2009 - Lionel Dricot & Bertrand Rousseau
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------


"""
The core functionality GTG.

In order to not interact directly with the datastore, we provide
"requesters".  The requester is only an interface and there can be as
many requester as you want as long as they are all from the same
datastore.  Requester also provides an interface for the tagstore

If you want to display only a subset of tasks, you can either:

 - have access to the main FilteredTree (the one displayed in the main
   window) and apply filters on it.  (You can create your own)

 - get your own personal FilteredTree and apply on it the filters you
   want without interfering with the main view. (This is how the closed
   tasks pane is built currently)

"""


#=== IMPORT ====================================================================
import os
from xdg.BaseDirectory import xdg_data_home, xdg_config_home
from configobj         import ConfigObj
from GTG.tools.testingmode import TestingMode

import GTG
from GTG.tools.logger import Log
from GTG.tools.borg   import Borg


DEFAULTS = {
'browser': {
            'bg_color_enable' : False,
            "contents_preview_enable" : False,
            'tag_pane' : False,
            "sidebar_width": 120,
            "closed_task_pane" : False,
            'bottom_pane_position' : 300,
            'toolbar' : True,
            'quick_add' : True,
            "bg_color_enable": True,
            'collapsed_tasks' : [],
            'collapsed_tags' : [],
            'view' : 'default',
            "opened_tasks": [],
            'width': 400,
            'height':400,
            'x_pos':10,
            'y_pos':10,
            }
}


#Instead of accessing directly the ConfigObj dic, each module will have
#one SubConfig object. (one SubConfig object always match one first level
#element of the ConfigObj directory)
#
#The goal of the SubConfig object is to handle default value and converting
#String to Bool and Int when needed. 
#
#Each GTG component using config should be ported to SubConfig and, for each
#setting, a default value should be written in the DEFAULTS above.
#
#Currently done : browser
#Todo : editor, plugins
class SubConfig():
    def __init__(self,name,conf_dic):
        self.__name = name
        self.__conf = conf_dic
        if DEFAULTS.has_key(name):
            self.__defaults = DEFAULTS[name]
        else:
            self.__defaults = {}
        
    #This return the value of the setting (or the default one)
    #
    #If a default value exists and is a Int or a Bool, the returned
    #value is converted to that type.
    def get(self,name):
        if self.__conf.has_key(name):
            toreturn = self.__conf[name]
            #Converting to the good type
            if self.__defaults.has_key(name):
                ntype = type(self.__defaults[name])
                if ntype in (bool,int) and type(toreturn) == str:
                    toreturn = eval(toreturn)
        elif self.__defaults.has_key(name):
            toreturn = self.__defaults[name]
            self.__conf[name] = toreturn
        else:
            print "Warning : no default conf value for %s in %s" %(name,self.__name)
            toreturn = None
        return toreturn 
    
    def set(self,name,value):
        self.__conf[name] = str(value)



class CoreConfig(Borg):
    #The projects and tasks are of course DATA !
    #We then use XDG_DATA for them
    #Don't forget the "/" at the end.
    DATA_FILE = "projects.xml"
    CONF_FILE = "gtg.conf"
    TASK_CONF_FILE = "tasks.conf"
    conf_dict = None
    #DBUS
    BUSNAME = "org.gnome.GTG"
    BUSINTERFACE = "/org/gnome/GTG"
    #TAGS
    ALLTASKS_TAG = "gtg-tags-all"
    NOTAG_TAG = "gtg-tags-none"
    SEP_TAG = "gtg-tags-sep"

    def __init__(self):
        if  hasattr(self, 'data_dir'):
            #Borg has already been initialized
            return
        if TestingMode().get_testing_mode():
            #we avoid running tests in the user data dir
            self.data_dir = '/tmp/GTG_TESTS/data'
            self.conf_dir = '/tmp/GTG_TESTS/conf'
        else:
            self.data_dir = os.path.join(xdg_data_home,'gtg/')
            self.conf_dir = os.path.join(xdg_config_home,'gtg/')
        if not os.path.exists(self.conf_dir):
            os.makedirs(self.conf_dir)
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        if not os.path.exists(self.conf_dir + self.CONF_FILE):
            f = open(self.conf_dir + self.CONF_FILE, "w")
            f.close()
        if not os.path.exists(self.conf_dir + self.TASK_CONF_FILE):
            f = open(self.conf_dir + self.TASK_CONF_FILE, "w")
            f.close()
        for file in [self.conf_dir + self.CONF_FILE,
                     self.conf_dir + self.TASK_CONF_FILE]:
            if not ((file, os.R_OK) and os.access(file, os.W_OK)):
                raise Exception("File " + file + \
                            " is a configuration file for gtg, but it "
                            "cannot be read or written. Please check it")
        self.conf_dict = ConfigObj(self.conf_dir + self.CONF_FILE)
        self.task_conf_dict = ConfigObj(self.conf_dir + self.TASK_CONF_FILE)
    
    def save(self):
        ''' Saves the configuration of CoreConfig '''
        self.conf_dict.write()
        self.task_conf_dict.write()
        
    def get_subconfig(self,name):
        if not self.conf_dict.has_key(name):
            self.conf_dict[name] = {}
        return SubConfig(name,self.conf_dict[name])

    def get_icons_directories(self):
        '''
        Returns the directories containing the icons
        '''
        return [GTG.DATA_DIR, os.path.join(GTG.DATA_DIR, "icons")]

    def get_data_dir(self):
        return self.data_dir

    def set_data_dir(self, path):
        self.data_dir = path

    def get_conf_dir(self):
        return self.conf_dir

    def set_conf_dir(self, path):
        self.conf_dir = path
