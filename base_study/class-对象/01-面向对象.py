class Cat:
    #属性
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age
    #方法
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def introduce(self):
        print("%s的年龄是%d"%(self.name,self.age))
        
#创建一个对象
tom = Cat("汤姆",40)
tom.eat()
tom.drink()
#给tom添加属性
#tom.name = "汤姆"
#tom.age = 40
#print("%s的年龄是%d"%(tom.name,tom.age))
tom.introduce()
lanmao = Cat("蓝猫",10)
#lanmao.name = "蓝猫"
#lanmao.age = 10
lanmao.eat()
lanmao.drink()
lanmao.introduce()
