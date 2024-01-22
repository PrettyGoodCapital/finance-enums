from os.path import abspath, join, dirname
from .finance_enums import lib

__version__ = "0.3.0"

def lib_path():
    return abspath(join(dirname(__file__), "finance_enums"))

def include_path():
    return abspath(join(lib_path(), "include"))

