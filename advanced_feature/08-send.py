def test():
    print("start")
    for i in range(5):
        print("1")
        temp = yield i
        print(temp)
        print("2")
t = test()
print(next(t))
t.__next__()
t.__next__()

