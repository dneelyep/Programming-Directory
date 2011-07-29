#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
# Copyright 2009 Didier Roche
#
# This file is part of Quickly ubuntu-application template
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

import sys
import os
import shutil
import subprocess

from quickly import templatetools
from internal import quicklyutils, SWF

import gettext
from gettext import gettext as _
# set domain text
gettext.textdomain('quickly')



def help():
    print _("""Usage:
$ quickly create ubuntu-flash-game path/to/project_name path/to/myflashgame.swf

where "project_name" is one or more words separated by an underscore and
path/to can be any existing path.

This will create a new project which runs your existing SWF, myflashgame.swf,
on the Ubuntu desktop, and makes it ready to be packaged and distributed in
the Ubuntu Software Centre.

After creating the project, you'll want to specify the title of your game
and the size of the window:

1. Changing your working directory to the new project:
$ cd path/to/project_name

3. Edit the code and specify the title and window size:
$ quickly edit
""")
templatetools.handle_additional_parameters(sys.argv, help)


# get the name of the project
if len(sys.argv) < 2:
    print _("""Project name not defined.\nUsage is: quickly create ubuntu-flash-game project_name myflashgame.swf""")
    sys.exit(4)

if len(sys.argv) < 3:
    print _("""Flash SWF file not defined.\nUsage is: quickly create ubuntu-flash-game project_name myflashgame.swf""")
    sys.exit(5)

path_and_project = sys.argv[1].split('/')
project_name = path_and_project[-1]

swf = os.path.realpath(sys.argv[2])
if not os.path.exists(swf):
    print _("""Flash SWF file '%s' not found.\nUsage is: quickly create ubuntu-flash-game project_name myflashgame.swf""" % swf)
    sys.exit(6)

# check that project name follow quickly rules and reformat it.
try:
    project_name = templatetools.quickly_name(project_name)
except templatetools.bad_project_name, e:
    print(e)
    sys.exit(1)

os.chdir(project_name)

# get origin path
pathname = templatetools.get_template_path_from_project()
abs_path_project_root = os.path.join(pathname, 'project_root')

python_name = templatetools.python_name(project_name)
sentence_name, camel_case_name = templatetools.conventional_names(project_name)

# Calculate the SWF's dimensions
try:
    width, height = SWF.dimensions(swf)
except SWF.SWFNotASWF:
    print "File '%s' does not seem to be a SWF. Terminating."
    sys.exit(7)
except SWF.SWFNoDimensions:
    print "(Could not read size from SWF file; defaulting to 640x480. You should edit bin/%s with the correct size.)" % project_name
    width, height = (640, 480)


substitutions = (("project_name",project_name),
            ("camel_case_name",camel_case_name),
            ("python_name",python_name),
            ("sentence_name",sentence_name),
            ("swf_height",str(height)),
            ("swf_width",str(width)),
            )


for root, dirs, files in os.walk(abs_path_project_root):
    try:
        relative_dir = root.split('project_root/')[1]
    except:
        relative_dir = ""
    # python dir should be replace by python_name (project "pythonified" name)
    if relative_dir.startswith('python'):
        relative_dir = relative_dir.replace('python', python_name)

    for directory in dirs:
        if directory == 'python':
            directory = python_name
        os.mkdir(os.path.join(relative_dir, directory))
    for filename in files:
        templatetools.file_from_template(root, filename, relative_dir, substitutions)

# set the mode to executable for executable file 
exec_file = os.path.join('bin', project_name)
try:
    os.chmod(exec_file, 0755)
except:
    pass

# Copy the specified SWF file into the project
shutil.copyfile(swf, os.path.join("data", "game.swf"))

# We require a specific version of the ubuntu-application template, so
# edit the project's .quickly file to specify it.
#WORKAROUND
fp = open(".quickly", "a")
fp.write("\nversion_ubuntu-application = 0.4\n")
fp.close()

# add it to revision control
print _("Creating bzr repository and commiting")
bzr_instance = subprocess.Popen(["bzr", "init"], stdout=subprocess.PIPE)
bzr_instance.wait()
bzr_instance = subprocess.Popen(["bzr", "add"], stdout=subprocess.PIPE)
bzr_instance.wait()
subprocess.Popen(["bzr", "commit", "-m", "Initial project creation with Quickly!"], stderr=subprocess.PIPE)

# run the new application if X display
if templatetools.is_X_display() and os.path.isfile(exec_file):
    print _("Launching your newly created project!")
    subprocess.call(['./' + project_name], cwd='bin/')

print _("Congratulations, your new project is set up! cd %s/ to edit the details.") % os.getcwd()

sys.exit(0)
