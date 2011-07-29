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

import os
import shutil
import sys

import configurationhandler
import commands as commands_module
import quicklyconfig
import tools
import templatetools

import gettext
from gettext import gettext as _


def pre_create(command_template, project_template, project_dir, command_args):
    """Create the project directory before create command call"""

    if len(command_args) < 1:
        cmd = commands_module.get_command('create', project_template)
        templatetools.usage_error(_("No project name specified."), cmd=cmd, template=project_template)
 
    path_and_project = command_args[0].split('/')
    project_name = path_and_project[-1]
    
    # if a path is not present, create it
    if len(path_and_project) > 1:
        path = str(os.path.sep).join(path_and_project[0:-1])
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)
    
    # check that project name follow quickly rules and reformat it.
    try:
        project_name = templatetools.quickly_name(project_name)
    except templatetools.bad_project_name, e:
        print(e)
        return(4)

    #bail if the name if taken
    if os.path.exists(project_name):
        print _("There is already a file or directory named %s") % project_name
        return(1)

    #create directory and template file
    print _("Creating project directory %s" % project_name)
    os.mkdir(project_name)

    # creating quickly file
    configurationhandler.project_config['version'] = quicklyconfig.__version__
    configurationhandler.project_config['project'] = project_name
    configurationhandler.project_config['template'] = project_template
    configurationhandler.saveConfig(config_file_path=project_name)
    
    os.chdir(project_name)

    return 0

help_commands = _("List all commands ordered by templates")
def commands(project_template, project_dir, command_args, shell_completion=False):
    """List all commands ordered by templates"""

    # We have nothing for this
    if shell_completion:
        return("")

    all_commands = commands_module.get_all_commands()
    for template_available in all_commands:
        # copie all commands to a list (as sort() is an inplace function)
        command_for_this_template = list(all_commands[template_available].keys())
        command_for_this_template.sort()
        for command_name in command_for_this_template:
            command = all_commands[template_available][command_name]
            print "[%s]\t%s" % (template_available, command_name)
            
    return(0)

help_getstarted = _("Give some getstarted advice")
def getstarted(project_template, project_dir, command_args, shell_completion=False):
    """Give some getstarted advice"""

    # We have nothing for this
    if shell_completion:
        return("")

    print _('''-------------------------------
    Welcome to Quickly!
-------------------------------

You can create a project by executing 'quickly create <template-name> <your-project>'.

Example with ubuntu-application template:
1. create an ubuntu application and run the tutorial:
$ quickly create ubuntu-application foo
$ cd foo
$ quickly tutorial

2. You can also try:
$ quickly edit
$ quickly design
$ quickly run
Use bash completion to get every available command

3. How to play with a package and release it:

Optional (but recommended): build your package locally:
$ quickly package

BE WARNED: the two following commands will connect to Launchpad. Make sure that you have a Launchpad account and a PPA! You can find out more about setting up a Launchpad account and Launchpad features at https://launchpad.net/
$ quickly release or $ quickly share

Have Fun!''')
    return 0

help_help = _("Get help from commands")
usage_help = _("Usage: quickly help [template] <command>")
def help(project_template, project_dir, command_args, shell_completion=False):
    """Get help from commands"""

    # We have nothing for this
    if shell_completion:
        return("")

    # main quickly script has already made sure input is sane

    project_template = command_args[0]
    command_name = command_args[1]
    command = commands_module.get_command(command_name, project_template)

    # Also print usage if we can
    if command.usage():
        print # blank line before getting to help
    return command.help(project_dir, command_args)

help_quickly = _("Create a new quickly template from an existing one")
usage_quickly = _("Usage: quickly quickly [origin-template] destination-template")
def quickly(project_template, project_dir, command_args, shell_completion=False):
    """Create a new quickly template from an existing one"""

    # We have nothing for this
    if shell_completion:
        return("")

    project_template = command_args[0]
    if len(command_args) < 2:
        cmd = commands_module.get_command('quickly', project_template)
        templatetools.usage_error(_("No destination template name provided."), cmd=cmd, template=project_template)

    destination_path = os.path.expanduser("~/quickly-templates/")
    # create ~/quickly-templates/ if needed
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    template_destination_path = destination_path + command_args[1]
    if os.path.exists(template_destination_path):
        print _("%s already exists." % template_destination_path)
        return 1

    if not os.path.exists(template_destination_path):
        print _("Copy %s to create new %s template") % (project_template, template_destination_path)

    try:
        template_source_path = tools.get_template_directory(project_template)
    except tools.template_path_not_found, e:
        print(e)
        return 1
    except tools.template_not_found, e:
        print(e)
        return 1

    shutil.copytree(template_source_path, template_destination_path)

    # transform commands in import
    import_cmd_list = []
    for command_name in os.listdir(template_destination_path):
        file_path = os.path.join(template_destination_path, command_name)
        if file_path.split(".")[-1] == "pyc":
            os.remove(file_path)
            continue
        # if there is a ., remove extension
        if "." in command_name:
            command_name = ".".join(command_name.split('.')[0:-1])
        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            import_cmd_list.append(command_name)
            os.remove(file_path)
    if import_cmd_list:
        commandsconfig_path = os.path.join(template_destination_path, 'commandsconfig')
        filedest = file(commandsconfig_path + '.new', 'w')
        fileconfig = file(commandsconfig_path, 'rb')
        for line in fileconfig:
            filedest.write(line)
        filedest.write("\n[%s]\nIMPORT=%s" % (project_template, ';'.join(sorted(import_cmd_list))))
        fileconfig.close()
        filedest.close()
        os.rename(filedest.name, commandsconfig_path)
    return 0



# here, special builtin commands properties (if nothing specified, commands can be launched inside and outside projects)
launched_inside_project_only = []
launched_outside_project_only = []
followed_by_template = ['help', 'quickly']
followed_by_command = ['help']
exposed_in_bar = []
