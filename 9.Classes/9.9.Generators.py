def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

print(reverse)
# <function reverse at 0x7fd1fdb6de18>

print(reverse("Word"))
# <generator object reverse at 0x7fd1fda8cc50>

for char in reverse('golf'):
    print(char)
# f
# l
# o
# g
