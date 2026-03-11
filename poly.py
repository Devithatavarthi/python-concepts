#Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that override it.
#Demonstrate polymorphism by iterating over a list of different animal objects and calling make_sound()
from abc import abstractmethod
class Animal:
    def make_sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def make_sound(self):
        print("dog barks")
class Cat(Animal):
    def make_sound(self):
        print("cat meow")
class Cow(Animal):
    def make_sound(self):
        print("cow ambha")
Animal=[Dog(),Cat(),Cow(),Cat()]
for animal in Animal:
    animal.make_sound()
#Write a function operate(device) that calls device.start(). Pass in objects of Car, Computer, and WashingMachine — all of
# which define a start() method, but share no inheritance relationship.
#Show that Python’s polymorphism works through behavior, not type.
class Car:
    def start(self):
        print("car")
class Computer:
    def start(self):
        print("computer")
class WashingMachine:
    def start(self):
        print("Washing Machine")
def operate(device):
    device.start()
c=Car()
c1=Computer()
c2=WashingMachine()
operate(Car())
operate(c1)
operate(c2)

#Create a Vector class that supports:
#• + operator → add coordinates
#• == operator → compare equality
#Show how operator overloading gives natural polymorphism to user-defined classes.
class Vector:
    def operator(self, op, *a):
        if op =="+":
            sum=0
            for b in a:
                sum+=b
            print(sum)
        elif op == "==":
            if a[0]>a[1]:
                print(a[0],"is big")
            else:
                print(a[1],"is big")
v=Vector()
v.operator("+",3,9,8)
v.operator("==",8,3)
#sol2
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def show(self):
        print(self.x,self.y)

v1 = Vector(2,3)
v2 = Vector(4,5)

v3 = v1 + v2
v3.show()

print(v1 == v2)

#Create a base class Transport with move() and derived classes Bus and Bike that
#override it but also call the parent implementation using super().
#Show the combination of reuse + custom behavior.
class Transport:
    def move(self):

        print("Transport is moving")

class Bus(Transport):
    def move(self):
        super().move()
        print("Bus has 6 Wheels")
class Bike(Transport):
    def move(self):
        super().move()
        print("Bike has 2 Wheels")
b=Bike()
b1=Bus()
b.move()
b1.move()

#Using the abc module, create an abstract class Notification with send().
#Implement subclasses EmailNotification, SMSNotification, PushNotification — each with its own send() logic.
#Demonstrate polymorphism by looping over all and calling send().
from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Email sent")

class SMSNotification(Notification):
    def send(self):
        print("SMS sent")

class PushNotification(Notification):
    def send(self):
        print("Push notification sent")

notifications = [EmailNotification(),SMSNotification(),PushNotification()]

for n in notifications:
    n.send()

#Design:  Base class Payment with process(amount)
#Subclass CreditCardPayment adds process(amount, card_type)
#Demonstrate what happens when overriding with different signatures and how Python handles it.
class Payment:
    def process(self,amount):
        print(f"processed amount {amount}")
class CreditCardPayment(Payment):
    def process(self,amount,card_type=None):
        super().process(amount)
        print(f"{amount},{card_type}")
#p=Payment()
c=CreditCardPayment()
#p.process(1000)
c.process(2000,"visa")

#Create: Class Sorter with change(strategy) method. Separate strategy classes: BS, MS, QS, each implementing
# a different logic method. Demonstrate how polymorphism can be achieved without inheritance by using
#interchangeable strategy objects.
class BS:
    def logic(self, data):
        print("Bubble Sort")
class MS:
    def logic(self, data):
        print("Merge Sort")
class QS:
    def logic(self, data):
        print("Quick Sort")
class Sorter:
    def change(self, strategy):
        self.strategy = strategy
    def sort(self, data):
        self.strategy.logic(data)
s = Sorter()
s.change(BS())
#s.sort([5, 2, 1])
s.change(QS())
s.sort([5, 2, 1])


#Create:  Base Account → withdraw()  Subclass SavingsAccount → modifies withdraw()
#Subclass PremiumSavingsAccount → overrides again but calls parent using super()
#Show how polymorphism works across multiple levels.
class Account():
    def withdraw(self,amount):
        print("original amount",amount)
class SavingsAccount(Account):
    def withdraw(self,amount):
        super().withdraw(amount)
        print("Savings amount",amount)
class PremiumSavingsAccount(SavingsAccount):
    def withdraw(self,amount):
        super().withdraw(amount)
a=PremiumSavingsAccount()
a.withdraw(1000)

#Q9. Create a function draw(shape) that works for objects of classes Circle, Square, and Rectangle, each implementing
# a draw() method. Add another unrelated class Car with draw() and pass it — what happens and why?
class Circle:
    def draw(self):
        print("circle")
class Square:
    def draw(self):
        print("square")
class Rectangle:
    def draw(self):
        print("rectangle")
class Car:
    def draw(self):
        print("car")
def draw(shape):
    shape.draw()
c=Circle()
s=Square()
r=Rectangle()
c1=Car()
c.draw()
s.draw()
r.draw()
c1.draw()
#Q10. Design a polymorphic system for payment handling (UPI, Card, Cash) — all have a pay() method.
#Now implement a version that checks types explicitly using isinstance() before calling pay().
#Compare both designs and explain why one breaks the spirit of polymorphism

class UPI:
    def pay(self):
        print("Paid using UPI")
class Card:
    def pay(self):
        print("Paid using Card")
class Cash:
    def pay(self):
        print("Paid using Cash")
payments = [UPI(),Card(),Cash()]
for p in payments:
    p.pay()