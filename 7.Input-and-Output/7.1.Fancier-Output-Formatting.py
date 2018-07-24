# So far we’ve encountered two ways of writing values: expression statements and the print() function. (A third way
# is using the write() method of file objects; the standard output file can be referenced as sys.stdout.

# There are several ways to format output:

# 1. To use formatted string literals, begin a string with f or F before the opening quotation mark or triple
# quotation mark. Inside this string, you can write a Python expression between { and } characters that can refer to
# variables or literal values:
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
# Results of the 2016 Referendum

# The str.format() method of strings requires more manual effort. You’ll still use { and } to mark where a variable
# will be substituted and can provide detailed formatting directives, but you’ll also need to provide the information
# to be formatted:
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes/(yes_votes+no_votes)
print('>{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
# > 42572654 YES votes  49.67%

# When you don’t need fancy output but just want a quick display of some variables for debugging purposes,
# you can convert any value to a string with the repr() or str() functions.
print(repr(percentage))

# The str() function is meant to return representations of values which are fairly human-readable, while repr() is
# meant to generate representations which can be read by the interpreter (or will force a SyntaxError if there is no
# equivalent syntax). For objects which don’t have a particular representation for human consumption, str() will
# return the same value as repr().

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
print(repr(hello))
# 'hello, world\n'

import math
print(f'The value of pi is approximately {math.pi:.3f}.')
# The value of pi is approximately 3.142.

# Passing an integer after the ':' will cause that field to be a minimum number of characters wide.
# This is useful for making columns line up:
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10}')
# Sjoerd     ==>       4127
# Jack       ==>       4098
# Dcab       ==>       7678

# Other modifiers can be used to convert the value before it is formatted.
# '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
# My hovercraft is full of eels.
print('My hovercraft is full of {animals !r}.')
# My hovercraft is full of 'eels'.

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"

print('{0} and {1}'.format('spam', 'eggs'))
# spam and eggs

print('{1} and {1}'.format('spam', 'eggs'))
# eggs and eggs

print('{1} and {0}'.format('spam', 'eggs'))
# eggs and spam

print('This {food} is {adjective}.'.format(food='egg', adjective='absolutely horrible'))
# This egg is absolutely

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
# The story of Bill, Manfred, and Georg.

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
# The story of Bill, Manfred, and Georg.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}\nSjoerd: {0[Sjoerd]:d}\nDcab: {0[Dcab]:d}'.format(table))
# Jack: 4098
# Sjoerd: 4127
# Dcab: 8637678

# This is particularly useful in combination with the built-in function vars(), which returns a dictionary containing
# all local variables.

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125
#  6  36  216
#  7  49  343
#  8  64  512
#  9  81  729
# 10 100 1000

# Old style printf:
import math
print('The value of pi is approximately %5.3f.' % math.pi)
# The value of pi is approximately 3.142.
