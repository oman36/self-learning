# see https://www.python.org/dev/peps/pep-0318/


# decorator should to return decorated function instead of result
def decorator(func):

    def wrapper(*args, **kwargs):

        print('Start')

        result = func(*args, **kwargs)

        print('Finish')

        return result

    return wrapper


# If you use universal decorator, you should to use complex decorator
def decorator_with_args(start_word='Begin', finish_word='End'):

    def arg_wrapper(func):

        def wrapper(*args, **kwargs):

            print(start_word)

            result = func(*args, **kwargs)

            print(finish_word)

            return result

        return wrapper

    return arg_wrapper


def div(arg1, arg2):
    print('Executed')
    return arg1 / arg2


div = decorator(div)


@decorator
def div2(arg1, arg2):
    print('Executed')
    return arg1 / arg2


def div3(arg1, arg2):
    print('Executed')
    return arg1 / arg2


div3 = decorator_with_args('Start', 'Finish')(div3)


@decorator_with_args(start_word='Start', finish_word='Finish')
def div4(arg1, arg2):
    print('Executed')
    return arg1 / arg2


print(div(4, 2))
# Start
# Executed
# Finish
# 2.0


print(div2(4, 2))
# Start
# Executed
# Finish
# 2.0

print(div3(4, 2))
# Start
# Executed
# Finish
# 2.0

print(div4(4, 2))
# Start
# Executed
# Finish
# 2.0


def decorators_nesting(func):
    def wrapper(*args, **kwargs):
        print('Wrapping start')
        result = func(*args, **kwargs)
        print('Wrapping finish')
        return result
    return wrapper


@decorators_nesting
@decorator
def some_func(string):
    print('Executed')
    return 'STR: ' + string


print(some_func('Hello world'))
# Wrapping start
# Start
# Executed
# Finish
# Wrapping finish
# STR: Hello world


def asserts(*arg_types, **kwarg_types):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            for n, arg in enumerate(args):
                if n >= len(arg_types):
                    break
                if not isinstance(arg, arg_types[n]):
                    raise ValueError('Argument #{} should be {}, but {} given'.format(n, arg_types[n], type(arg)))

            for n, arg in kwargs.items():
                if n not in kwarg_types:
                    continue
                if not isinstance(arg, kwarg_types[n]):
                    raise ValueError('Named argument "{}" should be {}, but {} given'.format(n, kwarg_types[n], type(arg)))

            return func(*args, **kwargs)
        return wrapped
    return wrapper


def returns(*returns_types):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            if len(returns_types) > 1:
                if not isinstance(result, tuple):
                    raise ValueError('Function should to returns tuple of values, but one value was returned')
                if len(returns_types) != len(result):
                    raise ValueError('Function should to returns {} values, but returns {}'.format(
                        len(returns_types), len(result))
                    )

                for n, value in enumerate(result):
                    if not isinstance(value, returns_types[n]):
                        raise ValueError('Value #{} should be {}, but {} returned'.format(n, returns_types[n], type(value)))
            else:
                if not isinstance(result, returns_types[0]):
                    raise ValueError(
                        'Value should be {}, but {} returned'.format(returns_types, type(result)))

            return result
        return wrapped
    return wrapper


@asserts(int, (float, int), string=str)
@returns(str, bool)
def other_func(val1, val2, string=None):
    return '%s %s %s' % (val1, val2, string), True


other_func(1, 1, 'hello')
