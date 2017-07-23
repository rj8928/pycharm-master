def func(functionName):
    print("--1--")
    def func_in():
        print("--in1--")
        functionName()
        print("in2")

    print("--2--")
    return func_in
def test():
    print("test")

test = func(test)
test()
