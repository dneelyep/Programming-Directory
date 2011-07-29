# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('jotty')

import gtk
import logging
logger = logging.getLogger('jotty')

from jotty_lib import Window
from jotty.AboutJottyDialog import AboutJottyDialog
from jotty.PreferencesJottyDialog import PreferencesJottyDialog

from desktopcouch.records.server import CouchDatabase
from desktopcouch.records.record import Record

# pylint: disable=E1002,E1101

# See jotty_lib.Window.py for more details about how this class works
class JottyWindow(Window):
    __gtype_name__ = "JottyWindow"
    
    def finish_initializing(self, builder):
        """Set up the main window"""
        super(JottyWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutJottyDialog
        self.PreferencesDialog = PreferencesJottyDialog

        # Code for other initialization actions should be added here.
        self.database = CouchDatabase("jotty", create=True)

    def on_mnu_save_activate(self, widget, data=None):
        #get the title for the note
        title = self.ui.entry1.get_text()

        #get the string
        buff = self.ui.textview1.get_buffer()
        start_iter = buff.get_start_iter()
        end_iter = buff.get_end_iter()
        text = buff.get_text(start_iter,end_iter)

        #get all the records
        record_type = "http://wiki.ubuntu.com/Quickly/JottyDoc"
        results = self.database.get_records(record_type = record_type, create_view = True)

        #update a record that has the same title
        for result in results:
            document = result.value
            if document["title"] == title:
                key = document["_id"]
                self.database.update_fields(key, {"text":text})
                return

        #if no records had the title, create it 
        new_rec = Record({"record_type":record_type, "title":title, "text":text})
        self.database.put_record(new_rec)

    def on_mnu_open_activate(self, widget, data=None):
        #get the name of the document to open
        title = self.ui.entry1.get_text()
        text = ""
 
        #get all the records
        record_type = "http://wiki.ubuntu.com/Quickly/JottyDoc"
        results = self.database.get_records(record_type = record_type,create_view = True)
 
        #get the text if there is a matching title
        for result in results:
            document = result.value
            if document["title"] == title:
                text = document["text"]

        #set the UI to display the string
        buff = self.ui.textview1.get_buffer()
        buff.set_text(text)

    def on_mnu_new_activate(self, widget, data=None):
        self.ui.entry1.set_text("Note Title")
        buff = self.ui.textview1.get_buffer()
        buff.set_text("")
