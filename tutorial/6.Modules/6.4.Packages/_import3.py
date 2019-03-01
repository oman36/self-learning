from main_package.sub_package.some_nasted_module import another_func
# This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows:

another_func()
# another_func was called
del another_func

from main_package.sub_package.some_nasted_module import another_func

another_func()
# another_func was called
