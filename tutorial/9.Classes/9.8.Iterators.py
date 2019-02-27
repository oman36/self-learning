s = 'abc'
it = iter(s)
print(it)
# <iterator object at 0x00A1DB50>

print(next(it))
# a

print(next(it))
# b

print(next(it))
# c

try:
    print(next(it))
except StopIteration as e:
    print('StopIteration was catch')
# StopIteration was catch

# For add iterator behavior to your classes: define an `__iter__()` method
# which returns an object with a `__next__()` method.
# If the class defines `__next__()`, then `__iter__()` can just return `self`:
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
