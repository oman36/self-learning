# The __init__.py files are required to make Python treat the directories as containing packages. In the simplest
# case, __init__.py can just be an empty file, but it can also execute initialization code for the package or set the
# __all__ variable.

# see files import#.py

# Note that when using from package import item, the item can be either a submodule (or subpackage) of the package,
# or some other name defined in the package, like a function, class or variable. The import statement first tests
# whether the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails
# to find it, an ImportError exception is raised.

# Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last must be a package;
# the last item can be a module or a package but can’t be a class or function or variable defined in the previous
# item.

# if a package’s `__init__.py` code defines a list named `__all__`, it is taken to be the list of module names that
# should be imported when `from package import *` is encountered.
