class Car:
    def __init__(self,type):
        self.type =type

    @staticmethod
    def Start():
        print("CAR STARTS")
    
    @staticmethod
    def Stop():
        print("Car Stops")
class Toyota_Car(Car):
    def __init__(self,name,type):
        self.name= name
        super().__init__(type)

car1=Toyota_Car("TOYOTA","Electrtic")
print(car1.type)