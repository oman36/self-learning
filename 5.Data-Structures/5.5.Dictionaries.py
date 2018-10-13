tel = {'jack': 4098, 'sape': 4139}

print(tel['jack'])
# 4098

tel['guido'] = 4127
print(tel)
# {'jack': 4098, 'sape': 4139, 'guido': 4127}

del tel['sape']
# {'jack': 4098, 'guido': 4127}

print(list(tel))
# ['jack', 'guido']

# !!! IMPORTANT !!!
print(sorted(tel))
# ['guido', 'jack']

print('guido' in tel)
# True

print('fabio' in tel)
# False

print(4098 in tel)
# False

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
# !!! IMPORTANT !!! without order
print(dict(
    [('sape', 4139), ('guido', 4127), ('jack', 4098)]
))
# {'sape': 4139, 'guido': 4127, 'jack': 4098}
# or
# {'guido': 4127, 'jack': 4098, 'sape': 4139}
# ...

# Always true. Order doesn't matter:
print(
    dict({('sape', 4139), ('guido', 4127), ('jack', 4098)})
    ==
    dict((('sape', 4139), ('guido', 4127), ('jack', 4098)))
    ==
    dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    ==
    dict([['sape', 4139], ['guido', 4127], ['jack', 4098]])
    ==
    {'guido': 4127, 'jack': 4098, 'sape': 4139}
    ==
    dict(sape=4139, guido=4127, jack=4098)
)
# True

# dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
print({x: x**2 for x in (2, 4, 6)})
# {2: 4, 4: 16, 6: 36}

# !!! IMPORTANT !!!
print({True: 'a', 1: 'b', 1.0: 'c'})
# {True: 'c'}


class Base:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return repr(self.value)


class HashBroken(Base):
    def __hash__(self):
        return 1


class EqBroken(Base):
    def __eq__(self, other):
        return True

    def __hash__(self):
        return hash(self.value)


class Broken(Base):
    def __hash__(self):
        return 1

    def __eq__(self, other):
        return True


print({HashBroken('z'): 'a', HashBroken('x'): 'b'})
# {'z': 'a', 'x': 'b'}

print({EqBroken('z'): 'a', EqBroken('x'): 'b'})
# {'z': 'a', 'x': 'b'}

print({Broken('z'): 'a', Broken('x'): 'b'})
# {'z': 'b'}
