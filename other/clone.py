import copy

list1 = [[1, 2, 3], [4, 5, 6, ], [7, 8, 9]]

list2 = list1
print(list1 is list2)
# True

list1[0][0] = 1000
print(list2)
# [[1000, 2, 3], [4, 5, 6, ], [7, 8, 9]]

list3 = list(list1)
print(list1 is list3)
# False

# but:
list1[0][0] = 2000
print(list3)
# [[2000, 2, 3], [4, 5, 6, ], [7, 8, 9]]


list4 = copy.copy(list1)
print(list1 is list3)
# False

# but:
list1[0][0] = 300
print(list4)
# [[300, 2, 3], [4, 5, 6, ], [7, 8, 9]]

list4 = copy.deepcopy(list1)
print(list1 is list4)
# False

list1[0][0] = 400
print(list4)
# [[300, 2, 3], [4, 5, 6, ], [7, 8, 9]]

