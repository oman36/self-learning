def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == "__main__":
    # this condition will be execute if this file (fibo.py) will be called directly, not by import
    import sys
    if len(sys.argv) == 1:
        print('Error: need count of values as second argument')
    else:
        fib(int(sys.argv[1]))
