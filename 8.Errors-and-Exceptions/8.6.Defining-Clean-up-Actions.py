def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(2, 1)
# result is 2.0
# executing finally clause

divide(2, 0)
# division by zero!
# executing finally clause

divide("2", "1")
# executing finally clause
# Traceback (most recent call last):
#   File "8.Errors-and-Exceptions/8.6.Defining-Clean-up-Actions.py", line 18, in <module>
#     divide("2", "1")
#   File "8.Errors-and-Exceptions/8.6.Defining-Clean-up-Actions.py", line 3, in divide
#     result = x / y
# TypeError: unsupported operand type(s) for /: 'str' and 'str'

# In real world applications, the finally clause is useful for releasing external resources (such as files or network
# connections), regardless of whether the use of the resource was successful.
