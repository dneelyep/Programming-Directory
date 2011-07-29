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
import re
import subprocess
import sys

import builtincommands
import configurationhandler
import templatetools, tools

import gettext
from gettext import gettext as _


gettext.textdomain('quickly')

# A dictionary with keys either 'builtins' or the names of templates. Values
# are another dictionary mapping command names to their command objects. This
# is used as a cache of all commands that we've found in templates.
__commands = {}

def try_to_import_command(commands, importing_template, imported_template,
                          command_name):
    """Import command in one template from another template

    Ignore unknown command or template"""

    # let's override by locally defined command
    if command_name not in commands[importing_template]:
         try:
             commands[importing_template][command_name] = \
             commands[imported_template][command_name]
         except KeyError:
             # command/template doesn't exist: ignore
             pass
    return commands

def get_all_commands():
    """Load all commands

    First, load template command and then builtins one. Push right parameters
    depending if hooks are available, or if the command execution is special
    You can note that create command is automatically overloaded atm.
    """

    global __commands
    if len(__commands) > 0:
        return __commands

    try:
        template_directories = tools.get_template_directories()
    except tools.template_path_not_found:
        template_directories = []
    import_commands = {}

    for template_dir in template_directories:
        for template in os.listdir(template_dir):
            __commands[template] = {}
            import_commands[template] = {}
            template_path = os.path.join(template_dir, template)

            # load special attributes declared for every command
            launch_inside_project_command_list = []
            launch_outside_project_command_list = []
            command_followed_by_command_list = []
            command_exposed_in_bar_list = []
            current_template_import = None

            try:
                files_command_parameters = file(
                    os.path.join(template_path, "commandsconfig"), 'rb')
                for line in files_command_parameters:
                    # Suppress commentary after the value in configuration
                    # file and in full line.
                    fields = line.split('#')[0]
                    fields = fields.split('=') # Separate variable from value
                    # command definitions or import have two fields
                    if len(fields) == 2:
                        targeted_property = fields[0].strip()
                        command_list = [
                            command.strip()
                            for command in fields[1].split(';')]
                        if (targeted_property
                            == 'COMMANDS_LAUNCHED_IN_OR_OUTSIDE_PROJECT'):
                            launch_inside_project_command_list.extend(
                                command_list)
                            launch_outside_project_command_list.extend(
                                command_list)
                        if (targeted_property
                            == 'COMMANDS_LAUNCHED_OUTSIDE_PROJECT_ONLY'):
                            launch_outside_project_command_list.extend(
                                command_list)
                        if (targeted_property
                            == 'COMMANDS_FOLLOWED_BY_COMMAND'):
                            command_followed_by_command_list.extend(
                                command_list)
                        if (targeted_property
                            == 'COMMANDS_EXPOSED_IN_BAR'):
                            command_exposed_in_bar_list.extend(
                                command_list)
                        if (targeted_property
                            == 'IMPORT') and current_template_import:
                            import_commands[template][current_template_import] \
                                           = command_list
                    else:
                        # try to fetch import command results
                        reg_result = re.search('\[(.*)\]', fields[0].strip())
                        if reg_result:
                            current_template_import = reg_result.group(1)
                        
            except (OSError, IOError):
                pass

            for command_name in os.listdir(template_path):
                file_path = os.path.join(template_path, command_name)
                # if there is a ., remove extension
                if "." in command_name:
                    command_name = ".".join(command_name.split('.')[0:-1])
                icon_path = os.path.join(template_path, 'icons',
                                         "%s.png" % command_name)

                # add the command to the list if is executable (commands are
                # only formed of executable files)
                if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                    hooks = {'pre': None, 'post': None}
                    for event in ('pre', 'post'):
                        event_hook = getattr(
                            builtincommands, event + '_' + command_name, None)
                        if event_hook:
                            hooks[event] = event_hook
                    if not os.path.isfile(icon_path):
                        icon_path = None

                    # define special options for command
                    launch_inside_project = False
                    launch_outside_project = False
                    followed_by_template = False
                    followed_by_command = False
                    exposed_in_bar = False
                    if command_name in launch_inside_project_command_list:
                        launch_inside_project = True
                    if command_name in launch_outside_project_command_list:
                        launch_outside_project = True
                        followed_by_template = True
                    if command_name in command_followed_by_command_list:
                        followed_by_command = True
                    if command_name in command_exposed_in_bar_list:
                        exposed_in_bar = True
                    # default for commands: if not inside nor outside, and
                    # it's a template command, make it launch inside a project
                    # only
                    if not (launch_inside_project or launch_outside_project):
                        launch_inside_project = True

                    __commands[template][command_name] = Command(
                        command_name, file_path, template,
                        launch_inside_project, launch_outside_project,
                        followed_by_template, followed_by_command,
                        exposed_in_bar, hooks['pre'], hooks['post'], 
                        icon=icon_path)

    # now try to import command for existing templates
    for importing_template in import_commands:
        for imported_template in import_commands[importing_template]:
            for command_name in import_commands[importing_template][imported_template]:
                # if instruction to import all commands, get them first
                if command_name == 'all':
                    try:
                        for command_name in __commands[imported_template]:
                            __commands = try_to_import_command(__commands,
                                         importing_template, imported_template,
                                         command_name)
                    except KeyError:
                        # template doesn't exist: ignore
                        pass
                    break # no need to cycle anymore (all commands imported)
                else:
                    __commands = try_to_import_command(__commands,
                                 importing_template, imported_template,
                                 command_name)

    # add builtin commands (avoiding gettext and hooks)
    __commands['builtins'] = {}
    for elem in dir(builtincommands):
        command = getattr(builtincommands, elem)
        if (callable(command)
            and not command.__name__.startswith(('pre_', 'post_', 'help_', 'usage_', 'gettext'))):
            command_name = command.__name__
            # here, special case for some commands
            launch_inside_project = False
            launch_outside_project = False
            followed_by_template = False
            followed_by_command = False
            exposed_in_bar = False

            if command_name in builtincommands.launched_inside_project_only:
                launch_inside_project = True
            if command_name in builtincommands.launched_outside_project_only:
                launch_outside_project = True
            if command_name in builtincommands.followed_by_template:
                followed_by_template = True
            if command_name in builtincommands.followed_by_command:
                followed_by_command = True
            if command_name in builtincommands.exposed_in_bar:
                exposed_in_bar = True

            # default for commands: if not inside nor outside only, and it's a
            # builtin command, make it launch wherever
            if not launch_inside_project and not launch_outside_project:
                launch_inside_project = True
                launch_outside_project = True

            hooks = {'pre': None, 'post': None}
            for event in ('pre', 'post'):
                event_hook = getattr(builtincommands,
                                     event + '_' + command_name, None)
                if event_hook:
                    hooks[event] = event_hook

            __commands['builtins'][command_name] = Command(
                command_name, command, None, launch_inside_project,
                launch_outside_project, followed_by_template,
                followed_by_command, exposed_in_bar, hooks['pre'], hooks['post'])

    return __commands


