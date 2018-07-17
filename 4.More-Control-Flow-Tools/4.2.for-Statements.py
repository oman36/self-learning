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