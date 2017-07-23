def test(number):
    print("1")
    def test_in(number1):
        print("2")
        print(number+number1)
    print("3")
    return test_in
ret = test(100)
ret(1)
ret(100)
ret(200)
