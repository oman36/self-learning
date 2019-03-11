# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
# cat 3
# window 6
# defenestrate 12

# Loop over a slice copy of the entire list:
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words)
# ['defenestrate', 'cat', 'window', 'defenestrate']

# Enumerate for index - value:
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# 0 tic
# 1 tac
# 2 toe

for i in ['val1', 'val2', 'val3']:
    print(i)
    if i == 'val4':
        break
else:
    print('this message was show, because "break" was not happened')
# val1
# val2
# val3
# this message was show, because "break" was not called

for i in ['val1', 'val2', 'val3']:
    print(i)
    if i == 'val2':
        break
else:
    print('this message will not shown, because "break" was happened')
# val1
# val2
