def creatNum():
    print("---start--")
    a,b = 0,1
    for i in range(5):
        print("1")
        yield b
        a,b = b,a+b
    print("--end---")

a =creatNum()
a.__next__()
a.__next__()
