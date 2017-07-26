# coding=utf-8
def aa():
    print("start")
    for i in range(1,5):
        temp = yield i
        print(temp)

t =aa()

t.__next__()
t.send("xixi")
t.__next__()
