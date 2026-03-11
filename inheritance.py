#Create a base class Animal with a method sound(). Create a derived class Dog that overrides the sound() method.
# Demonstrate method overriding.
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("dog barks")
obj1=Dog()
obj1.sound()

#Create class A with method show(). Create class B(A) that overrides show() and
#also calls the parent method using super()
class A:
    def show(self):
        print("this is class A")
class B(A):
    def show(self):
        super().show()
        print("this is class B")

o=B()
o.show()


# Create multi-level inheritance with classes A → B → C, each having a method display() printing the class name.
# Create object of C and call display(), showing method resolution.
class A:
    def display(self):
        print("class A")
class B(A):
    def display(self):
        super().display()
        print("class B")

class C(B):
    def display(self):
        super().display()
        print("class C")

obj=C()
obj.display()
print(C.__mro__)
# Implement hierarchical inheritance using a base class Vehicle and two child
#classes Car and Bike, each defining a method wheels().
class Vehicle:
    def __init__(self,name,man_year):
        self.name=name
        self.man_year=man_year
class Car(Vehicle):
    def wheels(self):
        print("4 wheels")
class Bike(Vehicle):
    def wheels(self):
        print("2 wheels")
v1=Bike("splender",2020)
v2=Car("swift",2025)
v1.wheels()
v2.wheels()
print(Bike.mro())
# Create class Employee with an instance method salary(). Create class Manager(Employee) that overrides salary()
# and adds an incentive. Demonstrate both outputs.
class Employee:
    base_salary=15000
    def salary(self):
        print(Employee.base_salary)
class Manager(Employee):
    def salary(self,i):
        super().salary()
        self.incentive=i
        print(Employee.base_salary+self.incentive)
#e=Employee()
m=Manager()
#e.salary()
m.salary(5000)
#Create class University with a class variable and a class method.
# Inherit it into class College and access the parent’s class variable from the child class
class University:
    uni_name="IIIT"
    @classmethod
    def show_name(cls,new_name):
        cls.uni_name=new_name
        return University.uni_name
class College(University):
    pass
print(College.uni_name)
print(University.show_name("Cvcorp"))

#Create class MathOps with a static method add(a, b). Create class AdvancedOps(MathOps)
# use the static method without overriding it
class MathOps:
    @staticmethod
    def add(a,b):
        return a+b
class AdvancedOps(MathOps):
    pass
obj=AdvancedOps()
print(obj.add(3,2))
print(AdvancedOps.add(5,4))
print(MathOps.add(4,6))
#Create two classes Father and Mother, both defining a method skills(). Create
#class Child(Father, Mother) and check which skills() runs using MRO
class Father:
    def skills(self):
        print("farming and business")
        super().skills()
class Mother:
    def skills(self):
        print("housewife ")
        #super().skills()
class Child(Father,Mother):
    pass
c=Child()
c.skills()
print(Child.mro())

#Create an abstract class Shape with an abstract method area(). Create class Rectangle(Shape) that implements the area() method.
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        print( self.length*self.breadth)
r=Rectangle(5,8)
r.area()
# Create class Person with a constructor __init__(name). Create class Student(Person) with
# constructor __init__(name, roll). Use super() to call the parent constructor
class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll_number=roll
s=Student("Sathwika",35)
print(s.name,s.roll_number)