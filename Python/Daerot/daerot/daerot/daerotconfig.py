# -*- coding: utf-8 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

# THIS IS Daerot CONFIGURATION FILE
# YOU CAN PUT THERE SOME GLOBAL VALUE
# Do not touch until you know what you're doing.
# you're warned :)

# where your project will head for your data (for instance, images and ui files)
# by default, this is ../data, relative your trunk layout
__daerot_data_directory__ = '../data/'


import os

class project_path_not_found(Exception):
    pass

def getdatapath():
    """Retrieve daerot data path

    This path is by default <daerot_lib_path>/../data/ in trunk
    and /usr/share/daerot in an installed version but this path
    is specified at installation time.
    """

    # get pathname absolute or relative
    if __daerot_data_directory__.startswith('/'):
        pathname = __daerot_data_directory__
    else:
        pathname = os.path.dirname(__file__) + '/' + __daerot_data_directory__

    abs_data_path = os.path.abspath(pathname)
    if os.path.exists(abs_data_path):
        return abs_data_path
    else:
        raise project_path_not_found

