# Sets do not save ordering
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
# {'orange', 'banana', 'pear', 'apple'}

print('orange' in basket)
# True

print('crabgrass' in basket)
# False

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)
# {'a', 'r', 'b', 'c', 'd'}

# letters in a and not in b
print(a - b)
# {'r', 'd', 'b'}

# letters in a or b or both:
print(a | b)
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

# letters in both a and b
print(a & b)
# {'a', 'c'}

# letters in a or b but not both:
print(a ^ b)
# {'r', 'd', 'b', 'm', 'z', 'l'}

# Similarly to list comprehensions, set comprehensions are also supported:
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
# {'r', 'd'}
