def parent_func():
    variable = 'Value'
    other_var = 'Val2'

    if other_var == 'Val1':
        variable = 'Other value'

    def nested_func(a, b, third_val=2):
        return variable == a or third_val == b

    return nested_func


func = parent_func()

print(repr(func.__name__))
# 'nested_func'
print(repr(func.__qualname__))
# 'parent_func.<locals>.nested_func'
print(repr(func.__module__))
# '__main__'
print(repr(func.__defaults__))
# (2,)
print(repr(func.__kwdefaults__))
# None
# None
print(len(func.__closure__))
# 1
print(repr(func.__closure__[0].cell_contents))
# 'Value'
print(func.__code__.co_cellvars)
# ()
print(func.__code__.co_freevars)
# ('variable',)
print(parent_func.__code__.co_cellvars)
# ('variable',)
print(parent_func.__code__.co_freevars)
# ()
