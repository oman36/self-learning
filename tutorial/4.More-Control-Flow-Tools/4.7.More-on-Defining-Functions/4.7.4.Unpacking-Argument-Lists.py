list(range(3, 6))
# [3, 4, 5]
args = [3, 6]
# call with arguments unpacked from a list
list(range(*args))
# [3, 4, 5]


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
# -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

# kwargs dictionary must have strings as key only:
try:
    parrot(**{('volt', 'age'): 'one thousand', 'state': 'unknown'})
except TypeError as e:
    print(e.__str__())
# parrot() keywords must be strings

try:
    parrot(**{True: 'one trillion', 'state': 'favorite'})
except TypeError as e:
    print(e.__str__())
# parrot() keywords must be strings
