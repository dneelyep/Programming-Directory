import unittest
import os
import sys
import glob

proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","project_root"))
sys.path.insert(0, proj_root)
import logging
logging.debug(sys.path[0])

from python_lib.preferences import User_dict, preferences

# Clean up after ourselves
for f in glob.glob(os.path.join(proj_root, 'python_lib', '*.pyc')):
    os.remove(f)

class TestUser_dict(unittest.TestCase):

    def test_interface(self):
        foo = User_dict()
        # provides gobject signals
        self.assertTrue(callable(foo.emit))
        self.assertTrue(callable(foo.connect))
        
        # provides load and save
        self.assertTrue(callable(foo.load))
        self.assertTrue(callable(foo.save))

    def test_update_from_dict(self):
        foo = User_dict()
        bar = {'pluto':2}
        foo.update(bar)
        self.assertEqual(foo.get('pluto'), 2)

    def test_update_from_pairs(self):
        a = User_dict([['position', 'Public Relations'], ['name', 'Jayne Cobb']])
        b = {'name': 'Jayne Cobb', 'position': 'Public Relations'}
        self.assertEqual(a, b)

    def test_serialisation(self):
        # used in couchdb for instance
        import json
        a = User_dict([['position', 'Public Relations'], ['name', 'Jayne Cobb']])
        b = {'name': 'Jayne Cobb', 'position': 'Public Relations'}
        c =  json.loads(json.dumps(a))
        self.assertEqual(a, c)

    def test__setitem__(self):
        foo = User_dict()
        foo[2] = 3
        self.assertEqual(foo.get(2), 3)

    def test__delitem__(self):
        foo = User_dict()
        foo[2] = 3
        self.assertEqual(foo.get(2), 3)
        del foo[2]
        self.assertEqual(foo.get(2, 'default'), 'default')

    def test__getitem__(self):
        foo = User_dict()
        foo[2] = 3
        self.assertEqual(foo[2], 3)

class TestSignals(unittest.TestCase):

    def setUp(self):
        self.foo = User_dict()
        self.messages = []
        self.foo.connect('changed', self.callback)

    def callback(self, *args):
        self.messages.append(args)

    def test_update_with_additions(self):
        bar = {'foobar': 7}
        self.foo.update({'foobar': 7})
        self.assertEqual(self.messages[0][1], ('foobar',))
        self.foo.update({'fooey': 2})
        self.assertEqual(self.messages[1][1], ('fooey',))
        self.assertEqual(len(self.messages), 2)

    def test_update_with_changes(self):
        bar = {'foobar': 7}
        self.foo.update({'foobar': 7})
        self.assertEqual(self.messages[0][1], ('foobar',))
        self.foo.update({'foobar': 8})
        self.assertEqual(self.messages[1][1], ('foobar',))
        self.assertEqual(len(self.messages), 2)

    def test_update_without_changes(self):
        bar = {'foobar': 7}
        self.foo.update({'foobar': 7})
        self.assertEqual(self.messages[0][1], ('foobar',))
        self.foo.update({'foobar': 7})
        self.assertEqual(len(self.messages), 1)

    def test_update_with_several_items(self):
        data = {'pluto': 7, 'mickey': 8, 'minnie': 9}
        self.foo.update(data)
        self.assertEqual(self.messages[0][1], ('mickey', 'minnie', 'pluto'))
        self.assertEqual(len(self.messages), 1)
        data = {'mickey': 1, 'minnie': 2}
        self.foo.update(data)
        self.assertEqual(self.messages[1][1], ('mickey', 'minnie'))
        self.assertEqual(len(self.messages), 2)

    def test__setitem__with_additions(self):
        self.foo['too'] = 3
        self.assertEqual(self.messages[0][1], ('too',))

    def test__setitem__with_changes(self):
        self.foo['too'] = 3
        self.assertEqual(self.messages[0][1], ('too',))
        self.assertEqual(len(self.messages), 1)
        self.foo['too'] = 4
        self.assertEqual(len(self.messages), 2)

    def test__setitem__without_changes(self):
        self.foo['too'] = 3
        self.assertEqual(self.messages[0][1], ('too',))
        self.assertEqual(len(self.messages), 1)
        self.foo['too'] = 3
        self.assertEqual(len(self.messages), 1)

class TestPreferences(unittest.TestCase):
    ''' this one we really need '''

    def setUp(self):
        self.messages = []
        preferences.connect('changed', self.callback)

    def callback(self, *args):
        self.messages.append(args)

    def test_update(self):
        preferences.update({'foobar': 7})
        self.assertEqual(self.messages[0][1], ('foobar',))
        self.assertEqual(len(self.messages), 1)
        # preferences persist so we need to clean our changes
        del preferences['foobar']

    def test__setitem__(self):
        preferences['too'] = 3
        self.assertEqual(self.messages[0][1], ('too',))
        self.assertEqual(len(self.messages), 1)
        # preferences persist so we need to clean our changes
        del preferences['too']

if __name__ == '__main__':
    unittest.main()
