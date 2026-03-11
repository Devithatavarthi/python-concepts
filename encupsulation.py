#Create a BankAccount class that stores: account number ,balance (should not be directly modifiable)
#You must: 1. Make the balance attribute inaccessible from outside.
#2. Provide functions to deposit/withdraw that validate the amount.
#3. Prevent withdrawal if balance becomes negative.
#4. Show what happens if someone tries to modify balance directly and why encapsulation prevents it.
class BankAccount():
    def __init__(self,acc,init_balance=0):
        self.acc_number=acc
        self.__balance=init_balance
    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount<=0:
            print("Invalid Amount")
            return
        self.__balance+=amount
        print(self.__balance)
    def withdraw(self,amount):
        if amount<=0:
            print("Invalid Withdrawl")
            return
        elif amount > self.__balance:
            print("Insufficient balance")
            return
        self.__balance -= amount
        print(self.__balance)
a=BankAccount(123456,1000)
a.deposit(1000)
a.withdraw(200)
a.__balance=10000
print(a.get_balance())

# Design a Student class where marks:  should always be between 0 and 100 should never be set directly
#Enable updating marks only through a controlled method that performs range checks.
#Demonstrate: trying to assign marks manually why encapsulation protects invalid states
class Student:
    def __init__(self,name):
        self.name=name
        self.__marks=20
    def get_marks(self):
        return self.__marks
    def set_marks(self,new_marks):
        if 0<=new_marks<=100:
            self.__marks=new_marks
            print(new_marks)
        else:
            print("Invalid marks")
s=Student("vikky")
print(s.get_marks())
print(s.set_marks(50))

#Create a SecureFile class that: stores content privately  provides a method read(password)
#refuses access if the password is incorrect logs an "Unauthorized attempt" internally (cannot be accessed from outside)
class SecureFile:
    def __init__(self,content,password):
        self.__content=content
        self.__password=password
        self.__log=[]
    def read(self,password):
        if password==self.__password:
            return self.__content
        else:
            self.__log.append("Unauthorized attempt")
        return "Access denied"
file=SecureFile("Secret data","12334")
print(file.read("wrong"))
print(file.read("12334"))
#Design an Employee class where: salary is hidden outsiders cannot read salary directly
#use getter method that logs each access attempt provide a method to update salary but only
# if the new salary is higher (prevent accidental downgrade)
class Employee:
    def __init__(self,salary):
        self.__salary=salary
    def get_salary(self):
        print("Salary Accessed")
        return self.__salary
    def update_salary(self,new_salary):
        if new_salary>self.__salary:
            self.__salary=new_salary
            print("salary updated")
        else:
            print("salary is not increased")
a=Employee(12000)
print(a.get_salary())
a.update_salary(20000)
print(a.get_salary())

#Create a Product class where: price cannot be negative, discount cannot exceed 70%
#internal final price calculation should not be directly exposed Provide only one public method get_final_price().
class Product:
    def __init__(self,price,discount):
        self.price=price
        self.__discount=discount
        if price<=0:
            print("Invalid Price")
        if discount>70:
            print("Discount cannot exceed")
    def get_final_price(self):
        final=self.price*(1-self.__discount/100)
        return final
p=Product(500,50)
p1=Product(0,60)
print(p.get_final_price())
print(p1.get_final_price())
#Create a Character class with: private _health methods to damage(points) and heal(points)
#health cannot drop below 0 or exceed max limit expose only current health through a read-only getter
class Character:
    def __init__(self,name,max_health):
        self.name=name
        self.__health=max_health
        self.__max_health=max_health
    def damage(self,points):
        if points>0:
            self.__health-=points
            if self.__health<0:

                print(f"{self.name},{points} damage")
    def heal(self,points):
        if points>0:
            self.__health+=points
            if self.__health>self.__max_health:
                self.__health = self.__max_health
            print(f"{self.name},{points} healed")
    def get_health(self):
        return self.__health
h=Character("sathwika",20)
h.damage(50)
print(h.get_health())
h.heal(40)
print(h.get_health())
#Create: An Engine class with private state like temperature  A Car class that uses an Engine but should:
#Not allow users to manipulate engine temperature Only expose methods like start_car() or cool_engine()
class Engine:
    def __init__(self):
        self.__temperature=30
    def heat_up(self):
         self.__temperature += 50
    def cool_down(self):
         self.__temperature -= 30
    def get_temperature(self):
       return self.__temperature
class Car:
    def __init__(self):
        self.__engine = Engine()
    def start_car(self):
         self.__engine.heat_up()
         print("Car started")
    def cool_engine(self):
         self.__engine.cool_down()
         print("Engine cooled")
    def show_temperature(self):
         print( self.__engine.get_temperature())
car = Car()
car.start_car()
car.show_temperature()
car.cool_engine()
car.show_temperature()

# 8. Create a ShoppingCart class where:
# • items are stored privately
# • users cannot directly modify item list
# • only add/remove methods are allowed
# • provide a method to get a safe copy of the cart items (not direct reference to internal list)

class ShoppingCart:
    def __init__(self):
         self.__items=[]
    def add_item(self,item):
         self.__items.append(item)
         print(item,"Added.")
    def remove_item(self,item):
         if item in self.__items:
             self.__items.remove(item)
             print(item,"Removed.")
         else:
             print(item,"Not in Cart.")
    def get_items(self):
         return self.__items.copy()
cart=ShoppingCart()
cart.add_item("Apple")
cart.add_item("Milk")
cart.add_item("Cool Drink")
cart.get_items()
cart.remove_item("Milk")
cart.remove_item("Biscuit")
print(cart.get_items())

# 9. Implement a class incorrectly first:
# • Attendance stored in a list
# • Exposed directly so any outside code can modify it
# Then redesign properly:
# • Make attendance private
# • Provide controlled methods for marking attendance only
# Explain the difference.

class BadAttendance:
 def __init__(self):
     self.attendance = []
bad = BadAttendance()
bad.attendance.append("Alice")
#bad.attendance.clear()
print(bad.attendance)

class Attendance:
 def __init__(self):
     self.__attendance=[]
 def mark_present(self,name):
     if name in self.__attendance:
         print(name,"Already Marked")
     else:
         self.__attendance.append(name)
         print(name,"Marked Present")
 def get_attendance(self):
     return self.__attendance.copy()
att = Attendance()
att.mark_present("Alice")
att.mark_present("Bob")
print(att.get_attendance())
att.mark_present("Bob")


# 10. Create a class using @property and @setter for a private attribute.
# Then:1. Show correct usage
#      2. Show how forgetting to use underscore prefix breaks encapsulation
#      3. Show what happens if you implement a setter without validation

class Student:
    def __init__(self, grade):
        self._grade = grade
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self,x):
        if 0 <= x <= 100:
            self._grade = x
        else:
            print("Invalid grade! Must be between 0 and 100.")
s = Student(85)
print(s.grade)
s.grade = 95
print(s.grade)
s.grade = 101