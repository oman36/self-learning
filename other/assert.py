# RULES:
#   Python’s assert statement is a debugging aid that tests a condition as an internal self-check in your program.
#   Asserts should only be used to help developers identify bugs. They’re not a mechanism for handling run-time errors.
#   Asserts can be globally disabled with an interpreter setting.


# next line will print "False" if python start with flag -O (big o)
# and if `__debug__` is `False`, assert will be never execute
print(__debug__)


# next line will do nothing
assert 1 == 1

try:
    assert 1 == 2
except AssertionError as e:
    print(e.__str__())  # will print empty line
#

try:
    assert 1 == 2, 'Error message'
except AssertionError as e:
    print(e.__str__())
# Error message