def get_commands_by_criteria(**criterias):
    """Get a list of all commands corresponding to criterias

    Criterias correponds to Command object properties.
    """

    # all criterias are None by default, which means, don't care about the
    # value.
    matched_commands = []
    all_commands = get_all_commands()

    for template_available in all_commands:
        if ('template' in criterias
            and criterias['template'] != template_available):
            continue # go to next round if no template match
        for candidate_command_name in all_commands[template_available]:
            candidate_command = all_commands[
                template_available][candidate_command_name]
            command_ok = True
            # check all criterias (template has already been checked)
            for elem in criterias:
                if (elem is not 'template'
                    and getattr(candidate_command, elem) != criterias[elem]):
                    command_ok = False
                    continue # no need to check other criterias
            if command_ok:
                matched_commands.append(candidate_command)

    return matched_commands


def get_command_names_by_criteria(**criteria):
    """Get a list of all command names corresponding to criteria.

    'criteria' correponds to Command object properties.
    """
    return [command.name for command in get_commands_by_criteria(**criteria)]


def get_command(command_name, template=None, **kwargs):
    template = template or "builtins"
    try:
        command = get_commands_by_criteria(name=command_name, template=template, **kwargs)[0]
    except IndexError:
        if template == "builtins":
            return None
        try:
            command = get_commands_by_criteria(name=command_name, template="builtins", **kwargs)[0]
        except IndexError:
            return None
    return command


def get_all_templates():
    """Get a list of all templates"""
    return [
        template for template in get_all_commands().keys()
        if template != "builtins"]

