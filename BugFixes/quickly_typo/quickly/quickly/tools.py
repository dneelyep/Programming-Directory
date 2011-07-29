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
import sys
import stat

import gettext
from gettext import gettext as _

import quicklyconfig
import commands
import configurationhandler
import version
import templatetools

__project_path = None

class project_path_not_found(Exception):
    pass

class data_path_not_found(Exception):
    def __init__(self, path):
        self.path = path
    def __str__(self):
        return repr(self.path)

class template_path_not_found(Exception):
    pass
class template_not_found(Exception):
    pass

def usage():
    print _("""Usage:
    quickly [OPTIONS] command ...

Options:
    -t, --template <template>  Template to use if it differs from default
                               project template
    --staging                  Target launchpad staging server
    --verbose                  Verbose mode
    -h, --help                 Show help information

Commands:
    create <template> <project-name> (template is mandatory for this command)
    quickly <template-origin> <template-dest> to create a create derived template
    getstarted to get some starting hints

Examples:
    quickly create ubuntu-application foobar
    quickly push 'awesome new comment system'
    quickly -t cool-template push 'awesome new comment system'""")


def get_quickly_data_path():
    """Retrieve quickly data path

    This path is by default <quickly_lib_path>/../data/ in trunk
    and /usr/share/quickly in an installed version but this path
    is specified at installation time.
    """

    # get pathname absolute or relative
    if quicklyconfig.__quickly_data_directory__.startswith('/'):
        pathname = quicklyconfig.__quickly_data_directory__
    else:
        pathname = os.path.dirname(__file__) + '/' + quicklyconfig.__quickly_data_directory__
    abs_data_path = os.path.abspath(pathname)

    if os.path.exists(abs_data_path):
        return abs_data_path
    else:
        raise data_path_not_found(abs_data_path)

def get_template_directories():
    """Retrieve all directories where quickly templates are

    :return a list of directories
    """

    # default to looking up templates in the current dir
    invalid_data_path = None
    template_directories = []

    # Add user defined, and hard-coded template directories.
    user_paths = os.environ.get('QUICKLY_TEMPLATES', '').split(':')
    user_paths.insert(0, '~/quickly-templates')
    for path in user_paths:
        path = os.path.expanduser(path)
        if os.path.exists(path):
            template_directories.append(path)

    # retrieve from trunk or installed version
    try:
        abs_template_path = get_quickly_data_path() + '/templates/'
        if os.path.exists(abs_template_path):
            template_directories.append(abs_template_path)
    except data_path_not_found, e:
        #TODO: add here some kind of warning log about data path
        invalid_data_path = e

    if not template_directories:
        error_message = None
        if invalid_data_path:
            error_message = _("%s is an invalid data path.\n") % invalid_data_path
        raise template_path_not_found(error_message + _("No template directory found. Aborting"))

    return template_directories


def get_template_directory(template):
    """Detect where the quickly template and if it exists"""

    # check for the first available template in template_directories
    for template_directory in get_template_directories():
        template_path = template_directory + "/" + template
        if os.path.exists(template_path):
            template_found = True
            break
        template_found = False

    # if still false, no template found in template_directories
    if not template_found:
        raise template_not_found(_("ERROR: Template '%s' not found. Aborting")) % template

    return template_path


def get_root_project_path(path=None):
    """Try to guess where the .quickly config file is.

    path is optional (needed by the create command or api, for instance).
    getcwd() is taken by default.
    If nothing found, try to find it up to 6 parent directory

    :return project_path. Raise a project_path_not_found elsewhere.
    """

    # cache, but check that the path asked in still the same
    global __project_path
    if  __project_path:
        if path and __project_path in path:
            return __project_path

    if path is None:
        current_path = os.getcwd()
    else:
        current_path = path

    # check for .quickly file until root is found
    while os.path.dirname(current_path) != current_path:
        quickly_file = current_path + "/.quickly"
        if os.path.isfile(quickly_file):
            __project_path = current_path
            return current_path
        current_path = os.path.abspath(os.path.dirname(current_path))
    raise project_path_not_found()

def check_template_exists(template):
    """Check if template exists"""
   
    try: 
        commands.get_all_commands()[template]
    except KeyError:
        return False
    return True

def process_command_line(argv):
    """Entry point for command line processing
    use sys.argv by default if no args to parse

    :return: options
    """

    opt_command = []
    opt_template = None
    i = 0

    while i < len(argv):
        arg = argv[i]

        if arg.startswith('-'):
            if arg == '--template' or arg == '-t':
                if i + 1 < len(argv):
                    opt_template = argv[i + 1]
                    i += 1
                else:
                    print _("ERROR: %s needs one argument: %s" % ('--template', '<template name>'))
                    sys.exit(1)
            elif arg == '--staging':
                oldenv = ""
                if os.environ.has_key('QUICKLY'):
                    oldenv = os.environ['QUICKLY']
                os.environ['QUICKLY'] = "staging:" + oldenv
            elif arg == '--verbose':
                oldenv = ""
                if os.environ.has_key('QUICKLY'):
                    oldenv = os.environ['QUICKLY']
                os.environ['QUICKLY'] = "verbose:" + oldenv
            elif arg == '--version':
                version.show_version()
                sys.exit(0)
            elif arg == '--help' or arg == '-h':
                usage()
                sys.exit(0)
            elif arg == '--':
                # turn off option detection, give everything to templates (even -f, --version)
                opt_command.extend(argv[i:])
                break
            else:
                opt_command.append(arg)
        else:
            opt_command.append(arg)
        i += 1

    if len(opt_command) == 0:
        print _("ERROR: No command provided in command line")
        usage()
        sys.exit(1)

    return (opt_command, opt_template)


