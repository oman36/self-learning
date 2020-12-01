x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

data = None
# next 2 lines are equal
data = {} if data is None else data
data = data is None and {} or data
