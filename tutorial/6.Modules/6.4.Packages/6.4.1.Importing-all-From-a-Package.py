# The __init__.py files are required to make Python treat the directories as containing packages. In the simplest
# case, __init__.py can just be an empty file, but it can also execute initialization code for the package or set the
# __all__ variable.

from main_package import *

some_module.defined_in_init_func()
# File main_package.some_module.py doesn't loaded

try:
    some_module.defined_in_file_func()
except AttributeError as error:
    print(error.__str__())
# module 'main_package.some_module' has no attribute 'defined_in_file_func'

print(valid_module.variable)
# 120

# variable `__all__` doesn't contain `not_defined_module`, so:
try:
    not_defined_module.exist_func()
except NameError as error:
    print(error.__str__())
# name 'not_defined_module' is not defined

# But we can load the module directly:
from main_package import not_defined_module
not_defined_module.exist_func()
# Function exists

# sub_package's modules don't load by `from main_package import *`:
try:
    sub_package.some_nasted_module.another_func()
except AttributeError as error:
    print(error.__str__())
# module 'main_package.sub_package' has no attribute 'some_nasted_module'

# every sub package should be loaded manually:
from main_package.sub_package import *
sub_package.some_nasted_module.another_func()
# another_func was called

# !!! IMPORTANT !!! Remember, there is nothing wrong with using `from Package import specific_submodule`! In fact,
# this is the recommended notation unless the importing module needs to use submodules with the same name from
# different packages
