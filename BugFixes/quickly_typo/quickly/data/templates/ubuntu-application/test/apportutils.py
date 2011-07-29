#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import unittest

import os
import sys
import StringIO
from lxml import etree

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","..","..")))

from internal import apportutils

class TestApportUtils(unittest.TestCase):
    def test_lpi_existing(self):
        lines = """#!/usr/bin/python
import sys
import os
import gtk
import gettext
from gettext import gettext as _
gettext.textdomain('project_name')

# optional Launchpad integration
# this shouldn't crash if not found as it is simply used for bug reporting
try:
    import LaunchpadIntegration
    launchpad_available = True
except:
    launchpad_available = False        
        
class camel_case_nameWindow(gtk.Window):
    __gtype_name__ = "camel_case_nameWindow"

    def __init__(self):
        pass

    def finish_initializing(self, builder):
        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.builder.connect_signals(self)

        if launchpad_available:
            # see https://wiki.ubuntu.com/UbuntuDevelopment/Internationalisation/Coding for more information
            # about LaunchpadIntegration
            LaunchpadIntegration.set_sourcepackagename('project_name')
            LaunchpadIntegration.add_items(self.builder.get_object('helpMenu'), 1, True, True)
            
    def about(self, widget, data=None):
        about = Aboutcamel_case_nameDialog.NewAboutcamel_case_nameDialog()
        response = about.run()
        about.destroy()
""".splitlines()
        self.failIf(apportutils.detect_or_insert_lpi(lines, "project_name1", "helpMenu1"))

    def test_partial_lpi_import_only(self):
        lines = """#!/usr/bin/python
import sys
import os
import gtk
import gettext
from gettext import gettext as _
gettext.textdomain('project_name')

# optional Launchpad integration
# this shouldn't crash if not found as it is simply used for bug reporting
try:
    import LaunchpadIntegration
    launchpad_available = True
except:
    launchpad_available = False        
        
class camel_case_nameWindow(gtk.Window):
    __gtype_name__ = "camel_case_nameWindow"

    def __init__(self):
        pass

    def finish_initializing(self, builder):
        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.builder.connect_signals(self)
            
    def about(self, widget, data=None):
        about = Aboutcamel_case_nameDialog.NewAboutcamel_case_nameDialog()
        response = about.run()
        about.destroy()
""".splitlines()
        self.failIf(apportutils.detect_or_insert_lpi(lines, "project_name1", "helpMenu1"))

    def test_no_lpi(self):
        lines = """#!/usr/bin/python
import sys
import os
import gtk
import gettext
from gettext import gettext as _
gettext.textdomain('project_name')
       
class camel_case_nameWindow(gtk.Window):
    __gtype_name__ = "camel_case_nameWindow"

    def __init__(self):
        pass

    def finish_initializing(self, builder):
        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.builder.connect_signals(self)
            
    def about(self, widget, data=None):
        about = Aboutcamel_case_nameDialog.NewAboutcamel_case_nameDialog()
        response = about.run()
        about.destroy()
""".splitlines(True)
        expected = """#!/usr/bin/python
import sys
import os
import gtk
import gettext
from gettext import gettext as _
gettext.textdomain('project_name')
       
class camel_case_nameWindow(gtk.Window):
    __gtype_name__ = "camel_case_nameWindow"

    def __init__(self):
        pass

    def finish_initializing(self, builder):
        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.builder.connect_signals(self)

        # Optional Launchpad integration
        # This shouldn't crash if not found as it is simply used for bug reporting.
        # See https://wiki.ubuntu.com/UbuntuDevelopment/Internationalisation/Coding
        # for more information about Launchpad integration.
        try:
            import LaunchpadIntegration
            LaunchpadIntegration.add_items(self.ui.helpMenu1, 1, True, True)
            LaunchpadIntegration.set_sourcepackagename('project_name1')
        except:
            pass
            
    def about(self, widget, data=None):
        about = Aboutcamel_case_nameDialog.NewAboutcamel_case_nameDialog()
        response = about.run()
        about.destroy()
"""
        # print "".join(apportutils.detect_or_insert_lpi(lines, "project_name1", "helpMenu1"))
        # print "".join(expected.splitlines(True))
        self.assertEqual("".join(expected.splitlines(True)).strip(), "".join(apportutils.detect_or_insert_lpi(lines, "project_name1", "helpMenu1")).strip())

    def test_find_about_menu(self):
        xml_tree = etree.parse(StringIO.StringIO("""<?xml version="1.0"?>
<interface>
  <requires lib="gtk+" version="2.16"/>
  <!-- interface-requires python_name_window 1.0 -->
  <!-- interface-naming-policy project-wide -->
  <!-- interface-local-resource-path ../media -->
  <object class="camel_case_nameWindow" id="python_name_window">
    <property name="title" translatable="yes">sentence_name</property>
    <property name="icon">../media/project_name.svg</property>
    <signal name="destroy" handler="on_destroy"/>
    <child>
      <object class="GtkVBox" id="vbox1">
        <property name="visible">True</property>
        <property name="orientation">vertical</property>
        <property name="spacing">5</property>
        <child>
          <object class="GtkMenuBar" id="menubar1">
            <property name="visible">True</property>
            <child>
              <object class="GtkMenuItem" id="menuitem4">
                <property name="visible">True</property>
                <property name="label" translatable="yes">_Help</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="testHelpMenu">
                    <property name="visible">True</property>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem10">
                        <property name="label">gtk-about</property>
                        <property name="visible">True</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                        <signal name="activate" handler="about"/>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="position">0</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>"""))
        self.assertEqual("testHelpMenu", apportutils.find_about_menu(xml_tree))

unittest.main()
