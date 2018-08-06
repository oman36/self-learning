# Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined
#  by subclasses), there is limited support for such a mechanism, called name mangling. Any identifier of the form
# `__spam` (at least two leading underscores, at most one trailing underscore) is textually replaced with
# `_classname__spam`, where classname is the current class name with leading underscore(s) stripped. This mangling is
# done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a
# class.

class MappingName:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update


print('__update' in dir(MappingName))
# False

print('_MappingName__update' in dir(MappingName))
# True

print(MappingName.__dict__)
# True
