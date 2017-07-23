#def test1():
#    print("--1--")
#def test1():
#    print("--2--")
#
#
##test1()

def w1(func):
    def inner():
        print("验证权限")
        func()
    return inner
@w1
def f1():
    print("f1")
@w1
def f2():
    print("f2")

#innerFunc = w1(f1)
#innerFunc()
#f1 = w1(f1)
f1()
f2()

