class CarStore(object):
    def order(self,money,car_type):
            return car


class Car(object):
    def move(self):
    print("..车动..")
    def music(self):
    print("..音乐..")
    def stop(self):
    print("..车停..")

class benchi(Car):
    pass
class baoma(Car):
    pass

car_store = CarStore()
car = car_store.order(500000)
car.move()
car.music()
car.stop()
