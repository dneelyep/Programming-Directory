#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

import nautilus
import pygtk
import gtk
import vte

try:
    from quickly import api as quicklyapi
    #from quickly import prompts
    has_quickly = True
except:
    has_quickly = False

command_order = ('create', 'edit', 'design', 'save', 'package', 'share', 'release', 'tutorial')
command_without_output = ('edit', 'design', 'save', 'tutorial')

class DevBar(nautilus.LocationWidgetProvider):
    pass
    def __init__(self):
        self.bars = {}
        pass

    def get_widget(self, uri, window):
        """Draw Ubuntu dev widgets depending on context

        if Quickly:
           - draw available actions in Quickly project
           - draw available actions outside of Quickly project in dev directory"""

        uri = uri.replace('file://', '')

        if has_quickly:
            commands = [command for command in
                        quicklyapi.get_commands_in_context(path=uri)
                        if command.exposed_in_bar == True] 
            fingerprint = "".join([command.name for command in commands])
            try:
                bar = self.bars[fingerprint]
            except KeyError:
                bar = UbuntuDevBar(spacing=30)
                # Don't load when I uncomment the cache! WTF happened???
                #self.bars[fingerprint] = bar
                current_template = None
                current_template = quicklyapi.get_current_template(path=uri)
                if not current_template:
                    current_template = ""
                sorted_commands = []
                # reorder commands
                for item in command_order:
                    for command in commands:
                        if item == command.name:
                            sorted_commands.append(command)
                for command in commands:
                    if command.name not in command_order:
                        sorted_commands.append(command)
                
                bar.add_image("/usr/share/quickly/icons/quickly48x48.png", current_template)
                commands_already_listed = []
                for command in sorted_commands:
                    if command.name in commands_already_listed:
                        continue
                    if command.followed_by_template and not current_template:
                        bar.add_button_with_selection(bar.click_on_quickly_button, command.name, quicklyapi.list_template_for_command(command.name), ["quickly", command.name], uri, icon=command.icon)
                    else:
                        bar.add_button(bar.click_on_quickly_button, command.name, ["quickly", command.name], uri, icon=command.icon)
                    commands_already_listed.append(command.name)
                bar.show()
        
        if not ('devel' in uri or current_template):
            return
        return bar


class UbuntuDevBar(gtk.HBox):
    '''Container to all buttons in nautilus.'''

    def __init__(self, *args, **kwargs):
        '''create a Ubuntu Dev Bar'''
        super(UbuntuDevBar, self).__init__(*args, **kwargs)
        self._logo = None
        self._image = None
        self._subtitle = None
        self._buttons = []
        self._buttons_with_selection = []

    def add_image(self, image_name, subtitle=None):
        """Add an image to the bar and a subtitle below if one."""
        self._logo = gtk.VBox(homogeneous=False, spacing=0)
        self._image = gtk.Image()
        self._logo.pack_start(self._image, expand=True, fill=True, padding=0)
        pixbuf = gtk.gdk.pixbuf_new_from_file(image_name)
        if pixbuf:
            scaled_pixbuf = pixbuf.scale_simple(48, 48, gtk.gdk.INTERP_BILINEAR)
            self._image.set_from_pixbuf(scaled_pixbuf)
            self._image.show()
        if subtitle:
            self._subtitle = gtk.Label(subtitle)
            self._logo.pack_start(self._subtitle, expand=True, fill=True, padding=0)
            self._subtitle.show()
        self.pack_start(self._logo, expand=False, fill=False, padding=0)
        self._logo.show()

    def add_button(self, signal, label, command_line, path, icon=None):
        """Adds a new new button to the bar widget."""
        button = gtk.Button()
        button.connect("clicked", signal, command_line, path)
        button.set_label(label)
        if icon:
            image = gtk.Image()
            image.set_from_file(icon)
            settings = button.get_settings()
            settings.set_property("gtk-button-images", True)
            button.set_image(image)
        button.show()
        vbox = gtk.VBox(homogeneous=False, spacing=0)
        vbox.pack_start(button, expand=True, fill=False, padding=0)
        vbox.show()
        self._buttons.append(button)
        self.pack_start(vbox, expand=False, fill=False, padding=0)

    def add_button_with_selection(self, signal, label, selection, command_line,
                                  path, icon=None):
        """Adds a new button with a multiple selection widget"""
        combobox = gtk.combo_box_new_text()
        for item in selection:
            combobox.append_text(item)
        combobox.show()
        button = gtk.Button()
        button.set_label(label)
        button.connect("clicked", signal, command_line, path, combobox)
        if icon:
            image = gtk.Image()
            image.set_from_file(icon)
            settings = button.get_settings()
            settings.set_property("gtk-button-images", True)
            button.set_image(image)
        button.show()
        vbox = gtk.VBox(homogeneous=False, spacing=0)
        vbox.pack_start(combobox, expand=True, fill=False, padding=0)
        vbox.pack_start(button, expand=True, fill=False, padding=0)
        self._buttons_with_selection.append((combobox,button))
        vbox.show()
        self.pack_start(vbox, expand=False, fill=False, padding=0)

    def click_on_quickly_button(self, widget, *argscommand):
        """Quickly buttons can have a template associated"""

        command = argscommand[0]
        try:
            associated_combobox = argscommand[2]
            model = associated_combobox.get_model()
            index = associated_combobox.get_active()
            if index >= 0:
                command.insert(2, "-t")
                command.insert(3, model[index][0])
        except IndexError:
            pass
        command = self.add_additional_actions(command)
        v = vte.Terminal()
        v.fork_command(command[0], argv=command, directory=argscommand[1])
        window = gtk.Window()
        window.add(v)
        if command[1] not in command_without_output:
            window.show_all()
        gtk.main()

    def add_additional_actions(self, command):
        """Some commands needs additional args, filter them here"""

        # TODO: Add missing prompts module
        #if command[1] == "create":
        #    response, val = prompts.string("Project Name","Please enter a project name")
        #    if response == gtk.RESPONSE_OK:
        #        command.append(val)

        return command
