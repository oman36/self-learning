try:
    x = int('NaN')
except ValueError:
    print("Oops!  That was no valid number.  Try again...")
# Oops!  That was no valid number.  Try again...

import random

try:
    if 0 == random.randint(0, 1):
        print('NaN')
        x = int('NaN')
    else:
        print('2 / 0')
        x = 2 / 0
except (ValueError, ZeroDivisionError):
    print("Any of error from tuple will be handled")


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
# B
# C
# D

for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")
# B
# B
# B


# The last except clause may omit the exception name(s), to serve as a wildcard. Use this with extreme caution,
# since it is easy to mask a real programming error in this way! It can also be used to print an error message and
# then re-raise the exception (allowing a caller to handle the exception as well):
import sys

try:
    try:
        x = 2 / 0
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise  # last error wil be raised
except:
    pass
# Unexpected error: <class 'ZeroDivisionError'>

# The try … except statement has an optional else clause, which, when present, must follow all except clauses.
# It is useful for code that must be executed if the try clause does not raise an exception.
# For example:
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# The use of the else clause is better than adding additional code to the try clause because it avoids accidentally
# catching an exception that wasn’t raised by the code being protected by the try … except statement.

try:
    raise Exception('spam', 'eggs')
except (Exception, TypeError) as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    x, y = inst.args
    print('x =', x)
    print('y =', y)
# <class 'Exception'>
# ('spam', 'eggs')
# ('spam', 'eggs')
# x = spam
# y = eggs
