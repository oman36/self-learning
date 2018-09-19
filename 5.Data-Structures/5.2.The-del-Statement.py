a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]
print(a)
# [1, 66.25, 333, 333, 1234.5]

del a[2:4]
print(a)
# [1, 66.25, 1234.5]

del a[:]
print(a)
# []

del a
# Referencing the name a hereafter is an error
try:
    print(a)
except NameError as err:
    print(err.__str__())
# name 'a' is not defined
