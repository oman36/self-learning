class BaseClass:
    def say_hello(self):
        print('Hello', end=' ')

    def other_function(self):
        print('Other_', end='')


class SubClass(BaseClass):
    def say_hello(self):
        super().say_hello()
        print('world')

    def other_function(self):
        BaseClass.other_function(self)
        print('other_function')


class SomeClass:
    def say_hello(self):
        print('Hello', end=' ')

    def other_function(self):
        print('Other_', end='')


obj = SubClass()

obj.say_hello()
# Hello world

obj.other_function()
# Other_other_function

print(isinstance(obj, SubClass))
# True

print(isinstance(obj, BaseClass))
# True

print(issubclass(SubClass, BaseClass))
# True

print(issubclass(SubClass, BaseClass))
# True

print(issubclass(SubClass, SomeClass))
# False

print(issubclass(BaseClass, SubClass))


# False


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiInheritance(Base1, Base2, Base3):
    pass
# For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class
# as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy.
# Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base
#  classes of Base1, and if it was not found there, it was searched for in Base2, and so on.
