#Create a class Car with:
#instance attribute mileage
#class attribute wheels = 4,Add an instance method display_specs() that prints mileage and wheels.
#Then change wheels using a class method, and print again.
class car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    def display_space(self):
        print("mileage:",self.mileage)
        print("wheels:",car.wheels)
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.wheels=new_wheels
c1=car(20)
c1.display_space()
car.change_wheels(9)
c1.display_space()