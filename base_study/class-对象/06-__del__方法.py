class Dog:
    def __del__(self):
        print("我死了")

dog1 = Dog()
dog2 = dog1
#del dog1 #内存
