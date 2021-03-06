# Important warning: The default value is evaluated only once.
# This makes a difference when the default is a mutable object such as a list,
# dictionary, or instances of most classes.
# For example, the following function accumulates the arguments passed to it on subsequent calls:
def f(a, l=[]):
    l.append(a)
    return l


print(f(1))
# [1]
print(f(2))
# [1, 2]
print(f(3))
# [1, 2, 3]


# If you don’t want the default to be shared between subsequent calls,
# you can write the function like this instead:
def fu(a, li=None):
    if li is None:
        li = []
    li.append(a)
    return li


print(fu(1))
# [1]
print(fu(2))
# [2]
print(fu(3))
# [3]


def fun(a, b):
    print(a, b)

fun(b=1, *(2,))
# 2 1

try:
    fun(a=1, *(2,))
except TypeError as e:
    print(e)
# fun() got multiple values for keyword argument 'a'

fun(1, *(2,))
# 1 2
