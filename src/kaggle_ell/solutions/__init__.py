import os
from os.path import dirname, basename, isfile, join
import glob

import sys
from setuptools import find_packages
from pkgutil import iter_modules

def find_modules(path):
    modules = set()
    for pkg in find_packages(path):
        modules.add(pkg)
        pkgpath = path + '/' + pkg.replace('.', '/')
        if sys.version_info.major == 2 or (sys.version_info.major == 3 and sys.version_info.minor < 6):
            for _, name, ispkg in iter_modules([pkgpath]):
                if not ispkg:
                    modules.add(pkg + '.' + name)
        else:
            for info in iter_modules([pkgpath]):
                if not info.ispkg:
                    modules.add(pkg + '.' + info.name)
    return modules

__HERE__ = os.path.dirname(os.path.abspath(__file__))

__all__ = find_modules(__HERE__)