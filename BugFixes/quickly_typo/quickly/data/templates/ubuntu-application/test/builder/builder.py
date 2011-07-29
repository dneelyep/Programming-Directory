#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

import unittest
import sys
import os
import gtk
import inspect
import logging
import glob
logging.basicConfig(level=logging.DEBUG)

proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","project_root"))
sys.path.insert(0, proj_root)

from python_lib import Builder

# Clean up after ourselves
for f in glob.glob(os.path.join(proj_root, 'python_lib', '*.pyc')):
    os.remove(f)

# alias belongs in helpers, but it cannot be imported
def alias(alternative_function_name):
    '''see http://www.drdobbs.com/web-development/184406073#l9'''
    def decorator(function):
        '''attach alternative_function_name(s) to function'''
        if not hasattr(function, 'aliases'):
            function.aliases = []
        function.aliases.append(alternative_function_name)
        return function
    return decorator

class TestAlias(unittest.TestCase):

    def test_alias_is_in_helpers(self):
        # instead of importing alias check we have an exact copy
        str_alias = inspect.getsource(alias)
        fp = open(os.path.join(proj_root, 'python_lib', 'helpers.py'), 'r')
        str_helpers = fp.read()
        fp.close()

        self.assertTrue(str_alias in str_helpers)

class App():
    def __init__(self):
        self.messages = []
        
    def on_label_show(self, widget, data=None):
        self.messages.append('on_label_show')

    @alias('on_tool_foo_activated')
    @alias('on_btn_foo_clicked')
    def on_mnu_foo_activated(self, widget, data=None):
        self.messages.append('on_mnu_foo_activated')

    # safe to decorate before and after, even duplicates
    @alias('asterix')
    @alias('mickey mouse')
    def cartoon(self):
        pass
    miffy = cartoon
    asterix = cartoon
    doraemon = cartoon

    # glade does not have on_window_show
    def on_window_show(self, widget, data=None):
        self.messages.append('on_window_show')

    def window_show_cb(self, widget, data=None):
        self.messages.append('window_show_cb')

class App2():
    def __init__(self):
        self.messages = []

    @alias('on_window_show')
    def foo(self, widget, data=None):
        self.messages.append('called by alias')

class TestBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = Builder.Builder()
        self.builder.add_from_file(os.path.join(os.path.dirname(__file__), 'test.ui'))
        self.widget_keys = ['1wind-o w/3', 'filefilter', 'label',
        'wind?o-w two', 'wind_o_w_two', 'window'] # sorted list

    def test_interface(self):
        builder = dir(gtk.Builder)
        
        # sanity test
        self.assertTrue('add_from_file' in builder)
        
        # any name clashes ?
        self.assertTrue('widgets' not in builder)
        self.assertTrue('get_ui' not in builder)
        self.assertTrue('get_name' not in builder)
        self.assertTrue('connections' not in builder)
        self.assertTrue('default_handler' not in builder)
        
        
        self.assertTrue('glade_handler_dict' not in builder)
        self.assertTrue('_reverse_widget_dict' not in builder)

    def test_ui_iterate(self):
        ui = self.builder.get_ui()
        objs = list(ui)
        objs2 = []
        for obj in ui:
            objs2.append(obj)
        self.assertTrue(len(objs) == 6)
        self.assertEqual(objs, objs2)

        objs3 = self.builder.get_objects()
        objs.sort()
        objs3.sort()
        self.assertEqual(objs, objs3)

    def test_ui_dot_access(self):
        ui = self.builder.get_ui()

        attribute_names = dir(ui)
        public_attribute_names = [x for x in attribute_names if x[0] != '_']
        public_attribute_names.sort()
        expected = self.widget_keys
        self.assertEqual(public_attribute_names, expected)
        # we also expect an unusual one
        self.assertTrue('_wind_o_w_3' in attribute_names)

        self.assertEqual(ui.filefilter, self.builder.get_object('filefilter'))
        self.assertEqual(ui.window, self.builder.get_object('window'))
        self.assertEqual(ui.label, self.builder.get_object('label'))
        self.assertEqual(ui.wind_o_w_two, self.builder.get_object('wind_o_w_two'))
        # simple dot access via name mangle with no clash
        self.assertEqual(ui._wind_o_w_3, self.builder.get_object('1wind-o w/3'))
        # name clash prevents simple dot access
        self.assertEqual(getattr(ui, 'wind?o-w two'), self.builder.get_object('wind?o-w two'))
        #confirm clash did not hide a widget
        self.assertTrue(getattr(ui, 'wind?o-w two') != ui.wind_o_w_two)

    def test_ui_dictionary_access(self):
        ui = self.builder.get_ui()
        self.assertEqual(ui['filefilter'], self.builder.get_object('filefilter'))
        self.assertEqual(ui['window'], self.builder.get_object('window'))
        self.assertEqual(ui['label'], self.builder.get_object('label'))
        self.assertEqual(ui['wind?o-w two'], self.builder.get_object('wind?o-w two'))
        self.assertEqual(ui['wind_o_w_two'], self.builder.get_object('wind_o_w_two'))
        self.assertEqual(ui['1wind-o w/3'],  self.builder.get_object('1wind-o w/3'))

    def test_dictionary_access_to_builder(self):
        # expected glade handlers
        glade_handler_dict = {'on_label_show': None,
         'window_show_cb': None}
        
        builder_keys = self.builder.widgets.keys()
        builder_keys.sort()
        self.assertEqual(builder_keys, self.widget_keys)
        self.assertEqual(self.builder.glade_handler_dict, glade_handler_dict)

    def test_dictionary_access_to_callback_obj(self):
        app = App()
        dict_callback_obj = Builder.dict_from_callback_obj(app)
        actual = dict_callback_obj.keys()
        actual.sort()
        expected = ['__init__', 'asterix', 'cartoon','doraemon',
         'mickey mouse', 'miffy', 'on_btn_foo_clicked', 'on_label_show',
         'on_mnu_foo_activated', 'on_tool_foo_activated', 'on_window_show',
         'window_show_cb']
        self.assertEqual(actual, expected)

    def test_connect_glade(self):
        app = App()
        self.builder.connect_signals(app)
        
        label = self.builder.get_object('label')
        label.emit('show')
        self.assertEqual(app.messages, ['on_label_show'])

        window = self.builder.get_object('window')
        window.emit('show')
        self.assertEqual(app.messages, ['on_label_show', 'window_show_cb'])

    def test_connect_auto(self):
        app = App()
        Builder.auto_connect_by_name(app, self.builder)

        # glade does not have on_window_show
        window = self.builder.get_object('window')
        window.emit('show')
        self.assertEqual(app.messages, ['on_window_show'])

    def test_alias(self):
        app = App()
        dict_callback_obj = Builder.dict_from_callback_obj(app)
        expected = app.on_mnu_foo_activated

        for name in ['on_mnu_foo_activated',
                     'on_tool_foo_activated', 
                     'on_btn_foo_clicked']:
            self.assertEqual(dict_callback_obj[name] , expected)

    def test_connect_alias(self):
        app = App2()
        Builder.auto_connect_by_name(app, self.builder)

        window = self.builder.get_object('window')
        window.emit('show')
        self.assertEqual(app.messages, ['called by alias'])

unittest.main()