class Command:

    def _errmsg(self, function_name, return_code):
       '''Quit immediately and print error if return_code != 4'''
       if return_code != 4:
            print _("ERROR: %s command failed") % function_name
            print _("Aborting")

    def __init__(self, command_name, command, template=None,
                 inside_project=True, outside_project=False,
                 followed_by_template=False, followed_by_command=False,
                 exposed_in_bar=False, prehook=None, posthook=None,
                 icon=None):
        self.command = command
        # self.template is the native template where the command is from
        # if this command is imported into another template, the object
        # is still the same, only the access byx
        # get_all_commands()[importing_template]["command_name"]
        self.template = template
        self.prehook = prehook
        self.posthook = posthook
        self.inside_project = inside_project
        self.outside_project = outside_project
        self.followed_by_template = followed_by_template
        self.followed_by_command = followed_by_command
        self.name = command_name
        self.exposed_in_bar = exposed_in_bar
        self.icon = icon

    def shell_completion(self, template_in_cli, args):
        """Smart completion of a command

        This command try to see if the command is followed by a template and
        present template if it's the case. Otherwise, it calls the
        corresponding command argument.
        """

        completion = []

        if len(args) == 1:
            if not template_in_cli:
                if self.followed_by_template: # template completion
                    if not self.template: # builtins command case
                        completion.extend(get_all_templates())
                    else:
                        # complete with current template (which != from
                        # template_in_cli: ex create command (multiple
                        # templates)). Fetch as well imported command in
                        # other template
                        for template in get_all_templates():
                            try:
                                if get_all_commands()[template][self.name] == self:
                                    completion.extend([template])
                            except KeyError:
                                pass
            else: # there is a template, add template commands
                if self.followed_by_command: # template command completion
                    completion.extend(
                        get_command_names_by_criteria(
                            template=template_in_cli))
            if self.followed_by_command: # builtin command completion
                completion.extend(
                    get_command_names_by_criteria(template="builtins"))

        elif len(args) == 2:
            if self.followed_by_template and tools.check_template_exists(args[0]):
                template_in_cli = args[0]
                # template command completion and builtins command.
                if self.followed_by_command:
                    completion.extend(
                        get_command_names_by_criteria(
                            template=template_in_cli))
                    completion.extend(
                        get_command_names_by_criteria(template="builtins"))

        # give to the command the opportunity of giving some shell-completion
        # features
        if template_in_cli == self.template and len(completion) == 0:
            if callable(self.command): # Internal function
                completion.extend(
                    self.command(template_in_cli, "", args, True))
            else: # External command
                instance = subprocess.Popen(
                    [self.command, "shell-completion"] + args,
                    stdout=subprocess.PIPE)
                command_return_completion, err = instance.communicate()
                if instance.returncode != 0:
                    print err
                    sys.exit(1)
                completion.extend(command_return_completion.strip().split(' ')) # pylint: disable=E1103

        return completion

    def usage(self):
        """Print usage of the current command"""

        return_code = False
        if callable(self.command): # intern function
            name = 'usage_'+self.name
            if hasattr(builtincommands, name):
                print getattr(builtincommands, name)
                return_code = True
        else: # launch command with "_usage" parameter
            process = subprocess.Popen([self.command, "_usage"], stdout=subprocess.PIPE)
            output = process.communicate()[0].strip()
            if output:
                print output
                return_code = True

        return return_code

    def help(self, dest_path, command_args):
        """Print help of the current command"""

        return_code = 0
        if callable(self.command): # intern function
            name = 'help_'+self.name
            if hasattr(builtincommands, name):
                print getattr(builtincommands, name)
            else:
                print self.command.__doc__ # untranslatable fallback
        else: # launch command with "help" parameter
            process = subprocess.Popen([self.command, "help"] + command_args,
                                       cwd=dest_path, stdout=subprocess.PIPE)
            output = process.communicate()[0].strip()
            if output:
                print output
            return_code = process.returncode

        return return_code

    def is_right_context(self, dest_path, verbose=True):
        """Check if we are in the right context for launching the command.

        If you are using this to introspect available commands, then set
        verbose to False.
        """
        # check if dest_path check outside or inside only project :)
        if self.inside_project and not self.outside_project:
            try:
                project_path = tools.get_root_project_path(dest_path)
            except tools.project_path_not_found:
                if verbose:
                    print (_(
                        "ERROR: Can't find project in %s.\nEnsure you launch "
                        "this command from a quickly project directory.")
                           % dest_path)
                    print _("Aborting")
                return False
        if self.outside_project and not self.inside_project:
            try:
                project_path = tools.get_root_project_path(dest_path)
                if verbose:
                    print _(
                        "ERROR: %s is a project. You can't launch %s command "
                        "within a project. Please choose another path."
                        % (project_path, self.command))
                    print _("Aborting")
                return False
            except tools.project_path_not_found:
                pass

        return True

    def launch(self, current_dir, command_args, project_template=None):
        """Launch command and hooks for it

        This command will perform the right action (insider function or script
        execution) after having checked the context.
        """

        if not self.is_right_context(current_dir): # check in verbose mode
            return 1

        # get root project dir
        try:
            project_path = tools.get_root_project_path(current_dir)
            inside_project = True
        except tools.project_path_not_found:
            # launch in current project
            project_path = current_dir
            inside_project = False

        # transition if we are inside a project and template is not None (builtins)
        # (call upgrade from native template)
        if inside_project and self.name != "upgrade" and self.template:
            (project_version, template_version) = templatetools.get_project_and_template_versions(self.template)
            if project_version < template_version:
                try:
                    return_code = get_all_commands()[self.template]['upgrade'].launch( current_dir, [project_version, template_version], project_template)
                    if return_code == 0:
                        templatetools.update_version_in_project_file(template_version, self.template)
                    else:
                        sys.exit(return_code)
                except KeyError: # if KeyError, no upgrade command for this template
                    pass

        if self.prehook:
            return_code = self.prehook(self.template, project_template, project_path, command_args)
            if return_code != 0:
                self._errmsg(self.prehook.__name__, return_code)
                return return_code

        if callable(self.command): # Internal function
            return_code = self.command(project_template, project_path, command_args)
        else: # External command
            return_code = subprocess.call(
                [self.command] + command_args, cwd=project_path)
        if return_code != 0:
            self._errmsg(self.name, return_code)
            return return_code

        if self.posthook:
            return_code = self.posthook(project_template, project_path, command_args)
            if return_code != 0:
                self._errmsg(self.posthook.__name__, return_code)
                return return_code

        return 0
