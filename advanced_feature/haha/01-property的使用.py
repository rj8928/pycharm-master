class Num(object):
    def __init__(self):
        self.__num= 100
    
    def setNum(self,new_num):
        print("set")
        self.__num = new_num

    def getNum(self):
        print("get")
        return self.__num
    num = property(getNum,setNum)

t = Num()
t.num =200
print(t.num)

