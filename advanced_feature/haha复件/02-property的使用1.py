class Num(object):
    def __init__(self):
        self.__num= 100
    @property     
    def Num_f(self):
        print("get")
        return self.__num
    @Num_f.setter
    def Num_f(self,new_num):
        print("set")
        self.__num = new_num


t = Num()
t.Num_f=200
print(t.num)

