squares = [1, 4, 9, 16, 25]

# indexing returns the item:
print(squares[0])
# 1
print(squares[-1])
# 25

# slicing returns a new list:
new_list = squares[-3:]
print(new_list)
# [9, 16, 25]

# lists are mutable:
squares[2] = 36
print(squares)
# [1, 4, 36, 16, 25]

# You can also add new item at the end of the list, by using the `append()` method:
squares.append(49)
print(squares)
# [1, 4, 36, 16, 25, 49]

# You can replace some values:
squares[2:4] = [64, 81]
print(squares)
# [1, 4, 64, 81, 25, 49]

# You can remove some values:
squares[2:4] = []
print(squares)
# [1, 4, 25, 49]

