#!/usr/bin/python
#
# main.py
# Copyright (C) Daniel Neel 2011 <dneelyep@gmail.com>
# 
# guitar-tuner is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# guitar-tuner is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys
try:
    import gtk
except ImportError:
    sys.exit("pygtk not found.")

#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "data/guitar_tuner.ui"
#UI_FILE = "/usr/local/share/guitar_tuner/ui/guitar_tuner.ui"


class GUI:
    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file(UI_FILE)
        self.window = self.builder.get_object("window1")
        self.label = self.builder.get_object("label1")
        self.builder.connect_signals(self)
        
    def change_text(self, widget, *event):
        self.label.set_text("Hello, pygtk world!")

    def quit(self, widget, *event):
        gtk.main_quit()

def main():
    app = GUI()
    app.window.show()
    gtk.main()

if __name__ == "__main__":
    sys.exit(main())
