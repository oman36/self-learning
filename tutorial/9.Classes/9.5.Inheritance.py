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

# You can check if object is instance of any type from tuple
print(isinstance(obj, (BaseClass, float, int)))
# True

print(isinstance(obj, (float, int)))
# False

print(issubclass(SubClass, BaseClass))
# True

# You can check if object is subclass of any class from tuple
print(issubclass(SubClass, (BaseClass, float)))
# True

print(issubclass(SubClass, SomeClass))
# False

print(issubclass(BaseClass, SubClass))
# False


# For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class
# as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy.
# Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base
#  classes of Base1, and if it was not found there, it was searched for in Base2, and so on.
# @see https://rhettinger.wordpress.com/2011/05/26/super-considered-super/

class Parent:
    def method(self):
        print('Parent')


class Child(Parent):
    def method(self):
        print('Child')
        super().method()


class OtherClass:
    def method(self):
        print('OtherClass')


class Result1(Child, OtherClass):
    def method(self):
        super().method()


print(*Result1.__mro__, sep='\n')
# <class '__main__.Result1'>
# <class '__main__.Child'>
# <class '__main__.Parent'>
# <class '__main__.OtherClass'>
# <class 'object'>

Result1().method()
# Child
# Parent


class Parent2:
    def method(self):
        print('Parent2')


class Child2(Parent2):
    def method(self):
        print('Child2')
        super().method()


class OtherChild(Parent2):
    def method(self):
        print('OtherChild')


class Result2(Child2, OtherChild):
    def method(self):
        super().method()


print(*Result2.__mro__, sep='\n')
# <class '__main__.Result2'>
# <class '__main__.Child2'>
# <class '__main__.OtherChild'>
# <class '__main__.Parent2'>
# <class 'object'>


Result2().method()
# Child2
# OtherChild

# Inheritance test
position = Result2.__mro__.index
assert position(Child2) < position(OtherChild)
assert position(OtherChild) < position(Parent2)
