# When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the
# items() method:
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# gallahad the pure
# robin the brave

# Enumerate for key - value:
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# 0 tic
# 1 tac
# 2 toe

# To loop over two or more sequences at the same time,
#  the entries can be paired with the zip() function:
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.

# To loop over a sequence in reverse, first specify the sequence in a forward direction
# and then call the reversed() function.

# To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving
# the source unaltered.
