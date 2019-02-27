# You can also write relative imports, with the from module import name form of import statement.
from . import main_package
from .. import fibo

# !!! IMPORTANT !!! Note that relative imports are based on the name of the current module. Since the name of the
# main module is always "__main__", modules intended for use as the main module of a Python application must always
# use absolute imports.
