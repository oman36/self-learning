# open() returns a file object, and is most commonly used with two arguments: open(filename, mode).
f = open(__file__, 'r')

# In text mode, the default when reading is to convert platform-specific line endings (\n on Unix, \r\n on Windows)
# to just \n. When writing in text mode, the default is to convert occurrences of \n back to platform-specific line
# endings.

# It is good practice to use the with keyword when dealing with file objects.
# The advantage is that the file is properly closed after its suite finishes,
# even if an exception is raised at some point.
# Using with is also much shorter than writing equivalent try-finally blocks:
with open('/etc/hosts', 'r') as f2:
    read_data = f2.read()
print(f2.closed)
# True

# If you’re not using the with keyword, then you should call f.close() to close the file and immediately free up any
# system resources used by it. If you don’t explicitly close a file, Python’s garbage collector will eventually
# destroy the object and close the open file for you, but the file may stay open for a while. Another risk is that
# different Python implementations will do this clean-up at different times.

print(repr(f.read(98)))
# # open() returns a file object, and is most commonly used with two arguments: open(filename, mode)


# If the end of the file has been reached, f.read() will return an empty string (''):
f.read()
print(repr(f.read()))
# ''

# For reading lines from a file, you can loop over the file object.
# This is memory efficient, fast, and leads to simple code:
#
# !!! IMPORTANT !!! lines in variable `line` save with '\n'
for line in open(__file__, 'r'):
    print(line, end='')
    break
# # open() returns a file object, and is most commonly used with two arguments: open(filename, mode).

# If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().

# f4.write(string) writes the contents of string to the file, returning the number of characters written.
f4 = open('for-write.log', 'w')
print(f4.write('Test\n'))
# 5

# f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes
# from the beginning of the file when in binary mode and an opaque number when in text mode:
print(f4.tell())
# 5

# To change the file object’s position, use f.seek(offset, from_what).
# The position is computed from adding offset to a reference point;
# the reference point is selected by the from_what argument.
# A from_what value of 0 measures from the beginning of the file,
# 1 uses the current file position,
# and 2 uses the end of the file as the reference point.
# from_what can be omitted and defaults to 0, using the beginning of the file as the reference point.
f5 = open('workfile', 'wb+')
print(f5.write(b'0123456789abcdef'))
# 16

# Go to the 6th byte in the file:
print(f5.seek(5))
# 5

print(f5.read(1))
# b'5'

# Go to the 3rd byte before the end:
print(f5.seek(-3, 2))
# 13

print(f5.read(1))
# b'd'

# !!! IMPORTANT !!! In text files (those opened without a b in the mode string), only seeks relative to the beginning
#  of the file are allowed (the exception being seeking to the very file end with seek(0, 2)) and the only valid
# offset values are those returned from the f.tell(), or zero. Any other offset value produces undefined behaviour.

print(f5.isatty())
# False

#JSON
import json
print(repr(json.dumps([1, 'simple', 'list'])))
# '[1, "simple", "list"]'
