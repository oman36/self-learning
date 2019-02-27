# lambda:
def make_incrementor(n):
    return lambda x: x + n


inc = make_incrementor(5)
print(inc(2))
# 7
