class Car:
    @staticmethod
    def Start():
        print("CAR STARTS")
    
    @staticmethod
    def Stop():
        print("Car Stops")
class Toyota_Car(Car):
    def __init__(self,name):
        self.name= name

car1=Toyota_Car("TOYOTA")
print(car1.name)
print(car1.Start())