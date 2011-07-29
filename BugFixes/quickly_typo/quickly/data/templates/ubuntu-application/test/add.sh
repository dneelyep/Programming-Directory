#!/bin/sh

cd /tmp

rm -rf test-project

quickly create ubuntu-application test-project
# Creating bzr repository and committing
# Congrats, your new project is setup! cd /tmp/test-project/ to start hacking.
# Creating project directory test-project

cd test-project

quickly add
# ERROR: Cannot add, no plugin name provided.
# Usage:
#   quickly add dialog <dialog-name>
#   quickly add help-guide <guide-name>
#   quickly add help-topic <topic-name>
#   quickly add indicator

quickly add foo
# ERROR: Cannot add, did not recognize plugin name: foo
# Usage:
#   quickly add dialog <dialog-name>
#   quickly add help-guide <guide-name>
#   quickly add help-topic <topic-name>
#   quickly add indicator

quickly add dialog
# Usage: quickly add dialog <dialog-name>

quickly add dialog 1 2
# Usage: quickly add dialog <dialog-name>

bzr status

quickly add dialog foo-bar

bzr status
# unknown:
#   data/ui/FooBarDialog.ui
#   data/ui/foo_bar_dialog.xml
#   test_project/FooBarDialog.py

cat data/ui/foo_bar_dialog.xml
# <glade-catalog name="foo_bar_dialog" domain="glade-3" 
#                depends="gtk+" version="1.0">
#   <glade-widget-classes>
#     <glade-widget-class title="Foo Bar Dialog" name="FooBarDialog" 
#                         generic-name="foo_bar_dialog" parent="GtkDialog"
#                         icon-name="widget-gtk-dialog"/>
#   </glade-widget-classes>
# 
# </glade-catalog>

rm data/ui/FooBarDialog.ui data/ui/foo_bar_dialog.xml test_project/FooBarDialog.py

quickly add indicator 1
# Usage: quickly add indicator

quickly add indicator

bzr status
# unknown:
#   test_project/indicator.py

grep new_application_indicator test_project/indicator.py
# def new_application_indicator(window):

rm  test_project/indicator.py

quickly add help-topic
# Usage: quickly add help-topic <topic-name>

quickly add help-topic a.b
# ERROR: unpermitted character in name.
# The name must start with a letter and contain only letters, spaces, dashes (-), and digits.
# ERROR: add command failed
# Aborting

quickly add help-topic "Quickly Rocks"

bzr status
# unknown:
#   help/C/quickly-rocks.page

grep title help/C/quickly-rocks.page
# <title>Quickly Rocks</title>

grep id= help/C/quickly-rocks.page
#       id="quickly-rocks">

rm help/C/quickly-rocks.page

quickly add help-guide
# Usage: quickly add help-guide <guide-name>

quickly add help-guide a.b
# ERROR: unpermitted character in name.
# The name must start with a letter and contain only letters, spaces, dashes (-), and digits.
# ERROR: add command failed
# Aborting

quickly add help-guide "Quickly Rocks and Rolls"

bzr status
# unknown:
#   help/C/quickly-rocks-and-rolls.page

grep title help/C/quickly-rocks-and-rolls.page
# <title>Quickly Rocks And Rolls</title>

grep id= help/C/quickly-rocks-and-rolls.page
#       id="quickly-rocks-and-rolls">

rm help/C/quickly-rocks-and-rolls.page
