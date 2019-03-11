with open('some_file.txt', 'w') as f:
    f.write('Hello world')

# previous 2 code lines are same as next:
f = open('some_file.txt', 'w')
try:
    f.write('Hello world')
except:
    pass
finally:
    f.close()

# correctly first to lines is same as:
f = open('some_file.txt', 'w')
f.__enter__()
try:
    f.write('Hello world')
except BaseException as e:
    f.__exit__(type(e), e, e.__traceback__)
    raise e
else:
    f.__exit__(None, None, None)


# First way to create context manager
class MyContextManager:
    def __init__(self, path, mode, *args, **kwargs):
        self.file = open(path, mode, *args, **kwargs)

    def __enter__(self):
        print('return object')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('close')
        if self.file:
            self.file.close()


# Second way to create context manager
import contextlib


@contextlib.contextmanager
def enter_plus_exit(path, mode, *args, **kwargs):
    f = open(path, mode, *args, **kwargs)
    try:
        print('yield')
        yield f
    finally:
        print('close')
        f.close()


with MyContextManager('some_file.txt', 'w') as f:
    f.write('Hello world')
    print('end of first block')
# return object
# end of first block
# close

with enter_plus_exit('some_file.txt', 'w') as f:
    f.write('Hello world')
    print('end of second block')
# yield
# end of second block
# close


try:
    with enter_plus_exit('some_file.txt', 'w') as f:
        f.write('Hello world')
        print(5 / 0)  # Exception
        print('end of second block')
except ZeroDivisionError as e:
    print(e.__str__())
# yield
# close
# division by zero


