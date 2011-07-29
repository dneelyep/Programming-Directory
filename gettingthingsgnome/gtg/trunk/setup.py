#!/usr/bin/env python
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

from distutils.core     import setup
from distutils.command.install_data import install_data
from subprocess import call

import glob
import os

from GTG import info

### CONSTANTS ################################################################

DATA_DIR        = "share/gtg"
GLOBAL_ICON_DIR = "share/icons/hicolor"

### TOOLS ####################################################################

def create_icon_list():
    fileList = []
    rootdir  = "data/icons"
    for root, subFolders, files in os.walk(rootdir):
        dirList = []
        for file in files:
            if file.endswith(".png") or file.endswith(".svg"):
                dirList.append(os.path.join(root, file))
        if len(dirList)!=0:
            newroot = root.replace("data/", "")
            fileList.append((os.path.join(DATA_DIR, newroot), dirList))
    return fileList


def create_data_files():
    data_files = []
    # icons
    icons = create_icon_list()
    data_files.extend(icons)
    # gtg .desktop icon
    data_files.append(('share/icons/hicolor/16x16/apps', \
                       ['data/icons/hicolor/16x16/apps/gtg.png']))
    data_files.append(('share/icons/hicolor/22x22/apps', \
                       ['data/icons/hicolor/22x22/apps/gtg.png']))
    data_files.append(('share/icons/hicolor/24x24/apps', \
                       ['data/icons/hicolor/24x24/apps/gtg.png']))
    data_files.append(('share/icons/hicolor/32x32/apps', \
                       ['data/icons/hicolor/32x32/apps/gtg.png']))
    data_files.append(('share/icons/hicolor/scalable/apps', \
                       ['data/icons/hicolor/scalable/apps/gtg.svg']))
    # misc
    data_files.append(('share/applications', ['gtg.desktop']))
    data_files.append(('share/dbus-1/services', ['org.gnome.GTG.service']))
    data_files.append(('share/man/man1', ['doc/gtg.1', 'doc/gtg_new_task.1']))
    return data_files


#### TRANSLATIONS (from pyroom setup.py) ######################################

PO_DIR = 'po'
MO_DIR = os.path.join('build', 'po')

for po in glob.glob(os.path.join(PO_DIR, '*.po')):
    lang = os.path.basename(po[:-3])
    mo = os.path.join(MO_DIR, lang, 'gtg.mo')
    target_dir = os.path.dirname(mo)
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)
    try:
        return_code = call(['msgfmt', '-o', mo, po])
    except OSError:
        print 'Translation not available, please install gettext'
        break
    if return_code:
        raise Warning('Error when building locales')


class InstallData(install_data):

    def run(self):
        self.data_files.extend(self.find_mo_files())
        install_data.run(self)

    def find_mo_files(self):
        data_files = []
        for mo in glob.glob(os.path.join(MO_DIR, '*', 'gtg.mo')):
            lang = os.path.basename(os.path.dirname(mo))
            dest = os.path.join('share', 'locale', lang, 'LC_MESSAGES')
            data_files.append((dest, [mo]))
        return data_files

### SETUP SCRIPT ##############################################################

author = 'The GTG Team'

setup(
  name         = 'gtg',
  version      = info.VERSION,
  url          = info.URL,
  author       = author,
  author_email = info.EMAIL,
  description  = info.SHORT_DESCRIPTION,
  packages     = [
    'GTG',
    'GTG.backends',
    'GTG.backends.rtm',
    'GTG.backends.tweepy',
    'GTG.core',
    'GTG.core.plugins',
    'GTG.gtk',
    'GTG.gtk.liblarch_gtk',
    'GTG.gtk.editor',
    'GTG.gtk.browser',
    'GTG.gtk.backends_dialog',
    'GTG.gtk.backends_dialog.parameters_ui',
    'GTG.tools',
    'GTG.tools.liblarch',
    'GTG.plugins',
    'GTG.plugins.bugzilla',
    'GTG.plugins.export',
    'GTG.plugins.geolocalized_tasks',
    'GTG.plugins.hamster',
    'GTG.plugins.notification_area',
    'GTG.plugins.task_reaper',
    'GTG.plugins.send_email',
    'GTG.plugins.tomboy',
    'GTG.plugins.import_json',
    ],
  package_data = {
    'GTG.core.plugins': ['pluginmanager.glade'],
    'GTG.gtk': ['preferences.glade', 'deletion.glade', 'backends_dialog.glade'],
    'GTG.gtk.browser': ['taskbrowser.glade'],
    'GTG.gtk.editor': ['taskeditor.glade'],
    'GTG.plugins': [
        'bugzilla.gtg-plugin',
        'export.gtg-plugin',
        'geolocalized-tasks.gtg-plugin',
        'hamster.gtg-plugin',
        'notification-area.gtg-plugin',
        'task-reaper.gtg-plugin',
        'send-email.gtg-plugin',
        'tomboy.gtg-plugin',
        'import-json.gtg-plugin',
        ],
    'GTG.plugins.export': ['export.ui',
                          'export_templates/thumbnail_textual.txt',
                          'export_templates/template_simple.html',
                          'export_templates/template_textual.txt',
                          'export_templates/thumbnail_simple.html',
                          'export_templates/thumbnail_statusrpt.txt',
                          'export_templates/thumbnail_textual.html'],
    'GTG.plugins.geolocalized_tasks': ['geolocalized.glade',
                          'icons/hicolor/24x24/geolocalization.png',
                          'icons/hicolor/16x16/assign-location.png',
                          'icons/hicolor/svg/assign-location.svg',
                          'icons/hicolor/svg/geolocalization.svg'],
    'GTG.plugins.tomboy': ['tomboy.ui'],
    'GTG.plugins.hamster': ['prefs.ui'],
    'GTG.plugins.task_reaper': ['reaper.ui'],
    'GTG.plugins.import_json': ['import_json.ui'],
    'GTG.plugins.notification_area': ['notification_area.ui']},
  data_files = create_data_files(),
  scripts=['gtg', 'gtg_new_task'],
  cmdclass={'install_data': InstallData},
)
