for i in range(5):
    print(i, end=' ')
# 0 1 2 3 4

# !!! important !!! A strange thing happens if you just print a range:
print(range(10))
# range(0, 10)

# Enumerate for key - value:
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# 0 tic
# 1 tac
# 2 toe
