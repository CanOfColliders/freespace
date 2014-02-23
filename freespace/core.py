import sys

__title__ = 'freespace'
__version__ = '0.1'
__author__ = 'Michael Detzner'
__license__ = 'MIT'

if sys.platform == 'darwin' or sys.platform.startswith('linux'):
	from .nix import *

elif sys.platform == 'win32':
	from .win import *

from .convert import *
