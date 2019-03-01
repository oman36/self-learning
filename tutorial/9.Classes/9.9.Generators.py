def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


print(reverse)
# <function reverse at 0x7fd1fdb6de18>

golf = reverse('golf')
print(golf)
# <generator object reverse at 0x7fd1fda8cc50>

for char in golf:
    print(char)
# f
# l
# o
# g


def reverse2(data):
    yield from reverse(data)


for char in reverse2('golf'):
    print(char)
# f
# l
# o
# g

files = dict()


def generator_1(filename):
    with open(filename, 'w') as f:
        files['main'] = f
        for i in range(10):
            yield 'hei ' + str(i)


for i, string in enumerate(generator_1('test')):
    print(files['main'].closed)
    if i == 1:
        break
# False
# False

print(next(generator_1('test')))
# hei 0

# Will be closed after looping, it does not matter that not all values was yielded.
print(files['main'].closed)
# True


def generator_2(filename):
    f = open(filename, 'w')
    files['main'] = f
    for i in range(10):
        yield 'hei ' + str(i)


for i, string in enumerate(generator_2('test')):
    print(files['main'].closed)
    if i == 1:
        break
# False
# False

# Will be not closed after looping.
print(files['main'].closed)
# False


print(next(generator_2('test')))
# hei 0


def manual_generator(initial=0):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                new = yield initial
                initial += 1 + (new or 0)
            except Exception as e:
                print('Error: ' + e.__str__())
    finally:
        print("Don't forget to clean up when 'close()' is called.")


generator = manual_generator(10)
print(next(generator))
# 10
print(generator.send(-2))
# 9
print(next(generator))
# 10
print(generator.send(None))
# 11
print(next(generator))
# 12
print(generator.send(7))
# 20
print(next(generator))
# 21
generator.throw(TypeError, "spam")
# Error: spam
print(next(generator))
# 22
generator.close()
# Don't forget to clean up when 'close()' is called.
