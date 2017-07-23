class Animal:
    def eat(self):
        print("chichichi")
    def drink(self):
        print("hehehe")
    def sleep(self):
        print("shuishuishui")
    def run(self):
        print("paopaopao")


class Dog(Animal):
    """
    def eat(self):
        print("chichichi")
    def drink(self):
        print("hehehe")
    def sleep(self):
        print("shuishuishui")
    def run(self):
        print("paopaopao")
    """
    def bark(self):
        print("jiaojiaojiao")

class Cat(Animal):
    def catch(self):
        print("抓老鼠")
wangcai = Dog()
#wangcai.eat()
#mao = Cat()
#mao.catch()
#mao.run()
class xiaotianquan(Dog):
    def bark(self):
        print("狂叫")
xiaotian = xiaotianquan()
xiaotian.bark()
xiaotian.eat()
