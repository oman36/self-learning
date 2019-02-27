print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))
# True

print((1, 2, ('aa', 'ab')) > (1, 2, ('aa', 'a'), 4))
# True

# !!! IMPORTANT !!! Note that comparing objects of different types with < or > is legal provided that the objects
# have appropriate comparison methods. For example, mixed numeric types are compared according to their numeric
# value, so 0 equals 0.0, etc. Otherwise, rather than providing an arbitrary ordering, the interpreter will raise a
# TypeError exception.
