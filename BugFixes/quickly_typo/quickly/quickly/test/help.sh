#!/bin/sh

quickly --help
# Usage:
#     quickly [OPTIONS] command ...
# 
# Options:
#     -t, --template <template>  Template to use if it differs from default
#                                project template
#     --staging                  Target launchpad staging server
#     --verbose                  Verbose mode
#     -h, --help                 Show help information
# 
# Commands:
#     create <template> <project-name> (template is mandatory for this command)
#     quickly <template-origin> <template-dest> to create a create derived template
#     getstarted to get some starting hints
# 
# Examples:
#     quickly create ubuntu-application foobar
#     quickly push 'awesome new comment system'
#     quickly -t cool-template push 'awesome new comment system'

## We set HOME here to avoid picking up any odd templates the user might have

HOME=/ quickly help
# ERROR: No template or command provided to help command.
# Usage: quickly help [template] <command>
# Candidate templates are: ubuntu-application, ubuntu-cli, ubuntu-flash-game, ubuntu-pygame
# Candidate commands are: commands, getstarted, help, quickly

HOME=/ quickly help help
# Usage: quickly help [template] <command>
# 
# Get help from commands

HOME=/ quickly help ubuntu-application
# ERROR: No command provided to help command.
# Usage: quickly help [template] <command>
# Candidate commands are: add, commands, configure, create, debug, design, edit, getstarted, help, license, package, quickly, release, run, save, share, submitubuntu, test, tutorial, upgrade

HOME=/ quickly help ubuntu-application help
# Usage: quickly help [template] <command>
# 
# Get help from commands

HOME=/ quickly help not-a-template
# ERROR: not-a-template is neither a template nor a standard command.
# Usage: quickly help [template] <command>
# Candidate templates are: ubuntu-application, ubuntu-cli, ubuntu-flash-game, ubuntu-pygame
# Candidate commands are: commands, getstarted, help, quickly

HOME=/ quickly help not-a-template help
# ERROR: Template not-a-template does not exist.
# Usage: quickly help [template] <command>
# Candidate templates are: ubuntu-application, ubuntu-cli, ubuntu-flash-game, ubuntu-pygame

cd /tmp

rm -fr test-project

quickly create ubuntu-application test-project
# Creating bzr repository and committing
# Congrats, your new project is setup! cd /tmp/test-project/ to start hacking.
# Creating project directory test-project

cd test-project

HOME=/ quickly help
# ERROR: No command provided to help command.
# Usage: quickly help [template] <command>
# Candidate commands are: add, commands, configure, create, debug, design, edit, getstarted, help, license, package, quickly, release, run, save, share, submitubuntu, test, tutorial, upgrade

HOME=/ quickly help help
# Usage: quickly help [template] <command>
# 
# Get help from commands

HOME=/ quickly help ubuntu-cli help
# Usage: quickly help [template] <command>
# 
# Get help from commands

HOME=/ quickly help ubuntu-cli
# ERROR: No command provided to help command.
# Usage: quickly help [template] <command>
# Candidate commands are: commands, configure, create, debug, edit, getstarted, help, license, package, quickly, release, run, save, share, test

HOME=/ quickly help foobar
# ERROR: No foobar command found in ubuntu-application template.
# Usage: quickly help [template] <command>
# Candidate commands are: add, commands, configure, create, debug, design, edit, getstarted, help, license, package, quickly, release, run, save, share, submitubuntu, test, tutorial, upgrade
