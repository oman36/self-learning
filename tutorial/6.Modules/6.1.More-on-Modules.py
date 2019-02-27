# There is a variant of the import statement that imports names from a module directly into the importing module’s
# symbol table. For example:
from fibo import fib, fib2
fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# This imports all names except those beginning with an underscore (_):
from fibo import *
fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

import fibo as fib
fib.fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from fibo import fib as fibonacci
fibonacci(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# Note
# For efficiency reasons, each module is only imported once per interpreter session. Therefore, if you change your
# modules, you must restart the interpreter – or, if it’s just one module you want to test interactively,
# use importlib.reload(), e.g. import importlib; importlib.reload(modulename).



import sys
for path in sys.path:
    # sys.path is initialized from these locations:
    #  - The directory containing the input script (or the current directory when no file is specified).
    #  - PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
    #  - The installation-dependent default.
    print(path)
    # /var/www/python/self-learning/6.Modules
    # /usr/lib/python35.zip
    # /usr/lib/python3.5
    # /usr/lib/python3.5/plat-x86_64-linux-gnu
    # /usr/lib/python3.5/lib-dynload
    # /home/neoman/www/python/self-learning/venv/lib/python3.5/site-packages
    # /home/neoman/www/python/self-learning/venv/lib/python3.5/site-packages/setuptools-39.1.0-py3.5.egg
    # /home/neoman/www/python/self-learning/venv/lib/python3.5/site-packages/pip-10.0.1-py3.5.egg

# After initialization, Python programs can modify sys.path.
# The directory containing the script being run is placed at the beginning of the search path

# To speed up loading modules, Python caches the compiled version of each module in the __pycache__ directory under
# the name module.version.pyc, where the version encodes the format of the compiled file; For example, in CPython
# release 3.3 the compiled version of spam.py would be cached as `__pycache__/spam.cpython-33.pyc`.
