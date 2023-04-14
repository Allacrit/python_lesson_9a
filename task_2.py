"""
Реализовать метакласс. позволяющий создавать всегда один и тот же объект класса.
"""


class DocMeta(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__()
        return self.__instance
class MyClass(metaclass=DocMeta):
    pass

obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()
print(obj_1 is obj_3)