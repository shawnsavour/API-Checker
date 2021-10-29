from distutils.core import setup 
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 2, 'compressed': True}},
    data_files = [('', ['pepe.ico']),('driver',['driver/chromedriver.exe','driver/phantomjs.exe'])],
    windows = [{'script': "checkAPI.py", "icon_resources": [(1, u"pepe.ico")]} ],
    zipfile = None,
)