import copy

list_ = [[1, 2, 3], [4, 5, 6, ], [7, 8, 9]]

list2 = list_
print(list_ is list2)
# True

list_[0][0] = 1000
print(list2)
# [[1000, 2, 3], [4, 5, 6, ], [7, 8, 9]]

list3 = list(list_)
print(list_ is list3)
# False

# but:
list_[0][0] = 2000
print(list3)
# [[2000, 2, 3], [4, 5, 6, ], [7, 8, 9]]


list4 = copy.copy(list_)
print(list_ is list3)
# False

# but:
list_[0][0] = 300
print(list4)
# [[300, 2, 3], [4, 5, 6, ], [7, 8, 9]]

list4 = copy.deepcopy(list_)
print(list_ is list4)
# False

list_[0][0] = 400
print(list4)
# [[300, 2, 3], [4, 5, 6, ], [7, 8, 9]]

