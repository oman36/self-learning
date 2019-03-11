# Each value is an object, and therefore has a class (also called its type). It is stored as `object.__class__`.
the_list = list((2, 3))

print(the_list.__class__)
# <class 'list'>


class X:
    a = 1


Y = type('Y', (object,), dict(a=1))

Z = type('Y', (object,), dict(a=1))

for klass in (X, Y, Z):
    print(klass().__class__)
    print(klass.a)
# <class '__main__.X'>
# 1
# <class '__main__.Y'>
# 1
# <class '__main__.Y'>
# 1
