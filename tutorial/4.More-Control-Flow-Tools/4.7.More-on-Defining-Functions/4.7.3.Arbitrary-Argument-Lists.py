# Normally, these variadic arguments will be last in the list of formal parameters,
# because they scoop up all remaining input arguments that are passed to the function.
# Any formal parameters which occur after the *args parameter
# are ‘keyword-only’ arguments, meaning that they can only be used as keywords
# rather than positional arguments:
def concat(*arguments, sep="/"):
    return sep.join(arguments)


concat("earth", "mars", "venus")
# 'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
# 'earth.mars.venus'
