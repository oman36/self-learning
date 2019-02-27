for i in range(5):
    print(i, end=' ')
# 0 1 2 3 4

# !!! important !!! A strange thing happens if you just print a range:
print(range(10))
# range(0, 10)

# using it as list use `list`:
print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
