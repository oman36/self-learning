from main_package.sub_package import some_nasted_module
# This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows:
some_nasted_module.another_func()
