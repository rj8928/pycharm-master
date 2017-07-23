class Animal:
    def eat(self):
        print("chichichi")
    def drink(self):
        print("hehehe")
    def sleep(self):
        print("shuishuishui")
    def run(self):
        print("paopaopao")


class Dog:
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
    pass
class Cat(Animal):
    def catch(self):
        print("抓老鼠")
wangcai = Dog()
#wangcai.eat()
mao = Cat()
mao.catch()
mao.run()