def get_completion_in_context(argv, context_path=None):
    """seek for available completion (command, template…)

    : return tuples with list of available commands and origin (default or template)
    """

    if context_path is None:
        context_path = os.getcwd()
    else:
        context_path = os.path.abspath(context_path)

    available_completion = []

    # get available templates after option if needed
    if argv[-2] in ("-t", "--template"):
        available_completion.extend([template for template in commands.get_all_templates()])

    else:
        # treat commands and try to get the template from the project directory if we are in a project (if not already provided by the -t option)
        (opt_command, opt_template) = process_command_line(argv[3:])
        if not opt_template and configurationhandler.loadConfig(can_stop=False, config_file_path=context_path) == 0:
            try:
                opt_template = configurationhandler.project_config['template']
            except KeyError:
                pass
        # if no command yet, check for available command
        if len(opt_command) == 1:
            available_completion.extend([command.name for command in _get_commands_in_context(opt_template, context_path)])
        else:
            # ask for the command what she needs (it automatically handle the case of command followed by template and command followed by command)
            for command in commands.get_commands_by_criteria(name=opt_command[0]): # as 1: is '' or the begining of a word
                available_completion.extend(command.shell_completion(opt_template, opt_command[1:]))

    # dash option completion.  Some commands have dash args, but we also have them.  So we take what command thought
    # should be the completions and add our own.  We also strip anything that doesn't start with a dash, since many
    # completion functions are naive and just give all possible matches, even if they don't match.
    if argv[-1].startswith("-"):
        available_completion.extend(["-h", "--help", "-t", "--template", "--staging", "--verbose", "--version"])
        available_completion = [arg for arg in available_completion if arg.startswith('-')]

    # remove duplicates and sort
    completion = list(set(available_completion))
    completion.sort()
    return (completion)


def _get_commands_in_context(opt_template, context_path=None):
    """seek for available commands in current context (internally called)"""

    command_completion = []
    # list available command in template suiting context (even command "followed by template" native of that template)
    if opt_template: 
        command_completion.extend([command for command in commands.get_commands_by_criteria(template=opt_template) if command.is_right_context(context_path, verbose=False)])

    # add commands followed by a template if we don't already have a template provided (native command followed by template has already been handled before)
    else:
        command_completion.extend([command for command in commands.get_commands_by_criteria(followed_by_template=True) if command.is_right_context(context_path, verbose=False)])

    # add builtin commands
    command_completion.extend([command for command in commands.get_commands_by_criteria(template="builtins") if command.is_right_context(context_path, verbose=False)])

    return command_completion

def get_commands_in_context(context_path=None):
    """seek for available commands in current context (extern call)"""
    opt_template = None
    if configurationhandler.loadConfig(can_stop=False, config_file_path=context_path) == 0:
        try:
            opt_template = configurationhandler.project_config['template']
        except KeyError:
            pass
    return(_get_commands_in_context(opt_template, context_path))


def list_template_for_command(command_name):
    """from the command_name, return all templates containing it"""
    proposed_templates = []
    for template in commands.get_all_templates():
        try:
            commands.get_all_commands()[template][command_name]
            proposed_templates.append(template)
        except KeyError:
            pass
    return proposed_templates

def check_for_followed_by_args(cmd, command_args, project_template):
    if not cmd.followed_by_template and not cmd.followed_by_command:
        return command_args # nothing to check

    command = None

    if cmd.followed_by_template and cmd.followed_by_command:
        # If no arguments, there is something obviously wrong
        if len(command_args) == 0:
            if project_template:
                templatetools.usage_error(_("No command provided to %s command.") % cmd.name, cmd=cmd, template=project_template)
            else:
                templatetools.usage_error(_("No template or command provided to %s command.") % cmd.name, cmd=cmd)
        # At least one argument.  What is it?  First check if it's a command if we already have a template
        if project_template:
            command = commands.get_command(command_args[0], project_template)
            if command:
                command_args.insert(0, project_template) # use default template
            elif not command and not check_template_exists(command_args[0]):
                # Wasn't a command or a template name, but we are in the context of a template
                templatetools.usage_error(_("No %s command found in %s template.") % (command_args[0], project_template), cmd=cmd, template=project_template)
        if not command:
            # must be a template name then (or nonsense)
            if not check_template_exists(command_args[0]):
                command = commands.get_command(command_args[0]) # did user provid a valid builtin command?
                if command:
                    command_args.insert(0, 'builtins')
                elif len(command_args) == 1:
                    templatetools.usage_error(_("%s is neither a template nor a standard command.") % (command_args[0]), cmd=cmd)
                else:
                    templatetools.usage_error(_("Template %s does not exist.") % (command_args[0]), cmd=cmd, show_templates_for=None)
            project_template = command_args[0]
            # OK, we have a template!
            if len(command_args) < 2:
                templatetools.usage_error(_("No command provided to %s command.") % cmd.name, cmd=cmd, template=project_template)
            command = commands.get_command(command_args[1], project_template)
            if not command:
                templatetools.usage_error(_("No %s command found in %s template.") % (command_args[1], project_template), cmd=cmd, template=project_template)

    elif cmd.followed_by_template:
        if len(command_args) > 0:
            if check_template_exists(command_args[0]):
                project_template = command_args[0]
        if not project_template:
            templatetools.usage_error(_("No template provided to %s command.") % cmd.name, cmd=cmd)

    elif cmd.followed_by_command:
        if len(command_args) > 0:
            command = commands.get_command(command_args[0], project_template)
            if not command:
                templatetools.usage_error(_("No %s command found.") % command_args[0], cmd=cmd, template=project_template)
        if not command:
            templatetools.usage_error(_("No command provided to %s command.") % cmd.name, cmd=cmd, template=project_template)

    return command_args

