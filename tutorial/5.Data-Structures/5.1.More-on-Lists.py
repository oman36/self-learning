print([x ** 2 for x in range(10)])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# more readable
print([
    (x, y)
    for x in [1, 2, 3]
    for y in [3, 1, 4]
    if x != y
])
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print(combs)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# EXAMPLES
vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled:
print([x * 2 for x in vec])
# [-8, -4, 0, 4, 8]

# filter the list to exclude negative numbers:
print([x for x in vec if x >= 0])
# [0, 2, 4]

# apply a function to all the elements:
print([abs(x) for x in vec])
# [4, 2, 0, 2, 4]

# call a method on each element:
print([number.zfill(6) for number in ['1', '20', '340']])
# ['000001', '000020', '000340']

# create a list of 2-tuples like (number, square)
print([(x, x ** 2) for x in range(6)])
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# the tuple must be parenthesized, otherwise an error is raised:
#
#     [x, x**2 for x in range(6)]
#


# flatten a list using a list comp with two 'for'
print([num for elem in [[1, 2, 3], [4, 5, 6], [7, 8, 9]] for num in elem])
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# flatten a list using a list comp with two 'for'
print([
    num
    for group in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for num in group
])
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

broken_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, ],  # <- three numbers
]

print([[row[col] for row in matrix] for col in range(len(matrix[0]))])
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# you should prefer built-in functions to complex flow statements
print(list(zip(*matrix)))
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

print(list(zip(*broken_matrix)))
# [[1, 5, 9], [2, 6, 10], [3, 7, 11]]

# unpacking:
row1, row2, row3 = matrix
print(row2)
# [5, 6, 7, 8]

# lists can be multiplied (their values will be repeated), but it not safe
danger_list = [{'value': 'original'}] * 3
safe_list = [{'value': 'original'} for _ in range(3)]

print(danger_list)
# [{'value': 'original'}, {'value': 'original'}, {'value': 'original'}]
print(safe_list)
# [{'value': 'original'}, {'value': 'original'}, {'value': 'original'}]

danger_list[0]['value'] = 'new'
print(danger_list)
# [{'value': 'new'}, {'value': 'new'}, {'value': 'new'}]

safe_list[0]['value'] = 'new'
print(safe_list)
# [{'value': 'new'}, {'value': 'original'}, {'value': 'original'}]

danger_list2 = ['val'] * 3
safe_list2 = ['val' for _ in range(3)]

print(danger_list2)
# ['val', 'val', 'val']
print(safe_list2)
# ['val', 'val', 'val']

danger_list2[0] = 'new'
print(danger_list2)
# ['new', 'val', 'val']

safe_list2[0] = 'new'
print(safe_list2)
# ['new', 'val', 'val']
