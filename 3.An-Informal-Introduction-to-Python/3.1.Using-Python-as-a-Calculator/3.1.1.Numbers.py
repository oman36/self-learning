print(2 + 2)
# 4
print(50 - 5 * 6)
# 20
print(8 / 5)  # divisions always returns `float`
# 1.6
print(17 / 3)  # 3 * 5 + 2 = 17; 2/3 = 0.6666..67
# 5.66666..67
print(17 // 3)  # floor division discards the factorial part
# 5
print((17 // 3).__class__)  # floor division discards the factorial part
# <class 'int'>
print(17 % 3)  # 3 * 5 + 2 = 17
print((17 // 3).__class__)  # floor division discards the factorial part
# <class 'int'>
# 2
print(2 ** 7)  # 2 to the power of 7
# 128

# !!! In interactive mode, the last printed expression is assigned to variable `_` (lowerdash)
# >>> tax = 12.5 / 100
# >>> price = 100.50
# >>> price * tax
# 12.5625
# >>> price + _
# 113.0625
# >>> round(_, 2)
# 113.06
