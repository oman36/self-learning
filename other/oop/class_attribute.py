class ClassAttr:
    def __get__(self, instance, owner):
        print(f'__get__(self={self}, instance={instance}, owner={owner})')
        return f'{self} Value'

    def __set_name__(self, owner, name):
        print(f'__set_name__(self={self}, owner={owner}, name={name})')

    def __set__(self, instance, value):
        print(f'__set__(self={self}, instance={instance}, value={value})')

    def __delete__(self, instance):
        print(f'__delete__(self={self}, instance={instance})')


class Klass:
    class_attr = ClassAttr()

    def __init__(self):
        self.obj_attr = ClassAttr()
# __set_name__(self=<__main__.ClassAttr object at 0x1>, owner=<class '__main__.Klass'>, name=class_attr)


obj = Klass()

var = obj.obj_attr
print(var)
# <__main__.ClassAttr object at 0x0>
var = obj.class_attr
# __get__(self=<__main__.ClassAttr object at 0x1>, instance=<__main__.Klass object at 0x2>, owner=<class '__main__.Klass'>)

print(var)
# <__main__.ClassAttr object at 0x1> Value

hasattr(obj, 'obj_attr')
hasattr(obj, 'class_attr')
# __get__(self=<__main__.ClassAttr object at 0x1>, instance=<__main__.Klass object at 0x2>, owner=<class '__main__.Klass'>)

obj.obj_attr = 1
obj.class_attr = 3
# __set__(self=<__main__.ClassAttr object at 0x1>, instance=<__main__.Klass object at 0x2>, value=3)

del obj.obj_attr
del obj.class_attr
# __delete__(self=<__main__.ClassAttr object at 0x1>, instance=<__main__.Klass object at 0x2>)

try:
    del obj.obj_attr
except AttributeError as e:
    print(repr(e))
# AttributeError('obj_attr')

del obj.class_attr
# __delete__(self=<__main__.ClassAttr object at 0x1>, instance=<__main__.Klass object at 0x2>)


class NoGetClassAttr:
    def __set_name__(self, owner, name):
        print(f'__set_name__(self={self}, owner={owner}, name={name})')

    def __set__(self, instance, value):
        print(f'__set__(self={self}, instance={instance}, value={value})')

    def __delete__(self, instance):
        print(f'__delete__(self={self}, instance={instance})')


class NoNameClassAttr:
    def __get__(self, instance, owner):
        print(f'__get__(self={self}, instance={instance}, owner={owner})')
        return f'{self} Value'

    def __set__(self, instance, value):
        print(f'__set__(self={self}, instance={instance}, value={value})')

    def __delete__(self, instance):
        print(f'__delete__(self={self}, instance={instance})')


class NoDelClassAttr:
    def __set_name__(self, owner, name):
        print(f'__set_name__(self={self}, owner={owner}, name={name})')

    def __get__(self, instance, owner):
        print(f'__get__(self={self}, instance={instance}, owner={owner})')
        return f'{self} Value'

    def __set__(self, instance, value):
        print(f'__set__(self={self}, instance={instance}, value={value})')


class NoSetClassAttr:
    def __set_name__(self, owner, name):
        print(f'__set_name__(self={self}, owner={owner}, name={name})')

    def __get__(self, instance, owner):
        print(f'__get__(self={self}, instance={instance}, owner={owner})')
        return f'{self} Value'

    def __delete__(self, instance):
        print(f'__delete__(self={self}, instance={instance})')


class Klass2:
    no_name_class_attr = NoNameClassAttr()
    no_get_class_attr = NoGetClassAttr()
    no_set_class_attr = NoSetClassAttr()
    no_del_class_attr = NoDelClassAttr()
# __set_name__(self=<__main__.NoGetClassAttr object at 0x4>, owner=<class '__main__.Klass2'>, name=no_get_class_attr)
# __set_name__(self=<__main__.NoSetClassAttr object at 0x5>, owner=<class '__main__.Klass2'>, name=no_set_class_attr)
# __set_name__(self=<__main__.NoDelClassAttr object at 0x6>, owner=<class '__main__.Klass2'>, name=no_del_class_attr)


obj2 = Klass2()

var = obj2.no_get_class_attr
print(var)
# <__main__.NoGetClassAttr object at 0x4>


print(hasattr(obj2, 'no_get_class_attr'))
# True

obj2.no_get_class_attr = 11
# __set__(self=<__main__.NoGetClassAttr object at 0x4>, instance=<__main__.Klass2 object at 0x7>, value=11)
print(obj2.no_get_class_attr)
# <__main__.NoGetClassAttr object at 0x4>

try:
    obj2.no_set_class_attr = 12
except AttributeError as e:
    print(repr(e))
# AttributeError('__set__')

try:
    del obj2.no_del_class_attr
except AttributeError as e:
    print(repr(e))
# AttributeError('__delete__')
