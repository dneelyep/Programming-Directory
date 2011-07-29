# -*- coding: utf-8 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import sys
import os
import gtk

from daerot.daerotconfig import getdatapath

class AboutDaerotDialog(gtk.AboutDialog):
    __gtype_name__ = "AboutDaerotDialog"

    def __init__(self):
        """__init__ - This function is typically not called directly.
        Creation of a AboutDaerotDialog requires redeading the associated ui
        file and parsing the ui definition extrenally, 
        and then calling AboutDaerotDialog.finish_initializing().
    
        Use the convenience function NewAboutDaerotDialog to create 
        NewAboutDaerotDialog objects.
    
        """
        pass

    def finish_initializing(self, builder):
        """finish_initalizing should be called after parsing the ui definition
        and creating a AboutDaerotDialog object with it in order to finish
        initializing the start of the new AboutDaerotDialog instance.
    
        """
        #get a reference to the builder and set up the signals
        self.builder = builder
        self.builder.connect_signals(self)

        #code for other initialization actions should be added here

def NewAboutDaerotDialog():
    """NewAboutDaerotDialog - returns a fully instantiated
    AboutDaerotDialog object. Use this function rather than
    creating a AboutDaerotDialog instance directly.
    
    """

    #look for the ui file that describes the ui
    ui_filename = os.path.join(getdatapath(), 'ui', 'AboutDaerotDialog.ui')
    if not os.path.exists(ui_filename):
        ui_filename = None

    builder = gtk.Builder()
    builder.add_from_file(ui_filename)    
    dialog = builder.get_object("about_daerot_dialog")
    dialog.finish_initializing(builder)
    return dialog

if __name__ == "__main__":
    dialog = NewAboutDaerotDialog()
    dialog.show()
    gtk.main()

