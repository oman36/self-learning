# If you don't want characters prefaced by '\' to be interpreted as special characters,
# you can use raw strings by adding an 'r' before first quote:
print('C:\some\name')
# C:\some
# ame
print(r'C:\some\name')  # note the r before the quote
# C:\some\name

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")  # slash at the end of line prevent end of line auto including

# Strings can be concatenated by '+'
'one ' + 'two' == 'one two'

# Strings can be repeated by '*'
'one,' * 2 == 'one,one,'

# String leterals can be concatenated without '+'
'one ' 'two' == 'one two'

# This feature is particularly useful when you want to break long strings:
text = ('Put several strings within parentheses '
        'to have them joined together.')

# Strings can be indexed
word = 'Python'
print(word[1])
# y

print(word[0])
# P

print(word[-0])
# P

print(word[-1])
# n

print(word[2:5])
# tho

print(word[-3:-1])
# ho

print(word[42:45])
# 


# The built-in function len() returns the length of a string:
print(len(word))
# 6

# stings are immutable:
try:
    word[2] = 'h'
except TypeError as e:
    print(e.__str__())
# 'str' object does not support item assignment
