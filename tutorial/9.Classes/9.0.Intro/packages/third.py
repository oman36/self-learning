import the_module

try:
    print('third', the_module.variable)
except AttributeError as err:
    print(f'Exception {err} in third')

the_module.variable = 76
