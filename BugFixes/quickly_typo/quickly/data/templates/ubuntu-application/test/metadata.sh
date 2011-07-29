#!/bin/sh

cd /tmp

rm -rf test-project

quickly create ubuntu-application test-project
# Creating bzr repository and committing
# Congrats, your new project is setup! cd /tmp/test-project/ to start hacking.
# Creating project directory test-project

cd test-project

quickly package --extras | sed 's/^\.\+//'
# Ubuntu packaging created in debian/
# Ubuntu package has been successfully created in ../test-project_0.1_all.deb

cat debian/control | sed "s/project-$(lsb_release -c | cut -f2)*\./project-RELEASE./"
# Source: test-project
# Section: python
# Priority: extra
# Build-Depends: cdbs (>= 0.4.43),
#  debhelper (>= 6),
#  python,
#  python-support (>= 0.6.4),
#  python-distutils-extra (>= 2.10)
# Maintainer: UNKNOWN <UNKNOWN>
# Standards-Version: 3.8.3
# XS-Python-Version: current
# 
# Package: test-project
# Architecture: all
# XB-Python-Version: ${python:Versions}
# XB-AppName: Test Project
# XB-Category: GNOME;Utility;
# XB-Screenshot-Url: https://software-center.ubuntu.com/screenshots/t/test-project-RELEASE.png
# XB-Thumbnail-Url: https://software-center.ubuntu.com/screenshots/t/test-project-RELEASE.thumb.png
# XB-Icon: test-project.svg
# Depends: ${misc:Depends},
#  ${python:Depends},
#  python-gobject,
#  python-launchpad-integration,
#  python-gtk2,
#  python-desktopcouch-records,
#  yelp
# Description: UNKNOWN
#  UNKNOWN

cat debian/rules
# #!/usr/bin/make -f
# DEB_PYTHON_SYSTEM := pysupport
# DEB_PYTHON_PREFIX_ARG := /opt/extras.ubuntu.com/test-project
# 
# include /usr/share/cdbs/1/rules/debhelper.mk
# include /usr/share/cdbs/1/class/python-distutils.mk
# # langpack.mk is relevant on Ubuntu only, not Debian; it does not matter if it's missing
# -include /usr/share/cdbs/1/rules/langpack.mk
# 
# common-install-indep::
# 	cp data/media/test-project.svg ../test-project.svg
# 	dpkg-distaddfile test-project.svg raw-meta-data -

## Older versions of quickly had logo.svg instead of project_name.svg, so test those too

mv data/media/test-project.svg data/media/logo.svg

quickly package --extras | sed 's/^\.\+//'
# Ubuntu packaging created in debian/
# Ubuntu package has been successfully created in ../test-project_0.1_all.deb

grep XB-Icon debian/control
# XB-Icon: test-project.svg

tail -n 3 debian/rules
# common-install-indep::
# 	cp data/media/logo.svg ../test-project.svg
# 	dpkg-distaddfile test-project.svg raw-meta-data -

## Finally, make sure we gracefully handle no icon at all

rm data/media/logo.svg

quickly package --extras | sed 's/^\.\+//'
# Ubuntu packaging created in debian/
# Ubuntu package has been successfully created in ../test-project_0.1_all.deb

grep XB-Icon debian/control

grep dpkg-distaddfile debian/rules
