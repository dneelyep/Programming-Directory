#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
# quickly: quickly project handler
#
# Copyright (C) 2009 Didier Roche
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License version 3,
#    as published by the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


# UPDATE VERSION WHEN NEEDED (it updates all versions needed to be updated)
VERSION = '11.04'

import glob
import os
import sys
import subprocess

try:
    import DistUtilsExtra.auto
except ImportError:
    print >> sys.stderr, 'To build quickly you need https://launchpad.net/python-distutils-extra'
    sys.exit(1)

assert DistUtilsExtra.auto.__version__ >= '2.18', 'needs DistUtilsExtra.auto >= 2.18'

def update_config(values = {}):

    oldvalues = {}
    try:
        fin = file('quickly/quicklyconfig.py', 'r')
        fout = file(fin.name + '.new', 'w')

        for line in fin:
            fields = line.split(' = ') # Separate variable from value
            if fields[0] in values:
                oldvalues[fields[0]] = fields[1].strip()
                line = "%s = %s\n" % (fields[0], values[fields[0]])
            fout.write(line)

        fout.flush()
        fout.close()
        fin.close()
        os.rename(fout.name, fin.name)
    except (OSError, IOError), e:
        print ("ERROR: Can't find quickly/quicklyconfig.py")
        sys.exit(1)
    return oldvalues

def update_tutorial(tutorial_layouts):

    for tutorial_layout in tutorial_layouts:
        tutorial_dir = tutorial_layout[0]
        file_name = tutorial_layout[1]
        po_dir= "%s/po" % tutorial_dir
        # update .pot
        update_cmd = ['xml2po', '-e', '-o', '%s/%s.pot' % (po_dir, file_name),
                      '%s/%s.xml' % (tutorial_dir, file_name)]
        subprocess.call(update_cmd)
        # update lang
        for po_file in glob.glob("%s/*.po" % po_dir):
            lang = os.path.basename(po_file[:-3])
            update_cmd = ['xml2po', '-p', '%s/%s.po' % (po_dir, lang), '-o',
                          '%s/%s-%s.xml' % (tutorial_dir, file_name, lang),
                          '%s/%s.xml' % (tutorial_dir, file_name)]
            subprocess.call(update_cmd)

class InstallAndUpdateDataDirectory(DistUtilsExtra.auto.install_auto):
    def run(self):
        values = {'__quickly_data_directory__': "'%s'" % (self.prefix + '/share/quickly/'),
                  '__version__': "'%s'" % self.distribution.get_version()}
        previous_values = update_config(values)
        update_tutorial([("data/templates/ubuntu-application/help",
                           'tutorial'),
                         ("data/templates/ubuntu-pygame/help",
                           'tutorial')])
        DistUtilsExtra.auto.install_auto.run(self)
        update_config(previous_values)


DistUtilsExtra.auto.setup(name='quickly',
      version="%s" % VERSION,
      description='build new Ubuntu apps quickly',
      long_description='Quickly enables for prospective programmer a way to easily build new ' \
                  'apps for Ubuntu based on templates and other systems for helping them ' \
                  'write their code in a guided manner. This also includes packaging and ' \
                  'deploying code.',
      url='https://launchpad.net/quickly',
      license="GPL v3",
      author='Quickly Developer Team',
      author_email='quickly-talk@lists.launchpad.net',
      data_files=[('share/quickly/templates/ubuntu-application/project_root', glob.glob('data/templates/ubuntu-application/project_root/project_name.desktop.in')),
                  ('share/quickly/templates/ubuntu-pygame/project_root', glob.glob('data/templates/ubuntu-pygame/project_root/project_name.desktop.in')),
                  ('share/quickly/templates/ubuntu-flash-game/project_root', glob.glob('data/templates/ubuntu-flash-game/project_root/project_name.desktop.in'))],
      cmdclass={'install': InstallAndUpdateDataDirectory})

