# annotations don't do anything
def fun(ham: str, eggs: str = 'eggs') -> str:
    return ham + ' and ' + eggs


print(fun.__annotations__)
# {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
