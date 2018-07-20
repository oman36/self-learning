print(3 == 3)
# True

print([3] == [3])
# True

print(3 is 3)
# True

# this only matters for mutable objects like lists:
print([3] is [3])
# False

# Comparisons can be chained.
# For example, a < b == c tests whether a is less than b and moreover b equals c.

# `A and not B or C`
# is equivalent to
# `(A and (not B)) or C`

# If `A` and `C` are true but `B` is false, `A and B and C` does not evaluate the expression `C`:
def func(string:str, flag:bool = False) -> bool:
    print(string, flag)
    return flag


if func('first', True) and func('second', False) and func('third', False):
    pass
# first True
# second False

# `or` allows to assign first not empty value to variable:
empty_string, the_none, zero, empty_set, empty_list, string2, string3 =\
    '', None, 0, (), [], 'Trondheim', 'Hammer Dance'
non_null = (empty_string or the_none or zero or empty_set or empty_list or string2 or string3)
print(non_null)
# Trondheim
