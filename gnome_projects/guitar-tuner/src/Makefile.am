## Process this file with automake to produce Makefile.in
## Created by Anjuta

uidir = $(datadir)/guitar_tuner/ui
ui_DATA = ../data/guitar_tuner.ui

## The main script
bin_SCRIPTS = guitar_tuner.py

## Directory where .class files will be installed
guitar_tunerdir = $(pythondir)/guitar_tuner

EXTRA_DIST = $(ui_DATA)

guitar_tuner_PYTHON = \
	guitar_tuner.py

# Remove ui directory on uninstall
uninstall-local:
	-rm -r $(uidir)
	-rm -r $(datadir)/guitar_tuner
