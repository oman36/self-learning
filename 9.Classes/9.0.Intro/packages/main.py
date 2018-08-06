import first
import second
import the_module
try:
    print('main', the_module.variable)
except AttributeError as err:
    print(f'Exception {err} in main')
import third
