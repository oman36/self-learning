# If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the raise
# statement allows you to re-raise the exception:
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
