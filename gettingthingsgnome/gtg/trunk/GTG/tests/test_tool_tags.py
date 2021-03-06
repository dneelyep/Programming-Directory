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

'''
Tests for the tags utilities
'''

import unittest

from GTG.tools.tags import *



class TestTagsUtils(unittest.TestCase):
    '''
    Tests for the tags utilities
    '''
    
    def test_extract_tags_from_text(self):
        '''
        Test for extracting tags from a string
        '''
        tests = (\
                 ("@mamma mia", ["@mamma"]),
                 ("vive le @roy", ["@roy"]),
                 ("hey @mr. jack!", ["@mr"]),
                 ("no @emails allowed: invernizzi.l@gmail.com", ["@emails"]),
                 ("and no @@diff stuff", []),
                 ("@we @do @love @tags!", ["@we", "@do", "@love", "@tags"]),
                )
        for text, tags in tests:
            self.assertEqual(extract_tags_from_text(text), tags)





def test_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestTagsUtils)

