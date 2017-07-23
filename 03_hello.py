# coding:utf-8
class Foo(object):
    def __init__(self):
        pass
    def __getattr__(self, item):
        print(item)
        return self
    def __str__(self):
        return ""

# obj  = Foo()

print(Foo().think.different.itcast)
