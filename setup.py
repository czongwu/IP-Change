# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

py2exe_options = {
    'incloudes': ['sip'],
    'dll_excloudes': ['MSVCP90.dll'],
    'compressed': 1,
    'optimize': 0,
    'ascii': 0,
    'bundle_files': 1
}

setup(
    name='批量修改',
    version='1.0',
    windows=['main-view.py'],
    zipfile=None,
    options={'py2exe': py2exe_options}

)